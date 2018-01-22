Starting from Rasbian Lite

username: aqua
password: aqua123
set static ip 192.168.1.85 or nmap -v -sn 192.168.1.0/24
hostname aquaponics-pi

sudo ln -s /home/aqua/repos/aquaponics.git/sensors/t /bin/t &&
sudo ln -s /home/aqua/repos/aquaponics.git/sensors/f /bin/f

sudo apt-get install python python-pip git sqlite
sudo pip install Flask pygal

=============

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

Enable SPI and One Wire in raspi-config
Setup for US keyboard and Internationalisation options

Increase One Wire limit to 20 (max allowed):
sudo nano /etc/modules

Add the line:
wire max_slave_count=20

Make more than one One Wire GPIO instead of default of GPIO4 (BCM pin):
sudo nano /boot/config.txt

Add the lines (to make multiple pins 21, 16, and 4):
dtoverlay=w1-gpio,gpiopin=21
dtoverlay=w1-gpio,gpiopin=16
dtoverlay=w1-gpio,gpiopin=4

Install my already working DS18S20 code

Install Adafruits DHT python code

Install Adafruits MCP3008 code (***not working yet on mine)

-----

Set up static IP
Make backup first
sudo cp /etc/dhcpcd.conf /etc/dhcpcd.conf.backup
sudo nano /etc/dhcpcd.conf

For wired:
interface eth0

static ip_address=192.168.0.10/24
static routers=192.168.0.1
static domain_name_servers=192.168.0.1

For wireless:
interface wlan0

static ip_address=192.168.2.35/24
static routers=192.168.2.1
static domain_name_servers=192.168.2.1

Now all you need to do is reboot, and everything should be set!
reboot

You can double check by typing
ifconfig

And checking the interfaces IP address

-----
Setup SSH with key only (https://www.raspberrypi.org/documentation/remote-access/ssh/passwordless.md)
Edit the SSH config

In the config:
sudo nano /etc/ssh/ssh_config

Uncomment:
RSAAuthentication yes

Now generate the key on the desired device or check if one already exists:

ls ~/.ssh

If you see files named id_rsa.pub or id_dsa.pub you have keys set up already, so you can skip the generating keys step (or delete these files with rm id* and make new keys).
Generate new SSH keys

To generate new SSH keys enter the following command (Choose a sensible hostname such as <YOURNANME>@<YOURDEVICE> where we have used eben@pi):

ssh-keygen -t rsa -C eben@pi

You can also use a more descriptive comment using quotes if you have spaces, e.g. ssh-keygen -t rsa -C "Raspberry Pi #123"

Upon entering this command, you'll be asked where to save the key. We suggest you save it in the default location (/home/pi/.ssh/id_rsa) by just hitting Enter.

You'll also be asked to enter a passphrase. This is extra security which will make the key unusable without your passphrase, so if someone else copied your key, they could not impersonate you to gain access. If you choose to use a passphrase, type it here and press Enter, then type it again when prompted. Leave the field empty for no passphrase.

Now you should see the files id_rsa and id_rsa.pub in your .ssh directory in your home folder:

ls ~/.ssh

authorized_keys  id_rsa  id_rsa.pub  known_hosts

The id_rsa file is your private key. Keep this on your computer.

The id_rsa.pub file is your public key. This is what you put on machines you want to connect to. When the machine you try to connect to matches up your public and private key, it will allow you to connect.

Take a look at your public key to see what it looks like:

cat ~/.ssh/id_rsa.pub

It should be in the form:

ssh-rsa <REALLY LONG STRING OF RANDOM CHARACTERS> eben@pi

Copy your public key to your Raspberry Pi

If your Pi does not have an .ssh directory you will need to set one up so that you can copy the key from your computer.

cd ~
install -d -m 700 ~/.ssh

To copy your public key to your Raspberry Pi, use the following command to append the public key to your authorized_keys file on the Pi, sending it over SSH:

cat ~/.ssh/id_rsa.pub | ssh <USERNAME>@<IP-ADDRESS> 'cat >> .ssh/authorized_keys'

Note that this time you will have to authenticate with your password.

Now try ssh <USER>@<IP-ADDRESS> and you should connect without a password prompt.

If you see a message "Agent admitted failure to sign using the key" then add your RSA or DSA identities to the authentication agent ssh-agent then execute the following command:

ssh-add

If this did not work, delete your keys with rm ~/.ssh/id* and follow the instructions again.

You can also send files over SSH using the scp command (secure copy). See the SCP guide for more information.


==================
Notes for end user on DHT11
The update rate is pretty slow (as much as 15 seconds for humidity and 30 sec for temp). The DHT22 is <5 sec for humidity and <10 sec for temp. Also the 22 has a Rel. Humidity range of 0-99% vs the 11 with 30-80%. 11 temp range is 0 - 50C and 22 is -40 to +80C.
