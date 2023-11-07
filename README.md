# Watermelon Disease Prediction

This repository contains a Flask web application for predicting watermelon diseases from images. Below are the installation instructions to set up and run the application on your local machine.

## Installation Instructions

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your-username/watermelon_disease_prediction.git
    ```

2. Navigate to the project directory:

    ```bash
    cd watermelon_disease_prediction
    ```

3. Create a virtual environment for the project (recommended for isolation):

    ```bash
    python -m venv env
    ```

4. Activate the virtual environment:

    - On Windows:

    ```bash
    .\env\Scripts\activate
    ```

    - On macOS and Linux:

    ```bash
    source env/bin/activate
    ```

5. Install the required Python packages from the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

6. Navigate to the `my_flask_app` directory:

    ```bash
    cd my_flask_app
    ```

7. Run the Flask application:

    ```bash
    python app.py
    ```

The application will start, and you can access it in your web browser:

- To upload an image, go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

- To capture an image using your camera, go to [http://127.0.0.1:5000/capture](http://127.0.0.1:5000/capture)

Follow the on-screen instructions to use the application.