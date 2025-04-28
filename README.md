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



If you feel it is difficult for doing above, so could you please just plot the graph from excel and then I can lable it and do the rest ? Besides this, we can coupld the above complex method with the Fortier transform method. You can write code and do this method. And Please come up with ideas about the presentation and the poster ! And the presentation might need everyone to engage.


There is a simple glance about the Fortier Transform method: ( just like an extension version of the project one, if you fininshed the project one, you can do it !)


The Fourier Transform is a mathematical tool that transforms a signal from the time domain (how a signal changes over time) into the frequency domain (how much different frequencies exist in the signal). It shows us which frequencies are present and how strong they are.

In the case of EEG signals:
Normal brain activity shows a balanced spread across frequencies.
Seizure activity often shows a sudden increase in low-frequency energy (for example, 0–10 Hz).
By applying the Fourier Transform to EEG data, we can:

1. Identify changes in frequency energy.

2. Detect seizures by checking if low-frequency energy rises above a chosen threshold.

This method is simple, explainable to medical professionals, and effective for detecting seizures in real-world data.
We use Python's numpy library (np.fft.fft) to perform the Fourier Transform and calculate energy in specific frequency bands. (You even do not need to know what is Fortier Transform, and what is the main principle of that, the only thing you need to do is applying the numpy !!! )  ( you can search online, ask chatgpt, about how to use it )



