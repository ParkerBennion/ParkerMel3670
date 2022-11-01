import maya.cmds as cmds
##Body
cmds.polySphere(name="base")
cmds.polySphere(name="middle", radius=.7)
cmds.move(0, 1, 0, relative=True, objectSpace=True, worldSpaceDistance=True)
cmds.polySphere(name="Head")
cmds.move(0, 1.8, 0, relative=True, objectSpace=True, worldSpaceDistance=True)
cmds.polySphere(e=True, radius=.3)
# nose
cmds.polyCone(name="Nose", r=.2, height=.5)
cmds.move(.3, 1.8, 0, relative=True, objectSpace=True, worldSpaceDistance=True)
cmds.rotate(0, 0, -90, relative=True, objectSpace=True)
# eyes
cmds.polyCube(name="LeftEye", axis=(.2, .2, .2), depth=.1, height=.1, width= .1)
cmds.move(.2, 1.9, .15, relative=True, objectSpace=True, worldSpaceDistance=True)
cmds.polySoftEdge(angle=0, ch=1, name="LeftEye")

cmds.polySoftEdge(angle=0, ch=1, name="LeftEye")

# button1
cmds.polyCube(name="Button1", axis=(.2, .2, .2), depth=.1, height=.1, width= .1)
cmds.move(.7, 1, 0, relative=True, objectSpace=True, worldSpaceDistance=True)
cmds.polySoftEdge(angle=0, ch=1, name="LeftEye")
cmds.select('Button1', r=True)

# button2
cmds.duplicate(returnRootsOnly=True)
# duplicate comand has alot of function i dont understand and some that i could see being usefull if used in hierarchy.
cmds.move(.3, -1, 0, relative=True, objectSpace=True, worldSpaceDistance=True)

cmds.polyCube(name="RightEye", axis=(.2, .2, .2), depth=.1, height=.1, width=.1)
cmds.move(.2, 1.9, .15, relative=True, objectSpace=True, worldSpaceDistance=True)
cmds.polySoftEdge(angle=0, ch=1, name="RightEye")

cmds.polyCube(name="LeftArm")
cmds.move(0, 1.1, .7, relative=True, objectSpace=True, worldSpaceDistance=True)
cmds.scale(.1, .1, .1, relative=True)
# move r 0 0 0.4
cmds.select('LeftArm', r=True)
cmds.select('LeftArm.f[0]', r=True)
cmds.polyExtrudeFacet('LeftArm.f[0]', constructionHistory=True, keepFacesTogether=True, divisions=True, twist=True, taper=True, off=False, thickness=.5)
cmds.polyExtrudeFacet('LeftArm.f[0]', constructionHistory=True, keepFacesTogether=True, divisions=True, twist=10, taper=1, off=0, thickness=.5)
cmds.move(.3, .1, 0, relative=True, objectSpace=True, worldSpaceDistance=True)
# create and extrude arms
# this is an edge loop which ive included (and copied from maya) to see the complexity. it does not seem to be practical and am wodering how this would be approached for code.
# cmds.delete (polyMoveVertex=True, ch=True, |LeftArm|LeftArmShape.vtx[0] polySplit ch 1 sma 180 ep 0 0.571102 ep 3 0.571102 ep 2 0.571102 ep 1 0.571102 ep 18 0.571102 ep 26 0.571102 ep 22 0.571102 ep 14 0.571102 ep 0 0.571102 |LeftArm|LeftArmShape  select cl)
cmds.select('LeftArm', r=True)
cmds.select('LeftArm.f[19]', r=True)
cmds.polyMirrorFace('LeftArm', cutMesh=1, axis=2, axisDirection=1, mirrorAxis=2, mirrorPosition=0, ch=1)

cmds.polyExtrudeFacet('LeftArm.f[0]', constructionHistory=1, keepFacesTogether=1, divisions=1, twist=20, taper=1, off=0, thickness=.1)
# hat
cmds.polyCylinder(r=.2, subdivisionsHeight=30)
cmds.move(0, 2.93, 0, r=True)
# cmds.select (r=True, pCylinder=1.f[0:19])
# cmds.scale (1.940202, 1.940202, 1.940202, r=True, pivot=(2.23517e08cm, 1.833333cm, 2.98023e08cm))
# pivot seems to be impractical to find withought already knowing what it is from modeling.