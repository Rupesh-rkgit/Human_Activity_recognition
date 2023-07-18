# Import Flask library
from flask import Flask, request, render_template
import cv2
from model import FacialExpressionModel
import numpy as np

facec = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
model = FacialExpressionModel("model.json", "model_weights\model_weight_only.h5")
font = cv2.FONT_HERSHEY_SIMPLEX
# Import OpenCV and Watson Assistant libraries
import cv2

# Initialize the app
app = Flask(__name__, static_folder='static')

# Initialize the assistant with your credentials
# Define a route for the home page


@app.route('/')
def home():
    # Render the home page template
    return render_template('home.html')

# Define a route for the video upload page

count = {"calling":0, "clapping":0,
                     "cycling":0,
                     "dancing":0, "drinking":0,
                     "eating":0, "fighting":0,
                     "hugging":0, "laughing":0,
                     "listening_to_music":0,
                     "running":0,
                     "sitting":0,
                     "sleeping":0,
                     "texting":0,
                     "using_laptop":0}
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    # Check if the request method is POST
    if request.method == 'POST':
        # Get the uploaded file from the request
        file = request.files['file']

        # Check if the file is valid
        if file and file.filename.endswith('.mp4'):
            # Save the file to a temporary location
            file.save('static/temp.mp4')

            # Load the video file using OpenCV
            video = cv2.VideoCapture('static/temp.mp4')

            # Process the video using your machine learning model and store the results in a global variable
            global results
            results = []
            
            # Loop through the frames of the video
            while True:
                # Read a frame from the video
                ret, fr = video.read()

                # Check if the frame is valid
                if not ret:
                    break

                # Process the frame using your machine learning model as explained in step 1
                else:
                    gray_fr = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
                    faces = facec.detectMultiScale(gray_fr, 1.3, 5)

                    for (x, y, w, h) in faces:
                        fc = gray_fr[y:y+h, x:x+w]

                        roi = cv2.resize(fc, (48, 48))
                        pred = model.predict_emotion(roi[np.newaxis, :, :, np.newaxis])
                        count[pred]+=1
        
                        cv2.putText(fr, pred, (x, y), font, 1, (255, 255, 0), 2)
                                # cv2.putText(fr, str(self.count[pred]),
                             #             (50, 50), font, 1, (255, 255, 0), 2)
                        cv2.rectangle(fr, (x, y), (x+w, y+h), (255, 0, 0), 2)

                    _, jpeg = cv2.imencode('.jpg', fr)
                    # return jpeg.tobytes()

                # Append the results to the global variable
                results.append(fr)

            # Render the chat page template with the video file name as an argument
            return render_template('chat.html', video=file.filename)

        else:
            # Render an error message if the file is invalid
            return "Invalid file format. Please upload a .mp4 video file."

    else:
        # Render the upload page template if the request method is GET
        return render_template('upload.html')

# Define a route for the chat page
@app.route('/chat', methods=['GET', 'POST'])
def chat():
    # Check if the request method is POST
    if request.method == 'POST':
        # Get the user message from the request form data
        message = request.form['message']

        # Check if the message is empty or "quit"
        if not message or message.lower() == "quit":
            # Render a goodbye message if the message is empty or "quit"
            return "Assistant: Thank you for using the chatbot. Goodbye!"
        elif message == "Can you show me count of actions?":
            return "Assistant: yes, tell me which action you want to know"
        else:
            # Send the message to the assistant and get the response as explained in step 2
            # response = assistant.message(
            # assistant_id=assistant_id,
            # session_id=session_id,
            # input={
            #     'message_type': 'text',
            #     'text': message
            #     }
            # ).get_result()
            
        

            # Check if the response contains any entities related to the video context
            # For example, you can check if the entity type is "action" or "count"
            # if response['output']['entities']:
            #     # Get the entity value from the response
            #     entity = response['output']['entities'][0]['value']

            #     # Use the global results variable to find the answer from the video analysis
            #     # For example, you can count how many times a certain action occurred in the video
            #     answer = 0
            #     for result in results:
            #         if result['action'] == entity:
            #             answer += 1

            #     # Append the answer to the response text
            #     response['output']['generic'][0]['text'] += f" The answer is {answer}."

            # # Return the response text as an HTML element
            return f"<p>Assistant: The total count is {count[message]}</p>"

    else:
        # Render an error message if the request method is GET
        return "Invalid request method. Please use POST."


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)