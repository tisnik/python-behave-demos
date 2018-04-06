from behave import given, then, when


@given(u'a list of integers')
def list_of_integers(context):
    numbers = []
    for row in context.table:
        numbers.append(int(row["value"]))
    context.numbers = numbers


@given(u'the following exchange rate table')
def exchange_rate_table_init(context):
    tbl = {}
    for row in context.table:
        currency = row["currency"]
        rate = float(row["rate"])
        tbl[currency] = rate
    context.exchange_rate_table = tbl


@when(u'I sell {sold} {currency}')
def step_impl(context, sold, currency):
    exchange_rate = context.exchange_rate_table[currency]
    context.result = exchange_rate * float(sold)


@then(u'I should receive {amount:g} CZK')
def step_impl(context, amount):
    assert isclose(context.result, amount, rel_tol=1e-5), \
        "Wrong result: {r} != {a}".format(r=context.result, a=amount)


def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)
