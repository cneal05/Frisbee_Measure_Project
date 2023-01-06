# type: ignore
import adafruit_mpu6050
import busio
import board
import time
import digitalio
#assigns the scl to GP6 and assigns sda to GP7 on the pico board
sda_pin = board.GP6
scl_pin = board.GP7
buttonPin = digitalio.DigitalInOut(board.GP17)
buttonPin.direction = digitalio.Direction.INPUT
buttonPin.pull = digitalio.Pull.UP 
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c)
counter = 0
list_x = []
list_y = []
list_z = []
while buttonPin.value == False:
    pass
    print("PASSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
# button syntax still needed.
timer = time.monotonic()
while True:
    x_angular_velocity = mpu.gyro[0]
    y_angular_velocity = mpu.gyro[1]
    z_angular_velocity = mpu.gyro[2]
    list_x = [list_x, x_angular_velocity]
    list_y = [list_y, y_angular_velocity]
    list_z = [list_z, z_angular_velocity]
    print(z_angular_velocity)
    current_time = time.monotonic() - timer
    if current_time > 2 and mpu.gyro[0]+mpu.gyro[1]+mpu.gyro[2]<1:
        break
#break out of while true and save data