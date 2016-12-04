Start program at start up
sudo crontab -e
@reboot /bin/t >> temperature.log 2&>1
@reboot /bin/f >> water_level.log 2&>1

To see it as it updates
tail -f --lines=5 /var/log/temperature.log
tail -f --lines=5 /var/log/water_level.log

Set up One Wire devices
sudo modprobe w1-gpio
sudo modprobe w1-therm
ls /sys/bus/w1/devices


Run 
ln -s /path/to/binary /bin/cheese
to create global executable (symbolic link to an executable).

I did this for t and f:
sudo ln -s /home/pi/repo/aquaponics.git/sensors/t /bin/t
sudo ln -s /home/pi/repo/aquaponics.git/sensors/f /bin/f

