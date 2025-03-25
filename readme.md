# Breast Cancer Detection

This project is a web-based application for predicting whether a breast tumor is **Malignant** or **Benign** based on user-provided features. The application uses a trained machine learning model and is built with Flask for the backend.

## Features
- Accepts 9 input features related to breast cancer diagnosis.
- Predicts whether the tumor is **Malignant** (cancerous) or **Benign** (non-cancerous).
- Displays predictions with a user-friendly interface.
- Highlights **Malignant** predictions in red and **Benign** predictions in green.

## Dataset
The model is trained on the Breast Cancer Wisconsin (Diagnostic) dataset. The features include:
1. Clump Thickness
2. Uniformity of Cell Size
3. Uniformity of Cell Shape
4. Marginal Adhesion
5. Single Epithelial Cell Size
6. Bare Nuclei
7. Bland Chromatin
8. Normal Nucleoli
9. Mitoses

The target variable is:
- `2`: Benign
- `4`: Malignant

## Technologies Used
- **Python**: For backend logic and machine learning.
- **Flask**: For building the web application.
- **HTML/CSS**: For the user interface.
- **Scikit-learn**: For training the machine learning model.
- **Pickle**: For saving and loading the trained model.

## Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/breast-cancer-detection.git
   cd breast-cancer-detection
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
3. Ensure the model.pkl file (trained model) is in the project directory.
4. Run the Flask application:
    ```bash
    python app.py
5. Open your browser and navigate to:
    http://127.0.0.1:5000/

## Usage
1. Enter the 9 features in the input fields on the web page.
2. Click the Predict button.
3. The result will display whether the tumor is Malignant or Benign:
    Malignant: Displayed in red.
    Benign: Displayed in green.

## File Structure
Breast-Cancer-Detection/

│

├── Codes/

│   └──logistic_regression.ipynb                          # Code

│   └──logistic_regression.py                             # Code

├── Dataset/

│   └──breast_cancer.csv                                  # Dataset

├── [app.py](http://_vscodecontentref_/1)                 # Flask application

├── [model.pkl](http://_vscodecontentref_/2)              # Trained machine learning model

├── templates/

│   └── index.html         # HTML template for the web interface

└── [readme.md](http://_vscodecontentref_/3)              # Project documentation


## Screenshots
![Screenshot 2025-03-25 154440](https://github.com/user-attachments/assets/9bbd0e5c-70cc-4db4-99af-d39766acb9e0)

## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.
