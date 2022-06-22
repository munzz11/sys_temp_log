#!/usr/bin/python3

########### Run setup.sh to setup cronjob to run every minute and copy/update this script to /usr/local/bin/ where it can be accessed by cron ###########  

import os
import socket
import subprocess
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

bucket = 'sys_temp'
org = 'mltdma'
token = '4ncNIyyi-BXk4zsK0f93hO_Q1LUfYEC6sQWLXZ9qRnLyti65X6ZPpgJLByOuPK-WmrOuA5Ksyx5__mzBSfoQFQ=='
url = 'http://localhost:8086'

client = InfluxDBClient(url = url, token = token, org = org)

write_api = client.write_api(write_options=SYNCHRONOUS)

#Zone 0

try:
	cmd = 'cat /sys/class/thermal/thermal_zone0/temp'
	output = subprocess.run(cmd, shell=True, capture_output=True)
	stderr = output.stderr.decode('utf-8')
	stdout = float(output.stdout.decode('utf-8'))
	temp = round(stdout/1000, 1)

	p = Point('Tempatures').tag('Type', 'acpitz').field('Degrees C', temp)
	write_api.write(bucket=bucket, record=p)
	
except:
  print("Invalid Output")
	
#Zone 1 

try:
  cmd = 'cat /sys/class/thermal/thermal_zone1/temp'
  output = subprocess.run(cmd, shell=True, capture_output=True)
  stderr = output.stderr.decode('utf-8')
  stdout = float(output.stdout.decode('utf-8'))
  temp = round(stdout/1000, 1)

  p = Point('Tempatures').tag('Type', 'acpitz').field('Degrees C', temp)
  write_api.write(bucket=bucket, record=p)

except:
  print("Invalid Output")
	
#Zone 2

try:
  cmd = 'cat /sys/class/thermal/thermal_zone2/temp'
  output = subprocess.run(cmd, shell=True, capture_output=True)
  stderr = output.stderr.decode('utf-8')
  stdout = float(output.stdout.decode('utf-8'))
  temp = round(stdout/1000, 1)

  p = Point('Tempatures').tag('Type', 'pch_skylake').field('Degrees C', temp)
  write_api.write(bucket=bucket, record=p)

except:
  print("Invalid Output")
	
#Zone 3

try:
  cmd = 'cat /sys/class/thermal/thermal_zone3/temp'
  output = subprocess.run(cmd, shell=True, capture_output=True)
  stderr = output.stderr.decode('utf-8')
  stdout = float(output.stdout.decode('utf-8'))
  temp = round(stdout/1000, 1)

  p = Point('Tempatures').tag('Type', 'iwlwifi_1').field('Degrees C', temp)
  write_api.write(bucket=bucket, record=p)

except:
  print("Invalid Output")
	
#Zone 4

try:
  cmd = 'cat /sys/class/thermal/thermal_zone4/temp'
  output = subprocess.run(cmd, shell=True, capture_output=True)
  stderr = output.stderr.decode('utf-8')
  stdout = float(output.stdout.decode('utf-8'))
  temp = round(stdout/1000, 1)

  p = Point('Tempatures').tag('Type', 'x86_pkg_temp').field('Degrees C', temp)
  write_api.write(bucket=bucket, record=p)

except:
  print("Invalid Output")

