import RPi.GPIO as GPIO
import serial
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)     # Control Data Direction Pin
GPIO.setup(6,GPIO.OUT)      # Blue LED Pin

GPIO.setup(26,GPIO.IN)      # S2 Push Button Pin
GPIO.setup(19,GPIO.IN)      # S3 Push Button Pin
GPIO.setup(13,GPIO.IN)      # S4 Push Button Pin


Dynamixel=serial.Serial("/dev/ttyS0",baudrate=1000000,timeout=0.1, bytesize=8)   # UART in ttyS0 @ 1Mbps


while True:

    if GPIO.input(26):
        GPIO.output(6,GPIO.LOW)
    else:
        GPIO.output(6,GPIO.HIGH)
        GPIO.output(18,GPIO.HIGH)
        Dynamixel.write(bytearray.fromhex("FF FF 01 05 03 1E CD 00 0B"))  # Move Servo with ID = 1 to position 205
        GPIO.output(18,GPIO.LOW)
        startDynamixel = Dynamixel.read()
        startDynamixel = Dynamixel.read()
        idDynamixel = Dynamixel.read()
        lenghtDynamixel = Dynamixel.read()
        errorDynamixel = Dynamixel.read()
        chkDynamixel = Dynamixel.read()
        print("Servo ID = " , int.from_bytes(idDynamixel,byteorder='big') , " Errors = ", int.from_bytes(errorDynamixel,byteorder='big'))
        time.sleep(1)

    if GPIO.input(19):
        GPIO.output(6,GPIO.LOW)
    else:
        GPIO.output(6,GPIO.HIGH)
        GPIO.output(18,GPIO.HIGH)
        Dynamixel.write(bytearray.fromhex("FF FF 01 04 02 2A 01 CD"))   # Read Voltage of Servo with ID = 1 
        GPIO.output(18,GPIO.LOW)
        startDynamixel = Dynamixel.read()
        startDynamixel = Dynamixel.read()
        idDynamixel = Dynamixel.read()
        lenghtDynamixel = Dynamixel.read()
        errorDynamixel = Dynamixel.read()
        voltDynamixel = Dynamixel.read()
        chkDynamixel = Dynamixel.read()
        print("Servo Voltage = " , int.from_bytes(voltDynamixel,byteorder='big'))
        GPIO.output(18,GPIO.HIGH)
        Dynamixel.write(bytearray.fromhex("FF FF 01 04 02 2B 01 CC"))   # Read Temperature of Servo with ID = 1
        GPIO.output(18,GPIO.LOW)
        startDynamixel = Dynamixel.read()
        startDynamixel = Dynamixel.read()
        idDynamixel = Dynamixel.read()
        lenghtDynamixel = Dynamixel.read()
        errorDynamixel = Dynamixel.read()
        tempDynamixel = Dynamixel.read()
        chkDynamixel = Dynamixel.read()
        print("Servo Temperature = " , int.from_bytes(tempDynamixel,byteorder='big'))
        GPIO.output(18,GPIO.HIGH)
        Dynamixel.write(bytearray.fromhex("FF FF 01 04 02 24 02 D2"))   # Read Position of Servo with ID = 1
        GPIO.output(18,GPIO.LOW)
        startDynamixel = Dynamixel.read()
        startDynamixel = Dynamixel.read()
        idDynamixel = Dynamixel.read()
        lenghtDynamixel = Dynamixel.read()
        errorDynamixel = Dynamixel.read()
        posDynamixel = Dynamixel.read(2)
        chkDynamixel = Dynamixel.read()
        print("Servo Position = " , int.from_bytes(posDynamixel,byteorder='little'))
        time.sleep(1)

    if GPIO.input(13):
        GPIO.output(6,GPIO.LOW)
    else:
        GPIO.output(6,GPIO.HIGH)
        GPIO.output(18,GPIO.HIGH)
        Dynamixel.write(bytearray.fromhex("FF FF 01 05 03 1E 32 03 A3"))    # Move Servo with ID = 1 to position 816
        GPIO.output(18,GPIO.LOW)
        startDynamixel = Dynamixel.read()
        startDynamixel = Dynamixel.read()
        idDynamixel = Dynamixel.read()
        lenghtDynamixel = Dynamixel.read()
        errorDynamixel = Dynamixel.read()
        chkDynamixel = Dynamixel.read()
        print("Servo ID = " , int.from_bytes(idDynamixel,byteorder='big') , " Errors = ", int.from_bytes(errorDynamixel,byteorder='big'))
        time.sleep(1)


