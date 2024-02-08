from stroke_prediction.data_processing import pipeline
import pickle

def make_prediction(X):
    X = pipeline(X)
    file = "../models/classifier.pkl"
    clf = pickle.load(open(file, "rb"))

    return clf.predict(X)