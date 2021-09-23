import requests
import re
from requests.exceptions import MissingSchema


def is_image_accessible(link):
    try:
        source = requests.get(link)
        source.raise_for_status()
    except (requests.HTTPError, MissingSchema):
        return False
    content_type = source.headers.get("Content-Type", None)
    if content_type and re.match('image/*', content_type):
        return True
    return False
