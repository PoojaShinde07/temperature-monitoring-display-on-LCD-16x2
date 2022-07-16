/*DHT11 Pins Raspberry pi
 Left Pin GPIO
 CENTRE 5V
 Right GND */

//CODE
import Adafruit_CharLCD as LCD
import time
import Adafruit_DHT
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
lcd1 = 12
lcd2 = 7
lcd3 = 8
lcd4 = 25
lcd5 = 24
43
lcd6 = 23
lcd = LCD.Adafruit_CharLCD(lcd1, lcd2, lcd3, lcd4, lcd5, lcd6, 0 , 16, 2)
while True:
hum, tem = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 3)
print("Humidity :",hum," Temperature : ",tem)
lcd.clear()
lcd.message("Temp : "+str(tem)+" C\n"+" Humidity : "+str(hum)+" %")
time.sleep(1)
