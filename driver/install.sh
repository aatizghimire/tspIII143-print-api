#!/bin/sh

if [ $( echo $(uname -m) | grep "x86_64") ]; then
  #64bit
  rpm -ivh Star_CUPS_Driver-3.14.0-1.x86_64.rpm
else
  #32bit
  rpm -ivh Star_CUPS_Driver-3.14.0-1.i386.rpm
fi
