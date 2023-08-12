############################################
# recomended companion:
# testingChecklist.pdf
############################################

import myapp
import unittest
import os

class TestMyApp(unittest.TestCase):
	
	############################
	# TESTING EXISTANCE
	############################
	
	# 1. can we access the app?
	def test_appExists(self):
		app = myapp.Pythagorean()
		self.assertIsNotNone(app)
	
	# 2. can we access the graphic interface?
	def test_guiExists(self):
		app = myapp.Pythagorean()
		gui = app.build() # returns a UserInterface object
		self.assertIsNotNone(gui)
		
	# 3. does gui have a method called callback?
	def test_callbackExists(self):
		app = myapp.Pythagorean()
		gui = app.build()
		self.assertIsNotNone(gui.callback)
	
	# 4. does gui have a method called pythagorean?
	def test_pythagoreanExists(self):
		app = myapp.Pythagorean()
		gui = app.build()
		self.assertIsNotNone(gui.pythagorean)

	# 5. can we access the widgets?
	def test_widgetsExists(self):
		app = myapp.Pythagorean()
		gui = app.build()
		widgets = gui.children
		
		print("PRINTING UI WIDGETS...")
		[print(idx,val) for idx,val in enumerate(widgets)]
		
		# are there widgets?
		self.assertIsNotNone(widgets)
		# are there enough widgets?
		self.assertEqual(len(widgets), 5)
	
	# 6. is there a button widget at index 0 of gui?
	def test_buttonExists(self):
		app = myapp.Pythagorean()
		gui = app.build()
		widgets = gui.children
		
		# we find which UI element is the button via index:
		print("PRINTING UI WIDGETS...")
		[print(idx, val) for idx, val in enumerate(gui.children)]
		
		# fetch button element
		button = widgets[0]	
		self.assertIsNotNone(button)
		
	# 7. can we access the assets? (images, databases, none-code files)
	def test_assetsExist(self):
	
		# fetch current folder (where test_myapp.py lives)
		cwd = os.getcwd()
		# generate a path to both image assets
		img1 = os.path.join(cwd, "assets", "diagram.png")
		img2 = os.path.join(cwd, "assets", "logo.png")
		# assert that path contains accsssible files
		self.assertEqual(os.path.isfile(img1), True)
		self.assertEqual(os.path.isfile(img2), True)

	# 8. does the pythagorean method of gui always returns a dictionary?
	def test_dictExists(self):
		app = myapp.Pythagorean()
		gui = app.build()
		output = gui.pythagorean()
		# returns a dictionary
		self.assertIsInstance(output, dict)
		# returns a dictionary of strings
		for key, val in output.items():
			self.assertIsInstance(key, str)
			self.assertIsInstance(val, str)

	# 9. test ideal input for inputs A and B
	def test_inputAB(self):
		app = myapp.Pythagorean()
		gui = app.build()
		widgets = gui.children		
		# fetch inner GridLayout
		inner_widgets = widgets[1].children
		
		print("PRINTING NESTED WIDGETS...")
		[print(idx,val) for idx,val in enumerate(inner_widgets)]
		
		# fetch inputs A and B
		inputA = inner_widgets[4]
		inputB = inner_widgets[2]
		# update their values
		inputA.text = "3.0"
		inputB.text = "4.0"
		# fetch output
		output = gui.pythagorean()
		# assert we get the expected output
		self.assertEqual(output, {"c": "5.0"})

	# 10. test accidental input for inputs A, B and C
	def test_inputABC(self):
		app = myapp.Pythagorean()
		gui = app.build()
		widgets = gui.children
		inner_widgets = widgets[1].children
		# fetch all inputs
		inputA = inner_widgets[4]
		inputB = inner_widgets[2]
		inputC = inner_widgets[0]
		# insert their values
		inputA.text = "3"
		inputB.text = "4"
		inputC.text = "5"
		# fetch output
		output = gui.pythagorean()
		# assert we get the correct error message
		self.assertEqual(output, {"error": "if you already know ALL sides then you don't need me!"})

	# 11. test mathematically wrong input B
	def test_inputABWrong(self):
		app = myapp.Pythagorean()
		gui = app.build()
		widgets = gui.children
		inner_widgets = widgets[1].children
		inputA = inner_widgets[4]
		inputB = inner_widgets[2]
		inputA.text = "3"
		# a length metric can only be positive!
		# this input should not be accepted!
		inputB.text = "-4"
		output = gui.pythagorean()
		
		# uncomment the assertion to fail the test and try fixing the app!
		#self.assertNotEqual(output, {"c": "5.0"})
		
	# 12. test malicius input for input A
	def test_inputMalicius(self):
		app = myapp.Pythagorean()
		gui = app.build()
		widgets = gui.children	
		inner_widgets = widgets[1].children
		# fetch inputs A and B
		inputA = inner_widgets[4]
		inputB = inner_widgets[2]
		# update their values
		inputA.text = "banana"
		inputB.text = "4.0"
		
		# uncomment the lines below to fail the test and try fixing the app!
		#output = gui.pythagorean()
		#self.assertNotEqual(output, {"c": "5.0"})

# run unittests
if __name__ == '__main__':
	unittest.main()
	
############################################
# code by: mariya sha
# aka: the gal from python simplified 
# date: august 2023

# please share, adapt, correct, refine, clone, pull, commit and use this code as your heart desires!
############################################
