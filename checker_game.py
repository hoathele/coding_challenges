from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

move_message = (By.ID, "message")

# Navigate to the website
driver = webdriver.Chrome()  # Insert your chromedriver path
driver.get("https://www.gamesforthebrain.com/game/checkers/")

# Confirm that the site is up
if "Checkers" in driver.title:
    print("Website is up.")
else:
    print("Website is NOT up!")
    driver.quit()
    exit()

# Select an orange piece make the 1st move
WebDriverWait(driver,10).until(EC.visibility_of_element_located(move_message))
driver.find_element(By.NAME, "space62").click()
driver.find_element(By.NAME, "space73").click()
time.sleep(2)

# Orange makes 2nd move
WebDriverWait(driver,10).until(EC.visibility_of_element_located(move_message))
driver.find_element(By.NAME, "space42").click()
driver.find_element(By.NAME, "space53").click()
time.sleep(2)

# Orange makes 3rd move
WebDriverWait(driver,10).until(EC.visibility_of_element_located(move_message))
driver.find_element(By.NAME, "space22").click()
driver.find_element(By.NAME, "space33").click()
time.sleep(2)

# Orange makes 4th move
WebDriverWait(driver,10).until(EC.visibility_of_element_located(move_message))
driver.find_element(By.NAME, "space02").click()
driver.find_element(By.NAME, "space13").click()
time.sleep(2)

# Orange makes 5th move
WebDriverWait(driver,10).until(EC.visibility_of_element_located(move_message))
driver.find_element(By.NAME, "space71").click()
driver.find_element(By.NAME, "space62").click()
time.sleep(2)


# Restart the game
restart_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/p[2]/a[1]")
restart_button.click()
time.sleep(2)

# Confirm that restarting had been successful

move_message = WebDriverWait(driver,10).until(EC.visibility_of_element_located(move_message))
if move_message.text == "Select an orange piece to move.":
    print("Restart successful.")
else:
    print("Restart failed.")

# Close the browser
time.sleep(2)
driver.quit()
