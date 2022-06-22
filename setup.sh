#!/bin/bash

cp sys_temp_logger.py /usr/local/bin/sys_temp_logger.py 
grep '* * * * * root /usr/bin/python3 /usr/local/bin/sys_temp_logger.py' /etc/crontab || echo '* * * * * root /usr/bin/python3 /usr/local/bin/sys_temp_logger.py' >> /etc/crontab
