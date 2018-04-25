#!/bin/bash
timeout 10 /home/ubuntu/tegrastats | tee percent.txt

cat percent.txt | grep -P "(?<=GR3D.)[[:digit:]]*" -o > gpuPercent.txt

cat percent.txt | grep -P "(?<=%@)[[:digit:]]*" -o > gpuHertzMe.txt

#cat gpuPercent.txt - get the percent of GPU with this loop
percentCount=0;
percentTotal=0;
for i in $( awk '{ print $1; }' gpuPercent.txt )
	do
		percentTotal=$(echo $percentTotal+$i | bc)
		((percentCount++))
	done

hertzCount=0;
hertzTotal=0;
for i in $( awk '{ print $1; }' gpuHertzMe.txt )
	do
		hertzTotal=$(echo $hertzTotal+$i | bc)
		((hertzCount++))
	done

echo "GPU Percent Average: "$(($percentTotal / $percentCount))"%"
echo "GPU Hertz Average: "$(($hertzTotal / $hertzCount))" Mhz"
