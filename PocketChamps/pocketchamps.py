import cv2
import numpy as np
import mss
import time
from win32gui import FindWindow, GetWindowRect
from ppadb.client import Client as AdbClient
import os

# Get the images used to automate
directory_of_python_script = os.path.dirname(os.path.abspath(__file__))
file_name ='X.png'
X = cv2.imread(os.path.join(directory_of_python_script,file_name), cv2.IMREAD_UNCHANGED)
black_X = cv2.cvtColor(X, cv2.COLOR_BGR2GRAY)
file_name ='badge.png'
badge = cv2.imread(os.path.join(directory_of_python_script,file_name), cv2.IMREAD_UNCHANGED)

# Set threshold for matching
threshold = 0.8

# Location of the buttons to press
Play ='550 2000'
Race = '540 2230'
middle = '550 1000'
home = '530 2270'
Box = '150 1700'
Start = '550 1650'
timee = '550 700'
date = '570 1240'
day = '540 1830'
done = '790 2090'
res = '950 450'

# Connect phone to pc to send commands
def connect():
    client = AdbClient(host="127.0.0.1", port=5037) # Default is "127.0.0.1" and 5037

    devices = client.devices()

    if len(devices) == 0:
        print('No devices')
        quit()

    device = devices[0]

    return device, client

def check_X():
    game = np.array(sct.grab(monitor1))
    game_crop = game[700:-1,0:-1] 
    game_crop = cv2.cvtColor(game_crop, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(game_crop, black_X, cv2.TM_CCOEFF_NORMED)
    result = np.where(result >= threshold)
    if len(result[1]) > 1:
        Xx = '530 2160'
        device.shell(f'input tap {Xx}')
        time.sleep(1)
        return True
    else:
        return False

if __name__ == '__main__':
    device, client = connect()

    with mss.mss() as sct:

        while "Screen capturing":

            #Part of the screen to capture
            window_handle = FindWindow(None, "SM-G781B")
            window_rect   = GetWindowRect(window_handle)
            monitor1 = {"top": window_rect[1], "left": window_rect[0], "width": (window_rect[2] - window_rect[0]), "height": (window_rect[3] - window_rect[1])}
            game = np.array(sct.grab(monitor1))
            
            # Press the play button
            device.shell(f'input tap {Play}')
            time.sleep(1)

            # Select the left most recommend gadget
            x = 200
            Rec = str(x) +' 1900'
            device.shell(f'input tap {Rec}')
            time.sleep(1.5)
            while check_X():
                x = x + 250
                Rec = str(x) + ' 1900'
                device.shell(f'input tap {Rec}')
                time.sleep(1.5)

            # Start the race
            device.shell(f'input tap {Race}')

            # Press the screen until the home screen is reached
            while 1:
                device.shell(f'input tap {home}')
                game = np.array(sct.grab(monitor1))
                game_crop = game[750:850,0:-1] 
                result = cv2.matchTemplate(game_crop, badge, cv2.TM_CCOEFF_NORMED)
                result = np.where(result >= threshold)
                if len(result[1]) > 1 or check_X():
                    
                    break
                time.sleep(1.5)

            time.sleep(2)
            check_X()
            time.sleep(2)
            
            # Go to home screen in case not there
            device.shell(f'input tap {home}')
            time.sleep(1)

            # Click where the first box his
            device.shell(f'input tap {Box}')
            time.sleep(2)

            # Start the openning of the box
            device.shell(f'input tap {Start}')
            time.sleep(0.5)

            # Go to the app menu to select the options to change the time
            for i in range(2):
                device.shell('input keyevent 187')
                time.sleep(1)

            # Select tho change the time
            device.shell(f'input tap {timee}')
            time.sleep(1)

            # Select the date to change
            device.shell(f'input tap {date}')
            time.sleep(1)

            # Select one day forward
            device.shell(f'input tap {day}')
            time.sleep(1)

            # Save changes
            device.shell(f'input tap {done}')
            time.sleep(1)

            # Go back to game
            for i in range(2):
                device.shell('input keyevent 187')
                time.sleep(1)

            # Click box to open
            device.shell(f'input tap {Box}')
            time.sleep(3)

            # Get all the rewards
            while 1:
                device.shell(f'input tap {middle}')
                time.sleep(1)
                if check_X():
                    break

            # Wait for the level up and go back
            time.sleep(10)
            device.shell(f'input tap {middle}')
            time.sleep(3)
        
            # Go to options tab again
            for i in range(2):
                device.shell('input keyevent 187')
                time.sleep(1)

            # Change date back to correct day
            for i in range(2):
                device.shell(f'input tap {res}')
                time.sleep(0.5)

            # Go to game again
            device.shell('input keyevent 187')
            time.sleep(1)
            device.shell('input keyevent 187')
            time.sleep(1)

            