# AI-Based Communication Intelligence Platform using NLP and Machine Learning

## Live Demo

https://ai-communication-intelligence-system-pz6enjbtm.vercel.app

---

## Overview

AI-Based Communication Intelligence Platform is a real-time AI-powered system that analyzes human communication using Natural Language Processing (NLP), Machine Learning, and Speech Recognition.

The platform evaluates:

- Emotion
- Confidence
- Communication Quality
- Fluency / Hesitation
- AI-based Communication Feedback

The system supports both:

- Text-based communication analysis
- Voice-based speech-to-text communication analysis

It also provides:

- Interactive analytics dashboard
- Dynamic charts and visualizations
- Downloadable PDF reports
- Real-time communication insights

---

# Features

## Real-Time Communication Analysis

Analyzes user communication instantly using Machine Learning and NLP.

---

## Speech-to-Text Integration

Users can speak through microphone input.

The system converts speech into text using browser Speech Recognition APIs and performs AI analysis on the generated text.

---

## Emotion Detection

Detects whether communication tone is:

- Positive
- Negative
- Neutral

---

## Confidence Analysis

Evaluates communication confidence level.

---

## Hesitation Detection

Detects filler words such as:

- um
- uh
- like
- actually

and estimates fluency level.

---

## AI Feedback System

Generates intelligent communication improvement suggestions.

Example:

- Improve confidence while speaking
- Reduce filler words
- Use more positive communication tone

---

## Analytics Dashboard

Interactive dashboard with:

- Confidence score
- Communication score
- Fluency score
- Dynamic charts

---

## PDF Report Download

Users can download communication analysis reports directly as PDF.

---

# Technologies Used

## Frontend

- HTML
- CSS
- JavaScript
- Chart.js

## Backend

- FastAPI
- Python

## Machine Learning / NLP

- Scikit-Learn
- TF-IDF Vectorization
- Logistic Regression
- NLP Text Processing

## Speech Recognition

- Browser Speech Recognition API

---

# Machine Learning Workflow

```text
Speech/Text Input
        ↓
Speech-to-Text Conversion
        ↓
Text Preprocessing
        ↓
TF-IDF Vectorization
        ↓
Logistic Regression Model
        ↓
AI Communication Analysis
        ↓
Dashboard + Feedback + PDF Report
```

---

# Dataset Used

The project uses a real-world sentiment analysis dataset:

- Sentiment140 Dataset

The dataset was used to train the communication sentiment prediction model.

---

# Project Architecture

```text
Frontend (HTML/CSS/JS)
        ↓
FastAPI Backend
        ↓
Machine Learning Model
        ↓
NLP Analysis Engine
        ↓
Analytics Dashboard
```

---

# How to Run the Project

## Backend Setup

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

---

## Frontend Setup

Open frontend folder using VS Code.

Run using Live Server.

---

# Future Improvements

- User Authentication
- MongoDB Integration
- Cloud Deployment
- Advanced Deep Learning Models
- Real-Time Voice Emotion Detection
- AI Interview Performance Analysis

---

# Resume Highlights

- Developed an AI-powered communication analysis platform using NLP and Machine Learning.
- Integrated speech-to-text functionality for real-time voice communication analysis.
- Trained a sentiment analysis model using TF-IDF Vectorization and Logistic Regression.
- Built interactive analytics dashboards with AI-generated feedback and PDF report generation.

---

# Author

Prathyusha Myla
