import json
import os.path

from behave.log_capture import capture
import requests


def _is_accessible(context, accepted_codes=None):
    accepted_codes = accepted_codes or {200, 401}
    url = context.api_url
    try:
        res = requests.get(url)
        if res.status_code in accepted_codes:
            return True
    except requests.exceptions.ConnectionError:
        pass
    return False


def before_all(context):
    context.is_accessible = _is_accessible
    context.api_url = "https://api.github.com"
