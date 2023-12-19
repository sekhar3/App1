from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utils.browser_config import driver
import utils.logger as cl
import time
import os


class SeleniumDriver:
    def __init__(self, driver):
        self.driver = driver

    log = cl.customLogger()

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "linktext":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType + " not correct/supported")
        return False

    def getScreenShot(self, name):
        fileName = name + "_" + str(round(time.time() * 1000)) + ".png"
        currentDirectory = os.path.dirname(__file__)
        screenShotsDir = "../../Screenshots/"
        relativeFileName = screenShotsDir + fileName
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        desinationDirectory = os.path.join(currentDirectory, screenShotsDir)
        try:
            if not os.path.exists(desinationDirectory):
                os.makedirs(desinationDirectory)
            self.driver.save_screenshot(destinationFile)
        except:
            self.log.warning("Failed to take screenshot")

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
        except:
            raise Exception("Element is not found")
        return element

    def element_clickable(self, locatorType, locator):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            wait = WebDriverWait(driver, 60)
            wait.until(expected_conditions.element_to_be_clickable((byType, locator)))
        except:
            self.log.error("Element is not clickable")
            print_stack()
            raise Exception("Element is not clickable")

    def element_Is_Visible(self, locatorType, locator):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            wait = WebDriverWait(driver, 120)
            wait.until(expected_conditions.visibility_of_element_located((byType, locator)))
        except:
            self.log.error("Element is not visible")
            print_stack()
            raise Exception("Element is not visible")

    def presence_of_element(self, locatorType, locator):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            wait = WebDriverWait(driver, 60)
            wait.until(expected_conditions.presence_of_element_located((byType, locator)))
        except:
            self.log.error("Element is not present")
            print_stack()
            raise Exception("Element is not present")

    def enterText(self, locatorType, locatorVal, data):
        element = None
        try:
            element = self.getElement(locatorVal, locatorType)
            time.sleep(0.5)
            element.send_keys(data)
            self.log.info("Enter Text on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorVal)
        except:
            self.getScreenShot("FailedToEnterData")
            self.log.error("Unable to Enter Text on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorVal)
            print_stack()
            raise Exception("Failed to enter data in text field")

    def clickElement(self, locatorType, locatorVal):
        element = None
        try:
            element = self.getElement(locatorVal, locatorType)
            time.sleep(0.5)
            element.click()
            self.log.info("Clicked on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorVal)
        except:
            self.log.error("Unable to click on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorVal)
            print_stack()
            raise Exception("Failed to click on the element")

    def getText(self, locatorType, locatorVal):
        element = None
        try:
            wait = WebDriverWait(self.driver, 60)
            wait.until(expected_conditions.visibility_of_element_located((locatorType, locatorVal)))
            wait.until(expected_conditions.element_to_be_clickable((locatorType, locatorVal)))
            element = self.getElement(locatorVal, locatorType)
            act = element.text
            self.log.info("Get text  on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorVal)
            return act
        except:
            self.log.error("Failed to enter data")
            print_stack()
            raise Exception("Failed to enter data in text field")