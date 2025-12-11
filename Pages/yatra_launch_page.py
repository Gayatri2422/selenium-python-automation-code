from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time
from Base.base_driver import BaseDriver
from Pages.search_flights_results_page import SearchFlightResults
from utilities.utils import Utils



class LaunchPage(BaseDriver):

    log = Utils.custom_logger()
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        #self.wait = wait
    
    
    # Locator's
    DEPART_FROM_FIELD = "//p[contains(text(),'DEL, Indira Gandhi International')]"
    DEPART_FROM_INPUT_FIELD = "//label[text()='Departure From']/following-sibling::div//input"
    SELECT_VALUE_FROM_DROPDOWN = "//li[.//span[text()='New Delhi'] and .//span[text()='DEL']]"
    GOING_TO_FIELD = "//p[contains(text(),'Going To')]"
    GOING_TO_INPUT_FIELD = "//input[@id='input-with-icon-adornment']"
    SELECT_VALUE_TO_DROPDOWN = "//li[.//span[text()='New York'] and .//span[text()='NYC']]"
    CALENDAR_FIELD = "(//div[@class='css-13lub7m'])[1]"
    CALENDAR_DATE_TEMPLATE = "//div[contains(@class,'react-datepicker__day') and contains(@aria-label,'{date}')]"
    SEARCH_BUTTON  = "//button[contains(@class,'MuiButton-root') and text()='Search']"

    

    # Depart From location selection process
    def getDepartfromfield(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.DEPART_FROM_FIELD)
        
    def enterValueindepartfrom(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.DEPART_FROM_INPUT_FIELD)
    
    def selectValuefromdropdown(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.SELECT_VALUE_FROM_DROPDOWN)
   
    def enterValuefromDropdown(self,departlocation):
        self.getDepartfromfield().click()
        self.enterValueindepartfrom().click()
        self.enterValueindepartfrom().send_keys(departlocation)
        self.selectValuefromdropdown().click()
        time.sleep(10)

    # Going to location selection process
    def getGoingtofield(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.GOING_TO_FIELD)
    
    def enterValueingoingto(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.GOING_TO_INPUT_FIELD)
    
    def selectValuetodropdown(self):
        return self.wait_for_visibility_of_element_located(By.XPATH, self.SELECT_VALUE_TO_DROPDOWN)
    
    def enterValuetodropdwon(self,goingtolocation):
        self.getGoingtofield().click()
        self.log.info("Click on going to field")
        self.enterValueingoingto().click()
        self.enterValueingoingto().send_keys(goingtolocation)
        self.log.info("Enter going to place name in text field")
        self.selectValuetodropdown().click()

    # date selection 
    def clickOndatefield(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.CALENDAR_FIELD)
    
    def selectDatefromcalendar(self, flightdate):
        self.clickOndatefield().click()
        # Fill in the placeholder dynamically
        date_xpath = self.CALENDAR_DATE_TEMPLATE.format(date=flightdate)
        Selectdate = self.wait_until_element_is_clickable(By.XPATH, date_xpath)
        Selectdate.click()

    # Click on search button
    def getserachButton(self):
        return self.wait_until_element_is_clickable(By.XPATH,self.SEARCH_BUTTON)
    
    def clickOnsearchbutton(self):
        self.getserachButton().click()
        time.sleep(25)
        
    def searchFlights(self,departlocation,goingtolocation,departuredate):
        self.enterValuefromDropdown(departlocation)
        self.enterValuetodropdwon(goingtolocation)
        self.selectDatefromcalendar(departuredate)
        self.clickOnsearchbutton()
        SFR = SearchFlightResults(self.driver)
        return SFR
        