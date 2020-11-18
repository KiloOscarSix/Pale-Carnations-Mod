################################################################################
################################################################################
###                               PALE CARNATIONS                            ###
################################################################################
################################################################################

default galleryUnlocked = False

### EXTRAS PARENT SCREEN--------------------------------------------------------


screen leisureroom():
    modal True
    tag menu
    add "screen"


    imagemap:

        idle "gui/screens/imagemaps/leisure_idle.png"
        hover "gui/screens/imagemaps/leisure_hover.png"
        ground "gui/screens/imagemaps/leisure_ground.png"
        hotspot (225,250,340,340) action [ ui.callsinnewcontext("galleryNameChange"), Play ("menu_click","sound effects/page-turn.wav") ], ShowMenu("scenereplay"), Hide("jukebox") hovered [ Play ("hover_load", "sound effects/click.wav") ]
        hotspot (200,659,250,340) action [ Play ("menu_click","sound effects/page-turn.wav") ], ShowMenu("jukebox"), Hide("scenereplay") hovered [ Play ("hover_load", "sound effects/click.wav") ]
        hotspot (450,550,350,320) action [ Play ("menu_click","sound effects/page-turn.wav") ], ShowMenu("bonusimages"), Hide("jukebox"), Hide("scenereplay") hovered [ Play ("hover_load", "sound effects/click.wav") ]
        hotspot (10, 22, 180, 180) action [Return(), Hide("jukebox"), Hide("scenereplay")]



### Bonus Images ---------------------------------------------------------------

screen bonusimages():
    tag menu
    imagemap:

        idle "gui/screens/imagemaps/return_idle.png"
        hover "gui/screens/imagemaps/return_hover.png"
        ground "gui/screens/imagemaps/return_ground.png"
        hotspot (10, 22, 180, 180) action [Hide("bonusimages"), ShowMenu ("leisureroom")]


### Scene Replay ---------------------------------------------------------------

label galleryNameChange:

    default persistent.galleryMcf = ""
    default persistent.galleryMcl = ""


    if persistent.galleryMcf == "":
        show transitionhousegirls with cmet
        show screen textbox2 with dissolve
        "Please enter the name the player character will go by in the scene replay mode."
        hide screen textbox2 with dissolve
        $ persistent.galleryMcf = renpy.input("Enter the player character's given name: ")
    if persistent.galleryMcl == "":
        $ persistent.galleryMcl = renpy.input("Enter the player character's surname: ")
        show screen textbox2 with dissolve
        "You've chosen the name [persistent.galleryMcf] [persistent.galleryMcl]. Is this correct?"
        hide screen textbox2 with dissolve
        menu:
            "Yes, I'll go with [persistent.galleryMcf] [persistent.galleryMcl].":
                pass
            "No, let me rethink that.":
                $ persistent.galleryMcf = ""
                $ persistent.galleryMcl = ""
                jump galleryNameChange

    return


label galleryNameChange2:
    show transitionhousegirls with cmet
    show screen textbox2 with dissolve
    "Do you want to change the name the main character will go by in the scene replay?"
    hide screen textbox2 with dissolve
    menu:
        "Yes, change the name.":
            $ persistent.galleryMcf = renpy.input("Enter the player character's given name: ")
            $ persistent.galleryMcl = renpy.input("Enter the player character's surname: ")

        "No. Keep it as [persistent.galleryMcf] [persistent.galleryMcl].":
            return

