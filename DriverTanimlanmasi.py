from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ChromeDriver:
    import time

    def __init__(self, headless=False):
        self.options = Options()
        self.options.headless = headless
        self.options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=self.options)

    def quit(self):
        self.driver.quit()


chrome = ChromeDriver()


def dummy():
    pass

    # Ana pencereye geri dönün
    # chrome.driver.switch_to.window(main_window_handle)


def generating_data_graph(bucketName, graphName, bucketNameSecondary, graphNameSecondary):

    # go to link
    chrome.driver.get("http://akbank-shippingtest.adqura.com/prweb/")

    # Wait until the login form is visible
    login_form = WebDriverWait(chrome.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "txtUserID"))
    )

    # Fill in the username and password fields
    chrome.driver.find_element(By.ID, "txtUserID").send_keys("caglar.sinik@adqura.com")
    chrome.driver.find_element(By.ID, "txtPassword").send_keys("Akbank2027*")

    # Click the login button
    chrome.driver.find_element(By.ID, "sub").click()

    # Wait until the home page is loaded
    home_page = WebDriverWait(chrome.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,
                                          "#RULE_KEY > div > div > div > div > div > div > div > div.content-item.content-label.item-1.remove-top-spacing.remove-left-spacing.standard_dataLabelWrite.dataLabelWrite.flex.flex-row"))
    )
    chrome.driver.find_element(By.CSS_SELECTOR,
                               "#RULE_KEY > div.flex.content.layout-content-inline_middle.content-inline_middle.set-width-auto.header-layout.workspace-header.dev-studio-header > div.content-item.content-field.item-6.flex.flex-row.launch-portals.no-spacing.dataValueWrite > span > a").click()

    home_page = WebDriverWait(chrome.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,
                                          "#pyNavigation1664381971134 > li.menu-item.menu-item-enabled.menu-item-active > a > span > span"))
    )

    # Launch Portal
    chrome.driver.implicitly_wait(10)
    chrome.driver.find_element(By.LINK_TEXT, "Launch portal").click()
    chrome.time.sleep(2)

    # STF
    chrome.driver.implicitly_wait(10)
    chrome.driver.find_element(By.LINK_TEXT, "STF").click()
    chrome.time.sleep(2)

    # Yeni pencereye geçin
    chrome.driver.switch_to.window(chrome.driver.window_handles[-1])

    # Yeni pencereye yapılabilecek işlemleri gerçekleştirin
    # ...
    crm_portal = WebDriverWait(chrome.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,
                                          "#RULE_KEY > div > div.content-item.content-label.item-2.flex.flex-row.standard_label_for_heading_dataLabelWrite.margin-l-1x.dataLabelWrite.standard_label_for_heading_dataLabelWrite"))
    )

    data_designer = WebDriverWait(chrome.driver, 10).until(
        EC.visibility_of_element_located((By.LINK_TEXT,
                                          "Data Designer"))
    )

    # Data Generator
    chrome.driver.implicitly_wait(10)
    chrome.driver.find_element(By.LINK_TEXT, "Data Generator").click()
    chrome.time.sleep(2)

    # Click Bucket Name and Write it
    chrome.driver.implicitly_wait(10)
    chrome.driver.find_element(By.NAME, "$PGeneratorTab$pBucketName").click()
    chrome.driver.find_element(By.NAME, "$PGeneratorTab$pBucketName").send_keys(bucketName)
    chrome.time.sleep(2)

    # Click one more time
    chrome.driver.implicitly_wait(10)
    chrome.driver.find_element(By.XPATH, "//span[.='" + bucketName + "']").click()
    chrome.time.sleep(2)

    # Click GraphName and Write GraphName
    chrome.driver.implicitly_wait(10)
    chrome.driver.find_element(By.NAME, '$PGeneratorTab$pGraphName').click()
    chrome.driver.find_element(By.NAME, '$PGeneratorTab$pGraphName').send_keys(graphName)
    chrome.driver.find_element(By.XPATH, "//span[.='" + graphName + "']").click()
    chrome.time.sleep(2)

    # Enter Number of Records
    chrome.driver.implicitly_wait(10)
    chrome.driver.find_element(By.NAME, '$PGeneratorTab$pRecordCount').click()
    chrome.driver.find_element(By.NAME, '$PGeneratorTab$pRecordCount').send_keys("1")
    chrome.time.sleep(2)

    # Refresh one time
    chrome.driver.implicitly_wait(10)
    chrome.driver.find_element(By.XPATH, "//button[.='Refresh']").click()
    chrome.time.sleep(5)

    # Click Generate Button
    chrome.driver.implicitly_wait(10)
    chrome.driver.find_element(By.XPATH, "//button[.='Generate']").click()
    chrome.time.sleep(2)

    # complete text must be shown on screen for specified graph the latest generation
    locator = (By.XPATH, '//*[@id="$PpgRepPgSubSectionStatusB$ppxResults$l1"]/td[4]/div/span')
    for i in range(10):

        status_check = chrome.driver.find_element(*locator).text

        # Refresh
        chrome.driver.implicitly_wait(10)
        chrome.driver.find_element(By.XPATH, "//button[.='Refresh']").click()
        chrome.time.sleep(1)

        if status_check == "Complete":
            break
        else:
            chrome.time.sleep(3)

    # clear bucket name
    chrome.driver.implicitly_wait(10)
    chrome.driver.find_element(By.NAME, "$PGeneratorTab$pBucketName").click()
    chrome.time.sleep(2)

    # Click down arrow
    chrome.driver.implicitly_wait(10)
    chrome.driver.find_element(By.XPATH, '//*[@id="RULE_KEY"]/div/div[1]/div[3]/div/div[1]/div/div/button/i').click()
    chrome.time.sleep(2)

    # click clear 'x' button
    chrome.driver.implicitly_wait(10)
    chrome.driver.find_element(By.XPATH, '//*[@id="autocompleAG_Clear_Icon"]').click()
    chrome.time.sleep(2)

    # Refresh
    chrome.driver.implicitly_wait(10)
    chrome.driver.find_element(By.XPATH, "//button[.='Refresh']").click()
    chrome.time.sleep(2)

    # Click Bucket Name and Write it
    chrome.driver.implicitly_wait(10)
    chrome.driver.find_element(By.NAME, "$PGeneratorTab$pBucketName").click()
    chrome.driver.find_element(By.NAME, "$PGeneratorTab$pBucketName").send_keys(bucketNameSecondary)
    chrome.time.sleep(2)

    # Click one more time
    chrome.driver.implicitly_wait(10)
    chrome.driver.find_element(By.XPATH, "//span[.='" + bucketNameSecondary + "']").click()
    chrome.time.sleep(2)

    # Click GraphName and Write GraphName
    chrome.driver.implicitly_wait(10)
    chrome.driver.find_element(By.NAME, '$PGeneratorTab$pGraphName').click()
    chrome.driver.find_element(By.NAME, '$PGeneratorTab$pGraphName').send_keys(graphNameSecondary)
    chrome.driver.find_element(By.XPATH, "//span[.='" + graphNameSecondary + "']").click()
    chrome.time.sleep(2)

    # Refresh one time
    chrome.driver.implicitly_wait(10)
    chrome.driver.find_element(By.XPATH, "//button[.='Refresh']").click()
    chrome.time.sleep(2)

    # Click Generate Button
    chrome.driver.implicitly_wait(10)
    chrome.driver.find_element(By.XPATH, "//button[.='Generate']").click()
    chrome.time.sleep(2)

    for i in range(10):

        status_check = chrome.driver.find_element(*locator).text

        # Refresh
        chrome.driver.implicitly_wait(10)
        chrome.driver.find_element(By.XPATH, "//button[.='Refresh']").click()
        chrome.time.sleep(1)

        if status_check == "Complete":
            break
        else:
            chrome.time.sleep(3)

    chrome.time.sleep(3)
