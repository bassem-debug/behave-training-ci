

class Browser(object):
    def __init__(self, driver):
        self.driver = driver
    def return_target_message(self):
        target = self.driver.find_element_by_id("droppable")
        return target.text