from pytest import fixture
from sample_package.sample_module import Calculator


@fixture
def calculator():
    return Calculator()
