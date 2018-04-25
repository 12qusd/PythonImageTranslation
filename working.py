#!/usr/bin/env python -u

mult=1

#import everything
import sys, getopt
import numpy as np
import cv2
import os as os
from sailfish.geo import EqualSubdomainsGeometry2D
from sailfish.subdomain import Subdomain2D
from sailfish.node_type import NTFullBBWall, NTHalfBBWall
from sailfish.controller import LBSimulationController
from sailfish.lb_single import LBFluidSim
from sailfish.lb_base import LBForcedSim



#sim size
rezx=256*mult
rezy=256*mult
#print(rezx)
#print(rezy)


# Load an color image in grayscale
img = cv2.imread('image.jpg',0)
	

##Gets the edges of the image
## source, minval,maxval, size of sobel kernal(default 3), L2 gradient(specifies equation for magniture{default false})
edges = cv2.Canny(img,150,50)
scrapedges = cv2.Canny(img,150,50)

##thickens the image if neccisary
kernel = np.ones((5,5), np.uint8)
#fat = cv2.dilate(edges,kernel,iterations = 1) 
cv2.imwrite("1.jpg",edges)


contours,hierarchy = cv2.findContours(scrapedges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)


#fill in
cv2.drawContours(edges,contours,-1,(255,255,255),-1)
cv2.imwrite("2.jpg",edges)

if len(contours) == 0 :
	print " "
	print "Please take a picture with higher contrast"
	sys.exit(0) 
#print contours[0].size

cnt = contours[0]
i=0

for i in range(np.size(contours)) :
	cnt = np.concatenate((cnt,contours[i]), axis=0)
	i=i+1

x,y,w,h = cv2.boundingRect(cnt)
cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

#topy:ottomy,topx:bottomx
edges=edges[y:y+h,x:x+w]
#edges=edges[y-(.25*((y+h)-y)):y+(.25*((y+h)-y)),x-(.25*((x+w)-x)):x+(.25*((x+w)-x))]
#edges=edges[y:y+h,x:x+w]


y=1
x=1

##Get size of image
width, height = edges.shape[:2]

#print height
#print width

#height=75
#width=75



##converts the image to numpy array coordinates for the simulation


f = open("walls.txt", "w")
print "proccesing"
while y < height:
	while x < width:
		xy = edges[x, y]
		if xy != 0:
			f.write("(hx == " + str(x+((int)(rezx-width)/2)) + ") & (hy == " + str(y+((int)(rezy-height)/2)) + ") | ")
	#		print "success"
		x += 1
		
		#print str(x) + "/" + str(width)
		
	
	y += 1
	x=0
f.close()

x=0
y=0
print 'done'
			

#####SAVE THE IMAGE
#cv2.imwrite('output.jpg',edges)

######SHOW THE IMAGE
#cv2.imshow('image', crop)
#destroy window on keypress
#cv2.waitKey(0)
#cv2.destroyAllWindows()

cv2.imwrite("3.jpg",img)
cv2.imwrite("4.jpg",edges)
#cv2.imwrite("crop.jpg",crop)
#cv2.imwrite("croped.jpg",croped)









###################################################################SAILFISH####################################################

#opens numpy coordinates in readable format
for line in open("walls.txt"):
	readline = line[:-3]


class CylinderBlock(Subdomain2D):
    def boundary_conditions(self, hx, hy):
        wall_bc = NTFullBBWall
	walls = eval(readline)
	
	
	#creates the walls	
	self.set_node(walls, wall_bc)
      
        

    def initial_conditions(self, sim, hx, hy):
        sim.rho[:] = 1.0
        sim.vy[:] = 0.0
        sim.vx[:] = 0.0


class CylinderSimulation(LBFluidSim, LBForcedSim):
    subdomain = CylinderBlock

    @classmethod
    def update_defaults(cls, defaults):
        defaults.update({
		
            'lat_nx': rezx,
            'lat_ny': rezy,
            'visc': 0.05})


    @classmethod
    def add_options(cls, group, dim):
        group.add_argument('--vertical', action='store_true')

    @classmethod
    def modify_config(cls, config):
        if config.vertical:
            config.periodic_y = True
        else:
            config.periodic_x = False

    def __init__(self, config):
        super(CylinderSimulation, self).__init__(config)

        if config.vertical:
            self.add_body_force((0.0, 1e-5))
        else:
            self.add_body_force((1e-5, 0.0))


if __name__ == '__main__':
    ctrl = LBSimulationController(CylinderSimulation, EqualSubdomainsGeometry2D)
    ctrl.run()


