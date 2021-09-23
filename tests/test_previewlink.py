import pytest
from previewlink import preview_link
from pytest_httpserver import HTTPServer
from tests.helpers import get_page
from previewlink.helper_utils import is_image_accessible
from werkzeug.wrappers.response import Response


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (
            "opengraph.html",
            {
                "title": "sreehari1997 - Overview", 
                "description": "Developer. sreehari1997 has 69 repositories available.", 
                "domain": "github.com",
                "image": "https://avatars.githubusercontent.com/u/22663556?v=4?s=400"
            }
        ),
        (
            "twitter.html",
            {
                "title": "sreehari1997 - Overview", 
                "description": "Developer. sreehari1997 has 69 repositories available.", 
                "domain": None,
                "image": "https://avatars.githubusercontent.com/u/22663556?v=4?s=400"
            }
        ),
        (
            "generic_1.html",
            {
                "title": "sreehari1997 - Overview", 
                "description": "Developer. sreehari1997 has 69 repositories available.", 
                "domain": "github.com",
                "image": "https://avatars.githubusercontent.com/u/22663556?v=4?s=400"
            }
        ),
        (
            "generic_2.html",
            {
                "title": "sreehari1997 - Overview", 
                "description": "Developer. sreehari1997 has 69 repositories available.", 
                "domain": None,
                "image": "https://avatars.githubusercontent.com/u/22663556?v=4?s=400"
            }
        ),
        (
            "generic_3.html",
            {
                "title": "sreehari1997 - Overview", 
                "description": None, 
                "domain": None,
                "image": None
            }
        )
    ]
)
def test_previewlink(test_input, expected, httpserver: HTTPServer):
    page = get_page(test_input)
    httpserver.expect_request("/test").respond_with_data(
        page, headers={"Content-Type": "text/html"}
    )
    preview = preview_link(httpserver.url_for("/test"))
    for key, value in preview.items():
        assert value == expected[key]


def test_invalid_content_type(httpserver: HTTPServer):
    page = get_page("twitter.html")
    httpserver.expect_request("/invalid").respond_with_data(
        page, headers={"Content-Type": "image/png"}
    )
    preview = preview_link(httpserver.url_for("/invalid"))
    for _, value in preview.items():
        assert value == None


def test_image_accessible(httpserver: HTTPServer):
    page = get_page("twitter.html")
    httpserver.expect_request("/invalid").respond_with_data(
        page, headers={"Content-Type": "text/html"}
    )
    is_accessible = is_image_accessible(httpserver.url_for("/invalid"))
    assert is_accessible == False


def test_large_content_size(httpserver: HTTPServer):
    class LargeResponse(Response):
        automatically_set_content_length = False

    httpserver.expect_request("/large").respond_with_response(
        LargeResponse(
            mimetype='text/html',
            headers={"Content-Length": "2000000"}
        )
    )
    preview = preview_link(httpserver.url_for("/large"))
    for _, value in preview.items():
        assert value == None


def test_invalid_url(httpserver: HTTPServer):
    page = get_page("twitter.html")
    httpserver.expect_request("/twitter").respond_with_data(
        page, headers={"Content-Type": "text/html"}
    )
    preview = preview_link(httpserver.url_for("/invalid"))
    for _, value in preview.items():
        assert value == None


def test_no_content_type(httpserver: HTTPServer):
    httpserver.expect_request("/invalid").respond_with_response(
        Response(
            mimetype=""
        )
    )
    preview = preview_link(httpserver.url_for("/invalid"))
    for _, value in preview.items():
        assert value == None


def test_invalid_image_url(httpserver: HTTPServer):
    is_accessible = is_image_accessible("img/profile.jpg")
    assert is_accessible == False
