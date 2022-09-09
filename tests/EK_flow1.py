from selenium import webdriver
from time import sleep

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import random
import string
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path=r"C:\Users\jeet\PycharmProjects\NufDemo\driver\chromedriver.exe")

# driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://home.staging.nuflights.com/auth/login/workbench")
driver.implicitly_wait(50)
sleep(1)
driver.find_element_by_xpath("//input[@name='username']").send_keys("jeet2das2+gta@gmail.com")
driver.find_element_by_xpath("//input[@name='password']").send_keys("Jeet@123")
driver.find_element_by_xpath("//button[text()='Login']").click()
ele = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[text()='1 Adults, 0 Child, 0 Infant']")))
ele1 = driver.find_element_by_xpath("//div[text()='1 Adults, 0 Child, 0 Infant']")
ele1.click()
driver.find_element_by_xpath("//p[text()='Adults']/..//span[@class='counter-btn' and text()='+']").click()
#sleep(1)
driver.find_element_by_xpath("//p[text()='Child (2-12 YRS)']/..//span[@class='counter-btn' and text()='+']").click()
driver.find_element_by_xpath("//p[text()='Child (2-12 YRS)']/..//span[@class='counter-btn' and text()='+']").click()
#sleep(1)
driver.find_element_by_xpath("//p[text()='Infant (Below 2 YRS)']/..//span[@class='counter-btn' and text()='+']").click()
#driver.find_element_by_xpath("//p[text()='Infant (Below 2 YRS)']/..//span[@class='counter-btn' and text()='+']").click()
ele1.click()
sleep(1)
driver.find_element_by_name("departure").send_keys("LHR")
sleep(1)
driver.find_element_by_name("arrival").send_keys("DXB")
sleep(1)
driver.find_element_by_xpath("//input[@placeholder='Select a departure date']").click()

for i in range(1, 13):
    curr_mnth = driver.find_element_by_xpath("//div[@class='react-datepicker__current-month']").text
    if curr_mnth == "January 2023":
        driver.find_element_by_xpath("//div[@class='react-datepicker__day react-datepicker__day--019']").click()
        break
    else:
        driver.find_element_by_xpath("//button[text()='Next Month']").click()

driver.find_element_by_xpath("//button[text()='Search Flights']").click()
ele = WebDriverWait(driver, 100).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@class='flight-card']")))

driver.find_element_by_xpath("(//div[@class='airline-filter'])[3]").click()
driver.find_element_by_xpath("(//div[@class='flight-card'])[1]").click()

ele2 = WebDriverWait(driver, 100).until(
    EC.visibility_of_element_located((By.XPATH, "//div[text()='TTL']")))

driver.find_element_by_xpath("//button[text()='Continue']").click()
# sleep(1)
# driver.refresh()
ele3 = WebDriverWait(driver, 100).until(
    EC.visibility_of_element_located((By.XPATH, "(//div[@class='link'])[1]")))

driver.find_element_by_xpath("(//div[@class='link'])[1]").click()

# Adding pax details for first ADT [1]
driver.find_element_by_xpath("(//div[@class='link'])[1]").click()
driver.find_element_by_xpath("(//input[@name='passportNumber'])[1]").send_keys(random.getrandbits(30))
sel = Select(driver.find_element_by_xpath("(//select[@name='nationality'])[1]"))
sel.select_by_value("IN")
ele7 = WebDriverWait(driver, 100).until(
    EC.visibility_of_element_located((By.XPATH, "(//input[@name='passportExpiry'])[1]")))
