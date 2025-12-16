import pytest
from calculator import Calculator

class TestCalculator:
    def setup_method(self):
        self.calculator = Calculator()

    def test_add(self):
        assert self.calculator.add(2, 3) == 5

    
    def test_add_negative(self):
        assert self.calculator.add(-1, 1) == 0

    def test_subtract(self):
        assert self.calculator.subtract(5, 3) == 2
    
    '''
    def test_subtract_negative(self):
        assert self.calculator.subtract(0, 4) == -4

    def test_multiply(self):
        assert self.calculator.multiply(2, 3) == 6

    def test_multiply_negative(self):
        assert self.calculator.multiply(-1, 5) == -5

    def test_divide(self):
        assert self.calculator.divide(6, 3) == 2

    def test_divide_by_zero(self):
        with pytest.raises(ValueError):
            self.calculator.divide(5, 0)
    '''