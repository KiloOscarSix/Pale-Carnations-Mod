screen save():

    tag menu
    add "gui/screens/backgrounds/save_screen.png"
    use file_slots(_("Save"))
    imagebutton auto "gui/screens/imagebuttons/return_%s.png" action Return() xpos 10 ypos 22

    text "{color=#fff}Save Name:{/color}":
        align(0.03, 0.2)
    input:
        align(0.03, 0.25)
        value VariableInputValue("save_name")
