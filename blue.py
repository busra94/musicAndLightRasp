#coding: utf-8
import RPi.GPIO as GPIO #Çikis vermek için bu kütüphaneleri import etmeniz gerekiyor
import time #Ledleri yakinca birer saniye bekleyecegiz
# blinking function
def blink(pin): #Bir pin i parametre olarak alan metodumuz
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(pin,GPIO.LOW)
        time.sleep(0.1)
        return
# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
# set up GPIO output channel
GPIO.setup(12, GPIO.OUT) 
# blink GPIO17 50 times
for i in range(0,1800):
        blink(12)#12.pini parametre olarak verip ledi 11.pine bagliyoruz
GPIO.cleanup()
