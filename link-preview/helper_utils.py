import requests
import re


def is_image_accessible(link):
    source = requests.get(link)
    source.raise_for_status()
    content_type = source.headers.get("Content-Type", None)
    if content_type and re.match('image/*', content_type):
        return True
    return False
