from behave import given, then, when
from src.adder import add


@given('The function {function_name} is callable')
def initial_state(context, function_name):
    pass
