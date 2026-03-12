from flask import Flask, jsonify, request

from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotionDetector():

    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    result = {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant_emotion
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
