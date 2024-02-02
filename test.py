from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

"""
bot = Bot()

bot.login(username="lernatelier1303", password="imsprojekt")
"""

def Login():
    cookie_button = browser.find_element(By.XPATH, '//button[text()="Allow all cookies"]')
    cookie_button.click()
    sleep(5)
    username_input = browser.find_element(By.NAME, 'username')
    password_input = browser.find_element(By.NAME, 'password')
    username_input.send_keys("lernatelierprojekt@gmail.com")
    password_input.send_keys("imsprojekt")
    sleep(2)
    login_button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    login_button.click()
    sleep(10)
    Save_info = browser.find_element(By.XPATH, '//button[text()="Save info"]')
    Save_info.click()
    sleep(5)
    Notification_button = browser.find_element(By.XPATH, '//button[text()="Not Now"]')
    Notification_button.click()

def WriteMessage(message):
    textBoxField = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]')
    textBoxField.send_keys("adlfjaldfeoijd")
    sleep(2)
    textBoxField.send_keys(Keys.CONTROL + "a")
    textBoxField.send_keys(Keys.DELETE)
    textBoxField.send_keys(message)
    textBoxField.send_keys(Keys.ENTER)
    sleep(2)

def AnalyseMessages(other_messages_analyse):
    for idx, x in enumerate(other_messages_analyse):
        if idx == 0:
            WriteMessage("Yo")
        elif idx == 1:
            try:
                WriteMessage("Heyyy")
            except:
                print("failed")

def FindUsersWithDMs(People_In_DMs):
    for x in People_In_DMs:
        x.click()
        sleep(2)
        messages = browser.find_elements(By.XPATH, '//div[@class="x6prxxf x1fc57z9 x1yc453h x126k92a xzsf02u"]')
        AnalyseMessages(messages)

def CheckMessages():
    browser.find_element(By.XPATH, '//a[@href="/direct/inbox/"]').click()
    sleep(2)
    People_Writing = browser.find_elements(By.XPATH, '//div[@class="x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx x2lwn1j xeuugli x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x87ps6o x1lku1pv x1a2a7pz x168nmei x13lgxp2 x5pf9jr xo71vjh x1lliihq xdj266r x11i5rnm xat24cr x1mh8g0r xg6hnt2 x18wri0h x1l895ks xbbxn1n xxbr6pl x1y1aw1k xwib8y2"]')
    FindUsersWithDMs(People_Writing)
    sleep(2)

def CheckNotifications():
    browser.find_element(By.XPATH, '//a[@href="/#"]').click()
    sleep(2)

browser = webdriver.Firefox()

browser.implicitly_wait(5)

browser.get('https://www.instagram.com/')

sleep(2)
Login()

sleep(5)
CheckMessages()


sleep(50)
browser.close()