
# Operating system imports
import os
# Environment variable imports
from dotenv import load_dotenv
load_dotenv()

# Selenium imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


# Your path to chrome driver executable.
chrome_driver = os.getenv("chrome_driver_path")
""" --- Chrome driver options ---"""
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--disable-cookies")
#chrome_options.add_argument("--headless")





class ScraperTemplate:
    wait_time = 5
    def __init__(self):
        self.browser = None
    '''----------------------------------- Browser Utilities -----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    def read_data(self, xpath: str, wait: bool = False, _wait_time: int = wait_time, tag: str = "") -> str:
        '''
        :param xpath: Path to the web element.
        :param wait: Boolean to determine if selenium should wait until the element is located.
        :param wait_time: Integer that represents how many seconds selenium should wait, if wait is True.  
        :return: (str) Text of the element. 
        '''

        if wait:
            try:
                data = WebDriverWait(self.browser, _wait_time).until(EC.presence_of_element_located((By.XPATH, xpath))).text
            except TimeoutException:
                print(f"[Failed Xpath] {xpath}")
                if tag != "":
                    print(f"[Tag]: {tag}")
                raise NoSuchElementException("Element not found")
        else:
            data = self.browser.find_element("xpath", xpath).text
        # Return the text of the element found.
        return data
    '''-----------------------------------'''
    def click_button(self, xpath: str, wait: bool = False, _wait_time: int = wait_time, scroll: bool = False, tag: str = "") -> None:
        '''
        :param xpath: Path to the web element. 
        :param wait: Boolean to determine if selenium should wait until the element is located.
        :param wait_time: Integer that represents how many seconds selenium should wait, if wait is True.  
        :return: None. Because this function clicks the button but does not return any information about the button or any related web elements. 
        '''


        if wait:
            try:
                element = WebDriverWait(self.browser, _wait_time).until(EC.presence_of_element_located((By.XPATH, xpath)))
                # If the webdriver needs to scroll before clicking the element. 
                if scroll:
                    self.browser.execute_script("arguments[0].click();", element)
                element.click()
            except TimeoutException:
                print(f"[Failed Xpath] {xpath}")
                if tag != "":
                    print(f"[Tag]: {tag}")
                raise NoSuchElementException("Element not found")
        else:
            element = self.browser.find_element("xpath", xpath)
            if scroll:
                    self.browser.execute_script("arguments[0].click();", element)
            element.click()
    '''-----------------------------------'''
    def build_snapshot_url(self, year, month, day):
        # Build the date url
        date = self.format_date(year, month, day)

        snapshot_url = self.histroical_url.format(date)
        return snapshot_url
    '''-----------------------------------'''
    def create_browser(self, url=None):
        '''
        :param url: The website to visit.
        :return: None
        '''
        service = Service(executable_path=chrome_driver)
        self.browser = webdriver.Chrome(
            service=service, options=chrome_options)
        # Default browser route
        if url == None:
            self.browser.get(url=self.sec_annual_url)
        # External browser route
        else:
            self.browser.get(url=url)
    '''-----------------------------------'''
    def scroll_page(self, pixel_to_scroll: int = 500, element_to_scroll = "", by_pixel: bool = True, by_element: bool = False) -> None:
        '''
        :param element_to_scroll: Scroll to the specified element on the webpage. 
        :returns: There is no data to return. 
        '''
        if by_pixel:
            self.browser.execute_script(f"window.scrollBy(0, {pixel_to_scroll})", "")
        
        if by_element:
            self.browser.execute_script("arguments[0].scrollIntoView(true);", element_to_scroll)
        
    '''-----------------------------------'''
    def create_element(self, xpath: str) -> webdriver.remote.webelement.WebElement:
        '''
        :param  xpath: The xpath to the element that we are creating. 
        '''
        element = self.browser.find_element("xpath", xpath)
        return element
    '''-----------------------------------'''
    def get_webpage_dimensions(self):
        '''
        Get the webpage width and height for the current url. 
        '''
        width = self.browser.execute_script("return window.outerWidth")
        height = self.browser.execute_script("return window.outerHeight")
        return width, height