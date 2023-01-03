from pydantic import BaseModel
from typing import Optional


class Nmc(BaseModel):
    hf_id_hmis : Optional[str]
    hf_id_abdm : Optional[str]
    health_facility_name : Optional[str]
    PatientName : Optional[str]
    Age : Optional[str]
    PtnAddress : Optional[str]
    City : Optional[str]
    prmnt_pin : Optional[str]
    Abha_Id : Optional[str]
    AadharNo : Optional[str]
    PtnIdentificationNo : Optional[str]
    PtnMobileNo : Optional[str]
    VisitType : Optional[str]
    DepartmentVisitedName : Optional[str]
    DepartmentVisitedCode : Optional[str]
    datetime_of_transaction : Optional[str]