screen scenereplay():

    python:
        sceneGalleryList = [
        #  CONDITION                    IMAGE                   LABEL                                           SCOPE
        [persistent.RoseTAGallery, "roseTakeAdvantage", "rosetakeadvantage", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "trait_governor":True}, "Take advantage of Rosalind \nduring the prologue to unlock."],
        [persistent.felBathroomGallery, "felDiscoBathroom", "prDiscoFeliciaBathroomSexStart", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "perk_strongman":True, "history_voyeur":True}, "Ignore Mina at the club \nand do shots with Felicia."],
        [persistent.minaFeliciaKissGallery, "minaFeliciaKiss", "prAfterPartyMinaFeliciaKiss", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl}, "Afterparty: Use your get out of \njail card on Felicia."],
        [persistent.felAfterPartyGallery, "felDiscoAfterParty", "prFelAfterPartyFun", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl}, "Afterparty: Accept Felicia's \nadvances."],
        [persistent.felDiscoThreesomeGallery, "felDiscoThreesome", "prAfterPartyThreesome", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl}, "Afterpaty, high bromance: \ninvite Killian to jon you."],
        [persistent.katCarnationInterviewReplay, "katCarnationInterview", "prMay12meeting", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "perk_socialChameleon":True}, "Progress through the story."],
        [persistent.HarpSaunaBJGallery, "HarpSaunaBJ", "prLeisureTime", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl}, "Progress through the story."],
        [persistent.VeroEggInsertGallery, "VeroEggInsert", "prFaceOffVerRotor", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl}, "Progress through the story."],
        [persistent.FEG1Gallery, "FauxExhibitionGame1", "prFaceOffEndurance", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl}, "Progress through the story."],
        [persistent.FEG2Gallery, "FauxExhibitionGame2", "prFaceOffServility", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl}, "Progress through the story."],
        [persistent.FEG3LucyGallery, "FauxExhibitionGame3Lucy", "prFaceOffCarnalityLucy", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl}, "Progress through the story."],
        [persistent.FEG3VeroGallery, "FauxExhibitionGame3Vero", "prFaceOffCarnalityVer", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "perk_socialChameleon":True, "perk_socialButterfly":True, "history_voyeur":True, "kat_polite":True}, "Progress through the story."],
        [persistent.roseGonzoGallery, "roseGonzo", "w1RoseInterview", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "perk_socialChameleon":True, "perk_socialButterfly":True, "prAfterParty":True, "history_voyeur":True, "kat_polite":True}, "Interview Rosalind during \nWeek 1."],
        [persistent.felGonzoGallery, "felGonzo", "w1FelInterview", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "perk_socialChameleon":True, "perk_socialButterfly":True, "history_voyeur":True, "kat_polite":True}, "Interview Felicia during \nWeek 1."],
        [persistent.veroGonzoGallery, "veroGonzo", "w1VeroInterview", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl}, "Interview Veronica during \nWeek 1."],
        [persistent.roseW1SexGallery, "roseW1Sex", "w1RoseFlag", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "trait_governor":True, "perk_socialButterfly":True, "w1RoseGonzo":True, "kat_polite":True, "roseGonzoPositions":True}, "Rosalind route: Accept \nher proposal."],
        [persistent.felW1FantasyGallery, "felW1Fantasy", "w1FelFantasy", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl}, "Felicia route: progress \nthrough the story."],
        [persistent.gonzoRewardGallery, "gonzoReward", "w1GonzoRewardStart", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "history_voyeur":True, "kat_polite":True}, "Nail the Carnation \ninterview during week 1."],
        [persistent.roseBodyWritingText, "roseBodyWritingText", "w1RosalindSelfies", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl}, "Having fully accepted Rosalind's \nterms, make her prove it."],
        [persistent.veroEx1Grope, "veroEx1Grope", "w1ExVeronica", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "Veronica_Horniness":99}, "Visit Veronica before \nexhibition #1."],
        [persistent.felExhibition1Game1, "felExhibition1Game1", "w1ExIntuitionGameFelicia", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "kat_polite":True}, "Progress through the story."],
        [persistent.roseExhibition1Game1, "roseExhibition1Game1", "w1ExIntuitionGameRosalind", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "kat_polite":True}, "Progress through the story."],
        [persistent.veroExhibition1Game1, "veroExhibition1Game1", "w1ExIntuitionGameVeronica", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "kat_polite":True}, "Progress through the story."],
        [persistent.w1ExGame2VeroFelGallery, "w1ExGame2VeroFel", "w1ExFollowThroughVeroFel", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "kat_polite":True}, "Rosalind won week 1, game 1."],
        [persistent.w1ExGame2VeroRoseGallery, "w1ExGame2VeroRose", "w1ExFollowThroughVeroRose", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "kat_polite":True}, "Felicia won week 1, game 1."],
        [persistent.w1ExGame2RoseFelGallery, "w1ExGame2RoseFel", "w1ExFollowThroughRoseFel", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "kat_polite":True}, "Veronica won week 1, game 1."],
        [persistent.w1ExGame3RoseGallery, "w1ExGame3Rose", "w1ExEarningsGameRosalind", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "kat_polite":True}, "Rosalind lost some variation \nof week 1, game 2."],
        [persistent.w1ExGame3FelGallery, "w1ExGame3Fel", "w1ExEarningsGameFelicia", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "kat_polite":True}, "Felicia lost some variation \nof week 1, game 2."],
        [persistent.w1ExGame3VeroGallery, "w1ExGame3Vero", "w1ExEarningsGameVeronica", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "kat_polite":True}, "Veronica lost some variation \nof week 1, game 2."],
        ]


    add "gui/screens/backgrounds/leisure_jukebox.png"
    textbutton "Change player name" action ui.callsinnewcontext("galleryNameChange2") xpos 0.77 ypos 0.945

    imagebutton:
        action ToggleVariable("galleryUnlocked")
        if galleryUnlocked:
            auto "/modAdditions/images/lockscenes_%s.png"
        else:
            auto "/modAdditions/images/unlockscenes_%s.png"
        anchor (1.0,0.0)
        pos (1310, 250)

    vpgrid:
        cols 2
        spacing 5
        scrollbars "vertical"
        mousewheel True
        draggable True
        pos (0.685, 0.165)
        ymaximum 825

        for i in sceneGalleryList:
            if i[0] or galleryUnlocked:
                imagebutton:
                    auto "images/misc/scene replay/"+i[1]+"_%s.png"
                    action Replay(i[2], scope=i[3], locked=False)
            else:
                imagebutton:
                    action NullAction()
                    idle "images/misc/scene replay/"+i[1]+"_locked.png"
                    tooltip i[4]
    $ tooltip = GetTooltip()
    if tooltip:
        text "[tooltip]":
            pos (1420, 8)

