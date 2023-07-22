# Define the knob variable in the outer scope
knob = None

def copy_cornerpin():
    # Get the selected CornerPin node
    selected_node = nuke.thisNode()
    
    if selected_node is None:
        nuke.message("No node selected.")
        return
    
    if selected_node.Class() != 'CornerPin2D':
        nuke.message("Please select a CornerPin node.")
        return
    
    global knob  # Use the knob variable from the outer scope
    knob_name = "Ref Frame"
    knob = selected_node.knob(knob_name)
    if knob is None:
        knob = nuke.Int_Knob(knob_name, "Ref Frame")
        selected_node.addKnob(knob)
    
    script_knob_name = "Set to Current Frame"
    script_knob = selected_node.knob(script_knob_name)
    if script_knob is None:
        script_knob = nuke.PyScript_Knob(script_knob_name, "SetCurrent", "copy_cornerpin_values(nuke.thisNode(), knob)")
        selected_node.addKnob(script_knob)
    
    py_script_knob_name = "Copy Values"
    py_script_knob = selected_node.knob(py_script_knob_name)
    if py_script_knob is None:
        py_script_knob = nuke.PyScript_Knob(py_script_knob_name, "Copy Values", "copy_cornerpin_values(nuke.thisNode(), knob)")
        selected_node.addKnob(py_script_knob)

def copy_cornerpin_values(selected_node, knob):
    knob.setValue(nuke.frame())
    # Get the values from the "to" parameters
    to1 = selected_node['to1'].getValue()
    to2 = selected_node['to2'].getValue()
    to3 = selected_node['to3'].getValue()
    to4 = selected_node['to4'].getValue()
    
    # Clear any existing animation on the "from" parameters
    selected_node['from1'].clearAnimated()
    selected_node['from2'].clearAnimated()
    selected_node['from3'].clearAnimated()
    selected_node['from4'].clearAnimated()
    
    # Set the values to the "from" parameters
    selected_node['from1'].setValue(to1)
    selected_node['from2'].setValue(to2)
    selected_node['from3'].setValue(to3)
    selected_node['from4'].setValue(to4)

# Register the copy_cornerpin_values() function as a callback for the onCreate event
nuke.addOnCreate(copy_cornerpin, nodeClass='CornerPin2D')
