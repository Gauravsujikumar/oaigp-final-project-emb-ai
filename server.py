from flask import Flask, request
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def detect_emotion():

    text = request.args.get("textToAnalyze")

    if text == "":
        return "Invalid input"

    result = emotion_detector(text)

    return str(result)

app.run(host="0.0.0.0", port=5000)
