from typing import List, Tuple, Annotated
from typing_extensions import TypedDict
from operator import add

class State(TypedDict):
    input:dict
    math_revision:str
    math_part:str
    math_report_class:str
    math_report_revision:str
    physics_part:str
    physics_revision:str
    physics_report_class:str
    physics_report_revision:str
    organic_chemistry_part:str
    organic_chemistry_revision:str
    organic_chemistry_report_class:str
    organic_chemistry_report_revision:str
    experience_organic:str
    inorganic_chemistry_part:str
    inorganic_chemistry_revision:str
    inorganic_chemistry_report_class:str
    inorganic_chemistry_report_revision:str
    physical_chemistry_part:str
    physical_chemistry_revision:str
    physical_chemistry_report_class:str
    physical_chemistry_report_revision:str
    final_report:str
    final_score:int