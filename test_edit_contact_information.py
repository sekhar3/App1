import allure
from utils.browser_config import driver
from POM.BaseTest.upass_holder import RegBaseTest
from POM.Portal.upass_holder_app import HolderPortal
import logging
from utils.read_data import ReadData
LOGGER = logging.getLogger(__name__)

"""
@author        : Srinivas Reddy
Description    : This class is used to Edit User Contact Details
"""


class TestAccountDetails(RegBaseTest):
    upass_holder_portal = HolderPortal(driver)

    def test_edit_contact_info(self):
        with allure.step("Reading test data"):
            data = ReadData()
            test_data = data.get_test_data()
            excel_data = data.get_excel_data(2, 2)

        with allure.step("Clicking Continue button"):
            self.upass_holder_portal.upass_portal_page()

        with allure.step("Clicking on Login to existing account button"):
            self.upass_holder_portal.click_existing_account()

        with allure.step("Entering Username"):
            self.upass_holder_portal.enter_username(excel_data)

        with allure.step("Entering Password"):
            self.upass_holder_portal.enter_login_password(test_data["details"]["password"])

        with allure.step("Clicking Continue button to Signin"):
            self.upass_holder_portal.click_continue_signin()

        with allure.step("Clicking Profile button"):
            self.upass_holder_portal.click_profile_tab()

        with allure.step("Clicking Account Details button"):
            self.upass_holder_portal.click_account_details_tb()

        with allure.step("Clicking Edit button"):
            self.upass_holder_portal.click_contact_info_edit_btn()

        with allure.step("Entering Secondary Email"):
            self.upass_holder_portal.enter_secondary_email(test_data["details"]["secondary_email"])

        with allure.step("Clicking Save button"):
            self.upass_holder_portal.click_save_btn()
