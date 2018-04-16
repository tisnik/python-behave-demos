from behave import given, then, when

# import testovane funkce
from src.count_words import count_words


@given(u'a sample text')
def a_sample_text(context):
    assert context.text
    context.input = context.text


@when(u'I count all words in text')
def step_impl(context):
    """Zavolani testovane funkce."""
    context.result = count_words(context.input)


@then('I should get {expected:d} as a result')
def check_result(context, expected):
    """Porovnani vypocteneho vysledku s vysledkem ocekavanym."""
    assert context.result == expected, \
        "Wrong result: {r} != {e}".format(r=context.result, e=expected)
