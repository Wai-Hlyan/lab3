from lab2.bmi import calculate_bmi as bmi  # type: ignore

def test_underweight(): 
    assert bmi(1.75, 50) == -1

def test_normal_weight():
    assert bmi(1.75, 68) == 0

def test_overweight():
    assert bmi(1.75, 80) == 1   