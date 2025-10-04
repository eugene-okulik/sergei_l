from playwright.sync_api import Page, expect, Route
import re
import json


def test_requests(page: Page):
    def route_handler(route: Route):
        response = route.fetch()
        body = response.json()
        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = 'яблокофон 17 про'
        body = json.dumps(body)
        route.fulfill(
            response=response,
            body=body
        )

    page.route(re.compile('digital-mat'), route_handler)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.get_by_role('heading', name='iPhone 17 Pro &').click()
    expect(page.locator('h2[data-autom="DigitalMat-overlay-header-0-0"]')).to_have_text('яблокофон 17 про')
