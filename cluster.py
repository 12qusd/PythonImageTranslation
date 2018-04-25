from sailfish.config import MachineSpec

nodes = [
	MachineSpec('ssh=abra@one//chdir=/home/ubuntu/image', 'abra', cuda_nvcc='/usr/local/cuda/bin/nvcc'),
	MachineSpec('ssh=ubuntu@two//chdir=/home/ubuntu/image', 'ubuntu', cuda_nvcc='/usr/local/cuda/bin/nvcc'),
	MachineSpec('ssh=ubuntu@three//chdir=/home/ubuntu/image', 'ubuntu', cuda_nvcc='/usr/local/cuda/bin/nvcc')

]
