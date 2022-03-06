import mouseinfo
import pyautogui
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


# print(mouseinfo.mouseInfo())

chrome_options = Options()
chrome_options.add_argument('--lang=pt-BR')
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)

wait = WebDriverWait(
            driver=driver,
            timeout=10,
            poll_frequency=1,
            ignored_exceptions=[
                NoSuchElementException,
                ElementNotVisibleException,
                ElementNotSelectableException
            ]
        )

driver.get("https://lagged.com.br/jogo/1143/#goog_slotcar_ad")

button_play = wait.until(
    expected_conditions.element_to_be_clickable(
        (By.XPATH, "//button[@id='playnow']")
    )
)
button_play.click()

sleep(3)

# Close ads
pyautogui.press('f12')
sleep(1)
pyautogui.press('f12')

start_button = wait.until(
    expected_conditions.element_to_be_clickable(
        (By.XPATH, "//a[@id='playBtn']")
    )
)

start_button.click()
# pyautogui.moveTo(x=509, y=474, duration=1)
# pyautogui.click()
# Play
#
# pyautogui.moveTo(x=253, y=300, duration=2)
# # Dog
# while True:
#     for c in range(1, 50):
#         pyautogui.click()

    # Upgrades
    # pyautogui.moveTo(x=581, y=240, duration=0.5)
    # pyautogui.click()
    # pyautogui.moveTo(x=253, y=300, duration=0.5)
    # pyautogui.click()