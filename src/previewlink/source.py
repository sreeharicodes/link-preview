import requests
from bs4 import BeautifulSoup
from urllib.parse import  urlparse
from .helper_utils import is_image_accessible

from .exceptions import (
    InvalidContentError,
    InvalidMimeTypeError,
    MaximumContentSizeError
)


class PageSource:
    def __init__(self, url, max_size=1048576):
        self.url = url
        self.max_size = max_size
    
    def get_soup(self):
        try:
            request = requests.get(self.url)
            request.raise_for_status()
        except requests.HTTPError:
            return BeautifulSoup()

        content_type = request.headers.get("Content-Type")
        if not content_type:
            raise InvalidContentError("Invalid content type")
        
        mimetype = content_type.split(";")[0].lower()
        if mimetype != "text/html":
            raise InvalidMimeTypeError("Invalid mime type")

        response_length = request.headers.get("Content-Length")
        if response_length and int(response_length) > self.max_size:
            raise MaximumContentSizeError("Content exceeded 1MB")

        soup = BeautifulSoup(request.content, "html.parser")

        return soup


class PreviewLink:
    def __init__(self, soup):
        self.soup = soup

    @property
    def title(self):
        # Open graph protocol
        og_title = self.soup.find("meta", property="og:title")
        if og_title:
            return og_title.get("content")
        # Twitter card
        twitter_title = self.soup.find(
            "meta", attrs={"name": "twitter:title"}
        )
        if twitter_title:
            return twitter_title.get("content")
        # Title of the webpage
        page_title = self.soup.title
        if page_title:
            return page_title.string
        # Check for h1 tags
        h1_title = self.soup.find("h1")
        if h1_title:
            return h1_title.string
        # Check for h2 tags
        h2_title = self.soup.find("h2")
        if h2_title:
            return h2_title.string

        return None

    @property
    def description(self):
        # Open graph protocol
        og_description = self.soup.find("meta", property="og:description")
        if og_description:
            return og_description.get("content")
        # Twitter card
        twitter_description = self.soup.find(
            "meta", attrs={"name": "twitter:description"}
        )
        if twitter_description:
            return twitter_description.get("content")
        # Description of the webpage
        page_description = self.soup.find(
            "meta", attrs={"name": "description"}
        )
        if page_description:
            return page_description.get("content")
        # Check for p tags
        p_tag = self.soup.find("p")
        if p_tag:
            return p_tag.string

        return None

    @property
    def domain(self):
        # From <link rel="canonical">
        link = self.soup.find("link", attrs={"rel": "canonical"})
        if link:
            url = link.get("href")
            if url:
                return urlparse(url).netloc
        # From og:url
        og_url = self.soup.find("meta", property="og:url")
        if og_url:
            url = og_url.get("content")
            if url:
                return urlparse(url).netloc

        return None

    @property
    def image(self):
        # Open graph
        og_image = self.soup.find("meta", property="og:image")
        if og_image:
            link = og_image.get("content")
            if link and is_image_accessible(link):
                return link
        # Twitter image
        twitter_image = self.soup.find(
            "meta", attrs={"name": "twitter:image"}
        )
        if twitter_image:
            link = twitter_image.get("content")
            if link and is_image_accessible(link):
                return link
        # <link rel="image_src">
        image_link = self.soup.find("link", attrs={"rel": "image_src"})
        if image_link:
            link = image_link.get("href")
            if link and is_image_accessible(link):
                return link
        # Check for img element with src
        image_tag = self.soup.find("img", src=True)
        if image_tag:
            link = image_tag.get("src")
            if link and is_image_accessible(link):
                return link

        return None

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "domain": self.domain,
            "image": self.image
        }