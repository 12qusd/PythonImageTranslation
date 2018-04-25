# About
Captures a hand drawn image using a Jetson TX1s build in camera and inputs it into a liquid simulation.

This a proof of concept project created by Xavier Quinn and Shingo Lavine to demonstrate capabilities of heterogenous computers and the clustering of them.

##Installation

###Connect board to internet
Log in to the Jetson board with the default password of `ubuntu`
Click on the wifi symbol in the top right hand corner
Put in your wifi credentials


###Put the required files on your board

Open up your terminal by either clicking on the terminal icon or using the keyboard shortcut `CTRL+ALT+T`

run `sudo apt-get install git`

Be sure you are in home dir `cd ~`

run `git clone https://github.com/12qusd/PythonImageTranslation.git image`

##Setting up

run `cd ~/image`

run `sudo ./setup.sh`

##Usage

Be sure you are in image dir `cd ~/image`
Then run `./go.sh`

press any key to dismiss the image, and press space or r to continue or retake the image.

You can run `./tegra.sh` to get the average CPU usage (which uses \home\ubuntu\tegrastats)

##Clustering

This is a more complicated proccess without a a clean output, so we do not suggest this unless you know what you are doing.

cluster.py is an example of cluster definition file

Cluster definition requires passwordless ssh to be set up between all nodes and that all required software is on each node

To setup passwordless ssh run `ssh-keygen -t rsa`

The IP of each of the compute nodes must be within `/etc/hosts`

Then run `ssh-copy-id <username>@<hostname` for each of the compute nodes


You must set up DHCP and have each of the nodes you want to use in the cluster definition file

Then you will run `python working.py --cluster_spec=cluster.py --subdomains <number of subdomains>`

Other possible arguments include:

`--cluster_spec=cluster.py (to set cluster definition)`

`--cluster_sync=$PWD (sync up cluster files so that sailfish can run on each, we recommend doing this the first time and after any change to the code)`

`--max_iters 10000 (or whatever number you want for max iterations)`

`--subdomains 3 (or multiple of however many nodes are being used)`

`--output DIRECTORY/FILENAME (set where you want output)`

`--output_format vtk,npy,mat (we used vtk and paraview to see results)`


Running on multiples nodes will split the output, which must be combined and viewed in a separate program, paraview seems to work.
