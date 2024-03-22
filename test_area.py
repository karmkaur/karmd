import pytest  
from src.area import calculate_area_square  
  
def test_calculate_area_square_negative():  
    with pytest.raises(TypeError):  
        calculate_area_square(-2)  
  
def test_calculate_area_square_string():  
    with pytest.raises(TypeError):  
        calculate_area_square("2")  
  
def test_calculate_area_square_list():  
    with pytest.raises(TypeError):  
        calculate_area_square([16])

def test_calculate_area_square_student_number():  
    
        input_value = 83**0.5 # Square root of 83
        expected_output = 16
        assert calculate_area_square(input_value) == expected_output, "The area calculation is incorrect"