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
    """
        _summary_
    :param filter: (dict) _description_
    :return: List[Patient] _description_
    """

    return DB.query(Patient).outerjoin(Record).filter(Record.file_name == "-",
                extract('year', Record.createdon).between(filter['from_year'], (filter['to_year'])),
                extract('month', Record.createdon).between(filter['from_month'], (filter['to_month'])),
                extract('day', Record.createdon).between(filter['from_day'], (filter['to_day'])),).all()

def get_patients_file_by_date(filename: str, year: int, month: int, day: int) -> Patient:
    """
        _summary_: Get a patient from the patients table
    :param filename: (str) _description_
    :param year: (str) _description_
    :param month: (str) _description_
    :param day: (str) _description_
    :return: models.Patient _description_
    """

    file_hear = DB.query(Record).filter(Record.file_name.ilike("%"+filename+"%",),
                    Record.doctor_first_name=="N/A", Record.doctor_last_name=="N/A",
                    extract('year', Record.createdon) == year, extract('month', Record.createdon) == month,
                    extract('day', Record.createdon) == day).first()

    if file_hear is None:
        return None

    id = file_hear.id

    # left join to get all the records for the patient
    return DB.query(Patient).outjoin(Record).filter(Record.id == id).all()