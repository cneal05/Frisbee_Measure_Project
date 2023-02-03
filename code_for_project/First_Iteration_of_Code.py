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
mpu.gyro_range = 3
counter = 0
list_x = []
list_y = []
list_z = []
list_time = []
while buttonPin.value == False:
    pass
    #print("Pass")
timer = time.monotonic()
while True:
    x_angular_velocity = mpu.gyro[0]
    y_angular_velocity = mpu.gyro[1]
    z_angular_velocity = mpu.gyro[2]
    list_x = [list_x, x_angular_velocity]
    list_y = [list_y, y_angular_velocity]
    list_z.append(z_angular_velocity)
    list_time.append(time.monotonic())
    #print(z_angular_velocity)
    current_time = time.monotonic() - timer
    if current_time > 2 and mpu.gyro[0]+mpu.gyro[1]+mpu.gyro[2]<1:
        break
#break out of while true and save data
Values=open(f"/data/{time.monotonic()}.csv","w")
for i in range(len(list_z)):
    Values.write(f"{list_time[i]}{list_z[i]}\n")
Values.close