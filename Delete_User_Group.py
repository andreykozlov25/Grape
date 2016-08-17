import os
from selenium import webdriver
import time
import random
import string

test_enviroment_details = {
    'platform': 'Linux',
    'browserName': 'chrome',
    'version': '48',
    'name': 'Test_Delete_User_Group'
}

driver = webdriver.Remote(
    command_executor='http://%s:%s@ondemand.saucelabs.com:80/wd/hub' % ('fellow_couch', '4eb2ad3a-fd8a-44d2-b3ce-90df01c4b052'),
    desired_capabilities=test_enviroment_details
    )

def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

ValidLogin = 'grape'
ValidPassword = 'grape$4'
GroupName = random_char(7)

#Test
driver.maximize_window()
driver.get('https://web-dev.grapeforce.de/')

element = driver.find_element_by_id('username')
element.send_keys(ValidLogin)

element = driver.find_element_by_id('passwd')
element.send_keys(ValidPassword)

element = driver.find_element_by_css_selector("[ng-click ='login.processLogin(login.userData)']")
element.click()

time.sleep(3)

element = driver.find_element_by_id('simple-dropdown')
element.click()
element = driver.find_element_by_link_text('qwerty')
element.click()

element = driver.find_element_by_link_text('Account Administration')
element.click()

element = driver.find_element_by_link_text('User Management')
element.click()

element = driver.find_element_by_link_text('User Groups')
element.click()

time.sleep(2)

element = driver.find_element_by_css_selector("[ui-sref ='dashboard.account.newUsergroup']")
element.click()

time.sleep(3)

element = driver.find_element_by_id('groupName')
element.send_keys(GroupName)

element = driver.find_element_by_css_selector("[ng-click ='createUserGroupCtrl.createAccount()']")
element.click()

time.sleep(1)

element = driver.find_element_by_css_selector("[ng-click ='ok()']")
element.click()

element = driver.find_element_by_css_selector("[ui-sref ='dashboard.account.usergroups']")
element.click()

time.sleep(1)

element = driver.find_element_by_css_selector("[ng-change ='userGroupCtrl.queryUserGroups(1)']")
element.send_keys(GroupName)

time.sleep(2)

element = driver.find_element_by_css_selector("[ng-click = 'userGroupCtrl.goToUpdatePage(userGroup)']")
element.click()


element = driver.find_element_by_css_selector("[ng-click = 'updateUserGroupCtrl.deleteUserGroup()']")
element.click()

time.sleep(1)

element = driver.find_element_by_css_selector("[ng-click ='ok()']")
element.click()

driver.quit()