import allure
from allure_commons.types import AttachmentType
from utils.browser_config import driver


class Screenshot:

    def __init__(self, driver):
        self.driver = driver

    """
        @author : sreenivas reddy
        Description: This method is used to take screenshot and attach taken screenshot to allure report
        parameter i/p: method name
    """

    def attach_screenshot_to_allure_report(self, method_name):
        allure.attach(driver.get_screenshot_as_png(), name=method_name, attachment_type=AttachmentType.PNG)
