import json
from pathlib import Path
from typing import List,Dict

#Data_File= Path("..","data","products.json")
DATA_FILE = Path(__file__).resolve().parent.parent.parent / "data" / "products.json"
def load_products() -> List[Dict]:
    if DATA_FILE.exists():
        with open(DATA_FILE,'r',encoding="utf-8") as file_data:
            return json.load(file_data)
    else:
        return []
    
def all_products() -> List[Dict]:
    if DATA_FILE.exists():
        with open(DATA_FILE,'r',encoding="utf-8") as data_file:
            return json.load(data_file)
    print("data file not found")
    return []

