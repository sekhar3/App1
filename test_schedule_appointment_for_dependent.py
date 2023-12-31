import time

import allure
from utils.browser_config import driver
from POM.BaseTest.upass_holder import RegBaseTest
from POM.Portal.upass_holder_app import HolderPortal
import logging
from utils.read_data import ReadData
import pytest
LOGGER = logging.getLogger(__name__)

"""
    @author             : Sreenivas Reddy
    Description         : This method is used to schedule an appointment service category medical test
"""


class TestScheduleAppointment(RegBaseTest):
    upass_holder_portal = HolderPortal(driver)

    def test_dependent_schedule_appointment(self):
        with allure.step("Reading test data"):
            data = ReadData()
            test_data = data.get_test_data()
            excel_data = data.get_excel_data(2, 2)

        with allure.step("Entering in login page"):
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

        with allure.step("Clicking get care button"):
            self.upass_holder_portal.click_get_care()

        with allure.step("Clicking the appointments"):
            self.upass_holder_portal.click_appointments()

        with allure.step("Clicking the appointments"):
            self.upass_holder_portal.click_dependent_scheduled_appointment()

        with allure.step("Selecting service category"):
            self.upass_holder_portal.select_service_category_medical()

        with allure.step("Selecting service type"):
            self.upass_holder_portal.select_service_type_antibody()

        with allure.step("Selecting Issuer Type CVS Pharmacy"):
            self.upass_holder_portal.select_issuer_cvs_pharmacy()

        with allure.step("Clicking Find a Slot button"):
            self.upass_holder_portal.click_find_slot()

        with allure.step("Selecting Appointment slot"):
            self.upass_holder_portal.select_appointment_slot()

        with allure.step("Confirming Appointment slot"):
            self.upass_holder_portal.select_confirm_appointment_slot()

        with allure.step("Clicking Review All Details Button"):
            self.upass_holder_portal.click_review_all_details()

        with allure.step("Clicking Confirm Appointment button"):
            self.upass_holder_portal.click_confirm_appointment()

        with allure.step("Verifying Scheduled Appointment"):
            self.upass_holder_portal.verify_dependent_appointment_scheduled()