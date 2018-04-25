#!/bin/bash

while :
do
	while :
	do
		
		read -n1 -r -p "Press space to continue..." key
		if [[ $key = "" ]]
		then
			break
		fi
	done

	echo starting

	gst-launch-1.0 nvcamerasrc num-buffers=1 ! 'video/x-raw(memory:NVMM), width=(int)1280, height=(int)720,format=(string)I420' ! nvvidconv ! videoflip method=5 ! videoflip method=1 ! jpegenc ! filesink location='image.jpg'

	echo captured

	python working.py --mode=visualization

	echo opening
	xdg-open image.jpg
done
