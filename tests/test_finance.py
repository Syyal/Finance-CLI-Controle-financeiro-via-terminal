from services.finance_service import load_data

def test_load_data():
    data = load_data()
    assert isinstance(data, list)