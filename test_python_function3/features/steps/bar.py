from behave import given, then, when
from src.adder import add


@when('I call function {function} with arguments {x:d} and {y:d}')
def call_add(context, function, x, y):
    context.result = add(x, y)
