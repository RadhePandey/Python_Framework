import pytest

from pages.blog import blog


@pytest.mark.smoke
def test_blog(page):

    blogs = blog(page)

    blogs.blog_navigation()