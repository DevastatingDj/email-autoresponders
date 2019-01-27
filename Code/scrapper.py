import re
import time
import classify
import knowledgebase
import translate
from selenium import webdriver
from support import remove
from selenium.webdriver.common.keys import Keys
"""
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options=options, executable_path=r'E:/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(10)
driver.get("https://www.gmail.com")

# Login

userid = driver.find_element_by_xpath('//*[@id="identifierId"]')
userid.click()
userid.send_keys('sharma.dj1998@gmail.com')

nextbutton1 = driver.find_element_by_xpath('//*[@id="identifierNext"]/content')
nextbutton1.click()

time.sleep(3)
passwd = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
passwd.click()
passwd.send_keys('commandos4jjxb')

nextbutton2 = driver.find_element_by_xpath('//*[@id="passwordNext"]/content/span')
nextbutton2.click()

# Email Extraction

newmails = driver.find_elements_by_xpath('//*[@class="zF"]')
newmails = remove(newmails)
newmails[0].click()
time.sleep(3)
content = driver.find_element_by_xpath('//div[@class="adn ads"]')
content = content.get_attribute('innerHTML')
content = str(content)

matchObj = re.sub(r'<.*?>', "", content)
l = matchObj.split("ago)")
extracted_mail = l[-1]
moreStuff = l[0]
# extracted mail
print(extracted_mail)
name = re.match(r'[\w ]*', moreStuff)
name = name.group()
# name = name of user
e = moreStuff.split('&')
email_id = e[1].split(';')[-1]
# email_id
extracted_mail = translate.translate_to_english(extracted_mail)
"""
extracted_mail = "Hello, While I working on my computer yesturday my mouse wheel just suddenly stopped working.What could be the reason?. Do i have to be worried? I am using a windows operating system. Please Help. Thank you."
# Generating Tags and querying questions and their answers from KB
extracted_mail_tags = classify.generate_tags(extracted_mail)
print(extracted_mail_tags)
l = knowledgebase.get_question_answers()
questions = l[0]
answers = l[1]


# Comparing tags and finding the solution
count = 0
maxcount = 0
for i in range(len(questions)):
    for j in extracted_mail_tags:
        if j in list(set(classify.generate_tags(questions[i]))):
            count += 1
            break
    if count > maxcount:
        index = i
    count = 0

print(answers[index])

"""

# Reply
if index:
    reply = driver.find_element_by_xpath('//span[@class="ams bkH"]')
    reply.click()

    write = driver.find_element_by_xpath('//div[@class="Am aO9 Al editable LW-avf"]')
    write.send_keys(answers[index])
    write.send_keys(Keys.CONTROL + Keys.RETURN)
else:
    reply = driver.find_element_by_xpath('//span[@class="ams bkH"]')
    reply.click()

    write = driver.find_element_by_xpath('//div[@class="Am aO9 Al editable LW-avf"]')
    write.send_keys("Cannot Find Answer")
    write.send_keys(Keys.CONTROL + Keys.RETURN)

"""