
import time  # 导入此模块，获取当前时间
from gpiozero import LED
from gpiozero import Button
#import tkinter # 导入控件

ledG = LED(27)
ledR = LED(22)
button = Button(3)

# 设置定时时间
hour = 0
minute = 1
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
        if button.is_pressed:
            ledR.on()
            time.sleep(1)
            ledR.off()
            hour = 36
            minute = 0
            sec = 0
        sec = sec - 1
        time.sleep(1)
        print("hour:", hour,"minute:", minute,"sec:", sec)
    if loop == 2:
        ledR.on()
        ledG.off()
        time.sleep(1)
        print("wash hair")
        if button.is_pressed:
            hour = 36
            minute = 0
            sec = 0
            loop = 1
            
