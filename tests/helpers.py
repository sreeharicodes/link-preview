from os.path import dirname, abspath, join

this_dir = dirname(abspath(__file__))
pages_dir = join(this_dir, "pages")


def get_page(path):
    with open(join(pages_dir, path), "r") as f:
        return f.read()