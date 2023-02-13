# type: ignore
import busio
import board
import time
import digitalio
import math

import adafruit_gps

#assigns the scl to GP6 and assigns sda to GP7 on the pico board
TX_pin = board.GP0
RX_pin = board.GP1
buttonPin = digitalio.DigitalInOut(board.GP17)
buttonPin.direction = digitalio.Direction.INPUT
buttonPin.pull = digitalio.Pull.UP 
counter = 0
list_x = []
list_y = []
list_z = []
list_time = []

uart = busio.UART(tx=TX_pin, rx=RX_pin, baudrate=9600, timeout=10)
gps = adafruit_gps.GPS(uart, debug=False)

while buttonPin.value == False:
    pass
    #print("Pass")
timer = time.monotonic()
last_print = time.monotonic()
while True:
    # Make sure to call gps.update() every loop iteration and at least twice
    # as fast as data comes from the GPS unit (usually every second).
    # This returns a bool that's true if it parsed new data (you can ignore it
    # though if you don't care and instead look at the has_fix property).
    gps.update()
    # Every second print out current location details if there's a fix.
    current = time.monotonic()
    if current - last_print >= 1.0:
        last_print = current
        if not gps.has_fix:
            # Try again if we don't have a fix yet.
            print("Waiting for fix...")
            continue
        # We have a fix! (gps.has_fix is true)
        # Print out details about the fix like location, date, etc.
        print("=" * 40)  # Print a separator line.
        print(
            "Fix timestamp: {}/{}/{} {:02}:{:02}:{:02}".format(
                gps.timestamp_utc.tm_mon,  # Grab parts of the time from the
                gps.timestamp_utc.tm_mday,  # struct_time object that holds
                gps.timestamp_utc.tm_year,  # the fix time.  Note you might
                gps.timestamp_utc.tm_hour,  # not get all data like year, day,
                gps.timestamp_utc.tm_min,  # month!
                gps.timestamp_utc.tm_sec,
            )
        )
        #print("Fix quality: {}".format(gps.fix_quality))
        # Some attributes beyond latitude, longitude and timestamp are optional
        # and might not be present.  Check if they're None before trying to use!
        #if gps.satellites is not None:
            #print("# satellites: {}".format(gps.satellites))
        if gps.altitude_m is not None:
            print("Altitude: {} meters".format(gps.altitude_m))
        if gps.speed_knots is not None:
            print("Speed: {} knots".format(gps.speed_knots))

    ''' x_angular_velocity = mpu.gyro[0]
        y_angular_velocity = mpu.gyro[1]
        z_angular_velocity = mpu.gyro[2]
        list_x = [list_x, x_angular_velocity]
        list_y = [list_y, y_angular_velocity]
        list_z.append(z_angular_velocity)
        list_time.append(time.monotonic())
        #print(z_angular_velocity)
        current_time = time.monotonic() - timer
        if current_time > 2 and math.fabs(mpu.gyro[0]+mpu.gyro[1]+mpu.gyro[2])<1:
            break
        #break out of while true and save data
        '''
    Values=open(f"/data-{}-{}-{} {:02}:{:02}:{:02}".format(
                gps.timestamp_utc.tm_mon,  # Grab parts of the time from the
                gps.timestamp_utc.tm_mday,  # struct_time object that holds
                gps.timestamp_utc.tm_year,  # the fix time.  Note you might
                gps.timestamp_utc.tm_hour,  # not get all data like year, day,
                gps.timestamp_utc.tm_min,  # month!
                gps.timestamp_utc.tm_sec,.csv),"w")
    for i in range(len(list_z)):
        Values.write(f"{list_time[i]}{list_z[i]}\n")
    Values.close