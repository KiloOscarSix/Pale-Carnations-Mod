################################################################################
################################################################################
###                               PALE CARNATIONS                            ###
################################################################################
################################################################################

## The opening, character creation, and prologue goes here.

# OPENING TITLE CARD -----------------------------------------------------------

label prStart:

    stop music fadeout 1.5
    scene black with dissolve
    $ renpy.pause(3, hard=True)
    play ambient "sound effects/city-night.wav"
    scene pr0001 with dissolve

    show screen textbox2

    show intronight with squares
    "If I had to describe myself in as few words as possible, I would answer how I think most people would."
    "{i}I'm a good and decent person{/i}."
    "On the surface, that claim might well be true."
    "I study diligently in the pursuit of my dream of becoming a doctor, I'm willing to rock the boat when human decency requires it, and I make sure to call my mother at least three times a week."
    "All in all, not exactly the measure for humanitarian of the year, but I do try not to actively put more shit into the world than I take out."
    "That should at least count me as {i}decent{/i}."
    "......"
    play music "music/leaving-home.mp3"
    "..."

    stop ambient
    scene pr0003 with pixellate

    cm "Haha, man. You guys did a real number on the bitch, huh?"
    cm "Haven't you ever heard of taking it easy on the newbie?"
    scene pr0004 with blinds
    cm "So much for needing to get home, she can barely string two words together."
    cm "Someone roll her into the shower! I bet she could go another round or two."

    scene pr0005 with dissolve
    yth "(Why am I watching this {b}filth{/b}...?)"
    "I {i}like{/i} to consider myself a good and decent person, {b}but{/b}..."

    scene pr0006 with dissolve
    yth "(The face staring back at me through the reflection of the monitor tells a different story.)"
    play sound "sound effects/door-knock.wav"
    "*Knock, knock*"

    scene pr0007 with dissolve
    you "Shit, who could that be?"

    scene pr0001 with fade
    play ambient "sound effects/city-night.wav"
    nl "Hi, I'm across the hall. I think I've got some of your mail by mistake..."
    you "Oh, thank you very much."
    "Truth is, you simply can't take stock of a man's character who lives in an immutable bubble. I have simply never been given the opportunity to prove my conceited self-image right or wrong. "
    "That is, {b}until now{/b}..."
    "With the arrival of a strange letter."

    stop music fadeout 4.0
    hide screen textbox2 with dissolve
    scene pr0008 with Dissolve(5.0)
    $ renpy.pause(4.0, hard=True)
    scene black with blinds
    stop ambient fadeout 3.0
    $ renpy.pause(4.0, hard=True)

#------------------------------------------------------------------------------#
#                              Character Creation                              #
#------------------------------------------------------------------------------#

    scene screen
    with dissolve
    play music "music/on-the-ground.mp3"

# Id-Choice --------------------------------------------------------------------

    show screen textbox2 with dissolve
    sys "Before we begin this twisted tale, let's add a little personal touch to the character whose shoes you're about to fill."
    sys "First, some background."

label idchoice:

    sys "You are a 21 year old college student, studying physics at the local university with the aspiration of getting into medical school. You dream of one day being a general practitioner with your own private practice."
    sys "This dream is motivated purely out of your desire for..."

    scene screen-choice
    with dissolve

    hide screen textbox2 with dissolve

    menu:
        "Money":

            scene screen
            with dissolve

            show screen textbox2 with dissolve
            sys "As they say... {i}money isn't everything, but not having it is{/i}. Growing up watching your mother try and scrape by, you understand that as well as anyone."
            sys "However, for the time being, you're broke-as-shit just like most students. You live off campus subsisting on instant foods, your mother's cooking, and the occasional takeout."
            sys "You are fundamentally concerned with the pursuit and accumulation of wealth. The {b}{color=#008000}pursuit of wealth{/color}{/b} will act as the the counterbalance to your moral scale."
            hide screen textbox2 with dissolve
            jump greedconfirm

        "Respect":

            scene screen
            with dissolve

            show screen textbox2 with dissolve
            sys "You desire to have people treat you with respect and to willingly place their wellbeing in your hands."
            sys "Currently however, you don't even hold the respect of the snot-nosed brats that your tutor as a part-time job."
            sys "You are fundamentally concerned with gaining the upper hand on people. \n{b}{color=#8B0000}Power{/color}{/b} will act as the the counterbalance to your moral scale."
            hide screen textbox2 with dissolve
            jump powerconfirm

        "Helping people":

            scene screen
            with dissolve

            show screen textbox2 with dissolve
            sys "You want to make a difference in people's lives, plain and simple."
            sys "The doctors that cared for your father following his accident were a great comfort to your mother and you desire to emulate that."
            sys "However, that goodwill is tempered by your baser impulses. \n{b}{color=#FF1493}Lust{/color}{/b} will act as the the counterbalance to your moral scale."
            hide screen textbox2 with dissolve
            jump lustconfirm

        "[gr]\[Mod\]{/color} Becoming Omnipotent":
            scene screen
            with dissolve

            show screen textbox2 with dissolve
            sys "You are fundamentally concerned with the pursuit and accumulation of wealth. The {b}{color=#008000}pursuit of wealth{/color}{/b} will act as the the counterbalance to your moral scale."
            sys "You are fundamentally concerned with gaining the upper hand on people. \n{b}{color=#8B0000}Power{/color}{/b} will act as the the counterbalance to your moral scale."
            sys "However, that goodwill is tempered by your baser impulses. \n{b}{color=#FF1493}Lust{/color}{/b} will act as the the counterbalance to your moral scale."
            hide screen textbox2 with dissolve

            $ id_greed = True
            $ toughness += 1
            $ id_power = True
            $ toughness += 2
            $ id_lust = True
            jump namechoice

    sys "Does this sound like the kind of person you want to be?"

    scene screen-choice
    with dissolve

    menu greedconfirm:

        "Yes, let's move on.":
            $ id_greed = True
            $ toughness += 1
            $ toughness = clamp(toughness, 0, 30)

            jump namechoice

        "No, let's go back.":
            jump idchoice

    menu powerconfirm:

        "Yes, let's move on.":
            $ id_power = True
            $ toughness += 2
            $ toughness = clamp(toughness, 0, 30)

            jump namechoice

        "No, let's go back.":
            jump idchoice

    menu lustconfirm:

        "Yes, let's move on.":
            $ id_lust = True
            $ toughness -= 3
            $ toughness = clamp(toughness, 0, 30)

            jump namechoice

        "No, let's go back.":
            jump idchoice


# Name-Choice ------------------------------------------------------------------

label namechoice:

    scene pr0009
    with fade
    show screen textbox2
    sys "This is you. Not the worst mug in the world to be saddled with."
    sys "Let's put a name to that face."

    python:
        mcf = renpy.input("Please input your character's given name. Left blank, it will default to {b}{color=#4169E1}Edwin{/color}{/b}.")
        mcf = mcf.strip()

        if not mcf:
            mcf = "Edwin"
        persistent.mc = mcf

    scene screen
    with dissolve

    sys "Your first name is [mcf]. It was the name of a close friend of your mother growing up."
    sys "You've never met your namesake, but the tender fondness your mother shows when reminiscing about those days fills you with warmth."

    python:
        mcl = renpy.input("Now, what is your family name? Left blank, it will default to {b}{color=#4169E1}Turner{/color}{/b}.")
        mcl = mcl.strip()

        if not mcl:
            mcl = "Turner"
        persistent.mcl = mcl

    sys "Great, you shall be known as {b}{color=#4169E1}[mcf] [mcl]{/color}{/b} for the duration of the story."
    sys "[mcl] is the name passed down to you by your late father. You share it with your mother, who has not since remarried."

# Trait-Choice -----------------------------------------------------------------

    sys "Last but not least, lets fill in some of [mcf]'s personal history."
    sys "These decisions will impart a background and traits that will be reflected in a number of ways as you advance through the story."
    sys "They will alter the context in which some characters view you, open up new dialogue options and actions, and offer you a lens to help understand and navigate [mcf]'s decisions."
    sys "Let's begin."

label traitchoice:

    show screen textbox2
    sys "Starting with your father's death, you had what some might describe as a difficult childhood."
    sys "Growing up you presented with a number of behavior problems, primarily stemming from..."

    hide screen textbox2
    scene screen-choice
    with dissolve

    menu:

        "An abundance of curiosity.":
            scene screen with dissolve
            show screen textbox2
            sys "Your keen interest in pushing boundaries and figuring out how things work was an endless source of consternation for your mother, who did her best to funnel your thirst for knowledge into more productive outlets."
            sys "As an adult, you still derive pleasure from fulfilling that curiosity. You will start the game with the {color=#FF1493}\[Inquisitive]{/color} trait. Would you like to continue?"

            hide screen textbox2
            jump inquisitiveconfirm

        "An abundance of energy.":
            scene screen with dissolve
            show screen textbox2

            sys "Seemingly boundless energy would be enviable in an adult, but in a child makes them quite the handful. You were always moving from one thing to the next, susceptible to finding new ways of getting into trouble."
            sys "The near-endless well of energy you had as a child persists into your young adulthood. You will start the game with the {color=#FF1493}\[Tireless]{/color} trait. Would you like to continue?"
            hide screen textbox2
            jump tirelessconfirm

        "An abundance of anger.":
            scene screen with dissolve
            show screen textbox2

            sys "Due to unreasonable circumstances beyond a child's understanding, you were an angry child. Fortunately, and with great patience, your mother taught you how to mitagate, manage, and sometimes even utilize these feelings toward productive ends."
            sys "Being in control is important to you. You will start the game with the {color=#FF1493}\[Governor]{/color} trait. Would you like to continue?"

            hide screen textbox2
            jump governorconfirm

        "[gr]\[Mod\]{/color} An abundance of godliness":
            scene screen with dissolve
            show screen textbox2
            sys "As an adult, you still derive pleasure from fulfilling that curiosity. You will start the game with the {color=#FF1493}\[Inquisitive]{/color} trait. Would you like to continue?"
            sys "The near-endless well of energy you had as a child persists into your young adulthood. You will start the game with the {color=#FF1493}\[Tireless]{/color} trait. Would you like to continue?"
            sys "Being in control is important to you. You will start the game with the {color=#FF1493}\[Governor]{/color} trait. Would you like to continue?"
            hide screen textbox2

            $ trait_inquisitive = True
            $ trait_tireless = True
            $ trait_governor = True
            $ toughness += 1
            jump historychoice

    menu inquisitiveconfirm:

        "Yes, next question.":
            $ trait_inquisitive = True
            show screen textbox2
            sys "Great! Moving on..."
            jump historychoice
        "No, let me rethink it.":
            jump traitchoice

    menu tirelessconfirm:

        "Yes, next question.":
            $ trait_tireless = True
            show screen textbox2
            sys "Great! Moving on..."
            jump historychoice
        "No, let me rethink it.":
            jump traitchoice

    menu governorconfirm:

        "Yes, next question.":
            $ trait_governor = True
            $ toughness += 1
            $ toughness = clamp(toughness, 0, 30)
            show screen textbox2
            sys "Great! Moving on..."
            jump historychoice
        "No, let me rethink it.":
            jump traitchoice

# History-Choice ---------------------------------------------------------------

label historychoice:
    show screen textbox2
    if trait_inquisitive == True:
        sys "In middle school, this curiosity culminated into one big event which branded you for your entire adolescence.  You..."
    if trait_tireless == True:
        sys "In middle school, this energy culminated into one big event which branded you for your entire adolescence.  You..."
    if trait_governor == True:
        sys "In middle school, this anger culminated into one big event which branded you for your entire adolescence.  You..."

    hide screen textbox2
    scene screen-choice
    with dissolve

    menu:

        "Burned a neighbors garden shed to the ground.":

            show screen textbox2
            scene screen with dissolve

            if trait_inquisitive == True:
                sys "Your curiosity and propensity for seeing the results of even the most destructive acts ended up earning you the reputation of a firebug."
                sys "You are remembered for this deed and will start the game with the {color=#FF1493}\[Firestarter]{/color} history. Would you like to continue?"
                hide screen textbox2
                jump firestarterconfirm

            if trait_tireless == True:
                sys "Unfortunately for your neighbor, as a child you found no better outlet for your tireless energy and the encroaching boredom than starting fires."
                sys "You are remembered for this deed and will start the game with the {color=#FF1493}\[Firestarter]{/color} history. Would you like to continue?"
                hide screen textbox2
                jump firestarterconfirm

            if trait_governor == True:
                sys "Before you got your anger under control, you were prone to lashing out. Unfortunately for your neighbor, one of those outlets included starting fires."
                sys "You are remembered for this deed and will start the game with the {color=#FF1493}\[Firestarter]{/color} history. Would you like to continue?"
                hide screen textbox2
                jump firestarterconfirm

        "Started a business selling creepshots of the neighborhood moms.":

            show screen textbox2
            scene screen with dissolve

            if trait_inquisitive == True:
                sys "Growing boys are naturally curious, but you took it to an enterprising and deviant level - and created quite the neighborhood scandal in the process."
                sys "You are remembered for this deed and will start the game with the {color=#FF1493}\[Voyeur]{/color} history. Would you like to continue?"
                hide screen textbox2
                jump voyeurconfirm

            if trait_tireless == True:
                sys "As a child you, your tireless energy was only matched by your enterprising nature and budding interest in women, resulting in quite the scandalous side business."
                sys "You are remembered for this deed and will start the game with the {color=#FF1493}\[Voyeur]{/color} history. Would you like to continue?"
                hide screen textbox2
                jump voyeurconfirm

            if trait_governor == True:
                sys "Nothing made you angrier than the snobby neighborhood bitches who looked down on your mother. It brought you great pleasure being able to both humiliate them and make some cash on the side."
                sys "You are remembered for this deed and will start the game with the {color=#FF1493}\[Voyeur]{/color} history. Would you like to continue?"
                hide screen textbox2
                jump voyeurconfirm

        "Stole a large sum of money from a school fundraiser.":
            show screen textbox2
            scene screen with dissolve

            if trait_inquisitive == True:
                sys "You were always pushing the envelope in seeing what you could get away with. It stopped firmly at you pocketing your neighbor's money during a school fundraising drive and trying to cover your tracks by giving them discount chocolate bars instead."
                sys "You are remembered for this deed and will start the game with the {color=#FF1493}\[Sticky Fingers]{/color} history. Would you like to continue?"
                hide screen textbox2
                jump stickyfingerconfirm

            if trait_tireless == True:
                sys "The constant need for stimulation would often get the better of you and lead you down the wrong path. In this case, the path involved a \"little\" embezzlement from selling chocolate bars to your neighbors and trying to cover your tracks by giving them discount ones instead."
                sys "You are remembered for this deed and will start the game with the {color=#FF1493}\[Sticky Fingers]{/color} history. Would you like to continue?"
                hide screen textbox2
                jump stickyfingerconfirm

            if trait_governor == True:
                sys "Before you got your anger under control, you were prone to lashing out. This time it took the form of a tinsy-bit of embezzlement from selling chocolate bars to your neighbors and trying to cover your tracks by giving them discounted ones instead."
                sys "You are remembered for this deed and will start the game with the {color=#FF1493}\[Sticky Fingers]{/color} history. Would you like to continue?"
                hide screen textbox2
                jump stickyfingerconfirm

        "[gr]\[Mod\]{/color} Created the Heavens and the Earth in 7 days":
            sys "You are remembered for this deed and will start the game with the {color=#FF1493}\[Firestarter]{/color} history."
            sys "You are remembered for this deed and will start the game with the {color=#FF1493}\[Voyeur]{/color} history."
            sys "You are remembered for this deed and will start the game with the {color=#FF1493}\[Sticky Fingers]{/color} history."
            $ history_firestarter = True
            $ history_voyeur = True
            $ history_stickyFingers = True
            $ statsScreenDict["stats_pcian"]["{u}History{/u}"] = "GOD!"
            jump perkchoice

    menu firestarterconfirm:

        "Yes, next question.":
            $ history_firestarter = True
            show screen textbox2
            "Moving on..."
            jump perkchoice

        "No, let me rethink it.":
            jump historychoice

    menu voyeurconfirm:

        "Yes, next question.":
            $ history_voyeur = True
            show screen textbox2
            "Moving on..."
            jump perkchoice

        "No, let me rethink it.":
            jump historychoice

    menu stickyfingerconfirm:

        "Yes, next question.":
            $ history_stickyFingers = True
            show screen textbox2
            "Moving on..."
            jump perkchoice

        "No, let me rethink it.":
            jump historychoice


# Perk-Choice ------------------------------------------------------------------

label perkchoice:
    show screen textbox2
    sys "By high school, you cleaned up your act. Aside from the friends you made in the physics club, you found a new peer group thanks to your..."

    hide screen textbox2
    scene screen-choice
    with dissolve

    menu:
        "Enthusiasm for athletics.":
            show screen textbox2
            scene screen with dissolve

            sys "You were drawn to the soccer team as a sophomore in high school. The thrill of competition, the sting of loss, and the jubilation of crushing an opponent proved an intoxicating combination."
            sys "As a result, your current level of fitness remains excellent. You will start the game with the {color=#FF1493}\[Strongman]{/color} perk. Would you like to continue?"
            hide screen textbox2
            jump strongmanconfirm

        "Budding social grace and charm.":
            show screen textbox2
            scene screen with dissolve

            sys "You discovered an innate talent at using your words and humor to ingratiate yourself to others and overcome their defenses."
            sys "As a result, you're quite adept at winning people over with your words. You will start the game with the {color=#FF1493}\[Social Butterfly]{/color} perk. Would you like to continue?"
            hide screen textbox2
            jump socialbutterflyconfirm

        "Willingness to lie and conform to get what you want.":
            show screen textbox2
            scene screen with dissolve

            sys "You were quick to discover the best way to get what you want is to {i}be{/i} what other people want."
            sys "As a result, you're quite deft at manipulating people. You will start the game with the {color=#FF1493}\[Social Chameleon]{/color} perk. Would you like to continue?"
            hide screen textbox2
            jump socialchameleonconfirm

        "[gr]\[Mod\]{/color} Transcendence":
            show screen textbox2
            scene screen with dissolve
            sys "As a result, your current level of fitness remains excellent. You will start the game with the {color=#FF1493}\[Strongman]{/color} perk."
            sys "As a result, you're quite adept at winning people over with your words. You will start the game with the {color=#FF1493}\[Social Butterfly]{/color} perk."
            sys "As a result, you're quite deft at manipulating people. You will start the game with the {color=#FF1493}\[Social Chameleon]{/color} perk."
            hide screen textbox2

            $ perk_strongman = True
            $ perk_socialButterfly = True
            $ perk_socialChameleon = True
            $ toughness += 1
            $ statsScreenDict["stats_pcian"]["{u}Perk{/u}"] = "GOD!"
            jump may07start

    menu strongmanconfirm:

        "Yes.":
            $ perk_strongman = True
            jump may07start

        "No, let me rethink it.":
            jump perkchoice

    menu socialbutterflyconfirm:

        "Yes.":
            $ perk_socialButterfly = True
            jump may07start

        "No, let me rethink it.":
            jump perkchoice

    menu socialchameleonconfirm:

        "Yes.":
            $ perk_socialChameleon = True
            $ toughness += 1
            $ toughness = clamp(toughness, 0, 30)

            jump may07start

        "No, let me rethink it.":
            jump perkchoice


label may07start:

    show screen textbox2
    sys "Great! We are now ready to begin."
    sys "So, without further ado, let's get this show on the road. {b}Enjoy!{/b}"
    hide screen textbox2
    stop music fadeout 3.0

#------------------------------------------------------------------------------#
#                                  May 07                                      #
#------------------------------------------------------------------------------#

# Carnation Club Invitation ---------------------------------------------------

    scene black with fade
    $ date = "may07day"
    $ renpy.pause(3, hard=True)
    play music "music/lobby-time.mp3"
    scene player-room with blinds
    show screen textbox2
    show may07day with squares
    "Before me, a strange letter."

    scene pr0010 with dissolve

    "Seemingly addressed to no one in particular, it was written on ornate parchment and was suspiciously devoid of a return address."
    "The quick and dirty of it read..."

    hide screen textbox2
    scene player-room blur with dissolve

    show text "Dear esteemed sir, the {font=gui/fonts/Pacifico.ttf}{color=#FF1493}{i}Carnation Club{/i}{/color}{/font} would like to extend to you the opportunity to join our humble establishment." at truecenter
    with dissolve
    pause 2.75
    pause
    hide text
    with dissolve

    show text "You have come to our attention through a like-minded member who believes you share in our exacting taste." at truecenter
    with dissolve
    pause 2.75
    pause
    hide text
    with dissolve

    show text "Should you wish it, the chance to gratify these tastes is within your reach." at truecenter
    with dissolve
    pause 2.5
    pause
    hide text
    with dissolve

    show text "Do note, this is not an opportunity we afford to just anyone." at truecenter
    with dissolve
    pause 2.5
    pause
    hide text
    with dissolve

    show text "You will find enclosed, blah blah {b}blah{/b}..." at truecenter
    with dissolve
    pause 1.5
    pause
    hide text
    with dissolve

    scene player-room with dissolve
    show screen textbox2 with dissolve
    "It continued on like that for some length, full of bewildering language and other nebulous-like promises before directing me to a phone number."
    "I would've simply tossed it in the trash without a second thought, chalking it up as a sales pitch for a shady multi-level marketing scheme, had it not been for another small note neatly enclosed within."

    hide screen textbox2
    scene player-room blur with dissolve

    show text "Sorry for that cryptic hogwash. My nephew tells me you're looking for a new line of work?" at truecenter
    with dissolve
    pause 2.5
    pause
    hide text
    with dissolve

    show text "Do me the favor of giving an old man a call and I'll explain to you what this is all about. {color=#FF1493}{i}- Chuck{/i}{/color}" at truecenter
    with dissolve
    pause 2.5
    pause
    hide text
    with dissolve

    scene player-room with dissolve
    show screen textbox2 with dissolve

    "'Chuck' was Dr. Charles Kohler, or as the Morehead Hills High School Physics Club affectionately knew him..."

    scene pr0011
    with dissolve

    mct "(Dr. Chuck has a job for me...?)"

    scene player-room
    with dissolve

    "As odd as the letter was, Dr. Chuck was once a real deal rocket scientist and a personal mentor to me through out high school. He also just happens to be the uncle of my best friend."
    "Whatever this is about, it would be safe to say it's more legitimate than it appears."

    scene pr0011
    with dissolve

    mct "(Coming from a man of his stature, it might even be a good way to pad my résumé for med school...)"

    if toughness <= 15:
        mct "(At the very least, it'd be nice if I could quit tutoring those difficult brats.)"

    else:
        mct "(At the very least, it'd be nice if I could quit tutoring those unmotivated shits.)"

    scene player-room
    with dissolve


    "Presently, I work part time as a math tutor to a handful of spoiled, underachieving monsters."
    "Needless to say, it isn't something I'd be doing if the money wasn't so good."
    "Witnessing the upper class of Morehead Hills take their social privilege for granted is not my idea of job satisfaction, but it pays extremely well."
    "If I could find a part-time job that could even compare to what I currently pull in, even if it had longer hours, I'd jump ship in an instant."

    scene pr0011
    with dissolve

    mc "...I should give Dr. Chuck a call first before I get my hopes up."

    scene player-room

    show cell-phone at Position (ypos=0.6)
    with dissolve

    "Trying my best to keep my expectations in check, I take out my cellphone and begin to scroll through its meager contact list."

    scene pr0011
    show cell-phone at Position (ypos=0.6)
    with dissolve

    mct "(I should still have his number...)"
    mc "Aha! There it is."

# May 07 Call with Dr. Chuck ---------------------------------------------------

    scene player-room blur

    show cell-phone at Position (ypos=0.6)
    with dissolve
    play sound "sound effects/ringing-outbound.mp3"

    "{i}*Ring... ring...*{/i}"
    "Eventually the ringing is cut short by a familiar voice on the other end."

    stop sound
    scene player-room blur with dissolve
    show chuck-call with dissolve

    chuck "[mcl]? Is that you? Good to hear from you, lad!"
    chuck "How the hell are you?"

    "Dr. Chuck's boisterous and genial nature was coming in loud and clear on the other line."
    "Despite being exposed to it at length throughout my childhood, the abruptness of his booming voice was startling after not hearing it for some time."

    hide screen textbox2 with dissolve
    scene player-room blur with dissolve

    menu:
        "Be polite. [red]\[Toughness -1\]":
            show screen textbox2
            scene player-room blur
            show chuck-call with dissolve
            mc "Uh... It's going well, sir. How are you?"
            chuck "Sir? C'mon, lad! You've eaten Thanksgiving with my family. You know that Chuck is just fine."
            $ chuck_polite = True
            $ toughness -= 1
            $ toughness = clamp(toughness, 0, 30)

        "Match his enthusiasm. [gr]\[Chuck +1\]":
            $ Chuck_Friendship +=1
            $ Chuck_Friendship = clamp(Chuck_Friendship, 0, 10)
            show screen textbox2
            scene player-room blur
            show chuck-call with dissolve
            mc "Likewise, Dr. Chuck! It's great to hear your voice again."


    chuck "So, how's my alma mater treating you? I bet you're too busy chasing skirts to focus on your studies. Am I right? {b}Bahaha{/b}!"
    mct "(He hasn't changed a bit, has he?)"

    if chuck_polite == True:
        mc "College is good, sir. Thank you again for your recommendation."
    else:
        mc "College is good. Thank you again for your recommendation."

    chuck "Of course, lad. No problem, but speaking of {b}letters{/b}..."
    chuck "I'm assuming it was {i}that{/i} letter which prompted this call. Am I right?"
    mc "Yeah, that strange one on the gaudy letterhead. I called you as soon as I read it."
    chuck "{i}Gaudy{/i} is a good way of putting it, eh? That would be ol' August's doing. Fits him to the tee."
    chuck "Quite frankly, I don't know what the hell is wrong with a simple phone call, but I suppose it's all part of the mystique he seeks to cultivate."
    chuck "Says secrecy and exclusivity is paramount to drum up the brand of customer we cater to."
    chuck "Anyway, to get the {b}point{/b} of the letter..."
    chuck "To put it simply, I own a significant stake in a local business, alongside two of my oldest friends. It's a lounge of sorts."
    chuck "We're looking for a new set of hands, and as luck would have it, my nephew told me you were {i}unhappy with teaching math to shitty brats{/i}. His words."
    chuck "Anyway, he quite emphatically recommended you for the position."
    chuck "I gave it some thought and realized, while you're not the type of person we typically employ, I don't think that's necessarily a bad thing."
    chuck "Interested in a change of careers?"
    mc "A job at the... the {b}Carnation Club{/b}, you mean?"
    "I recalled the name ostentatiously printed in big gold letters."
    mc "I've never heard of it."
    chuck "That's by design. Our members are, to put it mildly, concerned with the question of privacy."
    chuck "As for specifics, well..."

    scene black
    with dissolve

    "..."

    scene player-room blur with dissolve
    show chuck-call with dissolve

    chuck "Good! I'll set up the meeting for say... around noon?"
    mc "Noon works for me."
    chuck "Excellent. You'll be meeting with an August Byrnes. He's a part-owner and the gentleman who runs the day-to-day business."
    chuck "Sorry for being light on the details, but the job itself is something that is best detailed in person."
    chuck "I can assure you though, it's worth your time. You'll be well compensated, plus there's some unique perks that'll knock you flat on your ass. I guarantee it! {b}Bahaha{/b}!"


    if chuck_polite == True:
        mc "Count on me being there, sir."
    else:
        mc "Count on me being there, Dr. Chuck."

    mc "Thank you for the opportunity."

    scene player-room
    with dissolve

    "Whatever it is."

    scene player-room blur
    show chuck-call
    with dissolve

    chuck "Well, alright lad. I've got to run."
    chuck "If you take the job, I'm sure we'll be seeing each other very soon."

    if chuck_polite == True:
        mc "Have a good afternoon, sir. Goodbye."
    else:
        mc "Great! Have a good one, Dr. Chuck. Goodbye!"

    play sound "sound effects/call-end.wav"

    "*Beep.*"

    scene player-room
    with dissolve

    "He wasn't kidding about being light on the details."
    "In fact, I barely learned more than that bizarre letter already told me - which was precisely jack shit."
    "All I know is the place is some kind of lounge, but as to what I'd be doing there, Dr. Chuck was oddly evasive."
    "Some form of hospitality or service job would be a safe bet."

    scene pr0011
    with dissolve

    mct "(I guess I'll just have to wait until tomorrow to find out definitively.)"
    mc "..."
    mc "Ah, {b}crap{/b}!"

    scene player-room
    with dissolve

    "Suddenly, I remembered a conflicting date I had made."

    scene pr0011
    with dissolve

    mct "(I was supposed to have lunch with mom tomorrow...)"
    mct "(I guess I'll have to reschedule. It seems I bail on the plans we make more and more these days...)"

    scene player-room
    with dissolve

    "She'll be cool with it, but I still can't help but feel a little guilty when I picture her eating dinner all alone in that house."

    scene black
    with fade
    stop music fadeout 3.0

    "I tried looking the \'Carnation Club\' up on the Internet, but failed to find a single mention of it anywhere."
    mct "(It must really must be as exclusive as he says.)"
    "......"
    "..."

    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionhana01 with blinds
    $ renpy.pause(6, hard=True)

# Dinner with Mom---------------------------------------------------------------

    $ date = "may07night"
    stop sound
    scene pr0012 with blinds
    show screen qmenu with dissolve
    show screen textbox2 with dissolve
    show may07night with squares

    play music "music/crinoline-dreams.mp3"

    "To make up for having to cancel tomorrow's lunch plans, I instead had dinner at my mother's place that night."

    scene pr0013
    with dissolve

    vic "I remember Dr. Kohler. Wasn't he... uh..."

    scene pr0014
    with fade

    vic "Wasn't he a bit... off?"

    scene pr0015
    with dissolve

    mc "He treated us more like adults than the other teachers did, if that's what you mean."

    scene pr0016
    with dissolve

    vic "Hmm. Maybe that's it..."
    "She seemed like she wanted to say more, but thought better of it."

    scene pr0017
    with dissolve

    vic "Well, if you're going to miss our date, you better get a good job out of this! Who else is going to take care of me when I'm old?"

    hide screen textbox2 with dissolve
    scene pr0018 with fade

    menu:

        "Reassure her.":
            show screen textbox2 with dissolve
            mc "We'll see, but I won't take it if it'll impact my studies."
            scene pr0019 with dissolve
            vic "Sometimes I wonder how I managed to raise you to be so damn serious. You don't get that from your father OR me."


        "Joke with her.":
            show screen textbox2 with dissolve
            mc "That's a good question... we should probably start looking into retirement homes for you, huh?"
            scene pr0020 with dissolve
            vic "Oh, you ass!"


    scene pr0024 with dissolve
    vic "So you have no idea what sort of job you're interviewing for?"
    mc "I'm not even sure if it's going to even be an interview."
    scene pr0025 with dissolve
    vic "That's kind of a weird thing not to know, ain't it?"
    scene pr0022 with dissolve
    mc "Ian recommended me for the job, so I don't know if this is more of an informal introduction or a proper job interview."
    scene pr0028 with dissolve
    vic "It pays to know people, huh? Speaking of Ian..."
    vic "How {i}is{/i} our little heart throb?"
    mc "Pretty much like high-school, but... uh, {i}worse{/i}."
    scene pr0019 with dissolve
    vic "You shouldn't be so harsh on him, hun."
    vic "There's not anything wrong with enjoying your youth. How else are you going to work out what you want out of life?"
    vic "In fact, I don't think it'd hurt for you to follow his example once in a while."
    hide screen textbox2 with dissolve
    scene pr0018

    menu:
        "Agree. [gr]\[Toughness +1\] \[Killian +1\]":
            $ toughness += 1
            $ toughness = clamp(toughness, 0, 30)
            $ Killian_Bromance += 1
            $ Killian_Bromance = clamp(Killian_Bromance, 0, 40)
            show screen textbox2 with dissolve
            mc "You might be right, but... his definition of fun is the kind of frivolity his family's wealth affords him."
            mc "Although, I'm not sure if I had all the money in the world I'd behave the way he does."
            scene pr0028 with dissolve
            vic "That's 'cause you're a sweet boy, but then so is Ian in his own way."

        "There's a limit.[red]\[Toughness -1\] \[Killian -1\]":
            $ toughness -= 1
            $ toughness = clamp(toughness, 0, 30)
            $ Killian_Bromance -= 1
            $ Killian_Bromance = clamp(Killian_Bromance, 0, 40)
            show screen textbox2 with dissolve
            mc "Sure, but there's such a thing as common decency. He can be a {b}real{/b} prick sometimes."

    scene pr0025 with dissolve
    vic "You should cut him some slack. You know how he was brought up."
    scene pr0022 with dissolve
    "My mom was right. Even if our personalities are night and day, Ian has always been a good friend to me."
    "Even though I suck at calling him, he's been insistent on keeping in touch over the years."
    mct "(Come to think of it, I should call and thank him for mentioning me to his uncle.)"
    scene pr0028 with dissolve
    vic "Say hi to him from me the next time you see him, okay?"
    mc "Will do."
    scene pr0022 with dissolve
    mc "So..."
    hide screen textbox2 with dissolve

    menu prVicDinner:

        "Talk about..." if prVicDinner_score < 3:
            menu:

                "Her work." if prVicDinner_work == False:
                        show screen textbox2
                        mc "How's work coming?"
                        scene pr0024 with dissolve
                        vic "Mind numbing! Just about the only regular work I can find is copy editing."
                        "A few years after I moved away from home, my mother is finally dusting off her English degree she was working on when she met dad."
                        vic "Don't get me wrong, I'm enjoying the freedom. I like working from home and it's better than being walked all over as PA or book-keeping with a handsy boss..."
                        scene pr0022 with dissolve
                        "Growing up, my mother often had to work multiple jobs to make ends meet."
                        "My mom has worn many hats over the years, from clerical work to retail to more demeaning labor. That's why..."
                        mc "Once I'm a doctor and pulling in money, you can focus on what you want to write, okay?"
                        scene pr0028 with dissolve
                        vic "Oh? Already writing checks you can't cash are we?"
                        vic "I was only kidding earlier about you taking care of me. You know that, right?"
                        scene pr0022 with dissolve
                        mc "So? I'm serious."
                        mc "It's only fair after all you've..."
                        scene pr0026 with dissolve
                        vic "{b}Stop it{/b}! I appreciate the sentiment..."
                        vic "But, you know I could never ask or accept that from you. I have too much pride for that."
                        hide screen textbox2 with dissolve
                        scene pr0018 with dissolve
                        $ prVicDinner_work = True
                        $ prVicDinner_score += 1
                        jump prVicDinner






                "Her dating life." if prVicDinner_date == False:
                            show screen textbox2 with dissolve
                            mc "Hey... didn't you mention last week you set up an online dating profile? How's that going?"

                            "Growing up, my mother's romantic entanglements were few and far between. Even as a kid I could tell she was lonely."
                            "I'd wager even more so since I moved out of the house three years ago."
                            scene pr0027 with dissolve
                            vic "I did, but I'm still not sure if I should take it seriously. Online dating at my age feels kinda... pathetic."
                            scene pr0018 with dissolve
                            hide screen textbox2 with dissolve

                            menu:
                                "Tell her it's not pathetic.":
                                    $ toughness -= 1
                                    $ toughness = clamp(toughness, 0, 30)
                                    show screen textbox2 with dissolve

                                    mc "It's not pathetic - it's just about how everyone does it these days. You should try to find someone."
                                    scene pr0019
                                    vic "I can say the same to you. It's not good for a young man in his prime to lock himself away in his apartment studying all the time."
                                    vic "You're only 21, it's your prerogative to let loose and sow a few wild oats."
                                    scene pr0018
                                    mc "How could I ever think of dating when I've got my own aging mother facing spinsterhood?"
                                    scene pr0020
                                    vic "Nice try, but you don't fool me. You just want someone else to help out around here."
                                    hide screen textbox2 with dissolve
                                    scene pr0018 with dissolve

                                    $ prVicDinner_date = True
                                    $ prVicDinner_score += 1
                                    jump prVicDinner

                                "Dissuade her.":
                                    show screen textbox2 with dissolve
                                    mc "It might be for the best. Who know what kinda weirdos are out there?"
                                    scene pr0027 with dissolve
                                    vic "Yeah, you do hear stories..."
                                    hide screen textbox2 with dissolve
                                    scene pr0018 with dissolve
                                    mc "Just give it time."
                                    mc "People found other people before online dating."

                                    $ prVicDinner_date = True
                                    $ prVicDinner_score += 1
                                    jump prVicDinner


                "Recent Movies." if prVicDinner_movies == False:
                                show screen textbox2 with dissolve
                                mc "You watch any movies recently?"
                                scene pr0021
                                vic "Hmm, I did watch one I hadn't seen before recently. A movie called {i}Spirits of the Dead{/i}."
                                vic "It's an anthology film depicting three adaptations of Edgar Allen Poe short stories, one of which is by Fellini."
                                vic "I think you would like it. {b}In fact{/b}, we could watch it tonight if you want..."
                                hide screen textbox2 with dissolve
                                scene pr0018 with dissolve

                                $ prVicDinner_movies = True
                                $ prVicDinner_score += 1
                                jump prVicDinner



        "Compliment her cooking." if prVicDinner_compliment == False:
            show screen textbox2 with dissolve
            mc "Dinner was delicious, Mom. Thanks for the food."
            scene pr0028 with dissolve
            vic "Happy to hear it. I've been trying to become a better cook now that I've got more free time."
            vic "I always felt bad about the amount of takeout we ate when you were growing up."
            scene pr0025 with dissolve
            vic "You come around more often, there may be more in it for you."
            hide screen textbox2 with dissolve
            scene pr0018 with dissolve

            $ prVicDinner_compliment = True
            jump prVicDinner


        "Finish the conversation and excuse yourself to the bathroom.":

            show screen textbox2 with dissolve
            mc "I've got to hit the head."
            scene pr0021
            vic "Would you like a plate to take home?"
            scene pr0018
            mc "Yeah, it's been ramen for me all week... so, {b}yes{/b}. I would like that."


# Mom exposition ---------------------------------------------------------------

    scene black with dissolve
    "My mother..."
    stop music fadeout 4.0
    play sound "sound effects/door-openclose.wav"
    $ renpy.pause(4, hard=True)
    scene player-room-dark with dissolve

    "She's the only person I call family."
    play music "music/leaving-home.mp3" fadein 3.0
    "Her and I have been on our own since I was six years old."

    scene pr0030 with dissolve

    "Even at life's most bitter moments, she never faltered in her role as a mother to me."
    "Having run away from home when she was a teenager, and with my paternal grandparent's not wanting anything to do with us following my father's death, the responsibility of my upbringing rested solely on her shoulders."

    scene pr0031 with dissolve

    "Despite being utterly alone, I remember her always looking ahead for my sake, face affixed in a radiant smile and putting on a brave front so I wouldn't worry."

    scene pr0032 with dissolve

    "When I was too much to handle, and trust me I was, she never so much as veered from her characteristic gentle demeanor."

    scene pr0033 with dissolve

    "I don't know how she managed it alone. Rearing a child, paying the bills, putting food on the table..."
    "I brought it up one time, and all she had to say was..."

    scene pr0034 with dissolve

    vic "I wasn't alone! I have you, dummy."

    scene black
    with fade

    mc "(...but I do know how she managed it, don't I?)"

    scene pr0035 with pixellate


    cm "Why are you acting so shy, Ma'am?"

    stop music fadeout 3.0
    scene pr0036 with dissolve
    with dissolve

    cm "It's not like it's your first time, right?"

    scene player-room-dark with pixellate
    play sound "sound effects/sms-chime.wav"

    mct "(Oh...?)"
    mct "(Good, it's Ian.)"
    play music "music/thief-in-the-night.mp3" fadein 3.0
    mct "(I can take this opportunity to thank him properly.)"
    hide screen textbox2 with dissolve
    hide screen qmenu

# May 07 Ian Text --------------------------------------------------------------

    scene player-room-dark blur with dissolve
    call phone_start_kil from _call_phone_start_kil_1


    call message_start("Killian", "Hey, Doc!") from _call_message_start_1
    call message ("Killian", "Why don't you put a pin in studying and come join us for some fun?") from _call_message
    call message_img("Killian", "Mina's got an OLDER friend that's keen to meet you. I know that's how you like 'em. ;)","killian01") from _call_message_img
    call phone_end_kil from _call_phone_end_kil_1
    scene pr0041 with dissolve

    "I got to hand it to Killian. Aside from being the one who makes the effort, he does his best as a wingman."
    mct "(At least one of us is trying to get me laid.)"
    scene player-room-dark blur with dissolve


    call phone_start_kil from _call_phone_start_kil_2
    call message_start("Killian", "You got a sailor uniform somewhere? I may or may not have told her you were a pent up navyman on shore leave.") from _call_message_start_2

    call phone_end_kil from _call_phone_end_kil_2

    mct "..."
    "I just wish he didn't do it in the worst way imaginable."

    scene player-room-dark blur with dissolve

    call phone_start_kil from _call_phone_start_kil_3
    call message_start("Killian", "So, what do you think? Blow off some steam before finals?") from _call_message_start_3

    call screen phone_reply("Politely decline.","politelydecline","Get annoyed.","getannoyed")

label politelydecline:

    $ toughness -= 1
    $ toughness = clamp(toughness, 0, 30)
    $ Killian_Bromance += 1
    $ Killian_Bromance = clamp(Killian_Bromance, 0, 40)

    call phone_after_menu from _call_phone_after_menu
    call message_start("[mcf]", "Nah, it's late and I'm going to hit the sack.") from _call_message_start_4
    call reply_message("Plus, I've got a meeting with your uncle tomorrow about working at that lounge he owns. Thanks for that, by the way. You're a better friend than I.") from _call_reply_message
    call message("Killian", "Already? I didn't expect that to get set up so soon. When?") from _call_message_1
    call reply_message ("Noon.") from _call_reply_message_1
    call message("Killian", "I see...") from _call_message_2
    call message("Killian", "Anyway more fun for me I guess!") from _call_message_3
    call message("Killian", "Night!") from _call_message_4
    call phone_end_kil from _call_phone_end_kil_3
    jump killiangoodnight

label getannoyed:
    $ toughness += 1
    $ toughness = clamp(toughness, 0, 30)
    $ Killian_Bromance -= 1
    $ Killian_Bromance = clamp(Killian_Bromance, 0, 40)
    $ prKillianAnnoyed = True

    call phone_after_menu from _call_phone_after_menu_1
    call message_start("[mcf]", "Will you stop lying on my behalf? That woman looks nice. Don't be a jerk.") from _call_message_start_5
    call message("Killian", "C'mon, dude! Start thinking with that seriously underused, OTHER head of yours.") from _call_message_5
    call reply_message("Anyway, I can't go out tonight. I got a meeting that your uncle set up for me tomorrow about that job.") from _call_reply_message_2
    call message("Killian", "Shit. I didn't expect that to get set up so soon. When?") from _call_message_6
    call reply_message("Noon.") from _call_reply_message_3
    call message("Killian", "I see...") from _call_message_7
    call message("Killian", "Anyway, since you're being a self-righteous ass, more fun for me I guess!") from _call_message_8
    call message("Killian", "Night.") from _call_message_9
    call phone_end_kil from _call_phone_end_kil_4
    jump killiangoodnight

label killiangoodnight:

    if prKillianAnnoyed == True:
        scene player-room-dark with dissolve
        mc "..."
        mct "(Shit. I forgot to thank him...)"
        mct "(I'll do it the next time I talk to him.)"

    stop music fadeout 4.0
    show screen textbox2 with dissolve
    show screen qmenu
    scene black with dissolve
    $ profilehubunlock = True
    play sound "sound effects/notification.wav"
    show biounlock with dissolve
    $ renpy.pause(3, hard=True)
    "..."
    scene pr0040 with dissolve
    play sound "sound effects/shower.wav"
    "As much as I want to, it's too late to study tonight."
    mct "(Mom ended up roping me into watching one of her old Italian flicks.)"
    scene player-room-dark with dissolve
    stop sound fadeout 1.0
    mct "(I guess I'll just head to bed.)"
    scene black with dissolve

    "........."
    "......"
    "..."
    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionmina01 with blinds
    $ renpy.pause(6, hard=True)


    $ date = "may08day"
    stop sound


label may08start:

#------------------------------------------------------------------------------#
#                                  May 08                                      #
#------------------------------------------------------------------------------#

    scene pr0042 with blinds
    show screen textbox2 with dissolve
    show screen qmenu
    show may08day with squares
    play ambient "sound effects/city-night.wav"

    "The next day I took the subway to the address Dr. Chuck provided me, a brick tower starkly at odds with its surrounding neighbors."
    "I was told to ride the elevator to the 10th floor, walk up two more floors, and give the bouncer the password."

# Meeting with Killian ---------------------------------------------------------

    scene pr0043 with blinds
    mct "(This whole thing feels stupidly clandestine.)"
    scene pr0044 with dissolve
    play music "music/hotshot.mp3"
    kil "Yo, Doctor [mcl]!"
    scene pr0045 with dissolve
    mc "Huh...?"
    scene pr0046 with dissolve
    mc "Ian!"
    scene pr0047 with dissolve
    mc "What are you doing here?"
    scene pr0048 with dissolve
    kil "I work here, but {b}today{/b}..."
    kil "Well, I didn't want you to go into this thing alone."
    mct "(I thought he worked as a photographer...?)"
    scene pr0047 with dissolve
    mc "... and just why shouldn't I go into this thing alone?"
    scene pr0048 with dissolve
    kil "Don't worry, figure of speech. This place is fucking awesome. I just know how you hate surprises."
    kil "Plus it'll be handy to have someone around to help remove that stick from your ass."
    kil "C'mon, let's head on up. I'll fill you in on the way."
    stop ambient fadeout 3.0
    scene black with blinds
    play sound "sound effects/elevator-bell.wav"
    kil "So, how much did the old bastard tell you exactly?"
    scene pr0049 with dissolve
    mc "Dr. Chuck?"
    mc "Next to nothing. He said this place is a lounge?"
    kil "That is {b}one{/b} way to paint the picture I suppose, but if you wanted to cut through the bullshit..."
    kil "Well, there's no way around this one: this place is a... brothel?"
    kil "Sex club...? Y'know, it's actually hard to categorize when you start splitting hairs."
    mc "A brothel? {b}Fuck{/b} off with your stupid jokes."
    kil "You don't believe me?"
    mc "No, of course not. You're busting my balls."
    kil "Fine, if you don't want to believe me, just don't say I didn't give you a heads up."
    play sound "sound effects/elevator-bell.wav"
    "{b}*Ding!*{/b}"
    scene black with dissolve

# Meeting Jacob ----------------------------------------------------------------

    scene pr0050 with dissolve
    "After ascending the next two floors on foot, we emerged into a room very unlike the sterile, office-like environment that preceded it. "
    scene pr0051 with dissolve
    kil "Jacob!"
    scene pr0052 with dissolve
    kil "This is my friend [mcf]. He's who you're expecting."
    kil "[mcf], this is Jacob. He's one of two bouncers here. You'll come to note he's the handsome and likable one."
    scene pr0053 with dissolve
    jacob "You have a friend outside the club that {b}doesn't{/b} have a set of long legs and a pair of breasts?"
    scene pr0054 with dissolve
    kil "We go way back. All the way back to elementary school."
    scene pr0203 with dissolve
    jacob "Is that so? Well, it's good to meet you, [mcf]."
    mc "Likewise, Jacob. It's good to meet you too."
    scene pr0054 with dissolve
    kil "Is it cool to head on in?"
    scene pr0055 with dissolve
    jacob "Be my guest. Boss is behind the bar."
    scene pr0053 with dissolve
    kil "C'mon, let's go."
    stop music fadeout 3.0

# Meeting August and Kathleen---------------------------------------------------

    hide screen textbox2 with dissolve
    scene black with dissolve
    $ renpy.pause(2, hard=True)
    scene pr0056 with dissolve
    $ renpy.pause(1.5, hard=True)
    scene pr0057 with dissolve
    play music "music/as-i-figure.mp3"
    show screen textbox2 with dissolve
    kil "Look at what the cat dragged in!"
    scene pr0058 with dissolve
    bar "That's my line, kid."
    scene pr0059 with squares
    woman "Whose your handsome friend, Ian?"
    scene pr0057 with dissolve
    kil "He's the guy my uncle mentioned, Let me introduce you two to..."
    hide screen textbox2 with dissolve

    menu:
        "Let Ian finish. [gr]\[Killian +1\] [red]\[Toughness -1\]":
            $ toughness -= 1
            $ toughness = clamp(toughness, 0, 30)
            $ Killian_Bromance += 1
            $ Killian_Bromance = clamp(Killian_Bromance, 0, 40)
            show screen textbox2 with dissolve
            scene pr0060 with dissolve
            kil "...to [mcf]. You might not believe it, but I actually owe a lot of who I am today to him."
            mct "(Considering his {i}personality{/i}, is that supposed to be a ringing endorsement...? Still, he's clearly doing his best to sell me.)"
            mct "(Thanks, Ian.)"


        "Interrupt Ian and introduce yourself. [gr]\[Toughness +1\] [red]\[Killian -1\]":
            $ toughness += 1
            $ toughness = clamp(toughness, 0, 30)
            $ Killian_Bromance -= 1
            $ Killian_Bromance = clamp(Killian_Bromance, 0, 40)
            show screen textbox2 with dissolve
            scene pr0061 with dissolve
            mc "...[mcf] [mcl]. Thank you for seeing me."

    scene pr0062 with dissolve
    bar "Nice to meet you, [mcf]. I'm August Byrnes, manager and part proprietor of the Carnation Club."
    show pr0063 with wipeleft
    aug "This vision of loveliness is Kathleen Pulman. She also owns a stake in the club, as well as managing our entertainment and headhunting needs."
    scene pr0064 with dissolve
    kat "My, you're certainly easy on the eyes."
    kat "It's nice to get a fresh, young face around here. Ian excluded, all a girl can get in this place for eye-candy are old men."
    scene pr0063 with dissolve
    hide screen textbox2 with dissolve

    menu katflirt01:

        "{color=#FF1493}\[Social Butterfly]{/color} Flirt with her. [gr]\[Kathleen +1\]" if perk_socialButterfly == True:
            $ Kathleen_Affection += 1
            $ Kathleen_Affection = clamp(Kathleen_Affection, 0, 30)
            show screen textbox2 with dissolve
            scene pr0065 with dissolve
            mc "If a beautiful woman like yourself is hitting on me, it really must be that bad."
            scene pr0067 with dissolve
            kat "Hmm, I like you. You want to know what the first thing Ian said to me was?"
            kat "He said... {i}you got a great ass, for an old lady{/i}."
            scene pr0068 with dissolve
            kat "Can you believe that?"
            scene pr0066 with dissolve
            mc "Uh, yeah I unfortunately can."
            scene pr0069 with dissolve
            kil "Come on! Are you ever going to let that go? I said I was sorry. You know, in my defense..."
            scene pr0070 with dissolve
            kil "Eh... You know what? Never mind."
            kil "I'll stop before I put my foot in my mouth."


        "{color=#696969}\[Social Butterfly] Flirt with her.{/color}" if perk_socialChameleon == True or perk_strongman == True:
            jump katflirt01

        "Move on to why you're here.":
            show screen textbox2 with dissolve
            mc "Pleased to meet you."

    scene black with dissolve
    $ renpy.pause(1.5, hard=True)
    scene pr0071 with blinds
    "After a few minutes of friendly chatter, I arrived at the perfect opportunity to finally broach the question that's been burning in my mind."
    "After all, even if I didn't believe what Ian told me in the elevator, there was still a nasty seed planted in the back of my mind that he could actually be serious for once."
    mct "(Dr. Chuck had been suspiciously sparse with the details on this place...)"
    mc "You've got a nice place here, it seems pretty upscale. So, do you cater to businessmen or...?"
    scene pr0072 with dissolve
    aug "..."
    scene pr0204 with dissolve
    aug "Pfft, hahaha!"
    aug "Chuck had you walk in here for a meeting without even filling you in on the place, didn't he?"
    aug "Yep, that's definitely his idea of a joke!"
    scene pr0072 with dissolve
    aug "Still, Killian didn't blow the lid off this place? That I can't believe, with his 100 mile per hour mouth."
    mc "...well, he had some peculiar things to say, but he makes bad jokes all the time."
    scene pr0076 with dissolve
    kat "What did Ian tell you?"
    mc "He said this place was a brothel."
    scene pr0077 with dissolve
    "As I watched the man behind the bar pause for a moment to carefully consider his reply, my mind turned over on itself and began to entertain the outrageous possibility that Ian wasn't bullshitting me."
    scene pr0078 with dissolve
    aug "You know, I prefer the term {b}gentleman's lounge{/b} myself. Brothel has crass connotations, while the Carnation Club is {b}MUCH{/b} more than a simple cathouse."
    scene pr0075 with dissolve
    mc "........."
    mc "......"
    mc "..."
    stop music
    play sound "sound effects/breaking-glass.wav"
    scene pr0074 with hpunch
    mc "...huh?"
    mct "(Everyone is in on the joke, right...? That's has to be it.)"
    "An awkward silence fell over the room as I waited for the punchline that wasn't coming."
    "As the silence grew thicker, I recalled my mother's vague mistrust of Dr. Chuck last night, and suddenly, it seemed more and more valid."
    mc "You can't be..."
    scene pr0073 with dissolve
    play music "music/as-i-figure.mp3"
    aug "Serious as a heart attack."
    scene pr0071 with dissolve
    kat "{i}*sigh*{/i} Charles REALLY should've mention it to the boy, don't you think?"
    kil "It was necessary to get him in the door."
    "My brain immediately entered into a tug-o-war between being angry and finding the whole situation absurdly amusing."
    mct "(So that means Dr. Chuck, the mentor I've known for years, is some kind of... {b}pimp{/b}?)"
    "It's so outrageous, that it bordered on hilarious."
    scene pr0073 with dissolve
    aug "I can see on your face that you're already half way out the door."
    aug "Let me ask you this, is it the legality of our business that's giving you cold feet?"
    aug "There's no getting around it: the Morehead Hills Police Department doesn't look too kindly on the trade."
    scene pr0204 with dissolve
    aug "Luckily, we count the chief of police as one of our most senior members! Gufawhaha!"
    "All I could really do is stare at the old man, dumb-founded as he laughed at some imagined joke."
    scene pr0072 with dissolve
    aug "Let me put your fears to rest, kid. You don't have to worry. Working here won't {i}ever{/i} bring you any heat."
    aug "We're well-connected for one and otherwise well-insulated from the outside world."
    aug "This isn't a back-alley massage parlor or a tweaker tricking out his girlfriend in a motel room."
    aug "We've been up and running for nearly four years without a hint of the pigs sniffing around the place. I work hard to keep it that way."
    scene pr1993 with dissolve
    mc "...good for you, I guess?"
    scene pr1998 with dissolve
    "My brain was too busy looking for a way to eject myself from the situation than to process and tactfully respond to the bullshit the old man behind the counter was spewing."
    "In what world is that a convincing argument?"
    kat "{i}*sigh*{/i} No, he DEFINITELY should have told him. I think you've overwhelmed the poor boy."
    scene pr1995 with dissolve
    kil "C'mon, lighten up. I've been working here for a while now and this place is great."
    kil "Besides, I asked a favor of my uncle for this. At least hear about the job itself and what you'll get paid."
    scene pr1996 with dissolve
    mc "Um... yeah, no. Thanks, but {b}no thanks{/b}."
    mc "I've got my future to think of and getting wrapped up in something like this is out of the question."
    scene pr1997 with dissolve
    kil "That is EXACTLY why I want to get you in on this, dude. You and I aren't on the same wave-length anymore, but we could be."
    scene pr1996 with dissolve
    mc "...sorry, Ian. I can't. I should go."
    scene pr0073 with dissolve
    aug "I respect your decision. A man your age being careful about his future is admirable, but come back anytime if you change your mind."
    scene pr1994 with dissolve
    mc "I don't think I will."
    mc "I better leave now. I'm sorry to have wasted your time."
    scene pr0078 with dissolve
    aug "You'll see him out, Killian?"
    scene black with dissolve
    stop music fadeout 1.0
    "....."
    play music "music/leaving-home.mp3"
    "..."
    $ renpy.pause(1.5, hard=True)
    scene pr0079 with blinds
    kat "Hmm... what do you think, Augie?"
    kat "Why did Charles send a boy like that to us?"
    scene pr0080 with dissolve
    kat "It's almost the most lucrative time of the year for our little game."
    scene pr0081 with dissolve
    kat "Darius, that fucking idiot..."
    kat "Being down a man this close to the exhibition is unacceptable."
    scene pr0078 with dissolve
    aug "What I think is... the boy has potential."
    aug "Chuck knows the boy rather well and if he says he'll be a good fit, I trust his judgment."
    scene pr0077 with dissolve
    kat "You have a few others vetted just in case he still refuses, I hope."
    aug "..."
    scene pr0078 with dissolve
    aug "Don't worry about that, Kat. He'll be back."

    scene black with dissolve
    stop music fadeout 2.0
    play sound "sound effects/notification.wav"
    $ met_august = True
    $ met_jacob = True
    $ met_kathleen = True
    show bioadd with dissolve
    $ renpy.pause(3, hard=True)
    "......"
    "..."

    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionveronica03 with blinds
    $ renpy.pause(6, hard=True)

# May 08 Call with Dr. Chuck ---------------------------------------------------
    stop sound
    scene player-room with blinds
    play music "music/crinoline-dreams.mp3"
    show screen textbox2 with dissolve
    show screen qmenu with dissolve
    $ date = "may08night"
    show may08night with squares
    "To take my mind off of trying to make sense of today, I decided to focus my concentration on something else that didn't make a lick of sense to me: my impending Waves and Oscillation final."
    "Or at least I tried to."
    hide may08night with blinds
    play sound "sound effects/ringing-inbound.wav"
    "{b}*Ring, ring.*{/b}"

    "The face of my phone lit up, revealing to me that it was Dr. Chuck."
    mct "(What the hell do I even say to him?)"

    scene player-room blur
    show chuck-call

    play sound "sound effects/phonemenu.wav"
    "{i}*Beep*{/i}."
    mc "Hello."
    chuck "[mcf]. Glad you picked up."
    chuck "I hope you don't mind the impromptu call. Ian told me you weren't sold on working for the Carnation Club."
    mct "(Is... is he fucking serious? Did he really think I would be?)"
    mc "It's more like I can't even comprehend anything that happened today."
    mc "For one, you made a fortune making spaceplane parts, didn't you?"
    chuck "That I did, lad. This is more like a... hobby. A side business to wile away the days of my retirement."
    mct "(Is he hearing himself right now? Running a brothel as a hobby...?)"
    mc "Well, whatever. That's not important. The simple fact is that I'm not interested."
    mc "I have my future to consider and that is that."
    chuck "Ah, you see lad, your future is precisely why I thought you would be a good fit for the job in the first place, but you got so spooked that August never had the chance to explain the finer details."

    if chuck_polite == True:
        mc "I don't really want to hear it, sir. I have the MCATs and admission interviews next year."
    else:
        mc "I don't really need to hear them. I have the MCATs and admission interviews next year."

    chuck "You see, {b}that{/b} is one of the finer details I'd like to discuss with you."
    chuck "The Carnation Club isn't some den of iniquity. It's a fraternity."
    mc "It doesn't matter what you call it."
    chuck "Don't be so sure. What does a fraternity usually offer besides camaraderie and a sense of brotherhood?"
    "Without giving me a chance to even parse if that was meant to be rhetorical, Dr. Chuck continued on with his spiel."
    chuck "Networking. {b}Connections{/b}."
    chuck "Some of the most wealthy and influential of Morehead Hills and the surrounding tri-state area are among the club's member base. If you're looking to get into your first school of choice, it could likely be secured thanks to the club's connections."
    mc "Yeah, right."
    chuck "It's true! I promise!"
    chuck "You know how the world works. It's all about who you know, and with the club, you'll find yourself knowing a lot more people."
    "Is he telling me that if I work for that shady old man, I could schmooze my way all the way up to a good fellowship?"
    chuck "That's not to mention, on top of a pretty good working wage, for every semester you work at the club, I will see to it that your tuition is taken care of."
    stop music fadeout 1.0
    mc "..."
    play music "music/leaving-home.mp3"
    mc "...let me get this straight: you're offering to pay my way through school?"
    chuck "That's right."
    mc "...and what could I possibly do at the club that would make it worth all that money?"
    chuck "You'll be working under Kathleen during the summer exhibition, but year-round, you'll mostly be a pair of extra hands. Running errands, moving things, that kind of work."
    mc "Summer exhibition?"
    chuck "That's right. I can explain the details more later, but the gist is you'll be looking out for the performers well being during the event."
    chuck "Boosting morale, making sure they're safe, and keeping them fighting fit. It's a pretty good gig if I say so myself, lad."
    mc "...the value of that couldn't possibly justify paying my tuition."
    chuck "Weren't listening when I said it's about who you know? Having someone with a bright future like yourself as a member will bring the club both tangible and intagible benefits in the long run."
    chuck "Plus, I like you and we go way back."
    chuck "I made a private fortune during my time as an engineer, more than a man with my modest tastes could possibly spend, so I jump at the chance to spread it around to those I consider worthwhile."
    chuck "Putting a lad like you through school, I'd say that's worthwhile."
    mc "Listen, I'll admit that doesn't sound bad, but..."
    mct "(In fact, if what he's offering me is true, it's UNBELIEVABLY AMAZING.)"
    mct "(I'd be a fucking idiot for turning it down. The leg up I'd have from not going into student debt would be tremendous...)"
    chuck "I'll tell you what."
    chuck "Come to the club tomorrow at 8pm. You'll meet a charming lady who I suspect you'll enjoy working alongside."
    chuck "If you go there and it doesn't change your mind, I understand."
    mc "..."
    mc "Okay, fine, but tell me one thing."
    chuck "What is it, lad?"
    mc "Why consider me for this in the first place?"
    chuck "Honestly, it's my nephew. Having no children of my own, I have a soft-spot for Ian and he asked me to hire you."
    chuck "It's that simple."
    mc  "...I'll go. You said 8 PM, right?"
    chuck "Glad to hear it! You won't regret it in the least."
    "......"
    stop music fadeout 3.0
    scene black
    "..."

    scene pr0040 with blinds
    play sound "sound effects/shower.wav"
    mct "(It all comes down to Ian, huh?)"
    mct "(After dragging him into all kinds of trouble when we were kids, it seems we've flipped our dynamic on its head.)"
    "..."
    hide screen textbox2

## May 08 Mom Text -------------------------------------------------------------

    scene black with dissolve
    play music "music/lobby-time.mp3"
    play sound "sound effects/sms-chime.wav"

    scene player-room-dark blur with dissolve
    call phone_start_vic from _call_phone_start_vic
    call message_start("Mom", "Hey, hun! I haven't heard from you all day.") from _call_message_start_6
    call message("Mom", "How did your interview go?") from _call_message_10

    call screen phone_reply("It went okay.","wentokay","Deflect.","deflect")

label wentokay:

    call phone_after_menu from _call_phone_after_menu_2
    call message_start("[mcf]", "I have the job if I want it, but I'm not sure if it's a good fit for me.") from _call_message_start_7
    call message("Mom", "That's okay! You should do what you feel most comfortable with.") from _call_message_11
    call message("Mom", "You should know I'm proud of you no matter what direction you decide to go in life.") from _call_message_12
    call message("Mom", "I couldn't ask for a better son.") from _call_message_13
    call reply_message("Thanks mom, but you're laying it on pretty thick.") from _call_reply_message_4
    call message("Mom", "That's my job!") from _call_message_14
    call message("Mom", "Have a good night, sweetie.") from _call_message_15
    jump vicaftertext01

label deflect:

    call phone_after_menu from _call_phone_after_menu_3
    call message_start("[mcf]", "I don't want to talk about it.") from _call_message_start_8
    call message("Mom", "That bad?") from _call_message_16
    call message("Mom", "You shouldn't let it get you down.") from _call_message_17
    call message("Mom", "You should know I'm proud of you no matter what.") from _call_message_18
    call message("Mom", "I couldn't ask for a better son.") from _call_message_19
    call reply_message("Thanks mom, but you're laying it on pretty thick, don't you think?") from _call_reply_message_5
    call message("Mom", "Maaaaaybe. ;)") from _call_message_20
    call message ("Mom", "Have a good night, sweetie.") from _call_message_21
    jump vicaftertext01

label vicaftertext01:

    call phone_end_vic from _call_phone_end_vic
    scene player-room-dark with dissolve
    show screen textbox2 with dissolve
    "........."
    scene black with dissolve
    "......"
    stop music fadeout 3.0
    "..."

    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionrosalind01 with blinds

    $ renpy.pause(6, hard=True)

label may09start:

#------------------------------------------------------------------------------#
#                                   May 09                                     #
#------------------------------------------------------------------------------#

    $ date = "may09night"
    stop sound
    play ambient "sound effects/city-night.wav"
    scene pr0082 with blinds
    show may09night with squares
    show screen textbox2 with dissolve
    show screen qmenu with dissolve
    "The next night."
    scene club-fr-night2 blur
    hide screen textbox2
    scene club-fr-night2
    call phone_start_chuck from _call_phone_start_chuck

# May 09 Text with Dr. Chuck ---------------------------------------------------

    play music "music/i-knew-a-guy.mp3"
    call screen phone_reply("I'm here.","arrivalnormal","Now what?","arrivalcurt")

label arrivalnormal:
    call phone_after_menu from _call_phone_after_menu_4
    call message_start("[mcf]", "I'm here.") from _call_message_start_9
    call message("Dr. Kohler", "Excellent. Head up to the bar.") from _call_message_22
    call message("Dr. Kohler", "I'll honor whatever decision you come to regarding the lass. Talk to you later.") from _call_message_23
    jump rosalindintro

label arrivalcurt:
    call phone_after_menu from _call_phone_after_menu_5
    call message_start("[mcf]", "I'm outside. Now what?") from _call_message_start_10
    call message("Dr. Kohler", "Just head on in.") from _call_message_24
    call message("Dr. Kohler", "I'll honor whatever decision you come to regarding the lass. Talk to you later.") from _call_message_25
    jump rosalindintro



label rosalindintro:

    call phone_end_chuck from _call_phone_end_chuck
    show screen textbox2 with dissolve
    mct "(What the hell does that mean?)"

# Meeting Warren and Rose -----------------------------------------------------
    stop ambient fadeout 3.0
    scene club-door with fade
    "With no Ian or Jacob to usher me in, the trek up to the bar was an eerily quiet one."
    show pr0084 with wipeleft
    "Inside the bar, waited two bodies. One, an intimidatingly large man and the other a woman sitting quietly on a sofa near the entrance."
    "The man I recognized from yesterday's visit, though we were never introduced."
    scene pr0085 with dissolve
    "The woman..."
    scene pr0086 with dissolve
    "Was a beautiful, new face."
    scene pr0088 with dissolve
    man "Hiya, kid."
    man "You ran out of here so fast yesterday that I didn't get the chance to say hello."
    scene pr0089 with dissolve
    man "The name is Warren."
    war "I'm in charge of security around here."
    hide screen textbox2 with dissolve
    scene pr0090 with dissolve

    menu:
        "Return his greeting.":
            show screen textbox2 with dissolve
            mc "[mcf]. Nice to meet you."

        "Shake his hand. [gr]\[Warren +1\]":
            $ Warren_Friendship += 1
            $ Warren_Friendship = clamp(Warren_Friendship, 0, 10)
            show screen textbox2 with dissolve
            scene pr0091 with fade
            mc "[mcf]."


    scene pr0092 with dissolve

    war "Well, now that you're arrived, I can finally get the fuck out of here."
    "Warren abruptly began to leave."
    war "You'll have the run of the place for the next couple of hours."
    war "The {b}good{/b} alcohol is below the bar."
    stop music fadeout 3.0
    war "Don't do anything I wouldn't do! Hahahaha!"

    scene pr0093 with dissolve
    mc "Wait, what do you...?"

    scene pr0094 with dissolve
    mc "..."


    scene pr0095 with dissolve

    "As I turned to face the only other occupant in the bar, unable to make heads nor tails of what's going on, the woman timidly greeted me with a faint smile."
    "She seemed nervous, not knowing if she should be the one to break the silence."
    "After a few awkward seconds that felt like it spanned a lifetime, one of us finally yielded."

    scene pr0096 with dissolve
    play music "music/george-street-shuffle.mp3"
    woman "You're Mr. [mcl], right? I didn't expect you to be so young..."
    woman "Oh! I'm sorry if that came across as rude..."
    "She knows my name it seems."
    "I, on the other hand, haven't the faintest clue who she is."
    mc "I'm sorry, but who are you...?"
    scene pr0097 with dissolve
    woman "Oh! Sorry..."
    scene pr0098 with fade
    woman "I'm Rosalind Carter, but everyone calls me Rose."
    hide screen textbox2 with dissolve
    scene pr0099 with dissolve

    menu:
        "Compliment her name. [gr]\[Rosalind +1\]":
            $ Rosalind_Affection += 1
            $ Rosalind_Affection = clamp(Rosalind_Affection, 0, 40)
            show screen textbox2 with dissolve
            mc "Rosalind. I like that name, it's very pretty."
            scene pr0098 with dissolve
            rose "Thank you."
        "Move on.":
            show screen textbox2 with dissolve
            pass

    scene pr0101 with dissolve
    rose "So..."
    rose"Should we... begin?"
    mc "Begin what?"
    rose "My interview."
    rose "Do you want to talk first or should I just..."
    stop music
    play sound "sound effects/record-scratch.wav"
    rose "Undress?"
    mc "Huh...?"
    scene pr0102 with dissolve
    mc "What? {b}N-no!{/b}"
    scene pr0100 with dissolve
    "At my emphatic rejection to her offer, the color seemed to drain from her face and a sense of worry took its place."
    mct "(Damn it, this whole thing suddenly makes a lot of sense.)"
    scene pr0101 with dissolve
    rose "Did I do something wrong? I'm sorry if I..."
    mc "Not wrong. It's more like I wasn't expecting you to suddenly offer to take your clothes off."
    mc "To be honest, I didn't know what to expect tonight or even who I was meeting."
    scene pr0101
    rose "...you weren't told to expect me?"
    mc "No, not exactly."
    mc "How about we sit and have a friendly conversation, okay?"
    scene pr0100
    rose "Alright..."

    scene pr0103 with fade
    play music "music/george-street-shuffle.mp3"
    mc "Let's start from the beginning. Why do you think you're here?"

    scene pr0104 with dissolve

    rose "To interview for the club."
    rose "Specifically, I was told to meet a Mr. [mcl] - uh, you right? - and have sex with you."
    mc "...and who told you to do that?"

    scene pr0105 with dissolve
    rose "It was someone your age, his name was..."

    mc "...Killian?"

    scene pr0106 with dissolve
    rose "Yeah, that's it!"

    scene pr0104 with dissolve
    rose "Mrs. Pulman, the lady at the Eden Women's Fund, introduced me to him a month ago."
    rose "I was afraid that he was stringing me along, that this whole deal was a trick... but then he sent me this address and told me to 'convince' you of my qualifications."

    scene pr0107 with dissolve
    rose "That you would decide if I was... a good fit for this place."

    scene pr0104 with dissolve
    rose "... but you don't know anything about this?"

    scene pr0103 with dissolve
    "I suppose some transparency on my end is fair."
    mc "Not a thing, I only just had an interview here yesterday myself, but I left with no intention of working here."

    scene pr0107 with dissolve
    rose "So, you don't work for Mrs. Pulman then?"

    scene pr0103 with dissolve
    mc "No, I only recently met her myself through Killian. He's a..."
    hide screen textbox2 with dissolve

    menu:
        "Good friend of mine. [gr]\[Killian +1\] [red]\[Rosalind -1\]":
            $ Rosalind_Affection -= 1
            $ Rosalind_Affection = clamp(Rosalind_Affection, 0, 40)
            $ Killian_Bromance += 1
            $ Killian_Bromance = clamp(Killian_Bromance, 0, 40)
            show screen textbox2 with dissolve
            mc "A good friend of mine."


        "An acquaintance of mine. [red]\[Killian -1\]":
            $ Killian_Bromance -= 1
            $ Killian_Bromance = clamp(Killian_Bromance, 0, 40)
            show screen textbox2 with dissolve
            mc "Someone I used to go to school with."

    mc "Anyway, this is just a hunch, but I think you're being used to give me a taste for this place in addition to your interview."
    scene pr0108 with dissolve
    rose "...a taste?"

    scene pr0107 with dissolve
    rose "..."
    rose "...but what about me? I really {b}need{/b} this chance."

    scene pr0110 with dissolve
    "I could tell by the plaintive tone of her voice that joining the club must be important to her."
    "I recalled Dr. Chuck saying he'd honor my decision tonight. At the time that was indecipherable, but now it's clear what he meant."
    "It's up to me if this woman can join the club or not."
    mct "(I have no reason to deny her, but...)"
    "Just a quick glance over at the womanly curvature of Rosalind's body kindled a strong feeling of desire, but coupled with the ease of conquest presenting itself, spun that into a devious, actionable thought."
    mct "(She DID come here expecting as much, so there's no harm in taking advantage of the situation and having a little fun, right?)"
    stop music fadeout 2.0
    hide screen textbox2 with dissolve

    menu:
        "Take advantage of her. [gr]\[Toughness +5\] [red]\[Rosalind -10\]":
            $ toughness += 5
            $ toughness = clamp(toughness, 0, 30)
            $ Rosalind_Affection -= 10
            $ Rosalind_Affection = clamp(Rosalind_Affection, 0, 40)
            $ roseTakeAdvantage = True
            show screen textbox2 with dissolve
            jump rosetakeadvantage

        "Tell her she can join. [gr]\[Rosalind +5\] [red]\[Toughness -2\]":
            $ toughness -= 2
            $ toughness = clamp(toughness, 0, 30)
            $ Rosalind_Affection += 5
            $ Rosalind_Affection = clamp(Rosalind_Affection, 0, 40)
            show screen textbox2 with dissolve
            jump rosebenice


label rosetakeadvantage:

    if _in_replay:
        show transitionrosalind01 with cmet
        show screen textbox2 with dissolve
        "Please set [mcf]'s personality (toughness score) for this replay."
        hide screen textbox2 with dissolve
        menu:
            "Nice guy (Toughness: 0)":
                $ toughness = 0
            "Mischevious (Toughness: 18)":
                $ toughness = 18
            "Asshole (Toughness: 30)":
                $ toughness = 30

        scene black with fade
        show screen textbox2 with dissolve


    play music "music/leaving-home.mp3"
    "It's not everyday that a beautiful woman just falls into your lap."
    scene pr0111 with dissolve
    mc "Why don't we get started on the interview?"
    scene pr0112 with dissolve
    "Rosalind tensed up in my hands, no doubt sensing the sudden change in my demeanor."
    "Honestly, even part of me couldn't believe that I could slip into a predatory role so easily."

    scene pr0113

    rose "O-okay..."
    hide screen textbox2 with dissolve

    menu rosetakeadvantagemenu:

        "{color=#FF1493}\[Governor]{/color} That's 'Yes, Sir.'" if trait_governor == True and prYesSir == False:
            $ rosePN = "Sir"
            $ prYesSir = True
            show screen textbox2 with dissolve
            scene pr0112 with dissolve
            mc "From here on out, if you want to make a good impression, it's {i}Yes, sir{/i}."
            rose "..."
            scene pr0114 with dissolve
            rose "Yes... [rosePN]"
            scene pr0115
            hide screen textbox2 with dissolve
            jump rosetakeadvantagemenu

        "Tell her to undress.":
            show screen textbox2 with dissolve
            jump roseTAundress

        "[gr]Kiss her.":
            show screen textbox2 with dissolve
            jump RoseTAkiss

        "{color=#696969}\[Governor] That's 'Yes, Sir.'{/color}" if trait_governor == False:
            jump rosetakeadvantagemenu

label RoseTAkiss:
    $ Rosalind_Libido += 1
    $ Rosalind_Libido = clamp(Rosalind_Libido, 0, 20)
    scene pr0116 with fade
    "Before I could let my usual inhibitions get in the way of the fun, I pressed on."
    play sound "sound effects/kiss1.wav"
    rose "mmh...!"
    "At first it was awkward, a mismatch of my own enthusiasm and Rosalind's surprise at the sudden assault on her mouth."
    scene pr0117 with dissolve
    play sound "sound effects/kiss1.wav"
    rose "mmwa...!"
    "... but soon, she relaxed and was reciprocating in return, gradually falling into a pleasant rhythm as things started getting heated."
    scene black with fade
    "Minutes later, Rosalind had proven surprisingly receptive to my ministrations as all tension seemed to evaporate and I felt her body go slack in my arms."
    scene pr0118 with dissolve
    rose "Ha... ha..."
    "It was finally time to move things along."

    $ prRoseTAkiss = True
    jump roseTAundress

label roseTAundress:

    mc "I want you to slowly slide off the dress. Okay?"
    if prYesSir == True:
        "Rosalind took a few seconds to carefully process what I had asked of her, before finally answering..."

        if prRoseTAkiss == True:
            scene pr0120 with fade
            rose "Yes, [rosePN]..."

        else:
            scene pr0119 with fade
            rose "Yes, [rosePN]..."

    else:
        if prRoseTAkiss == True:
            "Rosalind took a few seconds to carefully process what I had asked of her, before wordlessly setting off on the task."
            scene pr0120 with fade
        else:
            "Rosalind took a few seconds to carefully process what I had asked of her, before wordlessly setting off on the task."
            scene pr0119 with fade



    scene pr0121 with dissolve
    "..."
    scene pr0122 with dissolve
    "Without any sense of theatrics, she quickly slipped out of her dress."

    scene pr0123 with dissolve
    mct "(...!)" with vpunch
    "As she turned to face me, it felt like someone had kicked me straight in the gut."
    "I could barely stop myself from sputtering, my breath catching in my throat as I took in the salacious curves and bends of the woman in front of me."
    "Large breasts resting a top a slender frame, with an invitingly pleasant, plump softness that extended from her waist to her hips."
    "I don't know how long I spent drinking in her near-nude form, but by the time I had been pulled from my reverie, Rosalind wore an uncomfortable expression practically begging to move things along."

    mc "Alright. Put your hands behind you back and stand up straight."

    if prYesSir == True:
        rose "Yes... [rosePN]."

    scene pr0124 with dissolve

    "It felt like magic. I had told her what to do and she had complied in spite of clear, burning embarrassment and clear reticence."
    "Seeing her there, almost fully exposed with nothing but a small cotton cloth to cover her modesty, stoked a sadistic fire in the pit of my stomach."


    if toughness <= 19:
        "Despite this, a part of me couldn't help but feel guilty and pathetic at taking advantage of the situation, but it's what she came here to do, right?"
        "Regardless, the sight of her ample breasts and near flawless alabaster skin was truly a sight to behold."

    else:
        "Any guilt or personal smallness I felt at taking advantage of the situation melted away in lieu of the sight of her ample breasts and near flawless alabastar skin."
        "She truly was a a sight to behold."

    hide screen textbox2 with dissolve

    menu:
        "Tell her she's beautiful.":
            show screen textbox2 with dissolve
            mc "You're incredible, downright beautiful."
            "Without really thinking, I shared my honest thoughts."
            "Naturally, given the situation, the words played less like a genuine compliment and more like the utterance of a creep."
            scene pr0125 with dissolve
            rose "Uh, thanks... I guess."
            scene pr0127 with dissolve

        "Let the moment pass.":
            show screen textbox2 with dissolve
            pass


label roseTAmasturbation:


    "To be honest, a part from some blips - a year-long relationship and a couple of casual encounters Ian practically threw in my lap - my experience with the opposite sex has been quite narrow."
    "Wanting to make the most of it, a devilish idea formed in my head."
    scene pr0124 with dissolve
    mc "Why don't you put on a show for me."
    scene pr0151 with irisin
    mc "Use the edge of the table and try to get yourself off."
    scene pr0128 with dissolve
    rose "You want me to...?"
    scene pr0129 with dissolve
    "Her face turned a deep shade of crimson."
    scene pr0128 with dissolve
    rose "Wouldn't you rather just have... {i}sex{/i}?"
    scene pr0129 with dissolve
    "The request seemed to deeply embarrass her. In some sense, masturbating in front of someone feels more intimate than simply fucking them."
    "It was only natural for her to pull back at the request, which was what made it so fun."
    scene pr0130 with dissolve
    mc "If you can't do that, don't you think you're barking up the wrong tree interviewing for a place like this?"
    scene pr0131 with dissolve
    rose "..."
    scene black with fade
    rose "H-how do you want me?"
    rose "...like this?"
    scene pr0132 with dissolve
    "Rosalind started slow, at first giving a few tentative thrusts, before starting in earnest."
    scene pr0133 with fade
    "This carried on for a few minutes, the dispassionate gyrations of Rosalind's hips not eliciting even a trace of arousal on the woman's bare skin."
    "No surprise there. The whole situation is about as awkward as you'd expect."
    "You can't just tell someone to fuck a piece of furniture and expect them to be into it."
    mc "Shall I give you a hand getting into it?"
    scene pr0134 with fade
    scene pr0153 with dissolve
    rose "--!"
    scene pr0134 with dissolve
    "Roughly taking ahold of Rose's fat tits in the palms of my hands, I went about exploring their ample surface - kneading, pulling, and squeezing them to my heart's content."
    rose "Nwha~!"
    scene pr0153 with dissolve
    "The sudden attention had brought Rose's own efforts to a halt."
    scene pr0134 with dissolve
    mc "I didn't say stop masturbating, did I?"
    scene pr0135 with flash
    "To emphasize my point, I roughly gave her right nipple a fierce tug."
    scene pr0152 with dissolve
    rose "T-too rough!"
    "Despite her protest, the sudden shock seemed to jump start her back to the task, igniting a more passionate display."
    mc "Y'know... I had heard that larger breasts were less sensitive than smaller ones, but that doesn't seem true in your case, does it?"
    mc "In fact, it seems these obscene milkbags are your weak points!"
    play sound "sound effects/slap3.wav"
    scene pr0134 with flash
    sys "{b}*Whack*{/b}!"
    rose "--{b}ghaaa!{/b}"
    scene pr0153 with dissolve
    "Before long, I couldn't restrain myself."
    "Try as I might to belabor the fun, the novelty of the situation and the friction of Rose's soft back grinding against my cock was putting me dangerously close to a premature ending."
    scene black with dissolve
    play sound "sound effects/zipper.wav"
    "..."
    scene pr0136 with dissolve
    mc "Get a good whiff of the dick that's gonna shoot a load straight down your esophagus."
    play sound "sound effects/slap1.wav"
    scene pr0136 with flash
    "*{b}Thwap{/b}!"
    rose "...huh?"
    hide screen textbox2 with dissolve

    menu:
        "Encourage her.":
            show screen textbox2 with dissolve
            mc "Let's both enjoy ourselves now, okay?"
            if prYesSir == True:
                rose "Y-yes [rosePN]!"

            else:
                rose "Y-yes!"

        "Chastise her.":
            show screen textbox2 with dissolve
            mc "I'm going to shove my dick down your throat and you'd better not stop rubbing yourself against the table, okay?"
            "Rosalind silently nodded and opened her mouth."

    scene pr0138 with dissolve
    "Just getting the tip of my dick into the precipe of her mouth felt so heavenly that I thought I would immediately cum."
    scene pr0137 with dissolve
    "To avoid that embarrassment, I took my time, slowly working Rose's warm mouth across the surface of my dick."
    "Meanwhile, Roselind's own pleasured efforts grew more erratic in response."
    scene pr0138 with dissolve
    mc "...don't tell me you're actually getting off on this?"
    scene pr0137 with dissolve
    mc "I had my doubts, but you might actually be a good fit for a place like this."
    mc "Well if you aren't going to hold back, neither am I..."
    scene pr0139 with flash
    play ambient "sound effects/fel1.wav"
    "Feeling an insidious bout of cruelty swell in me, I finally let loose on Rose's poor throat, taking a firm grip on Rosalind's head."
    "I furiously pistoned my hips back and fourth, jackhammering the back of the submissive woman's throat with wild abandon."
    "For her part, she leaned into the treatment, doing her best to form a tight seal with her lips and cupping the underside of my penis with her tongue."
    mc "S-shit! This ain't your first rodeo, is it?"
    scene pr0140 with dissolve
    mc "You've done this before!"
    scene pr0139 with dissolve
    "The rough treatment continued for another couple of minutes, at a delirious rhythm, until finally..."
    scene pr0140 with dissolve
    mc "Ngg--"
    scene pr0139 with dissolve
    mc "Take!"
    scene pr0140 with dissolve
    mc "My!"
    scene pr0139 with dissolve
    mc "Load!"
    scene pr0140 with dissolve
    mc "You!"
    scene pr0139 with dissolve
    mc "Bitch!"

    hide screen textbox2 with dissolve
    menu:
        "Cum on her face":
            show screen textbox2 with dissolve
            scene pr0141b with flash
            stop ambient
            mc "-------!" with flash
            with flash
            play sound "sound effects/spurt.wav"
            with flash
            mc "......"
            play sound "sound effects/spurt.wav"
            with flash
            scene pr0141c with flash
            "..."
        "Cum down her throat":
            show screen textbox2 with dissolve
            scene pr0141 with flash
            stop ambient
            play sound "sound effects/spurt.wav"
            mc "-------!" with flash
            with flash
            play sound "sound effects/spurt.wav"
            with flash
            mc "......"
            play sound "sound effects/spurt.wav"
            with flash
            "..."
    scene black with fade
    "As soon as I had cum, it was like the black bile that had surged in me just moments before had been exorcised."
    "I felt like a real prick. I had no reason to take advantage of Rose other than my most base, disgusting urges."
    scene pr0142 with blinds
    stop music fadeout 3.0
    "Yet I had done it so easily."
    scene pr0143 with dissolve
    play music "music/called-upon.mp3"
    rose "Are... are you feeling okay?"
    "Suddenly, the previous object of my lust transformed from a thing into a real, breathing woman expressing concern for me."
    $ renpy.end_replay()
    if not persistent.RoseTAGallery:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.RoseTAGallery = True
    $ history_rosalind = "From what little I have to go off of, Rosalind is a woman down on her luck - a fact that I took advantage of the night I decided to work at the Carnation Club."

    hide screen textbox2 with dissolve

    menu:
        "Apologize. [gr]\[Rosalind +1\] \[RoseApology\] [red]\[Toughness -1\]":
            $ Rosalind_Affection += 1
            $ Rosalind_Affection = clamp(Rosalind_Affection, 0, 40)
            $ toughness -= 1
            $ toughness = clamp(toughness, 0, 30)
            $ roseTAapology = True
            show screen textbox2 with dissolve
            jump RoseTAapology

        "More than okay. [gr]\[Toughness +1\]":
            $ toughness += 1
            $ toughness = clamp(toughness, 0, 30)
            show screen textbox2 with dissolve
            jump RoseTAconclusion


label RoseTAapology:

    scene pr0145 with dissolve
    mc "I'm... sorry I made you do that."
    "Her expression was a complicated one, a seeming mixture of confusion, and oddly enough, consolation."
    scene pr0146 with dissolve
    rose "What are you, a child? Take what you want and then apologize for it?"
    scene pr0147 with dissolve
    rose "You didn't {b}make{/b} me do anything, sweetie. I came here and did what I wanted to do."
    rose "If anything, it's my damn husband I have to blame for all of this, but even then..."
    rose "I'm a grown woman."
    mct "(Husband...?)"
    scene pr0146 with dissolve
    "It's funny. Rose seemed different than I had seen up to this point."
    "She had taken on an almost motherly affectation."
    rose "So you'll tell Mrs. Pulman to let me join the summer exhibition?"
    mc "Exhibition...? Uh, yeah. Of course. Definitely."
    scene pr0147 with dissolve
    rose "Thank you. I'm gonna... go now, okay?"
    scene pr0148 with fade
    $ renpy.pause(1, hard=True)
    scene pr0149 with dissolve
    "........."
    "I guess she's got the job... and so do I."
    "Truth be told, in my heart, I had decided to take the job the moment he offered to pay for my tuition."
    "Then this happened, which was... fun."
    "......"

    jump clubacceptance


label RoseTAconclusion:

    mc "I'm better than okay. That was a blast."
    scene pr0150 with dissolve
    rose "...I'm glad you enjoyed it."
    rose "You'll keep your word? You'll tell whoever to let me join the summer exhibition?"
    scene pr0143 with dissolve
    mc "I will... I promise."
    scene pr0147 with dissolve
    rose "Thank you. I'm gonna... go now, okay?"
    scene pr0148 with fade
    $ renpy.pause(1, hard=True)
    scene pr0149 with dissolve
    "........."
    "I guess she's got the job... and so do I."
    "Truth be told, in my heart, I had decided to take the job the moment he offered to pay for my tuition."
    "Then this happened, which was... fun."
    mct "(If I take this job, maybe I'll get to let loose like this more often?)"
    "......"

    jump clubacceptance

label rosebenice:

    scene pr0154 with dissolve
    mc "I have no reason to deny you. You're in if you want to be."
    scene pr0155 with dissolve
    rose "Just like that? You don't want to..."
    rose "Have sex with me?"
    mc "{b}No{/b}, I don't. I mean, n-not because you're unattractive or anything, but because..."
    mc "It's just I don't want to take advantage of you."

    scene pr0155 with dissolve
    rose "......"
    rose "..."
    scene pr0157 with dissolve
    rose "Pfff! Hahaha!"
    mc "What?!"

    scene pr0158 with dissolve
    rose "S-sorry. That was just so earnest, that I couldn't help but laugh. Still..."

    scene pr0159 with dissolve
    play music "music/love-or-lust.mp3"
    rose "I wouldn't have minded. You're pretty cute, you know."
    mc "...why are you looking at me like that?"
    scene pr0160 with dissolve
    mc "What are you doing? I told you, you don't have to do--"
    rose "Shush. This isn't because of that."

    scene pr0161 with dissolve
    "Rosalind gently pressed her lips to mine."
    scene pr0162 with dissolve
    "Whatever thoughts I had whirling around in my head up to that point was melted by her gentle embrace."
    scene pr0163 with dissolve
    "I'm not sure how much time had passed, but as soon as our lips parted and the comfortable warmness gave way to a delicate longing, I knew it had not nearly been long enough."
    scene pr0164 with dissolve
    mc "W-what was that for?"
    scene pr0165 with dissolve
    sys "*Smwack!*"
    scene pr0166 with dissolve
    rose "For not being an asshole."
    scene black with dissolve
    "..."
    "Some time passed and we moved on to talking about ourselves, until the subject of what I was doing here came up."
    scene pr0167 with dissolve
    rose "I can see why you're conflicted. College isn't easy..."
    scene pr0168 with dissolve
    mc "To be honest, this whole thing feels unreal."
    scene pr0169 with dissolve
    mc "Just a few days ago I was worried about my finals and my crummy tutoring job, but I'm looking at working at a sex club."
    mc "With that kind of money, this would be a no-brainer for most people, but..."
    mc "The prospect of living outside the lines is terrifying."
    scene pr0170 with dissolve
    "I don't know what opened the floodgates, but something about the woman above me just made me want to keep on blathering."
    scene pr0172 with dissolve
    mc "See, I used to be a shitty kid. I caused a lot of worry and headaches for my poor mother."
    mc "The {i}make-her-cry{/i} kind of worry."
    "Rose's expression softened at the mention of my mom."
    scene pr0171 with dissolve
    rose "Tell me more."
    scene pr0172 with dissolve
    mc "Well, I eventually realized what a fuck-up I was and I decided to live as best as I could so I would never trouble her again."
    scene pr0173 with dissolve
    rose "You seem like a good son."
    rose "I will say, as I've recently learned, living outside the lines is sometimes unavoidable."
    rose "I don't think working at a place like this will make you a bad person, no more than I'm a bad person for being here."
    scene pr0174 with dissolve
    mc "If you don't mind me asking, why are you here?"
    scene pr0173 with dissolve
    rose "I have few options in my current predicament. Let's leave it at that."
    scene pr0175 with dissolve
    rose "Well, sweetie... it's been very weird, but I got to get home to my daughter."
    scene pr0176 with dissolve
    "The night had been pleasant, a slice separate from the usual daily anxieties. I was sad to see it end."
    mc "...it was nice meeting you, Rosalind."

    scene black with dissolve
    stop music fadeout 3.0
    "Truth be told, in my heart, I had decided to take the job the moment he offered to pay for my tuition."
    "...but it wouldn't be bad seeing more of Rose too."
    "......"
    $ history_rosalind = "From what little I have to go off of, Rosalind is a woman down on her luck. We shared a small moment together after I turned her down for sex."
    jump clubacceptance

label clubacceptance:
    "..."
    scene black with fade
    play ambient "sound effects/city-night.wav"
    "I guess I should let Dr. Chuck know I accept his offer."
    scene club-fr-night2 blur with dissolve
    play music "music/cold-sober.mp3" fadein 3.0
    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve

    call phone_start_chuck from _call_phone_start_chuck_1
    call screen phone_reply("I'm in.","acceptA","This is for real?","acceptB")

label acceptA:
    call phone_after_menu from _call_phone_after_menu_6
    call message_start("[mcf]", "I'll work at the club, so long as you're being honest about about the tuition.") from _call_message_start_11
    call message("Dr. Kohler", "I'm happy to hear that myself, but I can only imagine how ecstatic my nephew will be.") from _call_message_26
    call message("Dr. Kohler", "You've made a wise choice regarding your future.") from _call_message_27
    call message("Dr. Kohler", "I'll have Ian pass along the pertinent details. Good night, lad.") from _call_message_28
    call phone_end_chuck from _call_phone_end_chuck_1
    scene black with dissolve
    stop music fadeout 3.0
    stop ambient fadeout 3.0
    "I walked home and went to bed, all the while mulling over the day's events in my head."
    "Only time will tell if this ends up being a smart decision."
    jump may10start

label acceptB:
    call phone_after_menu from _call_phone_after_menu_7
    call message_start("[mcf]", "This is for real? You'll pay for my tuition?") from _call_message_start_12
    call message("Dr. Kohler", "Of course, lad. I pride myself in being a man of my word.") from _call_message_29
    call reply_message("Then I'll take the job.") from _call_reply_message_6
    call message("Dr. Kohler", "I'm happy to hear that myself, but I can only imagine how ecstatic my nephew will be.") from _call_message_30
    call message("Dr. Kohler", "You've made a wise choice regarding your future.") from _call_message_31
    call message("Dr. Kohler", "I'll have Ian pass along the pertinent details. Good night, lad.") from _call_message_32
    call phone_end_chuck from _call_phone_end_chuck_2
    scene black with dissolve
    stop music fadeout 3.0
    stop ambient fadeout 3.0
    "I walked home and went to bed, all the while mulling over the day's events in my head."
    "Time will only tell if this ends up being a smart decision."
    jump may10start



label may10start:

    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionrosalind02 with blinds
    $ renpy.pause(6, hard=True)


#------------------------------------------------------------------------------#
#                                   May 10                                     #
#------------------------------------------------------------------------------#
    stop sound
    $ date = "may10day"

    scene pr0177 with blinds
    show screen textbox2 with dissolve
    show screen qmenu with dissolve
    show may10day with squares
    "The next day, I met up with Killian to grab a cup of coffee before we went to the club."
    hide may10day with blinds
    play sound "sound effects/notification.wav"
    $ met_rosalind = True
    $ met_warren = True
    show bioadd with dissolve
    $ renpy.pause(3, hard=True)
    "..."
    scene pr0178 with fade
    play music "music/happy-boy-end-theme.mp3"
    "To my surprise, he wasn't alone."
    kil "Ey, Doctor!"
    scene pr0179 with dissolve
    kil "Have you met Mina before?"

    "As I understood it, Mina was Ian's girlfriend - or at least as much of a girlfriend a man like my womanizing friend here can have."
    mct "(She has my deepest sympathies...)"


    if perk_socialButterfly == True:
        mc "You've spoken of her, but I haven't had the pleasure."
    else:
        mc "You've mentioned her a few times, but we haven't met."

    mc "Nice to meet you, Mina."
    scene pr0180 with dissolve
    mina "Oh? Ian talks about me?"
    "There was a sarcastic, flippant edge to her words. It's just a hunch, but I suppose she must be none too happy with Ian today."
    scene pr0181 with dissolve
    mina "It seems we have that in common! I feel like I practically know you already!"
    "On a dime, Mina shifted to a previously unseen bubbliness - one that came across so genuine and authentic that it crossed all the way back into phony."
    mina "He never misses a chance to talk my ear off with stories of the crazy stuff you guys used to get up to."
    scene pr0182 with dissolve
    mina "It's so finally good to meet you!"
    scene pr0183 with dissolve
    "Mina proceeded to hurl herself at me with unrestrained warmth, squeaking out pleasantries in a cloyingly mousy tone."
    "I wouldn't describe myself as socially awkward, but Mina's unabashed exuberance was making me more than a little uncomfortable."
    "At the same time... who can argue against the pleasant scent of her perfume and the soft warmness of her breasts pressing firmly against my chest?"
    hide screen textbox2 with dissolve

    menu:
        "Make a joke.":
            show screen textbox2 with dissolve
            scene pr0184 with dissolve
            mc "You're... certainly a friendly one, aren't you?"
            scene pr0185 with dissolve
            kil "Don't let her fool you. She's a real ball buster."
            mina "tch...!"
            scene pr0186 with dissolve
            mina "You think I'm...?!"
            mina "..."
            scene pr0187 with dissolve
            mina "Don't listen to him."
            mc "Don't worry. I've known him almost my entire life, remember? I know how just full of shit he is."

        "Hug her tighter. [gr]\[Mina +1\]":
            $ Mina_Affection += 1
            $ Mina_Affection = clamp(Mina_Affection, 0, 40)
            show screen textbox2 with dissolve
            scene pr0188 with dissolve
            mct "(Ah, fuck it. There's no harm in being friendly.)"
            scene pr0189 with dissolve
            mina "That was nice. People don't hug enough I say."


    scene pr0190 with dissolve
    "The three of us had a pleasant conversation over coffee."
    "I learned Mina was an aspiring actress, who met Killian during a modeling shoot where he was the photographer."
    "Given how beautiful, well-put together, and deliberate in her mannerisms she is, that made a whole lot of sense."

    scene pr0191 with dissolve
    "Soon Ian and I parted ways with her, him explaining to her that we had to go to the club for business."

    scene black with dissolve
    mct "(Does she know what kind of place the Carnation Club is...?)"

    play sound "sound effects/notification.wav"
    $ met_mina = True
    show bioadd with dissolve
    $ renpy.pause(3, hard=True)
    scene pr0192 with dissolve
    play ambient "sound effects/city-night.wav"
    play music "music/hotshot.mp3"

    kil "You don't know how through the fucking roof I was last night when Uncle Charles gave me the good news."
    scene pr0193 with dissolve
    kil "Butch Cassidy and the Sundance Kid ride again! Simon and Garfunkel! Bonnie and Clyde!"
    "He continued to list off a dozen or so famous duos, until it grew increasingly nonsensical."
    scene pr0194 with dissolve
    kil "...peanut butter and jelly!"
    mc "Okay, okay... you can stop. I get it."
    scene pr0195 with dissolve
    kil "You sure? I got maybe another six of them ready."
    mc "Yeah, enough!"
    scene pr0196 with dissolve
    "It was nice seeing Killian in high spirits. I mean, he always has a cocky, surefire attitude plastered on his stupid face, but unfiltered joy? That was rare."
    mc "I'm not entirely sold on the place yet, but you being there will help. Also..."
    hide screen textbox2 with dissolve

    menu:
        "Thank him (earnestly).":
            scene pr0197 with dissolve
            show screen textbox2 with dissolve
            mc "Thanks for doing this for me."
        "Thank him (with a joke). [gr]\[Killian +1\]":
            $ Killian_Bromance +=1
            $ Killian_Bromance = clamp(Killian_Bromance, 0, 40)
            show screen textbox2 with dissolve
            scene pr0198 with dissolve
            mc "Thanks for pulling that stick out of my ass."

    mc "Not having to worry about paying for college will be amazing."
    scene pr0199 with dissolve
    kil "Hey, you've always had my back, right?"
    scene pr0200 with fade
    kil "Remember that time the Dylan twins were picking on me after school? It was about ten years ago..."
    kil "They were two grades above us, easily a foot taller, yet you had no hesitation whatsoever."
    kil "You picked up a rock and cracked the pushier one right in his fat head without even saying a word. That was the first time I learned just how much a head wound {i}bleeds{/i}."
    scene pr0201 with dissolve
    mc "That's not a story I'm proud of. Their mother got the school involved..."
    scene pr0202 with dissolve
    kil "You may not be, but I remember it."
    kil "Despite how lame and shy I was, you always included me in things. Now, it's my turn."
    mc "If you say so."
    scene black with dissolve
    "..."
    scene pr0042 with blinds
    "We continued reminiscing about old times until we finally reached the increasingly familiar sight of that red brick tower."
    stop music fadeout 3.0
    stop ambient fadeout 3.0

    scene pr0205 with blinds
    kil "Hey, Jacob."
    jacob "Ian, [mcf]. Good to see you."
    jacob "Head on in."

    scene black with fade
    play music "music/as-i-figure.mp3" fadein 2.0
    "......"
    scene pr0206 with blinds
    "..."
    scene pr0207 with dissolve
    aug "It's lighter than usual, Dalia dear."
    dal "That's because Kimber is out sick with the flu."
    scene pr0208 with dissolve
    aug "Is she now? I should have Warren check up on her and see if she needs anything."
    scene pr0209 with dissolve
    dal "That won't be necessary, I'll--"

    scene pr0210 with dissolve
    aug "Ian! [mcf]!"
    scene pr0211 with dissolve

    play sound "sound effects/slap2.wav"
    sys "*{b}SMACK{/b}!*"
    aug "That'll be all, dear. Scram!"
    scene pr0212 with fade
    aug "I'm glad Chuck could find a way to ease your apprehensions and get you on board."
    aug "We like to keep the business in the family, so to speak. It keeps things simple."
    hide screen textbox2 with dissolve

    menu:
        "Thank him.":
            show screen textbox2 with dissolve
            scene pr0213 with dissolve
            mc "Well, thank you for the opportunity."
            scene pr0215 with dissolve
            aug "Ha! That's quite the different tune from yesterday, eh?"
            aug "I can only imagine what that old pervert cooked up to change your mind. Hehehehe."


        "Ask him about the money.":
            show screen textbox2 with dissolve
            scene pr0214 with dissolve
            mc "What's with all that money?"
            scene pr0216 with dissolve
            aug "Just some business. You'll see a ton of it."

    aug "I suppose you're still in the dark about what you'll be doing here?"

    scene pr0217 with dissolve
    mc "Dr. Chuck's mentioned something about looking out for the wellbeing of the performers, but I don't know what that means."
    scene pr0218 with dissolve
    aug "Ah, yes. {b}That{/b}! You'll technically be working with Kathleen. Entertainment is her purview, but I'll do my best to answer any questions you might have."
    scene pr0219 with dissolve
    mc "I would like that."
    stop music fadeout 3.0
    scene pr0220 with dissolve
    aug "But first, let me pour you a drink."

    scene pr0221 with blinds
    play music "music/horrible.mp3" fadein 3.0

    aug "...so Charles, he comes over to me and says: 'My French is pretty rusty, but I think he's either about to buy you a drink or glass you. Hahahaha!"
    kil "I never knew you and Uncle met while he was stationed in Stuttgart."
    scene pr0222 with dissolve
    aug "That's right, the army is how your uncle paid for college."
    scene pr0227 with dissolve
    mc "It's amazing the two of you stayed in touch your whole lives."
    scene pr0221 with dissolve
    aug "It's more like he couldn't get rid of me! {b}Ha!{/b}."
    scene pr0223 with dissolve
    aug "Anyway, let's move on to why you're here, [mcf]."
    aug "Between Killian and his uncle, I'm not sure what you've been told, so I'll just ask: what would you like to know about the club?"
    scene pr0227 with dissolve
    mct "(That's a pretty open ended question, considering I really only just know this place is a brothel...)"
    hide screen qmenu
    hide screen textbox2 with dissolve

    menu prAugQuestions:

        "So men come here for sex?" if prAugQuestions_sex == False:
            $ prAugQuestions += 1
            $ prAugQuestions_sex = True
            show screen textbox2 with dissolve
            scene pr0224 with dissolve
            mc "So, men really come here for sex?"
            scene pr0225 with dissolve
            kil "Uh, are you okay [mcf]? Did you forget the other day?"
            scene pr0227 with dissolve
            mc "Not that. I mean, do people just walk in all wham, bam, thank you ma'am, or...?"
            scene pr0223 with dissolve
            aug "No. The Carnation Club is pretty exclusive, the people who know about it are few in number and very wealthy."
            aug "No one just casually strolls in. One of our members finding the time to avail themselves of our service is a big deal."
            scene pr0227 with dissolve
            mc "I see..."
            hide screen textbox2 with dissolve
            jump prAugQuestions

        "What am I going to be doing here?" if prAugQuestions_work == False:
            $ prAugQuestions += 1
            $ prAugQuestions_work = True
            show screen textbox2 with dissolve
            scene pr0224 with dissolve
            mc "What exactly will I be doing here?"
            scene pr0223 with dissolve
            aug "I'll let Kathleen explain that in detail, but you'll basically be playing a customer-facing role in a special event we hold every summer."
            aug "Outside of the summer season, you'll do what Ian does: help facilitate things around the club."
            aug "Sometimes this means acting as a gopher, other times making sure our members are having their needs met. Sometimes still, you'll just have to laugh at some unfunny bastard's joke."
            scene pr0227 with dissolve
            mc "When you put it that way, it sounds like almost any other job..."
            scene pr0225 with dissolve
            kil "Nope, just a lot more fun!"
            hide screen textbox2 with dissolve
            jump prAugQuestions

        "What's my schedule going to be like?" if prAugQuestions_schedule == False:
            $ prAugQuestions += 1
            $ prAugQuestions_schedule = True
            show screen textbox2 with dissolve
            scene pr0224 with dissolve
            mc "How often will you need me to come in?"
            scene pr0226 with dissolve
            aug "You're asking because of school?"
            scene pr0223 with dissolve
            aug "You won't have to worry, we'll have a very low demand on your time."
            aug "While we provide some outside entertainment during the week, the actual club is only open on Saturdays and Sundays."
            hide screen textbox2 with dissolve
            jump prAugQuestions

        "Does Rosalind work here?" if prAugQuestions_woman == False:

            $ prAugQuestions += 1
            $ prAugQuestions_woman = True
            show screen textbox2 with dissolve
            scene pr0224 with dissolve
            mc "So, that woman I met last night... did you end up hiring her?"
            scene pr0226 with dissolve
            aug "What woman?"
            scene pr0225 with dissolve
            kil "He means Rosalind. Ah, Rosie! Beautiful, but a bit of a bore in bed."



            kil "You haven't met her yet, but she's a candidate for this summer's exhibition. She and Doc here had a productive... {i}rendezvous{/i} and so here we are."
            scene pr0223 with dissolve
            aug "So that's what the gearhead did to convince you, eh?."
            scene pr0225 with dissolve
            kil "As to your question, don't worry. You'll do more than just see her again. You two will become quite close."

            hide screen textbox2 with dissolve
            jump prAugQuestions

        "That's all." if prAugQuestions >= 2:
            show screen textbox2 with dissolve
            scene pr0227 with dissolve
            mc "That's it. If I think of anything else, I'll let you know."
            jump cctour


    label cctour:
    show screen qmenu with dissolve
    aug "Good! Why don't I get you a tour of the building before taking you to see Kathleen. She'll explain your duties to you more intimately."
    scene black with blinds
    "We proceeded through the building, August offhandedly pointing to rooms and facilities as we passed by them."
    "The building itself was originally an office building, but like the bar, it seems like extensive work had been done to transform it for the club's purposes."
    scene club-bath-day with blinds
    "The building has a few bathrooms, both small and large, modest AND over-the-top."
    scene club-sauna with blinds
    "They have installed a sauna."
    scene club-bedroom1 with blinds
    "Numerous bedrooms. Some for more intimate, normal encounters..."
    scene club-bdsm with blinds
    "Others specially tailored to specific purposes."
    scene club-exhibition with blinds
    "After passing by the kitchen and security room, we rode the elevator to the building's basement level, which has been converted into something resembling a conference hall."
    "The whole room is decorated and furnished in an almost overpowering crimson."
    aug "This is a room we use for our {i}exhibitions{/i}."
    mc "Exhibitions?"
    aug "That's right. That's another thing I'll leave for Kat to explain to you."
    kil "You're going to love them. They're the club's main selling point."
    aug "Now, shall we head back up?"
    stop music fadeout 3.0
    scene black with blinds
    "......"
    "..."

label kathleenmeeting:

    "..."
    scene pr0228 with dissolve
    aug "Well, here we are."
    scene pr0229 with dissolve
    aug "Before I go, take this."
    hide screen textbox2 with dissolve
    menu:
        "What's this?":
            show screen textbox2 with dissolve
            scene pr0230 with dissolve
            mc "What's this for?"
            aug "To make yourself presentable. Buy yourself a suit. Your current attire won't cut it during business hours."

        "I can't take this.":
            show screen textbox2 with dissolve
            scene pr0230 with dissolve
            mc "I can't take this."
            aug "It's not charity, it's a business expense. We can't have you running around here in a t-shirt. We have standards to maintain."

        "Take the money.":
            show screen textbox2 with dissolve
            scene pr0230 with dissolve
            mc "Don't mind if I do."
            aug "It's not a handout. Use it to buy yourself a suit. A t-shirt won't cut it around here."

    scene pr0231 with dissolve
    aug "Killian, you're with me. I need your help lugging up a crate of drinks."
    scene pr0232 with dissolve
    kil "Alright. I'll see you after you talk with the old lady, yeah?"
    mc "Yeah, see you soon."
    scene pr0233 with dissolve
    play sound "sound effects/door-knock.wav"
    "Knock, knock."
    scene pr0233 with dissolve
    kat "Who is it?"
    hide screen textbox2 with dissolve

    menu:
        "It's [mcl], Ma'am. [gr]\[Kat Polite\]":
            $ kat_polite = True
            show screen textbox2 with dissolve
            scene pr0235 with dissolve
            mc "It's [mcl], Ma'am. You asked to see me?"

        "It's [mcf].":
            show screen textbox2 with dissolve
            scene pr0235 with dissolve
            mc "It's [mcf]. You wanted to see me?"

    kat "Let yourself in."
    play sound "sound effects/door-openclose.wav"
    "..."
    scene pr0236 with wiperight
    play music "music/helping-hands.mp3" fadein 3.0
    kat "I was starting to think August was keeping you with one of his long winded stories."
    scene pr0237 with dissolve

    if kat_polite == True:
        mc "He was giving me the tour. How are you, Mrs. Pulman?"
        scene pr0236 with dissolve
        kat "I'm well, thank you for asking."

    else:
        mc "Nope, he was just showing me around the place."
        scene pr0236 with dissolve
        kat "Good, that'll save me the trouble."

    kat "Well, now that you're here..."
    scene pr0238 with fade
    kat "Guess what? I'm your new boss. You'll be working underneath me, at least as far as the summer is concerned."

    if kat_polite == True:
        mc "So Mr. Byrnes told me."
    else:
        mc "August filled me in."

    scene pr0238 with dissolve
    kat "I'm glad you decided to join the club, but I'm going to be frank with you."
    scene pr0239 with dissolve
    kat "Your friend Killian, the one who got you this job, is a moron. He was responsible for the person who held it before you, who turned out to be a catastrophic disappointment."
    kat "I was going to ignore his dumbass completely when looking for a new replacement, but he got his uncle involved - and August, he always listens to Charles."
    scene pr0238 with dissolve
    kat "So, here we are. I'm telling you, not to rake you over the coals about this, but to clear the air. If I don't come across as immediately amiable, good-humored, or courteous it's because you haven't earned my respect for me to pretend I'm otherwise."
    scene pr0240 with dissolve
    "Y-i-k-e-s."
    hide screen textbox2 with dissolve

    menu katyikes:

        "{color=#FF1493}\[Social Chameleon]{/color} Throw Killian under the bus. [gr]\[Kathleen +2\] \[Toughness +2\] [red]\[Killian -3\]" if perk_socialChameleon == True:
            $ Kathleen_Affection += 2
            $ Kathleen_Affection = clamp(Kathleen_Affection, 0, 30)
            $ toughness += 2
            $ toughness = clamp(toughness, 0, 30)
            $ Killian_Bromance -= 3
            $ Killian_Bromance = clamp(Killian_Bromance, 0, 40)
            show screen textbox2 with dissolve
            scene pr0242 with dissolve
            mc "We might be friends, but I'm not like Ian. He acts without thinking and he thinks with his dick."
            scene pr0241 with dissolve
            mc "I'm cautious and driven. I may have had my concerns about working here, but you want someone like that."
            mc "Now that I'm here, and this place is so tangibly linked to my future, I'm committed."
            scene pr0242 with dissolve
            kat "...hmm."
            scene pr0239 with dissolve
            kat "I'll admit you are a different cut than your predecessor. It remains to be seen if you have the qualities needed for this type of work."
            scene pr0242 with dissolve
            mc "What qualities are those?"

        "Reassure her. [gr]\[Kathleen +1\]":
            $ Kathleen_Affection += 1
            $ Kathleen_Affection = clamp(Kathleen_Affection, 0, 30)
            show screen textbox2 with dissolve
            scene pr0242 with dissolve

            if kat_polite == True:
                mc "You won't have any issue with me, Mrs. Pulman."
            else:
                mc "You won't have to worry about me. I'm solid."

            mc "I may have been hesitant about this place, but that was before Dr. Chuck offered to pay for my tuition. I'm not going to screw that opportunity up. Trust me."
            scene pr0239 with dissolve
            kat "...well, at least you can string together two coherent sentences. You have that on your predecessor, but it remains to be seen if you have the qualities needed for this type of work."
            scene pr0242 with dissolve
            mc "What qualities are those?"

        "Try and break the tension. [red]\[Toughness -1\]":
            $ toughness -= 1
            $ toughness = clamp(toughness, 0, 30)
            show screen textbox2 with dissolve
            scene pr0243 with dissolve
            mc "Can't we just go back to flirting, like we did the day before yesterday?"
            scene pr0239 with dissolve
            kat "That will be up to you, but first you're going to have to prove you have the qualities needed for this type of work."
            scene pr0240 with dissolve
            mc "What qualities are those?"

        "{color=#696969}\[Social Chameleon] Throw Killian under the bus.{/color}." if perk_socialButterfly == True or perk_strongman == True:
            jump katyikes

    scene pr0244 with dissolve
    kat "Cold, with with a mix of strong emotional intelligence to know where the line is when dealing with the performers. A good sense of showmanship will help too."
    scene pr0242 with dissolve
    mc "...I don't think I fully understand my job description."
    scene pr0245 with dissolve
    kat "Let's get to that then. Come join me on the couch."
    scene pr0246 with wipeleft
    kat "Every summer we hold a special event, called the {b}summer exhibition{/b}. It's an event spanning multiple weeks, pitting three women against each other."
    scene pr0248 with dissolve
    mc "What are they competing for?"
    scene pr0250 with dissolve
    kat "Usually, each contestant has a unique difficulty - one that is usually fixed with a sudden infux of liquid cash. Sometimes it's something else, but the point is..."
    scene pr0249 with dissolve
    kat "Essentially, the women are competing to make their lives easier."
    scene pr0247 with dissolve
    hide screen textbox2 with dissolve
    menu:
        "Isn't that messed up? [red]\[Toughness -2\]":
            $ toughness -= 2
            $ toughness = clamp(toughness, 0, 30)
            show screen textbox2 with dissolve
            scene pr0248 with dissolve
            mc "Isn't that a bit messed up... to turn their hardships into a spectacle?"
            scene pr0249 with dissolve
            kat "{b}No.{/b} Look at it this way, we're giving them an out, usually to problems of their own making I might add."

        "Go on. [gr]\[Toughness +1\]":
            $ toughness += 1
            $ toughness = clamp(toughness, 0, 30)
            show screen textbox2 with dissolve
            scene pr0248 with dissolve
            mc "Makes sense."

    scene pr0248 with dissolve
    mc "Where do I fit in with all that?"
    scene pr0250 with dissolve
    kat "Your primary role is to make sure the women don't leave the event prematurely. I'm not saying you have to be a friend or an advocate to do this, but you've got to keep them chasing after the carrot."
    scene pr0251 with dissolve
    kat "Basically either keep their morale up by gaining their trust or exploiting their desperation so they keep looking to that light at the end of the tunnel as their only way out."
    scene pr0250 with dissolve
    kat "To this end, that means you'll need to prepare them for the exhibition and control the pace of it, but we can get into the details of that later."
    scene pr0248 with dissolve
    mc "...uh, if they require that kind of management, what is it they'll be doing during these events, exactly?"
    scene pr0251 with dissolve
    kat "Oh, {i}all{/i} kinds of fun stuff. The kind of stuff you'd expect old rich bastards to get off to."
    scene pr0247 with dissolve
    mct "(To hear it put so plainly, makes me skittish about this setup... but, I've got to stay focused on why I'm here.)"
    scene pr0248 with dissolve
    mc "I see..."
    scene pr0252 with dissolve
    kat "Don't worry, I'll ease you into things. I have something fun planned later this week that will give you a taste of what to expect."
    kat "I'll be in touch."
    "......"
    stop music fadeout 3.0
    scene black with fade
    "..."


label hanameet:

    scene pr0254 with blinds
    "After wrapping up my talk with Kathleen, I found my way back to the bar."
    mct "(Huh, guess Ian's still busy...)"
    scene pr0255 with dissolve
    "..."
    woman "Who the hell are you?"
    scene pr0256 with dissolve
    play music "music/take-the-lead.mp3"

    scene pr0257 with dissolve:
        subpixel True
        yalign 0.7
        xalign 0.6
        linear 3 yalign 0.1

    mct "(...wow!)"
    scene pr0258 with dissolve
    woman "Hmm..."
    scene pr0259 with dissolve
    woman "You're too scruffy-looking to be part of the clientele, that must mean..."
    scene pr0260 with dissolve
    woman "... you're the {i}new guy{/i}. Darius' replacement."
    scene pr0261 with dissolve
    mc "That's right. I'm [mcf], nice to meet you..."
    scene pr0262 with dissolve
    scene pr0263 with dissolve
    scene pr0264 with dissolve
    woman "Hana."
    mct "(Hana? That's her name?)"
    scene pr0265 with dissolve
    hana "I tend bar here on the weekends."
    hide screen textbox2 with dissolve
    menu:
        "Look at her ass. [gr]\[Toughness +1\]":
            $ toughness += 1
            $ toughness = clamp(toughness, 0, 30)
            show screen textbox2 with dissolve
            scene pr0266 with dissolve
            mct "(It's kinda a waste thinking that's hidden behind a bar all night...)"

        "Don't be disrespectful. [red]\[Toughness -1\]":
            $ toughness -= 1
            $ toughness = clamp(toughness, 0, 30)
            show screen textbox2 with dissolve
            pass

    scene pr0267 with fade
    hana "Don't take this the wrong way, [mcf]..."

    if toughness >= 20:
        scene pr0268 with fade
        mct "I'm sure I won't..."

    elif toughness <= 19:
        scene pr0268 with fade
        mc "Take what the wrong way?"


    scene pr0269 with dissolve
    hana "You sure you're in the right place? {b}This{/b} is the place you want to be?"
    scene pr0270 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Yes. [gr]\[Toughness +1\]":
            $ toughness += 1
            $ toughness = clamp(toughness, 0, 30)
            show screen textbox2 with dissolve
            scene pr0271 with dissolve
            mc "Without a doubt."

            if roseTakeAdvantage == True:
                mc "I think I might have a lot of fun here."
            else:
                mc "This doesn't seem like such a bad gig."
            scene pr0272 with dissolve
            hana "Really? You don't look the part of an asshole."

        "What's that supposed to mean?":
            show screen textbox2 with dissolve
            scene pr0271 with dissolve
            mc "What are you suggesting?"
            scene pr0272 with dissolve
            hana "I'm saying you look like a big dork."
            scene pr0271 with dissolve
            hana "...no offense, there's nothing wrong with that."


    scene pr0273 with blinds
    kil "Looks can be deceiving."

    scene pr0274 with dissolve
    kil "Hey, Hana. Why don't you make us a drink?"
    scene pr0275 with dissolve
    hana "Get bent, dick-for-brains. I'm off the clock."
    hana "If you want something to drink, get it yourself."
    scene pr0276 with dissolve
    hana "Guess I'll see you around, [mcf]."
    stop music fadeout 3.0
    play sound "sound effects/notification.wav"
    $ met_hana = True
    show bioadd with dissolve
    $ renpy.pause(3, hard=True)
    "..."
    scene pr0277 with dissolve
    kil "What a bitch..."
    mct "(What's with the animosity...?)"
    scene pr0278 with dissolve
    kil "So..."
    kil "We're going out tonight: you, Mina, and myself."
    scene pr0279 with dissolve
    mc "I can't. I've got a final tomorrow."
    scene pr0278 with dissolve
    kil "Is it in the morning?"
    scene pr0279 with dissolve
    mc "...no."
    scene pr0278 with dissolve
    kil "Good, then you can't say no to me. We're going to celebrate us working together."
    scene pr0280 with dissolve
    kil "Don't forget who got you the gig that's going to pay for med school, eh?"
    scene pr0279 with dissolve
    mc "When you put it that way... how could I refuse?"
    scene pr0280 with dissolve
    kil "Good! You understand your position."
    scene pr0278 with dissolve
    kil "We'll be at {i}Circus{/i} tonight. You know the place?"
    scene pr0279 with dissolve
    mc "I do, the cover is a bit pricey though..."
    scene pr0280 with dissolve
    kil "No complaints!"
    scene pr0279 with dissolve
    mc "Fine, just this once."
    "........."
    scene black with fade
    "......"
    "..."
    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionfelicia02 with blinds
    $ renpy.pause(6, hard=True)
label prDiscoIntro:
    stop sound
    $ date = "may10night"
    play music "music/organic.mp3"
    scene pr0281 with blinds
    show may09night with squares
    show screen textbox2 with dissolve
    show screen qmenu with dissolve
    "The first thing that assaulted my senses, even before I'd even stepped inside from the adjoining hallway, was the overwhelming noise."
    "A cacophony of drunken laughter, dozens of conversations, and people just trying to be heard over the persistent din of the club's bad dance music."
    scene pr0282 with irisout
    "Suffice to say, this wasn't my typical idea of a night out, but as Killian had indelicately put it... I owed him."
    "And... well, I wasn't incapable of enjoying the atmosphere. Losing yourself in a mass of people can be fun."
    scene black with fade
    "Thankfully as it was a Sunday night, the place was nowhere near capacity. Finding Ian proved to be a relatively easy task."
    scene pr0283 with dissolve
    kil "There he is! Rare sight seeing you in the wild, doc."
    scene pr0284 with dissolve
    mc "I know. I'm Mr. Shut In, right? What can I say? You didn't leave me any choice tonight."
    scene pr0285 with dissolve
    kil "Well, Mr. Shut In, let me introduce you to Felicia."
    scene pr0286 with dissolve:
        subpixel True
        yalign 0.7
        xalign 0.9
        linear 3 yalign 0.1
    mct "(Legs for days, a slim waist, and huge tits...)"
    scene pr0287 with wipeleft
    fel "Funny, you don't look like a sailor."
    scene pr0288 with dissolve
    mc "That might be because I'm {b}not{/b} a sailor."
    scene pr0289 with dissolve
    mc "I guess Killian likes the thought of me in uniform."
    scene pr0290 with dissolve
    mina "Pfft, hahaha."
    scene pr0291 with dissolve
    mina "It's good to see you again so soon, [mcf]."
    scene pr0292 with dissolve
    mina "I'd hug you, but if I got up, there's no telling where my boyfriend might run off to."
    scene pr0293 with dissolve
    fel "He's been harping on about you most of this week, but I'm starting to wonder just how much he's told me about you is true."
    mct "(Oh boy...)"
    scene pr0294 with dissolve
    mc "Let's find out, shall we? Tell me about myself."
    scene pr0295
    fel "Is it true you ran All-Star Track in high school?"
    scene pr0294
    mc "Not remotely."
    if perk_strongman == True:
        mc "Though I did play a little bit of varsity soccer."
    scene pr0295
    fel "What about the rescue dogs? Do you really own three?"
    scene pr0294 with dissolve
    mc "I live in a small apartment with a no pets policy."

    if history_firestarter == True:
        scene pr0295 with dissolve
        fel "Did you really almost burn down a whole cul-de-sac?"
        scene pr0296 with dissolve
        mc "No--- uh, actually that one is partially true."
        mct "(I can't believe he told her about that. What the hell?)"
        mc "I'm not proud of it, but I was a bit of a firebug when I was a kid. Torched a neighbor's shed one time..."
        mc "It was pretty damn stupid."

    if history_voyeur == True:
        scene pr0295 with dissolve
        fel "Did you really sell pornography growing up?"
        scene pr0296 with dissolve
        mc "No--- uh, {b}wait{/b}... kinda true. He actually told you about that?"
        scene pr0293 with dissolve
        fel "As a shining example of your quote, unquote industrialism."
        scene pr0297 with dissolve
        "Her laugh had a pleasant, song note like quality."
        scene pr0296 with dissolve
        mc "It isn't anything I'm proud of, but I did sell a few photos I {i}might{/i} have secretly taken of some of the neighborhood ladies..."

    if history_stickyFingers == True:
        scene pr0295 with dissolve
        fel "Did you really steal thousands of dollars from your middle school?"
        scene pr0296 with dissolve
        mc "Not at all-- actually..."
        mct "(Why would he use {i}that{/i} to talk me up? I don't understand Ian at times.)"
        mc "It wasn't {i}thousands{/i} of dollars and it isn't anything I'm proud of."

    scene pr0298 with dissolve
    fel "Hey... boys will be boys, right?"
    hide screen textbox2 with dissolve

    menu:
        "That's an understanding view.":
            show screen textbox2 with dissolve
            scene pr0294 with dissolve
            mc "You are {b}amazingly{/b} understanding."
        "Joke. [gr]\[Felicia +1\]":
            $ Felicia_Affection += 1
            $ Felicia_Affection = clamp(Felicia_Affection, 0, 40)
            show screen textbox2 with dissolve
            scene pr0294 with dissolve
            mc "You must have amazingly low standards."
            scene pr0297 with dissolve
            fel "{b}Hahaha--ah!{/b}"

    scene pr0299 with dissolve
    mina "Hey, we've all done things we aren't proud of."
    scene pr0300 with dissolve
    kil "Yeah. Prim and Proper's idea here of regret is eating cake outside her cheat day."
    scene pr0301 with dissolve
    mina "Shut up! I've done things..."
    scene pr0302 with dissolve
    mina "If you'll excuse me, I've got to hit the ladies room."
    scene pr0303 with dissolve
    kil "Don't disappear on me now, sweetie."
    scene pr0304 with dissolve
    mc "Tell me about yourself, Felicia."
    scene pr0305 with dissolve
    fel "Oh, there's nothing to tell."
    scene pr0304 with dissolve
    mc "C'mon, you probably know a dozen fictitious things about me thanks to Ian. Why don't you at least make something up?"
    scene pr0306 with dissolve
    fel "Fair's fair? You just want me to lie?"
    scene pr0304 with dissolve
    mc "It doesn't have to be a lie, but whatever you do tell me, I'll have no way of knowing if it's the truth."
    scene pr0307 with dissolve
    fel "Okay."
    fel "Would you believe that before I was the respectable woman who sits before you, pillar of the PTA, shining example of all things dull and drab about the upper class..."
    scene pr0323 with dissolve
    fel "Before that... when I was in college, I worked as an escort."
    scene pr0304 with dissolve
    mc "W-what? Really?"
    scene pr0306 with dissolve
    fel "Maybe."
    scene pr0308 with dissolve
    kil "I wonder--"
    scene pr0309 with dissolve
    kil "--Oh?"
    scene pr0310 with dissolve
    kil "Hold that thought, I'll be right back."
    scene pr0328 with dissolve
    fel "..."
    mc "..."
    scene pr0311 with dissolve
    fel "Then there was two..."
    scene pr0312 with dissolve
    fel "So, Killian's bullshit can be fun, but how did you guys honestly meet? "
    scene pr0313 with dissolve
    mc "We've known each other since we were kids. We shared a homeroom together."
    mc "He didn't always have the confidence he has now, which is probably why we hit it off."
    scene pr0314 with dissolve
    fel "It must be nice knowing someone that long."
    mc "I suppose."
    scene pr0315 with dissolve
    fel "You don't think so?"
    scene pr0316 with dissolve
    mc "Time doesn't always temper a friendship. You know what they say: absence makes the heart grow fonder and familiarity breeds contempt."
    mc "How about you? How did you meet?"
    scene pr0317 with dissolve
    fel "Through Mina. I know her from work."
    scene pr0318 with dissolve
    mc "You're a model too?"
    scene pr0312 with dissolve
    fel "Oh no, I wish! I just help out at the agency."
    scene pr0313 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Compliment her.":
            show screen textbox2 with dissolve
            mc "Help out? You're certainly pretty enough to be a model yourself."
            scene pr0312 with dissolve
            fel "That's nice of you to say, but there's more to it than looks."
            scene pr0313 with dissolve
            mc "I thought that was pretty much the job description..."

        "Show interest in her work. [gr]\[Felicia +1\]":
            $ Felicia_Affection += 1
            $ Felicia_Affection = clamp(Felicia_Affection, 0, 40)
            show screen textbox2 with dissolve
            mc "Oh? You must have the chance to meet all kinds of people. What do you do there?"
            scene pr0319 with dissolve
            fel "I do, but I don't work there in any official capacity. Sometimes I take calls, sort applications, file documents. That kind of thing."
            scene pr0318 with dissolve
            mc "Not in an official capacity?"
            scene pr0312 with dissolve
            fel "Yeah, the owner is a friend of mine. He lets me help out when I go stir-crazy."


    scene pr0319 with dissolve
    fel "What about you? What do you do?"
    scene pr0318 with dissolve
    mc "I'm a student."
    scene pr0314 with dissolve
    fel "A student, huh? That must be nice, having so--"
    scene pr0320 with wiperight
    mina "Damn it! Where did that man run off to?"
    scene pr0321 with dissolve
    mc "..."
    scene pr0322 with dissolve
    fel "Well, it seems it's that time of the night."
    fel "This happens every time we go out. Poor girl's a fucking moron letting herself get worked up like that."
    stop music fadeout 3.0
    fel "You should go check on her."
    "..."
    play music "music/edm-detection-mode.mp3"
    jump DiscoFreeRoamTable

#------------------------------------------------------------------------------#
#                                   May 11                                     #
#------------------------------------------------------------------------------#


label prAfterParty:
    $ prAfterParty = True
    stop music fadeout 3.0
    scene black with fade
    show screen qmenu with dissolve
    scene pr0534 with blinds
    play ambient "sound effects/city-night.wav"
    "From the club, we moved to Ian's penthouse suite."
    scene pr0535 with dissolve
    fel "Aaaah-- this water feels AMAZING!"
    scene pr0536 with dissolve
    mina "It's too bad you don't have a bathing suit to change into."
    scene pr0537 with dissolve
    fel "Why would that stop me?"
    scene pr0538 with irisout
    kil "Why don't you girls change into something more comfortable?"
    scene pr0539 with dissolve
    mina "Good idea. My feet are killing me!"
    scene pr0540 with dissolve
    mina "Come on, Felicia. I've got some clothes here that might fit you."
    fel "Ah-- alright."
    scene pr0541 with dissolve
    fel "Don't get up to any fun without us!"
    scene pr0542 with fade
    stop ambient fadeout 3.0
    play music "music/night-on-the-docks-sax.mp3"
    mc "Nice view you have here."
    kil "Huh? This is your first time seeing it? I've lived here for two years..."
    mc "Nope. We only ever get coffee every now and then."
    scene pr0543 with dissolve
    kil "Damn, well all that will soon change. Working at the Carnation Club, you and I are going to get up to all sorts of things again."
    scene pr0544 with dissolve
    hide screen textbox2 with dissolve
    menu:
        "Looking forward to it. [gr]\[Killian +1\]":
            $ Killian_Bromance += 1
            $ Killian_Bromance = clamp(Killian_Bromance, 0, 40)
            show screen textbox2 with dissolve
            scene pr0545 with dissolve
            mc "Yeah, that actually sounds great."

        "If you say so.":
            show screen textbox2 with dissolve
            scene pr0545 with dissolve
            mc "Yeah, I bet..."

    kil "Count on it!"
    scene pr0546 with dissolve
    kil "So, how's Victoria doing?"
    scene pr0547
    mc "She's doing good. She told me to tell you 'hi' the next time I saw you."
    scene pr0546 with dissolve
    kil "Do you think she'd want to get lunch sometime. I'd like to catch up."
    scene pr0547
    mc "You kidding? She'd love it."
    scene pr0546
    kil "I do miss seeing her everyday after school. In some ways, she felt more like a mom to me than my own."
    scene pr0547
    mc "C'mon, you know your mother loves you..."
    kil "She has a funny way of showing it."
    hide screen textbox2 with dissolve
    menu:

        "So do you.":
            show screen textbox2 with dissolve
            scene pr0548 with dissolve
            mc "Yeah, but you of all people should know that showing affection doesn't come easy to some."
            mc "People aren't Hallmark cards."
            scene pr0549 with dissolve
            kil "Easy for you to say. You mother's fucking perfect."
            scene pr0547 with dissolve
            mc "I'm not going to argue with you there."


        "You've got it good, cut them some slack.":
            show screen textbox2 with dissolve
            scene pr0548 with dissolve
            mc "What are you talking about? You've got it better than most."
            mc "You parents set you up for life, they never emotionally or physically abused you..."
            mc "Hell, they never put any pressure on you altogether."
            scene pr0549 with dissolve
            kil "Couldn't you let me gripe without giving me a dose of reality, huh?"

    fel "We're back, boys."
    scene pr0550 with fade
    mc "--!"
    stop music fadeout 3.0
    play music "music/there-it-is.mp3"

    scene pr0551 with dissolve:
        subpixel True
        yalign 0.7
        xalign 0.6
        linear 3 yalign 0.1

    $ renpy.pause(2.3, hard=True)
    scene pr0552 with dissolve
    mct "(Hot damn, that's what Mina calls comfortable?)"
    kil "I thought we'd play a drinking game."
    scene pr0553
    mina "Ugh... more drinking?"
    scene pr0554 with dissolve
    kil "I'll get the stuff."
    scene black with fade
    stop music fadeout 3.0
    "Killian went to the kitchen, grabbed the alcohol, and we got set up for the game."
    play music "music/hotshot.mp3"
    scene pr0555 with blinds
    mc "Okay, so how do we play this?"
    kil "Okay. This one is called {i}King's Game{/i}."
    kil "It's simple. Each card is assigned an instruction."
    kil "We'll go around in a circle one at a time, draw cards, and execute those instructions until we're too shitfaced to play."
    kil "Here's the rules..."
    scene pr0556 with dissolve
    kil "Simple game, lots of rules. Luckily you don't have to remember all of that. I've got you covered."
    scene pr0557 with dissolve
    mina "Push ups?! How is that fun! Why can't we just talk and drink?"
    scene pr0558 with dissolve
    fel "Aw, come on, sweetie."
    fel "It's all just an excuse to loosen up and have a little fun."
    scene pr0559 with dissolve
    mina "{b}Fiiiine{/b}."
    scene pr0560 with dissolve
    mc "Seems like it might be fun."
    scene pr0561 with dissolve
    kil "Alright! That's the spirit!"
    kil "Let's get the ball rolling then. I'll start and then we'll go clockwise."
    scene pr0562 with fade
    "Killian turned a five face up."
    kil "That means you and I got to take a shot."
    scene pr0563 with fade
    mct "(Simple enough.)"
    scene pr0564 with dissolve
    kil "Now, it's your turn to draw, [mcf]."
    scene pr0565 with fade
    kil "A seven..."
    mina "What's that one mean again?"
    scene pr0566 with dissolve
    kil "{b}Ahem{/b}..."
    scene pr0567 with dissolve
    kil "...last one to stand up drinks."
    scene pr0568 with fade
    mina "Oh, you jerk--"
    mina "You stood up before you even told us!"
    scene pr0569 with dissolve
    kil "Rules are rules, gotta knock one back."
    mina "Grrrrrr!"
    fel "Here, let me help!"
    scene pr0570 with fade
    fel "Bottoms up!"
    kil "Felicia's turn now."
    scene pr0571 with dissolve
    fel "Coooome on {b}King{/b}!"
    scene pr0572 with fade
    "..."
    scene pr0573 with dissolve
    fel "Damn!"
    kil "That means everyone drinks but Felicia..."
    scene pr0574 with fade
    "..."
    scene pr0575 with fade
    mina "My turn!"
    scene pr0576 with dissolve
    mina "Yes! A queen! I get to ask everyone a question, right?"
    kil "That's right, exactly one question per person."
    kil "Pick a person, ask your question, and they must either answer it truthfully or take two shots."
    scene pr0577 with dissolve
    fel "Make them good!"
    mina "Hmm..."
    scene pr0578 with dissolve
    mina "I'll start with you, [mcf]."
    mc "Okay, shoot."
    mina "When's your birthday?"
    scene pr0579 with dissolve
    fel "Huh? That's it? You can ask him ANYTHING and you wanna know when his birthday is?"
    fel "You could just ask him that between rounds!"
    scene pr0580 with dissolve
    mina "Hey! I'm the asking the questions here, so pipe down!"
    scene pr0581 with dissolve
    kil "Well, what will it be? Answer the question or take two shots?"
    hide screen textbox2 with dissolve
    menu:
        "Tell her your birthday. [gr]\[Mina +1\]":
            $ prBirthdayMinaGift = True
            $ Mina_Affection += 1
            $ Mina_Affection = clamp(Mina_Affection, 0, 40)
            show screen textbox2 with dissolve
            scene pr0582 with dissolve
            mc "Gee, I wonder what I'll pick: it's June 7th."
            scene pr0583 with dissolve
            mina "That's in..."
            scene pr0584 with dissolve
            mina "Just over three weeks! That's close!"
            mina "How old will you be?"
            scene pr0585 with dissolve
            kil "Ah, ah, ah! You only get one question. Don't answer that, [mcf]."
            mina "WHAT?! For real?"
            kil "Those are the rules."
            kil "Now, you've got two questions remaining for Felicia and myself."


        "Take the shots. [gr]\[Felicia +1\]":
            $ Felicia_Affection += 1
            $ Felicia_Affection = clamp(Felicia_Affection, 0, 40)
            show screen textbox2 with dissolve
            "Obviously, it's a harmless question, but it might be fun to tease her by denying her the simple information."
            scene pr0586 with dissolve
            mina "WHAT?! You're kidding me?"
            mc "Huh? I'm here to drink."
            mina "What are you, an alcoholic?"
            scene pr0587 with dissolve
            mina "Ian! What's his birthday?"
            scene pr0588 with dissolve
            kil "Hey, if [mcf] doesn't want to share that information with you, it's not my place to go over his head."
            fel "Pffhahahaha!"
            kil "Now, you've got two questions remaining for Felicia and myself."


    scene pr0589 with dissolve
    mina "Alright, Felicia...."
    fel "Yeah, sweetie?"
    scene pr0590 with dissolve
    mina "Hmm..."
    scene pr0591 with dissolve
    mina "What is the MOST adventurous thing you've done in bed?"
    mct "(I can't help but notice a disparity between Felicia and my own questions...)"
    scene pr0592 with dissolve
    fel "That's more like it! Though I would've like to known [mcf]'s answer to that question."
    scene pr0591 with dissolve
    mina "You should tailor your questions to your audience."
    scene pr0593 with dissolve
    fel "I'm going to ignore that implication, sweet thing."
    mct "(Me too... I think.)"
    scene pr0594 with dissolve
    fel "My most wildest sex act, huh...?"
    scene pr0595 with dissolve
    fel "When I was pledging to my sorority, we had to endure all kinds of shit."
    fel "All sorts of... {b}degrading{/b} and {i}fun{/i} things."
    fel "One time I had to ride a Sybian machine in front of an entire greek mixer."
    scene pr0596 with dissolve
    kil "Oh, you kinky bitch!"
    scene pr0597 with dissolve
    mina "Ian! Don't call her that!"
    scene pr0598 with dissolve
    mina "..."
    scene pr0599 with dissolve
    mina "What's a... {i}Sybian{/i} machine...?"
    scene pr0600 with dissolve
    fel "Oh, sweetie..."
    fel "It's a..."
    scene pr0601 with dissolve
    kil "A motorized dildo on a seat, basically."
    scene pr0602 with dissolve
    mina "OH MY GOD! REALLY?"
    mina "In front of a {b}WHOLE{/b} room of PEOPLE?!"
    mina "How... h-how..."
    scene pr0603 with dissolve
    fel "You're burning red! I can't believe how cute you are."
    scene pr0604 with dissolve
    fel "What can I say? That's when I learned I liked being the center of attention."
    fel "I imagine you feel a similar thing when you're on a photo shoot, right sweetie?"
    mina "Well..."
    mina "I couldn't ever do anything THAT embarrassing, but I do enjoy all the pampering on set I suppose..."
    scene pr0607 with slideleft
    kil "Okay, it's my turn to get asked a question."
    scene pr0608 with dissolve
    mina "Okay! Same question as Felicia."
    kil "..."
    scene pr0609 with fade
    mina "HEY!"
    scene pr0610 with dissolve
    kil "Sorry, I know better than to open that can of worms."
    fel "What do you mean--!"
    scene pr0611 with dissolve
    kil "Now, it's back to me."
    scene pr0612 with dissolve
    kil "{b}We're all whores.{/b} Everyone take off a piece of clothing as fast as you can!"
    scene pr0613 with fade
    "In a flurry, everyone rushed to take off a piece of clothing. Paying no mind to modesty, three of us had a similar idea: the top's the quickest."
    "Meanwhile, Mina got hung up on her sock."
    scene pr0614 with dissolve
    mina "Grr..! {b}Drat!{/b}"
    mc "..."
    mc "(Wait a minute...)"
    fel "Looks like you're drinking, sweetie."
    mina "Yeah, yeah..."
    scene pr0615 with dissolve
    "Caught up in the moment, it was slow to dawn on me that Felicia was now topless."
    "Her golden breasts were unabashedly on display, yet it didn't seem to faze the three of them, least of all Felicia."
    scene pr0616 with fade
    "In fact, everything carried on business as usual..."
    scene pr0617 with dissolve
    mina "Eeeh, I'm starting to feel it."
    fel "There, there!"
    scene pr0618 with fade
    mc "Guess it's my go again..."
    scene pr0619 with fade
    $ prGetOutOfJail = True
    kil "That's a get out of jail free card. You get to force someone else to do a punishment affecting you."
    kil "Use it wisely!"
    scene pr0620 with fade
    mc "Awesome. Your go, Felicia."
    scene pr0621 with dissolve
    fel "Let's see..."
    kil "Three is me - take a drink."
    fel "Really? Another BORING draw."
    scene pr0622 with dissolve
    "With a sigh, Felicia quickly downed her punishment."
    scene pr0623 with fade
    mina "I'm up!"
    scene pr0624 with dissolve
    mina "Please, please, please, PLEEEASE don't let me have to drink..."
    scene pr0625 with fade
    kil "Spin the bottle. Whoever it lands on, you either both have to take a shot or kiss."
    scene pr0626 with dissolve
    mina "Heck yeah!"
    scene pr0627 with fade
    mina "Alright, here I go..."
    hide screen textbox2 with dissolve
    scene prAfterPartySpin
    $ renpy.pause(3.8, hard=True)
    show screen textbox2 with dissolve
    mina "Oh...!"
    "The bottle finally crawled to a stop on me."
    scene pr0634 with dissolve
    mina "Guess we have to kiss, huh?"
    mina "That is, if you want to..."
    "Who the hell wouldn't want to? Mina is easily one of the most attractive girl's I ever met."
    "On the flip side, I guess it would be kinda weird to kiss Ian's girl in front of him."
    "I could turn her down, but I might risk hurting her feelings. I could also use my get out of jail free card to have her kiss someone else."
    "In that case, she'd probably appreciate it if I picked Ian, but there is ALWAYS Felicia..."
    stop music fadeout 3.0
    hide screen textbox2 with dissolve
    menu:
        "Kiss her. [gr]\[Mina +1\]":
            $ Mina_Affection += 2
            $ Mina_Affection = clamp(Mina_Affection, 0, 40)
            play music "music/love-or-lust.mp3"
            show screen textbox2 with dissolve
            jump prAfterPartyMinaKiss


        "Have her kiss Ian. [gr]\[Mina +1\]":
            $ Mina_Affection +=1
            $ Mina_Affection = clamp(Mina_Affection, 0, 40)
            $ prGetOutOfJail = False
            play music "music/love-or-lust.mp3"
            show screen textbox2 with dissolve
            jump prAfterPatyMinaIanKiss

        "Have her kiss Felicia. [gr]\[Killian +1\] \[Mina Bi +1\]":
            $ Killian_Bromance += 1
            $ Killian_Bromance = clamp(Killian_Bromance, 0, 40)
            $ Mina_BiCurious += 1
            $ Mina_BiCurious = clamp(Mina_BiCurious, 1, 5)
            $ prGetOutOfJail = False
            play music "music/love-or-lust.mp3"
            show screen textbox2 with dissolve
            jump prAfterPartyMinaFeliciaKiss

        "Both of you take a shot. [red]\[Mina -1\]":
            $ Mina_Affection -= 1
            $ Mina_Affection = clamp(Mina_Affection, 0, 40)
            show screen textbox2 with dissolve
            jump prAfterPartyMinaKissDeny


label prAfterPartyMinaKiss:

    scene pr0635 with dissolve
    mc "It's only a game, right?"
    kil "Exactly!"
    kil "...but remember, you gotta make it good! No half assing it."
    mct "(Is it me, or does Killian seem extra-enthused about this...?)"
    scene pr0636 with fade
    mina "..."
    scene pr0637 with dissolve
    mina "You know, you've got a pretty good physique, [mcf]."
    mc "Uh... thank you."
    scene pr0638 with dissolve
    mina "Well, no half assing, right?"
    hide screen textbox2 with dissolve
    menu:
        "Half ass it.":
            show screen textbox2 with dissolve
            "Despite saying that, this is still pretty weird."
            scene pr0639 with dissolve
            "{b}*Fwup!*{/b}"
            "I opted to keep it as chaste as I could and luckily, Mina followed my lead."
            "......"
            scene pr0638 with dissolve
            "..."
            mina "That was nice."
            scene pr0640 with dissolve
            mina "...and I didn't have to drink! Woohoo!"
            jump prAfterParty2

        "Put on a show. [red]\[MinaKillian -1\]":
            $ Mina_KLove -= 1
            $ Mina_KLove = clamp(Mina_KLove, 0, 10)
            show screen textbox2 with dissolve
            "Ah, fuck it. If it's supposed to be believable..."
            scene pr0639 with dissolve
            "Might as well have fun with it."
            scene pr0641 with dissolve
            mina "Mmmhn....!"
            "Mina's body tensed up as she awkwardly tried to find the best way to reciprocate."
            scene pr0642 with dissolve
            mina "...aaah!"
            "Eventually, all that tension evaporated and she went slack in my arms, openly accepting the advance of my tongue as it intertwined with her own."
            "......"
            "..."
            scene pr0643 with dissolve
            mina "Ha... ha... ha..."
            mc "I hope I didn't go too far..."
            mina "N-no... it was part of the game."
            jump prAfterParty2





label prAfterPatyMinaIanKiss:
    "Let's not make this weird."
    scene pr0644 with dissolve
    mc "Yeaaaah, I'm going to use my get out of jail free card..."
    mc "...and pass the buck to Ian."
    scene pr0645 with dissolve
    mina "Yaaaay!"
    fel "Oh, come on. That's so boring."
    scene pr0646 with dissolve
    fel "Should've picked me at least, I can guarantee you she's never kissed a girl before."
    scene pr0647 with fade
    "The two of them shared an intimate, deep, but ultimately restrained kiss."
    scene pr0648 with dissolve
    mina "Kinda sucks it takes a game to get a little PDA, but thank you [mcf]."
    jump prAfterParty2



label prAfterPartyMinaFeliciaKiss:
    if _in_replay:
        show screen textbox2 with dissolve
        play music "music/love-or-lust.mp3"

    "Let's not make this weird... for me at least."
    scene pr0644 with dissolve
    mc "Yeeeeaaah, I'm going to use my get out of jail free card..."
    mina "Huh? You're making it sound like kissing me is a punish--"
    scene pr0649 with dissolve
    mc "...and hand it off to Felicia."
    kil "Hell yeah!"
    play sound "sound effects/slap3.wav"
    scene pr0650 with dissolve
    mina "Uh... really?" with flash
    mina "I've... never kissed a girl before..."
    fel "It's not much different than kissing a guy, just a little more... lip-balmy."
    mina "O-okay, if you say so..."
    scene pr0651 with fade
    fel "I'll take the lead, okay?"
    "Mina was clearly flustered by this turn of events. All she could do was silently nod in assent."
    scene pr0652 with dissolve
    fel "Hmm...? Is that strawberries?"
    fel "You gotta tell me what shampoo you use after this."
    scene pr0653 with dissolve
    mina "{b}Mmmh....!{/b}"
    scene pr0654 with dissolve
    "Felicia wasted no time in assaulting Mina's mouth, her tongue forcefully finding it's way past her pursed lips and into the warm valley beyond."
    scene pr0655 with dissolve
    "It wasn't long before Mina surrendered to Felicia's forceful ministrations, as the golden beauty crept her hand up to and gently massaged the model's breast."
    scene pr0656 with dissolve
    "{b}*Fwup... chup... fwah...!*{/b}"
    scene pr0657 with dissolve
    mina "{b}Maaaaaah!{/b}"
    "It was quicky evolving into more than a convincing kiss..."
    "In fact, it was going well beyond. Felicia's hand suddenly lurched down to Mina's cloth panties."
    scene pr0658 with dissolve
    "Mina had completely forgotten herself by this point. If Felicia wanted to take it any further, I doubt she'd have faced any resistance."
    scene pr0659 with dissolve
    "Fortunately for her, Felicia's ferocious attack gradually abated into a tender kiss."
    scene pr0660 with dissolve
    mina "T-that was WAY too far!"
    fel "Really? I'm sure the boys don't have any complaints."
    kil "{size=-10}Holy shit, that was fucking HOT. Well played, you horndog!{/size=-10}"
    mc "{size=-10}Don't give me too much credit, I wasn't expecting {b}THAT{/b}...{/size=-10}"
    if not persistent.minaFeliciaKissGalleryy:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.minaFeliciaKissGallery = True
    $ renpy.end_replay()

    jump prAfterParty2


label prAfterPartyMinaKissDeny:
    "Let's not make this weird."
    scene pr0661 with dissolve
    mc "Yeah, sorry. It's kinda weird kissing my friend's girlfriend."
    kil "Oh, I don't mind, in fact..."
    mc "It's still weird!"
    scene pr0662 with dissolve
    mc "Sorry Mina, you're extremely hot, but..."
    mina "Don't worry, I get it."
    scene pr0663 with fade
    mc "Bottoms up!"
    jump prAfterParty2

label prAfterParty2:
    stop music fadeout 3.0
    scene black with fade
    scene pr0664 with dissolve
    kil "Alrighty..."
    scene pr0665 with dissolve
    kil "King! That's mean--"
    scene pr0666 with dissolve
    mina "Oh no! You're gonna have us do something perverted, right?"
    scene pr0667 with dissolve
    kil "... c'mon, why would you come to that conclusion?"
    mc "Who are you trying to fool?"
    scene pr0668 with dissolve
    fel "Come on, {b}get on with it{/b}."
    scene pr0669 with dissolve
    kil "Hm..."
    scene pr0670 with dissolve
    kil "All three of you have to... jump in the pool."
    mc "Clothed? I don't have a change of clothes..."
    scene pr0671 with dissolve
    kil "You can do it nude if you want. I'll leave that up to you."
    "Well, there's no way I'm spending the night in wet jeans..."
    hide screen textbox2 with dissolve

    menu:
        "Jump into the pool with just your underwear on.":
            play music "music/hotshot.mp3"
            show screen textbox2 with dissolve
            jump prAfterPartyPoolJumpUnderwear

        "No way I'm walking home in soggy underwear: take it all off. [gr]\[Felicia +1\]":
            $ Felicia_Affection += 1
            $ Felicia_Affection = clamp(Felicia_Affection, 0, 40)
            play music "music/hotshot.mp3"
            show screen textbox2 with dissolve
            jump prAfterPartyPoolJumpNude

        "Use your get out of jail card: make Ian do it." if prGetOutOfJail == True:
            play music "music/hotshot.mp3"
            $ prGetOutOfJail = False
            show screen textbox2 with dissolve
            jump prAfterPartyPoolJumpIan

label prAfterPartyPoolJumpUnderwear:
    scene pr0672 with dissolve
    "Nope. I'll have a {i}little{/i} modesty at least."
    scene pr0673 with dissolve
    "Wordlessly, I began undoing my pants, stopping at my underwear."
    scene pr0674 with dissolve
    fel "Aw, keep going!"
    mc "Sorry, but if you'll excuse me..."
    scene pr0677 with irisout
    play sound "sound effects/water-splash.wav"
    mc "Geronimo!"
    scene pr0679 with fade
    kil "Your girl's turn... that or you can take three shots."
    scene pr0680 with fade
    mina "Ugh... no thank you! Besides, this might help me sober up."
    scene pr0681 with dissolve
    mina "I hate being drunk!"
    fel "Hey, wait for me!"
    scene pr0683 with fade
    play sound "sound effects/water-splash.wav"
    "..."
    scene black with fade
    mina "Yeeeees! The water feels so goooood, Ian."
    scene pr0684 with fade
    mina "Why don't you jooooin us?"
    scene pr0686 with dissolve
    kil "That didn't sober you up, did it?"
    mina "Mmmmh..."
    mina "No."
    kil "Come on out of there and dry off."
    kil "I don't want you catching a cold."
    mina "Fiiine."
    scene pr0688 with dissolve
    "..."
    jump prAfterParty3


label prAfterPartyPoolJumpNude:
    scene pr0672 with dissolve
    "Ah, fuck it. No one will remember this in the morning anyway."
    scene pr0675 with dissolve
    "Wordlessly, I began undoing my pants, underwear and all."
    scene pr0676 with dissolve
    fel "Nice dick!"
    kil "You sure wasted no time whipping your cock out."
    mc "Thank you."
    mc "{b}Now{/b}, if you'll excuse me..."
    scene pr0678 with irisout
    play sound "sound effects/water-splash.wav"
    mc "Geronimo!"
    scene pr0679 with fade
    kil "Your girl's turn... might I suggest following [mcf]'s example?"
    scene pr0680 with dissolve
    mina "Fat chance you, perv! Besides, this might help me sober up."
    scene pr0681 with dissolve
    mina "I hate being drunk!"
    fel "Hey, wait for me!"
    scene pr0682 with fade
    play sound "sound effects/water-splash.wav"
    "..."
    scene black with fade
    mina "Yeeeees! The water feels so goooood, Ian."
    scene pr0685 with dissolve
    mina "Why don't you jooooin us?"
    scene pr0687 with dissolve
    kil "That didn't sober you up, did it?"
    mina "Mmmmh..."
    mina "No."
    kil "Come on out of there and dry off."
    kil "I don't want you catching a cold."
    mina "Fiiine."
    scene pr0689 with fade
    "..."
    jump prAfterParty3

label prAfterPartyPoolJumpIan:
    $ prPoolJumpKillian = True
    scene pr0694 with dissolve
    mc "How about you do it? I'm turning in my--"
    scene pr0695 with fade
    kil "Suit yourself!"
    "Without hesitation, Ian barreled toward the pool."
    scene pr0690 with irisout
    play sound "sound effects/water-splash.wav"
    kil "Canon ball!"
    scene pr0696 with fade
    mina "That looks like fun. Maybe this will help me sober up, too."
    scene pr0697 with dissolve
    mina "I hate being drunk!"
    fel "Hey, wait for me!"
    scene pr0698 with fade
    play sound "sound effects/water-splash.wav"
    "..."
    scene black with fade
    kil "The water's nice. You should join us, [mcf]."
    scene pr0691 with dissolve
    mina "Yeah, why don't you jooooin us?"
    scene pr0692 with fade
    mc "I think I'll pass."
    kil "That didn't sober you up, did it?"
    mina "Mmmmh..."
    mina "No."
    kil "We should get out and dry off."
    kil "I don't want you getting sick."
    mina "Fiiine."
    scene pr0693 with fade
    mc "Let me help you--"
    scene black with fade
    play sound "sound effects/water-splash.wav"
    mc "Shit!"
    scene pr0693b with dissolve
    fel "Guess you're going to have to slip out of your clothes now, huh?"
    "......."
    scene black with fade
    "..."
    jump prAfterParty3

label prAfterParty3:

    if prPoolJumpKillian == False:
        scene pr0699 with blinds
        mc "Why did you change into a towel, exactly? You didn't even jump into the pool."
        scene pr0700 with dissolve
        kil "What? Can't a man get comfortable in his own house. Besides, there's never a bad time to air out the boys."
        mc "Riiiight..."

    scene pr0701 with dissolve
    mc "Okay, it was my turn, right?"
    scene pr0702 with dissolve
    "..."
    scene pr0703 with dissolve
    mc "A nine..."
    mc "What was that again?"
    mina "Push ups! ....right?"
    kil "Yep. Do twenty or take a sip for every rep you fail to do."
    "Doing push ups in the dead of night, drunk doesn't sound very fun."
    if prGetOutOfJail == True:
        "...but I still have my get out of jail card if I want to use it."
        hide screen textbox2 with dissolve
        hide screen qmenu with dissolve
        jump pushUpMenu
    else:
        "...but I guess I have no choice unless I want to drink."
        jump prAfterPartyPushUp
    menu pushUpMenu:
        "Just do it yourself.":
            show screen textbox2 with dissolve
            show screen qmenu with dissolve
            "Fuck it, I'll do them myself."
            jump prAfterPartyPushUp
        "Have Ian do them.":
            show screen textbox2 with dissolve
            show screen qmenu with dissolve
            jump prAfterPartyPushUpKillian
        "Have Mina do them. [red]\[Mina -1\]":
            $ Mina_Affection -= 1
            $ Mina_Affection = clamp(Mina_Affection, 0, 40)
            show screen textbox2 with dissolve
            show screen qmenu with dissolve
            jump prAfterPartyPushUpMina
        "Have Felicia do them.":
            show screen textbox2 with dissolve
            show screen qmenu with dissolve
            jump prAfterPartyPushUpFelicia

label prAfterPartyPushUp:
    scene pr0704 with blinds
    kil "Looking good, bro."
    mc "Here I go..."
    scene pr0705 with dissolve
    "..."
    scene pr0704 with dissolve
    mc "One..."
    scene pr0705 with dissolve
    "..."
    scene pr0704 with dissolve
    mc "Two..."
    scene pr0705 with dissolve
    "..."
    scene pr0704 with dissolve
    mc "Three..."
    scene black with fade

    if perk_strongman == True:
        $ Felicia_Affection += 1
        $ Felicia_Affection = clamp(Felicia_Affection, 0, 40)
        scene pr0707 with dissolve
        "..."
        scene pr0706 with dissolve
        mc "Twenty...!"
        scene pr0709 with dissolve
        kil "Nice! I knew you could do it."
        scene pr0710 with blinds
        fel "You really..."
        scene pr0711 with dissolve
        fel "Broke up a sweat, huh?"
        jump prAfterParty4

    else:
        scene pr0704 with dissolve
        mc "Seventeen...!"
        mc "Ugh..."
        scene pr0708 with dissolve
        mc "That's it. Anymore and I think I'll chuck."
        kil "That's three sips!"
        mc "Right..."
        scene pr0712 with dissolve
        mc "To your health!"
        scene pr0713 with dissolve
        "..."
        jump prAfterParty4


label prAfterPartyPushUpKillian:
    scene pr0717 with dissolve
    mc "I'll use my get out of jail free card here."
    mc "You're up, friend."
    scene pr0718 with dissolve
    kil "This'll be a cinch."
    scene pr0714 with dissolve
    kil "Here I go..."
    scene pr0715 with dissolve
    "..."
    scene pr0714 with dissolve
    kil "One..."
    scene pr0715 with dissolve
    "..."
    scene pr0714 with dissolve
    kil "Two..."
    scene pr0715 with dissolve
    "..."
    scene pr0714 with dissolve
    kil "Three..."
    scene black with fade
    "..."
    scene pr0714 with dissolve
    kil "Twenty!"
    scene pr0716 with dissolve
    kil "Easy peasy."
    "..."
    jump prAfterParty4


label prAfterPartyPushUpMina:
    scene pr0719 with dissolve
    mc "I'll use my get out of jail free card here on..."
    mc "Mina."
    mina "Huuuuh? {i}Meeee{/i}?"
    scene pr0720 with dissolve
    mina "You just picked me to be mean."
    scene pr0721 with dissolve
    mina "Whatever!"
    mina "I got this piece of cake!"
    scene pr0723 with dissolve
    mina "Here I go..."
    scene pr0722 with dissolve
    "..."
    scene pr0723 with dissolve
    mina "One..."
    scene pr0722 with dissolve
    "..."
    scene pr0723 with dissolve
    mina "Two..."
    scene pr0722 with dissolve
    "..."
    scene pr0723 with dissolve
    mina "Three..."
    scene black with fade
    "..."
    mina "Sixteen...!"
    scene pr0724 with dissolve
    mina "Nope... this is making me dizzy."
    kil "We can just... call that twenty."
    jump prAfterParty4



label prAfterPartyPushUpFelicia:

    scene pr0726 with dissolve
    mc "I'll use my get out of jail free card here on..."
    mc "Felicia."
    scene pr0727 with dissolve
    fel "You just want to see me sweat, don't you?"
    scene pr0733 with blinds
    fel "Keep count for me, [mcf]."
    scene pr0734 with dissolve
    "..."
    scene pr0733 with dissolve
    mc "One..."
    scene pr0734 with dissolve
    "..."
    scene pr0733 with dissolve
    mc "Two..."
    scene pr0734 with dissolve
    "..."
    scene pr0733 with dissolve
    mc "Three..."
    scene black with fade
    "..."
    "Twenty...!"
    scene pr0735 with dissolve
    fel "Enjoy the show?"
    "..."
    jump prAfterParty4

label prAfterParty4:
    scene pr0736 with fade
    fel "Okay, back to me."
    scene pr0737 with dissolve
    kil "You and Mina must take a drink."
    mina "Awww..."
    scene pr0725 with fade
    mina "Gh..."
    scene pr0738 with dissolve
    mina "Man, I'm not feeling too swift..."
    mina "I think I'm about tapped out..."
    scene pr0739 with dissolve
    "..."
    scene pr0740 with fade
    mina "That's...?"
    kil "The suicide glass..."
    mina "FRICK!"
    mina "I just had to say that, didn't I?"
    kil "You know, we can just skip that one..."
    scene pr0741 with dissolve
    mina "No! I'm a team player!"
    scene pr0742 with dissolve
    fel "I don't think that's a--"
    scene pr0743 with dissolve
    mina "Don't ever let it be said I bitch out."
    scene pr0744 with dissolve
    "Glug... guhg... gluh..."
    scene pr0745 with dissolve
    "......"
    "..."
    scene pr0746 with dissolve
    "..."
    scene pr0747 with dissolve
    stop music fadeout 3.0
    kil "I think we should call it a night. What do you say?"
    scene pr0748 with dissolve
    mina "What, why? I-I can sthill go..."
    scene pr0747 with dissolve
    kil "I know you can, but it's more like WE can't keep up with you."
    kil "So how about we say you win and I'll tuck you in for the night?"
    scene pr0749 with fade
    mina "...mmmh, that soundsh nice~!"
    scene pr0750 with dissolve
    kil "Apologies for the abrupt ending."
    kil "You two are obviously free to spend the night if you'd like."
    scene pr0752 with dissolve
    mct "(It's already 2 AM...)"
    "I've got a final in 11 hours. Walking home drunk doesn't sound fun, and if I wait until morning, I guess I can get Ian to drive me back to my apartment so I don't have to waste money on a cab..."
    scene pr0753 with dissolve
    mc "Thanks, I think I'll do that."
    kil "See you in the morning then! Help yourself to anything in the fridge!"
    scene pr0754 with fade
    fel "..."
    scene pr0755 with dissolve
    fel "{b}Sooooo...{/b}"
    scene pr0756 with dissolve
    play music "music/helping-hands.mp3"
    "With zero subtlety, Felicia leaned into me, pushing her pert mounds firmly into the naked flesh of my arm."
    fel "It's just YOU and ME, stud..."
    scene pr0757 with dissolve
    mc "...you spending the night too?"
    scene pr0758 with dissolve
    fel "No, I should get going soon, but before I leave..."
    scene pr0759 with dissolve
    fel "Between the alcohol and you staring at my tits all night, I'm feeling a little fired up..."
    fel "What do you say we have some fun before I go?"
    hide screen textbox2 with dissolve

    menu:
        "Accept Felicia's advances. [gr]\[Felicia +2\]":
            $ Felicia_Affection += 2
            $ Felicia_Affection = clamp(Felicia_Affection, 0, 40)
            $ feliciaSex = True

        "Put an end to this before it goes too far. [red]\[Felicia -5\]":
            $ Felicia_Affection -= 5
            show screen textbox2 with dissolve
            jump prAfterPartyEndNoFun

    scene pr0760 with dissolve
    show screen textbox2 with dissolve
    "I would've thought the growing stiffness in my crotch as Felicia ran the palm of her hand down it's length would've answered her question."
    mc "What do you think?"
    fel "I think I'm going to have to see for myself."
    scene pr0761 with fade
    fel "Hmmm... I'll take that as an emphatic yes."
    scene pr0763 with dissolve
    "Felicia gave the tip of my glans an exploratory lick."
    scene pr0761 with dissolve
    fel "...how does that feel?"

    if toughness >= 20:
        scene pr0762 with dissolve
        mc "It feels fucking amazing. Do it again."
    else:
        scene pr0762 with dissolve
        mc "I don't know, I think I'm gonna need you to do that again."

    scene pr0764 with dissolve
    "*Chup!*"
    "This time, she gave the crown of my cock a quick, teasing kiss."
    scene pr0761 with dissolve
    fel "You want me to suck your huge cock, is that it?"
    hide screen textbox2 with dissolve
    menu:
        "Humor her. [gr]\[Felicia +1\]":
            $ Felicia_Affection += 1
            $ Felicia_Affection = clamp(Felicia_Affection, 0, 40)
            show screen textbox2 with dissolve
            scene pr0762 with dissolve
            mc "What do you think?"
            scene pr0761 with dissolve
            fel "I want to hear you say it."
            scene pr0762 with dissolve
            mc "...I would {b}love{/b} if you wrapped those plush, gorgeous lips around my dick and suck my cock."
            scene pr0761 with dissolve
            fel "What a way with words. It would be my pleasure, stud."

        "Urge her to hurry up. [red]\[Felicia -1\]":
            $ Felicia_Affection -= 1
            $ Felicia_Affection = clamp(Felicia_Affection, 0, 40)
            show screen textbox2 with dissolve
            scene pr0765 with dissolve
            mc "Just hurry up and get those lips around my cock, okay?"
            scene pr0766 with dissolve
            fel "Tsk, tsk, tsk, you're being an impatient boy, [mcf]."

    scene pr0767 with fade
    "Where she had previously relished in teasing me, Felicia had fully switched gears now. She had taken me in her mouth without hesitation, fully enveloping my entire length in one quick motion."
    "For a few seconds, she held it there at the base, like the personal flourish of an artist, before she commenced bobbing her head up in down in rapid, violent succession."
    scene pr0768 with dissolve
    scene pr0769 with dissolve
    "*Slurp... chup... fwup...*"
    scene pr0768 with dissolve
    scene pr0767 with dissolve
    "To call it a blowjob or even a facefucking would be inadequate."
    scene pr0768 with dissolve
    scene pr0769 with dissolve
    "*Fwup... slurp...*"
    scene pr0768 with dissolve
    scene pr0767 with dissolve
    "No, instead of crudely allowing me to hammer away at her throat, she was in full control of her technique."
    scene pr0768 with dissolve
    scene pr0769 with dissolve
    "*Slurp... chup...*"
    scene pr0768 with dissolve
    scene pr0767 with dissolve
    "Every pass, she flicked her tongue across the underside of my glans, before attentively twisting it down my length in full. It was like she was making sure not a single inch of my dick was deprived of her artful touch."
    scene pr0768 with dissolve
    scene pr0769 with dissolve
    "*Chup... fwup...*"
    scene pr0770 with dissolve
    "Suddenly, as she reached the zenith of her practiced motion, she allowed her mouth to slip off the head of my cock and exposed it to the cool summer air."
    "The sudden shift wasn't wholly unpleasant, but before I could even begin to miss the warmth of her mouth, she replaced it with a different kind of friction."
    scene pr0771 with dissolve
    scene pr0772 with dissolve
    scene pr0771 with dissolve
    scene pr0772 with dissolve
    fel "Tell me that wasn't the best dick sucking you've ever experienced."
    "Considering she's in the driver seat here, who am I to disagree with the lady?"
    mc "Gh...! I'd be lying if I said it wasn't."
    fel "Just what I love hearing."
    stop music
    play sound "sound effects/record-scratch.wav"
    scene pr0775 with pushright
    kil "I thought I'd bring you a pillow and blanket, but... damn!"
    kil "You guys didn't waste any time."
    "Thanks to Killian's sudden appearance, Felicia had stopped what she was doing and turned her focus on Ian."
    mct "({b}--Damn it!{/b})"
    scene pr0776 with dissolve
    fel "How's Mina?"
    "Felicia was seemingly unperturbed by Killian's interjection and carried on as if getting caught with a dick in your hand was business as usual."
    kil "She went out like a light once I put her to bed."
    scene pr0777 with dissolve
    mc "......"
    mc "..."
    mc "Ahem..."
    hide screen textbox2 with dissolve
    menu prAfterPartySexSplit:
        "Ask for some privacy [red]\[Killian -1\]":
            $ Killian_Bromance -= 1
            $ Killian_Bromance = clamp(Killian_Bromance, 0, 40)
            show screen textbox2 with dissolve
            scene pr0778 with dissolve
            mc "Would you mind giving us a little privacy?"
            scene pr0779 with dissolve
            kil "Sure, but if you want privacy... maybe don't start getting your dick sucked in someone's else living room, eh?"
            scene pr0780 with dissolve
            kil "{b}Kidding!{/b} I get it, I'm killing the mood. I'll leave these here."
            kil "You two have fun."

        "Ask him if he wants to join in on the fun. [gr]\[Killian +3\]" if Killian_Bromance >= 18:
            $ Killian_Bromance += 3
            $ Killian_Bromance = clamp(Killian_Bromance, 0, 40)
            show screen textbox2 with dissolve
            "I don't know what came over me, but instead of asking for privacy a kinky idea took root in my brain and I allowed it to flower."
            scene pr0781 with dissolve
            play music "music/love-or-lust.mp3"
            mc "...you want to join us?"
            kil "For real? This coming from {i}you{/i} of all people?"
            mc "I don't mind if Felicia doesn't."
            scene pr0782 with fade
            mc "What do you say, Felicia? Think you can handle both of us?"
            fel "I don't know, it sounds fun, but Mina's in the other room."
            fel "If she walked in on her boyfriend spit-roasting me..."
            fel "She'd be destroyed."
            scene pr0783 with dissolve
            kil "Aw, come on. She's dead to the world, there's no risk of that."
            kil "Besides... you owe me for that favor I'm doing you, remember?"
            scene pr0784 with dissolve
            mct "(...favor?)"
            fel "..."
            scene pr0785 with dissolve
            fel "Alright, alright... {b}fine{/b}."

            jump prAfterPartyThreesome



        "{color=#696969}Ask him if he wants to join in on the fun.{/color=#696969}" if Killian_Bromance <= 17:
            show screen textbox2 with dissolve
            "I don't feel close enough to Ian to ask him that."
            hide screen textbox2 with dissolve
            jump prAfterPartySexSplit

label prFelAfterPartyFun:

    if _in_replay:
        show transitionfelicia02 with cmet
        show screen textbox2 with dissolve
        "Please set [mcf]'s personality (toughness score) for this replay."
        hide screen textbox2 with dissolve
        menu:
            "Nice guy (Toughness: 0)":
                $ toughness = 0
            "Mischevious (Toughness: 18)":
                $ toughness = 18
            "Asshole (Toughness: 30)":
                $ toughness = 30
        show screen textbox2 with dissolve

    scene pr0786 with fade
    fel "Well, well, well..."
    "Without missing a beat, and with her libido seemingly unhampered by the intrusion, Felicia turned her attention back toward me."
    fel "Now where were we?"
    mc "You were boasting about the best blowjob I've ever had, but..."
    "This is my opportunity to take a more active role."
    scene pr0787 with dissolve
    play music "music/love-or-lust.mp3"
    fel "---wah!"
    fel "What are you doing?"
    mc "I may not be as skilled as you, but it'd be rude to not try to return the favor."
    "Surprisingly, Felicia's face went flush with what I assume to be embarrassment."
    mct "(That's fresh!)"
    "Considering her cocksure attitude, who would've thought wanting to eat her out would make the whore blush?"
    scene pr0788 with dissolve
    fel "Y-you don't have to do that. Most guys--"
    hide screen textbox2 with dissolve
    menu:
        "I want to. [gr]\[Felicia +1\]":
            $ Felicia_Affection += 1
            $ Felicia_Affection = clamp(Felicia_Affection, 0, 40)
            show screen textbox2 with dissolve
            "Without leaving any room for debate, I firmly told her my honest desires."
            scene pr0789 with dissolve
            mc "I want to."
            fel "..."
            scene pr0788 with dissolve
            fel "{size=-10}Ah, alright...{/size=-10}"

        "Shut up.":
            show screen textbox2 with dissolve
            scene pr0789 with dissolve
            mc "Shut the hell up, slut."
            "Mustering my best commanding tone, I tried my best to abate Felicia's hesitation."
            mc "You had your fun teasing me, now it's only fair I get to try my hand at pleasuring you."
            fel "..."
            scene pr0788 with dissolve
            fel "O-okay..."

    scene pr0790 with dissolve
    "Finally, that slight piece of cloth that had teasing me all night was gone."
    "And with it, Felicia seemed to shrink from a dynamo force-of-nature to just a vulnerable woman awaiting her partner's move."
    mct "(Shit, I suppose I've should be more appreciative to Ian.)"

    if roseTakeAdvantage == True:
        mct "(Counting Rosalind, that's twice I've had fun with a stunning woman for floating within his sphere.)"
    else:
        mct "(I'd never have had the chance to make it with a stunning woman like Felicia if it wasn't for him.)"

    mc "You hear this all the time I bet, but... you're beautiful, Felicia."
    scene pr0791 with dissolve
    fel "... just shut up and get the fuck down there, stud."
    "Done with the talking, I lifted Felicia's long, gorgeous legs and brought my face close to her pelvis."
    scene pr0792 with dissolve
    "I started by rolling my tongue over her clit, drawing from Felicia a small murmur of pleasure, and lathering it up generously with saliva until it had rolled down to mix with her own juices."
    scene pr0793 with dissolve
    "Satisfied she was ready for it, my tongue found it's way into Felicia's depths, stretching deep and wide, lashing against her inner walls."
    fel "S-shit--!"
    fel "You said you weren't good at this!"
    scene pr0794 with dissolve
    fel "Ah... hah... --eh."
    "*Schlick, schlup...!*"
    fel "That's... that's..."
    "*Schlick, schlup...!*"
    "Those small murmurs of pleasure eventually crescendoed into more enthusiastic, affirming demands to continue."
    fel "Fuck! Don't stop!"
    "Schlick, schlup...!*"
    scene pr0795 with dissolve
    "I had managed to break the floodgates, as Felicia was by this time positively flowing with juices that I lapped up with every pass."
    "*Schlick, schlup...!*"
    "Felicia's breath had quickened to panting by this point, and though I couldn't see it, the thought of her pert golden breasts rising and falling in response to my efforts had me wanting to explode."
    "*Schlick, schlup...!*"
    fel "Yes... yes!"
    "Meanwhile, Felicia was working in tandem with my probing, desperately extending her pelvis more and more to get my tongue to reach even greater depths."
    mct "(If she wants me to go deeper, I can go deeper!)"
    scene pr0796 with fade
    fel "Aaah -- oh!"
    "Putting a momentary stop to the fun (and taking the chance to catch my breath), I grabbed hold of Felicia's ankles and threw her legs in the air."
    fel "What are...?"
    mc "I'm going to taste every inch of your cunt, slut."
    scene pr0797 with dissolve
    "It was a stupid claim, the kind of nonsensical shit you say in the throes of passion, but part of me actually wanted to try."
    "*Schlick, schlup...!*"
    "This new angle gave me access to all kinds of new ways to probe and torment Felicia's inner depths."
    fel "Shit. Shit! {b}Shit!{/b}"
    "*Schlick, schlup...!*"
    "And she seemed to taken to it as well."
    "*Schlick, schlup...!*"
    fel "Ah! You dumb bastard. You... -ah!- you!"
    "If not from the full body quakes, I could she was getting close as her explicatives became decreasingly verbose."
    fel "I'm... I'm..."
    scene pr0798 with flash
    with flash
    with flash
    fel "{b}Aaaaaeeeeh~!!!{b}"
    "....."
    "..."
    scene pr0799 with blinds
    mc "*Huff... huff....*"
    "For awhile, the room was a simple mixture of our labored breathing, with me content in the knowledge that I was able to bring a vivacious woman like Felicia to orgasm."
    mct "(I'm on top of the fucking world!)"
    scene pr0800 with dissolve
    "...there's still one matter though. I'm hard as fuck and ready to pop."
    "I needed to cum, like yesterday."
    "Felicia, while still insensate in a puddle of post-orgasm bliss, would doubtlessly be receptive to me finishing what she originally started."
    "I'm going to..."
    hide screen textbox2 with dissolve
    menu:
        "Cum deep in her throat!":
            show screen textbox2 with dissolve
            jump prAfterpartyCumTwosome
        "Take care of it yourself and cum on her face.":
            show screen textbox2 with dissolve
            jump prAfterPartyCumSolo

label prAfterpartyCumTwosome:
    scene pr0801 with dissolve
    stop music fadeout 3.0
    "This started with a blowjob, it's going to end with a blowjob."
    fel "...huh? I know you still haven't cum, but my body is like butter, stud. I don't know what good I'll be."
    mc "Oh, don't worry. You don't need to be very active."
    scene pr0802 with dissolve
    play music "music/leaving-home.mp3"
    fel "--!"

    if toughness >=20:
        "I'm going to fuck your face and blow my spunk straight down your whore throat."
        scene pr0803 with dissolve
        fel "Oh... I like the sound of that."
        scene pr0802 with dissolve
        mc "Then lay your head back and open up, slut."


    else:
        "Just relax your jaw and I'll do all the work."
        scene pr0803 with dissolve
        fel "You're going to use me like a toy...?"
        fel "I like the sound of that."

    scene pr0804 with dissolve
    fel "Aaah~"
    "With Felicia on the same page, seemingly eager to act as toy to slake my lust, I knew I didn't have to show restraint."
    "Which was {b}perfect{/b}. I hadn't planned to."
    scene pr0805 with dissolve
    "Felicia's welcoming maw readily accepted the length of my member, my cock easily gliding past her tongue until it hit a road block: the back of her throat."
    "As I'd learned previously, Felicia had no gag reflex to speak, but the sudden knocking did cause her to tense up and slightly sputter uncomfortably."
    "In response, I let a few peaceful moments pass, my cock sheathed in the warm embrace of her mouth, allowing her to adjust to my length."
    scene pr0806 with dissolve
    "Tilting her head back to get a good angle of attack, I rolled my hips back and commenced my assault."
    scene pr0805 with dissolve
    "Rather than try to expel the foreign object, Felicia's throat took the sudden intrusion effortlessly, pliantly conforming to the size and shape."
    scene pr0806 with dissolve
    fel "*Guhg... slap... guhg...*"
    scene pr0805 with dissolve
    mct "(Fuck, this feels amazing...!)"
    scene pr0806 with dissolve
    fel "*Slap... slap... guhg...*"
    scene pr0805 with dissolve
    "Every pass brought my member from Felicia's mouth to the depths of her throat and back again, creating a symphony of protracted wet noises as my dick slide past her tongue and my balls battered against her chin."
    scene pr0806 with dissolve
    "Having the golden beauty submissively letting me abuse her mouth hole to my heart's content elicited something primal in me."
    scene pr0805 with dissolve
    fel "*Guhg... guhg...*"
    scene pr0806 with dissolve
    "A feeling of bile was building up in the pit of my stomach."
    scene pr0805 with dissolve
    "I wanted to {i}thoroughly{/i} ruin Felicia. I wanted to leave her gasping and clawing for air."
    scene pr0806 with dissolve
    "Spurred on by these thoughts, I doubled my efforts, transforming my measured thrusts into a full-on rut."
    scene pr0808 with dissolve
    fel "Ngggh--!"
    "Felicia's hands pawed at my backside in surprise at the sudden change in tempo."
    scene pr0807 with dissolve
    fel "*{b}GLUHG... GUHG... GUHG...{/b}*"
    scene pr0808 with dissolve
    "...but rather than panic, she quickly adapted to the frenzied pace, doing her best to suck in gasping breaths of air on my down-thrusts."
    scene pr0807 with dissolve
    fel "Glug... slap... slap"
    scene pr0808 with dissolve
    mc "Ah...!"
    scene pr0807 with dissolve
    "As my orgasm built, so did my urge to lay down a little dirty talk."
    hide screen textbox2 with dissolve

    menu:
        "Tell her how you feel. [gr]\[Toughness +1\] \[Felicia +1\]":
            $ toughness += 1
            $ toughness = clamp(toughness, 0, 30)
            $ Felicia_Affection +=1
            $ Felicia_Affection = clamp(Felicia_Affection, 0, 40)
            show screen textbox2 with dissolve
            scene pr0808 with dissolve
            mc "You fucking cunt!"
            scene pr0807 with dissolve
            fel "Guhg... gluhg... gug..."
            mc "To be this good at taking a dick...ngh!"
            scene pr0808 with dissolve
            mc "You let every guy fuck your vapid, whore face don't you?"
            fel "{b}Mmmhh--! Mhh!{/b}"

        "Keep your dirty thoughts to yourself. [red]\[Toughness -1\]":
            $ toughness -=1
            $ toughness = clamp(toughness, 0, 30)
            pass

    scene pr0807 with dissolve
    "Finally, that familiar feeling of near-impeding orgasm was reaching it's peak."
    scene pr0808 with dissolve
    "Without abandon, as if I could get her mouth pregnant, I instinctively lurched my hips forward as deep as they'd go."
    scene pr0809 with dissolve
    "Pressing my crotch hard against Felicia's nose and her head deep into the couch, I reached my climax."
    play sound "sound effects/spurt.wav"
    mc "Take it, you bitch--!" with flash
    play sound "sound effects/spurt.wav"
    "Planted firmly in the confines of Felicia's windpipe, I deposited rope..." with flash
    play sound "sound effects/spurt.wav"
    scene pr0810 with dissolve
    "...after rope, straight down her throat."
    "Meanwhile, Felicia was doing her best to suck up everything I had to give her, but to no avail."
    "Some spilled out around the frays of her mouth, mixing with saliva, and forming spittle around the base of my cock."
    scene pr0811 with dissolve
    "{b}*Plop!*{/b}"
    "After some gentle rocking to wring out the last drops of cum from my urethra, I lazily withdrew my penis with a loud plop."
    "The gorgeous woman before me had turned into a mess."
    "Cum dripped out from the recesses of her mouth. Her carefully applied makeup ruined, gulping down air like a fish out of water..."
    scene pr0812 with dissolve
    "Her eyes couldn't quite seem to keep focus on anything."
    stop music fadeout 3.0
    mc "Uh... you okay, Felicia?"
    fel "*Huff... huff...!*"
    fel "Y-yeah..."
    scene pr0813 with dissolve
    fel "Holy shit, you gave it to me good."
    fel "You were an absolute beast."
    mc "I didn't take it too far, did I?"
    fel "No... huff... That was just the way I like it, stud."
    fel "...but give me a minute to catch my breath, yeah...?"
    scene black with fade
    "Felicia and I sat there in silence for awhile as she regained her composure. After enough time had passed, she cleaned up and I saw her off."
    $ renpy.end_replay()
    jump prAfterPartyTwosomeGoodNight

label prAfterPartyCumSolo:

    if toughness >= 20:
        scene pr0814 with dissolve
        "No need for a half-assed blowjob, I'll be content just to mark the slut as my own."
    elif toughness >= 11:
        scene pr0814 with dissolve
        "Honestly, I'll settle with painting Felicia in my spunk."
    else:
        scene pr0814 with dissolve
        "Why bother Felicia? I can take care of it myself."

    scene pr0815 with dissolve
    fel "...huh? I know you still haven't cum, but my body is like butter, stud. I don't know what good I'll be."
    scene pr0816 with dissolve
    if toughness >= 20:
        scene pr0817 with dissolve
        mc "That's fine. All I need you to do is lay there and be my cum rag."
    else:
        scene pr0817 with dissolve
        mc "That's fine. All I want you to do is lay there and take my jizz."
    scene pr0816 with dissolve
    scene pr0817 with dissolve
    scene pr0818 with dissolve
    fel "Just lay here while you jerk your fat cock?"
    scene pr0819 with dissolve
    fel "Mmhh, I do like the sound of that."
    "With my hand sliding up and down my dick, I moved to position myself above Felicia while building up speed, fully engrossed in the sight her of sun-kissed, well-toned figure."
    scene pr0818 with dissolve
    "For some time, Felicia and I shared in a lust-charged silence, her eyes firmly planted on my engorged cock, my head swimming in all the things I'd like to do to her if given half a chance."
    scene pr0819 with dissolve
    "Thoughts of giving and sharing in pleasure, of exploring and reveling in every detail of Felicia's beauty."
    scene pr0818 with dissolve
    "...but also, darker ones. Buried underneath those innocuous fantasies lurked something more brazen. I wanted to torment, tease, and ruin her."
    scene pr0819 with dissolve
    "With these thoughts, and with how worked up she had me previously, I knew it wouldn't be long before I blasted a load onto Felicia's eager face or tits."
    scene pr0820 with dissolve
    fel "Mmmh..."
    "Having recovered from her tongue-fucked reverie, Felicia's growing mewling pulled me from my fantasies back to reality."
    fel "Fuck, watching you stroke that monster..."
    fel "It's getting me so hot."
    scene pr0821 with dissolve
    "Meanwhile, Felicia snaked a hand down to her crotch and began touching herself."
    scene pr0820 with dissolve
    fel "If I didn't have to leave, I would ride that thing until morning."
    scene pr0821 with dissolve
    fel "Give me that big, FAT wad, stud."
    scene pr0820 with dissolve
    "Felicia was becoming increasingly more vocal, in an effort for this not to be such a one-sided deal."
    if toughness > 20:
        "Something about her shrill voice repeating fake, distracting porn-star like lines ad nauseam was taking me out of the moment and pissing me off, but I was so close to cumming I didn't give a shit."
    scene pr0821 with dissolve
    mc "--ah, fuck! I'm almost there!"
    scene pr0820 with dissolve
    mc "Where should I cum--?"
    scene pr0821 with dissolve
    fel "Cum wherever you want, baby!"
    "Anywhere?"
    "I desperately wanted to drown her beautiful, radiant face in my jizz."
    mc "Open up, slut!"
    scene pr0822 with dissolve
    mc "That did it!"
    scene pr0823 with dissolve
    play sound "sound effects/spurt.wav"
    mc "-----!" with flash
    scene pr0824 with dissolve
    "Rope after rope of jizz exploded from my urethra and onto Felicia's whorish countenance." with flash
    scene pr0825 with dissolve
    mc "Good girl!" with flash
    mc "Hngh... hunh..."
    scene pr0826 with dissolve
    "Giving my dick just a few more lethargic strokes to make sure I had deposited every last drop of semen, I took a second to admire my handiwork."
    mct "(Beautiful!)"
    "Felicia's once golden face was now coated with an incredibly think layer of spunk."
    mct "(Shit, I didn't know I had all that in me...)"
    fel "Mmmh!"
    scene pr0827 with dissolve
    fel "I made you cum that much? I'm glad."
    fel "That means you you were really into it - into {i}me{/i}."
    fel "...uh, do you think you could hand me a towel? I don't want to make an even bigger mess."
    stop music fadeout 3.0
    scene black with fade
    "After cleaning up and getting dressed, Felicia and I spent a few minutes idly chattering until it was finally time for her to leave."
    $ renpy.end_replay()
    jump prAfterPartyTwosomeGoodNight

label prAfterPartyTwosomeGoodNight:

    scene pr0867 with blinds
    if not persistent.felAfterPartyGallery:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.felAfterPartyGallery = True
    fel "Thanks for showing a girl a good time, lover."
    scene pr0868 with dissolve
    play sound "sound effects/notification.wav"
    $ history_felicia = "A beautiful woman Ian help set me up with, she got pretty handsy and we ended up fooling around on Ian's couch. Needless to say, I hope to see her again sometime."
    $ met_felicia = True
    show bioadd with dissolve
    $ renpy.pause(3, hard=True)
    scene pr0867 with dissolve
    mc "After all that, I should be the one thanking you."
    fel "Maybe I'll see you again?"
    mc "I'd like that."
    fel "Then see you around, stud."

    play sound "sound effects/door-openclose.wav"
    scene black with fade
    "With that Felicia left me alone, and the radiant warmth of her presence was quickly replaced by the sole drum of the open city air and a heavy tiredness beckoning me to sleep."
    scene pr0869 with dissolve
    mct "(I'm gonna regret all this drinking in the morning, but damn if it wasn't worth it...)"
    scene black with fade
    "....."
    "..."
    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionfelicia04 with blinds
    $ renpy.pause(6, hard=True)
    jump prDiscoAftermath

label prAfterPartyThreesome:

    if _in_replay:
        show transitionfelicia03 with cmet
        show screen textbox2 with dissolve
        "Please set [mcf]'s personality (toughness score) for this replay."
        hide screen textbox2 with dissolve
        menu:
            "Nice guy (Toughness: 0)":
                $ toughness = 0
            "Mischevious (Toughness: 18)":
                $ toughness = 18
            "Asshole (Toughness: 30)":
                $ toughness = 30
        show screen textbox2 with dissolve

    scene pr0828 with dissolve
    scene pr0829 with dissolve
    mc "...but, uh, what do we do?"
    "Despite being the one who shamelessly suggested it, it was a new experience for me. The logistics... who stands where, who starts what..."
    scene pr0830 with dissolve
    kil "Keep doing what you were doing and don't mind me."
    fel "Huh? You're not going to join in?"
    kil "Not yet, no."
    scene pr0831 with dissolve
    kil "Why don't you two put on a show and give me a bit of a jump start?"
    fel "So, you like to watch? That explains a few things."
    kil "What photographer doesn't?"
    mct "(Hmm...)"
    "Taking advantage of the lull in conversation, I seized the opportunity to be the one to set the pace."
    scene pr0832 with fade
    fel "--Ooh!"
    fel "Someone's getting impatient--mhhna!"
    scene pr0833 with dissolve
    "*Chup... fwup...*"
    "*Fwup... fwup... chup...*"
    "*Chup... chup...*"
    scene pr0834 with dissolve
    fel "Nggh-! S-shit!"
    fel "That feels... that feels...!"
    fel "~{b}Good♥~!{/b}"
    scene pr0835 with dissolve
    fel "You're a bigger fucking pervert than I gave you credit for, Ian."
    scene pr0834 with dissolve
    fel "Jerking that fat cock, watching me and your friend go at it."
    scene pr0835 with dissolve
    fel "All with your girlfriend just in the other room..nyaa!"
    scene pr0834 with dissolve
    kil "That last bit makes me sound like an asshole, you know."
    mct "(...but you ARE an asshole.)"
    "Resisting the urge to get a jab in at Ian's expense, I instead doubled my attention on Felicia."
    mc "Let's see how wet you are down here...."
    scene pr0836 with dissolve
    fel "Mmmh-!"
    "*Chup... fwup...*"
    "*Fwup... fwup... chup...*"
    "*Chup... chup...*"
    scene pr0837 with dissolve
    fel "Engines finally primed, stud?"
    stop music fadeout 3.0
    kil "Hmpph. You haven't seen nothing yet, bitch."
    kil "Grab her legs, [mcf]."
    scene pr0838 with fade
    play music "music/leaving-home.mp3"
    fel "...huh?"
    "Without hesitation, I followed his direction."
    fel "Whaah?"
    "Whatever Ian had planned, I knew it was going to be good."
    scene pr0839 with dissolve
    kil "You got a pretty cunt, Felicia. But it's looking a bit neglected."
    fel "Wh-what are you doing?"
    scene pr0840 with dissolve
    kil "I'm going to give your pussy some personal attention."
    fel "A toy...? I want the real thing--"
    scene pr0841 with dissolve
    fel "Oew!"
    kil "That's the problem with you, Felish. You never take the time to smell the roses."
    scene pr0842 with dissolve
    scene pr0841 with dissolve
    scene pr0842 with dissolve
    "With a big, shit-eating grin on his face, Ian unceremoniously started maneuvering the toy."
    scene pr0841 with dissolve
    "At first, he tested waters with short, shallow thrusts. Applying all kinds of twists and flourishes in effort to draw out a pleasurable response from the woman in my arms."
    scene pr0842 with dissolve
    scene pr0841 with dissolve
    kil "You want to know a secret about our girl here, [mcf]?"
    scene pr0843 with dissolve
    mc "A secret? Sure."
    scene pr0841 with dissolve
    kil "She ain't as experienced as she lets on."
    scene pr0841 with dissolve
    kil "I mean sure--"
    scene pr0842 with dissolve
    "As if to punctuate his point, Ian magnified his efforts, sending the ice blue toy haphazardly barreling into Felicia's soppy, clutching quim."
    scene pr0841 with dissolve
    kil "She's fucked a lot, and she's real good at it, but..."
    scene pr0844 with dissolve
    "While Killian rattled on candidly as if Felicia wasn't even here, a soft and warm sucking sensation brought my attention back to the woman in my arms."
    "Felicia had latched onto my thumb in an lusty fugue, sucking on it greedily."
    scene pr0845 with dissolve
    fel "Mmmh--oh!"
    scene pr0844 with dissolve
    kil "She's hasn't quite learned the pleasure of taking a backseat in things."
    scene pr0845 with dissolve
    kil "I guess fucking old men for fortunes means you get use to doing all the work."
    scene pr0844 with dissolve
    fel "Niii...!"
    "By now, all critical thought had left Felicia's skull, fucked out of her through Killian's ferocious assault."
    scene pr0845 with dissolve
    fel "Gaa-gghaa~!"
    scene pr0844 with dissolve
    fel "Fuck... fuck ... FUCK!"
    scene pr0845 with dissolve
    "In short order, Killian had skillfully brought Felicia on the cusp of cumming."
    scene pr0846 with dissolve
    "Then he stopped."
    fel "Wha--wha..."
    fel "Why did you stop, you prick? I was almost there."
    stop music fadeout 3.0
    kil "You haven't earned it yet."
    scene pr0847 with dissolve
    fel "I haven't EARNED it? What the fuck is that shit, Ian?"
    fel "Fuck off!"
    kil "Relax, I was only kidding."
    kil "It was just dirty talk, y'see..."
    fel "Well you fucking killed the mood. Let go of me, [mcf]."
    mc "R-right..."
    scene pr0848 with fade
    play music "music/thief-in-the-night.mp3"
    kil "Sorry, Felish. I didn't think..."
    fel "It's whatever."
    scene pr0849 with dissolve
    fel "Sorry, [mcf]. You didn't do anything wrong, but I'm not feeling it anymore. Blame Ian for the blue balls."
    fel "It's late anyway. I should go anyway."
    scene black with fade
    "Frustrated at being left high and dry so suddenly, all I could do was sit there in silence as Felicia got dressed and began to leave."
    $ renpy.end_replay()
    if not persistent.felDiscoThreesomeGallery:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.felDiscoThreesomeGallery = True
    scene pr0850 with dissolve
    kil "Same time next week, Felicia?"
    scene pr0851 with dissolve
    fel "..."
    scene pr0852 with dissolve
    fel "...yeeeeah."
    scene pr0853 with dissolve
    "With that Felicia had left, leaving me alone with Ian."
    mc "......"
    kil "..."
    hide screen textbox2 with dissolve
    menu:
        "Thanks for the blueballs. [gr]\[Killian +1\]":
            $ Killian_Bromance += 1
            $ Killian_Bromance = clamp(Killian_Bromance, 0, 40)
            show screen textbox2 with dissolve
            scene pr0854 with dissolve
            mc "Thanks for the blueballs, dick."
            scene pr0855 with dissolve
            kil "Pfffhahaha!"

        "What's her deal?":
            show screen textbox2 with dissolve
            scene pr0854 with dissolve
            mc "What's her problem?"

    scene pr0856 with dissolve
    kil "Sorry, sorry! I thought she'd totally go for the 'ask permission to cum' shtick."
    kil "Even if she wasn't into it, she didn't have to blow a gasket. She's usually pretty cool."
    scene pr0857 with dissolve
    kil "It does kinda remind me of when I blew your chance with Marlow in high school. Remember that?"
    mc "..."
    scene pr0858 with dissolve
    mc "We're not having at heart to heart with your junk hanging out, dude."
    scene pr0859 with dissolve
    kil "Hahaha, fair enough."
    scene pr0860 with dissolve
    kil "Well, it's late and we're both drunk. The pillow and blanket are over there."
    scene pr0861 with dissolve
    scene pr0862 with dissolve
    scene pr0863 with dissolve
    kil "Probably don't mention this to Mina..."
    scene pr0864 with dissolve
    mc "What? That you and me almost double-teamed her friend? Probably won't come up."
    scene pr0863 with dissolve
    kil "Good, good."
    scene pr0865 with dissolve
    kil "Well, good night. I'm glad you came out with me tonight. It's always good to see you bro."
    scene pr0866 with dissolve
    mc "Pffft-hahahhahaha!"
    "With Killian gone, I couldn't help but laugh."
    "Considering all the crazyness, him ending it on such a bro-y note was the perfect bookend for the night."
    scene pr0869 with blinds
    mct "(I'm gonna regret all this in the morning...)"
    play sound "sound effects/notification.wav"
    stop music fadeout 3.0
    $ history_felicia = "A beautiful woman Ian help set me up with, things got hot and heavy by the end of the night between the three of us, but Ian ruined it. I hope she doesn't hold that against me."
    $ met_felicia = True
    show bioadd with dissolve
    $ renpy.pause(3, hard=True)
    scene black with fade
    "....."
    "..."
    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionfelicia04 with blinds
    $ renpy.pause(6, hard=True)
    jump prDiscoAftermath


label prAfterPartyEndNoFun:
    scene pr0870 with dissolve
    mc "Sorry, but... no thanks."
    mc "You're an incredibly sexy woman, but..."
    scene pr0871 with dissolve
    fel "No thanks? You GOTTA be kidding me..."
    "Before I could even get the words fully out, Felicia had flipped from her pleasant come hither demeanor to one of visible frustration. She's clearly not used to being turned down."
    scene pr0872 with dissolve
    fel "You've been staring at my tits all night!"
    fel "You're telling me you don't want a piece of THIS?"
    hide screen textbox2 with dissolve
    menu:
        "It's not that I don't find you attractive, but... [gr]\[Felicia +1\]":
            $ Felicia_Affection += 1
            $ Felicia_Affection = clamp(Felicia_Affection, 0, 40)
            show screen textbox2 with dissolve
            if toughness > 20:
                scene pr0873 with dissolve
                mc "Jeez! Don't get your titties twisted."
            else:
                scene pr0873 with dissolve
                mc "Calm down!"

            mc "It's not like I don't WANT to. However, it's late, I'm drunk, and I've got an exam tomorrow afternoon."

        "No, I don't. [red]\[Felicia -1\]":
            $ Felicia_Affection -= 1
            $ Felicia_Affection = clamp(Felicia_Affection, 0, 40)
            show screen textbox2 with dissolve
            if toughness > 20:
                scene pr0873 with dissolve
                mc "Chill the fuck out."

            else:
                scene pr0873 with dissolve
                mc "Sorry, but I don't."

            mc "Not everyone is looking for a quick fuck."

    scene pr0874 with dissolve
    fel "..."
    fel "Sorry, I'm a bit... drunk."
    fel "I get it, I get it... you don't want to."
    fel "I know when I'm making an ass of myself. I guess I'll... go."
    "Felicia looked like a sad puppy dog. If this is a ploy on her part to make me feel bad, well..."

    if toughness > 18:
        mct "(Part of me DOES feel like a moron. A hot woman like Felicia wants to screw and I send her packing?)"
    else:
        mct "(It worked.)"

    scene black with fade
    "Felicia excused herself to get dressed, before poking her head out and to say good bye."
    scene pr0875 with blinds
    fel "I had a... good time, [mcf]."
    fel "It was nice meeting you."
    hide screen textbox2 with dissolve
    menu:
        "Likewise.":
            show screen textbox2 with dissolve
            scene pr0876 with dissolve
            mc "Likewise. I had fun."
            scene pr0875 with dissolve
            fel "Well, see you around, stud."

        "Kiss her goodbye.":
            show screen textbox2 with dissolve
            scene pr0876 with dissolve
            mc "Same, I don't get the chance to get out much. A night out with a beautiful woman was a nice change of pace."
            scene pr0877 with dissolve
            "Smooch."
            scene pr0876 with dissolve
            mc "We should do this again sometime."
            scene pr0875 with dissolve
            fel "Yeah, maybe..."
            fel "See you around, stud."

    play sound "sound effects/door-openclose.wav"
    scene black with fade
    "With that Felicia left me alone, and the radiant warmth of her presence was quickly replaced by the drum of the open city air and my drunkenness beckoning me to sleep."
    scene pr0869 with blinds
    mct "(I'm gonna regret all this in the morning...)"
    play sound "sound effects/notification.wav"
    $ history_felicia = "A beautiful woman Ian help set me up with, she was angry and hurt when I turned down her advances. Part of me feels like a fucking moron there."
    $ met_felicia = True
    show bioadd with dissolve
    $ renpy.pause(3, hard=True)
    scene black with fade
    "....."
    "..."
    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionfelicia04 with blinds
    $ renpy.pause(6, hard=True)
    jump prDiscoAftermath

label prAfterPartyCafe:
    "..."
    scene pr0878 with blinds
    play music "music/crinoline-dreams.mp3"
    "After leaving the club, I took Felicia to one of my usual haunts: Johnny's Dinner."
    scene pr0879 with wipeleft
    fel "Cute place. You come here often?"
    mc "Occasionally, I suppose."
    fel "Occasionally? The old fart behind the counter greeted you by name!"
    scene pr0880 with dissolve
    mc "Okay, okay..."
    mc "I've been coming in once a week, for a couple of years now."
    scene pr0881 with dissolve
    fel "That's more than occasionally!"
    scene pr0882 with dissolve
    waitress "Hey, [mcf]."
    mc "Hey, Susie."
    susie "It's rare to see you in here without a stack of textbooks."
    scene pr0883 with dissolve
    susie "What can I get you two?"
    fel "I'll have the hamburger. Well-done."
    scene pr0884 with dissolve
    susie "What about you, sweetie? The usual?"
    mc "That'll be fine, thank you."
    susie "I'll have it right out."
    scene pr0885 with dissolve
    mc "..."
    fel "..."
    scene pr0886 with dissolve
    mc "Soooo..."
    mc "This the way your dates usually go? Screw and then food?"
    scene pr0887 with dissolve
    fel "Date? Oh, you're cute."
    fel "I don't date anymore, but if I did, you couldn't afford to take me on one -- no offense."
    scene pr0888 with dissolve
    mc "What else would you call this?"
    scene pr0889 with dissolve
    fel "Two people fucking and eating?"
    mc "That's not a date to you?"
    scene pr0890 with dissolve
    fel "Don't get me wrong, I vastly prefer it to what I'd call a date."
    fel "This is fun. Dating, on the other hand, is shit."
    scene pr0891 with dissolve
    mc "Bad experiences?"
    scene pr0892 with dissolve
    fel "Quite the opposite actually. I'm really damn good at it and it's paid off in spades for me."
    scene pr0893 with dissolve
    mc "I'm not following. What makes it shit, then?"
    scene pr0894 with dissolve
    fel "It's because it's a soul-sucking charade."
    scene pr0895 with dissolve
    fel "It's smothering your personality, knowing when to look stupid, knowing when to laugh, and knowing when to bite your tongue."
    fel "It's starving yourself to fit into a size-0 dress and keeping up with topics I couldn't give a shit about."
    scene pr0894 with dissolve
    fel "It's killing your sense of self for a shot at security."
    scene pr0896 with dissolve
    mc "That's a cynical way of looking at romance. Isn't it just two people spending time together because they like each other?"
    scene pr0897 with dissolve
    fel "Pffft!"
    fel "Considering you're friends with Ian, you must've grown up well off, right? You wouldn't get it"
    scene pr0898 with dissolve
    mc "Actually, no. I didn't grow up rich."
    scene pr0895 with dissolve
    fel "Really? I know you're not as big as a douche as he is, but I had you pegged as being from the same stock."
    scene pr0897 with dissolve
    fel "I guess my talent for spotting rich boys is disappearing with age."
    scene pr0898 with dissolve
    mc "I mean, I didn't have it BAD. My mother, despite money being tight, had a knack for making every penny go far."
    mc "Still, NOT even close to Ian's wealth."
    scene pr0894 with dissolve
    fel "How'd you two become friends then?"
    scene pr0898 with dissolve
    mc "Ian would kill me if I told you."
    scene pr0899 with dissolve
    fel "You have to tell me then."
    scene pr0898 with dissolve
    mc "I don't know..."
    scene pr0897 with dissolve
    fel "You HAVE to tell me."
    scene pr0898 with dissolve
    mc "We met in public school."
    scene pr0899 with dissolve
    fel "Really? Our snobby Casanova went to a public school?"
    scene pr0898 with dissolve
    mc "Yep. Believe it or not, he used to be extremely withdrawn and shy."
    mc "He had trouble fitting in, so he begged and begged his parents to let him attend a government run school. We met, hit it off. The rest is history as they say."
    scene pr0900 with dissolve
    fel "Huh..."
    fel "I can't see it."
    scene pr0898 with dissolve
    mc "{b}Honest{/b}, but what about you?"
    mc "You said I wouldn't get it because I was well off, so does that mean...?"
    scene pr0901 with dissolve
    fel "Uh-huh. In another life, I grew up poor in a podunk town."
    scene pr0902 with dissolve
    mc "Security. I think I get what you mean."
    scene pr0901 with dissolve
    fel "Well, It's not rocket science."
    scene pr0903 with dissolve
    fel "That was fast!"
    scene pr0904 with dissolve
    susie "Just holler if you need anything else."
    scene pr0905 with fade
    fel "Aaaah..."
    fel "I miss burgers."
    scene black with fade
    "......"
    "..."
    scene pr0906 with dissolve
    fel "You done?"
    scene pr0907 with dissolve
    mc "Yeah, I don't like to eat when I'm drunk."
    scene pr0908 with dissolve
    fel "Huh? That's when you need to eat the most."
    scene pr0909 with dissolve
    fel "This is nice. Dancing and screwing - that's par for the course, but a greasy diner..."
    fel "That's a treat."
    scene pr0910 with dissolve
    "Come time to pay, Felicia firmly declared that she'd get the tab."
    "At first I wanted to insist otherwise, to at least let me pay for my own, but..."
    scene pr0911 with dissolve
    mct "(I'd never seen a black card in person before.)"
    mct "(Said she was poor, but she's fucking loaded now at least.)"
    "The chance to had passed thanks to my momentary gawking."
    scene pr0912 with dissolve
    fel "So, college aside, you do anything for money?"
    mct "(--!)"
    "It was a normal question: 'what do you do for work?' Still, it washed me over in a small wave of anxiety."
    "Come to think of it, I hadn't really thought about what I was going to tell people from now on."
    "I suppose I could just tell her I work as a tutor, which wouldn't be much of a lie. I still need to notify my clients and refer them to someone else after all."
    "I could also keep it vague, tell her I work at a club. That's what I'll have to tell people from now on, right? Hopefully she won't press me too hard on it."
    hide screen textbox2 with dissolve
    menu:
        "I'm a math tutor. [gr]\[Felicia +1\]":
            $ Felicia_Affection +=1
            $ Felicia_Affection = clamp(Felicia_Affection, 0, 40)
            show screen textbox2 with dissolve
            "I'll keep it simple. It's what I can easily answer any potential questions about."
            scene pr0913 with dissolve
            mc "I work part-time as a math tutor."
            scene pr0914 with dissolve
            fel "You're a teacher?"
            scene pr0915 with dissolve
            mc "A tutor. A few days a week, for a couple of hours a day, I balance attempting to teach kids with no interest in learning with their parent's crazy expectations."
            scene pr0916 with dissolve
            fel "Guess you don't like it, huh?"
            scene pr0915 with dissolve
            mc "It's not for me."
            scene pr0914 with dissolve
            fel "Would you believe I actually wanted to be a teacher growing up?"
            scene pr0918 with dissolve
            mc "For real? You would've made a hot teacher. I don't think any boy would be able to pay attention."
            scene pr0917 with dissolve
            fel "Shut up!"
            scene pr0914 with dissolve
            fel "In another life, I would've liked to think I could have made a good one."

        "I work at a club.":
            show screen textbox2 with dissolve
            "I suppose I should get used to telling people an approximation of the truth, at least."
            scene pr0915 with dissolve
            mc "I work at a club, doing... stuff..."
            "Smooth."
            scene pr0914 with dissolve
            fel "Oh? What club?"
            scene pr0915 with dissolve
            mc "You wouldn't have heard of it, it's a private thing."
            scene pr0914 with dissolve
            fel "Please! You'd be surprised. I bet I know every club in the city."
            fel "Is it the one Ian works at?"
            scene pr0918 with dissolve
            mct "(--huh?)"
            mc "You know about that...?"
            scene pr0912 with dissolve
            fel "Mina told me he moonlights at a place at some old fuddy duddy place, but I'm pretty sure he undersells it to her."
            scene pr0919 with dissolve
            fel "Any place Ian would work has got to see some action, right?"
            "There was something alarmingly devious written across Felicia's face, but I suppose her logic is pretty spot on."
            mc "I wouldn't know yet, Ian only just got me a job there..."


    scene pr0920 with dissolve
    susie "Here you, go miss. You two have a good night."
    susie "See you around, [mcf]."
    scene black with fade
    stop music fadeout 3.0
    "Our stomaches full of easy greasy diner food, we made our way back out into the warm city night, with the pretense of splitting a ride-share home."
    scene pr0921 with dissolve
    play ambient "sound effects/city-night.wav"
    fel "Even if Mina and Ian bailed tonight, you still had a pretty fun time, right?"
    fel "I know I did, stud."
    scene pr0922 with dissolve
    hide screen textbox2 with dissolve
    menu:
        "I don't usually do stuff like that. [red]\[Toughness -1\]":
            $ toughness -= 1
            $ toughness = clamp(toughness, 0, 30)
            show screen textbox2 with dissolve
            scene pr0923 with dissolve
            mc "Yeah, I'm not so sure what came over me tonight."
            scene pr0924 with dissolve
            play sound "sound effects/car-beep.wav"
            fel "Oh, I have pretty good idea."


        "We should do this again sometime.":
            show screen textbox2 with dissolve
            scene pr0923 with dissolve
            mc "Yeah, that was... fun. {i}This{/i} was fun."
            mc "We should go out again sometime."
            scene pr0924 with dissolve
            fel "Hm."
            play sound "sound effects/car-beep.wav"
            fel "That could be arranged."

    scene pr0925 with dissolve
    mc "Looks like that's us."
    play sound "sound effects/notification.wav"
    $ history_felicia = "A beautiful woman Ian help set me up with, we fucked in the dirty bathroom of a night club. Needless to say, I hope to see her again sometime."
    $ met_felicia = True
    show bioadd with dissolve
    $ renpy.pause(3, hard=True)
    "The night had finally come to a  crawl. What had started as a night out with a friend, spun into a sexual encounter, and had ended with a quiet meal at my regular place."
    stop ambient fadeout 3.0
    scene black with fade
    mct "(Maybe taking my head out of the books ain't so bad sometimes?)"
    "Speaking of books: I hope my hangover doesn't bleed into the afternoon..."
    "......"
    "..."
    $ feliciaSex = True
    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionfelicia04 with blinds
    $ renpy.pause(6, hard=True)
    jump prDiscoAftermath

label prDiscoAftermath:
    $ date = "may11day"
    stop sound
    if prAfterParty == True:
        scene pr0938 with blinds
        show screen textbox2 with dissolve
        show screen qmenu with dissolve
        show may11day with squares
        mc "Ngg... fuck!"
        "Yeah, famous last words, right?"
        scene black with fade
        "After bidding goodbye to an equally wretched Mina, an annoyingly chipper Ian drove me back to my place."
        play sound "sound effects/shower.wav"
        scene pr0040 with blinds
        "Where I showered and did a little last minute of cramming for my afternoon final."
        stop sound fadeout 1.5

    else:
        scene pr0939 with blinds
        show screen textbox2 with dissolve
        show screen qmenu with dissolve
        show may10day with squares
        mc "Ngg... fuck!"
        "Yeah, famous last words, right?"
        play sound "sound effects/shower.wav"
        scene pr0040 with blinds
        "After availing myself of my mother's hangover cure, tomato juice, I showered and did a little last minute cramming."
        stop sound fadeout 1.5

    scene pr0940 with blinds
    "It wasn't my most sunny send-up of a semester, but I was well-prepared at least."
    scene pr0941 with dissolve
    play ambient "sound effects/city-night.wav"
    "With that out of the way, my summer was wide open. Sort of."
    mct "(I still have my new job at the Carnation Club to worry about, but I'll leave that stress for future me.)"
    scene pr0942 with blinds
    mc "(Tonight: it's a pizza and some {i}really{/i} stupid action mov--)"
    scene pr0943 with vpunch
    play music "music/george-street-shuffle.mp3"
    mct "(--{i}fuck{/i}.)"
    scene pr0944 with dissolve
    "Waiting in front of my apartment, casually resting against a black limousine, was the burly, muscle-packed bouncer I had met the other night."
    "He was affable enough during our one brief meeting, but..."
    scene pr0945 with dissolve
    war "Finally."
    "Seeing him outside the glitz of the club's bar room, overcast in the city's shadow, was more than a little startling."
    scene pr0946 with dissolve
    war "I was just about to tell Mrs. P that we should come back after the party."
    mct "(Mrs. P... Mrs. P... Ah, he means Mrs. Pulman.)"
    scene pr0947 with dissolve
    war "Get in."
    "A ordinary line from a mouth of a driver perhaps, but the way he delivered it... it felt like a command with zero leeway to refuse."
    hide screen textbox2 with dissolve
    menu:
        "Climb inside the limousine. [red]\[Toughness -1\]":
            $ toughness -= 1
            $ toughness = clamp(toughness, 0, 30)
            show screen textbox2 with dissolve
            mct "(I mean... it's not like anything {i}bad{/i} is going to happen.)"
            mct "(...right?)"

        "Ask him what this is about. [gr]\[Toughness +1\]":
            $ toughness += 1
            $ toughness = clamp(toughness, 0, 30)
            show screen textbox2 with dissolve
            scene pr0948 with dissolve
            mc "Uh... Warren, right? What's this about?"
            scene pr0947 with dissolve
            war "Mrs. P had some things she wanted to discuss with you. Now, {b}get in{/b}."
            mc "Alright..."

    scene pr0949 with blinds
    "Inside was a comfortably lush leather interior, and sure enough, Mrs. Pulman sat at the very back with a disinterested expression etched on her face."
    "If I had to guess, going off what Warren said, I would say she's been sitting here for a while."
    hide screen textbox2 with dissolve
    menu:
        "Apologize for making her wait. [gr]\[Kathleen +1\] [red]\[Toughness -1\]":
            $ toughness -= 1
            $ toughness = clamp(toughness, 0, 30)
            $ Kathleen_Affection += 1
            $ Kathleen_Affection = clamp(Kathleen_Affection, 0, 30)
            show screen textbox2 with dissolve
            mc "Have you been here long? Sorry to make you wait."
            scene pr0951 with dissolve
            kat "Only about ten minutes or so. Come, sit down."

        "You could've called. [gr]\[Toughness +1\] [red]\[Kathleen -1\]":
            $ toughness += 1
            $ toughness = clamp(toughness, 0, 30)
            $ Kathleen_Affection -= 1
            $ Kathleen_Affection = clamp(Kathleen_Affection, 0, 30)
            show screen textbox2 with dissolve
            mc "Have you been here long? You could've called first, you know."
            scene pr0950 with dissolve
            kat "I couldn't, actually. I realized too late after you left that no one had taken down your contact information."
            kat "Bunch of imbeciles..."
            mct "(Could've asked Ian...)"
            scene pr0951 with dissolve
            kat "Come, sit down."


    scene pr0952 with fade
    "Taking a seat next to Kathleen, my attention was irresistibly drawn to two things."
    "The first, her perfume, a distinctively pungent aroma which my olfactory nerves failed to notice not a few feet next to her, but upon sitting down, overwhelmed my sense of smell and immediately gave me a hard on."
    "For whatever reason, waves of pornographic images were now rippling through my head."
    scene pr0953 with dissolve
    "The second thing that captured my attention was Kathleen's neckline."
    "The dress she wore was ostentatious, and between the hypnotizing erotic fragrance, I couldn't help but have my eyes wander down the inviting nape of her neck to the valley below."
    hide screen textbox2 with dissolve

    default dynamicChoice1 = ""
    if toughness > 20:
        $ dynamicChoice1 = "{color=#0f0}[Toughness +1]"
    else:
        $ dynamicChoice1 = "{color=#f00}[Toughness -1]"

    menu:
        "Try to resist the temptation! [dynamicChoice1]":
            show screen textbox2 with dissolve
            mct "(Don't look, don't look, don't look...!)"
            if toughness > 20:
                $ toughness += 1
                $ toughness = clamp(toughness, 0, 30)
                scene pr0956 with dissolve
                "*Clears throat* So... what do you want to talk about?"

            else:
                $ toughness -= 1
                $ toughness = clamp(toughness, 0, 30)
                scene pr0954 with dissolve
                mct "(Fuck it, I gotta look.)"
                scene pr0955 with dissolve
                kat "I don't mind you looking, but I've got business to discuss and then a charity gala to attend, so..."



        "Fuck it! Throw caution to the wind and look! [gr]\[Kathleen +1\]":
            $ Kathleen_Affection += 1
            $ Kathleen_Affection = clamp(Kathleen_Affection, 0, 30)
            show screen textbox2 with dissolve
            scene pr0954 with dissolve
            "How could it be rude? She's got the puppies so proudly displayed!"
            if toughness < 20:
                mct "(Again, what's got me thinking this shit?!)"
            scene pr0955 with dissolve
            kat "I don't mind you looking, but I've got business to discuss and then a charity gala to attend, so..."


    scene pr0957 with dissolve
    kat "As I've told you, the exhibition we hold every year is comprised of three women."
    kat "Obviously not everyone has the mental wherewithal to endure what's expected of them during the event."
    scene pr0958 with dissolve
    kat "We currently have two confirmed Carnations - that's what we call them - confirmed for the exhibition. Now, we need to pick the third."
    scene pr0959 with dissolve
    mc "One of them being Rosalind? The one you let me pick?"
    scene pr0960 with dissolve
    kat "Oh, dear. She was already a sure thing. We wouldn't actually let her take part unless we were certain her circumstances were conducive to our purpose."
    scene pr0961 with dissolve
    mc "I see..."
    scene pr0962 with dissolve
    kat "Like I said, we need our third and it's come down to two women."
    scene pr0961 with dissolve
    mc "You didn't seem to have much faith in me..."
    scene pr0962 with dissolve
    kat "Well, this is me making an effort. Plus, I had my guy look into you. You might have more potential than one of Killian's usual, dumbass friends."
    scene pr0961 with dissolve
    mc "Look into me...?"
    scene pr0960 with dissolve
    kat "Yes, your background and upbringing. That sort of thing."
    kat "Your mother, did you know she did porn?"
    mct "(--!)"
    hide screen textbox2 with dissolve
    menu:
        "Fuck you! [gr]\[Toughness +1\]":
            $ toughness += 1
            $ toughness = clamp(toughness, 0, 30)
            show screen textbox2 with dissolve
            scene pr0963 with dissolve
            mc "Why the fuck would you--"
            scene pr0964 with dissolve
            kat "So you do, interesting."

        "I do know...":
            show screen textbox2 with dissolve
            scene pr0961 with dissolve
            mc "I... do."
            scene pr0962 with dissolve
            kat "Interesting..."

    scene pr0965 with dissolve
    kat "God knows how that must color your perception of women."
    scene pr0966 with dissolve
    mc "It doesn't change a damn thing."
    mc "All it did was make me realize how much she cared for me."
    scene pr0965 with dissolve
    kat "Is that the way you've internalized? I wonder if SHE rationalized it that way."
    scene pr0963 with dissolve
    mc "Can we get back to why we're talking in the first place?"
    scene pr0967 with dissolve
    kat "Sorry, you're right. We have little time now, but I'd love to pick your brain one day. All kinds of fucked up childhoods go into making my club successful."
    kat "Understanding the people who work for you goes a long way in preventing hiccups."
    scene pr0968 with dissolve
    kat "Take this. It contains information on the two women, plus a little something to help get your head in the game."
    kat "Be at the Club at 11:30 tomorrow. That's when we'll interview the whores."
    scene pr0969 with dissolve
    kat "That about covers it. Give Warren your phone number when you get out. I'll be in touch."
    scene pr0970 with dissolve
    mc "Will do..."
    scene pr0971 with blinds
    stop music fadeout 3.0
    "As soon as I'd exited the limo, thankfully escaping that tortuous aroma, my erection nevertheless remained at full, steely attention."
    scene black with fade
    "It would be a full hour before it finally subsided, and that's when I built up the resolve to examine the USB drive's contents."
    scene pr0972 with blinds
    stop ambient
    play music "music/leaving-home.mp3"
    "On it were two PDF files and a sizable high quality video, all three vaguely labeled."
    scene pr0973 with pixellate
    "The first profile included a selfie of a raven-haired beauty, wearing nothing but a pair of lace designer panties, coyly smiling for the camera while raising her hips and putting her generous, plump ass on display."
    mct "(Lucy Long, huh?)"
    "It says here she's thirty four years old, married, mother of two, and works as a teacher at St. Ives."
    "In a small box labeled 'nature of hardship', found near the bottom of the document, one simple quantification was made: bribe - $22,000."
    "It's a large number to someone like me, but it seemed like a paltry amount to sell your dignity for."
    scene pr0974 with dissolve
    "The second profile was of a red-headed woman, demurely smiling for the camera, clad in a slingshot bikini that showed off her a well-toned, muscular figure."
    "Veronica Lynch - thirty one, divorced. Under occupation was a series of vague, but surprising descriptors."
    "Entrepreneur, entertainer, model. The list went on. The first profile was clinical enough that I was unsure if Katherine had authored the document herself, but this one was clearly a submitted application."
    "In stark contrast to her personal accomplishments, her listed hardship was dramatically underwritten."
    mct "(Growing overhead?)"
    scene pr0976 with dissolve
    "These are the two women Mrs. Pulman said I'd be meeting tomorrow at 11:30 am."
    "I can only colorfully imagine what those interviews might entail."
    scene pr0980 with dissolve
    "Both of these women were easily out of my league, but part of my lizard brain can't help but wonder..."
    play sound "sound effects/sms-chime.wav"
    "*Chirp, chirp.*"
    hide screen textbox2 with dissolve
    call phone_start_unknown from _call_phone_start_unknown
    call message_img("Unknown", "Hey!","mina01") from _call_message_img_1
    call phone_end_unknown from _call_phone_end_unknown
    scene pr0975 with dissolve
    show screen textbox2 with dissolve
    "The message was an odd selfie of Mina holding up a cup exclaiming 'I'm sorry'. Is she trying to apologize?"
    mct "(I'm not sure what she's apologizing for though...)"
    scene pr0980 with dissolve
    hide screen textbox2 with dissolve
    call phone_start_mina from _call_phone_start_mina
    call screen phone_reply("Don't sweat it?","minaTextSweat","What are you apologizing for?","minaTextConfused")

label minaTextSweat:
    call phone_after_menu from _call_phone_after_menu_8
    call message_start("[mcf]", "You didn't do anything wrong?") from _call_message_start_13
    if prAfterParty == True:
        call message ("Mina", "You mean it? Cause I feel bad about conking out on you guys without saying goodnight...") from _call_message_33
    else:
        call message ("Mina", "You mean it? Cause I feel bad about ditching you at the club last night all over Ian's silly games...") from _call_message_34
    call reply_message("Don't sweat it. I had a good time.") from _call_reply_message_7
    call message ("Mina", "Prooomise?") from _call_message_35
    call reply_message("I promise.") from _call_reply_message_8
    call message ("Mina", "Yaaaay! I'll talk to you later then, [mcf]. Good night!") from _call_message_36
    call phone_end_mina from _call_phone_end_mina
    jump prCarnationClubDemo


label minaTextConfused:
    call phone_after_menu from _call_phone_after_menu_9
    call message_start("[mcf]", "What are you talking about?") from _call_message_start_14
    if prAfterParty == True:
        call message ("Mina", "I conked out on you guys without saying goodnight. Probably embarrassed myself doing God knows what else...") from _call_message_37
    else:
        call message ("Mina", " I feel bad about ditching you at the club last night all over Ian's silly games...") from _call_message_38
    call reply_message("That's it? I didn't even feel slighted.") from _call_reply_message_9
    call message ("Mina", "Prooomise?") from _call_message_39
    call reply_message("I promise.") from _call_reply_message_10
    call message ("Mina", "Yaaaay! I'll talk to you later then, [mcf]. Good night!") from _call_message_40
    call phone_end_mina from _call_phone_end_mina_1
    jump prCarnationClubDemo


label prCarnationClubDemo:
    show screen textbox2 with dissolve
    mct "(Now, where was I?)"
    "Right, the video that was included on the USB drive."
    scene pr0981 with blinds
    "The footage opened with a simple title card on a black background, followed by an introduction of sorts."
    mct "(Public use - That is... probably what it sounds like, huh?)"
    scene pr0977 with pixellate
    "Mrs. Pulman was on stage alongside three women in bunny suits, adorned in a tacky masquerade mask herself, energetically wrangling an unseen crowd behind the film's frame."
    "She continued on, building up hype and parading the girl's around one by one like showdogs, lifting and bending body parts, drawing rapid interest from the crowd."
    scene pr0978 with fade
    "After a few minutes of showmanship, came the show. Side-by-side, back-to-back seemingly unending fellatio."
    "Men were corralled into a lines and the girl's did their best to bring each new man to orgasm quickly, inhaling dick after dick without respite."
    "Finally, when it looked like everyone had been satisfied, another crowd of men were herded onto the stage for the festivities to begin in full."
    scene pr0979 with fade
    "Strapped down to cherry leathers horses, they were the playthings for the whims of the pooling men. What had started as a concerted effort on each woman's part to please the crowd had devolved over time into insensate, mechanical action."
    "Naturally, I skipped through the prolonged parts. The last bit lasted over more than two hours. Until finally..."
    scene black with fade
    "Three people, conspicuously identified as the judges were called on to determine a winner."
    scene pr0983 with pixellate
    "Openly, they individually cast their votes. Points were somehow divvied up, and the winner for the event was declared."
    "And with that, the AFTER PARTY began..."
    scene pr0980 with dissolve
    mct "(Holy shit...)"
    mct "({b}THAT{/b} is an exhibition? That's what I've gotten myself into?)"
    "I had deluded myself I would be able to compartmentalize working at the Club, that I would be able to keep it separate in full view of the fact that Dr. Chuck had promised to pay for my med school, but..."
    "This kind of debauchery, it isn't the kind of thing you can just put back in a box, is it...?"
    "At the same time, I can't deny that I found certain parts of that video... appealing."
    play sound "sound effects/ringing-inbound.wav"
    "*Ring, ring*"
    scene pr0982 with dissolve
    play sound "sound effects/phonemenu.wav"
    show vic-call
    stop sound
    mc "Hey, Mom."
    vic "Hey, how are you? We haven't talked in a few days."
    mc "Sorry, been busy with... finals."
    vic "Today was your last one, right? How did that go?"
    mc "It went well. How about you? How have you been?"
    vic "You don't want to hear an old woman complain, do you?"
    vic "Say, why don't you drop by for dinner tomorrow? We can celebrate the end of another semester."
    mc "Sure, that'd be nice."
    "It really would. A bit of normalcy sounds good right about now."
    vic "Great, I won't keep you then."
    vic "Take care, hun."
    mc "You too Mom, good night."
    play sound "sound effects/call-end.wav"
    "*Beep*"
    hide vic-call
    scene pr0980 with dissolve
    "Giving the smut on the screen one last glance, I resisted the temptation to watch it again."
    mct "(I should just go to bed. Tomorrow I'll be meeting the two ladies profiled.)"
    "Lucy and Veronica, two women potentially facing down..."
    scene pr0979 with pixellate
    "That."
    stop music fadeout 3.0
    "......."
    scene black with fade
    "......"
    "..."
    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionveronica03 with blinds
    $ renpy.pause(6, hard=True)

#------------------------------------------------------------------------------#
#                                   May 12                                     #
#------------------------------------------------------------------------------#
    stop sound

label prMay12start:
    $ date = "may12day"
    stop sound
    scene pr0984 with blinds
    play ambient "sound effects/city-night.wav"
    show may12day with squares
    show screen textbox2 with dissolve
    show screen qmenu with dissolve
    "The Carnation Club -- 30 minutes before my meeting."
    scene pr0985 with dissolve
    mct "(That's...)"
    mct "(The club's bartender, I think)"
    "I've got time to kill I suppose, if I wanted to try and speak with her."
    hide screen textbox2 with dissolve
    menu may12hanamenu:
        "Call out to her. [gr]\[Hana +1\]":
            $ Hana_Affection += 1
            $ Hana_Affection = clamp(Hana_Affection, 0, 40)
            show screen textbox2 with dissolve
            pass
        "Just head inside.":
            show screen textbox2 with dissolve
            jump prMay12meeting

    scene pr0986 with dissolve
    play music "music/take-the-lead.mp3"
    mc "Hey! Hana, right?"
    scene pr0987 with fade
    hana "Oh, yeah! The {b}new{/b} guy."
    scene pr0988 with dissolve
    mc "Cool bike."
    scene pr0989 with dissolve
    hana "Thanks. Suzie Q here is the one gal who's never been cross with me."
    scene pr0987 with dissolve
    hana "Hows it going with you, Greenboy?"
    scene pr0988 with dissolve
    "Paying no mind to the odd nickname, I answered earnestly."
    if kat_polite == True:
        scene pr0990 with dissolve
        mc "I'm on my way to a meeting with Mrs. Pulman, but I'm a little early I suppose."
    else:
        scene pr0990 with dissolve
        mc "I'm on my way to meet with Kathleen, but I'm a little early I suppose."

    scene pr0991 with dissolve
    hana "Good. You don't want to be late with that old bat. She gets annoying when you're not on time, but then again she's always real cunty to begin with."
    scene pr0988 with dissolve
    mc "I guess it comes with the territory, huh?"
    scene pr0987 with dissolve
    hana "Yeah. Anyone who'd work at that place is an asshole, triple so if you got the kind of skin in it Kat or Charles has."
    scene pr0988 with dissolve
    mc "What about you? You mean to say everyone is an asshole except YOU, right?"
    scene pr0991 with dissolve
    hana "You can be the judge of that."
    scene pr0992 with dissolve
    hana "So, summer exhibition business?"
    scene pr0993 with dissolve
    mc "Uh... yeah, you got it actually. How'd you know?"
    scene pr0994 with dissolve
    hana "Well, it's that time of the year."
    scene pr0995 with dissolve
    "Again, I couldn't suggest otherwise."
    mc "How long have you been working here?"
    "She looked about my age, maybe a couple of years older at most."
    scene pr0992 with dissolve
    hana "Only over a year. I was next to the newest here, started a little before the last person who had your job."
    scene pr0993 with dissolve
    "My mind flashed back to Kathleen's angry comments from a couple of days ago."
    mc "I have heard things..."
    scene pr0992 with dissolve
    hana "About Darius you mean?"
    scene pr0993 with dissolve
    mc "The guy I'm replacing."
    scene pr0994 with dissolve
    hana "Yeah, him. Whatever you've heard is probably true. Bonafide shit head was what he was."
    scene pr0995 with dissolve
    mc "What did he do to get canned?"
    scene pr0994 with dissolve
    hana "He didn't exactly get FIRED, per se. More like he just stopped showing up altogether."
    hana "You should ask your friend Killian if you want to know more about it. They were two dumbass peas in a pod."
    scene pr0996 with dissolve
    play sound "sound effects/sms-chime.wav"
    scene pr0997 with dissolve
    hana "Hm. Sorry, but I gotta go."
    scene pr0998 with dissolve
    mc "Right, nice talking to you."
    scene pr0994 with dissolve
    hana "See you around, Greenboy."
    scene pr0999 with fade
    "I watched Hana sputter off, until the breaks and bends of the city had obscured her, before finally heading inside for my business."
    scene black with fade
    stop music fadeout 3.0
    "......"
    "..."

label prMay12meeting:
    if _in_replay:
        show transitionkathleen01 with cmet
        show screen textbox2 with dissolve
        "Please set [mcf]'s personality (toughness score) for this replay."
        hide screen textbox2 with dissolve
        menu:
            "Nice guy (Toughness: 0)":
                $ toughness = 0
            "Mischevious (Toughness: 18)":
                $ toughness = 18
            "Asshole (Toughness: 30)":
                $ toughness = 30
        show screen textbox2 with dissolve


    stop ambient
    scene pr1000 with blinds
    "When I arrived at the top of the tower, I gave a friendly wave to Jacob and headed directly to Mrs. Pulman's office."
    scene pr1001 with dissolve
    play sound "sound effects/door-knock.wav"
    "*Knock, knock*"
    kat "Come in."
    scene pr1002 with dissolve
    play music "music/horrible.mp3"
    "Inside Mrs. Pulman's posh office sat the two women featured on that USB drive, whose eyes fell on me as soon as I entered the room."
    mc "I'm not late am I?"
    scene pr1003 with dissolve
    kat "No. You're early, actually. The ladies here were just earlier."
    kat "Let me introduce you..."
    scene pr1004 with dissolve
    "Both women were quick to climb to their feet."
    scene pr1005 with dissolve
    kat "This is my aid, [mcf] [mcl]."
    kat "He has some say on which of you will join the Club, so he'll be sitting in on this interview."
    scene pr1006 with dissolve
    kat "Now, [mcf]..."
    kat "This alliterative angel is Lucy Long, an English teacher at St. Ives Academy."
    scene pr1007 with dissolve
    kat "Ironically, her kid's too stupid to get into St. Ives on his own merit, so she's looking for some help there."
    "Damn, she doesn't mince words."
    scene pr1008 with dissolve
    lucy "Uh... *clears throat* It's nice to meet you, Mr. [mcl]."
    scene pr1006 with dissolve
    mc "Same to you, Lucy."
    scene pr1009 with dissolve
    kat "This is--"
    scene pr1010 with dissolve
    ver "Veronica Lynch, proprietor of B-ForgeX and life coach."
    scene pr1011 with dissolve
    "Seizing her own chance at making an introduction (and after Lucy's editorialized version who could blame her), Veronica took my hand in hers and vigorously shook it."
    "Her hand, despite some rough calluses, had a surprisingly feminine touch. Her nails were well cared for and painted, and her palms had the faintest hint of lotion."
    hide screen textbox2 with dissolve
    menu:
        "Return her handshake. [gr]\[Veronica +1\]":
            $ Veronica_Affection += 1
            $ Veronica_Affection = clamp(Veronica_Affection, 0, 40)
            show screen textbox2 with dissolve
            scene pr1012 with dissolve
            mc "Nice to meet you, Veronica."
            scene pr1013 with dissolve
            ver "If you say so, boy."

        "Life coach? [gr]\[Kathleen +1\] \[Toughness +1\] [red]\[Veronica -1\]":
            $ Veronica_Affection -= 1
            $ Veronica_Affection = clamp(Veronica_Affection, 0, 40)
            $ Kathleen_Affection += 1
            $ Kathleen_Affection = clamp(Kathleen_Affection, 0, 30)
            $ toughness += 1
            $ toughness = clamp(toughness, 0, 30)
            show screen textbox2 with dissolve
            scene pr1014 with dissolve
            mc "If you're here, not much of a life coach, are you?"
            scene pr1015 with dissolve
            ver "Nobody asked you."

    scene pr1016 with slideright
    kat "Now that's out of the way, we need to determine if either of you ladies are suitable candidates for the club's summer exhibition."
    scene pr1017 with fade
    lucy "U-um... how are we going to determine that?"
    scene pr1018 with dissolve
    kat "All you have to do is do as I ask and to answer any questions I have truthfully."
    kat "It's in your best interest to be honest. If you're not cut out for the role, you'll end up regretting it."
    scene pr1019 with dissolve
    ver "It's just sex work, isn't it? You're overselling it."
    scene pr1020 with dissolve
    kat "Is that what you think? You think that this will be easy?"
    scene pr1021 with dissolve
    kat "Why don't you stand up for me, Miss Lynch."
    scene pr1022 with dissolve
    ver "Alright..."
    scene pr1023 with dissolve
    "Without warning, Mrs. Pulman began running her hands up and down Veronica's body, absent-mindedly making an audible note of her measurements."
    ver "What are you-?"
    scene pr1024 with dissolve
    kat "Only speak when you're spoken to, Miss Lynch."
    scene pr1025 with dissolve
    kat "Hmm, not bad. More hard-bodied than our usual offerings, {b}but{/b}..."
    scene pr1026 with dissolve
    kat "...I can't say you're not filled out in the right places."
    scene pr1027 with dissolve
    kat "Tell me, how did you know how to apply, Miss Lynch?"
    kat "Mrs. Long was referred to us by a junior member of our club. Isn't that right?"
    scene pr1028 with dissolve
    lucy "Yes, Ma'am. He told me--"
    scene pr1027 with dissolve
    kat "Meanwhile, your application came out of the blue. You left the referral box blank."
    scene pr1029 with dissolve
    ver "Sam--"
    kat "One sec."
    scene pr1030 with dissolve
    kat "Take your blouse and jacket off, dear."
    lucy "Huh, b-but--"
    scene pr1031 with dissolve
    kat "You were saying?"
    scene pr1032 with dissolve
    ver "...Samson Garcia told me about this place."
    scene pr1033 with dissolve
    kat "Ah, Mr. Garcia."
    scene pr1034 with dissolve
    kat "One of our junior members, [mcf]. Not much in the way of money, but other members enjoy basking in his glam and flash, so we're happy to comp him every now and then."
    mc "I see..."
    scene pr1033 with dissolve
    kat "How do you know Mr. Garcia?"
    scene pr1032 with dissolve
    ver "I pay him to be a spokesperson for my gym."
    scene pr1035 with dissolve
    kat "Hmm..."
    "Mrs. Pulman took a long pause as she considered Veronica's words."
    scene pr1036 with dissolve
    kat "Front and center, Mrs. Long. Give us a twirl"
    lucy "Uh, yes Ma'am."
    scene pr1037 with dissolve
    kat "What do you think, [mcf]?"
    mc "What do you mean?"
    scene pr1038 with dissolve
    kat "You're a man. Do you find Mrs. Long attractive?"
    mc "Uh, I suppose..."
    "Obviously, I was feeling embarrassed being so pointedly asked a question about the woman standing right in front of me."
    scene pr1039 with dissolve
    kat "You suppose?! What kind of answer is that?"
    kat "Hmm... you're right, though. It's not a fair assessment while she still has her bra on."
    scene pr1040 with dissolve
    kat "{b}Lose it{/b}, Mrs. Long."
    lucy "Y-yes Ma'am."
    kat "Well, you have the right attitude at least."
    scene pr1041 with fade
    kat "How about now, [mcf]?"
    mc "I, uh..."
    mct "(Like that helps things!)"
    scene pr1042 with dissolve
    kat "Oh, come now. Get a closer look."
    scene pr1043 with dissolve
    kat "Give them a feel."
    mc "...if you'll excuse me."
    scene pr1044 with dissolve
    kat "Well? What do you think? With those vulgar cow tits, I bet her students don't hear a single word that comes out of her mouth."
    scene pr1045 with dissolve
    lucy "That's n-not--"
    kat "I didn't ask for your input, Mrs. Long."
    scene pr1044 with dissolve
    lucy "S-sorry."
    kat "Well, what's your appraisal, [mcf]?"
    mct "(Is she {i}seriously{/i} asking me that?!)"
    mct "(How the hell do I respond to a question like that?)"
    hide screen textbox2 with dissolve
    menu:
        "Speak the god's honest truth. [gr]\[Toughness +1\] \[Kathleen +1\]":
            $ toughness += 1
            $ toughness = clamp(toughness, 0, 30)
            $ Kathleen_Affection += 1
            $ Kathleen_Affection = clamp(Kathleen_Affection, 0, 30)
            show screen textbox2 with dissolve
            scene pr1046 with dissolve
            mc "I mean, what do you think?"
            mc "These are some... fantastic tits."
            kat "Thank you for your honest opinion, [mcl]."

        "Keep it coy. [red]\[Toughness -1\] \[Kathleen -1\]":
            $ toughness -= 1
            $ toughness = clamp(toughness, 0, 30)
            $ Kathleen_Affection -= 1
            $ Kathleen_Affection = clamp(Kathleen_Affection, 0, 30)
            show screen textbox2 with dissolve
            scene pr1047 with dissolve
            mc "They're... they're alright, I mean."
            kat "You've seen better, huh?"
            mct "(I didn't mean that...)"

    scene pr1048 with dissolve
    kat "You're a bit overdressed don't you think? Take everything off."
    scene pr1049 with dissolve
    ver "If that's what it takes."
    scene pr1050 with dissolve
    kat "So, you're here because you want to get your son into St. Ives?"
    scene pr1051 with dissolve
    lucy "That's right."
    scene pr1052 with dissolve
    kat "There's other schools you know..."
    scene pr1051 with dissolve
    lucy "None like St. Ives."
    scene pr1052 with dissolve
    kat "...and you're willing to do whatever is asked of you just for a CHANCE at getting him in?"
    scene pr1053 with dissolve
    lucy "He deserves the best."
    scene pr1054 with dissolve
    kat "Ohoho? Is that the real reason? I have my doubts about that. Are you sure it's not just the vanity of a status-concerned whore?"
    lucy "No, wha--"
    scene pr1055 with dissolve
    kat "Well, I can't for sure, but I get the feeling the real reason you want your son into St. Ives is to lord it over your co-workers and friends. Am I wrong?"
    "Lucy was standing there in complete silence, troubled, unsure of how to answer Mrs. Pulman's prodding without jeopardizing her chance of getting picked."
    kat "No matter, wanting the best for your child or just wanting the best for you, it's ample motivation to carry you to the end of summer."
    scene pr1056 with dissolve
    kat "Get on your hands and knees, Mrs. Long."
    lucy "Okay..."
    scene pr1057 with dissolve
    kat "Try to keep steady, dear."
    scene pr1058 with fade
    "Without much in the way of warning, Kathleen sat square on Lucy's back, using her as a stool."
    "Surprised, Lucy buckled slightly under Mrs. Pulman's weight, but managed to successfully lock her shoulders in support."
    mct "(Holy shit, she's just letting it happen? It's like Mrs. Pulman has her under a spell.)"
    scene pr1059 with dissolve
    ver "...you're not sitting on me, that's for sure."
    scene pr1060 with dissolve
    kat "As fun as that would be, I know that's not happening. Yet."
    scene pr1061 with dissolve
    kat "But that's okay. Our members like a little fight in our Carnations. It makes the shows more interesting."
    scene pr1059 with dissolve
    ver "If you say so."
    scene pr1060 with dissolve
    kat "Still, I have to ask. Mr. Garcia did explain to you what we do here, right?"
    scene pr1062 with dissolve
    ver "He did. Put on a show for a bunch of old, impotent fucks and you'll help me with some business that needs taking care of."
    scene pr1061 with dissolve
    kat "That's right, more or less. The hitch is you've got to perform better than your opponents. Nothing is guaranteed."
    scene pr1062 with dissolve
    ver "That's not a problem. {b}I'll win{/b}."
    scene pr1061 with dissolve
    kat "You say it with such confidence, even I almost believe you."
    kat "Still, it's odd you believed him. How are you so sure he wasn't merely looking to take advantage of you?"
    scene pr1063 with dissolve
    ver "..."
    "Veronica shifted uncomfortably at the question."
    scene pr1064 with dissolve
    kat "You don't need to say it. You're on your last leg, aren't you?"
    kat "I believe you wrote 'growing overhead' on your application. That's your way of saying you're up to your tits in debt, isn't it?"
    scene pr1065 with dissolve
    ver "I have some... financial concerns."
    scene pr1064 with dissolve
    kat "Hmmm, you both have good reasons. I don't think either of you will be lacking in the motivation department, but the question is - do you have the willpower...?"
    scene pr1066 with dissolve
    kat "You'll be doing vile, humiliating things. Even an ounce of pride will be your enemy. Do you two you have it in you to do what's asked?"
    scene pr1067 with dissolve
    lucy "I can do it!"
    ver "I do."
    scene pr1068 with fade
    kat "If that's true, both of you lock your hand behind your head and spread your legs."
    lucy "Y-yes, Ma'am."
    ver "...fine."
    scene pr1069 with slideright
    kat "Come, don't be shy, [mcf]."
    scene pr1070 with dissolve
    kat "If it were on you to decide, which one of these sluts would you pick?"
    scene pr1072 with dissolve
    "Watching the interview unfold from the sidelines gave me some distance to what was happening. Being pulled into it all of a sudden, I was made intensely aware of just how fucked this whole thing felt."
    "No matter how I answered her question, I'll end up feeling like an asshole."
    scene pr1071 with dissolve
    mc "Uh, I can't say..."
    scene pr1070 with dissolve
    kat "Come on, you have to prefer one over the other. People always have preferences."
    scene pr1072 with dissolve
    "Maybe, but facing down the women while they stood there practically nude, suffering in embarrassment, made it impossible to blurt out."
    mc "..."
    scene pr1070 with dissolve
    "My indecisiveness produced an irritated sigh from the old woman."
    kat "Well, if you won't say who'd you pick, then how about you tell me which woman you find the most attractive?"
    scene pr1073 with dissolve
    kat "Mrs. Long's useless fat ass and vulgar cow tits or Miss Lynch's freakishly overdeveloped body?"
    scene pr1072 with dissolve
    "Not like it wasn't already abundantly clear, but Kathleen was thoroughly enjoying this."
    scene pr1071 with dissolve
    mc "...I don't know."
    scene pr1070 with dissolve
    stop music fadeout 3.0
    kat "Well, if you're truly having trouble picking, I know a surefire way to get the answer out of you."
    mct "(I don't like the sound of that...)"
    scene pr1074 with dissolve
    play music "music/leaving-home.mp3"
    kat "Take your cock out."
    mc "W-what? You can't be serious."
    "I knew she was 100 percent serious, but how else could I respond? By doing what she asked? Yeah, right."
    scene pr1075 with dissolve
    kat "What's the problem? You'll be expected to use that thing from time to time to perform your duties for the club."
    mc "gh..."
    hide screen textbox2 with dissolve
    menu:
        "Take your dick out. [gr]\[Kathleen +1\] \[Toughness +1\]":
            $ Kathleen_Affection += 1
            $ Kathleen_Affection = clamp(Kathleen_Affection, 0, 30)
            $ toughness += 1
            $ toughness = clamp(toughness, 0, 30)
            show screen textbox2 with dissolve
            scene black with fade
            play sound "sound effects/zipper.wav"
            "*{i}Ziiiiip*{/i}"
            scene pr1078 with dissolve
            "Fuck it. I'm in this thing, right? I'll get paid as long as I do as they ask."

        "Try to refuse. [red]\[Kathleen -1\] \[Toughness -1\]":
            $ Kathleen_Affection -= 1
            $ Kathleen_Affection = clamp(Kathleen_Affection, 0, 30)
            $ toughness -= 1
            $ toughness = clamp(toughness, 0, 30)
            show screen textbox2 with dissolve
            scene pr1076 with dissolve
            mc "I don't... want to."
            scene pr1077 with dissolve
            kat "You do remember your arrangement with Charles, yes?"
            scene pr1076 with dissolve
            mc "..."
            "Fuck it, she's right. If I want to get paid, I have to do this."
            scene black with fade
            play sound "sound effects/zipper.wav"
            "*{i}Ziiiiip*{/i}"
            scene pr1078 with dissolve
            mc "Satisfied?"

    kat "Hmm... consider me surprised. I wasn't expecting a cock like that from a boy like you."
    kat "Doesn't match your face, which is a plus. Some people pay a lot for that kind of contradiction."
    scene pr1079 with dissolve
    kat "You're already so hard too. At least I know one of these pig-whores managed that, but we're going to find out which one."
    mc "Nghh--"
    "Mrs. Pulman's cold grip on my cock had me choking out words. I was afraid to ask, but..."
    scene pr1080 with dissolve
    mc "H-how are you planning to do that?"
    scene pr1081 with fade
    mc "Ggh--!"
    kat "I'm glad you asked, [mcf]."
    scene pr1082 with dissolve
    "With relative ease, Mrs. Pulman pulled me into the sweltering embrace of her alabaster bosom."
    "The moment my nose made contact with that supple valley of flesh, I knew I had been ensnared just like in the limo."
    "That perfumantic aroma that had, just last night, left me painfully aching for release long after Kathleen had departed had once again found its home in my nostrils."
    "It wasn't as thickly pungent as last time, but it nevertheless did the same trick. All at once, every thought had emptied from my head, leaving only an animalistic urge behind."
    scene pr1083 with dissolve
    mc "Shit! {w}Fuck! {w}Bitch!"
    "As the moments passed with her holding me there, I was drowning in a wave of uncontrollable vulgarity."
    "It took all the willpower in my body not to shove Kathleen to the floor and ravage her then and there."
    scene pr1084 with dissolve
    kat "You're practically clawing for release by now, aren't you?"
    scene pr1085 with dissolve
    mc "Nggha, just jerk it, you bitch!"
    kat "Now, now, is that anyway to talk to your boss?"
    scene pr1086 with dissolve
    kat "No matter, I forgive you. This is dangerously potent stuff, after all. A large dose of it could actually drive you insane."
    mc "What is this shit?!"
    scene pr1087 with dissolve
    kat "To put it simply, it's a very powerful aphrodisiac."
    kat "It sends your body into overdrive. Ramps up your testosterone levels... baths your neurotransmitters in dopamine... removes ALL sense of inhibition..."
    kat "And this is the best part, it sends your gonads into overproduction."
    mc "Fuck you! That's not a real thing!"
    kat "Can you argue with what's happening to your body right now?"
    "I sure as shit couldn't. Everything she was saying had to be true. My brain felt like it was turning into liquid-fucking-magma after all."
    kat "It's best you get used to this as fast as possible. You'll become well-acquainted with it."
    scene pr1089 with dissolve
    scene pr1090 with dissolve
    "With those words, she begin to slowly jerk her hand back and forth, giving me a cruel taste of the release I maddeningly craved."
    scene pr1089 with dissolve
    scene pr1090 with dissolve
    "Of course, her gentle undulation wasn't nearly enough. You would think whatever this perfume would have me on a hair-trigger, but it paradoxically had me feeling that I'd never cum."
    scene pr1089 with dissolve
    scene pr1090 with dissolve
    "I was feeling an immense swelling in my loins, one that despite my intense arousal, seemed eons away from relief."
    scene pr1091 with dissolve
    mc "Fchk--faster, faster, faster you HAG!"
    "My hand, with a mind of its own, roughly grabbed at my tormentor's breast in attempt to convince her to increase the pace."
    scene pr1092 with dissolve
    "Instead, she simply grabbed me by the wrist and reprimanded me like I was a child."
    kat "Naughty, but I forgive you! {b}Don't{/b} touch me again, though."
    kat "I'll give you a hand, but I'm not the one you should be focusing your lusts on here."
    "Fuck this slag. All she has is words and I NEED to cum now."
    scene pr1093 with dissolve
    kat "Look in front of you!"
    kat "See those {b}whores{/b}, brazenly sticking their tits out, all for the mere chance of money?"
    scene pr1094 with dissolve
    ver "You're twisted, you know that bitch?"
    scene pr1093 with dissolve
    kat "Ha! That one's got a real mouth on her, doesn't she?"
    kat "I bet you'd love to drive that throbbing cock down her yapping bitch-maw."
    scene pr1095 with dissolve
    lucy "This is getting weird..."
    scene pr1093 with dissolve
    kat "Or how about the other one... {b}Mrs.{/b} Long."
    mc "Nggh--! Fuck, fuck, fuck!"
    "The grip on my dick tightened and the pace intensified as Mrs. Pulman ramped up on her verbal skewering."
    kat "Do you prefer those thick, meaty thighs and huge ass? Imagine hot-dogging yourself between those cheeks?"
    mc "Nga, fgwh, ommhaa!"
    "My brain was cooked. All that was escaping my mouth, in between ravenous oxygen-starved gasps of breath, was unintelligible garbage."
    scene pr1096 with dissolve
    kat "Get down on your knees! Keep your hands behind your head and your tits out!"
    scene pr1097 with dissolve
    ver "You're not going to--"
    kat "You said you'd do anything, remember? Get the FUCK down on your knees, pig."
    ver "...tsk! Whatever."
    scene pr1098 with dissolve
    kat "Now, which one will it be, [mcf]? Which of these miserable sows do you want to paint with your seed?"
    kat "Will it be Mrs. Long or Miss Lynch?"
    kat "I'll take whoever you choose as your answer for who to hire."
    "At this point, there was nothing upstairs but a raw, animinalistic desire to rut."
    "I didn't give a fuck about the competition or what I was cumming on, I just had to cum. Desperately."
    mct "(NGGGHHHHHHAAAAAAAAA! I'M THERE!)"
    "There was no time, so I ejaculated on..."
    hide screen textbox2 with dissolve
    menu:
        "Plaster Lucy with your baby batter!":
            show screen textbox2 with dissolve
            scene pr1099 with fade
            mc "Fuck, shit, fuck, shiiiiiiiii--"
            scene pr1100 with dissolve
            play sound "sound effects/spurt.wav"
            "The next thing I knew, my head was engulfed in a suffocatingly fuzzy feeling and my eyesight short circuited, plunging my mind into an abyss of purifying white."
            "I was ejaculating harder than I had ever before, with a dizzying intensity that almost made me lose my breakfast."
            play sound "sound effects/spurt.wav"
            mc "NGGHHAAAYAAAAAAA~! Take it, you slut!"
            scene pr1101 with dissolve
            mct "*huff* *huff* (H-holy shit!)"
            "Despite cumming more in my life than ever before, my dick remained hard as titanium, but thankfully, my good sense was returning to me."
            kat "Looks like you made your decision."
            kat "Aren't you flattered, Mrs. Long?"
            lucy "Uh, yes M-M'am."


        "Paint Veronica white! [red]\[Veronica -2\]":
            $ Veronica_Affection -= 2
            $ Veronica_Affection = clamp(Veronica_Affection, 0, 40)
            $ prVero_Facial = True
            show screen textbox2 with dissolve
            scene pr1102 with fade
            mc "Fuck, shit, fuck, shiiiiiiiii--"
            scene pr1103 with dissolve
            play sound "sound effects/spurt.wav"
            "The next thing I knew, my head was engulfed in a suffocatingly fuzzy feeling and my eyesight short circuited, plunging my mind into an abyss of purifying white."
            "I was ejaculating harder than I had ever before, with a dizzying intensity that almost made me lose my breakfast."
            play sound "sound effects/spurt.wav"
            mc "NGGHHAAYAAAAAAAA~! Take it, you slut!"
            scene pr1104 with dissolve
            mct "*huff* *huff* (H-holy shit!)"
            "Despite cumming more in my life than ever before, my dick remained hard as titanium, but thankfully, my good sense was returning to me."
            kat "Looks like you made your decision."
            kat "Aren't you flattered, Miss Lynch."
            ver "Fuck off, you bat. That was disgusting."




        "Screw this hag, she's taking the load! [red]\[Kathleen -3\]":
            $ Kathleen_Affection -= 3
            $ Kathleen_Affection = clamp(Kathleen_Affection, 0, 30)
            show screen textbox2 with dissolve
            scene pr1105 with fade
            "I could barely string together three words in my head, but in my gut I knew I wanted one thing: Kathleen started this, I wanted her to end it."
            "No, more specifically, I wanted to drown the hag in my jizz until she couldn't breath anymore, but I'd settle with replacing that wicked grin with the gleam of a cum-spattered whore."
            kat "What are--"
            scene pr1106 with dissolve
            play sound "sound effects/spurt.wav"
            mc "Take it you hag--!"
            "The next thing I knew, my head was engulfed in a suffocatingly fuzzy feeling and my eyesight short circuited, plunging my mind into an abyss of purifying white."
            "I was ejaculating harder than I had ever before, with a dizzying intensity that almost made me lose my breakfast."
            play sound "sound effects/spurt.wav"
            mc "Nhhggaaa~!"
            scene pr1107 with dissolve
            mct "*huff* *huff* (H-holy shit!)"
            "Despite cumming more in my life than ever before, and the eviscerating gaze Kathleen was leveling at me, my dick somehow remained hard as titanium."
            "Still, as my good sense returned, I was hit with an alarm of panic at what I had done."
            mc "Uh... {i}*clears throat*{/i} you can't really blame me for that. You dosed me with that stuff, after all..."
            kat "...gh!"
            kat "No, I CAN'T, I suppose."

    scene black with fade
    stop music fadeout 1.5
    if not persistent.katCarnationInterviewReplay:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.katCarnationInterviewReplay = True
    "After cleaning up, the girls returned to their chairs as if nothing happened, while I wallowed in shame in mine."
    $ renpy.end_replay()
    scene pr1108 with blinds
    play music "music/cold-sober.mp3"
    kat "Well, that was an interesting distraction, but hardly a decisive measure."
    scene pr1109 with dissolve
    ver "You got be shitting me? All that was just for fun"
    scene pr1110 with dissolve
    kat "Well, both of you want it badly enough and you both seem to follow commands well...."
    kat "I'm satisfied either of you could help us have a very entertaining summer for the Club, but alas only one of you can be chosen."
    kat "After all, we only need three girls and only one spot remains..."
    scene pr1111 with dissolve
    kat "I've got it! Tomorrow night, you ladies will get a taste of what's to come. We'll hold an unofficial exhibition, a contest, to determine which of you will be our lucky carnation #3."
    scene pr1112 with dissolve
    kat "How does that sound?"
    ver "Like we don't have much of a choice."
    scene pr1113 with dissolve
    kat "That's a good way of looking at it actually. Will you be here at 7PM, Mrs. Long?"
    lucy "I will. I'll do... anything."
    scene pr1114 with dissolve
    kat "You'll be there too, [mcf]."
    mc "Yeah, I figured..."
    scene pr1115 with dissolve
    kat "Good. See yourself out? I've got a couple of things left to discuss with the girls here."
    "Happily! I'm glad that this bizarre meeting is over. Whatever she has planned for tomorrow be damned, I'll deal with it then."
    play sound "sound effects/notification.wav"
    $ met_veronica = True
    $ met_lucy = True
    show bioadd with dissolve
    $ renpy.pause(3, hard=True)
    stop music fadeout 1.5
    scene black with fade

label prRoseDateSetup:
    "..."
    scene pr1116 with dissolve
    "On my way out, I ran into a certain familiar face."
    scene pr1117 with dissolve
    play music "music/lobby-time.mp3"
    mct "(It's Rosalind!)"
    rose "Hello, Mr. [mcl]."
    mct "(Mr. [mcl]? She's already been chosen for the club... she could probably drop that now...)"
    scene pr1118 with dissolve
    mc "Good afternoon, Rose. What brings you here today?"
    "I tried my best to sound normal, but that witch's perfume still had its devilish hands all over me."
    scene pr1123 with dissolve
    rose "Mr. Byrnes had asked me to deliver some test results."
    scene pr1124 with dissolve
    mc "Test results? Aren't a little old to be taking a test?"
    "I groaned internally at my terrible joke."
    scene pr1125 with dissolve
    rose "Uh... {b}STI{/b} test results..."
    scene pr1124 with dissolve
    mct "(Christ, what else could she have meant you idiot.)"
    scene pr1122 with dissolve
    rose "How about you? I guess you decided to work here?"
    scene pr1126 with dissolve
    mc "I guess it was just too good of a deal to pass up."
    scene pr1123 with dissolve
    rose "That makes sense."
    scene pr1124 with dissolve
    "After the (extremely) shallow well of small talk had dried up, the two of us stood there fidgeting in silence."
    "I should probably do both of us a favor of releasing us from this social standstill, but part of me..."
    hide screen textbox2 with dissolve
    menu:
        "[gr]Ask her to get coffee with you.":
            show screen textbox2 with dissolve
            scene pr1119 with dissolve
            mc "Say, do you... have some free time?"
            mc "If you do, I was thinking maybe, do you want to get some coffee with me?"
            if roseTakeAdvantage == True:
                "Though, considering I used our meeting as a chance to shove my dick down her throat, she's probably not too keen on the idea."
            scene pr1127 with dissolve
            rose "Oooh."
            "Rosalind suddenly transitioned to a look of surprise."
            rose "Like a date you mean?"
            scene pr1128 with dissolve
            if toughness >= 19:
                mc "Call it whatever you want. I'd just like to get to know you better."
            else:
                mc "Just two people getting coffee."
            scene pr1129 with dissolve
            rose "..."
            if roseTakeAdvantage == False and roseTAapology == False:
                scene pr1130 with dissolve
                rose "Why not? I have an hour to kill. Do you know a place close by?"
                mc "I have a place in mind."
                jump prRoseDateCoffee

            if roseTakeAdvantage == True and roseTAapology == True:
                "Rosalind paused, thinking the matter over carefully."
                mct "(It takes this long to decide if you want to get a cup of coffee?)"
                scene pr1131 with dissolve
                rose "Eh... Sure, I have an hour to kill. Do you know a place close by?"
                mc "I have a place in mind."
                jump prRoseDateCoffee

            if roseTakeAdvantage == True and roseTAapology == False:
                scene pr1132 with dissolve
                rose "Sorry, I've got a couple of errands to run, and..."
                rose "Quite frankly, I don't think we should see each other outside of the club. I hope you understand."
                mc "...I do."
                scene pr1121 with dissolve
                rose "See you around, Mr. [mcl]"
                jump prRoseDateSkip


        "(Politely) End the conversation.":
            show screen textbox2 with dissolve
            scene pr1126 with dissolve
            mc "Well, it was nice seeing you again, Rose. I suppose we'll be seeing each other around."
            scene pr1122 with dissolve
            rose "You too, Mr. [mcl]."
            stop music fadeout 1.5
            jump prRoseDateSkip


label prRoseDateSkip:
    "..."
    scene black with fade
    "With my business at the Club concluded, I went home to wait out the aphrodisiac in my system."
    scene pr1133 with blinds
    "To say the least, it took a lot of effort to work though."
    scene pr1134 with dissolve
    "I killed a few hours."
    scene pr0040 with blinds
    "Took and shower."
    scene black with fade
    "And headed out to meet my mother for dinner."
    jump prCelebratoryDinner

label prRoseDateCoffee:
    $ roseMarried = True
    $ roseSeduceFlag = True
    scene black with fade
    stop music fadeout 1.5
    "..."
    scene pr1135 with blinds
    rose "I'll drive?"
    mc "I don't have a car, so if you prefer not to walk... please."
    scene pr1136 with blinds
    play music "music/george-street-shuffle.mp3"
    "The drive to Cafe Luca carried on in relative quiet, with both of us filling in the gaps of silence where we could with simple smalltalk."
    "All the while, I remained under the lust-charged side effects of Kathleen's aphrodisiac perfume."
    scene pr1137 with fade
    "I was thankful when we finally reached Cafe Luca, the open air being kinder to my condition than the cramp confines of Rosalind's car."
    scene pr1138 with blinds
    "...or so I thought."
    mct "(Uggh, this might've been a mistake)."
    "The whole time we were waiting to order, my eyes remained glued on Rosalind, indelicately tracing the curves of her body."
    "I did my best not to make it obvious and failed miserably. The finer points of subtlety aren't in my repertoire to begin with, let alone in this heightened state of arousal."
    scene pr1139 with dissolve
    "All I could hope is she'd interpret my wandering eye-line as an innocent attraction instead of the depraved eye-fucking it really was."
    scene pr1140 with dissolve
    rose "{i}*Clears throat.*{/i} A-hem!"
    rose "This... is a cute place. Do you come here a lot?"
    scene pr1141 with dissolve
    mc "Oh! I-it's, uh, one of my study spots."
    scene pr1140 with dissolve
    rose "What are you studying?"
    scene pr1142 with dissolve
    mc "Physics."
    scene pr1144 with dissolve
    rose "That's incredible. You must be really smart to study something like that."
    scene pr1141 with dissolve
    mc "Well, there's all kinds of smarts, right? For me, if it's not on the test, I'm a moron."
    scene pr1142 with dissolve
    mc "You wouldn't believe my lack of common sense."
    scene pr1140 with dissolve
    rose "Try me."
    scene pr1143 with dissolve
    mc "Just the other night, I dumped a pot of boiling water into a colander. Straight onto the kitchen floor. Totally didn't register that I wasn't standing over the sink."
    scene pr1145 with dissolve
    rose "Pfft-!"
    scene pr1140 with dissolve
    rose "Everyone's a {i}little{/i} absent-minded occasionally."
    scene pr1146 with dissolve
    mc "Try all the time."
    scene pr1147 with dissolve
    $ renpy.pause(0.5, hard=True)
    scene pr1148 with dissolve
    $ renpy.pause(0.5, hard=True)
    scene pr1149 with dissolve
    $ renpy.pause(0.5, hard=True)
    rose "Oh! Shoot!"
    scene pr1150 with dissolve
    mc "--!"
    "All it took was a simple accident to get my mind back on the topic of sex."
    scene pr1151 with dissolve
    "Just like that, vulgar images carpet bombed my brain."
    "Thoughts of Rosalind strapped into an industrial grade milker, feebly struggling to endure unending discomfort as her reddened, milk-spouting nipples chaffing under the unfeeling mechanical assault..."
    mct "(JESUS! What the fuck? It's like all I can think about is sex.)"
    mct "(Not just normal sex, either. Some real weird, fucked up shit too.)"
    scene pr1152 with dissolve
    mct "(What I wouldn't give to just dive head first into those sweater puppies, to knead and assault them, to pinch and prod...)"
    mct "(I wonder just what kind of sweet cries Rose would make...)"
    scene black
    show pr1153 with hpunch
    play sound "sound effects/slap2.wav"
    "{i}*Smaaaack!*{/i}"
    mct "(Stop perving out, you idiot!)"
    scene pr1154 with fade
    rose "Huh? What was that sound?"
    mc "Just... accidentally kicked my chair."
    scene pr1155 with dissolve
    rose "Oh, okay! Now, where were we?"
    scene pr1156 with dissolve
    mc "So... how about you? What do you do?"
    scene pr1158 with dissolve
    rose "I'm an office assistant, but would you believe I never actually held a serious job until this year?"
    rose "I married straight out of high school. Did the homemaker thing for most of my adult life."
    scene pr1159 with dissolve
    mc "So, you're... married?"
    "I don't know why that should surprise me, considering the club's focus on older women."
    scene pr1160 with dissolve
    rose "Only... technically. The bastard and I are separated now."
    "Her shift in expression when talking about her marriage was the only red flag I needed to avoid that landmine. She clearly doesn't want to talk about it."
    scene pr1159 with dissolve
    mct "(I should change the subject, I think.)"
    hide screen textbox2 with dissolve
    menu prRoseDateTopics:
        "Ask her what she does for fun." if prRoseDateHobby == False:
            show screen textbox2 with dissolve
            scene pr1161 with dissolve
            mc "What do you do for fun?"
            scene pr1162 with dissolve
            rose "You mean do I have any hobbies...? Nothing interesting."
            rose "You'd probably make fun of me."
            scene pr1163 with dissolve
            mc "Tell me. I won't laugh, promise."
            scene pr1162 with dissolve
            rose "It's such an old spinster thing to do, though."
            scene pr1163 with dissolve
            mc "What is it?"
            scene pr1158 with dissolve
            rose "I guess you could call couponing a hobby."
            scene pr1161 with dissolve
            mc "What, like those crazy people on TV?"
            scene pr1164 with dissolve
            rose "You said you wouldn't make fun of me!"
            mc "Sorry! Sorry!"
            scene pr1163 with dissolve
            mc "Couponing, huh?"
            scene pr1162 with dissolve
            rose "Don't knock it! You can save a lot of money being thrifty. When the purse strings are tight it helps."
            scene pr1165 with dissolve
            rose "Plus, it's meditative. Just you, a pipping hot cup of coffee, and a pair of scissors. There's a cathartic quality to cutting things out! Okay?"
            scene pr1156 with dissolve
            mc "Do you do anything else?"
            scene pr1158 with dissolve
            rose "I like to run sometimes, but a lot of people do."
            scene pr1159 with dissolve
            "The thought of Rosalind in a sports bra, chest heaving from over-exertion, skin glistening with a coat of sweat..."
            mct "(No! Bad [mcf]! Stop it!)"
            $ prRoseDateHobby = True
            jump prRoseDateTopics

        "Ask her how she learned about the Carnation Club." if prRoseDateSponsor == False:
            show screen textbox2 with dissolve
            "A particular detail from today's interview, if you could call it that, sprung to mind."
            "Both Lucy and Veronica found their way to the club via a sponsor. If I recall correctly, she mentioned a relief fund when we first met."
            scene pr1161 with dissolve
            if toughness >= 20:
                mc "So, I've got a question, but if it's too personal, just tell me to get bent."
            else:
                mc "So, I've got a question. If it's too personal to answer, I understand."
            scene pr1158 with dissolve
            rose "Just ask it."
            scene pr1159 with dissolve
            mc "I'm still learning about the Club and how it works. How did you find out about it? You said something about a relief fund?"
            scene pr1166 with dissolve
            rose "Hmm... yeah."
            scene pr1158 with dissolve
            rose "The Eden Women's Relief Fund. You haven't heard of it?"
            scene pr1159 with dissolve
            mc "No, I don't think I have."
            scene pr1158 with dissolve
            rose "It's one of those charities you can donate to when you're checking out at the grocery store. They have a pretty broad mission: helping women in need."
            rose "They do all sorts of things. Help single mothers in debt secure low-interest loans, help transition domestic abuse survivors to living independently, help pay for rehab for women with substance abuse problems. Those kind of things."
            scene pr1161 with dissolve
            mc "I see. Seems like an amazing charity, but how does it connect to the Club?"
            scene pr1158 with dissolve
            rose "Uh, Mrs. Pulman, K-kathleen, she's the fund's chairwoman. She manages and directs the foundation."
            scene pr1159 with dissolve
            mc "You got to be kidding me. That piece of work is the head of a charity?"
            scene pr1167 with dissolve
            rose "Piece of work? What do you mean?"
            scene pr1168 with dissolve
            mc "She's got more than a few screws loose. You're telling me she didn't parade you around nude, berate and humiliate you, maybe use you as a piece of furniture?"
            scene pr1169 with dissolve
            rose "Heavens no! Why would she do all of that? The only time we met, she told my circumstances put me low on the relief fund's priority list, but that there was a way for me to jump ahead."
            scene pr1160 with dissolve
            rose "Then I... uh, meet with Mr. Beaufort a few times, and then you... and here we are."
            mct "(Mr. Beaufort....? Oh! She means Killian. I haven't heard anyone call him that. Ever.)"
            scene pr1157 with dissolve
            mc "I see..."
            scene pr1158 with dissolve
            rose "Does that answer your question?"
            scene pr1159 with dissolve
            mc "It did, thank you Rose."
            $ prRoseDateSponsor = True
            jump prRoseDateTopics

    scene pr1170 with dissolve
    rose "{i}*Clears throat.*{/i} A-hem!"
    "Rosalind's body language had suddenly taken a shift."
    rose "I got, uh... I mean, I can't help but {b}notice{/b}, Mr. [mcl]..."
    "She had shifted from being laid back to tripping over her words."
    mc "What? What is it...?"
    scene pr1171 with dissolve
    mc "What are yo--"
    rose "Ssssh, relax."
    "Rosalind had started a game of footsie from across the table. Under the best of circumstances, having a beautiful woman's foot pawing at my inner thigh would be exciting, but with where my headspace was at..."
    scene pr1172 with dissolve
    rose "I can't help but notice you've been staring at my breasts all afternoon."
    mct "(Shit! I knew she noticed, but I didn't expect her to openly call me on it.)"
    mct "(Apologize! It's the only thing I can do!)"
    scene pr1173 with dissolve
    mc "I'm sorry. It's inexcusable, really, uh--!"
    scene pr1174 with dissolve
    rose "No, no, i-it's fine! I don't... I don't {i}mind{/i} {b}you{/b} staring."
    scene pr1175 with dissolve
    scene pr1176 with dissolve
    scene pr1175 with dissolve
    mc "Kh...!"
    "Bringing my mind back to the action happening beneath the table, Rose suddenly brushed the arch of her foot across the tent I was pitching in my pants."
    mct "({b}Right{/b}! She's the one coming on to {i}me{/i} right now, never mind her calling me out!)"
    "Still, You got to be kidding me... I'm seeing more action this week than I have had all year!"
    scene pr1177 with dissolve
    rose "Oh my... did I... make you like THAT?"
    scene pr1178 with dissolve
    "Well, the real answer to that question is actually no. That sadistic hag is the reason it's like this, but I'll be damned if I'm telling Rose that an old lady got me hard over an hour ago."
    hide screen textbox2 with dissolve
    menu:
        "Tell her she's right.":
            show screen textbox2 with dissolve
            "In a normal, less unusual situation it's not like she'd have a problem getting me going."
            if toughness >= 20:
                mc "Yeah, you've got me harder than a rock."
            elif toughness >= 11:
                mc "What? Can't you tell?"
            else:
                mc "Uh, yeah. You did..."
            scene pr1179 with dissolve
            rose "I {b}thought{/b} so."


        "Don't say anything.":
            show screen textbox2 with dissolve
            "So instead, I let the moment pass in silence."
            scene pr1179 with dissolve
            rose "No need to say anything, I can tell..."

    scene pr1178 with dissolve
    "I have no idea where this was coming from."

    if roseTakeAdvantage == True:
        "Truth be told, I was shocked she accepted my invitation for coffee in the first place, considering what I made her do the other night."
        "I'm also not stupid enough to think a mature, adult woman like Rosalind would be interested in a college kid like me."
    else:
        "Truth be told, I was a little surprised she accepted my invitation for coffee in the first place."
        "I'm not stupid enough to think a mature, adult woman like Rosalind would be interested in a college kid like me."

    "...I mean, would she? And if she was, this approach is weird."
    hide screen textbox2 with dissolve
    menu:
        "What's going on? [red]\[Toughness -1\]":
            $ toughness -= 1
            $ toughness = clamp(toughness, 0, 30)
            show screen textbox2 with dissolve
            mc "Rose, I'm a little confused here..."
            scene pr1174 with dissolve
            rose "Basically, I've lived my whole life treading water."
            scene pr1178 with dissolve
            mc "I'm not following I'm afraid."
            scene pr1179 with dissolve
            rose "...don't think too hard about it, sweetie. What I'm saying is... I'm working through some things."

        "Who cares, just roll with it. [gr]\[Toughness +1\]":
            $ toughness += 1
            $ toughness = clamp(toughness, 0, 30)
            show screen textbox2 with dissolve
            "Who gives a damn about the WHY, the important part is the IS."
            "What she IS is currently flirting with me. Let's not throw gum in those works by over-thinking things, eh?"

    scene pr1175 with dissolve
    scene pr1176 with dissolve
    scene pr1175 with dissolve
    rose "It feels so large and stiff, like it's struggling to break out. Doesn't it... hurt?"
    mc "A little, yeah."
    scene pr1176 with dissolve
    scene pr1175 with dissolve
    rose "Aww, poor baby. I wish I could do something to help."
    scene pr1180 with dissolve
    rose "Oh, shoot! I've got to go or I'll be late!"
    mct "(YOU'RE KIDDING ME?!)"

    if roseTakeAdvantage == True:
        "Was she just having fun at my expense? Was this revenge for the night we met?"
    else:
        "Was she just having fun at my expense?"
    scene pr1181 with dissolve
    mc "Uh, you're leaving, just like that...?"
    mc "You were making fun of me, right? That's what this was?"
    scene pr1182 with dissolve
    rose "Oh, no! I wasn't! I really do like you, sweetie. You're cute."
    scene pr1183 with dissolve
    rose "Honestly, I don't normally do things like {b}that{/b}, but... I'm trying to live differently. I really didn't mean to take it that far, but it was so, SO much fun."
    scene pr1184 with dissolve
    "Fwup."
    scene pr1185 with dissolve
    rose "I hope you'll forgive me, Mr. [mcl]."
    scene pr1184 with dissolve
    "*Smoooooch*"
    scene pr1185 with dissolve
    rose "Now, I really have to run. Thanks for coffee."
    scene pr1187 with dissolve
    "Left alone with my coffee and a serious case of blue balls, I was finding Rosalind a woman difficult to qualify."
    $ history_rosalind = "From what little I have to go off of, Rosalind is a woman down on her luck. While getting coffee, I got {i}real{/i} familiar with her foot."
    $ unread_rosalind = True
    play sound "sound effects/notification.wav"
    show bioupdate with dissolve
    $ renpy.pause(3, hard=True)
    mct "(I've got to do something about what's happening in my pants...)"
    scene pr1133 with blinds
    stop music fadeout 1.5
    "I had a little time to kill before dinner with my mom, so that's exactly what I did."
    jump prCelebratoryDinner

label prCelebratoryDinner:
    $ date = "may12night"

    scene black with fade
    "......"
    "..."

    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionrosalind04 with blinds
    $ renpy.pause(6, hard=True)
    stop sound
    scene pr1199 with blinds
    play music "music/ill-remember-you.mp3"
    show may12night with squares
    show screen textbox2 with dissolve
    show screen qmenu with dissolve
    kil "Mm_____~ mm____~ Hey, da, da, da~"
    scene pr1200 with dissolve
    kil "I lost myself on a cool damp night~ I gave myself in that misty light~"
    kil "Was hypnotized by a strange delight~ Under a lilac tree~"
    kil "I made wine--"
    scene pr1201 with dissolve
    mc "You play better than you sing, you know."
    scene pr1191 with dissolve
    kil "I sing better than you, asshole"
    scene pr1192 with dissolve
    mc "You play better too. I never took the lessons seriously, but you..."
    scene pr1193 with fade
    mc "You really threw yourself into them. Hardest I've ever seen you work."
    scene pr1194 with dissolve
    kil "It was a lot of fun! Not to sound gay, but..."
    scene pr1195 with pixellate
    kil "The memories of Vicky teaching us to play are my best."
    mc "She had A LOT of patience, that's for sure."
    scene pr1196 with pixellate
    mc "Are you sure it wasn't because she was your first crush?"
    kil "It wasn't like that."
    mc "Really? You sure acted like it when we were kids. I remember a pair of panties she had left laying on the washer..."
    kil "S-shut up! It's called going through puberty, you ass!"
    mc "Relax, I'm just teasing you."
    scene pr1197 with dissolve
    vic "Hey boys, dinner's ready."
    kil "Mrs. [mcl]! Uh, how long have you been standing there?"
    scene pr1198 with dissolve
    vic "About the time you mentioned my panties."
    kil "Gh...!"
    vic "Sorry, didn't mean to eavesdrop, but I was enjoying the sight of you two together at the piano."
    vic "Now, let's say we eat while it's still hot. Sound good?"
    scene pr1202 with dissolve
    kil "Thanks for the meal, Mrs. [mcl]!"
    "It was a gesture Ian had made hundreds of times. It was something he'd always do before he'd eat here, be it breakfast, lunch, or dinner."
    "...back when he was a well-behaved, polite kid."
    scene pr1203 with dissolve
    vic "Don't thank me until you've tasted it, Ian."
    "......"
    scene black with fade
    stop music fadeout 1.5
    "..."
    scene pr1204 with dissolve
    play music "music/crinoline-dreams.mp3"
    "Dinner turned out nice, with good food and warm company. Turned out Mom had run into Ian by happenstance at the farmer's market earlier in the day and had invited him to join us."
    scene pr1205 with dissolve
    "It was nice to have him there. Killian on his best behavior, reminded me of simpler days that I took for granted."
    scene pr1206 with blinds
    vic "I'm going to draw myself a bath. You boys don't get into too much trouble while I'm away, okay?"
    scene pr1207 with dissolve
    kil "When have we ever gotten into trouble, Vicky?"
    scene pr1208 with dissolve
    vic "Ha! You should be a comedian, Ian. That or you should be a shit salesman."
    scene pr1209 with dissolve
    kil "You know It's a shame you didn't get her good humor, [mcf]"
    scene pr1210 with dissolve
    mc "What are you talking about? I'm a funny guy."
    scene pr1211 with dissolve
    "......"
    "..."
    scene pr1212 with dissolve
    kil "Pffthahaha!~~ I'll give you this, you try."
    mc "Yeah, whatever. Jerk."
    scene pr1213 with dissolve
    kil "So! Are you excited for the trial exhibition tomorrow?"
    scene pr1214 with dissolve
    "His question had caught me off guard. Thinking back at that video I watched..."
    "Assuming it's going to be anything like that, to have him openly ask about it, as casual as asking about going to a concert, felt unreal."
    hide screen textbox2 with dissolve
    menu:
        "I'm curious, to say the least. [gr]\[Toughness +1\]":
            $ toughness += 1
            $ toughness = clamp(toughness, 0, 30)
            show screen textbox2 with dissolve
            "I couldn't hide from a simple fact: deep down, part of me reveled in the debauchery shown on that video. It was far away from my quiet student life. It was... exciting."
            scene pr1215 with dissolve
            mc "I'm... interested, to say the least."
            scene pr1217 with dissolve
            kil "Really? That's great! I was afraid you'd be slow to come around."
            scene pr1216 with dissolve
            mc "I'm not on team gang-bang yet, mind you. Still, if I'm going to survive working there, I'm going to need to learn to be flexible with my hang ups."
            scene pr1219 with dissolve
            kil "Psssh, are you for real? You even look at sex parties clinically."

        "No, I'm not! [red]\[Toughness -1\]":
            $ toughness -= 1
            $ toughness = clamp(toughness, 0, 30)
            show screen textbox2 with dissolve
            "A tinsy, tiny part of me did find the prospect of tomorrow's exhibition exciting. I would be lying to say otherwise, but the overwhelming feeling going into tomorrow night for me was anxiety."
            scene pr1216 with dissolve
            mc "Can't say I am, no."
            scene pr1218 with dissolve
            kil "Yeah, I figured. You're going to be slow to come around. That's in your nature."
            scene pr1217 with dissolve
            kil "Trust me though, it's going to be A LOT of fun, buddy. You'll feel like a king coming out of it. I guarantee it."
            scene pr1220 with dissolve
            mc "Well, not like I have much of a choice anyway."
            scene pr1219 with dissolve
            kil "That's simply not true. You have a choice. You always do, idiot. Not like you're the first person to do something you don't enjoy for profit."

    scene pr1221 with dissolve
    mc "Will you be there too?"
    scene pr1222 with dissolve
    kil "Of course, I love those things. It's not just me either, Uncle Chuck is sure to be there. He never misses one."
    scene pr1216 with dissolve
    mc "I haven't seen him since high school..."
    mc "It blows my mind that he's got a hand in this. He seemed so... respectable."
    scene pr1217 with dissolve
    kil "Fuhahaha, you mean to say he's a dirty old man? You should call him that when you see him. He'd just die."
    scene pr1219 with dissolve
    kil "The old bastard cultivates this upstanding man of science bullshit, but he's a tried and true philanderer at heart."
    scene pr1221 with dissolve
    mc "He got you into this club business?"
    scene pr1222 with dissolve
    kil "Yep, my membership was a present for my 18th birthday three years ago. I fell into working there not too long after that. It's more fun to be on that end of things. The liberties you take with the girls doesn't cost you for one."
    scene pr1220 with dissolve
    mc "You shouldn't say things like that so shamelessly..."
    scene pr1219 with dissolve
    kil "What? Why shouldn't I? To thine own self be true."
    kil "Anyway, tomorrow should be interesting. Kat always cooks up some fun games."
    scene pr1223 with dissolve
    mc "You want anything?"
    kil "No, I'm good. Thanks."
    scene pr1224 with irisin
    mc "You have any idea what's going to happen tomorrow?"
    scene pr1225 with dissolve
    kil "Nope. Kat's got a deep bag of tricks though. It's pretty much a honed talent of hers, coming up with colorful ways to make perverts salivate."
    scene pr1226 with dissolve
    mc "She's twisted is more like it."
    scene pr1227 with dissolve
    kil "No argument here. She's got August and Uncle Chuck beat at least. Probably not Warren though... that guy..."
    kil "Well, I'd stick closer to Jacob if were you."
    scene pr1228 with dissolve
    mc "What does that mean?"
    scene pr1222 with dissolve
    kil "Just that if you ever need security for something, Jacob is the more delicate of the two."
    scene pr1220 with dissolve
    mc "Why would I ever need to go to security?"
    scene pr1218 with dissolve
    kil "It doesn't happen often, but if a club member steps out of line with one of the girls--"
    scene pr1216 with dissolve
    mc "What constitutes as {i}out of line{/i}?"
    scene pr1218 with dissolve
    kil "You'll know it if you see it. The lines of acceptable behavior gets blurred against the backdrop of all the sex, but they're there."
    kil "Throw a bunch of rich assholes who think they're untouchable in the mix and you have a powder keg."
    scene pr1219 with dissolve
    kil "Kathleen will have you believe your primary role is keeping the girls in line and working, but your true job is always their well being. Look out for them, man. This place ain't easy."
    mct "(That's... surprisingly compassionate for Ian.)"
    scene pr1229 with dissolve
    mc "...thanks, Ian."
    scene pr1230 with dissolve
    kil "What for?"
    scene pr1229 with dissolve
    mc "The way you put it makes me feel like I can do this job without becoming a heartless asshole."
    play sound "sound effects/door-openclose.wav"
    "{i}*Click, skreeeek*{/i}"
    "The opening of the hallroom bathroom door cut our candid conversation about the club short."
    scene pr1231 with dissolve
    vic "You boys want to stay for a movie?"
    scene pr1232 with dissolve
    kil "I would love to, Mrs. [mcl]."
    mc "Yeah, why not.."
    kil "What's on the marque for the night?"
    scene pr1233 with dissolve
    vic "I'm feeling like a little Fulci. How about you, boys?"
    scene pr1234 with dissolve
    kil "That sounds good to me."
    scene pr1235 with dissolve
    mc "*sigh* ...I'll defer to the majority then."
    mct "(It's always {i}Italian{/i}.)"
    scene pr1236 with dissolve
    vic "Great, I'm going to go get my pajamas on first and then I'll join you."
    scene black with fade
    "......"
    stop music fadeout 1.5
    "..."
    "After the movie, Ian was kind enough to drive me home."
    scene player-room-dark with blinds
    "In spite of the insanity earlier in the day, dinner with mom and Ian proved to be a nice conclusion for the day."
    "Tomorrow night, that insanity resumes, but talking with Ian did alleviate some of my anxiety about my role at the club."
    "As long as I think of my role as keeping the girls safe, I might be able to rationalize what I'm going to be party to."
    "...and maybe I won't feel so bad about enjoying it, either."
    mct "(Anyway, it's late, and I should get to bed.)"
    scene black with fade
    "........."
    "......"
    "..."

    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionveronica02 with blinds
    $ renpy.pause(6, hard=True)

#------------------------------------------------------------------------------#
#                                   May 13                                     #
#------------------------------------------------------------------------------#


label prMay13start:
    $ date = "may13night"

    stop sound
    scene club-fr-night with blinds
    show may13night with squares
    show screen textbox2 with dissolve
    show screen qmenu with dissolve
    "The next night..."
    scene pr1237 with blinds
    mc "...man, I hate the feel of a suit. Damn thing's so stuffy."
    scene pr1238 with blinds
    kil "You'll get used to it. The bosses insist we maintain standards, even if it's not an official event."

    play music "music/hold-on-a-second.mp3"
    scene pr1239 with blinds:
        subpixel True
        yalign 0.7
        xalign 0.6
        linear 3 yalign 0.1

    kil "Besides, don't be like that. You look good in it."
    scene pr1240 with dissolve
    mc "It's just a little embarrassing is all."
    scene pr1241 with dissolve
    kil "Well, suck it up. It's better than what the girl's have to wear."
    scene pr1240 with dissolve
    mc "....damn. That does make me sound like a whiny bitch, doesn't it?"
    scene pr1242 with dissolve
    kil "It could be worse. You could be a under dressed whiny bitch."
    scene pr1243 with dissolve
    mc "Very funny, you prick."
    scene pr1241 with dissolve
    kil "Anyway, this is probably about as low-key as it could get around here. Kat only invited the girl's sponsors, she wants to give them a proper thank you for the referrals."
    kil "Which means you'll have to help schmooze a couple of old assholes. How good are you at rimjobs?"
    scene pr1244 with dissolve
    kil "Speaking of old assholes..."
    scene pr1245 with dissolve
    chuck "Old asshole, huh?"
    scene pr1246 with fade
    chuck "Is that any way to speak about your adoring uncle?"
    chuck "Well, I'm not old at least, bfahhahaha!"
    scene pr1247 with dissolve
    chuck "[mcf]!"
    scene pr1248 with dissolve
    chuck "It's so good to see you, lad. It's been quite some time."
    if perk_strongman == True:
        chuck "Not an ounce of fat on you. You're still keeping in shape, eh? Bfhahahaha!"
    else:
        chuck "You look proper and healthy, my boy. Probably could do to eat a bite or two though. Bfhahahaha!"
    scene pr1249 with dissolve
    chuck "I'm so glad you took me up on my offer. Feel free to call me 'Uncle Chuck' from now on, okay?"
    hide screen textbox2 with dissolve
    menu:
        "Sure thing, Uncle Chuck. [gr]\[Chuck +1\]":
            $ Chuck_Friendship +=1
            $ Chuck_Friendship = clamp(Chuck_Friendship, 0, 10)
            $ chuck_polite = False
            $ chuck_uncle = True
            scene pr1250 with dissolve
            show screen textbox2 with dissolve
            mc "Uh... whatever you say, {b}Uncle Chuck{/b}."

        "How are you, Sir? [red]\[Chuck -1\]":
            $ Chuck_Friendship -=1
            $ Chuck_Friendship = clamp(Chuck_Friendship, 0, 10)
            show screen textbox2 with dissolve
            scene pr1250 with dissolve
            mc "Uh... it's good to see you too.  How are you, sir?"
            scene pr1249 with dissolve
            chuck "Good lad, good. In fact, I'm doing better than good."

    scene pr1251 with dissolve
    kil "What's up, uncle? Shouldn't you be entertaining?"
    scene pr1252 with dissolve
    chuck "Actually, I've come to fetch you lads. Well, come to fetch [mcf]. Kathy wants you to help Warren set up something."
    scene pr1253 with dissolve
    kil "I bet... heavy lifting, right? Why am I always saddled with that shit?"
    scene pr1254 with dissolve
    mc "It's probably because your ability to lift heavy objects is one of your finer points."
    scene pr1255 with dissolve
    "I was suddenly knocked off balanced by a thunderous pat on the back, Dr. Chuck overly pleased with my response to Ian's annoyed reaction."
    chuck "Pfhtt--! Took the words straight from Kathy's mouth already, have you lad? Hahahaha!"
    scene pr1256 with dissolve
    mc "Well, if he's doing that, what are you {i}fetching{/i} me for?"
    scene pr1257 with dissolve
    chuck "As my nephew would put it, {i}to sweat your ass off helping schmooze some old assholes{/i}."
    mc "...huh?"
    scene black with fade
    stop music fadeout 1.5
    "......"
    "..."
label prLeisureTime:

    if _in_replay:
        show transitionhousegirls with cmet
        show screen textbox2 with dissolve
        "Please set [mcf]'s personality (toughness score) for this replay."
        hide screen textbox2 with dissolve
        menu:
            "Nice guy (Toughness: 0)":
                $ toughness = 0
            "Mischevious (Toughness: 18)":
                $ toughness = 18
            "Asshole (Toughness: 30)":
                $ toughness = 30
        scene black with fade
        show screen textbox2 with dissolve

    "What Dr. Chuck had meant by that was that we were joining the night's special guests in the steam room for a little relaxation while Kathleen got the last minute preparations for the contest done."
    scene pr1280 with blinds
    "More explicitly, I was to get acquainted and make small talk with a couple of naked old dudes. And what's more..."
    scene pr1259 with dissolve
    play music "music/cello-suite-No-1-G-Major-Prelude.mp3"
    "*Mch... mgh... slsh... ehch... mph, schkkk....*"
    "One of the men was Isaak Miller, who I understood to be an admission officer at St. Ives Academy."
    "The gentleman availing himself to the services of one of the club's year round whores - or as Dr. Chuck put it, {b}house girl{/b} - was Samson Garcia, who didn't need an introduction."
    "I had failed to make the connection when I heard his name yesterday, but Samson Garcia was a relatively famous infomercial star and has-been, once starring in a string of popular low-budget action films before I was born."
    "I might add, the kind of b-movie shlock that I always wanted to watch on our movie nights, but inevitably got vetoed by my mom and Ian."
    chuck "Good! You're all introduced"
    chuck "I'd introduce you to Harper here, but she's got her mouth full."
    scene pr1260 with dissolve
    sam "Nice to meet you, kid. Any friend of Chuck is a friend of mine."
    "*Schkkk, mph, mmm~*"
    scene pr1261 with dissolve
    isak "Same. Good to meet you, Mr. [mcl]."
    scene pr1262 with slideleft
    chuck "Here, lad. Enjoy the high life a little."
    scene pr1263 with dissolve
    mc "I don't really..."
    "I don't know what it was about the look on his face, but it rebuffed any attempt at saying no."
    scene pr1264 with dissolve
    mc "Sure. When in Rome, right?"
    sam "Allow me to light that for you, kid."
    scene pr1265 with dissolve
    play sound "sound effects/lighter-flick.wav"
    "*Schnick, chk-!*"
    scene pr1266 with dissolve
    "Up until this point, I had never smoked anything in my life, legal or otherwise."
    mct "(This isn't so bad--)"
    scene pr1267 with dissolve
    mc "*{i}Cough, cough!{/i}*"
    mc "*{i}Cough, cough, cough!{/i}*"
    chuck "Bahahaha! There, there lad. Breath. You'll be alright."
    scene pr1268 with dissolve
    sam "You're not supposed to suck it down, kid. Just hold it in your mouth. Didn't anyone teach you that?"
    mc "Sorr- *{i}Cough, cough!{/i}* Sorry, this is my first time."
    sam "Well, not a bad place to start, these things cost $7,500 a box."
    mc "E-excuse me?!"
    scene pr1269 with dissolve
    isak "You're just shamelessly bragging, like you always do, you buffoon."
    "The small, bookish man who had previously taken a backseat in the conversation had used this opening to bare his fangs at his cohort."
    scene pr1268 with dissolve
    sam "I guess you're right about that, Ike. My ex-wife always called me a braggart. I don't see the harm in that though. Hahaha!"
    "However, either by stupidity or plain indifference, the giant payed no heed to Isaak's venomous words and took them in good humor. In a way, his disposition reminded me of a dimmer Dr. Chuck."
    scene pr1270 with pixellate
    mct "(Someone like Dr. Chuck, but with muscles...)"
    "That cursed image popped into my head."
    scene pr1271 with pixellate
    chuck "[mcf] here actually worked as a tutor previously."
    scene pr1272 with dissolve
    isak "Oh, is that so? Educating children is a noble, laudable pursuit... but it is a tiresome one, don't you find?"
    scene pr1273 with dissolve
    isak "Can't beat all the desperate mothers looking to get their kids enrolled though..."
    isak "Do you still work as a tutor, Mr [mcl]? You and I could come to a beautiful arrange--"
    scene pr1274 with dissolve
    mc "I'm afraid not, I quit that job to work here actually."
    "Despite how fascinating it was to see the man seamlessly transition into a flagrant pervert, I didn't have the stomach to let him finish his proposition."
    isak "Oh... that's too bad..."
    scene pr1275 with dissolve
    sam "That's some real ver-VERTICAL movement for you, kid! Good job! You're going to love it here."
    sam "You remind me a little of myself you know. I started out with nothing, just the burning desire to be the best..."
    scene pr1276 with dissolve
    sam "From body builder, to movie star, to a fitness equipment empire! You got to have hunger kid if you want to get anywhere..."
    mct "(I bet if I let him go on, he'll never stop talking...)"
    scene pr1277 with dissolve
    hide screen textbox2 with dissolve
    menu samschmooze:

        "{color=#FF1493}\[Social Chameleon]{/color} (Lie) I love your movies. [gr]\[Sam +1\]" if perk_socialChameleon == True:
            $ Sam_Friendship += 1
            $ Sam_Friendship = clamp(Sam_Friendship, 0, 10)
            show screen textbox2 with dissolve
            mc "Is that so, Mr Garcia? I loved your movies as a kid. In fact, I love them even now."
            mc "Inferno of Surrender, the big set piece with the burning skyscraper, THAT was an exciting movie."
            mct "(Fuck, I hope I  got the title to that shitty movie right. They played it on the movie channel all the time, but I never really paid attention to it...)"
            scene pr1275 with dissolve
            sam "Oh, that's always been a fan pleaser. Let me tell you..."


        "Thank you for the advice.":
            show screen textbox2 with dissolve
            mc "Hunger. Right. Uh, thank you for the advice, Mr. Garcia. I'll try to keep that in mind."
            scene pr1276 with dissolve
            sam "Oh, there's more to it than wanting it, kid. You've also got to..."

        "{color=#696969}\[Social Chameleon] (Lie) I love your movies.{/color}" if perk_socialChameleon == False:
            jump samschmooze

    scene pr1278 with dissolve
    play sound "sound effects/spurt.wav"
    with flash
    play sound "sound effects/spurt.wav"
    with flash
    sam "Gaaaah-! Shit! That's the stuff!"
    isak "Thank god! Saved by a blowjob! If you ever show any interest, he'll never shut up."
    scene pr1279 with dissolve
    sam "Aaaaah~ you want a go, buddy?"
    isak "Absolutely not!"
    sam "Your loss then."
    $ renpy.end_replay()
    if not persistent.HarpSaunaBJGallery:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.HarpSaunaBJGallery = True
    scene black with fade
    "The dance between them was an odd one, bordering on a comedy routine that continued until Warren came to retrieve us."
    "Our presence was requested in the exhibition hall."
    stop music fadeout 1.5
    "......"
    "..."
    scene pr1281 with blinds
    play music "music/i-knew-a-guy.mp3"
    play sound "sound effects/notification.wav"
    $ met_samson = True
    $ met_isaak = True
    show bioadd with dissolve
    $ renpy.pause(3, hard=True)
    "The walk to the exhibition hall provided the opening I needed to ask a question that had been formulating in my mind all night, on the topic of what we had all gathered here for."
    hide screen textbox2 with dissolve
    menu:
        "Ask Isaak about Lucy":
            show screen textbox2 with dissolve
            "Something about Lucy struck had struck me as odd, so I turned to the bookish pervert for answers."
            scene pr1282 with dissolve
            mc "Mr. Miller, I was curious about something."
            scene pr1283 with dissolve
            isak "Oh? What is it? If it's something I can help you with, I'd be delighted to answer."
            scene pr1284 with dissolve
            mc "It's about one of the performers tonight, more specifically the one you scouted."
            scene pr1285 with dissolve
            isak "Ah, yes. Mrs. Lucy Long..."
            scene pr1286 with dissolve
            "Just the mere mention of the raven-haired schoolteacher had a clear effect on the man, sending him down a path of perverted reverie I could only imagine."
            scene pr1287 with dissolve
            isak "What about her, Mr. [mcl]?"
            scene pr1286 with dissolve
            mc "You two work together, right? She's your co-worker at St. Ives?"
            scene pr1289 with dissolve
            isak "That's correct, yes. I've known her... well, going on five years now I think. She's an excellent educator if I say so myself, beloved by both her students and peers."
            scene pr1286 with dissolve
            mc "Why did you sponsor her tonight then?"
            scene pr1287 with dissolve
            isak "Why? What a funnny question. To do my dear co-worker and friend a favor. As you know, she's looking to enroll her kid at St. Ives Academy, but unfortunately, he falls short in almost all the areas we demand to qualify for enrollment."
            isak "It's sad, really..."
            scene pr1286 with dissolve
            mc "So she couldn't get her son into the very school she teaches at? You couldn't pull any strings?"
            scene pr1289 with dissolve
            isak "What? What do you think I'm doing here. This is me making an exception. Another, reason..."
            scene pr1288 with dissolve
            isak "Besides, she's an educator beloved by both her students and peers... wouldn't it be fun to see that conceited bitch get taken down a peg or two?"
            isak "We'll see which one of us is the true pervert, won't we?"
            scene pr1286 with dissolve
            "He said, seemingly directing an offhanded comment at no one, leaving me feeling gobsmacked."
            "Without a doubt, this man is a loathsome predator. I suppose that's the true nature of the club, taking advantage of women in disadvantageous positions, but..."
            "To target a woman you know with a thinly veiled vendetta somehow seems even more wretched."
            scene pr1297 with dissolve
            kat "[mcf]!"
            "As we were finishing our conversation, I heard a growingly familiar voice call out my name."


        "Ask Samson about Veronica":
            show screen textbox2 with dissolve
            "Something about the brawny, defiant woman I had met yesterday had struck me as odd, so I turned to the self-obsessed has-been for an answer."
            scene pr1290 with dissolve
            mc "Hey, Mr. Garcia... I've got a question about the woman you scouted for the club."
            scene pr1291 with dissolve
            sam "Ah, yes. Veronica. She's beautiful, right kid? I've known plenty of female body-builders, but she takes the cake. Fierce as a whip too."
            scene pr1292 with dissolve
            mc "How'd you convince a woman like that to take part in something like this?"
            "She wore her contempt as plain as day yesterday, but she was nevertheless here. If her business is failing, there's gotta be other ways to correct course than {i}this{/i}."
            scene pr1293 with dissolve
            sam "Honestly, I don't know, but it wasn't too hard if you would believe it. She contacted me recently looking for an investor to pull her from the hole she's in."
            scene pr1294 with dissolve
            sam "Naturally, I told her I wasn't interested. Who'd be stupid enough to invest in a business that was hemorrhaging money without any real plan to fix it? That's when I brought up the club..."
            scene pr1295 with dissolve
            sam "Oddly enough, she jumped at the opportunity. Didn't blink. Didn't waffle. I suppose that's the kind of woman she is. Incapable of doubt, always moving forward..."
            scene pr1292 with dissolve
            mc "That seems... odd."
            scene pr1293 with dissolve
            sam "I agree. I was 99 percent sure she would've clocked me for even suggesting it, but here we are."
            scene pr1295 with dissolve
            sam "Honestly, I can't {i}wait{/i} to see that haughty bitch brought down to her knees..."
            scene pr1292 with dissolve
            "There's obviously more to their history than he's letting on, a man like Samson doesn't hide their ulterior motives very well."
            "Not that he has to, being amongst friends."
            scene pr1296 with dissolve
            kat "[mcf]!"
            "As we were finishing our conversation, I heard a growingly familiar voice call out my name."

    scene pr1298 with dissolve
    kat "I have a task for you."
    scene black with fade
    stop music fadeout 1.5
    "....."
    "..."
    scene pr1299 with blinds
    play music "music/horrible.mp3"
    ver "I can dress myself. Why do I need a chaperone?"
    scene pr1300 with dissolve
    mc "You heard Mrs. Pulman..."
    scene pr1301 with dissolve
    ver "{i}You heard Mrs. Pulman{/i}..."
    scene pr1299 with dissolve
    ver "Damn, you sound like a whiny child."
    scene pr1300 with dissolve
    mct "(Christ, she's got a bad attitude. What the hell did I ever do to her?)"

    if prVero_Facial == True:
        scene pr1258 with pixellate
        "..."
        mct "(Oh, yeeeeah...)"

    scene pr1302 with dissolve
    mc "*sigh* Mrs. Pulman wanted me here to make sure everything is applied properly."
    "After calling me over, Kathleen had explicit instructions for me. I was to help Veronica to get ready for the opening event, while Killian was to help Lucy."
    scene pr1300 with dissolve
    mc "She's afraid you won't secure them properly."
    scene pr1303 with dissolve
    ver "Mmn..."
    "Confronted with the fact that I would remain, Veronica shot me a withering stare, like she was sizing me up for a fight."
    scene pr1299 with dissolve
    ver "{b}Fine{/b}. Not like it matters. I'll go ahead and get dressed."
    scene pr1300 with dissolve
    hide screen textbox2 with dissolve
    menu:
        "Turn around and give her some privacy. [gr]\[Veronica +1\] [red]\[Toughness -1\]":
            $ Veronica_Affection += 1
            $ Veronica_Affection = clamp(Veronica_Affection, 0, 40)
            $ toughness -= 1
            $ toughness = clamp(toughness, 0, 30)
            show screen textbox2 with dissolve
            jump prFaceOffVerGentleman

        "Enjoy the show. [gr]\[Toughness +1\]":
            $ toughness += 1
            $ toughness = clamp(toughness, 0, 30)
            show screen textbox2 with dissolve
            jump prFaceOffVerPig

label prFaceOffVerGentleman:

    scene pr1304 with dissolve
    mc "I'll give you some privacy, at least."
    scene pr1305 with dissolve
    ver "...you're kidding, right?"

    if prVero_Facial == True:
        ver "You've ejaculated on my fucking face. Think we're past modesty, stupid?"
    else:
        ver "You've seen me nude already. We're past modesty."

    scene pr1306 with dissolve
    mc "Just get dressed, will you? I'm trying to be nice here."
    scene pr1305 with dissolve
    ver "Whatever. Just know it's not going to get you any favors with me."
    "..."
    "The faint sound of clothes being removed filled the room."
    ver "You have any idea what she's planning to do to us tonight?"
    mc "No, I don't, but I can imagine..."
    "It was the truth. All I knew was what she told me: to make sure the rotors were properly secured."
    ver "Really? You don't have a clue? I don't buy it. You wouldn't tell me if you did."
    ver "That miserable old cunt probably wants it to be a surprise. Am I right?"
    scene pr1306 with dissolve
    mc "I couldn't say one way or the other, Miss Lynch."
    scene pr1305 with dissolve
    ver "Great, I bet she stuck me with the idiot of the place..."
    "Her endless complaining was starting to become grating, but I knew getting angry would only put me further on the losing side of our exchange."
    ver "You can turn around now."
    scene pr1307 with dissolve
    stop music fadeout 1.5
    mct "(Woah...)"
    ver "Wasn't much point in not looking, was there?"
    play music "music/philly-crew.mp3"
    scene pr1308 with fade:
        subpixel True
        yalign 0.7
        xalign 0.6
        linear 4.5 yalign 0.1
    "Veronica wasn't mistaken. The attire she had slipped her statuesque, well-endowed frame into was exceedingly lewd, proving far more tantalizing than any mere naked body could hope to reach."
    "Expensive looking stockings snaked their way up her long legs, ending in a garter belt that held the silk fabric taut against her skin. Paired with a 3-inch high heel, the result was a lust-driving showcase of the musculature of her powerful legs and firm ass."
    scene pr1309 with dissolve
    "You could almost say she looked {i}classy{/i}, if not for the slits in front of her bra that filthily bared the tips of her breasts for anyone to see."
    scene pr1310 with dissolve
    ver "I just said I was finished dressing. I didn't tell you to eye-fuck me, now did I?"
    jump prFaceOffVerRotor

label prFaceOffVerPig:
    "Considering the circumstances, not like there's any point in being modest."
    scene pr1311 with dissolve
    "Veronica was quick about it, beginning to undress as if she was the only person in the room."
    scene pr1312 with dissolve
    mc "You're not embarrassed?"
    scene pr1313 with dissolve
    stop music fadeout 1.5
    ver "...you're kidding, right?"
    play music "music/frame-of-mine.mp3"
    if prVero_Facial == True:
        scene pr1314 with dissolve
        ver "You've ejaculated on my fucking face. Think we're past modesty, creep?"
    else:
        scene pr1315 with dissolve
        ver "You've seen me nude already. We're past modesty already."

    scene pr1316 with dissolve
    ver "Besides, there's two things. For one, if you've got a killer body like me, you don't shy away from showing it."
    scene pr1317 with dissolve
    mc "What's the other thing?"
    scene pr1314 with dissolve
    ver "You're basically a human cockroach. Why would I wet myself like a schoolgirl undressing in front of a bug?"
    scene pr1317 with dissolve
    mct "(...gchk!)"
    "While I raged and cursed at her internally, in my head I knew I didn't have a leg to stand on."
    mct "(It's only natural for her to look at me like that, everything considered...)"

    if toughness >= 20:
        mct "(Still, that fucking... BITCH!!!)"

    stop music fadeout 1.5
    scene pr1318 with dissolve
    "A few moments of stewing to myself was interrupted by a question."
    scene pr1319 with fade
    play music "music/horrible.mp3"
    ver "So, you have any idea what she's planning to do to us tonight?"
    scene pr1320 with dissolve
    mc "No, I don't, but I can imagine..."
    "It was the truth. All I knew was what she told me: to make sure the rotors were properly secured."
    scene pr1321 with dissolve
    ver "Really? You don't have a clue? I don't buy it. You wouldn't tell me if you did."
    ver "That miserable old cunt probably wants it to be a surprise. Am I right?"
    mc "I couldn't say one way or the other, Miss Lynch."
    scene pr1322 with dissolve
    ver "Great, she stuck me with the idiot of the place..."
    "Her endless complaining was starting to become grating, but I knew getting angry would only put me further on the losing side of our exchange."
    scene pr1310 with fade
    ver "That's done."
    scene pr1309 with dissolve
    mct "(Woah...)"
    "Though all her bitching and bleating, I failed to appreciate just what she was slipping on."
    "Expensive looking stockings snaked their way up her long legs, ending in a garter belt that held the silk fabric taut against her skin. Paired with a 3-inch high heel, the result was a lust-driving showcase of the musculature of her powerful legs and firm ass."
    "You could almost say she looked {i}classy{/i}, if not for the slits in front of her bra that filthily bared the tips of her breasts for anyone to see."
    jump prFaceOffVerRotor


label prFaceOffVerRotor:
    if _in_replay:
        show transitionveronica01 with cmet
        show screen textbox2 with dissolve
        "Please set [mcf]'s personality (toughness score) for this replay."
        hide screen textbox2 with dissolve
        menu:
            "Nice guy (Toughness: 0)":
                $ toughness = 0
            "Mischevious (Toughness: 18)":
                $ toughness = 18
            "Asshole (Toughness: 30)":
                $ toughness = 30
        show screen textbox2 with dissolve

    stop music fadeout 3.0
    scene pr1310 with dissolve
    ver "I suppose those damn rotors come next?"
    "She was referring to the egg-shaped vibrators that were the whole reason I was here."
    scene pr1350 with pixellate
    kat "I need you to keep this mouthy bitch honest, otherwise she might try to pull a fast one and skimp on the number."
    kat "Make sure you use all of these. You'll see to it {b}personally{/b}, won't you?"
    scene pr1323 with pixellate
    play music "music/jazz-piano-bar.mp3"
    mc "Lie back on the bed."
    scene pr1324 with dissolve
    "She shot me yet another unnerving look, pausing to weigh her options, before finally silently and begrudgingly accommodating my request."
    scene pr1325 with dissolve
    ver "Fine! If you have to, just be quick about it."
    scene pr1326 with dissolve
    if toughness >= 20:
        mc "Then lie back more and spread 'em, then."
    else:
        mc "Then lie back more and spread your legs please."
    ver "...tsk!"
    "She clicked her tongue in irritation, but again, did as I asked."
    scene pr1327 with dissolve
    ver "Just so we're clear, don't try any funny business, creep."
    scene pr1328 with dissolve
    mc "Considering you could probably use your thighs to crush my head like a cantaloupe, I don't think you have to worry about that."
    scene pr1327 with dissolve
    ver "As long as you understand then."
    scene pr1329 with dissolve
    "..."
    scene pr1349 with dissolve
    "As I moved in closer, my attention was glued to the muscular woman's physique and curves."
    "I had never found myself attracted to brawny women before, but then again, I'd never seen a woman quite like Veronica either. I'd be lying if I said there wasn't something about her sturdy frame that was alluring to me."
    mct "(Could it be that the thought of a woman who can kick my ass gets me going?)"
    mct "(...then again, maybe I just like red heads with large tits. That could be it.)"
    scene pr1330 with dissolve
    ver "Stop wasting time and get it over with."
    mc "*ahem* R-right, sorry..."
    scene pr1349 with dissolve
    "I was keeping it cool until now, but that went out the window as soon as I was front and center (quite literally) with my task: inserting a number of pink, egg-shaped sex toys into a stranger's vagina."
    "It's easy to put it out of mind when things are getting hot and heavy, but facing it down business like, the intimate nature of the place had me running red in the face."
    scene pr1331 with dissolve
    mc "If you'll excuse me..."
    scene pr1332 with dissolve
    "With some uneasiness, I pulled aside the maroon colored panties and got my first look at the fiery woman's rosebud and petals."
    scene pr1333 with dissolve
    ver "What are you tip-toeing around for? This isn't some sight-seeing tour."
    scene pr1334 with dissolve
    hide screen textbox2 with dissolve
    menu:
        "Be honest with her. [red]\[Veronica -1\]":
            $ Veronica_Affection -= 1
            $ Veronica_Affection = clamp(Veronica_Affection, 0, 40)
            show screen textbox2 with dissolve
            scene pr1335 with dissolve
            mc "Don't you find this to be kinda... intimate?"
            scene pr1336 with dissolve
            ver "Fuck no! I don't. I told you not to try anything funny!"
            scene pr1335 with dissolve
            mc "I'm not trying to make a move on you or anything... I'm just saying this whole situation is weird."
            scene pr1336 with dissolve
            ver "Oh {b}boo-hoo{/b}, how do you think I feel having some strange creep awkwardly breathing into my vagina? What are you, trying to turn this into a moment or something? Just put the damn toys in."
            scene pr1334 with dissolve
            mct "(Might as well get to it, I guess...)"

        "Insert the first vibrator.":
            show screen textbox2 with dissolve
            mct "(Might as well get to it, I guess.)"

    scene pr1337 with dissolve
    "Taking the small egg in the tips of my fingers, I slowly brought it to the entrance of the stony-faced woman's canal."
    scene pr1338 with dissolve
    "The pleasant heat contrasted the cold toy in my hand nicely."
    scene pr1339 with dissolve
    "The first of the small, rose-colored devices slide into Veronica's love tunnel with little trouble, spearing apart the imposing woman's unstained petals with only a slight resistance."
    scene pr1340 with dissolve
    "The second one, needing to push the first one deeper in, proved a little more difficult in finding room in the dry passage."
    scene pr1341 with dissolve
    ver "Ngg-! Not so rough-!"
    mc "Sorry, it's just you're really, {b}really{/b} tight. I'm not sure how many of these I can actually fit..."
    mc "We have two more remaining..."
    scene pr1342 with dissolve
    ver "What? There's no way in HELL four are going to fit!"
    scene pr1343 with dissolve
    mc "I'm not even sure three will, if we're being honest..."
    mct "(For some reason, I doubt that crazy witch would be okay with only using half of the toys she told me to...)"
    mct "(Wait a minute. Just MAYBE...)"
    "She didn't say all of them had to fit inside her cunt, just that I had to use them."
    scene pr1344 with dissolve
    mc "Wait here, I've got an idea!"
    stop music fadeout 3.0
    ver "Huh? Where the hell are you going?"
    play sound "sound effects/door-openclose.wav"
    scene pr1345 with dissolve
    ver "Grrh-!! You just want me to just lay here?!"
    scene pr1346 with dissolve
    ver "........."
    ver "......"
    ver "..."
    scene pr1347 with dissolve
    play sound "sound effects/door-openclose.wav"
    "..."
    scene pr1348 with dissolve
    mc "So, she didn't say WHERE or HOW these things had to be used."
    ver "I'm listening..."
    scene black with fade
    $ renpy.end_replay()
    if not persistent.VeroEggInsertGallery:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.VeroEggInsertGallery = True
    "......"
    "..."

label prFaceOffStart:
    play music "music/leaving-home.mp3"
    scene pr1351 with blinds
    "Once the prep work had been taken care of, we all gathered in the exhibition hall. The old men got comfortably seated, Kathleen and the girls took center stage, and Killian and myself were told to stand off to the side expectantly."
    "I had no idea what to expect."
    scene pr1352 with dissolve
    kat "Gentlemen! The Carnation Club welcomes you!"
    "Despite only speaking to a handful of people, like a true showman, she spared no energy addressing her audience."
    scene pr1353 with dissolve
    kat "We are gathered here tonight to select the final carnation for our annual summer exhibition."
    kat "Sammy, Mr. Miller... thank you for being here on such short notice. It is thanks to you that these women are here with us tonight."
    scene pr1354 with dissolve
    "Mrs. Pulman paused for dramatic effect, lips stretched tightly into a diabolical smile, before continuing."
    scene pr1355 with dissolve
    kat "Now, this could have simply been taken care of behind closed doors, but... I mean, where's the fun in that, right?"
    scene pr1353 with dissolve
    kat "As an extension of our gratitude for your contribution to this year's exhibition, you two have been exclusively invited to witness and participate in tonight's revelry."
    scene pr1355 with dissolve
    kat "You have helped us find {b}flowers{/b} amongst weeds."
    kat "Two women who are capable of sinking to unimagined depths, to rise like a baptism, polished and shining like the {b}whores{/b} they were meant to be."
    scene pr1356 with dissolve
    mc "*whispering* Does she hear herself? She sounds ridiculous."
    scene pr1357 with dissolve
    kil "*whispering* Oh, you haven't heard nothing yet. Just wait until the actual summer exhibition starts, when this room is just FILLED with stodgy, old bastards."
    kil "*whispering* That's when she REALLY gets into it."
    scene pr1358 with dissolve
    kat "...and what better way to discover which of them will shine the brightest other than giving them a stage?"
    kat "Now! Girls, though you may know some of these gentlemen, it is only proper you introduce yourselves and thank your sponsor for the opportunity you've been given tonight."
    scene pr1359 with fade
    "The first to step forward, despite the anxiety plainly written on her face, was Lucy."
    scene pr1360 with dissolve
    lucy "My name is Lucy Long and--"
    scene pr1361 with dissolve
    kat "Sorry, honey. Let me stop you there. That's MISSUS Lucy Long, isn't it? You're married. Be precise."
    scene pr1360 with dissolve
    lucy "My name is Mrs. Lucy Long, it is nice to meet you."
    scene pr1362 with dissolve
    kat "There's no need to be brief, dear. Now, what are you here for? Try again."
    kat "*whispering* Make it colorful."
    scene pr1363 with dissolve
    "Even from behind, I could see the gears slowly turn in her head as she tried to arrive at what Mrs. Pulman considered a {i}proper{/i} introduction."
    "After some time spent deliberating in thorny silence, she finally arrived at a conclusion."
    scene pr1364 with dissolve
    lucy "My name is Mrs. Lucy Long, I'm a shameful married woman here for your pleasure. Please treat me well."
    scene pr1365 with irisout
    lucy "Thank you for helping provide me with this chance, Mr. Miller"
    scene pr1366 with dissolve
    isak "Please, call me Isaak. We're friends, aren't we?"
    scene pr1367 with dissolve
    lucy "...mghn. T-thank you, Isaak."
    "She did her best to hide her irritation, but her antipathy for the smarmy man was as clear as day."
    isak "You're welcome, Lulu. Don't embarrass me now."
    "After that terse exchange, came the comments from the peanut gallery."
    scene pr1368 with dissolve
    chuck "Ha! She may be slow on the uptake, but she's got spirit."
    scene pr1369 with dissolve
    sam "She stands no chance against my girl, though!"
    scene pr1370 with fade
    "Without waiting to be called, Veronica stepped forward."
    scene pr1371 with dissolve
    chuck "Oh? This one's got some initiative. Let's hear it sweetheart."
    scene pr1372 with dissolve
    kat "More like impertinent..."
    scene pr1373 with dissolve
    ver "My name is Veronica Lynch, divorced."
    scene pr1374 with dissolve
    ver "Please enjoy the body that I've worked so hard, and all its fuck holes, to your heart's desire."
    "The tall, fiery headed beauty had managed to somehow come up with an even more stupid, contrived line than her opponent. Not only that, but she did it with an odd sense of personal flair."
    "It was born from the luxury of going second I guess."
    "While Lucy had forced the words through her lips with a sense of shame, Veronica had done it with the skill of an actor reading for a part."
    scene pr1375 with dissolve
    ver "From the bottom of my heart, thank you for this opportunity Mr. Garcia."
    sam "*clap* *clap* *clap* Here, here!"
    "While Charles wore his usual grin on his face, and Isaak seemed amused by Veronica's blatant lip service, only Samson seemed to actually buy it hook, line, and sinker."
    scene pr1357 with dissolve
    kil "*whispers* She basically just told Kat to fuck off."
    "Despite the insincerity, she had done what was asked, denying Kathleen the pleasure of degrading her."
    kil "*whispers* Still... that's not going to work out for her. I've seen women try to make that play before, all it does is paint a target on your back."
    scene pr1376 with dissolve
    kat "Let's get the night properly started, shall we?"
    scene pr1377 with dissolve
    play sound "sound effects/vib-start.wav"
    ver "Ghh-!"
    "With the press of a button, the devices inside her quim, as well as the two tightly kissing her hefty globes, sprang to life. The sound of a faint, almost imperceptible mechanical droning resonated through the hall."
    scene pr1378 with dissolve
    kat "Tonight, these whores will be pitted against each other in {b}three{/b} games, each game serving..."
    scene pr1379 with dissolve
    play sound "sound effects/vib-start.wav"
    lucy "OoooHngaa!"
    "The educator's abrupt, slovenly change in expression and comical howling drew a light chuckle from the crowd."
    scene pr1380 with dissolve
    kil "*whispering* I could only manage to fit three up her cooch. Wanna guess where I put the last one?"
    scene pr1381 with dissolve
    kat "Each game serving as an assessment for the three qualities that a Carnation must have in spades if she even hopes to entertain the idea of becoming our summer {i}Carnation Queen{/i}."
    scene pr1382 with dissolve
    kat "What qualities are those, you might ask?"
    "The would-be Carnations were clearly distracted by other things as Kathleen smugly posed her rhetorical question to no one in particular."
    scene pr1383 with dissolve
    kat "To be a Carnation, one must possess the {b}endurance{/b} to withstand pleasure and pain, to focus clearly on the tasks given you and to provide a marvelous show for our patrons."
    scene pr1384 with dissolve
    kat  "The {b}best{/b} whores can both revel in giving and taking pleasure simultaneously."
    scene pr1385 with dissolve
    kat "Secondly, you need to possess the right {b}disposition{/b}, to be able to submit and serve without compunction."
    scene pr1386 with dissolve
    kat "On the other hand, meek and easily broken things are no good. A little fire can make things entertaining and insubordination can always be {b}ironed{b} out, one way or another..."
    kat "Finally, the last test will examine your raw, {b}carnal skill{/b}. Bedroom knowledge can be acquired, sure, but..."
    kat "There is such a thing as talent and we only have four weeks to mold you into the perfect specimens for our grand finale, where ultimately the winner WILL be crowned. So it counts for--"
    scene pr1387 with dissolve
    chuck "Aw, c'mon Kathy! Stop yammering and lets get to the good stuff. We're all waiting and I'm sure the girls are eager to get tonight over with, bahahaha!"
    "Thankfully Dr. Chuck helped push Mrs. Pulman's growingly self-indulgent explanation along."
    kat "~ghk!"
    scene pr1388 with dissolve
    sam "Don't be like that, old man! They say good things come to those who wait!"
    scene pr1389 with dissolve
    sam "Besides, ain't nothing wrong with watching a fine piece of ass like Kathleen prance around the stage. Hahahaha!"
    kat "..."
    scene pr1390 with dissolve
    kat "No, no, Charles is right. There's no reason for me to bore you with details when you're here to relax and have some fun. This is our guests of honor's night, after all."
    scene pr1391 with dissolve
    kat "You're here to watch the slut you hand-picked out squirm uncomfortably, right Sammy?"
    sam "Here, here!"
    scene pr1392 with dissolve
    kat "What about you, Isaak? You excited to begin?"
    isak "Naturally, Mrs. Pulman. I'm dying to see what games you've come up with."
    kat "Good, good.."
    scene pr1393 with dissolve
    kat "Boys! Prepare the stage!"
    stop music fadeout 1.5
    scene black with fade

label prFaceOffEndurance:
    if _in_replay:
        scene black with fade
        show screen textbox2 with dissolve

    "......"
    "..."
    play music "music/plans-in-motion.mp3"
    scene pr1394 with dissolve
    "A few minutes into the first game --"
    scene pr1395 with dissolve
    play sound "sound effects/vib-start.wav"
    "*Bzzzzzzzzzzzzzzzz!*"
    "The dull din of the small toy motors continued to fill the exhibition hall."
    scene pr1396 with dissolve
    lucy "nnH--!"
    kat "Yes, yes..."
    scene pr1397 with dissolve
    kat "Stiff as a board! You girls are managing well."
    scene pr1398 with dissolve
    kat "A little {i}too{/i} well, maybe. Let's see how you handle an increase in power."
    scene pr1399 with dissolve
    play sound "sound effects/vib-start.wav"
    "{b}*Bzzzzzzzzzzzzzzzz!*{/b}"
    scene pr1400 with dissolve
    "With a simple touch of the tip of her finger, the mechanical whirling intensified and the girls became even more uneasy on their feet."
    "The first game was a simple one, a test of endurance requiring Lucy and Veronica to balance a tray of drinks longer than their opponent."
    "Keeping an arm raised for a prolonged of period of time would be uncomfortable by itself, but add some weight to it and the unceasing carnal tickling of the egg vibrators, it's more trying than it looks."
    scene pr1401 with dissolve
    kat "You hold that position beautifully, Mrs. Long. You used to wait tables in college I bet."
    "The dark-haired teacher shot Kathleen an almost pleading look, as if to say: {i}don't distract me, I'm trying to focus!{/i}"
    "Naturally, Mrs. Pulman prattled on."
    scene pr1402 with dissolve
    kat "Tell me, how long have you been married, Mrs. Long?"
    lucy "...h-huh?"
    "The teacher let a baffled utterance slip through her gritted teeth."
    scene pr1403 with dissolve
    kat "I asked you how long have you been married. It's the kind of simple question you ask when you're getting to know a new friend. That's what we are here, aren't we? {b}Friends?{/b}"
    "With an exasperated expression at the direction Kathleen's questions were going, Lucy took a moment to painstakingly consider how she would respond."
    scene pr1404 with dissolve
    lucy "I would prefer not to... talk about it."
    scene pr1403 with dissolve
    kat "I get it. It must be difficult to talk about your husband in front of strangers with a bunch of toys shoved up your cunt."
    scene pr1405 with dissolve
    kat "You don't HAVE to answer me. After all, it isn't a requirement for this game."
    scene pr1406 with dissolve
    play sound "sound effects/vib-start.wav"
    "To underline her point, Kathleen gave the device in her hand another tap."
    scene pr1407 with dissolve
    lucy "Ght--!"
    kat "All you're required to do is {i}comfortably{/i} hold that pose."
    scene pr1408 with dissolve
    lucy "W-we've been married for 13 years. His name is John."
    scene pr1409 with dissolve
    kat "You married young! High-school sweethearts?"
    scene pr1408 with dissolve
    lucy "Y-yes. I've known him all my life."
    scene pr1407 with dissolve
    kat "That must be wonderful, dear! Having that kind of long-lasting relationship, but wait..."
    scene pr1409 with dissolve
    kat "It couldn't be that he's the only man you've had sex with, is it?"
    lucy "No, we didn't s-start dating until college!"
    scene pr1410 with dissolve
    kat "That's disappointing, Someone here would pay good money to be the first man to give you something to compare your husband to."
    scene pr1407 with dissolve
    kat "How often do you two have sex? Four times a week?"
    scene pr1408 with dissolve
    lucy "No... less. O-once..."
    scene pr1410 with dissolve
    kat "Once a week?!"
    "Mrs. Pulman feigned a shocked tone to her question."
    lucy "Once a month. N-no, it's been t-three months..."
    kil "*whispering* Why the hell is that moron being so honest?"
    scene pr1409 with dissolve
    kat "Oh, I see..."
    scene pr1411 with dissolve
    isak "Your husband's not man enough to satisfy you, eh?"
    "Lucy's sponsor called out to her derisively, the fleshy jowls of his cheeks pulled back in a stomach-churning smile."
    scene pr1413 with dissolve
    lucy "No, n-no... w-we're just busy. We have our jobs and..."
    scene pr1412 with dissolve
    "The tormented educator looked like she wanted to disappear from sight, cheeks running red in embarrassment even more than they had been from standing stark naked in front of a crowd of strangers."
    scene pr1414 with fade
    kat "Well, here's to hoping that tonight gives you a newer appreciation for sex."
    scene pr1415 with dissolve
    "Making some fucked up toast, she took a drink of the goblet's contents."
    lucy "...h-huh? What are you--"
    scene pr1416 with dissolve
    lucy "Ght--!"
    "Abruptly, Kathleen pulled Lucy into a passionate kiss, making a show of sharing the goblet's contents with the raven-haired teacher."
    scene pr1417 with dissolve
    lucy "Ngh... staahp... *plslsh... ehch... mph, schkkk...*"
    scene pr1418 with dissolve
    "*Chup... ehch... mph, schkkk~!♥ ... chup~!♥*"
    scene pr1419 with dissolve
    lucy "Nggh-- m-my b-body is on f-fire...?"
    lucy "W-what's... w-what's t-this f-feeling?"
    scene pr1421 with dissolve
    "Smiling contentedly, her tormentor ignored the confused woman and turned her attention to Lucy's towering opponent."
    scene pr1420 with dissolve
    kat "Don't think I've forgotten about you, Miss Lynch. You look like you're managing even better than your adversary. I suppose those arms of yours are good for something, aren't they?"
    scene pr1421 with dissolve
    "Veronica paid no attention to her comment, instead keeping a steely gaze straight ahead, as if she was looking beyond the exhibition hall."
    scene pr1420 with dissolve
    kat "Actually, I suppose this might be a little unfair..."
    kat "Your conditioning gives you a clear advantage over a fatass like Mrs. Long, doesn't it?"
    scene pr1422 with slideleft
    mc "*whispering* ...fatass? She's not fat."
    "Lucy was a pleasantly curvy woman, but she wasn't even approaching what you could call fat."
    scene pr1423 with dissolve
    kil "*whispering* Of course she isn't, that's not the point."
    scene pr1424 with dissolve
    kat "I think it's only fair we give you a handicap."
    scene pr1425 with dissolve
    ver "--!"
    play sound "sound effects/vib-start.wav"
    "*Bzzzzzzzzzzzzzzzz!*"
    scene pr1426 with dissolve
    "A sharp increase in power sent the steady woman reeling."
    scene pr1427 with dissolve
    ver "A handicap? That isn't, nggh-, f-fair."
    scene pr1428 with dissolve
    kat "Fair? Don't be a naive. It's up to me to determine what is and isn't fair, Miss Lynch."
    kat "If I wanted you to stand on one leg right now, you wouldn't have a choice but to do it if you want to have a shot at competing in the summer exhibition."
    kat "Besides, it's only a 10 percent handicap,I bet you can handle double that."
    scene pr1429 with dissolve
    ver "Ghttt--!"
    play sound "sound effects/vib-start.wav"
    "*Bzzzzzzzzzzzzzzzz!*"
    scene pr1430 with dissolve
    "Another swipe of her phone brought another stupefied reaction out of the amazon."
    ver "Aaa-, f-fhuck y-you, nggh, you crazy bitch!"
    scene pr1431 with dissolve
    kat "That's obstinate language from a whore that's going to be cumming very soon."
    scene pr1432 with dissolve
    ver "L-like, nghh, I could cum in a situation, aaa-, like dhis--!"
    "The toys were beginning to make it difficult for the hard bodied woman to get out the words."
    scene pr1431 with dissolve
    kat "Oh, don't sell yourself short, sweetie. Of course you can."
    scene pr1433 with dissolve
    kat "In fact, I'll consider it a personal failing if you don't piss yourself in pleasure by the end of this, Miss Lynch."
    scene pr1434 with fade
    kat "Now, drink."
    scene pr1435 with dissolve
    scene pr1436 with dissolve
    "Veronica answered Kathleen's curt order with a leery look, clearly not trusting what's in the cup."
    scene pr1435 with dissolve
    scene pr1436 with dissolve
    "The two wordlessly locked eyes for what felt like a century, until Veronica finally capitulated the meaningless challenge by opening her mouth."
    scene pr1437 with dissolve
    kat "If you're going to do it anyway, save us all some time next time."
    scene pr1438 with dissolve
    ver "*Mph... glp... chku...*"
    scene pr1439 with dissolve
    ver "*Glp... glp... chku...*"
    "The liquid rolled its way down the large beauty's gullet."
    "Where Lucy had only imbibed a mouthful, Veronica was sucking down the entirety of the goblet's contents."
    scene pr1440 with dissolve
    ver "...schuuua!"
    "As soon as the cup's rim left her lips, Veronica let out what could only be interpreted as a contented sigh."
    "Like with the schoolteacher, the effect of whatever elixir Veronica had consumed made itself readily apparent through her skin's ruddiness and dopey, unfocused expression."
    scene pr1441 with dissolve
    ver "Ghn- w-what was in that d-drink? My body f-feels, ngh..."
    kat "It feels like you need a dick, doesn't it?"
    kat "Ha! Don't worry. You didn't drink anything... {i}harmful{/i}. It'll just make things more entertaining."
    scene pr1422 with dissolve
    mc "*whispering* Is that the same stuff she wears as perfume?"
    scene pr1442 with dissolve
    kil "Oh? You've already had a taste of it? That's surprising."
    scene pr1423 with dissolve
    kil "Truth be told, I don't know that much about it. All I know that is, speaking as dude, you DON'T want your prostate tickled while on that shit."
    scene pr1443 with dissolve
    mc "Huh... --what?!"
    scene pr1444 with dissolve
    kil "It, uh, *ahem*,  it will change how you see sex. Trust me..."
    scene pr1445 with dissolve
    mc "..."
    "My sixth sense is telling me I probably shouldn't pry any further than that."
    scene pr1446 with dissolve
    kat "Now, girls, you may have thought the challenge had already started, but you would be wrong. This is where the fun TRULY begins."
    "The cruel woman beamed a truly spine chilling smile before simply lifting up her phone and pressing a button."
    scene pr1447 with dissolve
    play sound "sound effects/vib-start.wav"
    "{b}*Bzzzzzzzzzzzzzzzz!*{/b}"
    scene pr1448 with dissolve
    lucver "{b}gYYYAAAAAAAAaaaangH!!{/b}"
    "I didn't know what setting she had turned the devices to, but the the piercing shriek it wrenched from the two women's diaphragm told me it was no trivial adjustment."
    scene pr1449 with dissolve
    ver "W-wh,ngh--, what the fhuk!! I-ght- i-intense!"
    "The steadfast woman's composure had been ratcheted out of her with a press of a button."
    scene pr1450 with dissolve
    lucy "kkhT--!!♥ W-what's dhis... e-everthing is gonnd nhumb!"
    scene pr1451 with dissolve
    kat "Marvelous! You two should see the wretched look on your faces."
    "Kathleen wasn't wrong. The impression I had of the two women, that of a business owner and a schoolteacher, were distorting into a vulgar caricature."
    "They were starting to look less like human beings and more like animals. Before I knew it, I was enraptured by the sight."
    scene pr1452 with dissolve
    kat "Enjoy watching these pitiable women cum their brains out."
    scene pr1453 with fade
    "After making her proclamation, Kathleen left the stage and took a seat next to Samson to watch the event unfold."
    scene pr1454 with dissolve
    "In the absense of Mrs. Pulman's cruel chiding, the room descended into a round of small-talk while the women on stage howled idiotically for the room's entertainment."
    scene pr1455 with dissolve
    "As the minutes passed, their shoulders naturally grew more tired, the effect of which wore plain on their face. Teeth gritted, eyes fluttering, nose twitching in the struggle to keep the tray and its payload held upright."
    scene pr1456 with dissolve
    "Of course, that being the least of their difficulties. The true challenge was remaining standing in the face of the eggs' endless vibrations, which sent the toys battering against each other and into the overworked mucous membranes of their vaginal tracts."
    chuck "You know, Isaak, we can get somebody to take care of that for you..."
    scene pr1457 with dissolve
    isak "Thank you for the offer, Dr. Kohler, but I've got things in hand."
    "The bookish man laughed at his own shitty pun before commencing to jack it."
    mct "(Fuck, that guy grosses me out.)"
    scene pr1458 with dissolve
    "Back on the stage, the girls probably didn't register they even had an audience anymore, as every ounce of focus in their trembling bodies was being funneled into not dropping their cargo."
    scene pr1459 with dissolve
    scene pr1460 with dissolve
    ver "Ggghiii--!! My n-nhipples! They fheel like they're going to v-vhibrate off!"
    scene pr1459 with dissolve
    scene pr1460 with dissolve
    "Veronica, who had it worse than her opponent thanks to her handicap and the amount of aphrodisiac she had consumed, was beginning to look downright ragged."
    scene pr1459 with dissolve
    scene pr1460 with dissolve
    "The amazonian woman was practically glistening. Sweat poured from the pores of her face as she panted maniacally and and writhed desperately for release."
    scene pr1461 with dissolve
    "Not to say her opponent had an easier time. The schoolteacher was coming equally undone."
    lucy "gnnuuAAH, uech!!!"
    "Ugly and incomprehensible guttural wails were drawn out of the raven-haired woman at a quickening pace."

    scene pr1458 with dissolve
    kil "Damn, this is getting good. Who do you think will win?"
    "Killian asked me offhand, as if we were watching a ballgame."
    "Who {i}do{/i} I think is going to win?"
    scene pr1458 with dissolve
    hide screen textbox2 with dissolve
    menu:
        "I think Lucy is going to win.":
            show screen textbox2 with dissolve
            scene pr1456 with dissolve
            mc "It's gotta be Lucy, right? Veronica is at a disadvantage."
            kil "Yeah, I agree. The tall bitch is looking like she's done."


        "I think Veronica is going to win.":
            show screen textbox2 with dissolve
            scene pr1455 with dissolve
            mc "Even if it doesn't look like it, I'm going to say Veronica. Look at her: she's strong. She could hold that pose for hours I bet."
            kil "Under normal circumstances maybe, but I'm not so sure. She's got a pretty large handicap after all..."

    scene pr1462 with dissolve
    ver "Ghh-!! Shitth~!!"
    isak "I think she's getting close. Turn it up some more!"
    "The slime-ball was referring to Veronica, who had the signs of a woman in the throes of sexual gratification etched into her face, the whites of her eyes exposed and mouth agape desperately sucking down air like a goldfish."
    ver "nggH, anh--!!!"
    scene pr1463 with dissolve
    kat "Mr. Miller isn't wrong. Looks like your girl is about to lose, Samson."
    scene pr1464 with dissolve
    sam "If I know anything about that woman, it's that bitch won't quit!"
    scene pr1463 with dissolve
    chuck "Care to make a wager on that, Sammy?"
    scene pr1465 with dissolve
    sam "Sure! 5 grand on my girl taking this thing!"
    scene pr1466 with dissolve
    kat "If you feel so strongly about it, why don't you do the honors."
    scene pr1467 with dissolve
    sam "Heh-heh-heh, don't mind if I do. Thanks, Kathy."
    scene pr1468 with dissolve
    sam "HEY! VERONICA, YOU SNOBBY BITCH! I'M GOING TO BE THE ONE TO MAKE YOU CUM, SO DON'T FORGET IT."
    scene pr1469 with dissolve
    play sound "sound effects/vib-start.wav"
    "*Bzzzzzzzzzzzzzzzz!*"
    scene pr1470 with dissolve
    scene pr1471 with dissolve
    "Samson gleefully press down and held the button, sending the toy vibrators in Veronica's snatch and on her nipples into overdrive, the previously persistent whirling transforming into a shrill whine as the tiny motors were pushed to the brink."
    ver "W-wh,ngh w-what is this?!! This is, nguh, t-too much! My insides are gooOooing nhumbs from the v-viiiIbrations!!"
    scene pr1470 with dissolve
    scene pr1471 with dissolve
    sam "Hahahaha! Oh man, this is the best! CUM YOU SOW"
    scene pr1472 with dissolve
    scene pr1473 with dissolve
    ver "nggH, anh--!!! BiiiBiiii--!♥"
    ver "Ayynh, fh-fhuck---!"
    chuck "Oh?! I think she's cumming!"
    "All sense of reason Veronica may have had seemed to have gone up in a puff of smoke as dozens of orgasms seemed to hit the sturdy woman all at once."
    scene pr1472 with dissolve
    scene pr1473 with dissolve
    ver "Ennkh,--eugh! Ghighi--!!♥"
    "Veronica was cumming so hard that her eyes had rolled into the back of her head, exposing the white of her sclera and leaving the impression that she was a dumb, insensate animal to us onlookers."
    scene pr1474 with dissolve
    scene pr1475 with dissolve
    "--or so you would think. To everyone's surprise, though her legs was shaking like gelatin and her eyes lacked focus, Veronica had managed to remain on her feet."
    sam "She's still standing! That's my girl!"
    ver "Nhaaa... Nguuuh... Nhnnn... Ngh..."
    scene pr1476 with dissolve
    scene pr1477 with dissolve
    "Coming down from her orgasm, the tray remained high in the air, when coupled with a striking smile, almost seemed to silently pose a challenge to the entire room."
    scene pr1478 with dissolve
    kat "...huh?!"
    "Even Mrs. Pulman looked dumbfounded at the amazonian's resolve."
    scene pr1479 with dissolve
    scene pr1480 with dissolve
    "However, there was little time to marvel at Veronica's endurance, because despite her being the first to cum, it was actually Lucy who was now looking worse for wear."
    "It was hard to tell what was affecting her more, the physical discomfort or the extreme sexual pleasure."
    scene pr1479 with dissolve
    scene pr1480 with dissolve
    "On one hand, her elbow was beginning to buckle under the tray's weight, starting a dicey cycle of over-correcting her posture and sending the drinks precariously teetering back and forth in her panic."
    "At same time, her legs bowed, thighs rubbing against one another as if she was desperately trying to scratch an inescapable itch."
    scene pr1481 with dissolve
    isak "I know your shoulders must be burning, but just think about why you're doing this, Lulu. Think about Davis. Think about your so--"
    scene pr1482 with dissolve
    lucy "Ggh-- {b}s-shut up{/b}! Don't you, ngh, DARE f-fucking mention his name, you {b}pig BASTARD--!{/b}"
    isak "...huh?"
    scene pr1483 with dissolve
    lucy "{b}GnhhhaaaAAaaAAAA--!!♥{/b}"
    "At the same time as she climaxed, a blanket of silence fell over the hall at Lucy's outburst. That only thing that filled the dead air was the vibrator's mechanical ministrations and the schoolteacher's distorted, impassioned howl."
    scene pr1484 with dissolve
    lucy "{b}Biiibiiii---gh!!♥{/b}"
    "Her face had twisted from a flash of anger into one of ravishment and ruin, her eyes rolling back into her head and and mouth slovenly pried open in abject pleasure."
    "The pleasure was so great that Lucy ended up losing control of her bladder, vacating it's abundant contents in an explosion of faint-smelling urine. Just as Kathleen had predicted, someone had pissed themselves with pleasure."
    scene pr1485 with dissolve
    scene pr1486 with dissolve
    "However, as quickly as it hit, it was equally soon over. Like a puppet with it's strings cut, the conquered educator dropped to the floor, the light in her eyes diminished in the shadow of climax."
    scene pr1487 with dissolve
    lucy "Ghuu... ehhhh-- s-so-- g-good."
    "She didn't have the energy to fret over whether or not her angry outburst at her sponsor might have just sunk her chances at entering the summer exhibition."
    "Isaak, in contrast, had a bewildered look on his face, having not quite settled on taking the outburst in good humor or defaulting to anger. Thankfully, Dr. Chuck forced the former on him."
    scene pr1488 with dissolve
    chuck "Bfhhahaha! This one isn't so meek either. We got quite the pair this year, don't we Isaak?"
    scene pr1489 with dissolve
    isak "Ngh... quite right, Dr. Kohler. Lulu's {i}passionate{/i} personality is one of the things I like about her..."
    "I wasn't sure if that was Dr. Chuck's honest observation or an attempt at crowd control, but whatever it was, it worked."
    scene pr1490 with dissolve
    sam "Damn, straight! I think I like your girl too, Ike."
    sam "Hey, sweetie! If you don't make it through to the exhibition, what do you say to becoming my personal woman? I'll pay you tons, bhahahaha!"
    scene pr1491 with dissolve
    isak "Tsk-- shut it, you {b}oaf!{/b}"
    scene pr1492 with dissolve
    scene pr1493 with dissolve
    play sound "sound effects/vib-start.wav"
    "*Bzzzzzzzzzzzzzzzz!*"
    "Meanwhile, despite the witless state of the contestants and the game itself being over, the mechanical sounds continued unabated."
    kat "The first game goes to Miss Lynch."
    scene pr1494 with dissolve
    stop music fadeout 3.0
    kat "Congratulations."
    "With a press of a button, the overworked eggs finally came to a rest."
    $ renpy.end_replay()
    if not persistent.FEG1Gallery:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.FEG1Gallery = True
    kat "You girls lasted over 13 minutes. Color me impressed."
    chuck "Haha, we got a talented bunch this year that's for sure!"
    scene pr1495 with dissolve
    "As the room once more began to descend into small talk, Veronica started making her way toward her inert opponent with a concerned look on her face."
    "--only to be stopped in her tracks by Isaak beating her to the punch."
    scene pr1496 with dissolve
    isak "What a fucking disgrace."
    isak "Try and do better the next time, you stupid cunt."
    scene black with fade
    "It occured to me that, despite the curtain being spectacularly drawn on the first event, Veronica and Lucy still had to endure one or two more hellish challenges before a winner could be picked."

    if toughness <=19:
        "Even if they were here through their own free will, I couldn't help but feel a pang of pity for these two women."
    else:
        "Deep down, a part of me was looking forward to the things to come."

    "What would the second game be?"
    "......"
    "..."

label prFaceOffServility:

    if _in_replay:
        show screen textbox2 with dissolve

    scene pr1497 with blinds
    "The second game of the night..."
    scene pr1498 with dissolve
    play music "music/sonatina-in-c-minor.mp3"
    ver "Ahatts dee damn hoo up?"
    "Didn't go as planned. As to what happened..."
    scene black with fade
    "Happened in a flash."
    scene pr1499 with pixellate
    play sound "sound effects/punch.wav"
    sam "--gnggah!" with hpunch
    scene pr1500 with dissolve
    sam "You fucking bitch! That's my fucking money maker!"
    "During preparation for event #2, Samson had grabbed Veronica from behind. By consequence, he was now howling obscenities and bleeding all over the maroon colored carpet."
    scene pr1501 with dissolve
    "The whole thing was an accident if you think about it, one of that smug bastard's doing, but naturally Kathleen didn't see it that way."
    scene black with fade
    "She gave Veronica two choices: be DQ'd from the competition altogether and allow Lucy to win by default or..."
    "Take an L for the second event, endure a punishment game, and go on to compete in the third event to determine the night's winner."
    scene pr1498 with dissolve
    "Forty minutes has passed since Veronica made her decision, having opted for the second alternative without a modicum of hesitation. It was such a snap decision that it left me wondering if this woman was all there in the head to begin with."
    ver "Eeehts eht dhis over 'iith!"
    scene pr1502 with dissolve
    "In the meantime, She had been made to simply kneel, bound and confined to an odd wooden contraption. Unable to speak, see, or move, for a prolonged period of time, while Dr. Chuck regaled the room with stories about the Army Corps of Engineers."
    "On the periphery of the scene, I quietly sipped from a glass of wine with a heritage that was wasted on me, and wondered if {i}this{/i} alone was meant to be the game..."
    scene pr1497 with dissolve
    "Another five minutes..."
    "Ten..."
    "Twenty..."
    "The answer to my question came after Veronica had spent almost an hour locked in that position."
    scene pr1503 with dissolve
    ver "Gnnee-!!"
    "The abrupt grip on the back of her neck startled the large woman, dragging a (surprisingly) cute and feminine yelp from her gagged lips."
    scene pr1504 with dissolve
    play music "music/myst-on-the-moor.mp3"
    kat "Jumpy aren't we, dear?"
    scene pr1503 with dissolve
    ver "--nnghmmm! -cohlde!"
    scene pr1504 with dissolve
    kat "I just wanted to let you know: It's not too late to back out. After all..."
    scene pr1505 with dissolve
    kat "An attractive woman like yourself, wrapped up neatly like this, is a flower just waiting to be plucked by any of these cruel bastards. They could do anything they wanted and you couldn't stop it."
    scene pr1506 with dissolve
    scene pr1508 with dissolve
    scene pr1506 with dissolve
    scene pr1509 with dissolve
    scene pr1506 with dissolve
    "Veronica vigorously shook her head side-to-side, emphatically wagging her head to signify she wasn't prepared to call it quits."
    "Kathleen carried on the candid, one-sided exchange in a hush tone."
    scene pr1507 with dissolve
    kat "I didn't think so, but I like to give everyone a fair warning. Just remember... If you change your mind during the game, tap your heel three times to quit. Consider that your safe word, understood?"
    scene pr1506 with dissolve
    scene pr1510 with dissolve
    scene pr1506 with dissolve
    scene pr1510 with dissolve
    scene pr1506 with dissolve
    "Veronica bobbed her head to show her comprehension."
    scene pr1507 with dissolve
    kat "Excellent. Getting to put resolute little girls like yourself under the microscope is the best thing about this place."
    scene pr1511 with fade
    kat "[mcf], I need you to fetch somethings from the kitchen..."
    scene black with dissolve
    "....."
    "..."
    mct "(...what the fuck?)"
    scene pr1512 with blinds
    "The cruel woman let out a wry smile, taking survey of the assortment of food that I had laid out around the bound woman's head."
    "Half of them was innocuous and ordinary: a bottle of juice, an onion, a lollipop..."
    "Others were items not fit for human consumption, at least in my opinion. Raw pig intestines, dog food, a head of asparagus..."
    kat "{b}Now.{/b} We're going to play a little {b}guessing{/b} game, hun."
    ver "--gh..?"
    kat "I'm going to have you {i}feel{/i} and {b}taste{/b} some things and then you'll try and guess what they are."
    kat "Guess an item correctly... {b}good{/b}! No penalty. Make an incorrect guess..."
    scene pr1513 with dissolve
    "A quick flutter of her hand ushered me onto the stage, goblets and their rancid content in tow."
    scene pr1514 with dissolve
    "A chunky, foul-smeeling liquid filled the chalices' volume, chunks of it coagulating and rising to the surface like spoiled milk."
    scene pr1515 with dissolve
    "I have a pretty good (and horrific) guess as to what I was ferrying. Every step, it took every fiber of my being not to throw up."
    scene pr1516 with dissolve
    kat "Aaah..."
    scene pr1517 with dissolve
    kat "Now, this is truly fucking DISGUSTING."
    scene pr1518 with dissolve
    kat "Get it wrong and you'll take a shot of my special blend of... male extract."
    "She casually breathed life into my damnable suspicion."
    ver "Ghmg--!!"
    "Despite being bound, the tall beauty instinctively retched back in disgust, causing the wooden apparatus to creak forcibly."
    ver "ght deee ook?!!"
    scene pr1519 with dissolve
    sam "Bahaha! What the fuck?! What did you milk to get all of that? An {b}elephant{/b}?!"
    "It was a crass question, but..."
    "Where DID all that come from...?"
    mct "(Like what the fuck?)"
    scene pr1520 with dissolve
    kat "Should be easy enough, right hotstuff?"
    "Finally freed of her muzzle, the bound and obstinate woman exercised her jaw to work out some of the stiffness before answering Kathleen's question derisively."
    scene pr1521 with dissolve
    ver "Huh? You got to be fucking kidding me. What the hell's wrong with just fucking?."
    ver "Let's just get this stupid thing over with."
    scene pr1522 with dissolve
    "Veronica wore an opaque veneer of annoyance, like the banal kind of reaction you'd see  in response to a daily aggravation."
    "She had the face of a woman who was stuck in traffic, not one blindfolded and at risk of ingesting an {b}ungodly{/b} amount of unidentified jizz. If trepidation lurked behind her expression, she masked it well."
    scene pr1523 with dissolve
    kat "That's the spirit!"
    scene pr1524 with dissolve
    "Once more, her self-satisfied tormentor lowered the squid arm in her grip onto Veronica's face, this time with a loud {b}plop!{/p}"
    ver "Ehy...!"
    "The cold, pliant flesh of the tentacle produced a yelp of surprise out of the amazon as it's unusual texture abruptly made contact with her nose."
    kat "I can only imagine how weird this must feel. It's an odd sensation isn't it, sweetpea?  {b}What{/b}~ {b}Could{/b}~ {i}It{/i}~ {b}Be{/b}...? Heheh~"
    "Mrs. Pulman delighted in taking her time teasing the bound woman."
    scene pr1525 with dissolve
    "She dragged it across her cheek."
    scene pr1526 with dissolve
    "She tickled her ear with the tip of the appendage."
    scene pr1527 with dissolve
    kat "Open up and say 'aaaaah'!"
    scene pr1528 with dissolve
    "She had her taste the clammy flesh on her tongue."
    scene pr1529 with dissolve
    scene pr1530 with dissolve
    scene pr1529 with dissolve
    scene pr1530 with dissolve
    "She even went as far as almost to vigorously shove the phallic appendage down the confused woman's throat, causing her to gag and reel back as her throat fought back against the rude invader."
    scene pr1529 with dissolve
    scene pr1530 with dissolve
    scene pr1529 with dissolve
    scene pr1530 with dissolve
    "It was a completely bizarre sight. The old woman, like a cat playing with its prey, molesting Veronica with the sushi-themed implement."
    scene pr1531 with dissolve
    "..."
    "Finally, probably looking to end the assault, she began to venture a guess."
    scene pr1532 with dissolve
    ver "It's an..."
    scene pr1531 with dissolve
    "Veronica paused with bated breath, either to consider her answer carefully or perhaps hesitating due to the nauseating penalty facing her for a wrong answer. At last, she took the plunge."
    scene pr1532 with dissolve
    ver "It's the... arm of an octopus."
    "She said it with confidence."
    scene pr1533 with dissolve
    kat "Wow, that's an extremely good guess! You're..."
    kat "{b}Wrong{/b}. Sorry!"
    ver "Tsk--!"
    kat "It's actually a squid. Pretty close, but close doesn't cut it I'm afraid."
    "Veronica suddenly looked pale. She had charged headfirst into the challenge and now she was starring down the barrel of a cup full of jizz."
    "The goblet of gelatinous, sour man goop loomed over the captive amazon, casting a paralyzing shadow."
    scene pr1534 with dissolve
    kat "You know what that means? Open up and say 'aaaaah'!"
    "The shrinking giant ignored Kathleen's lecherous command, remaining tight-lipped as she mulled the situation over behind the folds of her mask."
    scene pr1535 with dissolve
    kat "I said open your fucking gob, you whore!"
    ver "...neuch--!!!"
    scene pr1536 with dissolve
    "The moment the cup's revolting contents hit her the tip of tongue, her body violently rejected the viscous liquid with extreme prejudice."
    scene pr1537 with dissolve
    ver "cough!* --euch!!! *cough!* *cough!* --buchh!!! *cough!*"
    scene pr1538 with dissolve
    "Just picturing the gummy, foul-smelling substance as it clung to the back of her throat was enough to make me feel ill."
    scene pr1539 with dissolve
    "On top of that, I could still picture the nauseating stench from when I carried it."
    scene pr1538 with dissolve
    kil "H-o-l-y shit. That is fucking repugnant. I could be living in a gutter and I'd never do that. Not for a million dollars."
    "With an offhanded comment, my privileged friend looked down on the struggling woman."
    hide screen textbox2 with dissolve
    menu:
        "(Joke) Agree with him. [gr]\[Killian +1\]":
            $ Killian_Bromance += 1
            $ Killian_Bromance = clamp(Killian_Bromance, 0, 40)
            show screen textbox2 with dissolve
            scene pr1539 with dissolve
            mc "Yeah, no shit. Someone could have a gun to your head and I wouldn't do that to save your life."
            scene pr1538 with dissolve
            kil "I wouldn't blame you, that's for sure."

        "Admonish him for his comment. [red]\[Killian -1\]":
            $ Killian_Bromance -= 1
            $ Killian_Bromance = clamp(Killian_Bromance, 0, 40)
            show screen textbox2 with dissolve
            scene pr1539 with dissolve
            mc "That's easy for you say, isn't it? What, with your rich uncle and never wanting for anything that money can buy."
            scene pr1538 with dissolve
            kil "Nah, fuck you man. It's about standards. How could you even look at yourself in a mirror and call yourself human after you guzzle down a cup of baby batter?"
            mct "(Yeah? And what does gleefully watching it happen make you?)"

    scene pr1537 with dissolve
    ver "*gulp!* *glub!* eeeuch--!!!!"
    scene pr1540 with dissolve
    kat "That's enough. Got to save some for later!"
    "Mrs. Pulman was absolutely beaming, a sadistic grin spread wide across her face. She was in her element, absolutely relishing this, happier than a clam at high tide."
    scene pr1541 with dissolve
    "..."
    "So it continued."
    "One by one, the items dwindled."
    scene pr1542 with dissolve
    "The asparagus."
    scene pr1543 with dissolve
    "The onion."
    scene pr1544 with dissolve
    "The lollipop."
    "The more distinctive items she managed to get right, but she got just as many wrong."
    scene pr1545 with dissolve
    "The juice."
    scene pr1546 with dissolve
    "..."
    scene pr1547 with dissolve
    "The pig guts."
    scene pr1548 with dissolve
    "..."
    scene pr1549 with dissolve
    "The dog food."
    scene pr1550 with dissolve
    "By the end of it, Veronica was looking green, having gobbled down the entire cup."
    kat "All gone!"
    scene black with fade
    "..."
    "Satisfied with the game's conclusion, Kathleen freed the tall woman from her restraints."
    stop music fadeout 3.0
    scene pr1551 with dissolve
    ver "g--guhh...!"
    "Standing up must not have agreed with her stomach, as she began to immediately look like she was about to evacuate its contents."
    kat "Excellent work, Miss Lynch!"
    ver "gh--!"
    scene pr1552 with dissolve
    ver "Shit, I think I'm going to p-puke...!"
    kat "Warren!"
    sam "Haha. There she blows!"
    scene pr1553 with dissolve
    ver "---!"
    ver "Bleee-ch!"
    scene black with fade
    "..."
    scene pr1554 with dissolve
    kat "Oh my god! How absolutely disgusting! You've got curdled semen dripping down your chin. Hahaha!"
    "For the first time, I heard the normally even-keeled woman laugh. No, not laugh exactly. It was a cackle. A stomach sinking, witchly cackle."
    scene pr1555 with fade
    kat "Marvelous! Stupendous! You really stuck in there, huh? I would've pegged you as bailing after your first failed guess!"
    "Veronica didn't even seem to register the cruel woman's harping. She had basically checked out by now, physically exhausted from the stress of the challenge and staring dopily at the floor."
    kat "Bah! You're not hearing me are you? Well, whatever."
    kat "[mcf]! Clean this pigwhore up, will you?"
    mcf "U-uh, right!. Sure thing..."
    scene pr1556 with dissolve
    mcf "Come on, I'll show you to the bathroom."
    "....."
    scene black with fade
    "..."
    $ renpy.end_replay()
    if not persistent.FEG2Gallery:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.FEG2Gallery = True
label prVerCleanup:

    play music "music/study-and-relax.mp3"
    scene pr1557 with fade
    "The face that peered up at me as I wiped away the remnants of stomach acid and man gunk from its furled lips wore a complicated expression."
    "Veronica's piercing green eyes, though staring up at mine, seemed to be transfixed elsewhere. Like a day dream, she was looking straight through me."
    "Understandably, she seemed... sullen. Sad. Out of it."
    scene pr1558 with dissolve
    mc "Uh, you alright? That was some pretty nasty stuff back there..."
    scene pr1559 with dissolve
    ver "I told you I'd clean myself off, but if you're not going to let me do that, you can at least stop talking and hurry up."
    scene pr1560 with dissolve
    "She deflected my concern."
    mc "Why? Are you in such a rush to get back?"
    scene pr1558 with dissolve
    ver "..."
    scene pr1561 with dissolve
    ver "No, no... you have a point. I should use this time to collect myself."
    scene pr1562 with dissolve
    "For the life of me, I couldn't properly understand her level of mental fortitude or where her determination came from. What she had just willingly subjected herself to was so utterly repulsive, yet she soldiered on, fighting for only a {i}chance{/i} to save her business."
    "It wasn't even a guarantee, after all. This was effectively an audition to endure even more horrific games in the future. How could she do it? Part of me wanted to understand the type of crazy that could do that, that could buy wholesale into this brand of lunacy."
    mct "(Then again, isn't that what I'm doing too?)"
    mc "..."
    scene pr1563 with dissolve
    mc "There's gotta be a better way to make money, right?"
    "Without thinking about it, I let the question on my mind slip casually out."
    scene pr1564 with dissolve
    "I expected her to ignore my question, but after sizing me up for a moment, she actually answered."
    scene pr1565 with dissolve
    ver "Good. Fast. Easy."
    scene pr1566 with dissolve
    mc "...huh?"
    scene pr1565 with dissolve
    ver "Good, fast, and easy. You can only pick two and I'm past {i}good{/i} and {i}easy{/i}."
    scene pr1566 with dissolve
    mc "I'm not following..."
    scene pr1567 with dissolve
    ver "This is the {i}good{/i} and {i}fast{/i} solution to my problem."
    scene pr1568 with dissolve
    mc "Good? This is the {i}good{/i} in your book?"
    scene pr1567 with dissolve
    ver "It's {i}good{/i} because all I have to do is put up with one shitty month, and after I win, I'll be able to buy some time and get my creditors off my back without digging myself deeper in the hole. It's the most direct, effective solution."
    scene pr1569 with dissolve
    mc "...that's a... utilitarian way of looking at it."
    mct "(Is this woman a robot?)"
    scene pr1570 with dissolve
    ver "..."
    "No, she's just hiding it well. I can tell by the exhausted look on her face that the punishment game took a toll on her. I mean, how could it not?"
    "Honestly, I'm stuck between admiring her mental fortitude and thinking she's an absolute moron. At any rate, she isn't asking for my opinion, so I should just keep it to myself."
    scene pr1571 with dissolve
    mc "All done."
    scene pr1572 with dissolve
    ver "Guess it's time to finish the night..."
    scene pr1573 with dissolve
    "It was slight, but she finally let a hint of dread creep into her words. Perhaps imagining the worst for what's to come. I..."
    hide screen textbox2 with dissolve
    menu:
        "Reassuringly put my hand on her shoulder. [blue]\[Veronica +1\] [red]\[Toughness -1\]":
            $ Veronica_Affection -= 1
            $ Veronica_Affection = clamp(Veronica_Affection, 0, 40)
            $ toughness -= 1
            $ toughness = clamp(toughness, 0, 30)
            show screen textbox2 with dissolve
            "By reflex, I lent the stiff-lipped woman an empathic hand."
            scene pr1574 with dissolve
            "As soon as my palm made contact with the amazon's warm flesh, I knew I fucked up."
            "The muscles in her shoulder went instantaneously rigid with tension and her eyes zeroed in on mine with a hawk-like intensity."
            "The shit-vacating look she was giving me immediately sent my mind searching for a plausible excuse to explain what was {i}clearly{/i} an idiotic, aberrant display of affection that crossed the line of common decency."
            "{b}Surely{/b} this is the result of a neurological defect that causes my body to spasm beyond my control? A fever has burned away all impulse control in my brain? ...there was a spider?!"
            "..."
            hide screen textbox2 with dissolve
            jump prVerCleanUpPushIt

        "Leave it alone and just head back.":
            show screen textbox2 with dissolve
            stop music fadeout 2.0
            scene black with fade
            jump prFaceOffCarnality

    menu prVerCleanUpPushIt:

        "Too late now, doubledown! [gr]\[Veronica +1\]":
            $ Veronica_Affection += 2
            $ Veronica_Affection = clamp(Veronica_Affection, 0, 40)
            show screen textbox2 with dissolve
            scene pr1575 with dissolve
            mc "Don't worry, you've got this! I believe in you!"
            "Unfortunately, the first thing that popped into my head were trite, overwrought words of encouragement more fitting for a rec league baseball game than a deranged underground sex club."
            scene pr1574 with dissolve
            ver "..."
            scene pr1576 with dissolve
            stop music
            play sound "sound effects/record-scratch.wav"
            ver "Bahahaha! Oh my-- oh man-- BAHAHAHAHA!"
            ver "You're such a fucking dork! What do you think this is? A sports movie? Bahahaha!"
            scene pr1577 with dissolve
            "She continued on belly laughing for an insultingly long time, so long that I was beginning she might asphyxiate from the lack of air getting into her lungs."
            "Finally her howls died down to mere chortles and finally into snickers. It was a drawn-out, self-esteem melting process."
            scene pr1578 with dissolve
            ver "Ah... oh, man... thanks, I needed a laugh."
            mc "Uh, glad to be of help..."
            scene black with fade
            "Having inadvertently played the role of the clown, we set off back to the exhibition hall where the third game awaited Veronica."
            jump prFaceOffCarnality

        "Fuck that, make my escape. [red]\[Veronica -1\]":
            show screen textbox2 with dissolve
            "What am I going to say? Go get 'em sport? My only option is to immediately remove myself from the situation. How do I do that? Simple."
            scene pr1579 with dissolve
            "I make a tactical retreat."
            scene pr1580 with dissolve
            stop music
            play sound "sound effects/record-scratch.wav"
            ver "...huh? What are you doing?"
            mc "I think I left my car unlocked!"
            scene black with fade
            ver "Seriously?!"
            jump prFaceOffCarnality



label prFaceOffCarnality:
    "......"
    "..."
    scene pr1581 with blinds
    "Back at the exhibition hall, August and Hana had joined us."
    scene pr1582 with dissolve
    "The distinguished looking man was quick to spot me, cooly wagging his hand in salutation."
    scene pr1583 with dissolve
    "The pair of them looked fairly chummy."
    scene black with fade
    "..."
    scene pr1584 with dissolve
    play music "music/as-i-figure.mp3"
    "It didn't take long for the room to find out. Kathleen was so eager to begin the tiebreaker game, that as soon as Veronica and I took our positions on stage, she quickly began the explanation."
    "The focus of the game -- {b}carnal skill{/b}."
    scene pr1585 with dissolve
    kat "For this game, you'll each pick a partner."
    kat "Since I'm so nice, it can be ANYONE you want in this room."
    kat "No one here has a problem with that, right?"
    scene pr1586 with dissolve
    sam "*whistling* Haha, hell no!"
    chuck "Of course not, bahaha!"
    isak "None at all, Mrs. Pulman. I would be happy to help."
    scene pr1587 with dissolve
    aug "Sorry, my back isn't quite what it used to be. I'll sit this one out."
    hana "..."
    scene pr1588 with dissolve
    kil "Ha! You old farts don't have a chance of being picked with two young studs like us here."
    scene pr1589 with dissolve
    hide screen textbox2 with dissolve
    menu:
        "Say nothing [red]\[Toughness -1\]":
            $ toughness -= 1
            $ toughness = clamp(toughness, 0, 30)
            show screen textbox2 with dissolve
            scene pr1590 with dissolve
            "..."
            mct "(I probably don't really have a choice in this, do I?)"

        "Agree. [gr]\[Toughness +1\]":
            $ toughness += 1
            $ toughness = clamp(toughness, 0, 30)
            show screen textbox2 with dissolve
            "I'm part of this now, no sense in pretending otherwise."
            scene pr1591 with dissolve
            mc "What he said."

    scene pr1592 with dissolve
    kat "There you have it. You girls can pick anyone, but Auggy."
    kat "Your task is a simple one. Make your partner cum as many times as you can within a ten minute time limit."
    kat "Once the time starts, how you achieve that is up to you. You're in the driver seat."
    scene pr1593 with dissolve
    kat "All we need now is to find out who's first."
    scene pr1594 with dissolve
    "Mrs. Pulman tossed the ancient looking coin into the air with a practiced motion, it's golden surface catching the light as it traced a graceful arc through the air."
    scene pr1595 with dissolve
    scene pr1596 with dissolve
    "..."
    scene pr1597 with dissolve
    kat "Miss Lynch! Heads or tails?"
    ver "Tails."
    scene pr1598 with dissolve
    kat "Heads. Looks like Mrs. Long gets to pick who goes first. What'll it be, dear?"
    scene pr1599 with dissolve
    lucy "..."
    scene pr1601 with dissolve
    "Lucy took a moment to think about it, as if there was a delicate strategy to this asinine circus to consider."
    scene pr1600 with dissolve
    lucy "I'll go first. Best to get it over with."
    scene pr1599 with dissolve
    kat "Heh, how blasé can you get? Fine. Mrs. Long will go first."
    kat "Who do you pick as your partner?"
    scene pr1601 with dissolve
    lucy "..."
    "Again the raven-haired educator considered her options, her eyes methodically panning across the room."
    scene pr1602 with dissolve
    "Past Dr. Chuck and her duplicitous co-worker."
    scene pr1603 with dissolve
    "Past Samson."
    scene pr1604 with dissolve
    "Her neck craned all way past center stage and settled on where Ian and I stood."
    scene pr1605 with dissolve
    lucy "..."
    mct "(She's going to pick one of us?)"
    scene pr1606 with dissolve
    lucy "I'll pick him."
    "A smug grin crossed my childhood friend's face, as if this was the natural course."
    scene pr1607 with dissolve
    kat "Heh. Not a bad choice if I say so myself, but tell us what thought went into your decision?"
    scene pr1608 with dissolve
    lucy "He's... he's the most attractive man here."
    scene pr1609 with dissolve
    chuck "Oh, great! As if he needed to hear that!"
    "Dr. Chuck had a point... after hearing that, the words went straight to his head. Ian was practically giddy."
    scene pr1610 with dissolve
    kat "You like them young, huh?"
    scene pr1611 with dissolve
    kat "Ian. Step up!"
    kil "Yes, Ma'am!"
    scene black with fade
    "..."
    scene pr1612 with dissolve
    "Mrs. Pulman retrieved a set of handcuffs from off stage and brandished them for the room to see."
    scene pr1613 with dissolve
    kil "Uh, what are those for?"
    scene pr1614 with dissolve
    kat "To bind your hands. She needs to be the one leading and you're not capable of taking a passive role, are you?"
    scene pr1615 with dissolve
    kil "You make it sound like I don't have any self-control."
    scene pr1616 with dissolve
    kat "...and DO you?"
    scene pr1617 with dissolve
    chuck "Don't blame the lad, my sister and her husband spoiled him rotten growing up."
    scene pr1618 with dissolve
    kil "...okay, yeah I get it."
    scene black with fade
    stop music fadeout 3.0
    "After getting Ian to undress, Mrs. Pulman fastened his wrists behind his back and then quickly strolled off the stage."
    "..."

label prFaceOffCarnalityLucy:
    if _in_replay:
        show transitionhousegirls with cmet
        show screen textbox2 with dissolve
        "Please set [mcf]'s personality (toughness score) for this replay."
        hide screen textbox2 with dissolve
        menu:
            "Nice guy (Toughness: 0)":
                $ toughness = 0
            "Mischevious (Toughness: 18)":
                $ toughness = 18
            "Asshole (Toughness: 30)":
                $ toughness = 30
        show screen textbox2 with dissolve

    scene pr1619 with dissolve
    kat "Ready..."
    kat "Set...!"
    scene pr1620 with dissolve
    play sound "sound effects/short-beep.wav"
    kat "{b}GO{/b}!"
    scene pr1621 with dissolve
    kil "So, cutie, how do you wanna pla--"
    scene pr1622 with dissolve
    play music "music/plans-in-motion.mp3"
    "Not wasting any time, the schoolteacher quickly sprung into action, hastily slipping behind Ian and knocking into him with full abandon."
    scene pr1623 with dissolve
    "Ian, caught off guard in surprise, tumbled into the invitingly warm embrace of the silky-red bedspread."
    kil "gh--!"
    scene pr1624 with dissolve
    kil "*THUD* Ata-! Y-you could've just told me to climb onto the bed, y'know!"
    scene black with fade
    "Ignoring my toppled friends grievance, Lucy wordlessly positioned herself above his naked hips."
    scene pr1625 with dissolve
    "Her eyes displayed the character of woman on a mission, unflappable and fiercely determined not to let anything stand in her way of winning."
    scene pr1626 with dissolve
    kil "C-cold! Haven't you ever heard you catch more flies with honey? Slow down and let me get into it!"
    scene pr1627 with dissolve
    lucy "Sorry, but there's no time for that. You can cum like this, right? It's a simple physiological response."
    scene pr1628 with dissolve
    lucy "It's not rocket science, all I need to do is stimulate your member and then your body will send a signal to your nervous system that it's time to pop."
    scene pr1629 with dissolve
    lucy "Besides, who are you kidding? Look how hard you already are in my hand."
    "Considering how tight-lipped she'd been, I was surprised at how comfortably Lucy took the lead for the final game."
    scene pr1630 with dissolve
    mc "I guess she likes being on top..."
    "I absent-mindedly voiced my curiosity aloud."
    scene pr1631 with dissolve
    aug "Maybe she's just the type that can throw herself into her work? That's my read at least."
    scene pr1632 with dissolve
    "The old man across the aisle acknowledged my offhanded comment by sharing an observation of his own, doling out wisdom built from his years of... what exactly?"
    scene pr1633 with dissolve
    if toughness >= 20:
        mc "Say old man, how long have you been doing this?"
    else:
        mc "If you don't mind me asking, how long have you been doing this?"
    scene pr1634 with dissolve
    aug "Doing what, [mcl]?"
    scene pr1633 with dissolve
    mc "Uh..."
    scene pr1632 with dissolve
    mct "(How should I put it...? {i}How long have you been a pimp{/i}?)"
    "I tried to find the most precise words to clarify."
    scene pr1633 with dissolve
    mc "Uh, {b}this{/b}."
    scene pr1632 with dissolve
    "I didn't do too well."
    scene pr1631 with dissolve
    aug "This...? Ah, you mean the skin trade?"
    scene pr1635 with dissolve
    aug "Well, let's see... I'm 63 now, so that means.... I made pornography for a little over two and a half decades before I started managing this place a little less than... five years ago? Has it really been that long?"
    scene pr1636 with dissolve
    "While August took survey of his life, his companion next to him used the opening to chime in with an observation of her own."
    scene pr1637 with dissolve
    hana "You're not disappointed she picked that monkey-brained idiot over you, are you new guy?"
    scene pr1638 with dissolve
    hide screen textbox2 with dissolve
    menu:
        "Absolutely not. [gr]\[Hana +1\]":
            $ Hana_Affection += 1
            $ Hana_Affection = clamp(Hana_Affection, 0, 40)
            show screen textbox2 with dissolve
            scene pr1639 with dissolve
            mc "Disappointed that I avoided stripping down and getting handcuffed in front of a room full of men?"
            mc "Yeah, I think my {i}feelings{/i} and I will manage."
            scene pr1641 with dissolve
            hana "Pssh! C'mon, where's your pride as a man? If I was swinging a dick, I wouldn't want to lose to that... {i}dick{/i}."
            scene pr1639 with dissolve
            mc "I wasn't aware I was competing...."

        "Maybe a little... [red]\[Hana -1\]":
            $ Hana_Affection -= 1
            $ Hana_Affection = clamp(Hana_Affection, 0, 40)
            show screen textbox2 with dissolve
            scene pr1640 with dissolve
            mc "A little, yeah. I wouldn't say no to some fun."
            scene pr1643 with dissolve
            hana "I guess you'll fit in just fine here."

    scene pr1644 with dissolve
    aug "Don't pay her any mind, [mcl]. Hana just likes to get under people's skin. She's like a child."
    scene pr1645 with dissolve
    "Back on the stage, a little over a minute and a half had passed since Lucy's boisterous kickoff."
    scene pr1646 with dissolve
    scene pr1647 with dissolve
    scene pr1646 with dissolve
    scene pr1647 with dissolve
    "In that time, in the face of Ian's grumbling, she had maintained a steady, speedy, unyielding pace, driving her palm up and down the length of Ian's swollen member in a fastidious fashion."
    scene pr1646 with dissolve
    scene pr1647 with dissolve
    scene pr1646 with dissolve
    scene pr1647 with dissolve
    kil "Gg-ah. Stop milking me like an animal and do something sexy, you bitch!"
    scene pr1648 with dissolve
    scene pr1649 with dissolve
    scene pr1648 with dissolve
    scene pr1649 with dissolve
    lucy "Your cock doesn't seem to mind. It's twitching in my hand."
    scene pr1651 with dissolve
    "Without slowing down, Lucy brought her free hand to Ian's scrotum."
    scene pr1650 with dissolve
    scene pr1651 with dissolve
    scene pr1650 with dissolve
    scene pr1651 with dissolve
    "*FAP* *FAP* *FAP*"
    lucy "Come on... come on... just give it up, will you?"
    scene pr1650 with dissolve
    scene pr1651 with dissolve
    "*FAP* *FAP* *FAP*"
    "The ticking clock was clearly at the forefront of her mind. She had to make Ian cum fast, as many times as possible, before it reached zero."
    "She cupped the playboy's ball-sack in her hand, deftly rolling them around in the palm, cradling and teasing them."
    scene pr1650 with dissolve
    scene pr1651 with dissolve
    "*FHAP* *FHAP* *FHAP*"
    "It was like Dr. Jekyll and Mr. Hyde: one hand tenderly delivering delicate ministrations from below while the other furiously rubbed the red headed man's meatpole raw."
    scene pr1650 with dissolve
    scene pr1651 with dissolve
    "*FHAP* *FHAP* *FHAP*"
    "However, the stark incongruity actually seemed to be working. From the audience, I could see Ian's toes began to curl and his body send body shiver after body shiver in response to the stimulus."
    scene pr1654 with dissolve
    kat "Looks like you enjoy being tied up, Ian. I never would've guessed it. You make a good looking bottom."
    "Mrs. Pulman called out from the side, seizing the opportunity to give my normally slick-as-oil friend a not-so-friendly ribbing."
    scene pr1655 with dissolve
    kil "nng-, I can't help it! Her hand is a fucking vice!"
    scene pr1652 with dissolve
    "By now, the callous resistance-laden, skin-on-skin rubbing had turn into a smooth, frictionless slide as Ian's dickhole spouted pre-cum and became lathered in its own juices."
    scene pr1653 with dissolve
    "The playboy's cockflesh was practically glistening under the exhibition hall's lighting, producing a sickly squelching noise in tandem with Lucy's relentless undulation."
    scene pr1652 with dissolve
    scene pr1653 with dissolve
    scene pr1652 with dissolve
    scene pr1653 with dissolve
    "*SCHLICK* *SCHLICK* *SCHLICK*"
    sam "Bahaha! He's wetting himself like a girl!"
    "My poor friend wasn't immune from teasing from this side of the room either it seemed."
    scene pr1652 with dissolve
    scene pr1653 with dissolve
    scene pr1652 with dissolve
    scene pr1653 with dissolve
    "*SCHLICK* *SCHLICK* *SCHLICK*"
    scene pr1656 with dissolve
    kil "g-gah! Shit! Y-you're way too good at this! Even b-better than some of the girls here--"
    scene pr1657 with dissolve
    play sound "sound effects/spurt.wav"
    with flash
    play sound "sound effects/spurt.wav"
    with flash
    "Before he could finish choking the words out, Ian reached his climax, letting out a guttural moan as thick ropes of semen erupted from his tip like a spurting geyser."
    scene pr1658 with dissolve
    play sound "sound effects/spurt.wav"
    with flash
    play sound "sound effects/spurt.wav"
    with flash
    kil "Fufuck--ngaaah!"
    "Heaps, {i}Reams of cum{/i}. Strand after strand of gooey man gunk arched through the air, splattering Lucy's hand and chest and staining the bed a viscous white."
    "It was actually kinda extraordinary."
    scene pr1659 with dissolve
    "..."
    kat "Impressive..."
    "It seemed Kathleen thought so as well."
    scene pr1660 with dissolve
    "Still on the clock, Lucy didn't give Ian any time to catch his breath or bask in post-orgasmic bliss. Without missing a beat, she raised her body, letting her broad hips precariously dangle over the playboy's slimy, still oozing member."
    lucy "Sorry, no time to stop..."
    scene pr1661 with dissolve
    lucy "Gnn--!"
    "In a single, fluid motion she brought herself straight down on Ian's rod, stuffing herself with cockmeat with no concern for either of their comfort."
    scene pr1662 with dissolve
    kil "You're using more than just your hand? You should've started with this!"
    scene pr1663 with dissolve
    lucy "Well, you'll need something more enticing to cum a second time so soon, right?"
    scene pr1664 with dissolve
    scene pr1665 with dissolve
    "In lieu of a waiting for a proper response from the playboy, Lucy began to rhythmically sway her hips, building into a gentle, pleasant pace."
    lucy "S-sorry for treating you so rough earlier. We don't have much time..."
    scene pr1664 with dissolve
    scene pr1665 with dissolve
    kil "n-ngh, no... I understand."
    lucy "Good... just lay back and enjoy this, okay?"
    scene pr1664 with dissolve
    scene pr1665 with dissolve
    "Lucy adopted a saccharine approach, softly cooing words of empathy, signaling to her partner that the second time around would be more enjoyable."
    kil "Like I have a choice BUT to lay here!"
    scene pr1666 with dissolve
    "Following my childhood friend's glib observation, Lucy slide herself back up the length of Ian's cock, tantalizing unsheathing herself inch by inch at a deliberate pace."
    "The teasing ascent produced the effect the schoolteacher was looking for. To the playboy's oversensitive dick, post-cumming, found the cool open air itself stimulating."
    scene pr1667 with dissolve
    "The achingly slow climb was followed by a quick, but measured descent."
    kil "--! Nnnh!"
    scene pr1666 with dissolve
    scene pr1667 with dissolve
    "Once more, she ungloved herself from Ian's cock, only to quickly swallow it whole again not a moment later."
    scene pr1666 with dissolve
    scene pr1667 with dissolve
    "It was like this, Lucy began to build a rhythm, the school teacher bouncing up and down, riding the playboy's meatstick while Ian could only lay there like a slab of meat."
    scene pr1666 with dissolve
    scene pr1667 with dissolve
    kat "Ha! You ride your husband like that or just the men you pick up in bars?"
    scene pr1666 with dissolve
    scene pr1667 with dissolve
    lucy "I've never c-cheated on my -nggh- husband."
    scene pr1666 with dissolve
    scene pr1667 with dissolve
    "She said flatly to Mrs. Pulman's cruel chiding, trying her best to keep focus."
    scene pr1666 with dissolve
    scene pr1667 with dissolve
    kat "Is that so? Could've fooled me. You look like a natural."
    lucy "H-nggh-how much, how much time do I have left?"
    scene pr1668 with dissolve
    kat "You have a little less than five minutes remaining, dear."
    scene pr1669 with dissolve
    kat "I wonder if you'll make it..."
    scene pr1670 with dissolve
    kat "Though he's young, Killian has a lot of experience. The fact that you made him cum once in the first five minutes is incredible, but I'd be very surprised if you manage another one with the time remaining."
    scene pr1671 with dissolve
    scene pr1672 with dissolve
    kil "Ghh-- d-don't let her get to you, Luce. Just focus on me, okay? If you keep this up, I'll have another load for you in no time."
    scene pr1671 with dissolve
    scene pr1672 with dissolve
    kil "You can win this thing!"
    "In his own twisted way, Ian offered his partner reassurance."
    scene pr1673 with dissolve
    scene pr1674 with dissolve
    lucy "R-right!"
    "Spurred by the playboy's encouragement, Lucy doubled her efforts."
    scene pr1675 with dissolve
    scene pr1676 with dissolve
    "She picked herself up and repeatedly speared herself back down on her partner's engorged sex, each cycle marked by the thunderous clap of flesh-on-flesh."
    scene pr1675 with dissolve
    scene pr1676 with dissolve
    "Up and down."
    scene pr1675 with dissolve
    scene pr1676 with dissolve
    "Up and down."
    "Every time she'd go back up, Ian's cock would come perilously close to slipping out, only to be tightly engulfed once more in a flash."
    scene pr1675 with dissolve
    scene pr1676 with dissolve
    scene pr1675 with dissolve
    scene pr1676 with dissolve
    lucy "Aaa-ah!"
    "This carried on for a minute, until the schoolteacher's breath became visibly ragged and sweet sounds began to escape her lips."
    scene pr1666 with dissolve
    scene pr1667 with dissolve
    kil "nng--you're getting into, eh? Glad I'm not the only one having fun."
    scene pr1666 with dissolve
    scene pr1667 with dissolve
    lucy "Gha-- H-gn-how could I not? *huff* *huff* I still have that drug from e-en-arlier in my system..."
    scene pr1671 with dissolve
    scene pr1672 with dissolve
    kil "Don't try to weasel out of responsibility for what you're feeling."
    scene pr1673 with dissolve
    scene pr1674 with dissolve
    lucy "*huff* *huff* ngg-an--I'm nooot, it's t-the truhth!"
    scene pr1671 with dissolve
    scene pr1672 with dissolve
    kil "It's been over an hour since the first game, meaning it's out of your system by now. This is all you. You're enjoying this."
    scene pr1673 with dissolve
    scene pr1674 with dissolve
    lucy "What? N-no, I'm d-doin' this to get my son into St. Ives...!"
    scene pr1671 with dissolve
    scene pr1672 with dissolve
    kil "Maybe, but you're also enjoying this! There's nothing wrong with that, just be true to who you are."
    "Killian began an offensive of his own, wearing down at the educator's mind with his words, trying to get her to openly admit her role in this filth."
    lucy "W-who I am?"
    "As if on cue, like this was a normal routine for the pair, Mrs. Pulman interjected."
    scene pr1666 with dissolve
    scene pr1667 with dissolve
    kat "You're a whore for money, creaming herself on the dick of someone other than your husband. What else would you call this?"
    scene pr1666 with dissolve
    scene pr1667 with dissolve
    lucy "Wh-ngh-why am I feeling this w-ng-way?"
    scene pr1666 with dissolve
    scene pr1667 with dissolve
    kat "How could I know? You like having sex while being watched? Maybe you like being in control of a handsome young man? You're the fucked up one here, not me."
    scene pr1666 with dissolve
    scene pr1667 with dissolve
    kat "Only you can answer that, but I do know one thing. You're getting off on SOMETHING about this."
    lucy "-gnngh! Anggha~♥ No..."
    scene pr1677 with dissolve
    kat "You have just over three minutes to make him cum once more, dear."
    lucy "--!"
    "Seeing the clock was enough for the educator to push the self-doubt out of her head and to refocus on the task at hand."
    scene pr1675 with dissolve
    scene pr1676 with dissolve
    lucy "nngh--we're running out of time."
    scene pr1675 with dissolve
    scene pr1676 with dissolve
    lucy "P-please, hurry up and cum!"
    scene pr1675 with dissolve
    scene pr1676 with dissolve
    kil "Forget about the clock! I told you to just focus on me, remember?"
    scene pr1675 with dissolve
    scene pr1676 with dissolve
    "..."
    scene pr1675 with dissolve
    scene pr1676 with dissolve
    sam "You're sure are enjoying the show, aren't you Isaak?"
    scene pr1678 with dissolve
    isak "That's right! This is the best! Watching that arrogant woman get dragged into the mud!"
    scene pr1666 with dissolve
    scene pr1667 with dissolve
    "..."
    scene pr1666 with dissolve
    scene pr1667 with dissolve
    "..."
    scene pr1666 with dissolve
    scene pr1667 with dissolve
    "..."
    scene pr1666 with dissolve
    scene pr1667 with dissolve
    kil "--! ggh, you did it! I'm going to explode!"
    scene pr1666 with dissolve
    scene pr1667 with dissolve
    "Hearing my friend's declaration, Lucy frantically slipped the playboy's tumescent, pulsing member out of her slit, letting it point freely into the air and then--"
    scene pr1679 with dissolve
    "Once more, Ian ejaculated, splattering the pale skin of Lucy's back with his baby batter."
    "Though not quite as much as his first go around, it was still a gobsmackingly stupid amount."
    mct "(Like seriously, what the hell? Is it something he eats?)"
    scene pr1680 with dissolve
    kil "*huff* *huff* Holy shit. Cumming back-to-back like that takes it out of you."
    lucy "*huff* *huff* Do you think you can go again? W-what's the time?"
    scene pr1681 with dissolve
    stop music fadeout 2.0
    kat "Afraid time's up, but you managed to make your partner cum twice."
    scene pr1682 with dissolve
    kat "It's a pretty good number for such a short time. You should be proud."
    mct "(Yeah, {i}proud{/i}. I'm not sure that's the word for it.)"
    scene pr1683 with dissolve
    kil "You did good picking me. I'm not even sure if these old geezers can even get it up."
    kil "You got this in the bag, Luce."
    "......"
    scene black with fade
    "..."
    $ renpy.end_replay()
    if not persistent.FEG3LucyGallery:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.FEG3LucyGallery = True

label prFaceOffCarnalityVer:

    if _in_replay:
        show screen textbox2 with dissolve

    scene pr1684 with dissolve
    play music "music/covert-affair.mp3"
    "After Lucy and Ian shuffled off the stage, it was now Veronica's turn to choose her partner."
    "The glint of apprehension I caught earlier in the night was no where to be found, not in the outlines of her face or through the language of her towering body."
    kat "Who shall it be, Miss Lynch? Take your pick."
    scene pr1685 with dissolve
    ver "Hmm..."
    scene pr1686 with dissolve
    ver "..."
    scene pr1687 with dissolve
    ver "You said I may pick ANYONE, right?"
    scene pr1688 with dissolve
    kat "That's right. Pick whoever you want. Pick whoever you feel you're most compatible with."
    scene pr1689 with dissolve
    ver "Excellent. Then I've made my decision."
    stop music fadeout 2.0
    scene pr1690 with dissolve
    kat "Well, spit it out."
    scene pr1691 with dissolve
    play music "music/Still_Standing.mp3"
    ver "I pick..."
    scene pr1692 with dissolve
    ver "I pick you."
    scene pr1693 with dissolve
    "......"
    "..."
    "A moment of stillness fell the room, Kathleen's face wearing a look of baffled amusement, until Dr. Chuck's hearty laugh cut through the silence."
    scene pr1694 with dissolve
    chuck "Ffhahaha! You set yourself up for that, Kat!"
    "The rest of the room followed suit, Samson matching Dr. Chuck's riotous laugh with his own and even Isaak gave a hearty chuckle at the development."
    scene pr1695 with dissolve
    aug "Well, this sure is a first."
    "August was smiling ear-to-ear and even Hana, who'd I noticed had been doing her best to look disinterested, had a captivated gleam in her eyes."
    scene pr1696 with dissolve
    kat "You can't be serious. Obviously, I'm not included in the options."
    scene pr1697 with dissolve
    ver "You told me I could pick anyone. Those are you words. Am I wrong?"
    ver "Then I pick you, Mrs. Pulman."
    scene pr1696 with dissolve
    kat "Tsk! You should know I didn't mean me."
    scene pr1698 with fade
    chuck "C'mon, Kat! Fair is fair. You did say she could pick ANYONE..."
    scene pr1699 with dissolve
    chuck "Didn't you say a couple of years ago that this club is {b}nothing{/b} if we're not true to our word?"
    scene pr1700 with dissolve
    kat "You know damn well that was in a different context, but..."
    scene pr1701 with dissolve
    kat "Ah, what the hell! If Miss Lynch wants to stake her participation in the summer exhibition on this gambit, then far be it from me to deny her."
    scene pr1702 with dissolve
    lucy "What? This isn't fair! It's not the same as with a man! How are we supposed to count how many times you orgasm?"
    scene pr1703 with dissolve
    ver "Oh, {b}you'll know{/b}."
    "Veronica interjected, confidently."
    scene pr1701 with dissolve
    kat "Neither of you have to worry. I'm an honest woman."
    kat "If Miss Lynch somehow manages to make me cum, I won't try to hide it."
    scene pr1704 with dissolve
    lucy "..."
    scene pr1705 with dissolve
    ver "..."
    stop music fadeout 2.0
    scene pr1706 with fade
    kat "I let you'll know in advance: I've got no interest in women physically. I probably won't feel a thing."
    kat "This is foolish."
    scene pr1707 with dissolve
    ver "Oh, we'll see about that."
    play music "music/FeelinIt.mp3"
    scene pr1708 with blinds
    kat "Start the timer, [mcf]. Let's get this over with."
    scene pr1709 with dissolve
    mc "Right..."
    scene pr1710 with dissolve
    "Doing as she asked, I pressed the button that would start counting down the final game of the night."
    play sound "sound effects/short-beep.wav"
    mc "You can begin."
    scene pr1711 with dissolve
    ver "Hmm..."
    "As she inched closer, Veronica wore a lecherous look on her face -- one not so unlike the crass leering she'd been subjected to tonight."
    scene pr1712 with dissolve
    ver "You're quite the looker. A regular silver vixen."
    scene pr1713 with dissolve
    ver "...but you know that, don't you? You bank on it. The grace that comes with old age, mixed with the allure that wealth and natural beauty affords..."
    scene pr1714 with dissolve
    kat "The clock's ticking, Miss Lynch. You're wasting time."
    scene pr1715 with dissolve
    scene pr1716 with dissolve
    ver "What? You eager to begin? Hah! You know, you're one to talk about others having cow tits."
    scene pr1715 with dissolve
    scene pr1716 with dissolve
    ver "These things are obscene!"
    scene pr1717 with dissolve
    scene pr1718 with dissolve
    kat "Thank you. I am rather proud of them."
    scene pr1715 with dissolve
    scene pr1716 with dissolve
    "Mrs. Pulman answered the amazon's teasing accusation audaciously."
    scene pr1717 with dissolve
    scene pr1718 with dissolve
    kat "You're not planning on talking me to orgasm, are you?"
    scene pr1719 with dissolve
    "*Fwmuch*"
    scene pr1720 with dissolve
    "Veronica kissed Mrs. Pulman's neck."
    scene pr1721 with dissolve
    "Dotting it's speckless surface with small peck after peck."
    "*Fwmuch*"
    scene pr1722 with dissolve
    scene pr1723 with dissolve
    ver "Lookie here. You've got goosebumps."
    scene pr1722 with dissolve
    scene pr1723 with dissolve
    ver "You got a soft spot for your neck, huh?"
    scene pr1724 with dissolve
    kat "Gh..!"
    scene pr1725 with dissolve
    scene pr1726 with dissolve
    kat "So what? It's an erogenous zone. That should be obvious."
    scene pr1722 with dissolve
    scene pr1723 with dissolve
    ver "Maybe, but it proves to me you're not the frigid bitch you're pretending to be."
    scene pr1727 with dissolve
    "*Fwmuch*"
    scene pr1728 with dissolve
    scene pr1729 with dissolve
    "*Fwmuch* *Fwmuch*"
    scene pr1728 with dissolve
    scene pr1729 with dissolve
    scene pr1728 with dissolve
    scene pr1729 with dissolve
    "*Fwmuch* *Fwmuch* *Fwmuch*"
    kat "...!"
    scene pr1730 with dissolve
    ver "Yeah! This is going to work."
    scene pr1731 with dissolve
    "Satisfied she had found an avenue for attack, Veronica got to work--"
    "Covering the austere woman's neck in soft, short kisses."
    scene pr1732 with dissolve
    "Assaulting her with playful bites."
    "Dragging her soft tongue across the length of her collar."
    scene pr1733 with dissolve
    "Little by little, Mrs. Pulman's alabaster skin became flushed, breath quickening in sexual arousal."
    "It was proof not to just her attacker, but to the room as well, that the tall beauty actually had a fighting chance at winning the final game."
    scene pr1734 with dissolve
    ver "Hey kid, how much time do I have to put this bitch in her place?"
    mct "(Kid...?)"
    scene pr1735 with dissolve
    mc "About nine minutes."
    scene pr1736 with dissolve
    ver "Good! Just so you know..."
    ver "I'm not going to stop at three orgasms."
    scene pr1737 with dissolve
    kat "Tsk! Go ahead and--"
    scene pr1738 with dissolve
    kat "--huh?"
    "Without warning, Veronica handily lifted Kathleen off the ground, as if she weighed nothing."
    scene pr1739 with dissolve
    kat "What do you think you're doing?"
    scene pr1740 with dissolve
    ver "Not used to be handled by a real woman, are you?"
    scene pr1741 with dissolve
    ver "Christ! You're practically oozing down here! All your talk about us being whores and what do you call this?"
    scene pr1742 with dissolve
    ver "You're a proper slut. Takes one to know one, I guess."
    scene pr1743 with dissolve
    kat "Heh, this has gotten interesting."
    kat "Do your best, Miss Lynch. Don't stop even if I tell you to."
    scene pr1744 with dissolve
    "The amazon's rough treatment had brought out Kathleen's lascivious side. She was having... fun?"
    "It was starting to look like the club was more than just an outlet to flex her sadistic, rich-lady predilections."
    "She had an interest in the carnal side of things as well."
    scene pr1745 with dissolve
    kat "...gah!"
    scene pr1746 with dissolve
    scene pr1747 with dissolve
    scene pr1746 with dissolve
    scene pr1747 with dissolve
    "Following Kathleen's cue, Veronica set to work, dipping her digits into the cruel woman's lubricated gash."
    scene pr1746 with dissolve
    scene pr1747 with dissolve
    ver "Huh? You do kegel or something? For an old hag, you're tighter than a nun's asshole down here."
    scene pr1746 with dissolve
    scene pr1747 with dissolve
    ver "You rich ladies really are something special."
    scene pr1746 with dissolve
    scene pr1747 with dissolve
    kat "gwnn--"
    scene pr1746 with dissolve
    scene pr1747 with dissolve
    "Hugging Kathleen tightly, Veronica picked up the pace, deftly maneuvering her wrist to perform a clearly well-practiced motion."
    scene pr1746 with dissolve
    scene pr1747 with dissolve
    "She attacked her target quickly, but it wasn't mindless. There was an uneven rhythm to the shallow jabs of her fingertips and alternating deep, knuckle-sinking thrusts."
    "It was a rough assault, but not careless or violent. The amazon was taking great effort not to drag her pointed nails across the soft membrane of Mrs. Pulman's insides."
    scene pr1748 with dissolve
    scene pr1749 with dissolve
    "Beads of sweat began to trickle down Kathleen's flawless, white skin."
    scene pr1748 with dissolve
    scene pr1749 with dissolve
    "Her chest began to rise and fall at an erratic pace."
    scene pr1748 with dissolve
    scene pr1749 with dissolve
    "For all her bluster earlier, she was finding her rough treatment at Veronica's hand gratifying."
    scene pr1748 with dissolve
    scene pr1749 with dissolve
    kat "nnhwa~! Nnhaha-! Hwah--!"
    scene pr1750 with dissolve
    scene pr1751 with dissolve
    ver "H-ol-oly shit. You dirty bitch. You're already feeling it."
    scene pr1750 with dissolve
    scene pr1751 with dissolve
    ver "Your lower mouth is greedily sucking on my fingers."
    scene pr1748 with dissolve
    scene pr1749 with dissolve
    kat "Y-you..."
    "For once, Kathleen had no verbal riposte to Veronica's teasing."
    scene pr1748 with dissolve
    scene pr1749 with dissolve
    kat "Nhha~! Ngg-ha~ha..."
    "Instead, all she put forth was a series of muffled, pleasured sighs and breathy grunts."
    scene pr1748 with dissolve
    scene pr1749 with dissolve
    kat "Nhaha-haha!"
    scene pr1752 with dissolve
    scene pr1753 with dissolve
    "Seeing her on the ropes, the amazon once again began to kiss and nibble at Kathleen's neck."
    "*Fwmuch*"
    scene pr1752 with dissolve
    scene pr1753 with dissolve
    kat "Ah-! R-ight Th-there! If you do it right there..."
    scene pr1752 with dissolve
    scene pr1753 with dissolve
    "*Fwmuch* *Fwmuch*"
    scene pr1752 with dissolve
    scene pr1753 with dissolve
    "*Fwmuch* *Fwmuch* *Fwmuch*"
    scene pr1754 with dissolve
    scene pr1755 with dissolve
    "Veronica's body was like a well-oiled machine, working in tandem in a three-pronged assault at the austere woman's erogenous zone."
    scene pr1754 with dissolve
    scene pr1755 with dissolve
    "Her mouth tickled and teased her neck."
    "*Fwmuch*"
    scene pr1754 with dissolve
    scene pr1755 with dissolve
    "One hand supported her body weight while she massaged and kneaded her plump breasts."
    kat "Nhhagh~ggh!"
    scene pr1756 with dissolve
    scene pr1757 with dissolve
    "The other never slowed down on the relentless finger fucking it was dishing out."
    scene pr1756 with dissolve
    scene pr1757 with dissolve
    "*Schlick* *Schlick* *Schlick*"
    scene pr1756 with dissolve
    scene pr1757 with dissolve
    "All three aspects was coming together beautifully, pushing Mrs. Pulman closer and closer to the edge, to the precipice of her first orgasm."
    scene pr1756 with dissolve
    scene pr1757 with dissolve
    "........."
    scene pr1756 with dissolve
    scene pr1757 with dissolve
    "...."
    scene pr1756 with dissolve
    scene pr1757 with dissolve
    "..."
    scene pr1758 with dissolve
    kat "--!"
    "Through gritted teeth and glassy eyes, Mrs. Pulman's body suddenly tensed up..."
    kat "nggg-aaah!"
    scene pr1759 with dissolve
    "Only to go slack again not too long after."
    "It happened quickly, but her body language and rapacious howling made one thing clear: Veronica had successfully made the austere woman cum."
    stop music fadeout 3.0
    scene pr1760 with dissolve
    "The first of many, with plenty of time to spare to tie Lucy's number of two."
    play music "music/Darkdub.mp3"
    scene pr1761 with dissolve
    scene pr1762 with dissolve
    "*THUD*"
    kat "--oofph!"
    "With little care for Kathleen's comfort, the amazon dropped her like she was a sack of potatoes."
    scene pr1763 with dissolve
    chuck "Hmm... that was {b}fast{/b}."
    "Chuck spoke aloud and clear, directed at no one in particular."
    scene pr1764 with dissolve
    chuck "I've seen Kathy ride men to the point of exhaustion and not been satisfied."
    scene pr1765 with dissolve
    chuck "You're quite skilled, lass."
    scene pr1766 with dissolve
    ver "You haven't seen anything yet, you old pervert. I'm just beginning."
    scene pr1767 with dissolve
    chuck "Bahaha! I'm sure you are. By all means, give us a show."
    scene pr1768 with dissolve
    "To punctuate her confident claim, Veronica grabbed Mrs. Pulman by the arm and placed her over her knee like she was disciplining a child."
    kat "*huff*"
    scene pr1769 with dissolve
    kat "Grr-- I'll admit I underestimated you, but you're getting a little impertinent now, Miss Lynch."
    "Her tone had a venomous edge to it, clearly unpleased at the rough treatment."
    scene pr1770 with dissolve
    play sound "sound effects/slap2.wav"
    scene pr1771 with dissolve
    "*THWACK!*"
    "As if to say {i}tough shit{/i}, Veronica gave Mrs. Pulman's pale, round ass a quick swat."
    scene pr1773 with dissolve
    ver "This is my show, remember?"
    ver "It's your job to lie there and cum like a stupid whore."
    scene pr1772 with dissolve
    play sound "sound effects/slap2.wav"
    scene pr1771 with dissolve
    "*THWACK!*"
    scene pr1773 with dissolve
    ver "Stick your ass out more! Give the boys watching a proper look at the goods!"
    scene pr1774 with dissolve
    "To my surprise, Kathleen complied."
    scene pr1775 with dissolve
    ver "Now... lets do away with these."
    "Veronica then removed Kathleen's panties, revealing her oozing, weeping quim for the room to see."
    "Streaks of girl cum was plastered to the skin of her interior thighs. Part of me was starting to wonder..."
    mct "(Does Mrs. Pulman have a masochistic side...?)"
    scene pr1776 with dissolve
    "*Squelch*"
    "Veronica's finger slide easily into the winking passage."
    ver "You're hungry for more, aren't you slut?"
    kat "You talk too much, Miss. Lynch..."
    ver "Ha! That's rich coming from you."
    scene pr1777 with dissolve
    scene pr1776 with dissolve
    "*Squelch*"
    scene pr1777 with dissolve
    scene pr1776 with dissolve
    scene pr1777 with dissolve
    scene pr1776 with dissolve
    "*Squelch* *Squelch*"
    ver "You know, this is a lot of fun..."
    scene pr1777 with dissolve
    scene pr1776 with dissolve
    "*Squelch*"
    ver "Those first two games weren't... {b}in fact{/b} that second one was hell."
    scene pr1777 with dissolve
    scene pr1776 with dissolve
    scene pr1777 with dissolve
    scene pr1776 with dissolve
    "*Squelch* *Squelch*"
    ver "This third game almost makes me forget that rotten taste in my mouth. {b}Almost{/!}"
    scene pr1778 with dissolve
    play sound "sound effects/slap2.wav"
    scene pr1779 with dissolve
    "*THWACK!*"
    kat "Ghha-!"
    "Removing herself from Kathleen's frothing insides, she gave her yet another slap on the ass -- this time much harder than before."
    scene pr1778 with dissolve
    play sound "sound effects/slap2.wav"
    scene pr1779 with dissolve
    scene pr1778 with dissolve
    play sound "sound effects/slap2.wav"
    scene pr1779 with dissolve
    "*THWACK!* *THWACK!*"
    kat "Gaa--ngg! Damn it!"
    "The memory of the second game was clearly giving the amazon a vindictive, spiteful edge."
    scene pr1780 with dissolve
    "*Squelch*"
    ver "Water under the bridge. This place might be fun..."
    "I wasn't sure if she really believed that or just simply wanted to."
    scene pr1781 with dissolve
    scene pr1780 with dissolve
    scene pr1781 with dissolve
    scene pr1780 with dissolve
    "*Squelch* *Squelch*"
    kat "ngg-nghh-ahh~!--!"
    "Again, sweet bedroom-like sounds started to pour from the cruel woman's gaping maw."
    ver "You call Lucy and I whores, but you're enjoying this..."
    scene pr1781 with dissolve
    scene pr1780 with dissolve
    "*Squelch*"
    ver "You like getting finger fucked to an audience."
    scene pr1781 with dissolve
    scene pr1780 with dissolve
    scene pr1781 with dissolve
    scene pr1780 with dissolve
    "*Squelch* *Squelch*"
    kat "Keep talking Miss Lynch and you'll run out of ti--"
    scene pr1782 with dissolve
    play sound "sound effects/slap2.wav"
    scene pr1783 with dissolve
    "*THWACK!*"
    scene pr1784 with dissolve
    ver "I said you LIKE getting finger fucked to an audience, don't you?"
    kat "--tsk...!"
    scene pr1782 with dissolve
    play sound "sound effects/slap2.wav"
    scene pr1783 with dissolve
    "*THWACK!*"
    scene pr1784 with dissolve
    kat "gnya-- S-stop it!"
    "A cracking, girlish plea was drawn out of Mrs. Pulman's pursed lips."
    scene pr1782 with dissolve
    play sound "sound effects/slap2.wav"
    scene pr1783 with dissolve
    "*THWACK!*"
    scene pr1784 with dissolve
    kat "Gnnn! Fuck!"
    ver "Admit it then."
    scene pr1782 with dissolve
    play sound "sound effects/slap2.wav"
    scene pr1783 with dissolve
    "*THWACK!*"
    scene pr1784 with dissolve
    kat "Gnngh--aaa! Fine! Yes! I'm enjoying this. I'm enjoying getting finger fucked with people watching."
    scene pr1785 with dissolve
    scene pr1786 with dissolve
    ver "Now, that wasn't so hard, was it?"
    scene pr1785 with dissolve
    scene pr1786 with dissolve
    kat "~aaah! *huff* *huff*"
    scene pr1785 with dissolve
    scene pr1786 with dissolve
    scene pr1785 with dissolve
    scene pr1786 with dissolve
    "I could almost swear Mrs. Pulman was cooing from the amazon's gentle touch."
    scene pr1787 with dissolve
    "Back in the audience, the room was... captivated?"
    scene pr1788 with dissolve
    "Isaak, who had thankfully put his dick away, stared at the domineering scene with a concerned look."
    scene pr1789 with dissolve
    "The egotistical movie star seemed utterly captivated by Veronica, clearly admiring his choice in sponsee. I don't think he was even seeing Mrs. Pulman anymore."
    scene pr1790 with dissolve
    "Meanwhile, August had a blank look on his face. It was hard to read."
    "His companion on the other hand, who had previously looked uninterested in being here, was now enraptured by the sight, grinning ear to ear in amusement."
    scene pr1791 with dissolve
    "Ian's interest was clearly written on his face."
    scene pr1792 with dissolve
    "Lastly, Dr. Chuck..."
    "Had a subtle look of curious amusement on his face, like he was watching a movie."
    scene pr1787 with dissolve
    "With the exception of Isaak, everyone seemed unperturbed at the club matriarch's disgraceful treatment."
    scene pr1780 with dissolve
    scene pr1781 with dissolve
    "*Squelch*"
    kat "Aaah-! Ahww--! Nggh--!"
    scene pr1780 with dissolve
    scene pr1781 with dissolve
    "I suppose why would they?"
    "Maybe it was pride in her sportsmanship. Maybe it was the sanctity of the club's rules..."
    scene pr1780 with dissolve
    scene pr1781 with dissolve
    "*Squelch* *Squelch*"
    "Maybe it was simply she didn't want it to stop."
    scene pr1780 with dissolve
    scene pr1781 with dissolve
    scene pr1780 with dissolve
    scene pr1781 with dissolve
    scene pr1780 with dissolve
    scene pr1781 with dissolve
    "*Squelch* *Squelch* *Squelch*"
    "Whatever the reason, Kathleen continued to abide by the rules of the game as Veronica picked up the pace, intent on finishing orgasm #2."
    "She had been going at a leisurely pace, but she did need {b}three{/b} to win after all."
    scene pr1793 with dissolve
    scene pr1794 with dissolve
    "*SLOSH*"
    kat "Agkhh-!"
    scene pr1793 with dissolve
    scene pr1794 with dissolve
    scene pr1793 with dissolve
    scene pr1794 with dissolve
    "*SLOSH* *SLOSH*"
    kat "Ah - Aah - Ah!!"
    scene pr1793 with dissolve
    scene pr1794 with dissolve
    scene pr1793 with dissolve
    scene pr1794 with dissolve
    scene pr1793 with dissolve
    scene pr1794 with dissolve
    "*SLOSH* *SLOSH* *SLOSH*"
    kat "ngg--gha!"
    scene pr1793 with dissolve
    scene pr1794 with dissolve
    kat "*huff* *huff* I c- can't... --ah!"
    scene pr1793 with dissolve
    scene pr1794 with dissolve
    "*SLOSH*"
    ver "You're getting close again, aren't you? You slutty old woman! Panting like this is the first good fuck you've had in ages."
    scene pr1793 with dissolve
    scene pr1794 with dissolve
    scene pr1793 with dissolve
    scene pr1794 with dissolve
    "*SLOSH* *SLOSH*"
    ver "Does {b}Mister{/b} Pulman not satisfy you in the bedroom? Or maybe he's no longer interested in such a miserable bitch."
    scene pr1793 with dissolve
    scene pr1794 with dissolve
    scene pr1793 with dissolve
    scene pr1794 with dissolve
    scene pr1793 with dissolve
    scene pr1794 with dissolve
    "*SLOSH* *SLOSH* *SLOSH*"
    kat "Gaa-h! I'm goint to cum cumming! I'm cumming!"
    scene pr1795 with dissolve
    ver "Then cum for me you intolerable cunt!"
    scene pr1796 with dissolve
    play sound "sound effects/slap2.wav"
    "*THWACK!*"
    scene pr1797 with dissolve
    kat "Gnnaaaa-- ghghghgk-- fffhk--!"
    "As a coup de grace, Veronica brought her palm down HARD on the Mrs. Pulman's bruised cheeks, releasing the floodgates."
    kat "Fhhk-- ngghg! --shwit--!"
    "The dignified woman was now shamelessly spraying the stage in girl spunk, wailing pleasurably without an ounce of restraint."
    scene pr1798 with dissolve
    kat "gh...why--wahy whant it stahp..."
    kat "....gh....ghk!"
    scene pr1799 with dissolve
    ver "No time to rest, slut."
    kat "..gh--huh? waht...?"
    scene pr1800 with fade
    ver "Time?!"
    "The amazon barked, more like a command than a question."
    scene pr1801 with dissolve
    mc "Two minutes and forty seconds."
    "*Smch...*"
    scene pr1802 with dissolve
    "*Smch...* *Mpgfh...*"
    scene pr1803 with dissolve
    ver "That's more than enough time."
    scene pr1804 with fade
    "Remaining confident, Veronica slid down the length of Kathleen's torso, bringing her face up to the woman's overworked, swollen quim and promptly got to work."
    "*Smch...*"
    scene pr1805 with dissolve
    "This time she took a gentle approach, lapping at the insensate woman's vulva and inner folds with precise, expert tongue work."
    "*Smch...* *Mpgfh...*"
    "Veronica clearly knew her way around a woman's body, which explained why she had been so brazen in picking Mrs. Pulman in the first place."
    scene pr1806 with dissolve
    scene pr1807 with dissolve
    scene pr1806 with dissolve
    scene pr1807 with dissolve
    "*Smch...* *Mpgfh...* *Fhwup...*"
    "Soon, Mrs. Pulman's listless form began showing signs of pleasure. Her overstimulated nether regions, dulled by pleasure, was responding to the towering woman's gentle lapping."
    kat "You-you're good at that..."
    scene pr1808 with dissolve
    kat "I should've had you pegged as a lesbian."
    "*Smch...* *Mpgfh...*"
    scene pr1809 with dissolve
    scene pr1810 with dissolve
    "With no time to respond, Veronica carried in her attentions, reaching an arm up to her partner's exposed breasts."
    scene pr1809 with dissolve
    scene pr1810 with dissolve
    "Her nipples had long since formed into an engorged points, allowing them to fit nicely between the red-head's limber fingers."
    scene pr1809 with dissolve
    scene pr1810 with dissolve
    kat "Ah~♥ *huff* *huff*"
    "Veronica pinched and rolled the sensitive peaks, not once letting up on her service below."
    scene pr1809 with dissolve
    scene pr1810 with dissolve
    "Her well-paced efforts were paying off."
    "Mrs. Pulman eyes had fogged over in the pleasure, not so much peering up at the exhibition hall's red ceiling as she had simply tuned out all worldly surroundings except her own pleasure.."
    "The only thing that was registering with her was the dutiful tongue lashing happening happening below, in between her wide, ivory-like thighs."
    scene pr1811 with dissolve
    kat "Ah~yes! --yuess!"
    "A pleasurable twitch involuntarily sent her long, pale legs wrapping around the back of the Veronica's head, wantonly pulling the amazon closer."
    "This woman, who had not an hour ago sadistically cackled while she degraded the prospective carnations, was now mewling like a bitch in heat."
    "*Smch...*"
    scene pr1812 with dissolve
    "*Smch...* *Mpgfh...*"
    "*Smch...* *Mpgfh...* *Fhwup...*"
    "The way Mrs. Pulman's stern face had contorted into a pleasured, animal-like expression..."
    scene pr1813 with dissolve
    "The sight was getting to me."
    "My dick was standing at full attention, straining painfully against my slacks."
    "*Smch...*"
    "Hell, honestly this whole night..."
    scene pr1814 with dissolve
    "Veronica and Lucy being paraded around and toyed with."
    scene pr1815 with dissolve
    "Veronica guzzling down ounce after ounce of semen."
    scene pr1816 with dissolve
    "Lucy riding Ian into the dirt, desperate for a win."
    scene pr1813 with dissolve
    "This whole night interfaced with something deep down in me, something untouched and unused."
    "The stirring I was feeling in response to that, it made me feel..."
    hide screen textbox2 with dissolve
    menu:
        "Excited. [gr]\[Toughness +1\]":
            $ toughness += 1
            $ toughness = clamp(toughness, 0, 30)
            show screen textbox2 with dissolve
            scene pr1817 with dissolve
            "Excited. Never in my boring life had I the chance to glimpse such erotic sights in person."
        "Scared. [red]\[Toughness -1\]":
            $ toughness -= 1
            $ toughness = clamp(toughness, 0, 30)
            show screen textbox2 with dissolve
            scene pr1818 with dissolve
            "Scared. The charms of this indecent place was getting to me and that scared me."

    scene pr1819 with dissolve
    mc "You have a minute remaining."
    "I called out, to give the red-headed woman fair warning, and to take my mind off my unslaked lusts."
    scene pr1820 with dissolve
    "*Smch...*"
    "*Smch...* *Mpgfh...*"
    scene pr1821 with dissolve
    scene pr1822 with dissolve
    kat "Ah~♥ so-so- close..."
    "Mrs. Pulman delightfully cooed."
    scene pr1821 with dissolve
    scene pr1822 with dissolve
    scene pr1821 with dissolve
    scene pr1822 with dissolve
    "Spurred on by the sweet admission, an invigorated Veronica folded the squeaking slut in half, pressing her legs as far as they'd go inwards, finish line in sight."
    "The formely gentle pace had descended into a controlled frenzy, the amazon's long pink tongue hungrily probing as deep as it could reach."
    scene pr1821 with dissolve
    scene pr1822 with dissolve
    "*Smch...*"
    "41s... 42s..."
    scene pr1821 with dissolve
    scene pr1822 with dissolve
    scene pr1821 with dissolve
    scene pr1822 with dissolve
    "*Smch...* *Mpgfh...*"
    "The clock was ticking down."
    scene pr1821 with dissolve
    scene pr1822 with dissolve
    scene pr1821 with dissolve
    scene pr1822 with dissolve
    "*Smch...* *Mpgfh...* *Fhwup...*"
    "...would she make it?"
    "In a twisted way, I was rooting for her deep down."
    scene pr1821 with dissolve
    scene pr1822 with dissolve
    kat "nggh--! Shit! I'm-- I'm--"
    scene pr1821 with dissolve
    scene pr1822 with dissolve
    kat "fuckfuckfuckFuckFuckFUCKFUCKFUCK!!"
    scene pr1821 with dissolve
    scene pr1822 with dissolve
    scene pr1821 with dissolve
    scene pr1822 with dissolve
    scene pr1821 with dissolve
    scene pr1823 with dissolve
    kat "yesyesYesYesYESYESYESS!!!!!"
    kat "Bhibhiiiii~♥"
    "With a blaring howl, Mrs. Pulman had reached her last climax."
    scene pr1824 with fade
    kat "*huff* huff*"
    "Putting her at a score of three, against Lucy's two."
    kat "giwhahtamI..."
    "20s... 19s..."
    kat "*huff* huff* Ahhhheebi...♥ "
    scene pr1825 with dissolve
    "13s... 12s..."
    kat "whathts...? ...huhh?"
    ver "I said I wasn't stopping at three, didn't I?"
    "05s... 04s..."
    ver "I want to see how far that tight clam of yours can stretch..."
    scene pr1826 with dissolve
    mc "--TIME!"
    stop music fadeout 2.0
    scene pr1827 with dissolve
    kat "*huff* *huff* Eheee..."
    "Coming down from back-to-back-to back orgasms, Mrs. Pulman was in no condition to officiate the night's closing or even announce the winner."
    "Not that she had to. One look into Mrs. Pulman's vacuous eyes was all you needed to see that Veronica had thoroughly outdone Lucy and Ian's performance."
    scene pr1828 with dissolve
    play music "music/cold-sober.mp3"
    chuck "Well, well, well..."
    chuck "Looks like we have a winner. Miss Lynch, having won the first and last game, is our final carnation for the summer exhibition."
    scene pr1829 with dissolve
    chuck "Isn't that great, lass? Everyone, give her a hand."
    $ renpy.end_replay()
    if not persistent.FEG3VeroGallery:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.FEG3VeroGallery = True
    scene pr1830 with dissolve
    "Samson was the only one who indulged Dr. Chuck, his large hands thunderously clapping, hooting and hollering like this was all thanks to him."
    sam "Haha! You're going to win this whole thing. I just know it!"
    scene pr1831 with fade
    lucy "..."
    kil "Ah, come on, cheer up..."
    kil "I know it might seem like you did all of this for nothing, but..."
    "Ian, in all his all his witless charm, couldn't find the words to comfort his partner."
    kil "Uh, I guess because you DID do it for nothing..."
    scene pr1832 with dissolve
    isak "I wouldn't say that, Mr. Beaufort. There is ANOTHER way we can get her son into St. Ives..."
    scene pr1833 with fade
    $ history_lucy = "Despite her determined efforts, the schoolteacher failed to earn a spot in the club's summer exhibition, making the humiliating treatment she endured all for naught."
    $ history_veronica = "Beating Lucy quite handily, Veronica has earned the final spot in the club's summer exhibition. There she seeks to remedy the financial woes that's facing her gym. I'm pretty sure she doesn't like me, not that I blame her."
    $ unread_lucy = True
    $ unread_veronica = True
    play sound "sound effects/notification.wav"
    show bioupdate with dissolve
    $ renpy.pause(3, hard=True)
    kat "Guh... *huff* *huff*..."
    "In the meantime, Dr. Chuck and I gave Mrs. Pulman a hand getting to her feet."
    "Despite being little more than dead weight, she felt surprisingly light. A fact that reminded me that she was a woman and not just some ivory-towered monster."
    mct "(Well, I suppose Veronica had already AMPLY demonstrated that fact...)"
    kat "Tsk...! That bitch really did it...!"
    scene pr1834 with dissolve
    play sound "sound effects/slap1.wav"
    "*THWACK!*"
    scene pr1835 with dissolve
    hana "Don't TOUCH me!"
    aug "Hana, dear..."
    scene pr1836 with dissolve
    hana "I don't want to hear that shit, August!"
    hana "Go fuck yourself, you decrepit old chode!"
    scene pr1837 with dissolve
    chuck "Hah... kids these days."
    scene pr1838 with dissolve
    "In a fit of anger, Hana had stormed off."
    if toughness >= 20:
        "Best I could tell, the old man must've made a move on her..."
    else:
        "Best I could tell, Mr. Byrnes must've made a move on her..."

    "No, it seemed more than that, considering the type of place this is..."
    scene pr1833 with dissolve
    kat "I've got a change of clothes in my office."
    "There was a sense of expectation in her voice. Considering her shaky legs, I can guess she wants a steady hand to guide her there."
    hide screen textbox2 with dissolve
    menu:
        "Follow Hana and put your nose where it doesn't belong. [gr]\[Hana +2\]":
            $ Hana_Affection += 2
            $ Hana_Affection = clamp(Hana_Affection, 0, 40)
            show screen textbox2 with dissolve
            jump prFaceOffHanaEnding

        "Help Mrs. Pulman to her office. [gr]\[Kathleen +2\]":
            $ Kathleen_Affection += 2
            $ Kathleen_Affection = clamp(Kathleen_Affection, 0, 30)
            show screen textbox2 with dissolve
            jump prFaceOffKatEnding



label prFaceOffHanaEnding:

    "Even if it doesn't involve me, I want to chase after her. I can't help it. There's something about a distressed, beautiful girl that makes me want to stick my nose where it doesn't belong."
    if toughness >= 19:
        "Hell, maybe I could give her someone to vent to. A shoulder to cry on...? One thing could lead to another and..."

    scene pr1839 with dissolve
    mc "Sorry. I've got to go check on something..."
    mc "You got Mrs. Pulman, right Dr. Chuck?"
    chuck "Uh..."
    scene pr1840 with dissolve
    mc "See ya!"
    stop music fadeout 2.0
    scene black with fade
    "......"
    "..."
    scene pr1841 with blinds
    "Hana had already taken the elevator up by the time I left the exhibition hall, fortunately my guess of where a bartender would run off to proved to be on the nose."
    play music "music/thief-in-the-night.mp3"
    scene pr1842 with dissolve
    hana "Huh... I expected the old man to walk in here, not you."
    hana "Did August send you?"
    mc "No, I just wanted to see if you were okay."
    hana "Cool, pull up a seat then."
    scene pr1843 with fade
    hana "You know Jacob, right?"
    jacob "Yeah, we've met."
    scene pr1844 with dissolve
    jacob "'You want a hit?"
    hide screen textbox2 with dissolve
    menu:
        "Sure, why not? [gr]\[Hana +1\]":
            $ Hana_Affection += 1
            $ Hana_Affection = clamp(Hana_Affection, 0, 40)
            show screen textbox2 with dissolve
            scene pr1845 with dissolve
            "Puff, puff, pass right?"
            scene pr1846 with dissolve
            "......"
            scene pr1848 with dissolve
            "..."

        "No thanks.":
            show screen textbox2 with dissolve
            scene pr1847 with dissolve
            mc "No, thanks. That stuff makes me paranoid."
            scene pr1848 with dissolve
            jacob "Suit yourself."

    scene pr1849 with dissolve
    "..."
    hana "Ah, this is good shit. My roommate may be a douche, but he knows where to get good weed."
    scene pr1850 with dissolve
    jacob "You should try the stuff they grow in Afghanistan."
    scene pr1851 with dissolve
    jacob "Well, I should get back out before anyone notices I'm missing from my post."
    jacob "Thanks for the kush, Hana."
    hana "Aaaw, anytime. See you Jacob."
    scene pr1852 with dissolve
    jacob "[mcf]."
    "The bouncer gave me a solemn nod before departing."
    scene pr1853 with dissolve
    "..."
    scene pr1854 with dissolve
    hana "So...! How you'd like your first taste of this place? Pretty {b}fucked up{/b}, right?"
    scene pr1855 with dissolve
    mc "It was... {i}something{/i}, alright."
    scene pr1856 with dissolve
    hana "Yeah, something rotten and {i}diseased{/i}. Only a creep would want to work here."
    scene pr1857 with dissolve
    mc "I can't help but notice YOU work here too..."
    scene pr1858 with dissolve
    hana "FUCK! Don't remind me!"
    "The subject of her employment is CLEARLY a sore spot for the tattooed woman."
    mc "My bad..."
    scene pr1859 with dissolve
    hana "Ah, shit, it's not your fault new guy..."
    scene pr1860 with dissolve
    mc "Whose fault is it?"
    scene pr1861 with dissolve
    hana "Mine? The old man? The goddamn world? I don't fucking know, but I'm not going to get into it with you."
    hana "I don't even know you. No offense."
    scene pr1862 with dissolve
    mc "..."
    scene pr1863 with dissolve
    hana "..."
    scene pr1862 with dissolve
    "I had no idea how to respond to that."
    scene pr1864 with dissolve
    hana "I need to get out of here. You ever ridden a motorcycle? Next to fucking, it's the best cure-all for anxiety crushing stress."
    scene pr1865 with dissolve
    mc "Are you offering me a ride home...?"
    scene pr1859 with dissolve
    hana "We're co-workers now, aren't we?"
    scene pr1866 with dissolve
    hana "What do you say, new guy? Don't mind riding bitch seat do you?"
    scene pr1867 with dissolve
    mc "..."
    stop music fadeout 2.0
    scene black with fade
    "......"
    "..."
    "*Flume-flume* *Ratatata*"
    scene pr1868 with dissolve
    "Happy to put an end to the night, I left with Hana on her motorbike."
    "The machine sputtered on, sounding like a blender of bolts."
    "It was my first time riding one, and not being the one in control, left me feeling vulnerable."
    "Wanting to hold onto something."
    scene pr1869 with dissolve
    hana "You good back there, new guy?"
    scene pr1868 with dissolve
    "I..."
    hide screen textbox2 with dissolve
    menu:
        "Place your hands on the biker's hips. [gr]\[Hana +1\]":
            $ Hana_Affection += 1
            $ Hana_Affection = clamp(Hana_Affection, 0, 40)
            show screen textbox2 with dissolve
            "You know, only because of the added sense of security it provides, and definitely NOT because the sweet, fruity scent of Hana's bath gel making me want to be closer to her."
            scene pr1870 with dissolve
            mc "Sure, let's go."
            scene pr1871 with dissolve
            hana "Hold on tight."
            scene pr1872 with dissolve
            play sound "sound effects/motorcycle-ride.wav"
            "*Flume-flume-flume* *Ratatata*"
            scene pr1876 with dissolve


        "Place your hands on the biker's shoulders.":
            show screen textbox2 with dissolve
            scene pr1873 with dissolve
            mc "Uh, yeah, let's go."
            scene pr1874 with dissolve
            hana "Hold on tight."
            scene pr1875 with dissolve
            play sound "sound effects/motorcycle-ride.wav"
            "*Flume-flume-flume* *Ratatata*"
            scene pr1877 with dissolve

    play music "music/big-rock.mp3"
    "......"
    "..."

    scene black with blinds
    "After a leisurely drive through the city, we arrived at my apartment."
    scene pr1878 with blinds
    stop music fadeout 3.0
    "Getting off the bike, I discovered my legs had turned to jelly somewhere during the twenty minute tussle with the midnight-blue machine."
    play music "music/cold-sober.mp3"
    scene pr1879 with dissolve
    hana "Smooth as silk, isn't she?"
    hana "You should be grateful. I usually only let cute girls on Suzie Q, not pervy guys who work at an underground sex club."
    scene pr1880 with dissolve
    mc "...YOU work at an underground sex club."
    scene pr1881 with dissolve
    hana "Fuck! Don't remind me."
    "Déjà vu..."
    scene pr1882 with dissolve
    mc "Why do you work at the club if you hate it so much?"
    hana "..."
    scene pr1883 with dissolve
    hana "Let me ask you something, [mcf]."
    scene pr1884 with dissolve
    "Her tone had shifted to a more serious timbre."
    scene pr1883 with dissolve
    hana "You working there because you're a degenerate or because...?"
    scene pr1884 with dissolve
    mc "...ah, well. It pays EXTREMELY well..."
    scene pr1883 with dissolve
    hana "I thought so. You don't really look like you fit the bill."
    scene pr1885 with dissolve
    hana "The last guy, Darius, that guy was a walking veneral disease. Practically spouting out noxious fumes when he walked."
    scene pr1883 with dissolve
    hana "Anyway, it's the same with me I guess. Tending bar at the club makes my personal situation infinitely more manageable."
    scene pr1885 with dissolve
    hana "I mean, don't get me wrong. I don't think there's anything wrong with consenting adults FREELY fucking however they want. I'm not some kind of puritan if you haven't guessed."
    scene pr1883 with dissolve
    hana "We both know that place isn't that though. Or at least I hope you do."
    scene pr1886 with dissolve
    mc "It's..."
    hide screen textbox2 with dissolve
    menu:
        "It's taking advantage of women in desperate situations. [gr]\[Hana +1\] [red]\[Toughness -1\]":
            $ Hana_Affection += 1
            $ Hana_Affection = clamp(Hana_Affection, 0, 40)
            $ toughness -= 1
            $ toughness = clamp(toughness, 0, 30)
            show screen textbox2 with dissolve
            scene pr1887 with dissolve
            hana "Exactly!"
            hana "I'm glad you don't see it like your asshole friend does at least."

        "It's not like anyone is forced to be there though. [gr]\[Toughness +1\] [red]\[Hana -2\]":
            $ Hana_Affection -= 2
            $ Hana_Affection = clamp(Hana_Affection, 0, 40)
            $ toughness += 1
            $ toughness = clamp(toughness, 0, 30)
            show screen textbox2 with dissolve
            scene pr1888 with dissolve
            hana "That's the same shit Ian says. Which is {b}bullshit{/b}!"
            hana "Sometimes we only have the illusion of choice."
            if perk_socialChameleon == True or perk_socialButterfly == True:
                "She's conflating her own feelings about working there with the other girls' situation."
                "She doesn't feel like she has agency, so no one else does either."

    scene pr1889 with dissolve
    mc "Yeah, maybe..."
    "This thread of small talk was getting down to the conversational spool, and wanting to get out of this damn dancing monkey outfit, I moved to bring our chat to its conclusion."
    mc "Anyway, thanks for the ride."
    scene pr1890 with dissolve
    hana "No problem. We're coworkers. Pass it forward some time."
    scene pr1891 with dissolve
    hide screen textbox2 with dissolve
    menu:
        "Ask if she wants to come in.":
            show screen textbox2 with dissolve
            mc "You want to come in for a drink or something?"
            scene pr1892 with dissolve
            hana "Awww, new guy. You're not trying to get in my pants, are you?"
            hana "I don't even know you."
            scene pr1893 with dissolve
            mc "N-no, you just you know... gave me a ride. It'd be shitty not to offer."
            scene pr1894 with dissolve
            hana "Sure, sure..."
            scene pr1895 with dissolve
            mc "..."
            scene pr1896 with dissolve
            hana "Pfft--relax! I'm just teasing you."
            scene pr1887 with dissolve
            hana "Maybe some other time though, if you keep NOT being an asshole."
            scene pr1890 with dissolve
            hana "Bye!"

        "Say goodnight and leave.":
            show screen textbox2 with dissolve
            mc "I guess I'll see you around. Good night!"
            scene pr1890 with dissolve
            hana "Same. Take it easy, new guy!"

    scene pr1897 with fade
    "With that, Hana's bike ride off into the city night."
    stop music fadeout 2.0
    scene black with fade
    "I could hear it's mechanical blare all the way into the lobby of my apartment building.."
    "........."
    "......"
    "..."
    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionhana01 with blinds
    $ renpy.pause(6, hard=True)
    jump prMeetTheCarnations

label prFaceOffKatEnding:

    "Whatever that was about, it's none of my business. I should score some points with my new boss instead."
    scene pr1898 with dissolve
    mc "I got her."
    chuck "You sure lad? She's going to be ornery after all that."
    scene pr1899 with dissolve
    kat "Oh, stop it Charles! I'm not some petulant child!"
    scene pr1900 with dissolve
    chuck "Please, you're the same girl I've known for two decades. Your beauty hasn't faded, but neither has your thorny side. Bahaha!"
    scene pr1901 with dissolve
    "Dr. Chuck's flattery seems to appease Kat a little, a small smile spreading across her face."
    scene pr1902 with dissolve
    mc "I... think I can handle it."
    scene pr1903 with dissolve
    chuck "Don't say I didn't warn you if she ends up biting your head off like a praying mantis, lad."
    scene pr1904 with dissolve
    kat "Away we go, Mr. [mcl]. Before he keeps talking. Please."
    stop music fadeout 2.0
    scene black with fade
    "......"
    "..."
    play music "music/jazz-piano-bar.mp3"
    scene pr1905 with dissolve
    kat "Thanks for lending me your shoulder, [mcf]."
    scene pr1906 with dissolve
    kat "I think I've mostly recovered from that cow's manhandling. The feeling has returned to my legs at least."
    mc "Yeah, no problem."
    scene pr1907 with dissolve
    kat "...hmm."
    kat "..."
    scene pr1908 with dissolve
    kat "I will say this. You got a softer face than your predecessor."
    scene pr1907 with dissolve
    "I wasn't sure how to respond to that."
    scene pr1909 with dissolve
    kat "It's a compliment, but don't let it go to your head."
    scene pr1907 with dissolve
    mc "Right..."
    scene pr1910 with dissolve
    kat "I'm going to get changed now. Have a seat."
    scene pr1907 with dissolve
    hide screen textbox2 with dissolve
    menu:
        "Offer to go outside. [gr]\[Kathleen +1\]":
            $ Kathleen_Affection += 1
            $ Kathleen_Affection = clamp(Kathleen_Affection, 0, 30)
            show screen textbox2 with dissolve
            scene pr1911 with dissolve
            mc "Wouldn't you prefer me to go outside?"
            scene pr1912 with dissolve
            kat "My, my... such a gentleman."
            scene pr1910 with dissolve
            kat "Sit! You just saw that meat golem tongue punch me until I couldn't speak."
            kat "I think you can stay."
            scene pr1907 with dissolve
            mc "You raise a good point, I guess..."



        "Do as she asks. Sit down.":
            show screen textbox2 with dissolve
            "I wasn't sure what else business she had with me, but I did as she asked."

    scene black with fade
    "..."
    scene pr1913 with dissolve
    kat "Aaah! That's better."
    scene pr1914 with dissolve
    kat "Come to think of it, you should leave at least a couple of changes of clothes here. It's a... handy thing to have in this place."
    scene pr1915 with dissolve
    mc "I think tonight helped me understand that."
    scene pr1916 with dissolve
    kat "I'm glad we have a chance to speak alone."
    mc "You are...?"
    scene pr1917 with dissolve
    kat "Yes. I'd like to get to know you better, [mcf]."
    scene pr1918 with dissolve
    mc "Why is that?"
    scene pr1919 with dissolve
    kat "It's important to know the people who work for you."
    scene pr1920 with dissolve
    kat "Don't want you running off like Ian's dumbass friend before you."
    "That's the second time tonight she's mentioned him."
    scene pr1921 with dissolve
    mc "Why'd he... quit?"
    scene pr1922 with dissolve
    kat "Oh, he didn't {i}quit{/i}. He dropped off the face of the planet."
    scene pr1923 with dissolve
    mc "What does that mean? He just disappeared?"
    scene pr1924 with dissolve
    kat "Exactly. Just stopped showing up. Number out of service. All the stuff left in his apartment, but him: {b}gone{/b}."
    scene pr1923 with dissolve
    mc "Isn't that kinda weird? Something could have happened to him. Maybe an accident. Maybe he could be..."
    scene pr1924 with dissolve
    kat "Dead in a ditch somewhere?"
    scene pr1922 with dissolve
    kat "Believe me, I had people look into it. Not. a. thing."
    kat "Effectively, he just vanished into thin air..."
    scene pr1925 with dissolve
    kat "No matter. He was unreliable anyway, thanks to a nasty proclivity toward party drugs. He was chronically late and he ran his mouth all the time."
    scene pr1923 with dissolve
    mc "Sounds like I have a low bar to live up to..."
    scene pr1926 with dissolve
    kat "Quite."
    kat "I'll pour us a drink."
    "It sounded more like a command than a hospitable invitation."
    scene black with fade
    "..."
    scene pr1927 with dissolve
    "After she returned, we made small talk for a little while."
    "About my hobbies and about my classes mostly. She shared a little bit about herself as well."
    kat "The relief was my older sister's thing. I took over after she passed."
    scene pr1928 with dissolve
    kat "She was the... {i}altruistic{/i} one amongst my brother and myself. Had the gall to make us feel like shit for just enjoying what life had given us."
    scene pr1927 with dissolve
    kat "Don't get me wrong, I loved that woman, but I could've also strangled her."
    mct "(Yeah, loved her so much you turned her charity into your hunting grounds...)"
    scene pr1929 with dissolve
    mc "I see. She sounded... nice."
    scene pr1927 with dissolve
    kat "How about you? What kind of person was your father?"
    "I'm reminded of the background check she ran on me."
    mct "(Right, she knows all about that...)"
    kat "He died in a traffic accident when you were seven, right?"
    scene pr1930 with dissolve
    mc "Yeah, honestly I was so young and the time was so stressful..."
    scene pr1929 with dissolve
    mc "I don't really remember much about him. Just the hole that he left in my mother when he died."
    scene pr1930 with dissolve
    mc "If I go a while without looking at one of my mother's pictures of him, it can be difficult to recall his face."
    scene pr1928 with dissolve
    kat "Don't feel bad about that. You were young and time is cruel, and while hurt feelings won't simply disappear, it does eventually bring us to an equilibrium in our lives."

    if perk_socialChameleon == True or perk_socialButterfly == True:
        "There was a surprisingly tender affectation to her words, bereft of artifice or just the usual feeling that she's talking just because she loves to hear herself speak."
        "She really means what she's saying."

    scene pr1931 with dissolve
    kat "Your mother loved your father then?"
    scene pr1932 with dissolve
    "Oddly enough, talking about this with someone openly (even her) was filling me with a warm feeling."
    mc "Yeah, without a doubt."
    mc "What about you? You're married right? {b}Mrs.{/b} Pulman."
    scene pr1933 with dissolve
    kat "That's right. Life is... unfair."
    scene pr1934 with dissolve
    mc "What makes you say that?"
    scene pr1933 with dissolve
    kat "Well, your mother didn't get enough time with the love of her life, while me..."
    scene pr1935 with dissolve
    stop music fadeout 2.0
    kat "..."
    scene pr1933 with dissolve
    kat "Thirty years later, I'm still chugging along with an old bastard who simply REFUSES to die."
    mc "..."
    scene pr1936 with dissolve
    kat "Relax! I'm only kidding. You gotta learn to cut loose if you want to thrive in a place like this."
    scene pr1931 with dissolve
    play music "music/on-the-ground.mp3"
    kat "Speaking of which, how did you enjoy tonight's fare? Albeit a small offering, it was your first taste of what the club has on tap. I'm interested in hearing your thoughts."
    scene pr1932 with dissolve
    mct "(What did I think of this shitshow tonight...?)"
    mc "Truthfully, well..."
    hide screen textbox2 with dissolve
    menu:
        "I enjoyed it more than I thought I would. [gr]\[Kathleen +1\] \[Toughness +1\]":
            $ Kathleen_Affection += 1
            $ Kathleen_Affection = clamp(Kathleen_Affection, 0, 30)
            $ toughness += 1
            $ toughness = clamp(toughness, 0, 30)
            show screen textbox2 with dissolve
            scene pr1938 with dissolve
            mc "I couldn't take my eyes off of it. This whole thing is twisted, but..."
            scene pr1937 with dissolve
            mc "I can't argue that seeing Lucy and Veronica compete wasn't exciting."
            scene pr1939 with dissolve
            kat "That's a more honest answer than I expected from you. It's natural to feel conflicted."
            kat "The dichotomy between what you know is in good taste and what your animal instincts finds stimulating is... delectable."

        "It was a bit... much. [red]\[Toughness -1\]":
            $ toughness -= 1
            $ toughness = clamp(toughness, 0, 30)
            show screen textbox2 with dissolve
            scene pr1940 with dissolve
            mc "I can't shake the feeling that this whole enterprise is deplorable."
            scene pr1941 with dissolve
            kat "Yet, here you are..."
            scene pr1931 with dissolve
            kat "Well, you don't hesitate to say how you truly feel at least. I like that myself, but fair warning: keep that trait to a minimum around our clientelle."
            kat "By the large, they're men accustomed to sycophantic flattery and knob polishing."
            scene pr1936 with dissolve
            kat "Part of you likes it though, right?"
            scene pr1937 with dissolve
            mc "I'd be lying if I didn't admit I found the games exciting."
            scene pr1939 with dissolve
            kat "I thought so. I could tell."

    scene pr1942 with dissolve
    kat "Tell me. What game of the three was your favorite? I want your honest answer."
    scene pr1932 with dissolve
    mc "I guess..."
    hide screen qmenu with dissolve
    hide screen textbox2 with dissolve
    menu:
        "The first game: I liked watching the girls dance.":
            show screen textbox2 with dissolve
            show screen qmenu with dissolve
            mc "The opening game, with the motorized vibrators. Watching the girls squirm was something... {i}new{/i}."
            scene pr1936 with dissolve
            kat "It was great, right? That one's a crowd pleaser. Being able to dictate the pace of the event has its advantages."
            scene pr1941 with dissolve
            kat "The way Miss Lynch kept her composure at the end... that was a surprise. She's going to make a promising carnation."
            scene pr1933 with dissolve
            kat "I honestly don't know how the other Carnations will stand a chance against that kind of determination."
            scene pr1936 with dissolve
            kat "Then again, with what I've learned from these exhibitions, things have a way of surprising you."

        "The second game: I didn't know a human being could ingest that much semen. [gr]\[Toughness +1\]":
            $ toughness += 1
            $ toughness = clamp(toughness, 0, 30)
            show screen textbox2 with dissolve
            show screen qmenu with dissolve
            "It was kind of fucked up to admit, but..."
            mc "The punishment game."
            scene pr1943 with dissolve
            kat "Really...? That's surprising."
            scene pr1939 with dissolve
            kat "I would've thought watching a woman choke down half a liter of ball-juice would be too hardcore for you."
            scene pr1938 with dissolve
            mc "..."
            scene pr1936 with dissolve
            kat "Oh, don't be embarrassed! It's good you're a fucked up pervert. It's practically a bonafide job requirement."
            scene pr1939 with dissolve
            kat "Like I tell prospective members... what's the point of having an obscene amount of money if you can't be honest about what a disgusting pervert you are?"
            scene pr1938 with dissolve
            mc "...that's uh, that's a sales pitch I guess..."

        "The third game: I liked how frenzied Lucy was.":
            show screen textbox2 with dissolve
            show screen qmenu with dissolve
            mc "The match with Lucy and Ian... I like how frantic it got by the end."
            scene pr1936 with dissolve
            kat "You like a little taste of desperation, eh?"
            scene pr1932 with dissolve
            mc "I wouldn't say that."
            scene pr1941 with dissolve
            kat "It's true. You were getting off to the exploitative nature of the game."
            scene pr1940 with dissolve
            mc "..."
            scene pr1938 with dissolve
            kat "Oh, don't clam up on me. At the Carnation Club, you don't need to be dishonest about what turns you on."
            scene pr1939 with dissolve
            kat "Like I tell prospective members... what's the point of having an obscene amount of money if you can't be honest about what a disgusting pervert you are?"
            scene pr1938 with dissolve
            mc "...that's uh, that's a sales pitch I guess..."

        "The third game: Veronica and you. [gr]\[Kathleen +1\]":
            $ Kathleen_Affection += 1
            $ Kathleen_Affection = clamp(Kathleen_Affection, 0, 30)
            show screen textbox2 with dissolve
            show screen qmenu with dissolve
            scene pr1944 with dissolve
            mc "The last match of the last game, with Veronica and..."
            scene pr1945 with dissolve
            kat "Oh? You liked that?"
            scene pr1946 with dissolve
            kat "Seeing that overdeveloped tramp have a go at me?"
            scene pr1947 with dissolve
            mc "Uh, I mean..."
            "Truth be told, the answer to her question was a stark {i}yes{/i}. Seeing the roles get reversed like that was {b}hot{/b}, but I'm starting to feel like I just willingly stepped into a mine field."
            kat "..."
            mc "..."
            mc "*clears throat* *ahem*"
            scene pr1948 with dissolve
            kat "Oh, I'm just fucking with you!"
            scene pr1941 with dissolve
            kat "Truth be told, that was an unexpected development, but I can't say I didn't enjoy the hands on evaluation."
            scene pr1939 with dissolve
            kat "It can be fun giving up control for a little bit. You should try it some time. Why I could tie you up and tickle you funny right now..."
            scene pr1949 with dissolve
            mc "N-no, no thanks. I'm good..."


    scene pr1950 with dissolve
    kat "Come to think of it, you didn't get a chance to pop your cork tonight, did you?"
    scene pr1951 with dissolve
    kat "It's got to be frustrating..."
    scene pr1958 with dissolve
    kat "To be so young and virile, watching all that fun, and not having any yourself...?"
    scene pr1959 with dissolve
    "The cruel woman's sudden amorous advance left me unable to speak."
    "Absent was the pheromone-laced perfume that she had previously weaponized. Instead, the tumescent growth in my pants could only be owed to Mrs. Pulman's womanly charms."
    scene pr1952 with dissolve
    stop music fadeout 3.0
    kat "I'm going to make you a promise, [mcf]. About the Carnation Club and your job..."
    play music "music/leaving-home.mp3"
    kat "Don't be a fucking idiot and this place will be good to you. It'll take care of you."
    kat "All you need to do is know when to shut-up, avoid stepping on our members toes, and follow everything I say."
    scene pr1953 with dissolve
    kat "The Carnation Club is mine, first and foremost. Forget about Charles and Auggy. You answer to me."
    kat "If you can do that, well, I'll let you live out all your fucked up fantasies with impunity."
    mc "..."
    scene pr1954 with dissolve
    kat "I want you sleep on those words. Internalize them. Carve it into the back of your eyelids if you have to."
    scene pr1955 with dissolve
    kat "Don't be like... Darius."
    "The ice coldness of her words had brought the blood in my veins to a standstill."
    scene pr1956 with dissolve
    mc "R-right..."
    scene pr1957 with dissolve
    kat "I'm glad we had this talk, Mr. [mcl]. Let me get Warren to drive you home."
    stop music fadeout 2.0
    scene black with fade
    "........."
    "......"
    "..."
    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionveronica01 with blinds
    $ renpy.pause(6, hard=True)

    jump prMeetTheCarnations

label prMeetTheCarnations:
    $ date = "may14day"
    stop sound
    scene pr1960 with blinds
    play music "music/study-and-relax.mp3"
    show screen textbox2 with dissolve
    show screen qmenu with dissolve
    show may14day with squares
    "The next couple of days were uneventful. I heard nary a peep from Mrs. Pulman, Dr. Chuck, or even Ian."
    scene pr1961 with dissolve
    $ date = "may15night"
    show may15night with squares
    "I passed the time watching dumb movies and running MCAT drills. After all the excitement of the past week, part of me appreciated the repose."
    scene club-fr-day with dissolve
    $ date = "may16day"
    show may16day with squares
    "Saturday, I received a call from Mrs. Pulman, asking me to come to the club's bar."
    "She didn't care to expound on the reason for the visit, leaving only my imagination to wildly speculate what was in store."
    scene pr1962 with dissolve
    mc "You're always here, huh?"
    scene pr1963 with dissolve
    jacob "Just me and Warren to guard the fort."
    scene pr1964 with dissolve
    jacob "--not that I can complain, they pay me a lot of money to sit my ass and read. It's the cushiest security detail I've worked by FAR."
    scene pr1965 with dissolve
    mc "What other kind of details have you worked?"
    scene pr1966 with dissolve
    jacob "After my contract with the FFL was up, I bounced around to the usual places. Bars, personal details, that kind of thing."
    if perk_socialChameleon == True or perk_socialButterfly == True:
         "I got the sense he was being tactfully vague, uninterested in going into details."
    scene pr1965 with dissolve
    mc "The FFL?"
    scene pr1966 with dissolve
    jacob "Légion étrangère - The {b}F{/b}rench {b}F{/b}oreign {b}L{/b}egion."
    scene pr1967 with dissolve
    mc "Really? That's so cool! How'd you end joining a foreign army?"
    scene pr1968 with dissolve
    jacob "Get me gassed one night and I'll tell you, deal?"
    mc "Yeah, sure. I'll hold you to that."
    scene pr1969 with dissolve
    jacob "Head on in. You're expected."
    "I still didn't know what I was here for."
    scene pr1970 with dissolve
    mc "Expected for what, exactly?"
    scene pr1971 with dissolve
    jacob "I don't know. They don't tell me. Maybe the usual, Eyes-Wide-Shut shit these rich people get up to?"
    scene pr1972 with dissolve
    mc "Riiiight, nice seeing you Jacob."
    stop music fadeout 2.0
    scene pr1973 with irisin
    "As soon as I entered, I spotted a pair of familiar faces sitting idly at the bar, appearing to be making small talk."
    "Once Rosalind caught sight of me, she offered an enthusiastic wave and a warm smile."
    "Veronica, for her part, gave me a simple nod."
    scene pr1974 with dissolve
    "Elsewhere, Mrs. Pulman stood by the bar, chatting with a fourth woman."
    play music "music/leaving-home.mp3"
    scene pr1975 with dissolve:
        subpixel True
        yalign 0.7
        xalign 0.6
        linear 3 yalign 0.1
    "It was clear, even from behind, that she was an attractive woman, younger than her conversational partner."
    "As my eyes lecherously wandered up the contours of her frame, a sense of familiarity came over me."
    mct "(Wait a minute, I know that ass...)"
    scene pr1976 with dissolve
    kat "There you are, Mr. [mcl]!"
    scene pr1977 with dissolve
    "..."
    scene pr1978 with dissolve
    fel "Oh! It's you!"
    fel "How you doin', stud?"
    scene pr1977 with dissolve
    "Felicia gave me a laid-back, casual greeting in stark contrast to my dumb-stricken surprise."
    mc "Oh, you're kidding me..."
    "After getting over the initial shock, considering our mutual connection to this place, I likely knew the answer to the question on my mind. Still, I asked it."
    mc "What are you doing here, Felicia?"
    scene pr1979 with dissolve
    fel "I'm competing in this summer thing Ian told me about. It sounded fun."
    scene pr1980 with fade
    rosever "..."
    scene pr1981 with dissolve
    kat "Oh? You two know each other already?"
    scene pr1982 with dissolve
    fel "Yeah, through Ian..."
    scene pr1983 with dissolve
    kat "That figures."
    scene pr1984 with dissolve
    mct "(Hold up... it sounded {i}fun{/}?!)"
    mct "(So she knew about the club the whole time?)"
    scene pr1985 with dissolve
    kat "I called you here to formally introduce you to this year's Carnations, but I guess you already know everyone here."
    scene pr1986 with dissolve
    kat "Mrs. Rosalind Carter."
    scene pr1987 with dissolve
    kat "Miss Veronica Lynch."
    scene pr1988 with dissolve
    $ history_felicia = "To my utter shock, my blind date turned out to be part of the Club's upcoming summer exhibition. I guess I'm getting my wish in seeing her again."
    $ unread_felicia = True
    play sound "sound effects/notification.wav"
    show bioupdate with dissolve
    kat "And finally, Mrs. Felicia Ford."
    scene pr1989 with dissolve
    kat "Girls, this is [mcf]. In two weeks, the summer exhibition will begin."
    kat "You've each been briefed on the schedule and what's expected of you."
    kat "You have any problems or concerns during the month-long event, it goes through him. He'll take care of you."
    scene pr1990 with dissolve
    kat "You have anything to add, [mcf]?"
    scene pr1991 with dissolve
    mc "..."
    "I like to think of myself as a good and decent person, but..."
    "I have simply never been given the opportunity to prove my conceited self-image right or wrong."
    mct "(Well, here's my chance.)"
    scene pr1992 with dissolve
    mc "Let's all get along."
    play sound "sound effects/sting-mumbaieffect.wav"
    stop music fadeout 3.0
    scene black with pixellate
    "......."
    "......"
    "..."
    jump june01start
