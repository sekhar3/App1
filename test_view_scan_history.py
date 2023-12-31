import allure
from POM.Portal.upass_holder_app import HolderPortal
from utils.browser_config import driver
from utils.read_data import ReadData
from POM.BaseTest.upass_holder import RegBaseTest
import logging

LOGGER = logging.getLogger(__name__)
"""
    @author             : Somasekhar
    Description         : This method is used to view scan history
"""


class TestViewScanHistory(RegBaseTest):
    upass_holder_portal = HolderPortal(driver)

    def test_view_scan_history(self):
        with allure.step("Reading test data"):
            data = ReadData()
            test_data = data.get_test_data()
            excel_data = data.get_excel_data(2, 2)

        with allure.step("Entered in login page"):
            self.upass_holder_portal.upass_portal_page()
            LOGGER.info("Entered in login page")

        with allure.step("Clicking on Login to existing account button"):
            self.upass_holder_portal.click_existing_account()

        with allure.step("Entering Username"):
            self.upass_holder_portal.enter_username(excel_data)

        with allure.step("Entering Password"):
            self.upass_holder_portal.enter_login_password(test_data["Login"]["Password"])

        with allure.step("Clicking Continue button to Signin"):
            self.upass_holder_portal.click_continue_signin()

        with allure.step("Clicking hamburger icon"):
            self.upass_holder_portal.click_hamburger_icon()
            LOGGER.info("Click hamburger icon successfully")

        with allure.step("Clicking view scan history"):
            self.upass_holder_portal.click_view_scan_history()
            LOGGER.info("Click view scan history")
