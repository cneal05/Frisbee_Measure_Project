# type: ignore
import busio
import board
import time
import digitalio
import random
import adafruit_gps

#assigns the scl to GP6 and assigns sda to GP7 on the pico board
TX_pin = board.GP0
RX_pin = board.GP1
buttonPin = digitalio.DigitalInOut(board.GP17)
buttonPin.direction = digitalio.Direction.INPUT
buttonPin.pull = digitalio.Pull.UP 
counter = 0
list_a = []
list_s = []
list_time = []
 
uart = busio.UART(tx=TX_pin, rx=RX_pin, baudrate=9600, timeout=10)
gps = adafruit_gps.GPS(uart, debug=False)

prev_alt = 0.0
prev_speed = 0.0
base_altitude = 0.0

while buttonPin.value == False:
    pass
    #print("Pass")
timer = time.monotonic()
last_print = time.monotonic()
Values=open(f"/data/{random.randint(1, 1000)}.csv","w")

while True:
    print(base_altitude)
    update = gps.update()
    # Make sure to call gps.update() every loop iteration and at least twice
    # as fast as data comes from the GPS unit (usually every second).
    # This returns a bool that's true if it parsed new data (you can ignore it
    # though if you don't care and instead look at the has_fix property).
    gps.update()
    # Every second print out current location details if there's a fix.
    current = time.monotonic()
    last_print = current
    if not gps.has_fix:
        # Try again if we don't have a fix yet.
        print("Waiting for fix...")
        continue
    if base_altitude == 0:
        base_altitude = gps.altitude_m
    if gps.altitude_m is not None and gps.speed_knots is not None:   
    
        altitude = round(float(gps.altitude_m), 3)
        speed = round(float(gps.speed_knots), 3)
        print(speed)
        if update and not ((prev_alt == altitude) and (prev_speed == speed)):
            list_a.append(altitude - base_altitude)
            list_s.append(speed)
            Values.write(f"{time.monotonic()},{altitude - base_altitude},{speed}\n")
            Values.flush()
            print("data is being collected")
        # The two below lines print fix quality, and amount of satellites, not required but can be useful
        # print("0Fix quality: {}".format(gps.fix_quality))
        # if gps.satellites is not None:
        #   print("# satellites: {}".format(gps.satellites))
            prev_alt = altitude
            prev_speed = speed
    current_time = time.monotonic() - timer