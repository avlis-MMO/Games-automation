import cv2
import numpy as np
import mss
import time
import pytesseract
from win32gui import FindWindow, GetWindowRect
import pyautogui
import os

directory_of_python_script = os.path.dirname(os.path.abspath(__file__))
threshold = 0.85
scale = 1

weapons = {'Training Sword':cv2.imread(os.path.join(directory_of_python_script,'weapon\c1.png'), cv2.IMREAD_UNCHANGED), 'Beginner Sword':cv2.imread(os.path.join(directory_of_python_script,'weapon\c2.png'), cv2.IMREAD_UNCHANGED),
'Cleaver':cv2.imread(os.path.join(directory_of_python_script,'weapon\c3.png'), cv2.IMREAD_UNCHANGED), 'Axe':cv2.imread(os.path.join(directory_of_python_script,'weapon\c4.png'), cv2.IMREAD_UNCHANGED),
'Pickaxe':cv2.imread(os.path.join(directory_of_python_script,'weapon\c5.png'), cv2.IMREAD_UNCHANGED),'Shuriken':cv2.imread(os.path.join(directory_of_python_script,'weapon\c6.png'), cv2.IMREAD_UNCHANGED),
'Makeshift Bow':cv2.imread(os.path.join(directory_of_python_script,'weapon\c7.png'), cv2.IMREAD_UNCHANGED), 'Boomerang':cv2.imread(os.path.join(directory_of_python_script,'weapon\c8.png'), cv2.IMREAD_UNCHANGED),
'Glock':cv2.imread(os.path.join(directory_of_python_script,'weapon\c9.png'), cv2.IMREAD_UNCHANGED), 'Longsword':cv2.imread(os.path.join(directory_of_python_script,'weapon\\r1.png'), cv2.IMREAD_UNCHANGED),
'Wushu Spear':cv2.imread(os.path.join(directory_of_python_script,'weapon\\r2.png'), cv2.IMREAD_UNCHANGED), 'Crimson Bow':cv2.imread(os.path.join(directory_of_python_script,'weapon\\r3.png'), cv2.IMREAD_UNCHANGED),
'P90':cv2.imread(os.path.join(directory_of_python_script,'weapon\\r4.png'), cv2.IMREAD_UNCHANGED), 'Mk 2 Grenade':cv2.imread(os.path.join(directory_of_python_script,'weapon\\r5.png'), cv2.IMREAD_UNCHANGED),
'Kunai':cv2.imread(os.path.join(directory_of_python_script,'weapon\\r6.png'), cv2.IMREAD_UNCHANGED), 'Sharanga':cv2.imread(os.path.join(directory_of_python_script,'weapon\epic1.png'), cv2.IMREAD_UNCHANGED),
'Harlott':cv2.imread(os.path.join(directory_of_python_script,'weapon\epic2.png'), cv2.IMREAD_UNCHANGED), 'Rhongomiant':cv2.imread(os.path.join(directory_of_python_script,'weapon\epic3.png'), cv2.IMREAD_UNCHANGED),
'Ascalon':cv2.imread(os.path.join(directory_of_python_script,'weapon\epic4.png'), cv2.IMREAD_UNCHANGED), 'Durendal':cv2.imread(os.path.join(directory_of_python_script,'weapon\l1.png'), cv2.IMREAD_UNCHANGED), 'Excalibur':cv2.imread(os.path.join(directory_of_python_script,'weapon\l2.png'), cv2.IMREAD_UNCHANGED),
'Bazooka':cv2.imread(os.path.join(directory_of_python_script,'weapon\l3.png'), cv2.IMREAD_UNCHANGED), 'Caladbolg':cv2.imread(os.path.join(directory_of_python_script,'weapon\l4.png'), cv2.IMREAD_UNCHANGED), 'Aldan':cv2.imread(os.path.join(directory_of_python_script,'weapon\l5.png'), cv2.IMREAD_UNCHANGED),
'Minigun':cv2.imread(os.path.join(directory_of_python_script,'weapon\l6.png'), cv2.IMREAD_UNCHANGED), 'Mjolnir':cv2.imread(os.path.join(directory_of_python_script,'weapon\l7.png'), cv2.IMREAD_UNCHANGED), 'Galatine':cv2.imread(os.path.join(directory_of_python_script,'weapon\l8.png'), cv2.IMREAD_UNCHANGED),
'Dragunov':cv2.imread(os.path.join(directory_of_python_script,'weapon\l9.png'), cv2.IMREAD_UNCHANGED), 'AK-47':cv2.imread(os.path.join(directory_of_python_script,'weapon\epic5.png'), cv2.IMREAD_UNCHANGED)}

