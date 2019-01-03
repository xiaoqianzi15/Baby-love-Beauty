
import time  # time function
from gpiozero import LED  //IO function
from gpiozero import Button
#import tkinter # 

ledG = LED(27)
ledR = LED(22)
button = Button(3)

# set time
hour = 24
minute = 0
sec = 0
ledG.on()
ledR.on()
time.sleep(1)
ledG.off()
ledR.off()



flag = 1
loop = 1
while flag:
    if loop ==1:
        ledG.on()
        ledR.off()
        if sec<1 and minute>0:
            minute = minute -1
            sec = 60
        if minute<1 and hour>0:
            hour = hour -1
            minute = 60
        if hour == 0 and minute ==0 and sec ==0:
            print("time out")
            loop = 2
        sec = sec - 1
        time.sleep(1)
        print("hour:", hour,"minute:", minute,"sec:", sec)
    if loop == 2:
        ledR.on()
        ledG.off()
        time.sleep(1)
        if button.is_pressed:
            hour = 24
            minute = 0
            sec = 0
            loop = 1
