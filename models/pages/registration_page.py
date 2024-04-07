import os

from selene import browser, by


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
        if value == 'Female':
            browser.element('[for="gender-radio-2"]').click()
        else:
            browser.element('[for="gender-radio-1"]').click()
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
        if value == 'Sports':
            browser.element('[for=hobbies-checkbox-1]').click()
        elif value == 'Reading':
            browser.element('[for=hobbies-checkbox-2]').click()
        else:
            browser.element('[for=hobbies-checkbox-3]').click()
        return self

    def fill_upload_picture(self, path):
        browser.element('#uploadPicture').send_keys(os.path.abspath(path))
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


registration_page = RegistrationPage()
