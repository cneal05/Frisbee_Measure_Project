# Frisbee_Measure_Project

Using this repository as a documentation place for the Frisbee Measure Project

 <br>
 
 ---
 
 <br>
 
 ## Table of Content
 
 * [Timeline](#timeline-weekly)
 
 * [Images](#progress-images)
 
 * [CAD Designs](#cad-designs)
 
 * [CODE](#code)
 
 * [DATA](#data)
 
<br>
<br>

---

<br>
<br>


### Iterations

<br>

* How our module might look with the Frisbee

![iteration #1](Images/Frisbee%20Iteration%20v.1.JPG)

<br>

* Psuedocoding of our module and how the code will look.


```mermaid
graph TD;
    A[(Press Button/ Flip Switch)] --> B(Begins Data Collection);
    B -->C{End of Data Collection};
    C --> |running in the background| D([When RPS = Many Certain Values for a decided amount of time -> flight = over => End Data Collection]);
    C -->E(If button = True for 5 seconds or more);
    E -->B;
    E --> F[False];
    F --> G([END]);
```

<br>
<br>

---

<br>
<br>


### Problems and Solutions

<details><summary>CLICK ME</summary>
<p>

<br>

* **Problem:**  The **MPU 6050** maxes out everytime even when the maximum value was changed. It practically dopesn't do anything as it doesn't collect any data when thrown.
   
   * **Solution:** The **MPU 6050** is replaced by the **GPS** and *only* the **GPS** will be used to collect **data**.
   
* **Problem:** The **GPS**  loses it's fix after sometime randomly and needs to get a fix again.

   * **Solution:** Although there isn't a **100% effective** solution, or any other **long term** solution that would prevent the problem, it is best to try and get a fix agian so that the GPS continues to work. 
 
* **Problem:** The hinge that is being used in **ONSHAPE** doesn't exist in the lab.
 
   * **Solution:** Will be making a hinge in **ONSHAPE** that will be **3D Printed**.
 
* **Problem:** The hinge being on the inside of the box isn't possible as the top and the box will conlide with each other so the top would have to be trimmed. That also isn't possible as the top piece will be basically floating and relying on the hinge and will have a big gap between the top and the wall of the enclosure which differs from what the goal is.
 
   * **Solution:** The hinge is moved on the outside so that the problem of overlapping is gone and the top can open without having any trimming needed.
   
* **Problem:** The **GPS** collects data but something in the code *ends* the loop and doesn't collect the **full data** when the frisbee is thrown.

   * **Solution:** 




 
</p>
</details>

<br>
<br>

---

<br>
<br>


### Timeline (weekly)

<details><summary>CLICK ME</summary>
<p>

* **01/09/2023** =  completed the wiring circuit for collecting data and making the data collector be powered without any cable connection.

* **01/17/2023** =  Finished CAD Designs of the **enclousure** and placed them for printing.

   * **01/19/2023** = the printed designs were finished but were incorrect. The **enclousure**turned out to be short for the whole circuit, so all the measurements were fixed and checked, and the new enclousure was placed for printing.

* **01/23/23** = the new enclosure is printed, and began sanding edges and gaps to prevent collisions.

* **01/30/23** = By the end of this week, the module (**circuit** and **enclosure**) will be completed.

   * **02/06/23**  = Will find center of mass, and mount module, and mostly likely the first test launch will take place.
   
   * **02/02/2023** = **TimeLine** shortened by ** 1 week** as the **Center of Mass**, **Mounting the Module** on the **Frisbee** *AND* taking a **test launch** completed. A small cut out is incorporated to get access to the power switch as it was inaccessible before.
   
   * **02/03/23** = A small cutout made in the enclosure is made to grant access to the power switch inside. 
   
* **02/06/23** = Testing to see if the module collects data and stores it when thrown most likely multiple times. 

   * **02/07/23** = Starting to write **new code** for **GPS**.
   
* **02/13/23** = Got a GPS fix and it started printing out **speed** and **altitude** which will be added to the **CSV** file.
   
   
   
<br>

### [BACK TO TimeLine](#timeline-weekly)

   
</p>
</details>

<br>
<br>

---

<br>
<br>


<br>

### Progress Images

<br>

<details><summary>CLICK ME</summary>
<p>

<br>

* Video of the **Gyroscope** working.

![Getting the Gyro to work](Images/Working%20Gyro(v.1).gif)

<br>

* The circuit, completed and working.

<img src="Images/Completed Circuit.jpg" alt="The circuit soldered, and assembeled with everything that will be used" width="650" height="750">

<br>
<br>

* The circuit and the enclosure completed and assemble.

<img src="Images/Completed Module.jpg" alt="The enclosure and the circuit put together." width="550" height="550">

<img src="Images/Completed Module with cover.jpg" alt="... together with the top cover." width="550" height="550">

<img src="Images/Completed Module with cover 2.jpg" alt="... together with the top cover2." width="550" height="550">

<br>
<br>

* The first test launch of the Module mounted, but **NOT** collecting **Data**.

<img src="Images/First Test Launch.jpg" alt="the module after being launched." width="500" height="520">

<img src="Images/Test Launch.gif" alt="video of the module being launched." width="650" height="600">

<br>
<br>

* A cutout was made separatly so that we can get access to the power switch **inside** the enclosure.

<img src="Images/Module Cutout on Top.jpg" alt="small cutout for acess to power switch" width="650" height="600">

<br>
<br>

* Ran two test runs that collected data and stored them in a CSV file.

<img src="Images/tomahawk.gif" alt="Thrwoing the frisbee with the tomahawk grip." width="650" height="600">

<img src="Images/backhand.gif" alt="Thrwoing the frisbee with the backhand grip." width="650" height="600">

<br>
<br>

* The Circuit is changed to house a **GPS** rather than the **MPU 6050** and is rewired,

<img src="Images/Circuit with GPS.jpg" alt="a new circuit that has the GPS and the MPU is removed." width="650" height="600">


<br>
<br>
<br>

### [BACK TO Progress Images](#progress-images)

</p>
</details>

<br>
<br>

---

<br>
<br>

### CAD Designs

<details><summary>CLICK ME</summary>
<p>

**Description:** All the designs and iterations completed to get a virtual visual of the final build are present in the OnShape Document.

<br>

Link to the [Onshape](https://cvilleschools.onshape.com/documents/8f23dd08753053fddae2e327/w/56d5ad7e3900473835bb5009/e/42cb564d32431f5d8d36b7a9) Document.

<br>

* The completed CAD version of the **enclosure** and **circuit**

<img src="Images/CAD Completed Circuit in Enclosure.PNG" alt="... together with the top cover2." width="750" height="650">

<br>

---

<br>


<details><summary>CIRCUIT</summary>
<p>

<br>

* The Circuit was completed in **ONSHAPE** to be used as a model for making an **enclosure** that the Circuit would be placed in.

<img src="Images/Circuit (front view).PNG" alt="The circuit model from the front." width="850" height="340">

<img src="Images/Circuit (side view).PNG" alt="The circuit model from the side." width="850" height="340">

<img src="Images/Circuit (isotopic view).PNG" alt="The circuit model from the front." width="750" height="600">

<img src="Images/MPU 5060.PNG" alt="The MPU board that is used in the Circuit" width="600" height="450">

<br>
<br>

* This version of the circuit holder changed the **original MPU6050** and replaced it with an **Adafruit GPS** and collects **alltitude and speed** much easier. The *MPU* wouldn't collect proper data so the need to replace it with something better was needed.

<img src="Images/Circuit (v.2).PNG" alt="The (2.0) iteration of the circuit." width="600" height="500">


<br>
<br>


* This iteration changes the location of **PowerBoost** and **GPS** as they are *closer* together. It also consists of *two* **switches**, one on the *PowerBoost* to turn the pico on or off, and a **second** next to the *PICO* which controls weather the circuit is in **read** mode or **write** mode.

<img src="Images/Circuit (v.2.5).PNG" alt="The (2.5) iteration of the circuit." width="600" height="500">


</p>
</details>

<br>
<br>

---

<br>
<br>

<details><summary>FRISBEE</summary>
<p>

<br>

* The frisbee was imported from a public document, and then altered to fit our frisbee's dimensions as best as possible. The **curves** of the frisbee couldn't be measured, and no **schematics** were found to get any dimensions. 
 
* this is the original **dimension** of the **frisbee** that changed to fit our **frisbee**.
 
<img src="Images/Frisbee (original [dimentions]).PNG" alt="the frisbee in its original dimensions" width="950" height="340">

<img src="Images/Frisbee (original).PNG" alt="The circuit model from the front." width="900" height="130">

<br>
<br>
 
* This is the **firsbee** with our **dimensions** and **diameter** to fit the enclosure. 

<img src="Images/Frisbee (changed [dimensions]).PNG" alt="The circuit model from the front." width="950" height="300">

<img src="Images/Frisbee (changed).PNG" alt="The circuit model from the side." width="950" height="150">


</p>
</details>


<br>
<br>

---

<br>
<br>

<details><summary>CIRCUIT HOLDER</summary>
<p>

<br>

* This **first** version of the holder was designed to be **weather proof** so for that reason it was completly covering the **Circuit** and had to be **unscrewed** from the frisbee in order to get access to the **circuit.**

<img src="Images/Circuit Holder (v.1).PNG" alt="First version of the holder" width="850" height="650">

<br>
<br>

* This new Iteration changes the previous build by **inverting** the holder so that the circuit would be **accessible** without the need to unscrew the whole **enclosure**. A cover slider is added to still have the module **protected**, and make it **accessibl** at the same time.

<img src="Images/Circuit Holder (v.2).PNG" alt="First version of the holder" width="860" height="650">

<br>
<br>

* This new version removes the previous **slide lid** and replaces it with a **hinge-connected** lid that is more mobile and opens without making contact with the frisbee's rim. the lid consists of a **bridge** locking mechanism for easier access. The Lids look inverted as they were accidentally placed there and wouldn't change direction. They work as intended for now.

<img src="Images/Circuit Holder (v.3.5).PNG" alt="First version of the holder" width="860" height="650">





</p>
</details>








<br>
<br>


### [BACK TO CAD Designs](#cad-designs)

</p>
</details>

<br>
<br>

---

<br>
<br>

### CODE

<details><summary>CLICK ME</summary>
<p>

<br>

**Description:** All *iterations* and **methods** to make the circuit, functions as should are present. The code runs the **methods**, and collects the data recieved and puts them in a **CSV file** which displays the Angular velcoity and time in an excel sheet.

<br>

* A first iteration of the code which confirms that the pico is communicating with the MPU6050.

```python
```circuit_python

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
buttonPin.pull = digitalio.Pull.DOWN 
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c)
counter = 0
list_x = []
list_y = []
list_z = []
timer = time.monotonic()
while buttonPin.value == True:
    pass
    print("PASSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
# button syntax still needed.
while True:
    x_angular_velocity = mpu.gyro[0]
    y_angular_velocity = mpu.gyro[1]
    z_angular_velocity = mpu.gyro[2]
    list_x = [list_x, x_angular_velocity]
    list_y = [list_y, y_angular_velocity]
    list_z = [list_z, z_angular_velocity]
    print(z_angular_velocity)


```

<br>
<br>

* This is the completed **code** for the Moduel, it **collects** the *data*, stores it in a CSV file, incorporates the button function where the module won't collect data as long as the button is held (**button value = false**).

```python
```circuit_python

# type: ignore
import adafruit_mpu6050
import busio
import board
import time
import digitalio
import math
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
    if current_time > 2 and math.fabs(mpu.gyro[0]+mpu.gyro[1]+mpu.gyro[2])<1:
        break
#break out of while true and save data
Values=open(f"/data/{time.monotonic()}.csv","w")
for i in range(len(list_z)):
    Values.write(f"{list_time[i]}{list_z[i]}\n")
Values.close


```

<br>
<br>

* This is the first iteration of the **GPS** code collecting **timestamp**, **altitude**, and **speed** when the Frisbee is thrown as the **MPU 6050** will not be used for technical issues.

```python
```circuit_python

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
    
    
```

<br>
<br>

* This is the main code for the **GPS** module and it saves the GPS value **Altitude** and **Speed** and saves it the the **CSV** file.


```python
```circuit_python

# type: ignore
import busio
import board
import time
import digitalio

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

gps.update()
base_altitude = gps.altitude_m

while buttonPin.value == False:
    pass
    #print("Pass")
timer = time.monotonic()
last_print = time.monotonic()
while True:
    print(base_altitude)
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
    if gps.altitude_m is not None:
        list_a.append(gps.altitude_m - base.altitude)
    if gps.speed_knots is not None:
        list_s.append(gps.speed_knots)
    # The two below lines print fix quality, and amount of satellites, not required but can be useful
    # print("Fix quality: {}".format(gps.fix_quality))
    # if gps.satellites is not None:
    #   print("# satellites: {}".format(gps.satellites))
    current_time = time.monotonic() - timer
    if current_time > 2 and gps.speed_knots <1:
        break
    #break out of while true and save data

    # Grab parts of the time from the
    # struct_time object that holds
    # the fix time.  Note you might
    # not get all data like year, day,
    # month!        
Values=open(f"/data/{gps.timestamp_utc.tm_mon}-{gps.timestamp_utc.tm_mday}-{gps.timestamp_utc.tm_year} {gps.timestamp_utc.tm_hour}:{gps.timestamp_utc.tm_min}:{gps.timestamp_utc.tm_sec}.csv","w")
#Values=open(f"/data/{gps.timestamp_utc.tm_mon}-{gps.timestamp_utc.tm_mday}-{gps.timestamp_utc.tm_year} {gps.timestamp_utc.tm_hour,}:{gps.timestamp_utc.tm_min,}:{gps.timestamp_utc.tm_sec}.csv","w")
for i in range(len(list_z)):
    Values.write(f"{list_time[i]}{list_z[i]}\n")
Values.close


```









<br>
<br>

### [BACK TO Code](#code)


</p>
</details>

<br>

<br>
<br>

---

<br>
<br>


### DATA

<br>

<details><summary>CLICK ME</summary>
<p>

<br>
<br>


* The use of **MPU 6050** and the data collected from it **maxes** out each try, so it doesn't collect the full data from the throw of the **frisbee**.

[link to MPU data collected](https://github.com/cneal05/Frisbee_Measure_Project/tree/main/data/MPU6050_data)

<br>

* The Switch to GPS **fixes** the previous problem but an **issue** in the code ends the loop early and doesn't collect the full data but instead does collects for approximately two seconds.

[link to GPS data collected](https://github.com/cneal05/Frisbee_Measure_Project/tree/main/data/GPS_data) ** 2-28-2023- [the time] ONLY!
         

</p>
</details>

<br>
<br>

---

<br>
<br>

# [BACK TO TOP](#frisbee_measure_project)
