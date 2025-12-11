from Base.base_driver import BaseDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from utilities.utils import Utils
import logging

class SearchFlightResults(BaseDriver):

    log = Utils.custom_logger(loglevel=logging.WARNING)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        #self.wait = wait

    #Locator's
    ONESTOP_FIELD = "//p[@class='font-lightgrey bold'][normalize-space()='1']"
    TWOSTOP_FIELD = "//p[@class='font-lightgrey bold'][normalize-space()='2']"
    NONSTOP_FIELD = "//p[@class='font-lightgrey bold'][normalize-space()='0']"
    SEARCH_FLIGHT_RESULTS = "//span[contains(text(), '1 Stop') or contains(text(), '2 Stop') or contains(text(), 'Non Stop')]"

    def get_onestop_filter_flights(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ONESTOP_FIELD)
    
    def get_twostop_filter_flights(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.TWOSTOP_FIELD)
    
    def get_nonstop_filter_flights(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.NONSTOP_FIELD)
    
    def get_search_result_flights(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.SEARCH_FLIGHT_RESULTS)
    
    
    def filter_flights_by_stop(self, by_stop):
        if by_stop == "1 Stop":
            time.sleep(10)
            self.get_onestop_filter_flights().click()
            self.log.warning("Selected flight with 1 stop") 

        elif by_stop == "2 Stop ":
            self.get_twostop_filter_flights().click()
            self.log.warning("Selected flight with 2 stop") 

        elif by_stop == "Non Stop":
            self.get_nonstop_filter_flights().click()
            time.sleep(2)
            self.log.warning("Selected flight with non stop") 
        else:
            self.log.warning("provide valid filter option")



    
