# Preview Link

[![Build Status](
    https://app.travis-ci.com/sreehari1997/link-preview.svg?branch=master
)](
    https://app.travis-ci.com/sreehari1997/link-preview
)
[![Coverage Status](
    https://coveralls.io/repos/github/sreehari1997/link-preview/badge.svg?branch=HEAD
)](
    https://coveralls.io/github/sreehari1997/link-preview?branch=HEAD
)
[![Downloads](
    https://pepy.tech/badge/previewlink
)](
    https://pepy.tech/project/previewlink
)

You may have seen a preview of a link with a title, image, domain, and description when you share a link on social media.

![alt text](https://github.com/sreehari1997/link-preview/blob/master/preview.png?raw=true)

This preview has a significant impact on the user's decision to click on or not click on that link.
previewlink will help you to get the preview of a link.

[PyPI](https://pypi.org/project/previewlink/)

## How it works?

previewlink looks for the following tags in the page source
- [Open graph protocol](https://ogp.me/)
- [Twitter cards](https://developer.twitter.com/en/docs/twitter-for-websites/cards/guides/getting-started)
- HTML tags (title, p, img, h1, h2)

## Installation

Run the following to install

```python
pip install previewlink
```
## Usage

```python
>>> from previewlink import preview_link
>>> # Generate link preview
>>> preview_link("https://github.com/sreehari1997")
{
    'title': 'sreehari1997 - Overview',
    'description': 'Developer. sreehari1997 has 69 repositories available. Follow their code on GitHub.',
    'domain': 'github.com',
    'image': 'https://avatars.githubusercontent.com/u/22663556?v=4?s=400'
}
```

## Developing previewlink

To install previewlink, along with the tools you need to develop and run tests,
run the following in your virtual env

```shell
$ pip install -e .[dev]
```
