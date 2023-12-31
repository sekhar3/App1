
import allure
from utils.browser_config import driver
from POM.BaseTest.upass_holder import RegBaseTest
from POM.Portal.upass_holder_app import HolderPortal
import logging
from utils.read_data import ReadData

LOGGER = logging.getLogger(__name__)

"""
@author        : Srinivas Reddy
Description    : This class is used to enable sms notifications 
"""


class TestNotificationPreferences(RegBaseTest):
    upass_holder_portal = HolderPortal(driver)

    def test_enable_sms_notifications(self):
        with allure.step("Reading test data"):
            data = ReadData()
            test_data = data.get_test_data()
            excel_data = data.get_excel_data(2, 2)

        with allure.step("Login to U-Pass Page"):
            self.upass_holder_portal.upass_portal_page()

        with allure.step("Clicking on Login to existing account button"):
            self.upass_holder_portal.click_existing_account()

        with allure.step("Entering Username"):
            self.upass_holder_portal.enter_username(excel_data)

        with allure.step("Entering Password"):
            self.upass_holder_portal.enter_login_password(test_data["Login"]["Password"])

        with allure.step("Clicking Continue button to Signin"):
            self.upass_holder_portal.click_continue_signin()

        with allure.step("Clicking Profile button"):
            self.upass_holder_portal.click_profile_tab()

        with allure.step("Clicking Notification Preferences button"):
            self.upass_holder_portal.click_notification_preferences()

        with allure.step("Clicking SMS toggle bar for Enabling notifications"):
            self.upass_holder_portal.click_enable_sms_notifications()

        with allure.step("Clicking Save button"):
            self.upass_holder_portal.click_save_btn()

        with allure.step("Verifying Success Notification Message"):
            self.upass_holder_portal.verify_success_notification()