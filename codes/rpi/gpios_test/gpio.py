import RPi.GPIO as GPIO            # import RPi.GPIO module  
from time import sleep             # lets us have a delay  

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT, initial=GPIO.LOW)           # set GPIO24 as an output   

try:
    print("Iniciou")
    
    while True:
        status = int(input("1 pra ligado e 0 para desligado."))

        if status == 1:
            GPIO.output(40,1)
            print("On")
            
        elif status == 0:
            GPIO.output(40,0)
            print("Off")



except KeyboardInterrupt:
    GPIO.output(40,0)
    GPIO.cleanup()
    print("fim")