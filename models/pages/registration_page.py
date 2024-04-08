import os

from config import FILES_DIR
from models.user import User, Hobby, Gender
from selene import browser, by, have


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')
        return self

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)
        return self

    def fill_user_email(self, value):
        browser.element('#userEmail').type(value)
        return self

    def fill_gender(self, value):
        if value == Gender.female:
            browser.element('[for="gender-radio-2"]').click()
        elif value == Gender.male:
            browser.element('[for="gender-radio-1"]').click()
        elif value == Gender.other:
            browser.element('[for="gender-radio-3"]').click()
        return self

    def fill_user_number(self, value):
        browser.element('#userNumber').type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click().element(by.text(month)).click()
        browser.element('.react-datepicker__year-select').click().element(by.text(year)).click()
        browser.element(f'.react-datepicker__day--0{day}').click()
        return self

    def fill_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()
        return self

    def fill_hobbies(self, value):
        if value == Hobby.sports:
            browser.element('[for=hobbies-checkbox-1]').click()
        elif value == Hobby.reading:
            browser.element('[for=hobbies-checkbox-2]').click()
        elif value == Hobby.music:
            browser.element('[for=hobbies-checkbox-3]').click()
        return self

    def fill_upload_picture(self, filename):
        browser.element('#uploadPicture').send_keys(os.path.join(FILES_DIR, filename))
        return self

    def fill_current_address(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def fill_state(self, value):
        browser.element('#state').click().element(by.text(value)).click()
        return self

    def fill_city(self, value):
        browser.element('#city').click().element(by.text(value)).click()
        return self

    def submit(self):
        browser.element('#submit').click()
        return self

    @property
    def modal_header(self):
        return browser.element('.modal-header')

    @property
    def form_table(self):
        return browser.element('.table').all('td').even

    def register(self, user: User):
        (self.fill_first_name(user.first_name)
         .fill_last_name(user.last_name)
         .fill_user_email(user.user_email)
         .fill_gender(user.gender)
         .fill_user_number(user.user_number)
         .fill_date_of_birth(user.birth_year, user.birth_month, user.birth_day)
         .fill_subjects(user.subject.value)
         .fill_hobbies(user.hobby)
         .fill_upload_picture(user.picture)
         .fill_current_address(user.address)
         .fill_state(user.state)
         .fill_city(user.city)
         .submit()
         )

    def should_have_registered(self, user: User):
        self.modal_header.should(have.text("Thanks for submitting the form"))

        self.form_table.should(have.exact_texts(
            f'{user.first_name} {user.last_name}',
            user.user_email,
            user.gender.value,
            user.user_number,
            f'{user.birth_day} {user.birth_month},{user.birth_year}',
            user.subject.value,
            user.hobby.value,
            os.path.basename(user.picture),
            user.address,
            f'{user.state} {user.city}'
        )
        )


registration_page = RegistrationPage()