driver.find_element_by_xpath("(//input[@name='passportExpiry'])[1]/..//button").click()
sel1 = Select(driver.find_element_by_xpath("//select[@class='react-datepicker__year-select']"))
sel1.select_by_value("2030")
driver.find_element_by_xpath("//div[@class='react-datepicker__day react-datepicker__day--018']").click()
sel2 = Select(driver.find_element_by_xpath("(//select[@name='title'])[1]"))
sel2.select_by_value("MR")
sel2 = Select(driver.find_element_by_xpath("(//select[@name='gender'])[1]"))
sel2.select_by_value("M")
driver.find_element_by_xpath("(//input[@name='dob'])[1]/..//button").click()
driver.find_element_by_xpath("//div[@class='react-datepicker__year-read-view']").click()
driver.find_element_by_xpath("//div[text()='1990']").click()
driver.find_element_by_xpath("//div[text()='15']").click()
#driver.find_element_by_xpath("(//input[@name='firstName'])[1]").click()
driver.find_element_by_xpath("(//input[@name='firstName'])[1]").send_keys("ADTA")
driver.find_element_by_xpath("(//input[@name='lastName'])[1]").send_keys("ATDA")
driver.find_element_by_xpath("(//input[@name='countryIsdCode'])[1]").send_keys("91")
driver.find_element_by_xpath("(//input[@name='contact'])[1]").send_keys("8617611106")
driver.find_element_by_xpath("(//input[@name='email'])[1]").send_keys("jeet2das2@gmail.com")
# Adding pax details for second ADT [2]
driver.find_element_by_xpath("(//div[@class='link'])[2]").click()
driver.find_element_by_xpath("(//input[@name='passportNumber'])[2]").send_keys(random.getrandbits(30))
sel = Select(driver.find_element_by_xpath("(//select[@name='nationality'])[2]"))
sel.select_by_value("IN")
driver.find_element_by_xpath("(//input[@name='passportExpiry'])[2]/..//button").click()
sel1 = Select(driver.find_element_by_xpath("//select[@class='react-datepicker__year-select']"))
sel1.select_by_value("2030")
driver.find_element_by_xpath("//div[@class='react-datepicker__day react-datepicker__day--018']").click()
sel2 = Select(driver.find_element_by_xpath("(//select[@name='title'])[2]"))
sel2.select_by_value("MR")
sel2 = Select(driver.find_element_by_xpath("(//select[@name='gender'])[2]"))
sel2.select_by_value("M")
driver.find_element_by_xpath("(//input[@name='dob'])[2]/..//button").click()
driver.find_element_by_xpath("//div[@class='react-datepicker__year-read-view']").click()
driver.find_element_by_xpath("//div[text()='1990']").click()
driver.find_element_by_xpath("//div[text()='15']").click()
#driver.find_element_by_xpath("(//input[@name='firstName'])[2]").click()
driver.find_element_by_xpath("(//input[@name='firstName'])[2]").send_keys("ADTB")
driver.find_element_by_xpath("(//input[@name='lastName'])[2]").send_keys("BTDA")
driver.find_element_by_xpath("(//input[@name='countryIsdCode'])[2]").send_keys("91")
driver.find_element_by_xpath("(//input[@name='contact'])[2]").send_keys("8617611106")
driver.find_element_by_xpath("(//input[@name='email'])[2]").send_keys("jeet2das2@gmail.com")
# Adding pax details for first CHD [3]
driver.find_element_by_xpath("(//div[@class='link'])[3]").click()
driver.find_element_by_xpath("(//input[@name='passportNumber'])[3]").send_keys(random.getrandbits(30))
sel = Select(driver.find_element_by_xpath("(//select[@name='nationality'])[3]"))
sel.select_by_value("IN")
driver.find_element_by_xpath("(//input[@name='passportExpiry'])[3]/..//button").click()
sel1 = Select(driver.find_element_by_xpath("//select[@class='react-datepicker__year-select']"))
sel1.select_by_value("2030")
driver.find_element_by_xpath("//div[@class='react-datepicker__day react-datepicker__day--018']").click()
sel2 = Select(driver.find_element_by_xpath("(//select[@name='title'])[3]"))
sel2.select_by_value("MR")
sel2 = Select(driver.find_element_by_xpath("(//select[@name='gender'])[3]"))
sel2.select_by_value("M")
driver.find_element_by_xpath("(//input[@name='dob'])[3]/..//button").click()
driver.find_element_by_xpath("//div[@class='react-datepicker__year-read-view']").click()
driver.find_element_by_xpath("//div[text()='2016']").click()
driver.find_element_by_xpath("//div[text()='15']").click()
#driver.find_element_by_xpath("(//input[@name='firstName'])[3]").click()
driver.find_element_by_xpath("(//input[@name='firstName'])[3]").send_keys("CHDA")
driver.find_element_by_xpath("(//input[@name='lastName'])[3]").send_keys("ADHC")
driver.find_element_by_xpath("(//input[@name='countryIsdCode'])[3]").send_keys("91")
driver.find_element_by_xpath("(//input[@name='contact'])[3]").send_keys("8617611106")
driver.find_element_by_xpath("(//input[@name='email'])[3]").send_keys("jeet2das2@gmail.com")
# Adding pax details for second CHD [4]
driver.find_element_by_xpath("(//div[@class='link'])[4]").click()
driver.find_element_by_xpath("(//input[@name='passportNumber'])[4]").send_keys(random.getrandbits(30))
sel = Select(driver.find_element_by_xpath("(//select[@name='nationality'])[4]"))
sel.select_by_value("IN")
driver.find_element_by_xpath("(//input[@name='passportExpiry'])[4]/..//button").click()
sel1 = Select(driver.find_element_by_xpath("//select[@class='react-datepicker__year-select']"))
sel1.select_by_value("2030")
driver.find_element_by_xpath("//div[@class='react-datepicker__day react-datepicker__day--018']").click()
sel2 = Select(driver.find_element_by_xpath("(//select[@name='title'])[4]"))
sel2.select_by_value("MR")
sel2 = Select(driver.find_element_by_xpath("(//select[@name='gender'])[4]"))
sel2.select_by_value("M")
driver.find_element_by_xpath("(//input[@name='dob'])[4]/..//button").click()
driver.find_element_by_xpath("//div[@class='react-datepicker__year-read-view']").click()
driver.find_element_by_xpath("//div[text()='2016']").click()
driver.find_element_by_xpath("//div[text()='15']").click()
#driver.find_element_by_xpath("(//input[@name='firstName'])[4]").click()
driver.find_element_by_xpath("(//input[@name='firstName'])[4]").send_keys("CHDB")
driver.find_element_by_xpath("(//input[@name='lastName'])[4]").send_keys("BDHC")
driver.find_element_by_xpath("(//input[@name='countryIsdCode'])[4]").send_keys("91")
driver.find_element_by_xpath("(//input[@name='contact'])[4]").send_keys("8617611106")
driver.find_element_by_xpath("(//input[@name='email'])[4]").send_keys("jeet2das2@gmail.com")
# Adding pax details for first INF [5]
driver.find_element_by_xpath("(//div[@class='link'])[5]").click()
driver.find_element_by_xpath("(//input[@name='passportNumber'])[5]").send_keys(random.getrandbits(30))
sel = Select(driver.find_element_by_xpath("(//select[@name='nationality'])[5]"))
sel.select_by_value("IN")
driver.find_element_by_xpath("(//input[@name='passportExpiry'])[5]/..//button").click()
sel1 = Select(driver.find_element_by_xpath("//select[@class='react-datepicker__year-select']"))
sel1.select_by_value("2030")
driver.find_element_by_xpath("//div[@class='react-datepicker__day react-datepicker__day--018']").click()
# sel2 = Select(driver.find_element_by_xpath("(//select[@name='title'])[4]"))
# sel2.select_by_value("MR")
sel2 = Select(driver.find_element_by_xpath("(//select[@name='gender'])[5]"))
sel2.select_by_value("M")
driver.find_element_by_xpath("(//input[@name='dob'])[5]/..//button").click()
driver.find_element_by_xpath("//div[@class='react-datepicker__year-read-view']").click()
driver.find_element_by_xpath("//div[text()='2021']").click()
driver.find_element_by_xpath("//div[text()='15']").click()
driver.find_element_by_xpath("(//input[@name='firstName'])[5]").click()
driver.find_element_by_xpath("(//input[@name='firstName'])[5]").send_keys("INFA")
driver.find_element_by_xpath("(//input[@name='lastName'])[5]").send_keys("AFNI")
#sleep(1)
# driver.find_element_by_xpath("(//input[@name='countryIsdCode'])[5]").send_keys("91")
# driver.find_element_by_xpath("(//input[@name='contact'])[5]").send_keys("8617611106")
# driver.find_element_by_xpath("(//input[@name='email'])[5]").send_keys("jeet2das2@gmail.com")
sel3 = Select(driver.find_element_by_xpath("//select[@name='selectedPassenger']"))
sel3.select_by_value("T2")
# -----------------------------------------------------------------------------------
# Book Order and view Order Detail
driver.find_element_by_xpath("//button[text()='Next']").click()
driver.find_element_by_xpath("//button[text()='Proceed & Book']").click()
ele5 = WebDriverWait(driver, 100).until(
    EC.visibility_of_element_located((By.XPATH, "//button[text()='View Order']")))
