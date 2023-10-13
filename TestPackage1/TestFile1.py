from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.implicitly_wait(300)
driver.get("http://automationexercise.com")
driver.maximize_window()
homepageTitle = driver.find_element(By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[1]/a").text
if homepageTitle == "Home":
    print("Homepage is visible successfully")
else:
    print("Homepage is not visible")
viewproductBtn = driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[2]/ul/li/a")
viewproductBtn.click()

addtocartBtn = driver.find_element(By.XPATH, "/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/button")
addtocartBtn.click()
viewcartBtn = driver.find_element(By.XPATH, "/html/body/section/div/div/div[2]/div[1]/div/div/div[2]/p[2]")
viewcartBtn.click()

driver.implicitly_wait(100)

"""
driver.implicitly_wait(10)
element = driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/a")
element.click()


cartElement = driver.find_element(By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[3]/a")
cartElement.click()
"""

cartpageTitle = driver.find_element(By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[3]/a").text

if cartpageTitle == "Cart":
    print("Cartpage is dispalyed")
else:
    print("Cartpage is not displayed")

proceedtocheckoutBtn = driver.find_element(By.XPATH, "/html/body/section/div/section/div[1]/div/div/a")
proceedtocheckoutBtn.click()

registerBtn = driver.find_element(By.XPATH, "/html/body/section/div/section/div[2]/div/div/div[2]/p[2]/a/u")
registerBtn.click()


name = driver.find_element(By.NAME, "name")
name.send_keys("hello")
driver.implicitly_wait(100)
email = driver.find_element(By.XPATH, "/html/body/section/div/div/div[3]/div/form/input[3]")
email.send_keys("hello+21@test.com")
driver.implicitly_wait(100)

signupBtn = driver.find_element(By.XPATH, "/html/body/section/div/div/div[3]/div/form/button")
signupBtn.click()

accountInfo = driver.find_element(By.XPATH, "/html/body/section/div/div/div/div/h2/b")
assert accountInfo.is_displayed()

radioBtn = driver.find_element(By.CSS_SELECTOR, "label[for='id_gender2']")
radioBtn.click()

driver.implicitly_wait(10)

password = driver.find_element(By.ID, "password")
password.send_keys("password")

selectDay = Select(driver.find_element(By.ID, "days"))
selectDay.select_by_value("5")

selectMonth = Select(driver.find_element(By.ID, "months"))
selectMonth.select_by_visible_text("January")

selectYear = Select(driver.find_element(By.ID, "years"))
selectYear.select_by_value("1996")

firstName = driver.find_element(By.ID, "first_name")
firstName.send_keys("Test")

lastName = driver.find_element(By.ID, "last_name")
lastName.send_keys("User")

company = driver.find_element(By.ID, "company")
company.send_keys("Test Group")

address1 = driver.find_element(By.ID, "address1")
address1.send_keys("New Test Apartment")

address2 = driver.find_element(By.ID, "address2")
address2.send_keys("Test Address 2")

selectCountry = Select(driver.find_element(By.ID, "country"))
selectCountry.select_by_visible_text("India")

driver.implicitly_wait(10)

state = driver.find_element(By.ID, "state")
state.send_keys("Tamil Nadu")

cityElement = driver.find_element(By.ID, "city")
cityElement.send_keys("Chennai")

zipcodeElement = driver.find_element(By.ID, "zipcode")
zipcodeElement.send_keys("1216")

mobileNumber = driver.find_element(By.ID, "mobile_number")
mobileNumber.send_keys("12345678909")

driver.implicitly_wait(100)

driver.find_element(By.XPATH, "/html/body/section/div/div/div/div/form/button").click()


accountTitle = driver.find_element(By.XPATH, "/html/body/section/div/div/div/h2").text

if accountTitle == "ACCOUNT CREATED!":
    print("User account has been created successfully")
else:
    print("Account creation not successful")
driver.implicitly_wait(10)

continueBtn = driver.find_element(By.XPATH, "/html/body/section/div/div/div/div/a")
continueBtn.click()

"""
userName = driver.find_element(By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[10]/a/b").text
print(userName)

if userName == name:
    print("User name verified as logged in")
else:
    print("User name not verified")
"""

cartBtn = driver.find_element(By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[3]")
cartBtn.click()

proceedtocheckoutBtn2 = driver.find_element(By.XPATH, "/html/body/section/div/section/div[1]/div/div/a")
proceedtocheckoutBtn2.click()

textArea = driver.find_element(By.XPATH, "/html/body/section/div/div[6]/textarea")
textArea.send_keys("This is test comment")

placeOrder = driver.find_element(By.XPATH, "/html/body/section/div/div[7]/a")
placeOrder.click()

cardName = driver.find_element(By.NAME, "name_on_card")
cardName.send_keys("Test User")

cardNumber = driver.find_element(By.NAME, "card_number")
cardNumber.send_keys("1111 2222 3333 4444")

cvcNumber = driver.find_element(By.NAME, "cvc")
cvcNumber.send_keys("123")

expiryMonth = driver.find_element(By.NAME, "expiry_month")
expiryMonth.send_keys("06")

expiryYear = driver.find_element(By.NAME, "expiry_year")
expiryYear.send_keys("2025")

payBtn = driver.find_element(By.ID, "submit")
payBtn.click()

orderPlaced = driver.find_element(By.XPATH, "/html/body/section/div/div/div/h2").text

if orderPlaced == "ORDER PLACED!":
    print("Your order has been placed successfully")
else:
    print("Order is not placed")



driver.implicitly_wait(10)

driver.close()
