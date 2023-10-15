# Operating system imports
import os
import sys


# Import macro-scraper 
from Scrapers.macro_scraper import MacroScraper

# Import commodity scraper.
from Scrapers.commodities_scraper import CommoditiesScraper

# 

''' ---------------------- Interest Rates ---------------------- '''
def fed_funds(mac: MacroScraper):
    mac.update_fed_funds()


''' ---------------------- CPI ---------------------- '''
def cpi(mac: MacroScraper):
    mac.update_cpi()






if __name__ == "__main__":

    # Create scraper objects
    mac = MacroScraper()
    com = CommoditiesScraper()

    # If arguments are passed
    if len(sys.argv) > 0:
        func = sys.argv[1]
        try:
            macro_data = sys.argv[2]
        except IndexError:
            macro_data = ""
    else:
        func = "Display"
        macro_data = "FedFunds"


    # Make macro-data argument lowercase to make case matching easier. 
    macro_data = macro_data.lower()

    # Make func arguement lowercase.
    func = func.lower()

    # Allowed arguements for Federal Funds Rate 
    fed_fund_args = ["fedfunds", "fedfund", "interestrates", "ffr"] # Note: Should all be lowercase, since all our comparisons are done in lowercase to avoid capitalization matching errors.
    cpi_args = ["cpi", "inflation"]
    

    if func != "other":
        if macro_data in fed_fund_args:
            if func == "update":
                fed_funds(mac)
            elif func == "display":
                pass
            elif func == "source":
                print(f"Fed Funds Source Url: {mac.get_fed_funds_source()}")

        elif macro_data in cpi_args:
            if func == "update":
                cpi(mac)
            elif func == "display":
                pass
            elif func == "source":
                print(f"CPI Source Url: {mac.get_fed_funds_source()}")
    
    else:
        mac.update_treasury_yield_diff()




