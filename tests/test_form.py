from models.pages.registration_page import registration_page
from models.user import liza


def test_success_submit():
    registration_page.open()

    registration_page.register(liza)

    registration_page.should_have_registered(liza)
