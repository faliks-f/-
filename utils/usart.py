import time
import serial

ser = None
com = "COM5"
ser = None


def openSerial():
    global ser
    ser = serial.Serial(com, 115200)
    print(ser.isOpen())


def serial_encoder(command):
    if command == "Right":
        buffer = [0x75, 0x03, 0xA9, 0xB9, 0x8A]
    elif command == "Left":
        buffer = [0x75, 0x03, 0xA9, 0xBA, 0x8A]
    elif command == "Down":
        buffer = [0x75, 0x03, 0xAA, 0xBA, 0x8A]
    elif command == "Up":
        buffer = [0x75, 0x03, 0xAA, 0xB9, 0x8A]
    else:
        buffer = [0x75, 0x04, 0x01, 0x01, 0x01]
    ser.write(buffer)


def serial_decoder():
    color = None
    shape = None
    p = None
    buffer = ser.read(5)
    print(buffer)
    if buffer[0] == 0x75 and buffer[1] == 0x02 and buffer[4] == 0x8A:
        if buffer[2] == 0xA3 and buffer[3] == 0xB3:
            p = "P1"
        elif buffer[2] == 0xA4 and buffer[3] == 0xA4:
            p = "P3"
        elif buffer[2] == 0xA5 and buffer[3] == 0xB5:
            p = "P5"
        elif buffer[2] == 0xA6 or buffer[2] == 0xA7 or buffer[2] == 0xA8:
            p = "P4"
            if buffer[2] == 0xA6:
                shape = "Circle"
            elif buffer[2] == 0xA7:
                shape = "Square"
            elif buffer[2] == 0xA8:
                shape = "Triangle"
            if buffer[3] == 0xB6:
                color = "Red"
            if buffer[3] == 0xB7:
                color = "Green"
            if buffer[3] == 0xB8:
                color = "Blue"
    return [p, shape, color]


def justStart():
    ser.write([0x75, 0x02, 0xA3, 0xB3, 0x8A])
    print("start")


if __name__ == '__main__':
    openSerial()
    # serial_encoder("Right")
    while True:
        serial_decoder()
        time.sleep(2)
