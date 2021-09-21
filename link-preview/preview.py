import requests
from bs4 import BeautifulSoup


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
        return og_title.get('content')
    # Twitter card
    twitter_title = soup.find("meta", name="twitter:title")
    if twitter_title:
        return twitter_title.get('content')
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
        return og_description.get('content')
    # Twitter card
    twitter_description = soup.find("meta", name="twitter:description")
    if twitter_description:
        return twitter_description.get('content')
    # Description of the webpage
    page_description = soup.find("meta", name="description")
    if page_description:
        return page_description.get('content')
    # Check for p tags
    p_tag = soup.find("p")
    if p_tag:
        return p_tag.string

    return None