driver.find_element_by_xpath("//button[text()='View Order']").click()
# -----------------------------------------------------------------------------------------------------
# Issue Ticket
sleep(1)
mime = WebDriverWait(driver, 100).until(
    EC.invisibility_of_element((By.XPATH, "//div[@class='loader-logo']")))
mim = WebDriverWait(driver, 200).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Issue']")))
driver.find_element_by_xpath("//button[text()='Issue']").click()
mim100 = WebDriverWait(driver, 200).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Proceed']")))
sleep(2)
driver.find_element_by_xpath("//button[text()='Proceed']").click()
mim1 = WebDriverWait(driver, 100).until(
    EC.visibility_of_element_located((By.XPATH, "//span[@class='total-amount-input']")))
driver.find_element_by_xpath("//button[text()='Continue']").click()
driver.find_element_by_xpath("//input[@type='text']").send_keys("a")
driver.find_element_by_xpath("//button[text()='Issue']").click()
mim2 = WebDriverWait(driver, 200).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='View Order']")))
driver.find_element_by_xpath("//button[text()='View Order']").click()
mim3 = WebDriverWait(driver, 100).until(
    EC.visibility_of_element_located((By.XPATH, "(//td[@class='order-section'])[3]")))
# ----------------------------------------------------------------------------------------------------------
# Select seat
mima = WebDriverWait(driver, 100).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Manage seats']/..")))
sleep(1)
driver.find_element_by_xpath("//span[text()='Manage seats']").click()
mim4 = WebDriverWait(driver, 100).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@class='segment-key']")))
# for 1st pax [1]
driver.find_element_by_xpath("(//div[@class='row-cell available color1'])[1]").click()
mim5 = WebDriverWait(driver, 100).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@class='seat-popup']")))
driver.find_element_by_xpath("(//i[@id='unchecked'])[1]").click()
# for 2nd pax [2]
driver.find_element_by_xpath("(//div[@class='row-cell available color1'])[2]").click()
mim6 = WebDriverWait(driver, 100).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@class='seat-popup']")))
driver.find_element_by_xpath("(//i[@id='unchecked'])[2]").click()
# for 3rd pax [3]
driver.find_element_by_xpath("(//div[@class='row-cell available color1'])[3]").click()
mim7 = WebDriverWait(driver, 100).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@class='seat-popup']")))
driver.find_element_by_xpath("(//i[@id='unchecked'])[3]").click()
# for 4th pax [4]
driver.find_element_by_xpath("(//div[@class='row-cell available color1'])[4]").click()
mim8 = WebDriverWait(driver, 100).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@class='seat-popup']")))
driver.find_element_by_xpath("(//i[@id='unchecked'])[4]").click()
driver.find_element_by_xpath("//button[text()='Proceed & Confirm']").click()
mim9 = WebDriverWait(driver, 100).until(
    EC.visibility_of_element_located((By.XPATH, "//button[text()='View Order']")))
