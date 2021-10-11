from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from browser import Browser

element_to_drag="draggable"
element_to_drop="droppable"





class HomePage(Browser):
    # Home Page Actions


    def drag_and_dop(self):
        action = ActionChains(self.driver)
        source = self.driver.find_element_by_id(element_to_drag)
        target = self.driver.find_element_by_id(element_to_drop)
        action.drag_and_drop(source, target).perform()

    def return_target_message(self):
        target = self.driver.find_element_by_id("droppable")
        return target.text

    def __init__(self, driver):
        self.driver = driver


