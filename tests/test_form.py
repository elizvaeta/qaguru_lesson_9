from models.pages.registration_page import registration_page
from selene import have


def test_success_submit():
    registration_page.open()

    (registration_page
     .fill_first_name('Elizaveta')
     .fill_last_name('Kazova')
     .fill_user_email('test@test.com')
     .fill_gender('Female')
     .fill_user_number('9997776655')
     .fill_date_of_birth('1999', 'September', '07')
     .fill_subjects('Maths')
     .fill_hobbies('Music')
     .fill_upload_picture('../files/test.jpg')
     .fill_current_address('Russia')
     .fill_state('Haryana')
     .fill_city('Karnal')
     .submit()
     )

    registration_page.modal_header.should(have.text("Thanks for submitting the form"))

    registration_page.form_table.should(have.exact_texts(
        'Elizaveta Kazova',
        'test@test.com',
        'Female',
        '9997776655',
        '07 September,1999',
        'Maths',
        'Music',
        'test.jpg',
        'Russia',
        'Haryana Karnal'
    )
    )