helmets = {'3D Glasses':cv2.imread(os.path.join(directory_of_python_script,'helmet\g1.png'), cv2.IMREAD_UNCHANGED),'Cheap Headphones':cv2.imread(os.path.join(directory_of_python_script,'helmet\g2.png'), cv2.IMREAD_UNCHANGED), 'Fez':cv2.imread(os.path.join(directory_of_python_script,'helmet\g3.png'), cv2.IMREAD_UNCHANGED),
'Graduation Cap':cv2.imread(os.path.join(directory_of_python_script,'helmet\g4.png'), cv2.IMREAD_UNCHANGED), 'Propeller Cap':cv2.imread(os.path.join(directory_of_python_script,'helmet\g5.png'), cv2.IMREAD_UNCHANGED), 'Reading Glasses':cv2.imread(os.path.join(directory_of_python_script,'helmet\g6.png'), cv2.IMREAD_UNCHANGED),
'Strawberry Cone':cv2.imread(os.path.join(directory_of_python_script,'helmet\g7.png'), cv2.IMREAD_UNCHANGED), 'Surgical Mask':cv2.imread(os.path.join(directory_of_python_script,'helmet\g8.png'), cv2.IMREAD_UNCHANGED), 'Suspicious Goggles':cv2.imread(os.path.join(directory_of_python_script,'helmet\g9.png'), cv2.IMREAD_UNCHANGED),
'Top Hat':cv2.imread(os.path.join(directory_of_python_script,'helmet\g10.png'), cv2.IMREAD_UNCHANGED), 'Brown Fedora':cv2.imread(os.path.join(directory_of_python_script,'helmet\\b1.png'), cv2.IMREAD_UNCHANGED), 'Cowboy Hat':cv2.imread(os.path.join(directory_of_python_script,'helmet\\b2.png'), cv2.IMREAD_UNCHANGED),
'Hard Hat':cv2.imread(os.path.join(directory_of_python_script,'helmet\\b3.png'), cv2.IMREAD_UNCHANGED), 'Panama Hat':cv2.imread(os.path.join(directory_of_python_script,'helmet\\b4.png'), cv2.IMREAD_UNCHANGED), 'Peaked Cap':cv2.imread(os.path.join(directory_of_python_script,'helmet\\b5.png'), cv2.IMREAD_UNCHANGED),
'Pointy Hat':cv2.imread(os.path.join(directory_of_python_script,'helmet\\b6.png'), cv2.IMREAD_UNCHANGED), 'Steel Helm':cv2.imread(os.path.join(directory_of_python_script,'helmet\\b7.png'), cv2.IMREAD_UNCHANGED), 'Straw Hat':cv2.imread(os.path.join(directory_of_python_script,'helmet\\b8.png'), cv2.IMREAD_UNCHANGED),
'Transparent Cap':cv2.imread(os.path.join(directory_of_python_script,'helmet\\b9.png'), cv2.IMREAD_UNCHANGED), 'Crimson Beak':cv2.imread(os.path.join(directory_of_python_script,'helmet\\b10.png'), cv2.IMREAD_UNCHANGED), '???':cv2.imread(os.path.join(directory_of_python_script,'helmet\p1.png'), cv2.IMREAD_UNCHANGED),
'Mushroom Cap':cv2.imread(os.path.join(directory_of_python_script,'helmet\p2.png'), cv2.IMREAD_UNCHANGED), 'Santa Hat':cv2.imread(os.path.join(directory_of_python_script,'helmet\p3.png'), cv2.IMREAD_UNCHANGED), 'Cozy Hat':cv2.imread(os.path.join(directory_of_python_script,'helmet\p4.png'), cv2.IMREAD_UNCHANGED),
'Midas Helm':cv2.imread(os.path.join(directory_of_python_script,'helmet\p5.png'), cv2.IMREAD_UNCHANGED), 'Bucket Helm':cv2.imread(os.path.join(directory_of_python_script,'helmet\p6.png'), cv2.IMREAD_UNCHANGED), 'Steampunk Goggles':cv2.imread(os.path.join(directory_of_python_script,'helmet\p7.png'), cv2.IMREAD_UNCHANGED),
'Voidmask':cv2.imread(os.path.join(directory_of_python_script,'helmet\y1.png'), cv2.IMREAD_UNCHANGED), 'Kingsguard Helm':cv2.imread(os.path.join(directory_of_python_script,'helmet\y2.png'), cv2.IMREAD_UNCHANGED), 'Oni Mask':cv2.imread(os.path.join(directory_of_python_script,'helmet\y3.png'), cv2.IMREAD_UNCHANGED)}

