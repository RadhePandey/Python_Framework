import pytest

from pages.verticals import vertical


@pytest.mark.smoke
def test_trading(page):

    verticals = vertical(page)
    verticals.trading_navigation()


def test_retails_and_ecommerce(page):

    verticals = vertical(page)
    verticals.retail_and_ecommerce_navigation()


def test_healthcare(page):

    verticals = vertical(page)
    verticals.healthcare_navigation()


def test_fintech(page):

    verticals = vertical(page)
    verticals.fintech_navigation()


def test_custom_app(page):

    verticals = vertical(page)
    verticals.custom_app_navigation()


    