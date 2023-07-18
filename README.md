# Action Recognition and chatbot
```
Human Action Recognition (HAR) aims to understand human behavior and assign a label to each action. It has a wide range of applications, and therefore has been attracting increasing attention in the field of computer vision. Human actions can be represented using various data modalities, such as RGB, skeleton, depth, infrared, point cloud, event stream, audio, acceleration, radar, and WiFi signal, which encode different sources of useful yet distinct information and have various advantages depending on the application scenarios.

```

Consequently, lots of existing works have attempted to investigate different types of approaches for HAR using various modalities.

 

> Our Task is to build an Image Classification Model using CNN that classifies to which class of activity a human is performing. We also built a chatbot which can answers queries about videos. 

# HAR-using-keras
This repository contains all the code and data used in the project. It includes the dataset from kaggle (https://www.kaggle.com/datasets/shashankrapolu/human-action-recognition-dataset)  completed Jupyter notebook for training, the Flask app to serve predictions, and other utility scripts. Please feel free to modify any and all aspects of the code to suit your needs.

Once you have cloned repository, make sure to install dependencies using pipenv with the provided Pipfile and execute all commands using pipenv. Also, please make sure to add the correct path to the video file in camera.py on line 11. Next, to install pipenv, the dependencies, and run the main.py file, execute the following commands from your terminal or command prompt, making sure to add the right paths where necessary:

$ cd \path\to\Project\

$ pip install pipenv

$ pipenv install

$ python main.py/flask_main.py 

or

$ pipenv run python3 main.py/flask_main.py


make sure to instal flask,opencv,tensorflow as major dependencies.

# Dataset 
* ### Link to dataset - https://dphi-live.s3.eu-west-1.amazonaws.com/dataset/Human+Action+Recognition-20220526T101201Z-001.zip



>The dataset features 15 different classes of Human Activities. The dataset contains about 12k+ labelled images including the validation images. Each image has only one human activity category and are saved in separate folders of the labelled classes
 

 

From the above link you will be able to download a zip file named ‘Human_Activities.zip’. After you extract this zip file, you will get four files:

* Train - contains all the images that are to be used for training your model.  In this folder you will find 15 folders namely - 'calling', ’clapping’, ’cycling’, ’dancing’, ‘drinking’, ‘eating’, ‘fighting’, ‘hugging’, ‘laughing’, ‘listening_to_music’, ‘running’, ‘sitting’, ‘sleeping’, texting’, ‘using_laptop’ which contain the images of the respective human activities.

* Test - contains 5400  images of Human Activities. For these images you are required to make predictions as the respective class names -'calling', ’clapping’, ’cycling’, ’dancing’, ‘drinking’, ‘eating’, ‘fighting’, ‘hugging’, ‘laughing’, ‘listening_to_music’, ‘running’, ‘sitting’, ‘sleeping’, texting’, ‘using_laptop’.

### Dataset structure 

Download the dataset using

``` shell
kaggle datasets download -d aryarishabh/hand-gesture-recognition-dataset
```

Make sure the directory structure looks like


```
.
├── Dataset
│   ├── test
│   │   ├──Image_1.jpg
│   │   ├──Image_10.jpg
│   │   ├──Image_100.jpg
│   │   ├──Image_1000.jpg
│   │   ├──Image_1001.jpg
│   │   ├── .
│   │   ├── ..
│   │   ├── ...

│   │   └── .....
│   └── train
│   │   ├──Image_1.jpg
│   │   ├──Image_10.jpg
│   │   ├──Image_100.jpg
│   │   ├──Image_1000.jpg
│   │   ├──Image_1001.jpg
│   │   ├── .
│   │   ├── ..
│   │   ├── ...


Summary
18.0k files

```

### **Sample Images of Actions**
![Sample Images of Actions](output\sample_images.png)

### **Training and Validation Accuracy & Loss**
![Training and Validation Accuracy & Loss](output\Training_and_validation.png)

### **Test Prediction**
![Test Prediction](output\test_pred.png)

# Chatbot

```
We tried to create chatbot for video context, but it didn't worked well in the time frame.
At first tried using IBM wattson assisstant chatbot to give answer using retrival documents but due to api key and cloud accound problems it don't worked out. Then due to time limitations just created a basic program which can answer about video from dictionary created.

```
### **Flask app run**
![Flask app run](output\Screenshot_3.png)

### **Upload screen**
![Upload screen](output\Screenshot_2.png)

### **Welcome screen**
![Welcome screen](output\Screenshot_1.png)

### **Chat Screen**
![chat screen](output\Screenshot_5.png)

### **Chatbot Screen**
![chatbot screen](output\Screenshot_4.png)
