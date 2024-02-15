import pandas as pd
import json
from datetime import date
import requests

# Interact with FastApi endpoint
import config as config
BACKEND_SERVER = config.get_backend_connection_server()

# Make prediction section

def get_prediction(features: dict) -> int:
    """
        _summary_: takes users input from user interface returns a singular prediction
    :param features: _type_: _description_
    :return:
    """
    url = BACKEND_SERVER + "predict"
    response = requests.get(url, json=features)
    if response.status_code == 200:
        results = response.json()
        prediction = results['prediction']
        return prediction
    else:
        print(response.status_code)
        return pd.DataFrame([])

def get_prediction_documnet(filename:str, data:pd.DataFrame) -> pd.DataFrame:
    """
        Takes file input from user interface returns a prediction dataframe
    :param filename:
    :param data:
    :return:
    """

    data = data_frame_fix_column_with_Nan_float(data)
    list_of_json = data.to_dict(orient='records')
    data_json = dict()
    data_json["record"] = {"id": 0, "file_name": filename}
    data_json["patient"] = list_of_json
    url = BACKEND_SERVER + "predict_multiple"
    response = requests.get(url, json=data_json)
    if response.status_code == 200:
        result = json.loads(response.content)
        prediction_df = pd.read_json(result, orient='index')
        data["prediction"] = prediction_df["prediction"]
        return data, True
    elif response.status_code == 422:
        return "File is not within the correct format!", False
    else:
        return pd.DataFrame([]), True

def data_frame_fix_column_with_Nan_float(data):
    """
        _summary_: Fix nan_float issues in data frame, pydantic model doesn't like Nan's in Float columns
        Json encoder doesn't like to deal with Nan's in Float columns.
    :param data:
    :return:
    """

    float_cols = data.select_dtypes(include=["float64", "int64"]).columns
    str_cols = data.select_dtypes(include=['object']).columns
    data.loc[:, float_cols] = data.loc[:, float_cols].fillna(0.0)
    data.loc[:, str_cols] = data.loc[:, str_cols].fillna('')
    return data

# Data Base services
def search_patient_by_fullname(firstname: str, lastname:str) -> pd.DataFrame:
    """
        _summary_: Search patient records by fullname.
    :param firstname:
    :param lastname:
    :return:
    """

    url = BACKEND_SERVER + f"search/patient/{firstname}&{lastname}".format(firstname=firstname \
    if len(firstname) else "%%", lastname=lastname if len(lastname) else "%%")

    response = requests.get(url)

    if response.status_code == 200:
        results = response.json()
        return results
    else:
        return pd.DataFrame([])

def search_patient_by_window_period(from_date: date, to_date: date) -> pd.DataFrame:
    """
        _summary_: Search patient records by Window period
    :param from_date:
    :param to_date:
    :return:
    """

    url = BACKEND_SERVER + f"search/patient/period/{from_date}&{to_date}".format( \
            fromdate=from_date.strftime("%Y-%m-%d"), todate=to_date.strftime("%Y-%m-%d"))

    response = requests.get(url)
    if response.status_code == 200:
        results = response.json()
        return results
    else:
        return pd.DataFrame([])

def search_patients_file_by_date(file_name:str, created_on: date) -> pd.DataFrame:
    """
        _summary_: Search file patients records by date crated on
    :param file_name:
    :param created_on:
    :return:
    """

    url = BACKEND_SERVER + f"search/file/{file_name}&{created_on}" \
    .format(filename=file_name,createdon=created_on.strftime("%Y-%m-%d"))

    response = requests.get(url)
    if response.status_code == 200:
        results = response.json()
        if results is not None:
            return results
        else:
            return pd.DataFrame([])
    else:
        return None

