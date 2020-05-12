from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase
class NewVisitorTest(LiveServerTestCase):#(1)
	def setUp(self):#(3)
		self.browser = webdriver.Firefox()
	def test_can_start_a_list_and_retrive_it_later(self):
		self.browser.get(self.live_server_url)
	def tearDown(self):#(3)
		self.browser.quit()
		
	def check_for_row_in_list_table(self,row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text,[row.text for row in rows])
	def test_can_start_a_list_and_retrieve_it_later(self):#(2)
		#Edith has heard about a cool new online to-do app
		#she goes to check out its homepages
		self.browser.get(self.live_server_url)
		#she notices the page title and header mention to-do lists
		self.assertIn('To-Do',self.browser.title)#(4)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do',header_text)#(5)
		#she is invite to enter a to-do item straight away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)
		#she types "Buy peocock feathers" into a text box(Ediths hobby
		#is tying fly-fishing lures)
		inputbox.send_keys('Buy peacock feathers')
		#when she hits enter,the page updates,and now the page lists
		#"1":Buy peocock feathers" as an item in a to-do list
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)
		self.check_for_row_in_list_table('1:Buy peacock feathers')
		#self.assertTrue(
		#	any(row.text == '1:Buy peacock feathers' for row in rows),
		#	f"New to-do item did not appear in table. Contents were:\n{table.text}"
		#)

		#There is still a text box inviting her to add another item.She
		#enters "use peocock feathers to make a fly"(Edith is very methodical)
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)
		#The page updates again, and now shows both items on her list
		self.check_for_row_in_list_table('1:Buy peacock feathers')
		self.check_for_row_in_list_table('2:Use peacock feathers to make a fly')
		#Edith wonders whether the site will  remember her list.
		#Then she sees that the site has generated a unique url for her --
		#There is some explanatory text to the effect
		self.fail('finish the test')
		#she visits that url -her to-do list is still there

		#satisfied ,she goes back to sleep

		#browser.quit()



