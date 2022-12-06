# type: ignore
import adafruit_mpu6050
import busio
import board
import time
#assigns the scl to GP6 and assigns sda to GP7 on the pico board
sda_pin = board.GP6
scl_pin = board.GP7
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c)
list_x = []
list_y = []
list_z = []

while True:
    x_angular_velocity = mpu.gyro[0]
    y_angular_velocity = mpu.gyro[1]
    z_angular_velocity = mpu.gyro[2]
    list_x = [list_x, x_angular_velocity]
    list_y = list_y + y_angular_velocity 
    list_z = list_z + z_angular_velocity 
    print(z_angular_velocity)