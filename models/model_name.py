from api.database import Base_1, Base_2 
from api.models.base_model import ModelBase

class DB_Schema1(Base_1, ModelBase):
    __tablename__ = "DB_Schema1_table"

class DB_Schema2(Base_2, ModelBase):
    __tablename__ = "DB_Schema2_table"    
    