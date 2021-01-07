
def test_add(calculator):
    """
    Testing if Addition is calculated correctly
    """

    result = calculator.add(10, 20)
    assert result == 30, "Incorrect calculations!!"


def test_sub(calculator):
    """
    Testing if Addition is calculated correctly
    """

    result = calculator.sub(20, 10)
    assert result == 10, "Incorrect calculations!!"


def test_mul(calculator):
    """
    Testing if Addition is calculated correctly
    """

    result = calculator.mul(10, 20)
    assert result == 200, "Incorrect calculations!!"


def test_div(calculator):
    """
    Testing if Addition is calculated correctly
    """

    result = calculator.div(10, 20)
    assert result == 0.5, "Incorrect calculations!!"
