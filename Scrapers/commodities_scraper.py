# Operating system imports
import os


# Time & Date imports
import time

# Import the scraper template
import Scrapers.scraper_template

# Pandas imports 
import pandas as pd

# Requests imports
import requests 

# Selenium import
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException






cwd = os.getcwd()
# Path to the commodities data folder.
commodities_data_folder_path = f"{cwd}\\CommoditiesData\\" 

fossil_fuels_tag = "Fossil Fuels"
agriculture_tag = "Agriculture"
materials_tag = "Basic Materials"

name_key = "Name"
class_key = "Classification"
category_key = "Category"


commodities = {
    "BZ=F": {
        name_key: "Brent Crude Oil Futures",
        class_key: "Oil",
        category_key: fossil_fuels_tag,
    },
    "CC=F": {
        name_key: "Cocoa Futures",
        class_key: "Cocoa",
        category_key: agriculture_tag,
    },
    "KC=F": {
        name_key: "",
        class_key: "",
        category_key: "",
    },
    "": {
        name_key: "",
        class_key: "",
        category_key: "",
    },
    "": {
        name_key: "",
        class_key: "",
        category_key: "",
    },
    "": {
        name_key: "",
        class_key: "",
        category_key: "",
    },
    "": {
        name_key: "",
        class_key: "",
        category_key: "",
    },
    "": {
        name_key: "",
        class_key: "",
        category_key: "",
    },
    "": {
        name_key: "",
        class_key: "",
        category_key: "",
    },
    "": {
        name_key: "",
        class_key: "",
        category_key: "",
    },
}


class CommoditiesScraper(Scrapers.scraper_template.ScraperTemplate):
    def __init__(self):
        self.browser = None
        super().__init__()
    
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    def reorder_data(self):
        path = f"{commodities_data_folder_path}\\commodity_info.csv"
        df = pd.read_csv(path)
        new_order = ["ticker", "name", "info", "tag"]
        reordered_df = df[new_order]
        reordered_df = reordered_df.rename(columns={"info": "classification", "tag": "category"})
        reordered_df.to_csv(path, index=False)
        print(f"DF: {df}")
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''