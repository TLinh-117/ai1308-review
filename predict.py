def predict(scores):
    return max(scores, key=scores.get)
