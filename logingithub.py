from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from Screenshot import Screenshot
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

capabilities=DesiredCapabilities().FIREFOX
capabilities['acceptSslCerts'] = False


username="root"
password="calvin"


driver = webdriver.Firefox(executable_path=r'/Users/saras008/Downloads/geckodriver',capabilities=capabilities)

# head to github login page
driver.get("https://192.168.247.143")
driver.find_element("id", "advancedButton").click()
driver.find_element("id", "exceptionDialogButton").click()
# find username/email field and send the username itself to the input field
driver.find_element("name", "user").send_keys(username)
# # find password input field and insert password as well
# driver.find_element("id", "password").send_keys(password)
# # click login button
# driver.find_element("id", "submit_lbl").click()

# ob = Screenshot.Screenshot()

# img_url=ob.hide_elements(driver, save_path=r'.',image_name="github.png",is_load_at_runtime=True,load_wait_time=3)
# print(img_url)
# driver.save_full_page_screenshot("github.png")
# driver.close()
# driver.quit()

sc=driver.find_element_by_tag_name('body')
sc=Screenshot('github.png')
driver.quit()