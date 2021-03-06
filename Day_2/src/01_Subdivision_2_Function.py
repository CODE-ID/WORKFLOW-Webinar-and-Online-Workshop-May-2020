__author__ = "Zuardin Akbar"
__version__ = "2020.04.18"

"""
Component Input -- srf, 
Item Access, 
Type Hint: Surface
"""

import Rhino as rh

def Subdivide(_srf):
    #Create emptylist
    listOfSubSurfaces = []
    
    #Get the the U & V domain of the surface as intervals
    u = rh.Geometry.Surface.Domain(_srf, 0)
    v = rh.Geometry.Surface.Domain(_srf, 1)
    
    #Get the domain edge values
    uMin = u.Min
    uMax = u.Max
    vMin = v.Min
    vMax = v.Max
    
    #Get the middle value of the domains
    uMid = (uMax+uMin)/2
    vMid = (vMax+vMin)/2
    
    #Create Division Intervals
    u0 = rh.Geometry.Interval(uMin, uMid)
    u1 = rh.Geometry.Interval(uMid, uMax)
    v0 = rh.Geometry.Interval(vMin, vMid)
    v1 = rh.Geometry.Interval(vMid, vMax)
    
    #Trim the surface using the intervals (Surface division)
    s0 = rh.Geometry.Surface.Trim(_srf, u0, v0)
    s1 = rh.Geometry.Surface.Trim(_srf, u1, v0)
    s2 = rh.Geometry.Surface.Trim(_srf, u0, v1)
    s3 = rh.Geometry.Surface.Trim(_srf, u1, v1)
    
    #Add the splited surfaces into the list
    listOfSubSurfaces.append(s0)
    listOfSubSurfaces.append(s1)
    listOfSubSurfaces.append(s2)
    listOfSubSurfaces.append(s3)
    
    return listOfSubSurfaces

#OUTPUT
sub_Srfs = Subdivide(srf)

#Change OUTPUT
#Create new subdividion from on of the sub surface
newSrfDiv = Subdivide(sub_Srfs[0])
#Remove the sub surface
sub_Srfs.RemoveAt(0)
#Add new surfaces
for s in newSrfDiv:
    sub_Srfs.append(s)

