import unittest
import random
from utils.driver import create_driver
from pages.home_page import HomePage
from pages.terms_conditions_page import TermsConditionsPage
from pages.finish_page import FinishPage
from pages.quit_page import QuitPage

class TestScenario(unittest.TestCase):
    def setUp(self):
        self.driver = create_driver()
        self.home_page = HomePage(self.driver)
        self.terms_page = TermsConditionsPage(self.driver)
        self.quit_page = QuitPage(self.driver)
        self.finish_page = FinishPage(self.driver)

    def test_scenario(self):
        # Step a: Launch the application and validate home screen
        self.assertTrue(self.home_page.is_displayed())

        # Step a: Launch the application and validate home screen
        self.assertTrue(self.home_page.input_id_is_displayed())
        self.assertTrue(self.home_page.start_button_is_displayed())

        # Step c: Enter ident ID and click start
        ident_ids = ['TST-FUFMT', 'TST-QJUVC', 'TST-NWSMW']
        random_ident_id = random.choice(ident_ids)
        self.home_page.enter_ident_id(random_ident_id)
        self.home_page.click_start_ident()

        # Step d: Validate terms and conditions screen is displayed
        self.assertTrue(self.terms_page.is_displayed())

        # Step e: Click on close icon
        self.terms_page.click_close()

        # Step f and g: Validate options with reasons and choose any option
        expected_reasons = ["I don’t have my document with me",
                            "I have privacy concerns",
                            "The app is not responding and I cannot go further",
                            "Not interested in the service for which this identification is required",
                            "I will complete the identification later"]
        actual_reasons = self.quit_page.get_reasons_text()
        self.assertEqual(actual_reasons, expected_reasons, "The reasons list does not match the expected values.")

        self.quit_page.choose_option_and_quit("I have privacy concerns")

        # Step h: Validate intermediate screen
        self.assertTrue(self.finish_page.is_displayed())
        self.assertTrue(self.home_page.is_displayed())
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
