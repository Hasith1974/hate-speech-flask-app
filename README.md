# Hate Speech Detection Web Application

A full-stack Machine Learning web application that identifies whether a given text contains Hate Speech, Offensive Language, or No Hate content.

The system integrates a trained ML model with a Flask backend and a web-based frontend interface.

This project is built and deployed as a complete web application on the Render cloud platform.

---

## Project Overview

The Hate Speech Detection Web Application allows users to enter any text and receive an instant classification result.  
It uses Natural Language Processing techniques with TF-IDF vectorization and a trained machine learning classifier.

The web application consists of:

- Backend server built with Flask  
- Machine Learning model trained using Scikit-learn  
- Frontend interface developed with HTML, CSS, and JavaScript  

---

## Folder Structure
hate-speech-flask-app/
│
└── Backend/
│
├── app.py
├── hate_model.pkl
├── tfidf_vectorizer.pkl
├── requirements.txt
├── Procfile
├── runtime.txt
├── .python-version
│
└── frontend/
├── index.html
├── style.css
└── script.js

## Technologies Used

- Python 3.10  
- Flask  
- Flask-CORS  
- Scikit-learn  
- NLTK  
- Joblib  
- HTML  
- CSS  
- JavaScript  
- GitHub  
- Render Cloud Platform  

---

## Machine Learning Implementation

The application uses:

- TF-IDF Vectorizer for feature extraction  
- Supervised machine learning classifier for text classification  

The trained model and vectorizer are saved and loaded using Joblib.

---

## Build and Deployment

The project is:

- Version controlled using GitHub  
- Built and hosted on Render  

Deployment includes:

- Gunicorn production server  
- Python runtime configuration  
- Automated cloud builds  

---

## Application Workflow

User input →  
Frontend interface →  
Flask API →  
Machine Learning model →  
Prediction result displayed.

---

## Project Outcome

The deployed system successfully classifies text into:

- No Hate  
- Offensive  
- Hate  

Providing fast and accurate results through a web-based interface.

---

## Author

Hasith Darla  

---

## License

This project is created for educational and demonstration purposes.
