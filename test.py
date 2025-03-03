import pytest

from app.calc import Calculator

class TestCalc:
    def setup (self):
        self.calc = Calculator


    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_division_success(self):
        assert self.calc.division(self,8,4) == 2

    def test_multiplication_success(self):
        assert self.calc.multiply(self,6,2) == 12

    def test_subtract_success(self):
        assert  self.calc.subtraction(self,10,5)== 5

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)



    def teardown(self):
        print('Выполнение метода Teardown')