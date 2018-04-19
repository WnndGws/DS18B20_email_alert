#!/usr/bin/python3
##
import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_id = '28*'  # DSB1820 device ID e.g. 28-000003cee4ca
device_folder = glob.glob(base_dir + device_id)[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    '''Reads and returns raw output from device file.
    '''
    with open(device_file, 'r') as f:
        lines = f.readlines()
    return lines

def parse_temp(raw_output):
    '''Parses temperature from raw output text.
    '''
    equals_pos = raw_output[1].find('t=') # Since raw output is a list, 1st item signals success, 2nd item contains data
    if equals_pos != -1:
        temp_string = raw_output[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

def read_temp():
    '''Loops until a successful response is obtained, then parses the raw output and returns the temperature.

    The raw output will either have YES or NO at the end of the first line.
    If it is YES, then the temperature will be at the end of the second line, in degC*1000.

    Successful response:
      4b 01 4b 46 7f ff 05 10 e1 : crc=e1 YES
      4b 01 4b 46 7f ff 05 10 e1 t=31225

    Failed response:
      ... NO  ???
    '''
    raw_output = read_temp_raw()
    while raw_output[0].strip()[-3:] != 'YES':
        # DSB1820 is set to 12-bit resolution by default, which has a max
        # ADC conversion time of 750ms. Need to wait for it to finish.
        time.sleep(0.8)
        raw_output = read_temp_raw()

    temp_c = parse_temp(raw_output[1])
    return temp_c

if __name__ == '__main__':
    while True:
        print(read_temp())
        time.sleep(1)
