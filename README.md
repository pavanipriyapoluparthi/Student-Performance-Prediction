# Student-Performance-Prediction
Student Performance Prediction System using Machine Learning and Flask.

Project Overview
The Student Performance Prediction System is a machine learning-based web application developed using Python and Flask. It predicts students' final academic scores based on their study habits and academic performance.

The application provides user registration and login, student performance prediction, and prediction history.

Features:
User Registration and Login
Secure User Sessions
Student Performance Prediction
Prediction based on five input parameters
Save predictions in MySQL database
View Previous Prediction History


Input Parameters:
Study Hours
Attendance
Assignment Score
Midterm Score
Sleep Hours


Technologies Used:

Technology                                      Purpose

Python                                         Programming language
Flask                                          Web framework
Machine Learning                               Score prediction
MySQL                                          Database
HTML and CSS                                   Frontend development
Pandas and NumPy                               Data processing
Joblib                                         Model loading


Student-Performance-Prediction/
│
├── app.py
├── data_analysis.py
├── student_performance_model.pkl
├── dataset/
├── templates/
└── README.md


How It Works:
Users register and log in to the application.
Users enter their study hours, attendance, assignment score, midterm score, and sleep hours.
The trained machine learning model predicts the final score.
The prediction is stored in the MySQL database.
Users can view their previous prediction records.


Installation and Execution

1.Clone the repository:
git clone https://github.com/pavanipriyapoluparthi/Student-Performance-Prediction.git

2.Open the project folder:
cd Student-Performance-Prediction

3.Create and activate a virtual environment:
python -m venv venv
venv\Scripts\activate

4.Install the required packages:
pip install flask joblib numpy mysql-connector-python pandas scikit-learn

5.Configure the following environment variables in Windows CMD:
set "DB_PASSWORD=your_mysql_password"
set "FLASK_SECRET_KEY=your_secret_key"

6.Create and configure the MySQL database and required tables.

7.Run the application:
python app.py

8.Open your browser and visit:
http://127.0.0.1:5000


Future Enhancements:
Improve prediction accuracy.
Add visual analytics and performance reports.
Enhance the user interface.
Deploy the application online.

Author

Developed as a Student Performance Prediction project using Machine Learning and Web Development.
