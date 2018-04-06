from behave import given, then, when
from src.sum import sum


@given(u'a list of integers')
def list_of_integers(context):
    numbers = []
    for row in context.table:
        numbers.append(int(row["value"]))
    context.numbers = numbers


@when(u'I summarize all those integers')
def step_impl(context):
    context.result = sum(context.numbers)


@then('I should get {expected:d} as a result')
def check_integer_result(context, expected):
    assert context.result == expected, \
        "Wrong result: {r} != {e}".format(r=context.result, e=expected)
