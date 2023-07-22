def CopyCatFrameHold(): 
    CopyHold = nuke.nodes.FrameHold()
    CopyHold['firstFrame'].setValue(nuke.frame())
    try:
        CopyHold.setInput(0,nuke.selectedNode())
    except ValueError:
        return None
    
def CopyCatFrameListHold():
    # get and catch a few nuke message errors
    try:
        input_string = nuke.getInput('i.e. 1018, 1125, 1344, ...').split(',')
    except ValueError:
        return None
    except AttributeError:
        return None
        
    # convert and check for errors
    try:
        input_integers = list(map(int, input_string))      
    except ValueError:
        nuke.message("i.e. 1001, 1010, 1020, ...")
        return None
    
    #loop over converted list and error check for non selected node 
    for i in input_integers:
        CopyHold = nuke.nodes.FrameHold()
        CopyHold['firstFrame'].setValue(i)
        try:
            CopyHold.setInput(0,nuke.selectedNode())
        except ValueError:
            next

def customCopyCat():
    #add two python script knobs that call functions
    n = nuke.thisNode()
    n.addKnob(nuke.PyScript_Knob('execute', "Create Frame Hold", "CopyCatFrameHold()"))
    n.addKnob(nuke.PyScript_Knob('execute_list', "Or Create From List", "CopyCatFrameListHold()"))

def main():
    #call custom copy cat
    nuke.addOnCreate(customCopyCat, nodeClass="CopyCat")
    
    
if __name__ == "__main__":
    main()