portal = cv2.imread(os.path.join(directory_of_python_script,'other\portal_2.png'), cv2.IMREAD_UNCHANGED)
portal_h, portal_w = portal.shape[:2]
vic = cv2.imread(os.path.join(directory_of_python_script,'other\\vic.png'), cv2.IMREAD_UNCHANGED)
vic_h, vic_w = vic.shape[:2]
end = cv2.imread(os.path.join(directory_of_python_script,'other\end.png'), cv2.IMREAD_UNCHANGED)
end_h, end_w = end.shape[:2]
buy_gold = cv2.imread(os.path.join(directory_of_python_script,'other\\buy_gold.png'), cv2.IMREAD_UNCHANGED)
bg_h, bg_w = buy_gold.shape[:2]
buy_cd = cv2.imread(os.path.join(directory_of_python_script,'other\\buy_cd.png'), cv2.IMREAD_UNCHANGED)
bcd_h, bcd_w = buy_cd.shape[:2]
click = cv2.imread(os.path.join(directory_of_python_script,'other\square.png'), cv2.IMREAD_UNCHANGED)
click_h, click_w = click.shape[:2]
skill = cv2.imread(os.path.join(directory_of_python_script,'other\skill.png'), cv2.IMREAD_UNCHANGED)
skill_h, skill_w = skill.shape[:2]
rewind = cv2.imread(os.path.join(directory_of_python_script,'other\\rewind.png'), cv2.IMREAD_UNCHANGED)
rewind_h, rewind_w = rewind.shape[:2]
button_r = cv2.imread(os.path.join(directory_of_python_script,'other\\button_r.png'), cv2.IMREAD_UNCHANGED)
button_r_h, button_r_w = rewind.shape[:2]
stat = cv2.imread(os.path.join(directory_of_python_script,'other\stat.png'), cv2.IMREAD_UNCHANGED)
stat_h, stat_w = stat.shape[:2]
battle = cv2.imread(os.path.join(directory_of_python_script,'other\\battle.png'), cv2.IMREAD_UNCHANGED)
battle_h, battle_w = battle.shape[:2]
camp = cv2.imread(os.path.join(directory_of_python_script,'other\camp.png'), cv2.IMREAD_UNCHANGED)
camp_h, camp_w = camp.shape[:2]
x2 = cv2.imread(os.path.join(directory_of_python_script,'other\\2x.png'), cv2.IMREAD_UNCHANGED)
x2_h, x2_w = x2.shape[:2]
ok = cv2.imread(os.path.join(directory_of_python_script,'other\ok.png'), cv2.IMREAD_UNCHANGED)
ok_h, ok_w = ok.shape[:2]
screen = cv2.imread(os.path.join(directory_of_python_script,'other\screen.png'), cv2.IMREAD_UNCHANGED)
screen_h, screen_w = screen.shape[:2]

def attack():

    time.sleep(3)
    # Attack until the return button is seen
    while 1:
        game = np.array(sct.grab(monitor1))
        game_h, game_w = game.shape[:2] 
        pyautogui.dragTo(window_rect[0] + int(game_w*3/4), window_rect[1] + int(game_h/5), 0.5, button='left')
        pyautogui.dragTo(window_rect[0] + int(game_w*3/4), window_rect[1] + int(game_h*4/5), 0.5, button='left')


        for i in np.linspace(0.5, 1.5, num=10):         
            end_r = cv2.resize(end, (int(i*end_w),int(i*end_h)), interpolation = cv2.INTER_AREA)
            end_result = cv2.matchTemplate(game, end_r, cv2.TM_CCOEFF_NORMED)
            end_result = np.where(end_result >= threshold)
            if len(end_result[1]) >= 1:
                pyautogui.click(x =window_rect[0] + end_result[1][0] + int(end_w/2), y = window_rect[1] + end_result[0][0] + int(end_h/2))
                break
        if len(end_result[1]) >= 1:
            break 
