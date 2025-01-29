from enum import Enum


class Language(Enum):
    PYTHON = 0
    R = 1


class Deployment_Type(Enum):
    API = 0
    DASHBOARD = 1
    ETL = 2
