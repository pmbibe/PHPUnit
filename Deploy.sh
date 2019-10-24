#!/bin/bash
Result=`python Result.py`
if [ $Result -eq 0 ]
then
echo "Failed"
else
rsync -e ssh PHPUnit/*.php root@192.168.141.203:/usr/share/nginx/html
fi
