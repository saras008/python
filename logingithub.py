from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from Screenshot import Screenshot


username="simatupang2000@gmail.com"
password="B0k3rdij4l4n"

driver = webdriver.Firefox(executable_path=r'/Users/saras008/Downloads/geckodriver')

# head to github login page
driver.get("https://github.com/login")
# find username/email field and send the username itself to the input field
driver.find_element("id", "login_field").send_keys(username)
# find password input field and insert password as well
driver.find_element("id", "password").send_keys(password)
# click login button
driver.find_element("name", "commit").click()

# ob = Screenshot.Screenshot()

# img_url=ob.hide_elements(driver, save_path=r'.',image_name="github.png",is_load_at_runtime=True,load_wait_time=3)
# print(img_url)
# driver.save_full_page_screenshot("github.png")
# driver.close()
# driver.quit()

sc=driver.find_element_by_tag_name('body')
sc=Screenshot('github.png')
driver.quit()