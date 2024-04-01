#sudo apt-get update
#sudo apt-get install python-picamera python3-picamera

From picamera import PiCamera
From time import sleep

camera = PiCamera()
camera.start_preview(fullscreen=false, windows = (50,150,1024,576)
sleep(10)
camera.capture(‘test.jpg’)
camera.stop_preview()
