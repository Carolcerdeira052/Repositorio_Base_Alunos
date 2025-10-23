import pyautogui as pg 
from time import sleep


#pg.mouseInfo()

pg.press("win")
pg.write("chorme")
pg.press("enter")
pg.moveto(555,850,duration=1)
pg.click()
pg.write("www.youtube.com")
pg.press("enter")
sleep(2)
pg.press(";")
pg.write("Dubai")
pg.press("enter")
pg.moveTo()