driver.find_element_by_xpath("//button[text()='View Order']").click()
mim10 = WebDriverWait(driver, 100).until(
    EC.visibility_of_element_located((By.XPATH, "(//td[@class='order-section'])[3]")))
# --------------------------------------------------------------------------------------------------------------
# Payment for seat (handle refresh order)
sleep(3)
for i in range(0, 2):
    try:
        txt = driver.find_element_by_xpath("//p[@class='text w-4 error']").text
        mima1 = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[text()='Refresh Order']/..")))
        driver.find_element_by_xpath("//button[text()='Refresh Order']").click()
        mima2 = WebDriverWait(driver, 100).until(
            EC.invisibility_of_element_located((By.XPATH, "//div[@class='loader-logo']")))
        mim12 = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[@class='text w-4 error']")))
    except Exception as e:
        driver.find_element_by_xpath("//button[text()='Issue']").click()
    break

# Issue ticket for seat
sleep(2)
mim100 = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//button[text()='Proceed']")))
driver.find_element_by_xpath("//button[text()='Proceed']").click()
mim1 = WebDriverWait(driver, 100).until(
    EC.visibility_of_element_located((By.XPATH, "//span[@class='total-amount-input']")))
driver.find_element_by_xpath("//button[text()='Continue']").click()
driver.find_element_by_xpath("//input[@type='text']").send_keys("a")
driver.find_element_by_xpath("//button[text()='Issue']").click()
mim2 = WebDriverWait(driver, 100).until(
    EC.visibility_of_element_located((By.XPATH, "//button[text()='View Order']")))
