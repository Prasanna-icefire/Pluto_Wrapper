# Pluto_Wrapper
This is a simple python Wrapper so that you can write a python script to make the drone move around.

Go ahead and pull up the terminal and type:

    git clone https://github.com/Prasanna-icefire/Pluto_Wrapper.git

Usage : 

The Pluto.py has the class with which we need to create drone Object.
Look into the example script at plutoControl.py and replicate the same.
The script arms the drone and keeps it spinning for 5 seconds before disarming.

In the script, my_pluto is the object created.
Assuming that the name of the object created is my_pluto, follow the lines below for using the wrapper.

To arm :
    my_pluto.arm()

To disarm :
    my_pluto.disarm()

To Takeoff :
    my_pluto.take_off()

To land : 
    my_pluto.land()

To move the drone forward() : 
    my_pluto.forward()

To move the drone backward() : 
    my_pluto.backward()

To move the drone left : 
    my_pluto.left()

To move the drone right : 
    my_pluto.right()

To rotate the drone right : 
    my_pluto.right_yaw()

To rotate the drone left : 
    my_pluto.left_yaw()