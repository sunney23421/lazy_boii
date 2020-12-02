from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import time
import random

mouse = Controller()
#mouse.position=(630, 814)
#Set the mouse position over here
i=1;

def stronglyAgreee():
    # This function has logi that will have a higher change to select on stronglyAgree
  randomThrToFive = random.randint(1,11);
  #randomThrToFive = 9;
  if (randomThrToFive==1):
    mouse.position=(626, 822);time.sleep(0.25);mouse.click(Button.left,1)#;print (1)
  elif randomThrToFive==2:
    mouse.position=(699, 822);time.sleep(0.25);mouse.click(Button.left,1)#;print (2)
  elif randomThrToFive>=3 and randomThrToFive<=5:
    mouse.position=(771, 822);time.sleep(0.25);mouse.click(Button.left,1)#;print (3)
  elif randomThrToFive>=6 and randomThrToFive<=8:
    mouse.position=(843, 822);time.sleep(0.25);mouse.click(Button.left,1)#;print (4)
  else:
    mouse.position=(917,822);time.sleep(0.25);mouse.click(Button.left,1)#;print (5)
  #print (randomThrToFive)
  time.sleep(0.5);
  mouse.scroll(0,-2.5)
  randomThrToFive = random.randint(1,11);
  
def stronglyDisagree():
  randomThrToFive = random.randint(1,11);
  if (randomThrToFive==1):
    mouse.position=(917,822);time.sleep(0.25);mouse.click(Button.left,1)#;print (5)
  elif randomThrToFive==2:
    mouse.position=(843, 822);time.sleep(0.25);mouse.click(Button.left,1)#;print (4)
  elif randomThrToFive>=3 and randomThrToFive<=5:
    mouse.position=(771, 822);time.sleep(0.25);mouse.click(Button.left,1)#;print (3)
  elif randomThrToFive>=6 and randomThrToFive<=8:
    mouse.position=(699, 822);time.sleep(0.25);mouse.click(Button.left,1)#;print (2)
  else:
    mouse.position=(626, 822);time.sleep(0.25);mouse.click(Button.left,1)#;print (1)
  #print (randomThrToFive)
  time.sleep(0.5);
  mouse.scroll(0,-2.5)
  randomThrToFive = random.randint(1,11);

def stronglyAlwasys():
  randomThrToFive = random.randint(1,11);
  #randomThrToFive = 9;
  if (randomThrToFive==1):
    mouse.position=(565, 747);time.sleep(0.25);mouse.click(Button.left,1)#;print (1)
  elif randomThrToFive==2:
    mouse.position=(658, 747);time.sleep(0.25);mouse.click(Button.left,1)#;print (2)
  elif randomThrToFive>=3 and randomThrToFive<=5:
    mouse.position=(752, 747);time.sleep(0.25);mouse.click(Button.left,1)#;print (3)
  elif randomThrToFive>=6 and randomThrToFive<=8:
    mouse.position=(848, 747);time.sleep(0.25);mouse.click(Button.left,1)#;print (4)
  else:
    mouse.position=(944,747);time.sleep(0.25);mouse.click(Button.left,1)#;print (5)
  #print (randomThrToFive)
  time.sleep(0.5);
  mouse.scroll(0,-2.5)
  randomThrToFive = random.randint(1,11);
  
def stronglyNever():
  randomThrToFive = random.randint(1,11);
  if (randomThrToFive==1):
    mouse.position=(944,747);time.sleep(0.25);mouse.click(Button.left,1)#;print (5)
  elif randomThrToFive==2:
    mouse.position=(848, 747);time.sleep(0.25);mouse.click(Button.left,1)#;print (4)
  elif randomThrToFive>=3 and randomThrToFive<=5:
    mouse.position=(752, 747);time.sleep(0.25);mouse.click(Button.left,1)#;print (3)
  elif randomThrToFive>=6 and randomThrToFive<=8:
    mouse.position=(658, 747);time.sleep(0.25);mouse.click(Button.left,1)#;print (2)
  else:
    mouse.position=(565, 747);time.sleep(0.25);mouse.click(Button.left,1)#;print (1)
  time.sleep(0.5);
  mouse.scroll(0,-2.5)
  randomThrToFive = random.randint(1,11);

#After fine-turn, you can call funtion inorder to you google from

stronglyAgreee()
stronglyAgreee()
stronglyDisagree()
stronglyDisagree()
stronglyAgreee()
stronglyAgreee()
stronglyAgreee()
stronglyAgreee()
stronglyAgreee()
stronglyAgreee();mouse.scroll(0,-2.58)#1######10
#mouse.scroll is to make mouse scroll though the page

while i<16:
    stronglyNever()
    i=i+1

mouse.scroll(0,-2)
i=1;
while i<20:
    stronglyNever()
    i=i+1

mouse.scroll(0,-2.5)
i=1;
while i<15:
    stronglyAgreee()
    i=i+1
mouse.scroll(0,-2.5)
mouse.scroll(0,-2.5)
i=1;
while i<29:
    stronglyAgreee()
    i=i+1
  
