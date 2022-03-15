import selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
firefox_options=Options()
webdriver.FirefoxProfile('C:\\Users\\Jitesh Chawla\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\zb7ta375.default-release')
firefox_options.add_argument("user-data-dir=C:\\Program Files\\Mozilla Firefox\\firefox.exe")

driver=webdriver.Firefox(executable_path=r'E:\\PROJECTS\\JARVIS AI ASSISTANT\\geckodriver-v0.26.0-win64\\geckodriver.exe')


driver.get("https://twitter.com/login")
uname=driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input')
uname.send_keys("jiteshchawla20")
passw=driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input')
passw.send_keys("elon1511")
enter=driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/form/div/div[3]/div/div')
enter.click()

tweet=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
tweet.click()
tweet_enter=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div')
tweet_enter.send_keys("lionel messi is the greatest of all time ")
tweet_button=driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]')
tweet_button.click()