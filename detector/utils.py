import pickle
import os

_model = None

def get_model():
    global _model
    if _model is None:
        model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "spam_model.pkl")
        with open(model_path, "rb") as f:
            _model = pickle.load(f)
    return _model