# Do one of the macro detection systems
def CheckCircle():
    
        while 1:

            time.sleep(1)
            loc_x, loc_y = 0, 0

            # Get only the rgb
            game = np.array(sct.grab(monitor1))
            game_bw = game[:,:,:3]
            game_r = game[:,:,:3]

            # Get just the white text
            maskw = cv2.inRange(game_bw, np.array([190, 190, 190]), np.array([255, 255, 255]))
            detected_output = cv2.bitwise_and(game_bw, game_bw, mask =  maskw) 
            
            # Check if its the circle pressing system
            text = pytesseract.image_to_string(detected_output)
            test = 'Tap'
            print(text)
            if test not in text:
                break
            
            # Get mask with the 3 colors of the circles
            mask1 = cv2.inRange(game_r, np.array([5, 50, 5]), np.array([20, 125, 30]))
            mask2 = cv2.inRange(game_r, np.array([0, 0, 140]), np.array([30, 30, 180]))
            mask3 = cv2.inRange(game_r, np.array([0, 100, 150]), np.array([25, 150, 210]))
        
            output1 = np.transpose(np.nonzero(mask1))
            output2 = np.transpose(np.nonzero(mask2))
            output3 = np.transpose(np.nonzero(mask3))

            # Find for each color the location of all the pixels of that color and find the average to get the center
            if len(output1)>0:
                for i in output1:
                    loc_y = loc_y + i[0]
                    loc_x = loc_x + i[1]
                loc_x = int(loc_x/len(output1))
                loc_y = int(loc_y/len(output1))
                pyautogui.click(x =window_rect[0] + loc_x, y = window_rect[1] + loc_y)
        
            if len(output2)>0:
                for i in output2:
                    loc_y = loc_y + i[0]
                    loc_x = loc_x + i[1]
                loc_x = int(loc_x/len(output2))
                loc_y = int(loc_y/len(output2))
                pyautogui.click(x =window_rect[0] + loc_x, y = window_rect[1] + loc_y)  

            if len(output3)>0:
                for i in output3:
                    loc_y = loc_y + i[0]
                    loc_x = loc_x + i[1]
                loc_x = int(loc_x/len(output3))
                loc_y = int(loc_y/len(output3))
                pyautogui.click(x =window_rect[0] + loc_x, y = window_rect[1] + loc_y)                         

# Do one of the macro detection systems
def CheckEquip():
    threshold = 0.75
    while 1:
        time.sleep(1)
        game = np.array(sct.grab(monitor1))
        game_h, game_w = game.shape[:2]  

        #Convert the image to gray scale
        game_crop = game[int(game_h/5):int(game_h/3),int(game_w/5):int(3*game_w/4)]
    
        # Read the text on the  screen
        text = pytesseract.image_to_string(game_crop)
        test = 'Select the'
        if test not in text:
            break
        
        # Select only the name of the equip
        if len(text)>1:
            text = text.split("Select the ",1)[1]
            text = text.strip('\n')
        
            # If is a helmet find the corresponding image on the dic and click on it
            if text in helmets:
                
                h, w = helmets[text].shape[:2]
                helmet_result = multiScale(game, helmets[text], w, h)
                pyautogui.click(x =window_rect[0] + helmet_result[1][0] + int(w*i/2), y = window_rect[1] + helmet_result[0][0]+int(h*i/2))

            # If is a weapon find the corresponding image on the dic and click on it
            elif text in weapons:
                
                h, w = weapons[text].shape[:2]
                weapon_result = multiScale(game, weapons[text], w, h)
                pyautogui.click(x =window_rect[0] + weapon_result[1][0] + int(w*i/2), y = window_rect[1] + weapon_result[0][0]+int(h*i/2)) 

            else:
                pyautogui.click(x =window_rect[0] + int(game_w/2), y = window_rect[1] + int(game_h/2))  

# Multiscale props because window isnt always the same size
def multiScale(game, img, img_w, img_h):

    for i in np.linspace(0.5, 2, num=50):         
        img_r = cv2.resize(img, (int(i*img_w),int(i*img_h)), interpolation = cv2.INTER_AREA)
        img_result = cv2.matchTemplate(game, img_r, cv2.TM_CCOEFF_NORMED)
        img_result = np.where(img_result >= threshold)
        if len(img_result[1]) >=1:
            global scale
            scale = i
            return img_result

