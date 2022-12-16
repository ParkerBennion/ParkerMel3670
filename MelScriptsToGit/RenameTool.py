import maya.cmds as cmds

def RenameSet(StingTemplate):
    sels = cmds.ls(selection=True)
    number = 1
    for sel in sels:
        count = StingTemplate.count("#")
        if count == 0:
            print('no Hashes Detected')
            return

        part = StingTemplate.partition('#' * count)

        prefix = part[0]
        suffix = part[2]
        if suffix == "":
            print('hashes need to be consecutive')
            return

        newName = prefix + '_' + str(number).zfill(count) + '_' + suffix
        cmds.rename(sel, newName)
        print(part)
        number += 1




RenameSet('Leg###Right')
