from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time
from Pages.yatra_launch_page import LaunchPage
from Pages.search_flights_results_page import SearchFlightResults
from utilities.utils import Utils
import softest
from ddt import ddt, data, file_data, unpack


@pytest.mark.usefixtures("setup")
@ddt
class TestSearchAndVeriryFlights(softest.TestCase):
    log = Utils.custom_logger()


    # @pytest.fixture(autouse=True)
    # def class_setup(self,setup):
    #     self.driver = setup
    #     self.lp = LaunchPage(self.driver)
    #     self.ut = Utils()

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.ut = Utils()
        

    # @data(("New Dehli", "New York", "December 9th, 2025", "1 Stop"), ("New Dehli", "New York", "December 10th, 2025", "1 Stop"))
    # @unpack
    # @file_data('../testcases/testdata/testdata.json')
    # @file_data('../testcases/testdata/testyml.yaml')
    #@data(*Utils.read_data_from_excel(r"C:\Python-Learning\TestFrameworkDemo\testcases\testdata\testflight.xlsx","Sheet1"))
    @data(*Utils.read_data_from_csv(r"C:\Python-Learning\TestFrameworkDemo\testcases\testdata\tdata.csv"))
    @unpack
    def test_search_flights_1_stop(self,departfrom, goingto, date, stops):
        # Launching browser and opening Yatra website
        # Enter "From" location Wait for autosuggestion list and select first option
        # Enter "To" location Wait for autosuggestion list and select first option
        # click on date, select the date and click on search button
        search_flight_result =self.lp.searchFlights(departfrom,goingto,date)
        #page scrolling 
        self.lp.page_scroll()
        #clcik on 1 stop
        search_flight_result.filter_flights_by_stop(stops)       
        #After scrolling, collect all flights with "1 Stop" , "2 stop" ,"non stop"
        allstop1 = search_flight_result.get_search_result_flights()
        self.log.info(len(allstop1))
        #print all the 1 stop and verifying the 1 stop       
        self.ut.assertListItemText(allstop1, stops)

        

    
    


         
        

        






        

