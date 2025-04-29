import pandas as pd
import matplotlib.pyplot as plt

filepath = r'D:\桌面\1A.csv' # you need to change it to your local path

df = pd.read_csv(filepath, encoding='utf-8-sig')
df.columns = df.columns.str.strip()

time = df['time'].values
data = df['Mouse1_Sample_A'].values


def plot_eeg_data(time, data, labels=None, title=None):
    plt.figure(figsize=(14, 4))
    plt.plot(time, data, linewidth=0.5, color='black', label='EEG signal')

    if labels is not None:
        is_seizing = False
        start = None
        for i in range(len(labels)):
            if labels[i] == 'Seizure' and not is_seizing:
                is_seizing = True
                start = time[i]
            elif labels[i] != 'Seizure' and is_seizing:
                is_seizing = False
                end = time[i]
                plt.axvspan(start, end, color='red', alpha=0.3)

        if is_seizing:
            plt.axvspan(start, time[-1], color='red', alpha=0.3)

    plt.title(title or "Mouse EEG Recording")
    plt.xlabel("Time (s)")
    plt.ylabel("Voltage (µV)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
plot_eeg_data(time, data, title="Mouse1_Sample_A EEG with Seizure Label")

#above is the way for loading the data


