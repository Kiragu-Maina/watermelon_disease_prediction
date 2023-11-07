from flask import Flask, request, render_template
import tensorflow as tf
import numpy as np
import zipfile
import cv2

app = Flask(__name__)

# Load your machine learning model
# Replace this with the path to your saved model directory
saved_model_path = "/home/kiragu-m/ml models/watermelon_disease_prediction_model/"

# Load the saved model
model = tf.saved_model.load(saved_model_path)
# Function to make predictions
def predict_image(image_path):
    
    with zipfile.ZipFile('class_names.zip', 'r') as archive:
        class_names_str = archive.read('class_names.txt').decode('utf-8')

    # Split the string to get the class names as a list
    class_names = class_names_str.split('\n')

    # Load the image from the local file
    img = tf.keras.utils.load_img(image_path, target_size=(512, 512))
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create a batch

    predictions = model(img_array)
    score = tf.nn.softmax(predictions[0])

    print(score)

    # Replace 'class_names' with the list of class names used by your model
    # class_names = [...]  # Add your class names here

    
    return class_names[np.argmax(score)]

@app.route("/", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if "file" not in request.files:
            return "No file part"
        file = request.files["file"]
        if file.filename == "":
            return "No selected file"
        if file:
            # Save the uploaded file to a temporary location
            file_path = "static/temp.jpg"
            file.save(file_path)
            # Make predictions using your model
            predictions = predict_image(file_path)
            return render_template("result.html", predictions=predictions, image_path=file_path)
    return render_template("upload.html")


@app.route('/capture', methods=['GET', 'POST'])
def capture_image():
    if request.method == 'POST':
        # Use OpenCV to capture an image from the camera
        capture = cv2.VideoCapture(0)
        ret, frame = capture.read()
        capture.release()
        
        if ret:
            # Save the captured image to a file
            cv2.imwrite('static/captured_image.jpg', frame)
            
            # Call your prediction function with the captured image
            predicted_class = predict_image('static/captured_image.jpg')
            
            return render_template("result.html", predictions=predicted_class, image_path='static/captured_image.jpg')
        else:
            return 'Error capturing image'

    return '''
        <form method="post">
            <p>Point the camera and press the "Capture Image" button:</p>
            <button type="submit">Capture Image</button>
        </form>
    '''
    
if __name__ == "__main__":
    app.run(debug=True)
