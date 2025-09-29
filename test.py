import pytest
from pydantic import ValidationError
from schema.user_input import UserInput

def test_valid_user_input():
    user_data = {
        "age": 30,
        "weight": 70.0,
        "height": 1.75,
        "income_lpa": 10.5,
        "smoker": False,
        "city": "Delhi",
        "occupation": "private_job"
    }
    user_input = UserInput(**user_data)
    assert user_input.age == 30
    assert user_input.weight == 70.0
    assert user_input.height == 1.75
    assert user_input.income_lpa == 10.5
    assert user_input.smoker is False
    assert user_input.city == "Delhi"
    assert user_input.occupation == "private_job"
    assert user_input.bmi == round(70.0 / (1.75**2), 2)
    assert user_input.city_tier == 1
    assert user_input.age_group == "adult"
    assert user_input.lifestyle_risk == "low"

def test_invalid_age():
    user_data = {
        "age": -5,
        "weight": 70.0,
        "height": 1.75,
        "income_lpa": 10.5,
        "smoker": False,
        "city": "Delhi",
        "occupation": "private_job"
    }
    with pytest.raises(ValidationError):
        UserInput(**user_data)

def test_invalid_weight():
    user_data = {
        "age": 30,
        "weight": 0.0,
        "height": 1.75,
        "income_lpa": 10.5,
        "smoker": False,
        "city": "Delhi",
        "occupation": "private_job"
    }
    with pytest.raises(ValidationError):
        UserInput(**user_data)

def test_invalid_height():
    user_data = {
        "age": 30,
        "weight": 70.0,
        "height": -1.75,
        "income_lpa": 10.5,
        "smoker": False,
        "city": "Delhi",
        "occupation": "private_job"
    }
    with pytest.raises(ValidationError):
        UserInput(**user_data)

def test_invalid_income():
    user_data = {
        "age": 30,
        "weight": 70.0,
        "height": 1.75,
        "income_lpa": -10.5,
        "smoker": False,
        "city": "Delhi",
        "occupation": "private_job"
    }
    with pytest.raises(ValidationError):
        UserInput(**user_data)

def test_invalid_occupation():
    user_data = {
        "age": 30,
        "weight": 70.0,
        "height": 1.75,
        "income_lpa": 10.5,
        "smoker": False,
        "city": "Delhi",
        "occupation": "invalid_occupation"
    }
    with pytest.raises(ValidationError):
        UserInput(**user_data)

def test_bmi_calculation():
    user_data = {
        "age": 30,
        "weight": 70.0,
        "height": 1.75,
        "income_lpa": 10.5,
        "smoker": False,
        "city": "Delhi",
        "occupation": "private_job"
    }
    user_input = UserInput(**user_data)
    expected_bmi = round(70.0 / (1.75**2), 2)
    assert user_input.bmi == expected_bmi

def test_city_tier_calculation():
    user_data_tier1 = {
        "age": 30,
        "weight": 70.0,
        "height": 1.75,
        "income_lpa": 10.5,
        "smoker": False,
        "city": "Mumbai",
        "occupation": "private_job"
    }
    user_input_tier1 = UserInput(**user_data_tier1)
    assert user_input_tier1.city_tier == 1

    user_data_tier2 = {
        "age": 30,
        "weight": 70.0,
        "height": 1.75,
        "income_lpa": 10.5,
        "smoker": False,
        "city": "Pune",
        "occupation": "private_job"
    }
    user_input_tier2 = UserInput(**user_data_tier2)
    assert user_input_tier2.city_tier == 2

    user_data_tier3 = {
        "age": 30,
        "weight": 70.0,
        "height": 1.75,
        "income_lpa": 10.5,
        "smoker": False,
        "city": "SomeOtherCity",
        "occupation": "private_job"
    }
    user_input_tier3 = UserInput(**user_data_tier3)
    assert user_input_tier3.city_tier == 3

def test_age_group_calculation():
    user_data_young = {
        "age": 20,
        "weight": 70.0,
        "height": 1.75,
        "income_lpa": 10.5,
        "smoker": False,
        "city": "Delhi",
        "occupation": "private_job"
    }
    user_input_young = UserInput(**user_data_young)
    assert user_input_young.age_group == "young"

    user_data_adult = {
        "age": 35,
        "weight": 70.0,
        "height": 1.75,
        "income_lpa": 10.5,
        "smoker": False,
        "city": "Delhi",
        "occupation": "private_job"
    }
    user_input_adult = UserInput(**user_data_adult)
    assert user_input_adult.age_group == "adult"

    user_data_middle_aged = {
        "age": 50,
        "weight": 70.0,
        "height": 1.75,
        "income_lpa": 10.5,
        "smoker": False,
        "city": "Delhi",
        "occupation": "private_job"
    }
    user_input_middle_aged = UserInput(**user_data_middle_aged)
    assert user_input_middle_aged.age_group == "middle_aged"

    user_data_senior = {
        "age": 65,
        "weight": 70.0,
        "height": 1.75,
        "income_lpa": 10.5,
        "smoker": False,
        "city": "Delhi",
        "occupation": "private_job"
    }
    user_input_senior = UserInput(**user_data_senior)
    assert user_input_senior.age_group == "senior"

def test_lifestyle_risk_calculation():
    # Low risk
    user_data_low_risk = {
        "age": 30,
        "weight": 70.0,
        "height": 1.75,
        "income_lpa": 10.5,
        "smoker": False,
        "city": "Delhi",
        "occupation": "private_job"
    }
    user_input_low_risk = UserInput(**user_data_low_risk)
    assert user_input_low_risk.lifestyle_risk == "low"

    # Medium risk (smoker and bmi > 27)
    user_data_medium_risk = {
        "age": 30,
        "weight": 90.0,
        "height": 1.75,
        "income_lpa": 10.5,
        "smoker": True,
        "city": "Delhi",
        "occupation": "private_job"
    }
    user_input_medium_risk = UserInput(**user_data_medium_risk)
    assert user_input_medium_risk.bmi > 27 and user_input_medium_risk.bmi <= 30
    assert user_input_medium_risk.lifestyle_risk == "medium"

    # High risk (smoker and bmi > 30)
    user_data_high_risk = {
        "age": 30,
        "weight": 100.0,
        "height": 1.75,
        "income_lpa": 10.5,
        "smoker": True,
        "city": "Delhi",
        "occupation": "private_job"
    }
    user_input_high_risk = UserInput(**user_data_high_risk)
    assert user_input_high_risk.bmi > 30
    assert user_input_high_risk.lifestyle_risk == "high"