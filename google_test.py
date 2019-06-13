"""
This module has a python script which uses selenium framework.
It launches google on chrome and searches a keyword on google
And it prints top 5 search results

"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException


class GoogleTest:
    """
    This class two methods and the constructor
    """
    def __init__(self, path, url):
        """
        Constructor launches the chrome browser with desired url
        :param path: path of chromedriver's executable file
        :param url: url of desired website to be searched.
        """
        self.driver = webdriver.Chrome(path)
        self.driver.get(url)
        return

    def do_search(self, search_keyword):
        """
        Searches given keyword in google search, "Sungard AS" in this case
        :param search_keyword: The keyword to be searched
        :return: returns none
        """
        search_elem = self.driver.find_element_by_name("q")
        search_elem.send_keys(search_keyword)
        search_elem.send_keys(Keys.RETURN)
        return

    def get_results(self, search_keyword):
        """
        This method calls the search_keyword method
        After getting the results it will store all the results
        It will iterate through the results and store them in a list
        and then it prints the top 5 results from the list
        :param search_keyword:
        :return:
        """
        self.do_search(search_keyword)
        links = self.driver.find_elements_by_xpath("//h3")
        results = []
        for link in links:
            results.append(str(link.text))
        self.driver.close()
        return results


PATH = "C:\\Users\\Swapnil.Chikodikar\\chromedriver.exe"
URL = "https://www.google.com"
SEARCH_KEYWORD = "Sungard AS"

try:
    OBJ = GoogleTest(PATH, URL)
    TOP_LINKS = OBJ.get_results(SEARCH_KEYWORD)
    print "\n".join(TOP_LINKS[:5])
except WebDriverException as ex:
    print ("Message: 'chromedriver.exe' executable needs to be in {}.".format(PATH))
