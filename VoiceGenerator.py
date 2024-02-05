import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyperclip


def get_voice(text):
    driver = webdriver.Chrome()
    driver.get("https://www.narakeet.com/languages/polish-text-to-speech/#trynow")
    driver.maximize_window() 
    element = driver.find_element(By.XPATH,'/html/body/main/div/div[2]/div[2]/form/div/div/div[3]/textarea').click()
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("backspace")
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1)
    element = driver.find_element(By.XPATH,'//*[@id="cfgVideoVoice"]/option[8]').click() #wybor glosu
    element = driver.find_element(By.XPATH,'/html/body/main/div/div[2]/div[2]/form/div/div/div[2]/select/option[2]').click() #wybor formatu
    element = driver.find_element(By.XPATH,'//*[@id="trynow"]/form/div/div/div[4]/input[2]').click()
    time.sleep(10)
    element = driver.find_element(By.XPATH,'/html/body/main/div[4]/div/div/div[3]/a[3]').click()
    time.sleep(1) 







