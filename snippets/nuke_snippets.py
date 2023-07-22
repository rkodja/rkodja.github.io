
#1----------------------------------------------------------------------------------------------
# NAME: ShowMix
for i in nuke.selectedNodes():
    if i.knob('label').value()=='':
        i.knob('label').setValue('Mix=[value mix]')
    else:
        i.knob('label').setValue('')
 
  

#2----------------------------------------------------------------------------------------------
# NAME: BigFont
for i in nuke.selectedNodes():
    if i.knob('note_font_size').value()==11:
        i.knob('note_font_size').setValue(25)
    else:
        i.knob('note_font_size').setValue(11)



#3----------------------------------------------------------------------------------------------
# NAME: ColorPicker
import nukescripts
nukescripts.color_nodes()



#4----------------------------------------------------------------------------------------------
# NAME: Bbox
for a in nuke.selectedNodes():
    classTypes = ['Merge','Keymix','Copy',]
    for n in classTypes:
        if n in a.Class():
            for p in a['bbox'].values():
                if 'B' in p:
                    a['bbox'].setValue(a['bbox'].values().index(p))



#5----------------------------------------------------------------------------------------------
# NAME: Mirror
selection = nuke.selectedNodes()
allXpos = [i.xpos()+(i.screenWidth()/2) 
for i in selection]
minXpos = min(allXpos)
maxXpos = max(allXpos)

for index, i in enumerate(selection):
    i.setXpos((maxXpos - allXpos[index] + minXpos)-(i.screenWidth()/2))



#6----------------------------------------------------------------------------------------------
# NAME: Select Similar
def getGroupName(name):
    #strip name of numbers at the end
    while name[-1] in [str(i) for i in range(10)]:
            name = name[:-1]  

    return name
    
classesList = [[],[]]

#compose list of selected nodes
for i in nuke.selectedNodes():
    nodeClass = i.Class() 
    if nodeClass != 'Group' and nodeClass not in classesList:
        classesList[0].append(nodeClass)
    else:
        name = getGroupName(i.name())
        if name not in classesList:
            classesList[1].append(name)

#select all nodes
for i in nuke.allNodes():
    nodeClass = i.Class() 
    if nodeClass == 'Group':
        if getGroupName(i.name()) in classesList[1]:
            i.knob('selected').setValue(True)
    else:
        if nodeClass in classesList[0]:
            i.knob('selected').setValue(True)