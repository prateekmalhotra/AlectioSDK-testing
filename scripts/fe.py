import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

class WebDriver:
	def __init__(self):
		options = Options()
		options.headless = True
		self.driver = webdriver.Firefox(executable_path="/home/ubuntu/Home/testing/geckodriver", options=options)

	def open_website(self, website):
		self.driver.get(website)

	def press_button(self, button_id):
		wait = WebDriverWait(self.driver, 10)
		wait.until(EC.element_to_be_clickable((By.ID, button_id)))
		button = self.driver.find_elements_by_id(button_id)[-1]
		button.click()

	def enter_text(self, box_id, text):
		wait = WebDriverWait(self.driver, 10)
		wait.until(EC.presence_of_element_located((By.ID, box_id)))
		tbox = self.driver.find_element_by_id(box_id)
		tbox.clear()
		tbox.send_keys(text)

	def get_all_ids(self):
		ids = self.driver.find_elements_by_xpath('//*[@id]')
		for ii in ids:
			print(ii.get_attribute('id'))

	def select_dropdown(self, dropdown_id, option):
		from selenium.webdriver.support.ui import Select
		self.driver.find_element_by_id(dropdown_id).click()
		self.driver.find_element_by_xpath("//mat-option/span[contains(., 'Classification')]").click()

	def upload_file(self, file_path):
		upload_button = self.driver.find_element_by_xpath("//input[@type='file']")
		upload_button.send_keys(file_path)

	def press_button_by_text(self, text):
		buttons = self.driver.find_elements_by_xpath("//*[contains(text(), '{}')]".format(text))

		for button in buttons:
			button.click()

	def press_button_by_value(self, value):
		button = self.driver.find_element_by_xpath("//input[@value='{}']".format(value))
		button.click()

	def enter_text_by_placeholder(self, placeholder, text):
		self.driver.implicitly_wait(1)
		tbox = self.driver.find_element_by_xpath("//input[@placeholder='{}']".format(placeholder))
		tbox.send_keys(text)
		time.sleep(2)
		tbox.send_keys(Keys.RETURN)
		time.sleep(1)

	def close(self):
		self.driver.close()

	def create_project(self, project_name, ip, port, training_size, task_type, json_file_path):
		self.open_website('http://platformfrontendtest-env.eba-m8rbzmhm.us-west-2.elasticbeanstalk.com/mainplatform/onboarding')
		self.enter_text("mat-input-0", project_name)
		self.press_button("next-button")
		self.press_button("mat-radio-2")
		self.press_button("next-button")
		self.press_button("dataset-library-card")
		self.press_button("next-button")
		self.enter_text("ip", ip)
		self.enter_text("port", port)
		self.enter_text("training_size", training_size)
		self.select_dropdown("mat-select-1", task_type)
		self.upload_file(json_file_path)
		self.press_button("next-button")
		self.press_button("mat-radio-6")
		self.press_button("next-button")
		self.press_button_by_text("Submit")

	def create_experiment(self, project_name, experiment_name, nloops, nrecordsperloop):
		self.open_website('http://platformfrontendtest-env.eba-m8rbzmhm.us-west-2.elasticbeanstalk.com/mainplatform/projects')
		self.enter_text_by_placeholder("Filter Rows", project_name)
		self.press_button_by_text("Test")
		self.press_button("experimentation-button")
		self.press_button("newexp-card")
		self.press_button_by_value("Next")
		self.enter_text("mat-input-0", experiment_name)
		self.press_button_by_value("Next")
		self.press_button("activelearning-card")
		self.press_button_by_value("Next")
		self.press_button("manualquery-card")
		self.press_button_by_value("Next")
		self.enter_text("nloops", nloops)
		self.press_button("limits")
		self.press_button("auto-loops")
		self.enter_text("nrecordsperloop", nrecordsperloop)
		self.press_button_by_value("Start")
		self.press_button_by_text("UNCERTAINTY-BASED")
		self.press_button("confidence_based")
		self.press_button("basic_lowest")
		self.press_button_by_value("Train")

if __name__ == "__main__":
	driver = WebDriver()
	driver.create_project("Test_", "54.214.167.54", "5000", "50000", "Classification", "/home/ubuntu/Home/testing/examples/image_classification/cifar10/cif_class_labels.json")
	driver.create_experiment("Test_", "testy", "10", "5000")
