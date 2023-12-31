import allure
from POM.Portal.upass_holder_app import HolderPortal
from utils.browser_config import driver
from utils.read_data import ReadData
from POM.BaseTest.upass_holder import RegBaseTest
import logging

LOGGER = logging.getLogger(__name__)

"""
    @author             : Somasekhar
    Description         : This method is used to link record for COVID 19 RT PCR(Issuer type: CDC)
"""


class TestLinkRecordHealthCovid19RTPCRDependent(RegBaseTest):
    upass_holder_portal = HolderPortal(driver)

    def test_link_record_health_covid_19_rt_pcr_dependent(self):
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

        with allure.step("Clicking the records"):
            self.upass_holder_portal.click_records()
            LOGGER.info("Click the records button")

        with allure.step("Clicking dropdown from top of records page"):
            self.upass_holder_portal.click_drop_down_from_records()
            LOGGER.info("Clicking dropdown from top of records page")

        with allure.step("Selecting the dependent"):
            self.upass_holder_portal.select_the_dependent()
            LOGGER.info("Dependent selected successfully")

        with allure.step("Clicking the add/get record"):
            self.upass_holder_portal.click_add_or_get_record()
            LOGGER.info("Click add/get record button")

        with allure.step("Clicking the link record"):
            self.upass_holder_portal.click_to_link_record()
            LOGGER.info("Click the link record")

        with allure.step("Selecting dependent holder name"):
            self.upass_holder_portal.select_dependent_holder_name()
            LOGGER.info("Select dependent holder name")

        with allure.step("Selecting record category type"):
            self.upass_holder_portal.select_record_category_health()
            LOGGER.info("Select record category")

        with allure.step("Selecting record type: covid 19 rt pcr"):
            self.upass_holder_portal.select_record_type_covid_19_rt_pcr()
            LOGGER.info("Select record type: covid 19 rt pcr")

        with allure.step("Selecting issuer type: Inspire Health"):
            self.upass_holder_portal.select_issuer_type_inspire_health_1()
            LOGGER.info("Select issuer type: Inspire Health")

        with allure.step("Clicking the search records"):
            self.upass_holder_portal.click_search_records()
            LOGGER.info("Click the search records")

        with allure.step("Clicking the save button"):
            self.upass_holder_portal.click_save_record()
            LOGGER.info("Click the save button")

        with allure.step("Clicking Health tab under Records page"):
            self.upass_holder_portal.click_health_tb()
            LOGGER.info("Click Health tab under Records page")

        with allure.step("Verifying covid 19 rt-pcr test health record"):
            self.upass_holder_portal.verify_covid_19_rt_pcr()
            LOGGER.info("Verify covid 19 rt-pcr test health record")

