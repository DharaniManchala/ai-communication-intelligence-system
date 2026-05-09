from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import joblib


app = FastAPI()


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# LOAD ML MODEL
model = joblib.load(
    "model/communication_model.pkl"
)


# REQUEST MODEL
class UserInput(BaseModel):

    text: str


# HOME ROUTE
@app.get("/")
def home():

    return {

        "message":
        "Backend Running Successfully"

    }


# ANALYZE API
@app.post("/analyze")
def analyze(data: UserInput):

    text = data.text


    # ML PREDICTION
    prediction = model.predict(
        [text]
    )[0]


    # POSITIVE
    if prediction == 1:

        emotion = "Positive"

        confidence = "High"

        communication = "Strong"


    # NEGATIVE
    else:

        emotion = "Negative"

        confidence = "Low"

        communication = "Weak"


    # HESITATION DETECTION
    filler_words = [
        "um",
        "uh",
        "like",
        "actually"
    ]

    hesitation_count = 0

    for word in text.lower().split():

        if word in filler_words:

            hesitation_count += 1


    # HESITATION LEVEL
    if hesitation_count == 0:

        hesitation = "Low"

    elif hesitation_count <= 2:

        hesitation = "Medium"

    else:

        hesitation = "High"


    # AI SCORES
    confidence_score = (
        90 if prediction == 1 else 40
    )

    communication_score = (
        85 if prediction == 1 else 35
    )

    hesitation_score = max(
        0,
        100 - (hesitation_count * 20)
    )


    # AI FEEDBACK
    suggestions = []


    # NEGATIVE EMOTION
    if emotion == "Negative":

        suggestions.append(
            "Your communication tone sounds negative. Try using more positive and confident language."
        )


    # LOW CONFIDENCE
    if confidence == "Low":

        suggestions.append(
            "Confidence level appears low. Try speaking more directly and assertively."
        )


    # WEAK COMMUNICATION
    if communication == "Weak":

        suggestions.append(
            "Communication clarity can be improved by using stronger sentence structures."
        )


    # HIGH HESITATION
    if hesitation == "High":

        suggestions.append(
            "Too many filler words detected. Reduce words like 'um', 'uh', and 'actually'."
        )


    # POSITIVE FEEDBACK
    if emotion == "Positive":

        suggestions.append(
            "Your communication tone is positive and engaging."
        )


    # STRONG COMMUNICATION
    if communication == "Strong":

        suggestions.append(
            "Communication delivery looks strong and confident."
        )


    # LOW HESITATION
    if hesitation == "Low":

        suggestions.append(
            "Fluency level is excellent with very low hesitation."
        )


    # DEFAULT FEEDBACK
    if len(suggestions) == 0:

        suggestions.append(
            "Communication analysis completed successfully."
        )


    # FINAL RESPONSE
    return {

        "emotion":
        emotion,

        "confidence":
        confidence,

        "communication":
        communication,

        "hesitation":
        hesitation,

        "confidence_score":
        confidence_score,

        "communication_score":
        communication_score,

        "hesitation_score":
        hesitation_score,

        "suggestions":
        suggestions

    }