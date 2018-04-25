\
#!/bin/bash

while :
do
	while :
	do
		read -n 1 -p "Press space to continue..." key
		if [[ $key = "" ]]
		then
			break
		fi
	done

	echo Starting
	while :
	do
		#720x480
		#
		#
		gst-launch-1.0 nvcamerasrc num-buffers=1 ! 'video/x-raw(memory:NVMM), width=(int)720, height=(int)480,format=(string)I420' ! nvvidconv ! videoflip method=3 ! jpegenc ! filesink location='image.jpg'

		echo captured
		echo "press any key to continue"
		python camera.py
		read -n 1 -p "Press r to retake, space to continue, or q to quit" key

		if [[ $key = "q" ]]
		then
			exit
		fi

		if [[ $key = "" ]]
		then
			break
		else [[ $key = "r" ]]
		fi
	done
	python working.py --mode=visualization --max_iters 20000

	#echo opening
	#xdg-open output.jpg
done
