import os
import unittest
import carbonate_sdk
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select

class example_test(unittest.TestCase):
    browser = None
    carbonate = None

    @classmethod
    def setUpClass(cls) -> None:
        # This can be any browser supported by webdriver
        driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        cls.browser = carbonate_sdk.WebDriver(driver)
        cls.carbonate = carbonate_sdk.SDK(
            browser=cls.browser,
            cache_dir=os.path.join(os.path.splitext(__file__)[0]),
            # api_user_id="<your user ID>",  # TODO: Change me
            # api_key="<your api key>",  # TODO: Change me
        )

    @carbonate_sdk.test("carbonate")
    def test_select_birthday_from_the_dropdown(self):
        self.carbonate.load(
            'https://carbonate.dev/demo-form'
        )

        self.carbonate.action('select Birthday from the event type dropdown')

        self.assertTrue(
            self.carbonate.assertion('the event type dropdown should be set to Birthday')
        )

    @carbonate_sdk.test("carbonate")
    def test_select_birthday_from_the_dropdown_advanced(self):
        self.carbonate.load(
            'https://carbonate.dev/demo-form'
        )

        select = self.carbonate.lookup('the event type dropdown')
        Select(select).select_by_visible_text('Birthday')

        self.assertEqual('Birthday', Select(select).first_selected_option.text)
