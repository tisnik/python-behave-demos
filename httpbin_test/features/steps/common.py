import json

from behave import given, then, when
from urllib.parse import urljoin
import requests


@given('API for httpbin.org is accessible')
def initial_state(context):
    assert context.is_accessible(context)


@when('I access the API endpoint {url}')
def access_endpoint(context, url):
    context.response = requests.get(context.api_url + url)


@then('I should receive {status:d} status code')
def check_status_code(context, status):
    """Check the HTTP status code returned by the REST API."""
    assert context.response.status_code == status
