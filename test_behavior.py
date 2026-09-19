import pytest

from pose_behavior import BehaviorDetector


@pytest.fixture
def detector():
    instance = BehaviorDetector.__new__(BehaviorDetector)
    instance.pose_history = []
    instance.max_history = 10
    return instance


def test_default_behavior_is_standing(detector):
    behavior, confidence = detector._classify_behavior({})
    assert behavior == "standing"
    assert confidence == 0.5


def test_posture_requires_visible_knees(detector):
    keypoints = {
        "left_hip": {"y": 0.5},
        "right_hip": {"y": 0.5},
        "left_knee": {"y": 0.6, "visibility": 0.4},
        "right_knee": {"y": 0.6, "visibility": 0.4},
    }

    behavior, confidence = detector._detect_posture(keypoints)

    assert behavior == "unknown"
    assert confidence == 0.5


def test_posture_detects_sitting(detector):
    keypoints = {
        "left_hip": {"y": 0.5},
        "right_hip": {"y": 0.5},
        "left_knee": {"y": 0.58, "visibility": 0.9},
        "right_knee": {"y": 0.58, "visibility": 0.9},
    }

    behavior, confidence = detector._detect_posture(keypoints)

    assert behavior == "sitting"
    assert confidence == 0.9
