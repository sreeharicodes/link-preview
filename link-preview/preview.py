import requests
from bs4 import BeautifulSoup
from .helper_utils import is_image_accessible


def get_soup(url):
    # https://andrejgajdos.com/how-to-hire-a-freelance-front-end-developer/
    source = requests.get(url)
    source.raise_for_status()
    soup = BeautifulSoup(source.content, "html.parser")
    return soup


def get_title(soup):
    # Open graph protocol
    og_title = soup.find("meta", property="og:title")
    if og_title:
        return og_title.get("content")
    # Twitter card
    twitter_title = soup.find("meta", attrs={"name": "twitter:title"})
    if twitter_title:
        return twitter_title.get("content")
    # Title of the webpage
    page_title = soup.title
    if page_title:
        return page_title.string
    # Check for h1 tags
    h1_title = soup.find("h1")
    if h1_title:
        return h1_title.string
    # Check for h2 tags
    h2_title = soup.find("h2")
    if h2_title:
        return h2_title.string

    return None


def get_description(soup):
    # Open graph protocol
    og_description = soup.find("meta", property="og:description")
    if og_description:
        return og_description.get("content")
    # Twitter card
    twitter_description = soup.find("meta", attrs={"name": "twitter:description"})
    if twitter_description:
        return twitter_description.get("content")
    # Description of the webpage
    page_description = soup.find("meta", attrs={"name": "description"})
    if page_description:
        return page_description.get("content")
    # Check for p tags
    p_tag = soup.find("p")
    if p_tag:
        return p_tag.string

    return None


def get_domain(soup):
    # From <link rel="canonical">
    link = soup.find("link", attrs={"rel": "canonical"})
    if link:
        return link.get("href")
    # From og:url
    og_url = soup.find("meta", property="og:url")
    if og_url:
        return og_url.get("content")

    return None


def get_image(soup):
    # Open graph
    og_image = soup.find("meta", property="og:image")
    if og_image:
        link = og_image.get("content")
        if link and is_image_accessible(link):
            return link
    # Twitter image
    twitter_image = soup.find("meta", attrs={"name": "twitter:image"})
    if twitter_image:
        link = twitter_image.get("content")
        if link and is_image_accessible(link):
            return link
    # <link rel="image_src">
    image_link = soup.find("link", attrs={"rel": "image_src"})
    if image_link:
        link = image_link.get("href")
        if link and is_image_accessible(link):
            return link
    # Check for img element with src
    image_tag = soup.find("img", src=True)
    if image_tag:
        link = image_link.get("src")
        if link and is_image_accessible(link):
            return link

    return None
