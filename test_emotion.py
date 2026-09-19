from emotion_engine import EmotionDetector


def test_happy_features_classify_as_happy():
    detector = EmotionDetector.__new__(EmotionDetector)

    features = {
        "mouth_curve": 0.1,
        "eye_aspect_ratio": 0.25,
        "mouth_aspect_ratio": 0.5,
        "eyebrow_position": 0.5,
    }

    emotion, confidence = detector._classify_emotion(features)

    assert emotion == "happy"
    assert confidence == 1.0


def test_neutral_features_fall_back_to_neutral():
    detector = EmotionDetector.__new__(EmotionDetector)

    features = {
        "mouth_curve": 0.0,
        "eye_aspect_ratio": 0.3,
        "mouth_aspect_ratio": 0.3,
        "eyebrow_position": 0.5,
    }

    emotion, confidence = detector._classify_emotion(features)

    assert emotion == "neutral"
    assert confidence == 0.6


def test_euclidean_distance():
    detector = EmotionDetector.__new__(EmotionDetector)

    assert detector._euclidean_distance((0, 0), (3, 4)) == 5.0
