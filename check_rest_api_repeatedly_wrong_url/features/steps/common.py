import json
import time

from behave import given, then, when
from urllib.parse import urljoin
import requests


@given('REST API service is accessible')
def initial_state(context):
    assert context.is_accessible(context)


@when('I access the API endpoint {url:S}')
def access_endpoint(context, url):
    context.response = requests.get(context.api_url + url)


@when('I access the API endpoint {url} {repeat_count:d} times with {delay:d} seconds delay')
def access_url_repeatedly(context, url, repeat_count, delay):
    context.api_call_results = []
    url = context.api_url + url
    # repeatedly call REST API endpoint and collect HTTP status codes
    for i in range(repeat_count):
        response = requests.get(url)
        context.api_call_results.append(response.status_code)
        time.sleep(delay)


@then('I should receive {status:d} status code')
def check_status_code(context, status):
    """Check the HTTP status code returned by the REST API."""
    assert context.response.status_code == status


@then('I should get {status:d} status code for all calls')
def check_status_code_for_all_calls(context, status):
    """Check the HTTP status codes returned by the REST API."""
    wrong_calls = [code for code in context.api_call_results if code != status]
    assert not wrong_calls, \
        "Wrong code returned {n} times: {codes}".format(n=len(wrong_calls), codes=wrong_calls)
