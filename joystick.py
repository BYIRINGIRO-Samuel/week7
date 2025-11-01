import serial
import time
from vpython import sphere, vector, color, rate

port = 'COM5'
baud_rate = 9600

try:
    ser = serial.Serial(port, baud_rate)
    print(f"Connected to {port}")
except:
    print("Connection failed")
    exit()

sprite = sphere(pos=vector(0, 0, 0), radius=0.5, color=color.cyan, make_trail=True)
CENTER = 512
SPEED = 0.02

time.sleep(2)

while True:
    rate(60)
    if ser.in_waiting > 0:
        try:
            line = ser.readline().decode().strip()
            parts = line.split(',')
            if len(parts) == 3:
                x_val, y_val, btn = map(int, parts)
                x_movement = (x_val - CENTER) * SPEED
                y_movement = (CENTER - y_val) * SPEED
                sprite.pos.x += x_movement
                sprite.pos.y += y_movement
                if btn == 0:
                    sprite.pos = vector(0, 0, 0)
                    sprite.color = color.red
                else:
                    sprite.color = color.cyan
                print(f"Position → X:{sprite.pos.x:.2f}, Y:{sprite.pos.y:.2f}")
        except Exception as e:
            print("Data error:", e)