driver.find_element_by_xpath("//button[text()='View Order']").click()
mim3 = WebDriverWait(driver, 100).until(
    EC.visibility_of_element_located((By.XPATH, "(//td[@class='order-section'])[3]")))
# ------------------------------------------------------------------------------------------------------------------------------
# Ancillary select
mima = WebDriverWait(driver, 100).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Manage ancillaries']/..")))
sleep(1)
driver.find_element_by_xpath("//button[text()='Manage ancillaries']").click()
mim4 = WebDriverWait(driver, 100).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@class='passenger-details']")))
driver.find_element_by_xpath("//div[@class='passenger-card card open m-b-10']").click()
# For 1st Pax [1]
sleep(1)
driver.find_element_by_xpath("(//div[@class='passenger-card card  m-b-10'])[1]").click()
driver.find_element_by_xpath("(//select[@class='selectbox fw-500'])[1]").click()
sel4 = Select(driver.find_element_by_xpath("(//select[@class='selectbox fw-500'])[1]"))
sel4.select_by_index(1)
sleep(1)
# For 2nd Pax [2]
driver.find_element_by_xpath("(//div[@class='passenger-card card  m-b-10'])[1]").click()
driver.find_element_by_xpath("(//select[@class='selectbox fw-500'])[2]").click()
sel5 = Select(driver.find_element_by_xpath("(//select[@class='selectbox fw-500'])[2]"))
sel5.select_by_index(1)
sleep(1)
# For 3rd Pax [3]
driver.find_element_by_xpath("(//div[@class='passenger-card card  m-b-10'])[1]").click()
driver.find_element_by_xpath("(//select[@class='selectbox fw-500'])[3]").click()
sel6 = Select(driver.find_element_by_xpath("(//select[@class='selectbox fw-500'])[3]"))
sel6.select_by_index(1)
sleep(1)
# For 4th Pax [4]
driver.find_element_by_xpath("(//div[@class='passenger-card card  m-b-10'])[1]").click()
driver.find_element_by_xpath("(//select[@class='selectbox fw-500'])[4]").click()
sel6 = Select(driver.find_element_by_xpath("(//select[@class='selectbox fw-500'])[4]"))
sel6.select_by_index(1)
sleep(1)
driver.find_element_by_xpath("//button[text()='Proceed & Confirm']").click()
mim47 = WebDriverWait(driver, 100).until(
    EC.invisibility_of_element_located((By.XPATH, "//div[@class='loader-logo']")))
mim44 = WebDriverWait(driver, 100).until(
    EC.visibility_of_element_located((By.XPATH, "//button[text()='View Order']")))
driver.find_element_by_xpath("//button[text()='View Order']").click()
mim50 = WebDriverWait(driver, 100).until(
    EC.visibility_of_element_located((By.XPATH, "(//td[@class='order-section'])[3]")))
