#!/bin/bash
me=$(whoami)
line=$(grep -rn -w '*) return;;' ../.bashrc | cut -d : -f 1)

if [ $me = "root" ]


then
	echo "Please run as the root"
else


if [ -z $line ]
then
echo ".bashrc is good "
else
sed -i "${line}s>.*>        *)\n        export PATH=/usr/local/cuda-7.0/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\n        export LD_LIBRARY_PATH=/usr/local/cuda-7.0/lib64:\n        export __GL_PERFMON_MODE=1\\n        return;;>" ~/.bashrc
fi
cd ~/
apt-get update -y
apt-get install nano -y
apt-get install git -y
apt-get install python-pip -y
#apt-get install nvcc -y
apt-get install python-scipy -y
apt-get install python-sympy -y
apt-get install python-zmq -y
apt-get install python-wxgtk2.8 -y
apt-get install python-pygame -y
apt-get install libboost-all-dev -y
pip install mako
apt-get install python-execnet -y
export CUDA_ROOT=/usr/local/cuda
#pycuda
PATH=/usr/local/cuda-7.0/bin:$PATH pip install pycuda

#now configuring

#sailfish
git clone https://github.com/sailfish-team/sailfish
cd sailfish*
export PYTHONPATH=$PWD:$PYTHONPATH
python configure.py
python setup.py build

python setup.py install 


#openCV 

apt-get install libopencv-dev python-opencv -y

fi
