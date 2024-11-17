from employee_info import get_employees_by_age_range, calculate_average_salary, get_employees_by_dept

def test_employee_by_age_range():
    expected = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    ]
    upper = 23
    lower = 40
    result =  get_employees_by_age_range(upper,lower)
    assert result == expected

def test_calculate_average_salary():
    expected = 60166.666666666664
    
    result = calculate_average_salary()
    
    assert result == expected