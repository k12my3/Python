import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)


TRIG = 10
ECHO = 12
IR = 8
BUZZ = 16

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(IR, GPIO.IN)
GPIO.setup(BUZZ, GPIO.OUT)

def distance():
    # set Trigger to HIGH
    GPIO.output(TRIG, True)
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = round(TimeElapsed * 34300, 2)
 
    return distance

def ring():
    GPIO.output(BUZZ, True)
    time.sleep(1)
    GPIO.output(BUZZ, False)
    
def nodetect():
    print ("No body detected, please try again")
    GPIO.output(BUZZ, False)
    time.sleep(3)

def detect():
    print("Body detected, ringing doorbell...\n\n")
    ring()
    time.sleep(3)
 
if name == 'main':
    try:
        while True:
            
            dist = distance()
            if dist > 40:
                print("Distance > 40, cannot activate sensor")
                time.sleep(3)
            
            else:
                
                print("Please place your hand in front of the sensor")
                
                if GPIO.input(IR) == False:
                    nodetect()
                 
                else:
                    print("Trial succesful, please raise your hand in 3s")
                    time.sleep(2)
                    
                    if GPIO.input(IR)==True:
                        detect()
                    else:
                        nodetect()
                
                    
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()