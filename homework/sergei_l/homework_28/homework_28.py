from playwright.sync_api import Page


def test_form_fill(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    page.get_by_role('link', name='Form Authentication').click()
    page.get_by_role('textbox', name='username').fill('test_user')
    page.get_by_role('textbox', name='password').fill('strongpassword')
    page.get_by_role('button').click()


def test_second_form_fill(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')
    page.locator('#firstName').fill('test first name')
    page.locator('#lastName').fill('test last name')
    page.locator('#userEmail').fill('test@email.fun')
    page.locator('.custom-control.custom-radio').nth(0).click()
    page.locator('#userNumber').fill('1232343455')
    page.locator('#dateOfBirthInput').click()
    page.locator('.react-datepicker__year-select').select_option('1996')
    page.locator('.react-datepicker__month-select').select_option('2')
    page.locator('.react-datepicker__day--012').nth(0).click()

    subjects_list = ['English', 'Physics', 'Arts']
    form_subjects = page.locator('#subjectsInput')
    for subject in subjects_list:
        form_subjects.press_sequentially(subject, delay=100)
        form_subjects.press('Enter')

    page.locator('.custom-control-label[for="hobbies-checkbox-2"]').click()
    page.locator('#currentAddress').fill('Better place palace, 29/3')
    form_state = page.locator('#react-select-3-input')
    form_state.press_sequentially('ncr', delay=100)
    form_state.press('Enter')
    form_city = page.locator('#react-select-4-input')
    form_city.press_sequentially('delhi', delay=100)
    form_city.press('Enter')
    page.locator('#submit').click()
