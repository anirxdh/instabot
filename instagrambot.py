from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

Chrome_driver_path = "D:\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=Chrome_driver_path)



driver.get("https://www.instagram.com/narendramodi/followers/")
sleep(5)

username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")

username.send_keys("abiabinownow")
password.send_keys("anirudh@03042001")
login_button = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
login_button.click()

sleep(3)
search_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[1]/div')
search_button.click()
sleep(1)
searching = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
searching.send_keys("narendra modi")
sleep(3)

driver.get("https://www.instagram.com/narendramodi/followers/")
""" click_nare = driver.find_element_by_xpath('//*[@id="ffd25b66967018"]/div/div/div[1]')
sleep(3)
followers = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span')
followers.click()
sleep(3) """
base_window = driver.window_handles[0]
nr_login_window = driver.window_handles[1]
driver.switch_to.window(nr_login_window)
sleep(6)
followers = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/ul/li[2]/a/span')
followers.click()

all_followers_class = driver.find_elements_by_class_name(".sqdOP  .L3NKy   y3zKF     ")
print(all_followers_class)