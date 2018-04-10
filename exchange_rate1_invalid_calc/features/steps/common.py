from behave import given, then, when


@given(u'the following exchange rate table')
def exchange_rate_table_init(context):
    # slovnik do ktereho se ulozi smenne kurzy
    tbl = {}

    # iterace pres vsechny radky tabulky v kroku Given
    for row in context.table:
        # nacist kod meny a aktualni kurz
        currency = row["currency"]
        rate = float(row["rate"])
        # ulozit do slovniku
        tbl[currency] = rate

    # slovnik se stane soucasti testovaciho kontextu
    context.exchange_rate_table = tbl


@when(u'I sell {sold} {currency}')
def step_impl(context, sold, currency):
    """Vypocet na zaklade smenneho kurzu."""
    exchange_rate = context.exchange_rate_table[currency]
    context.result = exchange_rate * float(sold) * 2


@then(u'I should receive {amount:g} CZK')
def step_impl(context, amount):
    """Porovnani vypocteneho vysledku s vysledkem ocekavanym."""
    assert isclose(context.result, amount, rel_tol=1e-5), \
        "Wrong result: {r} != {a}".format(r=context.result, a=amount)


def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    """Pomocna funkce pro porovnani dvou cisel s plovouci radovou carkou."""
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)
