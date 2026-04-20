import json
from datetime import datetime

FILE = "data/data.json"

def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_expense(value, category):
    data = load_data()

    expense = {
        "value": value,
        "category": category,
        "date": str(datetime.now())
    }

    data.append(expense)
    save_data(data)

    print("Gasto adicionado!")

def list_expenses():
    data = load_data()

    for e in data:
        print(f'{e["date"]} - {e["category"]}: R${e["value"]}')

def summary():
    data = load_data()
    total = sum(e["value"] for e in data)

    print(f"Total gasto: R${total}")