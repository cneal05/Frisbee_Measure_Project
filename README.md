# Frisbee_Measure_Project

Using this repository as a documentation place for the Frisbee Measure Project

 <br>
 
 ---
 
 <br>
 
 ## Table of Content
 
 * [Timeline](#timeline-weekly)
 
 * [Images](#progress-images)
 
 * [CAD Designs](#cad-designs)
 
 
<br>

---

<br>

### Timeline (weekly)

* **01/09/2023** =  completed the wiring circuit for collecting data and making the data collector be powered without any cable connection.

* **01/17/2023** =  Finished CAD Designs of the **enclousure** and placed them for printing.

   * **01/19/2023** = the printed designs were finished but were incorrect. The **enclousure**turned out to be short for the whole circuit, so all the measurements were fixed and checked, and the new enclousure was placed for printing.

* **01/23/23** = the new enclosure is printed, and began sanding edges and gaps to prevent collisions.

* **01/30/23** = By the end of this week, the module (**circuit** and **enclosure**) will be completed.

   * **02/06/23**  = Will find center of mass, and mount module, and mostly likely the first test launch will take place.
   
   * **02/02/2023** = **TimeLine** shortened by ** 1 week** as the **Center of Mass**, **Mounting the Module** on the **Frisbee** *AND* taking a **test launch** completed. A small cut out is incorporated to get access to the power switch as it was inaccessible before.
   
   * **02/03/23** = a small cutout made in the enclosure is made to grant access to the power switch inside. 
   

<br>
<br>

---

<br>
<br>

### Progress Images

<br>

* How our module might look with the Frisbee

![iteration #1](Images/Frisbee%20Iteration%20v.1.JPG)

<br>

* Psuedocoding of our module and how the code will look.

<img src="Images/SampleCode.jpg" alt="Sample code of how the project will work" width="750" height="750">

<br>

* Video of the **Gyroscope** working.

![Getting the Gyro to work](Images/Working%20Gyro(v.1).gif)

<br>

* The circuit, completed and working.

<img src="Images/Completed Circuit.jpg" alt="The circuit soldered, and assembeled with everything that will be used" width="650" height="750">

<br>

* The circuit and the enclosure completed and assemble.

<img src="Images/Completed Module.jpg" alt="The enclosure and the circuit put together." width="550" height="550">

<img src="Images/Completed Module with cover.jpg" alt="... together with the top cover." width="550" height="550">

<img src="Images/Completed Module with cover 2.jpg" alt="... together with the top cover2." width="550" height="550">

<br>

* The first test launch of the Module mounted, but **NOT** collecting **Data**.

<img src="Images/First Test Launch.jpg" alt="the module after being launched." width="500" height="520">

<img src="Images/Test Launch.gif" alt="video of the module being launched." width="650" height="600">

<br>

* a cutout was made separatly so that we can get access to the power switch **inside** the enclosure.

<img src="Images/Module Cutout on Top.jpg" alt="small cutout for acess to power switch" width="650" height="600">

<br>






<br>
<br>

---

<br>
<br>

### CAD Designs

**Description:** All the designs and iterations completed to get a virtual visual of the final build are present in the OnShape Document.

<br>

Link to the [Onshape](https://cvilleschools.onshape.com/documents/8f23dd08753053fddae2e327/w/56d5ad7e3900473835bb5009/e/42cb564d32431f5d8d36b7a9) Document.

<br>

* The completed CAD version of the **enclosure** and **circuit**

<img src="Images/CAD Completed Circuit in Enclosure.PNG" alt="... together with the top cover2." width="750" height="650">


<br>
<br>

---

<br>
<br>

### CODE

**Description:** All *iterations* and **methods** to make the circuit, functions as should are present. The code runs the **methods**, and collects the data recieved and puts them in a **VCS file** which displays the Angular velcoity and time in an excel sheet.

<br>

* A first iteration of the code which confirms that the pico is communicating with the MPU5060.

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

# [BACK TO TOP](#frisbee_measure_project)
