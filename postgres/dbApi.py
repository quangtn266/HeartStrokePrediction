from database import SessionLocal
from sqlalchemy import and_, extract
from venv import create
from models import Patient, Record
from typing import List

DB = SessionLocal()

def create_record(new_record: Record) -> int:
    """
        _summary_: Insert a record into the record table
    :param new_record: (model.Record): _description_
    :return: record id
    """

    DB.add(new_record)
    DB.flush()
    DB.commit()

    return new_record.id

def insert_patient(new_patient: Patient) -> int:
    """
        _summary_: insert a patient into the patient table
    :param new_patient: (models.Patient_in_db): _description_
    :return: int: patient
    """

    DB.add(new_patient)
    DB.flush()
    DB.commit()

    return new_patient

def get_patient_by_fullname(first_name: str, last_name: str) -> List[Patient]:
    """
        _summary_ : get a patient from the patients table
    :param first_name: (str) - _description_
    :param last_name: (str) - _description_
    :return: models.Patient: _description_
    """

    return DB.query(Patient).outerjoin(Record).filter(Record.file_name=="-",
        and_(Patient.firstname.ilike("%"+first_name+"%"),Patient.lastname.ilike("%"+last_name+"%"))).all()


def get_patients_by_window_period(filter: dict) -> List[Patient]: