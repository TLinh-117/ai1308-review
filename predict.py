THRESHOLD = 0.5


def predict(scores):
    return max(scores, key=scores.get)
