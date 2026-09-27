import pytest

from pages.technologies import technology


@pytest.mark.smoke
def test_ecommerce_development(page):

    technologies = technology(page)

    technologies.ecommerce_development_navigation()


def test_mobile_app_development(page):

    technologies = technology(page)

    technologies.mobile_app_development_navigation()


def test_artificial_intelligence(page):

    technologies = technology(page)

    technologies.artificial_intelligence_navigation()