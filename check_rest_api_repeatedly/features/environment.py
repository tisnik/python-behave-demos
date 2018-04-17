import json
import os.path

from behave.log_capture import capture
import requests


def _is_accessible(context, accepted_codes=None):
    accepted_codes = accepted_codes or {200, 401}
    url = context.api_url
    try:
        res = requests.get(url)
        return res.status_code in accepted_codes
    except requests.exceptions.ConnectionError as e:
        print("Connection error: {e}".format(e=e))
    return False


def before_all(context):
    """Perform setup before the first event."""
    context.is_accessible = _is_accessible
    context.api_url = "https://httpbin.org/"
