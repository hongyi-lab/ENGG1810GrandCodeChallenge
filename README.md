# ENGG1810GrandCodeChallenge
Idea: CNN-Based Seizure Detection from EEG Waveform Images

Instead of manually designing features like amplitude or line length,
we can turn each small segment of EEG data into a waveform image (time vs voltage plot).
Then, we train a small convolutional neural network (CNN) to automatically learn patterns that indicate seizures.

1. How it works:
Slice the EEG data into small windows (e.g., 2 seconds each).
Plot each window as a 2D graph (waveform) and save it as an image.
Label the images as "Seizure" or "No Seizure" based on the known classified data.

2. Train a CNN to classify the images.
After training, the CNN can look at a new EEG waveform and predict if a seizure is happening.
Why this is a good idea:
It doesn't rely on specific numbers like amplitude – it learns the shape of the signal.
It can handle noise better and might generalize better to different mice.
It's an end-to-end learning method (no need for manual feature engineering).
Although it might seem a bit like a black box, it is powerful and modern!

3. Extra:
We can use a very small CNN to make training fast and avoid overfitting.
This idea is inspired by how object detection works in computer vision (like detecting objects in photos).


We can write above to the report and the presenation 

steps by steps instructions :

1. from the csv file, plot the graph
2. save the graph to jpg
3. using labelme, mark the graph and converting it to json file
4. classify the json file and jpg ( I will show how to do this )
5. converting the json file to coco json
6. converting the coco json to txt
7. train the Yolo8n model with the txt file
8. call the model and testing the result
9. if the result is not that good, we need to get more data and train it again.
    

