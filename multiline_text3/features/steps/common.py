from behave import given, then, when

# import testovane funkce
from src.to_uppercase import to_uppercase


@given(u'a sample text')
def a_sample_text(context):
    assert context.text
    context.input = context.text


@when(u'I translate the text to upper case')
def step_impl(context):
    """Zavolani testovane funkce."""
    context.result = to_uppercase(context.input)


@then('I should get the following text as a result')
def check_result(context):
    """Porovnani vypocteneho vysledku s vysledkem ocekavanym."""
    assert context.result == context.text, \
        "Wrong result: {r} != {e}".format(r=context.result, e=context.text)
