import RPi.GPIO as GPIO #GPIO pinlerinin kutuphanesini import ettik
import time
GPIO.setmode(GPIO.BOARD) #Board uzerindeki numaralandirmalari gecerli yaptik
GPIO.setup(38,GPIO.OUT) #Pinlerin durmunu cikis yaptik
GPIO.setup(40,GPIO.OUT)
try: #Bu alt satirlarda hatayi yakalamamizi saglayan komut
    while True:
        GPIO.output(38,True) #12 nolu pini +5v cikis verdik
        time.sleep(1) #Bekleme suresi belirledik
        GPIO.output(38,False) #12 nolu pini 0v'a dusurduk.
        GPIO.output(40,True)
        time.sleep(1)
        GPIO.output(40,False)
except KeyboardInterrupt: #Hata yakaladigimizda calisacak komut
#Herhangi bir hata da aldigimizda veya ctrl+c ile cikis yaptigimizda pinlerin durumu 0v yaptik.
        GPIO.output(38,False)
        GPIO.output(40,False)
        print('Cikis Yapildi')
finally:
        GPIO.cleanup() #GPIO durumlarinin temizlenmesini sagladik
