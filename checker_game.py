from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

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


# Find all spaces with orange pieces
def find_orange_spaces():
    orange_side_board_space_list = []
    orange_space_list = []
    for i in range(0, 8):
        for j in range(0, 3):
            name = 'space' + str(i) + str(j)
            orange_side_board_space_list.append(name)
    for name in orange_side_board_space_list:
        element = driver.find_element(By.NAME, name)
        if "you" in element.get_attribute("src"):
            orange_space_list.append(name)
    print('Orange space list: ', orange_space_list)
    return orange_space_list


# Find eligible spaces to move to
def next_space_to_move(space):
    move_to_list = []
    row = int(space[-1])
    column = int(space[-2])
    if column == 0:
        move_to_space_left: str = "space" + str(column + 1) + str(row + 1)
        element_left = driver.find_element(By.NAME, move_to_space_left)
        if "gray" in element_left.get_attribute("src"):
            move_to_list.append(move_to_space_left)
    elif column == 7:
        move_to_space_right: str = "space" + str(column - 1) + str(row + 1)
        element_right = driver.find_element(By.NAME, move_to_space_right)
        if "gray" in element_right.get_attribute("src"):
            move_to_list.append(move_to_space_right)
    else:
        move_to_space_left: str = "space" + str(column + 1) + str(row + 1)
        move_to_space_right: str = "space" + str(column - 1) + str(row + 1)
        element_left = driver.find_element(By.NAME, move_to_space_left)
        element_right = driver.find_element(By.NAME, move_to_space_right)
        if "gray" in element_left.get_attribute("src"):
            move_to_list.append(move_to_space_left)
        if "gray" in element_right.get_attribute("src"):
            move_to_list.append(move_to_space_right)
    return move_to_list


# make legal move
def make_move(space_list):
    orange_move_space = random.choice(space_list)
    print('First random orange piece: ', orange_move_space)
    move_to_list = next_space_to_move(orange_move_space)
    while len(move_to_list) == 0:
        orange_move_space = random.choice(space_list)
        move_to_list = next_space_to_move(orange_move_space)
        print('random orange piece: ', orange_move_space)
    print('Next space to move list: ', move_to_list)
    space_to_move_to = random.choice(move_to_list)
    print('Space to move to: ', space_to_move_to)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(move_message))
    driver.find_element(By.NAME, orange_move_space).click()
    driver.find_element(By.NAME, space_to_move_to).click()
    time.sleep(2)
    space_list.remove(orange_move_space)
    space_list.append(space_to_move_to)
    print('Updated orange space list: ', space_list)
    return space_list


orange_space_list = find_orange_spaces()
for i in range(0,5):
    orange_space_list = make_move(orange_space_list)
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

