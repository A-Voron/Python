# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Test12():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_12(self):
    self.driver.get("http://192.168.1.176:5000/webman/index.cgi")
    self.driver.set_window_size(1552, 832)
    self.driver.find_element(By.ID, "login_username").click()
    self.driver.find_element(By.ID, "login_username").send_keys("User")
    self.driver.find_element(By.ID, "login_passwd").send_keys("L8#@Kf)se4")
    self.driver.find_element(By.ID, "ext-gen18").click()
    self.driver.find_element(By.ID, "login_passwd").click()
    self.driver.find_element(By.ID, "sds-login-dialog").click()
    self.driver.find_element(By.ID, "login_passwd").send_keys("L8#@KfOse4")
    self.driver.find_element(By.ID, "login_passwd").send_keys(Keys.ENTER)
    element = self.driver.find_element(By.ID, "ext-gen25")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "#ext-gen205 > .image").click()
  
