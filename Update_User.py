import os
from selenium import webdriver
import time
import random
import string

test_enviroment_details = {
    'platform': 'Linux',
    'browserName': 'chrome',
    'version': '48',
    'name': 'Test_Update_User'
}

driver = webdriver.Remote(
    command_executor='http://%s:%s@ondemand.saucelabs.com:80/wd/hub' % ('fellow_couch', '4eb2ad3a-fd8a-44d2-b3ce-90df01c4b052'),
    desired_capabilities=test_enviroment_details
    )

def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

ValidLogin = 'grape'
ValidPassword = 'grape$4'
Password = random_char(5)
NewPassword = random_char(5)
UserName = random_char(7)

#Test
driver.maximize_window()
driver.get('https://web-dev.grapeforce.de/')
#Create new user
element = driver.find_element_by_id('username')
element.send_keys(ValidLogin)

element = driver.find_element_by_id('passwd')
element.send_keys(ValidPassword)

element = driver.find_element_by_css_selector("[ng-click ='login.processLogin(login.userData)']")
element.click()

time.sleep(3)

element = driver.find_element_by_id('simple-dropdown')
element.click()

time.sleep(3)

element = driver.find_element_by_link_text('qwerty')
element.click()

element = driver.find_element_by_link_text('Account Administration')
element.click()

element = driver.find_element_by_link_text('User Management')
element.click()

element = driver.find_element_by_link_text('User')
element.click()

time.sleep(2)

element = driver.find_element_by_css_selector("[ui-sref ='dashboard.account.newUser']")
element.click()

time.sleep(3)

element = driver.find_element_by_id('userName')
element.send_keys(UserName)

element = driver.find_element_by_id('firstName')
element.send_keys(random_char(8))

element = driver.find_element_by_id('lastName')
element.send_keys(random_char(8))

element = driver.find_element_by_id('email')
element.send_keys(random_char(5)+'@gmail.com')

time.sleep(1)

element = driver.find_element_by_name('phone')
element.send_keys(random.randint(100000000, 999999999))

element = driver.find_element_by_name('fax')
element.send_keys(random.randint(100000000, 999999999))

element = driver.find_element_by_id('street_number')
element.send_keys(random_char(10))

element = driver.find_element_by_name('post_code')
element.send_keys(random.randint(10000, 99999))

element = driver.find_element_by_id('city')
element.send_keys(random_char(5))

element = driver.find_element_by_id('password')
element.send_keys(Password)

element = driver.find_element_by_id('confirmationPassword')
element.send_keys(Password)

time.sleep(1)

element = driver.find_element_by_css_selector("[ng-click='userGroup.isChecked = !userGroup.isChecked; createUserCtrl.userGroupsChanged()']")
element.click()

element = driver.find_element_by_css_selector("[ng-click='createUserCtrl.createUser()']")
element.click()

time.sleep(2)

element = driver.find_element_by_css_selector("[ng-click ='ok()']")
element.click()

time.sleep(1)

#Search and open new created user
element = driver.find_element_by_css_selector("[ui-sref = 'dashboard.account.user']")
element.click()

time.sleep(1)

element = driver.find_element_by_css_selector("[ng-change ='userCtrl.queryUsers(1)']")
element.send_keys(UserName)

time.sleep(5)

element = driver.find_element_by_css_selector("[ng-click = 'userCtrl.goToUpdatePage(user);']")
element.click()

#Update all fields and save user
element = driver.find_element_by_id('userName')
element.clear()
element.send_keys(random_char(10))

element = driver.find_element_by_id('firstName')
element.clear()
element.send_keys(random_char(10))

element = driver.find_element_by_id('lastName')
element.clear()
element.send_keys(random_char(10))

element = driver.find_element_by_id('email')
element.clear()
element.send_keys(random_char(8)+'@gmail.com')

time.sleep(1)

element = driver.find_element_by_name('phone')
element.clear()
element.send_keys(random.randint(100000000, 999999999))

element = driver.find_element_by_name('fax')
element.clear()
element.send_keys(random.randint(100000000, 999999999))

element = driver.find_element_by_id('street_number')
element.clear()
element.send_keys(random_char(15))

element = driver.find_element_by_name('post_code')
element.clear()
element.send_keys(random.randint(10000, 99999))

element = driver.find_element_by_id('city')
element.send_keys(random_char(8))

#Update password
element = driver.find_element_by_css_selector("[ng-click = 'updateUserCtrl.updatePassword()']")
element.click()

time.sleep(1)

element = driver.find_element_by_id('oldPassword')
element.send_keys(Password)

element = driver.find_element_by_id('newPassword')
element.send_keys(NewPassword)

element = driver.find_element_by_id('confirmPassword')
element.send_keys(NewPassword)

element = driver.find_element_by_css_selector("[ng-click = '$event.preventDefault(); ok()']")
element.click()

time.sleep(3)

element = driver.find_element_by_css_selector("[ng-click = 'params.btnOk.class']")
element.click()

#Save
element = driver.find_element_by_css_selector("[ng-click = 'updateUserCtrl.updateUser()']")
element.click()

time.sleep(1)

element = driver.find_element_by_css_selector("[ng-click = 'ok()']")
element.click()