if __name__ == '__main__':
    with mss.mss() as sct:

        while "Screen capturing":
            #Part of the screen to capture
            window_handle = FindWindow(None, "BlueStacks App Player")
            window_rect   = GetWindowRect(window_handle)
            monitor1 = {"top": window_rect[1], "left": window_rect[0], "width": (window_rect[2] - window_rect[0]), "height": (window_rect[3] - window_rect[1])}
        
            #attack()
            time.sleep(1)
            while 1:
                game = np.array(sct.grab(monitor1))
                game_h, game_w = game.shape[:2]
                for i in np.linspace(0.5, 2, num=10):         
                    screen_r = cv2.resize(screen, (int(i*screen_w),int(i*screen_h)), interpolation = cv2.INTER_AREA)
                    screen_result = cv2.matchTemplate(game, screen_r, cv2.TM_CCOEFF_NORMED)
                    screen_result = np.where(screen_result >= threshold)
                    if len(screen_result[1])>=1:
                        break
                if len(screen_result[1]) < 1:
                    break

            time.sleep(1)
            CheckCircle()
            time.sleep(1)
            CheckEquip()
            
            # Update screen and find the location to buy the CD stat
            game = np.array(sct.grab(monitor1))

            bcd_result = multiScale(game, buy_cd, bcd_w, bcd_h)
            game_c = game[bcd_result[0][0]:(bcd_result[0][0]+int(i*bcd_h)),bcd_result[1][0]:(window_rect[0])] 
            
            # Click to buy CD
            click_result = multiScale(game_c, click, click_w, click_h)
            pyautogui.click(x =window_rect[0] + bcd_result[1][0] + click_result[1][0] + int(scale*click_w), y = window_rect[1] + bcd_result[0][0] + click_result[0][0]+int(scale*click_h))       
            time.sleep(1)
            
            # Change to skills
            skill_result = multiScale(game, skill, skill_w, skill_h)
            pyautogui.click(x =window_rect[0] + skill_result[1][0] + int(skill_w/2), y = window_rect[1] + skill_result[0][0] + int(skill_h/2))       
            time.sleep(2)
            
            # Update screen and click to rewind
            game = np.array(sct.grab(monitor1))
            game_h, game_w = game.shape[:2]
            game_c = game[:,int(game_w/4):int(game_w/2)] ## Resize screen to find faster and avoid false detections 

            rewind_result = multiScale(game_c, rewind, rewind_w, rewind_h)
            pyautogui.click(x =window_rect[0] + rewind_result[1][0] + int(game_w/4) - int(scale*rewind_w), y = window_rect[1] +  rewind_result[0][0] + int(scale*rewind_h))       
            time.sleep(1.5)
            
            # Update screen and click to confirm rewind
            game = np.array(sct.grab(monitor1))
            game_h, game_w = game.shape[:2]  
            game_c = game[:,int(game_w/2):] ## Resize screen to find faster and avoid false detections

            rewind_result = multiScale(game_c, button_r, button_r_w, button_r_h)
            pyautogui.click(x =window_rect[0] + int(game_w/2) + rewind_result[1][0] + int(scale*button_r_w), y = window_rect[1] +  rewind_result[0][0] + int(scale*button_r_h))       
            time.sleep(1.5)
            
            # Update screen and change to stats
            game = np.array(sct.grab(monitor1))
            game_h, game_w = game.shape[:2] 
            game_c = game[:,0:int(game_w/5)] ## Resize screen to find faster and avoid false detections

            stat_result = multiScale(game_c, stat, stat_w, stat_h)
            pyautogui.click(x =window_rect[0] + stat_result[1][0] + int(stat_w/2), y = window_rect[1] + stat_result[0][0] + int(stat_h/2))       
            time.sleep(1.5)

            #Update screen and find Gold
            game = np.array(sct.grab(monitor1))
            game_h, game_w = game.shape[:2]
            game_c = game[int(game_h*4/5):-1,:] ## Resize screen to find faster and avoid false detections

            bg_result = multiScale(game_c, buy_gold, bg_w, bg_h)
            game_c2 = game[int(game_h*4/5)+bg_result[0][0]:(int(game_h*4/5)+bg_result[0][0]+int(scale*bg_h)),0:int(game_w/2)] 

            # Click to buy Gold
            if len(bg_result[1]) >= 1:
                click_result = multiScale(game_c2, click, click_w, click_h)
                pyautogui.click(x =window_rect[0] + click_result[1][0] + int(i*click_w), y = window_rect[1] + bg_result[0][0] + click_result[0][0] + int(scale*click_h) + int(game_h*4/5))       
            time.sleep(1)

            # Update screen and click battle
            game = np.array(sct.grab(monitor1))

            battle_result = multiScale(game, battle, battle_w, battle_h)
            pyautogui.click(x =window_rect[0] + battle_result[1][0] + int(battle_w/2), y = window_rect[1] + battle_result[0][0] + int(battle_h/2))       
            time.sleep(1)

            # Update screen and click Camp
            game = np.array(sct.grab(monitor1))

            camp_result = multiScale(game, camp, camp_w, camp_h)
            pyautogui.click(x =window_rect[0] + camp_result[1][0] + 4*int(camp_w/2), y = window_rect[1] + camp_result[0][0] + int(camp_h/2))       
            time.sleep(1)

            # Update screen and click 2x/OK
            game = np.array(sct.grab(monitor1))

            x2_result = multiScale(game, x2, x2_w, x2_h)
            pyautogui.click(x =window_rect[0] + x2_result[1][0] + int(x2_w/2), y = window_rect[1] + x2_result[0][0] + int(x2_h/2))       
            
        