# ----------------------------------------------------------------------------------------------
# Payment for ancillary (handle refresh order)
sleep(3)
for i in range(0, 2):
    try:
        txt = driver.find_element_by_xpath("//p[@class='text w-4 error']").text
        mima1 = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[text()='Refresh Order']/..")))
        driver.find_element_by_xpath("//button[text()='Refresh Order']").click()
        mima2 = WebDriverWait(driver, 100).until(
            EC.invisibility_of_element_located((By.XPATH, "//div[@class='loader-logo']")))
        mim12 = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[@class='text w-4 error']")))
    except Exception as e:
        driver.find_element_by_xpath("//button[text()='Issue']").click()
    break
# ----------------------------------------------------------------------------------------------------
# Issue ticket for ancillary
sleep(2)
mim101 = WebDriverWait(driver, 100).until(
    EC.visibility_of_element_located((By.XPATH, "//button[text()='Proceed']")))
driver.find_element_by_xpath("//button[text()='Proceed']").click()
mim111 = WebDriverWait(driver, 100).until(
    EC.visibility_of_element_located((By.XPATH, "//span[@class='total-amount-input']")))
driver.find_element_by_xpath("//button[text()='Continue']").click()
driver.find_element_by_xpath("//input[@type='text']").send_keys("a")
sleep(1)
driver.find_element_by_xpath("//button[text()='Issue']").click()
mim222 = WebDriverWait(driver, 100).until(
    EC.visibility_of_element_located((By.XPATH, "//button[text()='View Order']")))
driver.find_element_by_xpath("//button[text()='View Order']").click()
mim99 = WebDriverWait(driver, 100).until(
    EC.visibility_of_element_located((By.XPATH, "(//td[@class='order-section'])[3]")))
# -----------------------------------------------------------------------------------------------------------
# Cancel the order
sleep(1)
driver.find_element_by_xpath("//button[text()='Cancel Order']").click()
miml = WebDriverWait(driver, 100).until(
    EC.visibility_of_element_located((By.XPATH, "//button[text()='Proceed']")))
driver.find_element_by_xpath("//button[text()='Proceed']").click()
mimal3 = WebDriverWait(driver, 100).until(
            EC.invisibility_of_element_located((By.XPATH, "//div[@class='loader-logo']")))
miml5 = WebDriverWait(driver, 100).until(
    EC.visibility_of_element_located((By.XPATH, "//button[text()='Confirm Cancellation']")))
driver.find_element_by_xpath("//button[text()='Confirm Cancellation']").click()
try:
    mimal6 = WebDriverWait(driver, 200).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='loader-logo']")))
except TimeoutException as e:
    print("selenium.common.exceptions.TimeoutException: Message:" + "Failed in Cancelling the order")
miml7 = WebDriverWait(driver, 200).until(
    EC.visibility_of_element_located((By.XPATH, "//button[text()='View Order']")))
driver.find_element_by_xpath("//button[text()='View Order']").click()
miml8 = WebDriverWait(driver, 100).until(
    EC.visibility_of_element_located((By.XPATH, "(//td[@class='order-section'])[3]")))


# --------------------------------------------------------------------------------------------------------------
# try:
#     mimal6 = WebDriverWait(driver, 100).until(
#                 EC.invisibility_of_element_located((By.XPATH, "//div[@class='loader-logo']")))
#     miml7 = WebDriverWait(driver, 100).until(
#         EC.visibility_of_element_located((By.XPATH, "//button[text()='View Order']")))
#     driver.find_element_by_xpath("//button[text()='View Order']").click()
#     miml8 = WebDriverWait(driver, 100).until(
#         EC.visibility_of_element_located((By.XPATH, "(//td[@class='order-section'])[3]")))
# except TimeoutException as e:
#     driver.refresh()
#     driver.find_element_by_xpath("//button[text()='Confirm Cancellation']").click()
#     mimal6 = WebDriverWait(driver, 100).until(
#         EC.invisibility_of_element_located((By.XPATH, "//div[@class='loader-logo']")))
#     miml7 = WebDriverWait(driver, 100).until(
#         EC.visibility_of_element_located((By.XPATH, "//button[text()='View Order']")))
#     driver.find_element_by_xpath("//button[text()='View Order']").click()
#     miml8 = WebDriverWait(driver, 100).until(
#         EC.visibility_of_element_located((By.XPATH, "(//td[@class='order-section'])[3]")))
