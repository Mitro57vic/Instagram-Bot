from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

andere_bereits_geschriebene_nachrichten = 0
meine_bereits_geschriebenen_nachrichten = 0
nachrichten_liste = []

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

def schreibe_nachricht(message):
    textbox_div = browser.find_element(By.XPATH, '//div[@aria-label="Message"]')
    for x in message:
        textbox_div.send_keys(x)
    textbox_div.send_keys(Keys.ENTER)

def analysiere_nachrichten(nachrichten_liste):
        global meine_bereits_geschriebenen_nachrichten
        if (len(nachrichten_liste) > meine_bereits_geschriebenen_nachrichten):
            schreibe_nachricht(nachrichten_liste[meine_bereits_geschriebenen_nachrichten])
            meine_bereits_geschriebenen_nachrichten += 1
            return False
        else:
            return True

def warte_auf_neue_nachrichten(erste_nachricht):
    neue_nachrichten = browser.find_elements(By.XPATH, '//div[@class="x6prxxf x1fc57z9 x1yc453h x126k92a xzsf02u"]')
    global andere_bereits_geschriebene_nachrichten
    global meine_bereits_geschriebenen_nachrichten
    global nachrichten_liste
    if (erste_nachricht):
        analysiere_nachrichten(nachrichten_liste)
        return False
    n = 0
    if (len(andere_bereits_geschriebene_nachrichten) < len(neue_nachrichten)):     
        n = len(neue_nachrichten) - len(andere_bereits_geschriebene_nachrichten)
        n -= meine_bereits_geschriebenen_nachrichten
    if (n > 0):
        if analysiere_nachrichten(nachrichten_liste):
            return True
    return False

def FindUsersWithDMs(People_In_DMs, nachrichten_liste):
    for x in People_In_DMs:
        x.click()
        sleep(5)
        global andere_bereits_geschriebene_nachrichten
        global meine_bereits_geschriebenen_nachrichten
        andere_bereits_geschriebene_nachrichten = browser.find_elements(By.XPATH, '//div[@class="x6prxxf x1fc57z9 x1yc453h x126k92a xzsf02u"]')
        meine_bereits_geschriebenen_nachrichten = 0 
        erste_nachricht = True
        while (True):
            sleep(.5)
            if (warte_auf_neue_nachrichten(erste_nachricht)):
                break
            erste_nachricht = False

def pruefe_nachrichten(nachrichten_liste):
    browser.find_element(By.XPATH, '//a[@href="/direct/inbox/"]').click()
    sleep(2)
    People_Writing = browser.find_elements(By.XPATH, '//div[@class="x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx x2lwn1j xeuugli x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x87ps6o x1lku1pv x1a2a7pz x168nmei x13lgxp2 x5pf9jr xo71vjh x1lliihq xdj266r x11i5rnm xat24cr x1mh8g0r xg6hnt2 x18wri0h x1l895ks xbbxn1n xxbr6pl x1y1aw1k xwib8y2"]')
    FindUsersWithDMs(People_Writing, nachrichten_liste)
    sleep(2)

def frage_anzahl_nachrichten():
    user_input = input("Wie viele Nachrichten wollen Sie schreiben: ")
    if user_input.isdigit():
        return int(user_input)
    else:
        print("Die Eingabe muss aus Zahlen bestehen!")
        return frage_anzahl_nachrichten()
    
def definiere_nachrichten(anzahl_nachrichten):
    nachrichten_list = []
    for x in range(anzahl_nachrichten):
        nachricht = "Bitte geben Sie ihre Nachricht ein: "
        nachricht_input = input(nachricht)
        nachrichten_list.append(nachricht_input)
    return nachrichten_list

    
nummer = frage_anzahl_nachrichten()
nachrichten_liste = definiere_nachrichten(nummer)
print("Bot Startet (Beenden mit Ctrl+C)")

browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

browser.implicitly_wait(5)

browser.get('https://www.instagram.com/')

sleep(2)
Login()

sleep(5)
pruefe_nachrichten(nachrichten_liste)

browser.close()