import json
from pathlib import Path
from typing import List,Dict

Data_File= Path("...","data","products.json")

def load_products() -> List[Dict]:
    if Data_File.exists():
        with open(Data_File,'r',encoding="utf-8") as file_data:
            return json.load(file_data)
    else:
        return []
    
def all_products() -> List[Dict]:
    if Data_File.exists():
        with open(Data_File,'r',encoding="utf-8") as data_file:
            return json.load(data_file)
    return []

