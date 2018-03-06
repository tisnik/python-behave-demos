from behave import given, then, when


@given('The library {library_name} is loaded')
def initial_state(context, library_name):
    context.load_library(context, library_name)


@when('I call native function {function} with integer arguments {x:d} and {y:d}')
def call_add(context, function, x, y):
    context.result = getattr(context.tested_library, function)(x, y)


@then('I should get {result:d} as a result')
def check_integer_result(context, result):
    assert context.result == result
