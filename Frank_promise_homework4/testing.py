from unittest import TestCase, main
from homework4 import validate_cash_withdrawal
from homework4 import validate_pin_code


class TestForAmountAndPin(TestCase):
    def test_amount(self):
        expected = 1 >= 100
        result = validate_cash_withdrawal(amount=1000)

    def test_pin(self):
        expected = 12345
        result = validate_pin_code(number=1)


if __name__ == '__main__':
    main()