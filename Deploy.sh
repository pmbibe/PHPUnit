#!/bin/bash
Result=`python Result.py`
if [ $Result -eq 0 ]
then
whoami
else
pwd
fi
