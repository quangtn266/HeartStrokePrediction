import pandas as pd
import numpy as np
import re
import datetime import datetime
from dateutil.relativedelta import relativedelta

import web_services as ws
import streamlit as st

# Make predictions Services

def get_prediction() -> int:
    """
        _summary_: Take users input from user interface returns a singular prediction
    :return: _type_: _description_
    """

    features = input_details_to_json()
    prediction = ws.get_prediction(features)
    if prediction is not None:
        return prediction
    else:
        st.error("An error occurred while getting the predicton!")

def get_prediction_document(filename: str, data: pd.DataFrame) -> pd.DataFrame:
    """
        _summary_: Takes file input from User interface returns a Prediction Dataframe
    :param filename:
    :param data:
    :return:
    """

    predictions_file, success = ws.get_prediction_document(filename, data)

    if not success:
        st.error(predictions_file)
        return pd.DataFrame([])
    elif predictions_file is not None:
        return predictions_file
    else:
        st.error("An error occurred while getting the file's prediction!")
        return predictions_file

def input_details_to_json() -> dict:
    """
        _summary_: Takes User input and converts it to json format
    :return:
    """

    myform_json = {"record": {"id": 0,
                    "file_name": "-",
                    "doctor_first_name": doctor_first_name if len(doctor_first_name.strip()) else "N/A",
                    "doctor_last_name": doctor_last_name if len(doctor_last_name.strip()) else "N/A",}
                   "patient": {"id": 0,
                               "firstname": firstname,
                               "lastname": lastname,
                               "gender": gender,
                               "age": age,
                               "hypertension": 1 if hypertension == "yes" else 0,
                               "heart_disease": 1 if heart_disease == "yes" else 0,
                               "ever_married": ever_married,
                               "work_type": work_type,
                               "Residence_type": residence_type,
                               "avg_glucose_level": avg_glucose_level,
                               "bmi": bmi,
                               "smoking_status": smoking_status
                               }
                    }
    return myform_json

## DataFrame Stylers
def data_frame_style_color_neg(val):
    """
        _summary_
    :param val:
    :return:
    """

    color = "red" if type(val) == str and val == "Risk of Stroke" else "green"

    return 'color: %s' % color

def float_format(val):
    """
        _summary_ : Pandas dataframe styler
    :param val:
    :return:
    """

    return "{:.2f}".format(val)

def data_frame_style_display(data: pd.DataFrame) -> pd.DataFrame:
    """
        _summary_: Pandas Dataframe styler
    :param data:
    :return:
    """

