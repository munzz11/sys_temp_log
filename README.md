# sys_temp_log
A simple utility to log local system temps and record them in a local or remote influxdb

## Requirments
- linux system
- python3
- python `influxdb_client` 
- influxdb instance to point data to

## Setup
1.  Edit the script with your influxdb ip, bucket, org, and api token
2.  `sudo chmod +x sys_temp_logger.py`
3.  `sudo chmod +x setup.sh`
4.  `sudo ./setup.py`

## Note 
This script relies on `/sys/class/thermal/thermal_zone/` which is pressent on most linux systems. The labeling maybe different for your system though.
You can use `sensors` to see the different zones you have avaliable and change the labels in the script accordingly.
This script is specific to older intel NUC devices running Ubuntu 20.04
