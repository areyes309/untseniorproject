#Libraries
import os
import sys
import RPi.GPIO as GPIO
import time
from datetime import datetime
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
if __name__ == '__main__':
    try:
        while True:
		print("Orange") #This would be where the LED code would go for "processing"
                os.system("cd ~/Desktop/ ")
                dt = datetime.now()
                date_time = dt.strftime("%m%d%Y_%H%M%S")
                newname = date_time + '.mp4'
                print(newname) #new name prints "Finished"
                os.system("mkdir ~/Desktop/bagpictures")
		os.chdir("bagpictures/")             
		os.system("rs-record -t 3")
                os.system("rs-convert -p test -i test.bag")
		time.sleep(5)
                os.system("rename 's/.+/our $i; sprintf(\"pic%03d.png\", 1+$i++)/e' *")
                os.system("ffmpeg -r 6 -f image2 -s 640x480 -i pic%03d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p test.mp4")
                mp4 = "mv ~/Desktop/bagpictures/test.mp4 ~/Desktop/bagpictures/%s"%(newname)
                os.system(mp4)
                sendAws = "aws s3 cp %s s3://blacktheory/%s"%(newname, newname)
                startSearch = "aws rekognition start-face-search     --video \"S3Object={Bucket=blacktheory,Name=%s}\"     --collection-id my-faces | tee -a output.txt"%(newname)
                os.system(sendAws)
                os.system(startSearch)
                os.system("sed -i 's/[{}]//g' output.txt")
                os.system("sed -i 's/\"JobId\": \"//g' output.txt")
                os.system("sed -i 's/.$//' output.txt ")
                with open('output.txt', 'r') as file:
                    data = file.read().replace('\n', '')
                    print(data)
		time.sleep(10)
                getResult = "aws rekognition get-face-search --job-id %s | tee -a match.txt"%(data)
                print(getResult)
		os.chdir("..")
                os.system(getResult)
		os.system("dos2unix match.txt")
		os.system("python lock_and_sensor.py")
		os.system("rm -r ~/Desktop/bagpictures/")
		os.system("rm match.txt")

                time.sleep(25)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
