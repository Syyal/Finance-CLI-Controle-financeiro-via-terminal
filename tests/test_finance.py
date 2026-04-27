from services.finance_service import load_data, add_expense

def test_load_data():
    data = load_data()
    assert isinstance(data, list)

def test_add_expense():
    add_expense(10, "teste")
    data = load_data()
    assert any(e["category"] == "teste" for e in data)