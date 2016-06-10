Abstract
========

This is a script to record pairs of number and time[seconds].
This outputs these pair toward console and a file.  
Filename will be `./log_YYYYMMDD-HHMMSS.txt`.


Usage
=====

1. start program.  
`$ python timer_laprecorder.py`
1. type enter to record lap time.  
`[Enter]`  
`1 xx.xxxxx`  
then, this script outputs the number of lap and lap time.
    1. if you need to change page number, input number and type enter.  
    `5[Enter]`  
    `5 xx.xxxxx`
    1. next, you can increment page number only if input enter.
    `[Enter]`  
    `6 xx.xxxxxx`
1. when stop timer, input character \`q'.  
`q[Enter]`  
`7 xx.xxxx`  
`total xxxx.xxxx`  
then, this script outputs last lap time and total time.

Application
===========

for example, you can use this in order to measure time to explain each slide
when you train your presentation.
