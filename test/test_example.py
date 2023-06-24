import os
import unittest
import carbonate_sdk as carbonate
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select

class example_test(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)

        # This can be any browser supported by webdriver
        driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        self.browser = carbonate.WebDriver(driver)

    def setUp(self):
        self.carbonate_sdk = carbonate.SDK(
            browser=self.browser,
            cache_dir=os.path.join(os.path.splitext(__file__)[0]),
            # api_user_id="<your user ID>",  # TODO: Change me
            # api_key="<your api key>",  # TODO: Change me
        )

    @carbonate.test()
    def test_select_birthday_from_the_dropdown(self):
        self.carbonate_sdk.load(
            'https://carbonate.dev/test-form'
        )

        self.carbonate_sdk.action('select Birthday from the event type dropdown')

        self.assertTrue(
            self.carbonate_sdk.assertion('the event type dropdown should be set to Birthday')
        )

    @carbonate.test()
    def test_select_birthday_from_the_dropdown_advanced(self):
        self.carbonate_sdk.load(
            'https://carbonate.dev/test-form'
        )

        select = self.carbonate_sdk.lookup('the dropdown')
        Select(select).select_by_visible_text('Birthday')

        select = self.carbonate_sdk.lookup('the dropdown')
        self.assertEqual('Birthday', Select(select).first_selected_option.text)
