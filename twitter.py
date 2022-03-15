import selenium
from selenium import webdriver
driver=webdriver.Firefox
driver.get("https://www.twitter.com")

driver.find_element_by_xpath("//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input")
