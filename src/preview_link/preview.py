from source import (
    PageSource,
    PreviewLink
)


def preview_link(url):
    source = PageSource(url)
    soup = source.get_soup()
    preview = PreviewLink(soup)
    return preview.to_dict()