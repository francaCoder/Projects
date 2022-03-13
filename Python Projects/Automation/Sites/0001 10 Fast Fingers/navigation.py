from selenium import webdriver
from time import sleep
import pyautogui

while True:
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.get("https://10fastfingers.com/typing-test/portuguese")
    sleep(5)
    cookies = driver.find_element_by_xpath("//button[@id='CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll']")
    cookies.click()
    sleep(5)
    for c in range(300, 0, -1):
        if c == 1:
            break
        word = driver.find_element_by_xpath("//span[@class='highlight']")
        input_word = driver.find_element_by_xpath("//input[@id='inputfield']")
        input_word.send_keys(word.text)
        pyautogui.hotkey('space')

    accuracy = driver.find_element_by_xpath("//tr[@id='accuracy']//td[@class='value']")
    correct_words = driver.find_element_by_xpath("//tr[@id='correct']//td[@class='value']")
    wrong_words = driver.find_element_by_xpath("//tr[@id='wrong']//td[@class='value']")

    print(f"-=-=-=-= Result =-=-=-=-")
    print(f"Your accuracy was {accuracy.text}.")
    print(f"You got {correct_words.text} words right.")
    print(f"Wrong Words → {wrong_words.text}")
    print("-=-=-=-=-=-=-=-=-=-=-=-")

    print()
    sleep(10)
