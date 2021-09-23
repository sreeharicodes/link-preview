from bs4 import BeautifulSoup

from previewlink import (
    PreviewLink,
    PageSource
)
from previewlink.exceptions import PreviewLinkException


def preview_link(url):
    try:
        source = PageSource(url)
        soup = source.get_soup()
    except PreviewLinkException:
        soup = BeautifulSoup()

    preview = PreviewLink(soup)
    return preview.to_dict()
