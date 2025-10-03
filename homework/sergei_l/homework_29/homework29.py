from playwright.sync_api import Page, expect, BrowserContext


def test_alert(page: Page):
    page.on('dialog', lambda alert: alert.accept())
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.locator('.a-button').click()
    expect(page.locator('#result-text')).to_have_text('Ok')


def test_new_tab(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    button = page.locator('#new-page-button')
    with context.expect_page() as new_tab_event:
        button.click()
    new_tab = new_tab_event.value
    expect(new_tab.locator('#result-text')).to_have_text('I am a new page in a new tab')
    expect(button).to_be_enabled()


def test_color(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    expect(page.locator('#colorChange')).to_have_css('color', 'rgb(220, 53, 69)')
    page.locator('#colorChange').click()
