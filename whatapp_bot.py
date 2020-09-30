import pyautogui
import time
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
#print("Current Time =", current_time)

user = input("Please enter the message to be sent")
time = int(input("Please tell the time interval between each message")
num = int(input("Please enter the number of times the message has to be sent")
 # short break
time.sleep(5)
 
#pyautogui.alert('This is the message to display.')
word = user+ "Sent at time:- " + current_time
for i in range(10):
    pyautogui.typewrite(word)
    
