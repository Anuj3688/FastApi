from models import Tea
from typing import List
from db import database
class Crud(database.Database):
    def __init__(self):
        super().__init__()
    def add_new_tea(self,tea:Tea):
        self.cursor.execute()
        pass
    def remove_tea(self,tea):
        pass
    def get_all_tea(self) -> List[Tea]:
        pass
    def get_tea_from_id(self,tea_id:int):
        pass