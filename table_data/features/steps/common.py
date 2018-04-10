from behave import given, then, when

# import testovane funkce
from src.sum import sum


@given(u'a list of integers')
def list_of_integers(context):
    # seznam, do ktereho se ulozi hodnoty z tabulky
    numbers = []

    # iterace pres radky tabulky
    for row in context.table:
        # ziskani hodnoty ze sloupce "value" a prevod na int
        numbers.append(int(row["value"]))

    # zapamatovani hodnot
    context.numbers = numbers


@when(u'I summarize all those integers')
def step_impl(context):
    """Zavolani testovane funkce."""
    context.result = sum(context.numbers)


@then('I should get {expected:d} as a result')
def check_integer_result(context, expected):
    """Porovnani vypocteneho vysledku s vysledkem ocekavanym."""
    assert context.result == expected, \
        "Wrong result: {r} != {e}".format(r=context.result, e=expected)
