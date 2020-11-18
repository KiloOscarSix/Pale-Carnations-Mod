################################################################################
################################################################################
###                               PALE CARNATIONS                            ###
################################################################################
################################################################################

### Click to continue ----------------------------------------------------------

screen clicktocontinue():

    add SnowBlossom("gui/particle.png", count=10, border=50, xspeed=(25, 50), yspeed=-100, start=3, horizontal=False)

    imagebutton xpos 0.5 ypos 0.86:
        idle ("gui/screens/imagebuttons/confirm_idle.png")
        hover ("gui/screens/imagebuttons/confirm_hover.png")
        action MainMenu(confirm=False)
        hover_sound "sound effects/click.wav"
        activate_sound "sound effects/click2.wav"

    imagebutton xpos 0.7 ypos 0.86:
        idle ("gui/screens/imagebuttons/deny_idle.png")
        hover ("gui/screens/imagebuttons/deny_hover.png")
        action Quit(confirm=False)
        hover_sound "sound effects/click.wav"
        activate_sound "sound effects/click2.wav"


### Save File Names ------------------------------------------------------------


### SAVE FILE NAME INPUT

style SaveInputButton:
    color "#ffffff"

style SaveInputButton_text:
    color "#FF8C00"
    selected_color "#FFA500"
    hover_color "#FFA500"

screen give_save_name(slotIndex):
    modal True

    frame:
        xalign .5
        yalign .5
        vbox:
            xalign 0.5
            xsize 450
            ysize 120
            spacing 40
            first_spacing 10

            hbox:
                text "ENTER SAVE NAME"
                yalign 0.5
                xalign 0.5
            hbox:
                input value VariableInputValue("save_name") length 12
                xalign 0.5
                yalign 0.5

            hbox:
                spacing 30
                xalign 0.5

                textbutton "Done":
                    xalign 0.2
                    action [Hide("give_save_name"), FileSave(slotIndex, confirm=False), ShowMenu('save')]

                textbutton "Return":
                    xalign 0.2
                    action [Hide("give_save_name"), ShowMenu('save')]


    key  'K_RETURN' action [Hide("give_save_name"), FileAction(slotIndex, confirm=False), Show("file_slots", title = "Save")]

init python:
    def name_func(newstring):
        store.save_name = newstring
