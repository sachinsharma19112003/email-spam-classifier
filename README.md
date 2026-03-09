## 📌 Project Overview

This project is a Machine Learning–based web application that classifies SMS messages as **Spam** or **Ham (Not Spam)** using Natural Language Processing (NLP).

The trained model and TF-IDF vectorizer are loaded using Pickle, and the application is deployed using Streamlit for real-time prediction.

---

## 🎯 Problem Statement

Spam messages are a common issue in digital communication. Detecting spam automatically helps improve user experience and security.

The goal of this project is to build a text classification model that can accurately identify spam messages.

---

## 🧠 Machine Learning Workflow

### 1️⃣ Text Preprocessing

* Cleaning text
* Removing stopwords
* Tokenization

### 2️⃣ Feature Extraction

* TF-IDF Vectorization used to convert text into numerical format.

### 3️⃣ Model Training

* Supervised classification model trained on labeled SMS dataset.

### 4️⃣ Model Saving

Trained model saved as:

```
spam_model.pkl
```

Vectorizer saved as:

```
vectorizer.pkl
```

### 5️⃣ Deployment

Model deployed using Streamlit.

---

## 🚀 Application Features

✅ User-friendly interface
✅ Real-time spam prediction
✅ TF-IDF based text transformation
✅ Pre-trained model loading
✅ Error handling for empty input

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* NLP (TF-IDF)
* Streamlit
* Pickle

---

## 📂 Project Structure

```
├── app.py
├── spam_model.pkl
├── vectorizer.pkl
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run the Project

### 1️⃣ Clone Repository

```
gh repo clone sachinsharma19112003/email-spam-classifier
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run Streamlit App

```
streamlit run app.py
```

---

## 📈 Output Example

Input:

```
Congratulations! You have won a free lottery ticket.
```

Output:

```
🚨 This is a Spam Message
```

---

## 🌐 Deployment Options

The project can be deployed on: https://email-spam-classifier-26okxcrgtpuaehgex98cc9.streamlit.app/

* Streamlit Cloud

---

## 👨‍💻 Author

Sachin Sharma
Machine Learning | Data scientist 🚀

