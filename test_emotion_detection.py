from EmotionDetection import emotion_detector


def test_emotion_detection():

    test_cases = {
        "I am glad this happened": "joy",
        "I am really mad about this": "anger",
        "I feel disgusted just hearing about this": "disgust",
        "I am so sad about this": "sadness",
        "I am really afraid that this will happen": "fear"
    }

    for text, expected_emotion in test_cases.items():
        result = emotion_detector(text)
        detected_emotion = result["dominant_emotion"]

        if detected_emotion == expected_emotion:
            print(f"PASSED: '{text}' → {detected_emotion}")
        else:
            print(f"FAILED: '{text}' → expected {expected_emotion}, got {detected_emotion}")


test_emotion_detection()
