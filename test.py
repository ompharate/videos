import picamera

with picamera.PiCamera() as camera:
    camera.start_preview()
    camera.capture('/home/pi/Desktop/test_image.jpg')
