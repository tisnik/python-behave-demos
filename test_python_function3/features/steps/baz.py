from behave import given, then, when
from src.adder import add


@then('I should get {expected:d} as a result')
def check_integer_result(context, expected):
    assert context.result == expected, \
        "Wrong result: {r} != {e}".format(r=context.result, e=expected)
