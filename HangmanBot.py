from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from random import choice

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://abenner2000.github.io/Hangman")

difficulty = driver.find_element_by_class_name("OptionMenu")
time.sleep(1) #Allot time
difficulty.click()
time.sleep(1) #Allot time

alert = driver.switch_to.alert
alert.accept()
time.sleep(1) #Allot time for next page load

letterA = driver.find_elements_by_css_selector("div.LetterBox")[0]
letterA.click()
time.sleep(1) #Allot time for next page load

letterE = driver.find_elements_by_css_selector("div.LetterBox")[4]
letterE.click()
time.sleep(1) #Allot time for next page load

letterI = driver.find_elements_by_css_selector("div.LetterBox")[8]
letterI.click()
time.sleep(1) #Allot time for next page load

letterO = driver.find_elements_by_css_selector("div.LetterBox")[14]
letterO.click()
time.sleep(1) #Allot time for next page load

letterU = driver.find_elements_by_css_selector("div.LetterBox")[20]
letterU.click()
time.sleep(1) #Allot time for next page load

nextLetterNumber = 0
excludedList = [0,4,8,14,20]
def getNewNum(excludedList):
    nextLetterNumber = choice([i for i in range(0,25) if i not in excludedList])
    excludedList.append(nextLetterNumber)
    return nextLetterNumber

flag = False
while flag == False:
    try:
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(1) #Allot time for next page load
        flag = True
    except:
        nextLetterNumber = getNewNum(excludedList)
        nextLetter = driver.find_elements_by_css_selector("div.LetterBox")[nextLetterNumber]
        nextLetter.click()
        time.sleep(1) #Allot time for next page load
    

    

time.sleep(4)

driver.close()

#driver.title retrieves title of website
#driver.close() closes tab
#driver.quit() closes browser
