import RPi.GPIO as GPIO# GPIO pinlerinin kutuphanesini import ettik
import time
GPIO.setmode(GPIO.BOARD)#Board uzerindeki numaralandirmalari gecerli yaptik
GPIO.setup(12,GPIO.OUT)#pinlerin durmunu cikis yaptik
GPIO.setup(16,GPIO.OUT)
try: #  bu alt satirlarda hatayi yakalamamizi saglayan komut
 while True:
        GPIO.output(12,True)# 12 nolu pini +5v cikis verdik
        time.sleep(1)# bekleme suresi belirledik
        GPIO.output(12,False)#12 nolu pini 0v'a dusurduk.
        GPIO.output(16,True)
        time.sleep(1)
        GPIO.output(16,False)
except KeyboardInterrupt: #hata yakaladigimizda calisacak komut
#herhangi bir hata da aldigimizda veya ctrl+c ile cikis yaptigimizda pinlerin durumu 0v yaptik.
        GPIO.output(12,False)
        GPIO.output(16,False)
        print('Cikis Yapildi')
finally:
        GPIO.cleanup()#GPIO durumlarinin temizlenmesini sagladik
