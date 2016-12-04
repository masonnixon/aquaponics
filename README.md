Set up One Wire devices
sudo modprobe w1-gpio
sudo modprobe w1-therm
ls /sys/bus/w1/devices


Run 
ln -s /path/to/binary /bin/cheese
to create global executable (symbolic link to an executable).

I did this for t:
sudo ln -s /home/pi/repo/aquaponics.git/sensors/t /bin/t
