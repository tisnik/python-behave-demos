from behave import given, then, when
from src.adder import add


@given('The function {function_name} is callable')
def initial_state(context, function_name):
    g = globals()
    assert function_name in g, "Function is not visible"
    assert callable(g[function_name]), "Not a function"


@when('I call function {function} with arguments {x:d} and {y:d}')
def call_add(context, function, x, y):
    context.result = add(x, y)


@then('I should get {expected:d} as a result')
def check_integer_result(context, expected):
    assert context.result == expected, \
        "Wrong result: {r} != {e}".format(r=context.result, e=expected)
