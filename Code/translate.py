from selenium import webdriver
import time


def translate_to_english(mail):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options=options, executable_path=r'E:/chromedriver_win32/chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get("https://translate.google.co.in")

    text_box = driver.find_element_by_xpath('//*[@id="source"]')
    text_box.send_keys(mail)

    time.sleep(3)

    new_text = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div')
    return new_text.text