### JUKEBOX --------------------------------------------------------------------

init python:

    mr = MusicRoom(fadeout=1.0)

    mr.add("music/Still_Standing.mp3")
    mr.add("music/organic.mp3")
    mr.add("music/FeelinIt.mp3")
    mr.add("music/cello-suite-No-1-G-Major-Prelude.mp3")
    mr.add("music/philly-crew.mp3")
    mr.add("music/jazz-piano-bar.mp3")
    mr.add("music/frame-of-mine.mp3")
    mr.add("music/ill-remember-you.mp3")
    mr.add("music/hold-on-a-second.mp3")
    mr.add("music/helping-hands.mp3")
    mr.add("music/as-i-figure.mp3", always_unlocked=True)
    mr.add("music/big-rock.mp3")
    mr.add("music/crinoline-dreams.mp3")
    mr.add("music/despair-and-triumph.mp3")
    mr.add("music/george-street-shuffle.mp3")
    mr.add("music/happy-boy-end-theme.mp3")
    mr.add("music/i-knew-a-guy.mp3")
    mr.add("music/leaving-home.mp3")
    mr.add("music/lobby-time.mp3")
    mr.add("music/myst-on-the-moor.mp3")
    mr.add("music/night-on-the-docks-sax.mp3")
    mr.add("music/on-the-ground.mp3")
    mr.add("music/plans-in-motion.mp3")
    mr.add("music/sonatina-in-c-minor.mp3")
    mr.add("music/study-and-relax.mp3")
    mr.add("music/take-the-lead.mp3")
    mr.add("music/there-it-is.mp3")
    mr.add("music/thief-in-the-night.mp3")
    mr.add("music/horrible.mp3")
    mr.add("music/six-days-of-heat-pt2.mp3")
    mr.add("music/Darkdub.mp3")
    mr.add("music/love-or-lust.mp3")
    mr.add("music/hotshot.mp3")
    mr.add("music/called-upon.mp3")
    mr.add("music/thief-in-the-night.mp3")
    mr.add("music/edm-detection-mode.mp3")
    mr.add("music/Moonlight-Sonata.mp3")
    mr.add("music/a-lost-map-of-a-heaven.mp3")
    mr.add("music/beginning-of-conflict.mp3")
    mr.add("music/romantic-motivation.mp3")
    mr.add("music/jack-the-lumberer.mp3")
    mr.add("music/sneaky-snitch.mp3")
    mr.add("music/ukulele-fun.mp3")
    mr.add("music/a-brand-new-start.mp3")
    mr.add("music/happy-whistling-ukulele.mp3")
    mr.add("music/guiton-sketch.mp3")
    mr.add("music/heavy-trailer-1.mp3")
    mr.add("music/catalyst.mp3")
    mr.add("music/rifts-for-days.mp3")
    mr.add("music/pure-energy-9.mp3")
    mr.add("music/st-francis.mp3")
    mr.add("music/jazz-apricot.mp3")
    mr.add("music/swagger.mp3")
    mr.add("music/time-piece.mp3")
    mr.add("music/hep-cats.mp3")
    mr.add("music/epic-battle-speech.mp3")
    mr.add("music/doll-dancing.mp3")
    mr.add("music/victim-to-victor.mp3")
    mr.add("music/echo-sclavi.mp3")
    mr.add("music/anacaptainslogue.mp3")
    mr.add("music/dancebroom-riddim.mp3")



