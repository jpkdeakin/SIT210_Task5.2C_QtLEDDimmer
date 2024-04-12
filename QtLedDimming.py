import RPi.GPIO as GPIO
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
import sys

# Setting up class for the GUI Window.
class MyWindow(QMainWindow):

	# Constructor
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(100,100,300,200)
        self.setWindowTitle("SIT Task 5.2C")
        self.initUI()
        self.initGPIO()
    
	# Setup GPIO's and PWMs
    def initGPIO(self):
		# General GPIO Stuff
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
		
		# Setting up Outputs
        GPIO.setup(2,GPIO.OUT)
        GPIO.setup(3,GPIO.OUT)
        GPIO.setup(4,GPIO.OUT)
		
		# Allocating PWMs
        self.led_red = GPIO.PWM(2, 50)
        self.led_orange = GPIO.PWM(3, 50)
        self.led_green = GPIO.PWM(4, 50)
        self.led_red.start(0)
        self.led_orange.start(0)
        self.led_green.start(0)
        
    # Setup User Interface Devices
    def initUI(self):
	
		# Text Labels
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("LED Red : 0")
        self.label1.move(120,20)
 
        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText("LED Orange : 0")
        self.label2.move(120,60)
        
        self.label3 = QtWidgets.QLabel(self)
        self.label3.setText("LED Green : 0")
        self.label3.move(120,100)
		
        # Update label sizes to match text
        self.update()
		
		# Brightness Sliders
        self.sldr_red = QtWidgets.QSlider(Qt.Horizontal, self)
        self.sldr_red.setRange(0,100)
        self.sldr_red.move(10,20)
        self.sldr_red.valueChanged.connect(self.update_red)        

        self.sldr_orange = QtWidgets.QSlider(Qt.Horizontal, self)
        self.sldr_orange.setRange(0,100)
        self.sldr_orange.move(10,60)
        self.sldr_orange.valueChanged.connect(self.update_orange)

        self.sldr_green = QtWidgets.QSlider(Qt.Horizontal, self)
        self.sldr_green.setRange(0,100)
        self.sldr_green.move(10,100)
        self.sldr_green.valueChanged.connect(self.update_green)
        

        
		
	# Update red LED brightness
    def update_red(self):
        value = self.sldr_red.value()
        self.led_red.ChangeDutyCycle(value)
        self.label1.setText(f"LED Red: {value}")
        self.update()
        
	# Update orange LED brightness
    def update_orange(self):
        value = self.sldr_orange.value()
        self.led_orange.ChangeDutyCycle(value)
        self.label2.setText(f"LED Orange: {value}")
        self.update()
        
	# Update green LED brightness
    def update_green(self):
        value = self.sldr_green.value()
        self.led_green.ChangeDutyCycle(value)
        self.label3.setText(f"LED Green: {value}")
        self.update()

	# Update text label sizes
    def update(self):
        self.label1.adjustSize()
        self.label2.adjustSize()
        self.label3.adjustSize()

# Create window MyWindow object
def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

# Run the window!
window()
                                



