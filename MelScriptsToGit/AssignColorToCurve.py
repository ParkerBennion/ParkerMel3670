import maya.cmds as cmds

def ChangeColorAndName(StringTemplate, color):
    sels = cmds.ls(selection=True)
    number = 1
    for sel in sels:
        count = StringTemplate.count("#")
        if count == 0:
            print('no Hashes Detected')
            return

        part = StringTemplate.partition('#' * count)

        prefix = part[0]
        suffix = part[2]
        if suffix == "":
            print('hashes need to be consecutive')
            return

        newName = prefix + '_' + str(number).zfill(count) + '_' + suffix
        cmds.rename(sel, newName)
        print(part)
        number += 1

    ChangeColor(color)

def ChangeColor(color):
    sels = cmds.ls(selection=True)

    for sel in sels:
        if color > 31 or color < 0:
            print("Please select a color between 0-31")
            break
        else:
            cmds.setAttr(sel+"Shape.overrideEnabled", 1)
            cmds.setAttr(sel+"Shape.overrideColor", color)

ChangeColorAndName("LeftLeg####Ctrl", 9)

# if you don't rename the object the naming of the shape will be changed
# for example box = boxShape, box1 = boxShape1
# this creates issues if you have objects that both have and don't have numbers at the end of the name
# renaming solves this error but also itroduces limitations of its own