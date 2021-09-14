#created by Jonathan McCoy (c) 2021
#a "Drop it" script that places your object's bottom-most vertex at exactly zero in the Y axis and clearing rotations and transforms
#This is based on the bounding box of your object

from maya import cmds

selectedObject = cmds.ls(selection = True) #get selection

def newPosSet(selectedObj):
    for object in selectedObj:
        cmds.makeIdentity(object,a= True,t = True,r = True, s = True ) #zeros out/freezes transforms so the boundingBox Y min is accurate
        
        bB = cmds.exactWorldBoundingBox(object)[1] #stores minY coordinate
        val = 0-bB #value object moves up or down in Y axis
        
        setVal = cmds.setAttr(object+".translateY",val)
        
                       
a = newPosSet(selectedObject)       
cmds.makeIdentity(a = True,t = True,r = True, s = True, n = True)#resetTransforms
cmds.xform(piv =(0,0,0))#Reset pivot to 0,0,0