import json
import os
import glob
import numpy as np
from pathlib import Path
from collections import defaultdict
from tqdm import tqdm

def make_dirs_safe(dir='new_dir/'):
    dir = Path(dir)
    for p in [dir, dir / 'labels', dir / 'images']:
        p.mkdir(parents=True, exist_ok=True)
    return dir

def coco91_to_coco80_class():
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, None, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, None, 24, 25, None,
         None, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, None, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
         51, 52, 53, 54, 55, 56, 57, 58, 59, None, 60, None, None, 61, None, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72,
         None, 73, 74, 75, 76, 77, 78, 79, None]
    return x

def convert_coco_json(cocojson_folder, savepath, use_keypoints=False, cls91to80=True):
    save_dir = make_dirs_safe(savepath)
    coco80 = coco91_to_coco80_class()

    json_files = list(Path(cocojson_folder).glob('*.json'))
    if not json_files:
        raise FileNotFoundError(f'No json files found in {cocojson_folder}')

    for json_file in sorted(json_files):
        fn = Path(save_dir) / 'labels' / json_file.stem.replace('instances_', '')
        fn.mkdir(parents=True, exist_ok=True)
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        images = {str(x['id']): x for x in data['images']}
        imgToAnns = defaultdict(list)
        for ann in data['annotations']:
            imgToAnns[str(ann['image_id'])].append(ann)

        success_count = 0

        for img_id, anns in tqdm(imgToAnns.items(), desc=f'Processing {json_file.name}'):
            img = images.get(str(img_id))
            if img is None:
                continue
            h, w = img['height'], img['width']
            f_name = Path(img['file_name']).name  # ← 修正文件名问题
            bboxes = []
            keypoints = []

            for ann in anns:
                if ann['iscrowd']:
                    continue
                box = np.array(ann['bbox'], dtype=np.float64)
                box[:2] += box[2:] / 2
                box[[0, 2]] /= w
                box[[1, 3]] /= h
                if box[2] <= 0 or box[3] <= 0:
                    continue

                cls = coco80[ann['category_id'] - 1] if cls91to80 else ann['category_id']
                box = [cls] + box.tolist()
                if box not in bboxes:
                    bboxes.append(box)
                if use_keypoints and ann.get('keypoints') is not None:
                    k = (np.array(ann['keypoints']).reshape(-1, 3) / np.array([w, h, 1])).reshape(-1).tolist()
                    k = box + k
                    keypoints.append(k)

            if bboxes:
                output_txt_path = (fn / f_name).with_suffix('.txt')
                output_txt_path.parent.mkdir(parents=True, exist_ok=True)
                with open(output_txt_path, 'a') as file:
                    for i in range(len(bboxes)):
                        line = keypoints[i] if use_keypoints else bboxes[i]
                        file.write((' '.join(['%g'] * len(line)) + '\n') % tuple(line))
                success_count += 1

        print(f'✅ Generated {success_count} .txt files in {fn}')

        # 清除空txt
        txtlist = glob.glob(str(fn / '*.txt'))
        for txt in txtlist:
            if os.path.getsize(txt) == 0:
                os.remove(txt)

if __name__ == '__main__':
    cocojson_folder = r'D:\AAAUAVTemp\dataset.json'  # <-- 修正为 COCO 格式单文件所在路径的文件夹
    savepath = r'D:\AAAUAVdata\AAAUAVdata'

    convert_coco_json(cocojson_folder,
                      savepath,
                      use_keypoints=False,
                      cls91to80=False)
