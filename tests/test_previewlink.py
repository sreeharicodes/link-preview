import pytest
from previewlink import preview_link
from pytest_httpserver import HTTPServer
from tests.helpers import get_page


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
def test_opengraph(test_input, expected, httpserver: HTTPServer):
    page = get_page(test_input)
    httpserver.expect_request("/test").respond_with_data(
        page, headers={"content-type": "text/html"}
    )
    preview = preview_link(httpserver.url_for("/test"))
    for key, value in preview.items():
        assert value == expected[key]