from selenium import webdriver
from selenium.webdriver.common.keys import Keys

user = "abc.com"
pwd = "abc12"

driver = webdriver.Chrome("C:\Users\Swapnil.Chikodikar\chromedriver.exe")
driver.get("http://www.facebook.com")
assert "Facebook" in driver.title

elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)

elem.send_keys(Keys.RETURN)
driver.close()

# ******************************************************************


search_keyword = "Sungard AS"

driver = webdriver.Chrome("C:\Users\Swapnil.Chikodikar\chromedriver.exe")
driver.get("https://www.google.com")

search_elem = driver.find_element_by_name("q")
search_elem.send_keys(search_keyword)
search_elem.send_keys(Keys.RETURN)

links = driver.find_elements_by_xpath("//h3")
results = []

# for link in links:
#     d = {'url': link.get_attribute('href'),
#          'title': link.text}
#     results.append(d)
# print results

for link in links:
    results.append(str(link.text))

print("\n".join(results[:5]))
driver.close()