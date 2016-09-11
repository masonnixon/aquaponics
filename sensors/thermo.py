import os
import glob
import time
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
 
def read_temp_raw(index):
    device_folder = glob.glob(base_dir + '28*')[index]
    sensors = device_folder[len(base_dir):]
    device_file = device_folder + '/w1_slave'
    f = open(device_file, 'r')
    lines = f.readlines()
#    for i in range(0,len(sensors)-1):
#        print sensors
#    f.close()
    return lines, sensors
 
def read_temp(index):
    retVals = read_temp_raw(index)
    lines = retVals[0]
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return retVals[1], temp_f
	
while True:
	numSensors = len(glob.glob(base_dir + '*'))
	for i in range(0,numSensors-1):
            tempVals = read_temp(i)
	#	print i
	    print "Sensor ",i," (Device: ",tempVals[0],"): ",tempVals[1],"F "	
	print "\n"
	time.sleep(1)
