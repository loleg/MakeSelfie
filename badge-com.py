import serial.tools.list_ports
import time
ports = list(serial.tools.list_ports.comports())

for port, desc, hwid in sorted(ports):
        print("{}: {} [{}]".format(port, desc, hwid))
        if "Pico W - CircuitPython CDC2" in desc:
            print(f"badge found! port: {port}")
            badge_port = port

#badge_port = '/dev/ttyACM1'
ser = serial.Serial(badge_port)

print("Press TP1 on badge:")
while True:
    print(ser.readline())
    time.sleep(0.2)