screen jukebox():
    add "gui/screens/backgrounds/leisure_jukebox.png"
    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        xpos 0.7
        ypos 0.15
        ymaximum 825


        vbox:
            # The buttons that play each track.
            textbutton "Romantic Motivation by Aleksound" action mr.Play("music/romantic-motivation.mp3")
            textbutton "Catalyst - Alexander Nakarada" action mr.Play("music/catalyst.mp3")
            textbutton "Jack the Lumberer by Alexander Nakarada" action mr.Play("music/jack-the-lumberer.mp3")
            textbutton "Still Standing - Anno Domini Beats" action mr.Play("music/Still_Standing.mp3")
            textbutton "Moonlight Sonata - Beethoven" action mr.Play("music/Moonlight-Sonata.mp3")
            textbutton "Organic - Beat Doctor" action mr.Play("music/organic.mp3")
            textbutton "Feelin It - Bobby Renz / Text Me Records" action mr.Play("music/FeelinIt.mp3")
            textbutton "Bach Cello Suite No. 1, G Major, Prelude - Cooper Cannel" action mr.Play("music/cello-suite-No-1-G-Major-Prelude.mp3")
            textbutton "Philly Crew - Danny Kean / Doug Maxwell" action mr.Play("music/philly-crew.mp3")
            textbutton "Jazz Piano Bar - Doug Maxwell / Media Right Productions" action mr.Play("music/jazz-piano-bar.mp3")
            textbutton "Frame of Mine - Freedom Trial Studio" action mr.Play("music/frame-of-mine.mp3")
            textbutton "I'll Remember You - Jeremy Blake" action mr.Play("music/ill-remember-you.mp3")
            textbutton "Jazz Appricot - Joey Pecoraro" action mr.Play("music/jazz-apricot.mp3")
            textbutton "Hold On a Second - John Deley and the 41 Players" action mr.Play("music/hold-on-a-second.mp3")
            textbutton "St. Francis - Josh Lippi and The Overtimers" action mr.Play("music/st-francis.mp3")
            textbutton "Heling Hands - Ketsa" action mr.Play("music/helping-hands.mp3")
            textbutton "As I figure - Kevin MacLeod" action mr.Play("music/as-i-figure.mp3")
            textbutton "Big Rock - Kevin MacLeod" action mr.Play("music/big-rock.mp3")
            textbutton "Crinoline Dreams - Kevin MacLeod" action mr.Play("music/crinoline-dreams.mp3")
            textbutton "Despair and Triumph - Kevin MacLeod" action mr.Play("music/despair-and-triumph.mp3")
            textbutton "George Street Shuffle - Kevin MacLeod" action mr.Play("music/george-street-shuffle.mp3")
            textbutton "Guiton Sketch - Kevin MacLeod" action mr.Play("music/guiton-sketch.mp3")
            textbutton "Happy Boy End Theme - Kevin MacLeod" action mr.Play("music/happy-boy-end-theme.mp3")
            textbutton "Hep Cats - Kevin MacLeod" action mr.Play("music/hep-cats.mp3")
            textbutton "I Knew a Guy - Kevin MacLeod" action mr.Play("music/i-knew-a-guy.mp3")
            textbutton "Leaving Home - Kevin MacLeod" action mr.Play("music/leaving-home.mp3")
            textbutton "Lobby Time - Kevin MacLeod" action mr.Play("music/lobby-time.mp3")
            textbutton "Myst on the Moor - Kevin MacLeod" action mr.Play("music/myst-on-the-moor.mp3")
            textbutton "Night on the Docks (Sax) - Kevin MacLeod" action mr.Play("music/night-on-the-docks-sax.mp3")
            textbutton "On the Ground - Kevin MacLeod" action mr.Play("music/on-the-ground.mp3")
            textbutton "Plans in Motion - Kevin MacLeod" action mr.Play("music/plans-in-motion.mp3")
            textbutton "Sneaky Snitch - Kevin MacLeod" action mr.Play("music/sneaky-snitch.mp3")
            textbutton "Sonatina in C-Minor - Kevin MacLeod" action mr.Play("music/sonatina-in-c-minor.mp3")
            textbutton "Study and Relax - Kevin MacLeod" action mr.Play("music/study-and-relax.mp3")
            textbutton "Take the Lead - Kevin MacLeod" action mr.Play("music/take-the-lead.mp3")
            textbutton "There It Is - Kevin MacLeod" action mr.Play("music/there-it-is.mp3")
            textbutton "EDM Detection Mode - Kevin MacLeod" action mr.Play("music/edm-detection-mode.mp3")
            textbutton "Dancebroom Riddim - Konrad OldMoney" action mr.Play("music/dancebroom-riddim.mp3")
            textbutton "Horrible - Mela" action mr.Play("music/horrible.mp3")
            textbutton "Echo Sclavi - The Mini Vandals" action mr.Play("music/echo-sclavi.mp3")
            textbutton "AnaCaptainslogue - Noir Et Blanc Vie" action mr.Play("music/anacaptainslogue.mp3")
            textbutton "Six Days of Heat - Principles of Modeling" action mr.Play("music/six-days-of-heat-pt2.mp3")
            textbutton "Darkdub - Quincas Moreira" action mr.Play("music/Darkdub.mp3")
            textbutton "Love or Lust - Quincas Moreira" action mr.Play("music/love-or-lust.mp3")
            textbutton "Swagger - Quincas Moreira" action mr.Play("music/swagger.mp3")
            textbutton "Doll Dancing - Puddle of Infinity" action mr.Play("music/doll-dancing.mp3")
            textbutton "Beginning of Conflict - Rafael Krux" action mr.Play("music/beginning-of-conflict.mp3")
            textbutton "Happy Whistling Ukulele - Rafael Krux" action mr.Play("music/happy-whistling-ukulele.mp3")
            textbutton "Ukulele Fun - Rafael Krux" action mr.Play("music/ukulele-fun.mp3")
            textbutton "Victim to Victor - RKVC" action mr.Play("music/victim-to-victor.mp3")
            textbutton "Heavy Trailer 1 - Sascha Ende" action mr.Play("music/heavy-trailer-1.mp3")
            textbutton "Pure Energy 9 - Sascha Ende" action mr.Play("music/pure-energy-9.mp3")
            textbutton "Hotshot - Scott Holmes" action mr.Play("music/hotshot.mp3")
            textbutton "A Lost Map Of A Heaven - Shaoqing Li (Luna)" action mr.Play("music/a-lost-map-of-a-heaven.mp3")
            textbutton "Called Upon - Silent Partner" action mr.Play("music/called-upon.mp3")
            textbutton "Time Piece - Silent Partner" action mr.Play ("music/time-piece.mp3")
            textbutton "A Brand New Start - TrackTribe" action mr.Play("music/a-brand-new-start.mp3")
            textbutton "Riffs For Days - TrackTribe" action mr.Play("music/rifts-for-days.mp3")
            textbutton "Epic Battle Speech - Wayne Jones" action mr.Play("music/epic-battle-speech.mp3")

            # The button that lets the user exit the music room.
            textbutton "Return" action Hide("jukebox")
