################################################################################
################################################################################
###                               PALE CARNATIONS                            ###
################################################################################
################################################################################

# Screens ----------------------------------------------------------------------

screen prDiscoCenter:

    imagemap:

        idle "gui/screens/imagemaps/prDiscoCenter_idle.png"
        hover "gui/screens/imagemaps/prDiscoCenter_hover.png"
        ground "gui/screens/imagemaps/prDiscoCenter_ground.png"

        hotspot (0,4,200,1500) action Jump("DiscoFreeRoamUpper")
        if discoMinaUpper == True:
            hotspot (225,160,200,1500) action Jump("discoMinaRailing")
        if discoFelUpper == True:
            hotspot (436,267,200,1500) action Jump("discoFelTable")
        hotspot (1353,6,800,1500) action Jump("DiscoFreeRoamBar")
        hotspot (611,231,750,200) action Jump("DiscoFreeRoamDance")
        if discoDanceMina or discoDanceGroup == True:
            hotspot (955,429,100,100) action Jump("discoDanceInspect")
        if discoMinaBathroom == True:
            hotspot (725,449,150,150) action Jump("prDiscoMinaHarass")

screen prDiscoBar:

    imagemap:

        idle "gui/screens/imagemaps/prDiscoBar_idle.png"
        hover "gui/screens/imagemaps/prDiscoBar_hover.png"
        ground "gui/screens/imagemaps/prDiscoBar_ground.png"



        hotspot (1252,214,350,1500) action Jump("discoKillianTalk")
        hotspot (921,194,350,1500) action Jump("discoBartenderTalk")
        hotspot (1,616,1000,1000) action Jump("DiscoFreeRoamCenter")


screen prDiscoUpper:

    imagemap:

        idle "gui/screens/imagemaps/prDiscoUpper_idle.png"
        hover "gui/screens/imagemaps/prDiscoUpper_hover.png"
        ground "gui/screens/imagemaps/prDiscoUpper_ground.png"

        if discoFelInvite == False:
            hotspot (825,364,100,200) action Jump("DiscoFreeRoamTable")
        if discoDanceMina == False and discoMinaLeft == False and discoDanceGroup == False and discoMinaBathroom == False:
            hotspot (927,263,350,700) action Jump("discoMinaTalk")
        hotspot (5,678,920,500) action Jump("DiscoFreeRoamCenter")

screen prDiscoTable:

    imagemap:

        idle "gui/screens/imagemaps/prDiscoTable_idle.png"
        hover "gui/screens/imagemaps/prDiscoTable_hover.png"
        ground "gui/screens/imagemaps/prDiscoTable_ground.png"

        if discoFelInvite == False:
            hotspot (1019,81,1000,1000) action Jump("discoFelTalk")
        hotspot (0,500,1000,1000) action Jump("DiscoFreeRoamUpper")

screen prDiscoDance:

    imagemap:

        idle "gui/screens/imagemaps/prDiscoDance_idle.png"
        hover "gui/screens/imagemaps/prDiscoDance_hover.png"
        ground "gui/screens/imagemaps/prDiscoDance_ground.png"

        if discoDanceMina == True or discoDanceGroup == True:
            hotspot (852,503,500,500) action Jump("discoDanceFun")
        hotspot (2, 472, 820, 800) action Jump("DiscoFreeRoamCenter")


# Labels -----------------------------------------------------------------------

label DiscoFreeRoamCenter:
    show black
    call screen prDiscoCenter

label DiscoFreeRoamUpper:
    show black
    call screen prDiscoUpper

label DiscoFreeRoamBar:
    show black
    call screen prDiscoBar

label DiscoFreeRoamDance:
    show black
    call screen prDiscoDance

label DiscoFreeRoamTable:
    show black
    call screen prDiscoTable

label discoMinaRailing:
    scene pr0253 with fade
    "I should go upstairs if I want to talk to Mina."
    call screen prDiscoCenter with fade

label discoFelTable:
    scene pr0339 with dissolve
    if drinkGet == True and drinkGot == False:
        "There's Felicia. I should get her a drink before returning to her."
    if drinkGot == True and drinkGot == True:
        "I should go upstairs and give her the cocktail."
    if drinkGet == False and drinkGot == False:
        "Maybe I should see if she wants anything?"

    call screen prDiscoCenter

label discoKillianTalk:
    if discoKillianWarning == False:
        $ discoKillianWarning = True
        show black
        scene pr0329 with fade
        show screen textbox2 with dissolve
        mc "Dude, your girlfriend is not pleased."
        scene pr0330 with dissolve
        kil "Tell me something I don't already know."
        scene pr0329 with dissolve
        mc "You're going to act innocent?"
        scene pr0330 with dissolve
        kil "No, but I actually enjoy making her squirm a little when we go out."
        kil "She tries that much harder in bed afterwards, if you know what I'm saying."
        mct "(...)"
        hide screen textbox2 with dissolve
        menu:
            "I don't get you. [red]\[Toughness -1\]":
                $ toughness -= 1
                $ toughness = clamp(toughness, 0, 30)
                scene pr0331 with dissolve
                show screen textbox2 with dissolve
                mc "Mina's a nice girl and she's very attractive. I don't get why you'd risk messing that up."
                scene pr0333 with dissolve
                kil "Pssh, girls are a dime a dozen, man. You don't get it because you don't come from a wealthy family like I do, but they all just want one of two things."
                kil "Access to the purse strings or the good time that it can make happen."
                scene pr0329 with dissolve
                mc "..."
            "You're an asshole. [red]\[Toughness -2\] \[Killian -3\]":
                $ toughness -= 2
                $ toughness = clamp(toughness, 0, 30)
                $ Killian_Bromance -= 3
                $ Killian_Bromance = clamp(Killian_Bromance, 0, 40)
                scene pr0331 with dissolve
                show screen textbox2 with dissolve
                mc "Dude, what the hell is wrong with you? Mina's a nice girl."
                scene pr0333 with dissolve
                kil "Whatever. Girls come and go, and they're never as nice as they seem. You don't get it because you don't come from a wealthy family like I do, but they all just want one of two things."
                kil "Access to the purse strings or the good time that can make happen."
                scene pr0329 with dissolve
                mc "..."
            "Good plan. [gr]\[Toughness +2\] \[Killian +2\]":
                $ toughness += 2
                $ toughness = clamp(toughness, 0, 30)
                $ Killian_Bromance += 2
                $ Killian_Bromance = clamp(Killian_Bromance, 0, 40)
                scene pr0331 with dissolve
                show screen textbox2 with dissolve
                mc "You're a devious fucker, you know that?"
                scene pr0332 with dissolve
                kil "I'm surprised you're not lecturing me about it."
                scene pr0329 with dissolve
                mc "Even I find it a drag to act like a wet blanket all the time I guess."

        scene pr0332 with dissolve
        kil "Anyway, I'm going stay down here and let her stew a little. Talk to you later?"
        call screen prDiscoBar with fade

    if discoMinaConsole == True and discoMinaBathroom == True:
        jump prDiscoMinaHarassDouble

    if discoKillianWarning == True:
        show black
        scene pr0330 with fade
        kil "What are you sticking around for?"
        kil "Go let loose a little, I'll catch up with you later."
        call screen prDiscoBar with fade


label discoMinaTalk:
    if discoMinaConsole == False and drinkGot == False:
        scene pr0340 with fade
        mc "Hey Min--"
        scene pr0341 with dissolve
        mina "He always does this!"
        scene pr0352 with blinds
        mina "Grrr...!"
        scene pr0342 with dissolve
        mina "Sorry, [mcf]. Could you give me a minute please?"
        call screen prDiscoUpper with fade

    if discoMinaConsole == False and drinkGot == True:
        scene pr0341 with fade
        mina "Tsk!"
        scene pr0353 with blinds
        mina "Is... he... serious?!"
        scene pr0343 with dissolve
        mina "TWO GIRLS NOW?!"
        mc "(I should take Felicia her drink...)"
        call screen prDiscoUpper with fade

    if discoMinaConsole == True:
        scene pr0344 with fade
        mc "Hey Mi--"
        scene pr0345 with dissolve
        mina "You. Me. Dance floor!"
        mina "I need to let off some steam."
        scene pr0346 with dissolve
        mina "{size=-10}...and show that bastard I can play too.{/size=-10}"
        scene pr0347 with dissolve
        mct "(Subtle...)"
        hide screen textbox2 with dissolve

        menu:
            "Yeah, why not? [gr]\[DanceMina\]":
                $ discoDanceMina = True
                $ discoMinaUpper = False
                show screen textbox2 with dissolve

                mc "Err... sure, why not..."
                scene pr0348 with dissolve
                mina "Good, I'll meet you down there. Don't dally!"
                call screen prDiscoUpper with fade

            "Sure, but let me invite Felicia first. [gr]\[DanceGroup\]":
                $ discoDanceGroup = True
                $ discoMinaUpper = False
                show screen textbox2 with dissolve
                mc "Sure, but we should invite Felicia."
                scene pr0348 with dissolve
                mina "Good idea, the more the merrier."
                mina "You go get her and I'll meet you two on the dance floor."
                call screen prDiscoUpper with fade



label discoFelTalk:

    if discoDanceMina == True and discoFelInvite == False and drinkGet == True and drinkGot == True:

        if drinkGood == True:
            scene pr0372 with dissolve
        if drinkNeutral == True:
            scene pr0368 with dissolve
        if drinkBad == True:
            scene pr0359 with dissolve
        mc "Sorry, she wants to dance. I'll be right back, alright?"

        if drinkGood == True:
            scene pr0369 with dissolve
        if drinkNeutral == True:
            scene pr0367 with dissolve
        if drinkBad == True:
            scene pr0362 with dissolve

        fel "Let her have it, tiger."
        call screen prDiscoTable with fade



    if discoDanceGroup == True and discoFelInvite == False and drinkGet == True and drinkGot == True:
        $ discoFelInvite = True

        if drinkGood == True:
            scene pr0372 with dissolve
        if drinkNeutral == True:
            scene pr0368 with dissolve
        if drinkBad == True:
            scene pr0359 with dissolve

        mc "Care to come dance with Mina and I?"

        if drinkGood == True:
            scene pr0369 with dissolve
        if drinkNeutral == True:
            scene pr0367 with dissolve
        if drinkBad == True:
            scene pr0362 with dissolve

        fel "Heh, {i}gladly{/i}."

        $ discoFelUpper = False
        call screen prDiscoTable with fade

    if drinkGet == False:
        scene pr0354 with dissolve
        fel "Would you mind getting me something to drink on your way back?"
        scene pr0355 with dissolve
        mc "Sure, what would you like?"
        scene pr0356 with dissolve
        fel "Hmm... something fruity."
        fel "Surprise me."
        scene pr0355 with dissolve
        mc "Something fruity coming up."
        $ drinkGet = True
        call screen prDiscoTable with fade

    if drinkGet == True and drinkGot == False:
        scene pr0354 with dissolve
        fel "Where's my drink, cutie?"
        fel "Remember, get me something fruity."
        call screen prDiscoTable with fade


    if drinkGet == True and drinkGot == True and discoMinaConsole == False:

        if drinkGood == True:
            $ Felicia_Affection +=1
            $ Felicia_Affection = clamp(Felicia_Affection, 0, 40)
            scene pr0357 with dissolve
            mc "Here you go."
            fel "Thank you, [mcf]."
            scene pr0369 with dissolve
            fel "How's Mina doing? Working herself into a tizzy?"
            scene pr0372 with dissolve
            mc "She told me to go away."
            scene pr0369 with dissolve
            fel "She's yet to work up the nerve to really let him have it."
            scene pr0372 with dissolve
            mc "This is normal for them?"
            scene pr0371 with dissolve
            fel "Sadly. Well, what can you do?"
            scene pr0370 with dissolve
            fel "Why don't you sit down and we can continue to get to know each other?"
            hide screen textbox2 with dissolve
        if drinkNeutral == True:
            scene pr0358 with dissolve
            mc "Here you go."
            fel "Thank you, [mcf]."
            scene pr0367 with dissolve
            fel "How's Mina doing? Working herself into a tizzy?"
            scene pr0368 with dissolve
            mc "She told me to go away."
            scene pr0367 with dissolve
            fel "She's yet to work up the nerve to really let him have it."
            scene pr0368 with dissolve
            mc "This is normal for them?"
            scene pr0365 with dissolve
            fel "Sadly. Well, what can you do?"
            scene pr0366 with dissolve
            fel "Why don't you sit down and we can continue to get to know each other?"
            hide screen textbox2 with dissolve
        if drinkBad == True:
            $ Felicia_Affection -=1
            $ Felicia_Affection = clamp(Felicia_Affection, 0, 40)
            scene pr0359 with dissolve
            mc "Here you go."
            fel "Thank you, [mcf]."
            scene pr0362 with dissolve
            fel "How's Mina doing? Working herself into a tizzy?"
            scene pr0361 with dissolve
            mc "She told me to go away."
            scene pr0362 with dissolve
            fel "She's yet to work up the nerve to really let him have it."
            scene pr0361 with dissolve
            mc "This is normal for them?"
            scene pr0364 with dissolve
            fel "Sadly. Well, what can you do?"
            scene pr0363 with dissolve
            fel "Why don't you sit down and we can continue to get to know each other?"
            hide screen textbox2 with dissolve

        menu:
            "I can't see the harm in that.":
                show screen textbox2 with dissolve
                jump prDiscofeliciaChatter
            "I think I'm going to check on Mina again. [gr]\[MinaConsole\]":
                $ discoMinaConsole = True
                show screen textbox2 with dissolve
                if drinkGood == True:
                    scene pr0372 with dissolve
                if drinkNeutral == True:
                    scene pr0368 with dissolve
                if drinkBad == True:
                    scene pr0361 with dissolve
                mc "That sounds nice, but I think I'm going to see if Mina wants to join us first."

                if drinkGood == True:
                    scene pr0369 with dissolve
                if drinkNeutral == True:
                    scene pr0367 with dissolve
                if drinkBad == True:
                    scene pr0362 with dissolve

                fel "Okay, but I'm telling you, it's a vicious cycle. One I doubt you'll have a remedy for."
                call screen prDiscoTable with fade

    if drinkGet == True and drinkGot == True and discoMinaConsole == True and discoMinaBathroom == True:
        scene pr0495 with dissolve
        fel "You should hurry and get down there, that walking steroid looks like he's getting irritated."
        call screen prDiscoTable with fade

    if drinkGet == True and drinkGot == True and discoMinaConsole == True:
        scene pr0354 with dissolve
        fel "She's starting to look like a sad puppy dog over there. You should try and convince her to come join us."
        call screen prDiscoTable with fade



label discoBartenderTalk:
    if drinkGot == False and drinkGet == True:
        scene black
        scene pr0334 with fade
        bart "What can I get you, sir?"
        hide screen textbox2 with dissolve
        scene pr0335 with dissolve
        menu:
            "A dry martini":
                $ drinkBad = True
                $ drinkGot = True
                show screen textbox2 with dissolve
                scene pr0334 with dissolve
                bart "One martini, dry coming right up."
                scene black with fade
                mct "(Hope this is what Felicia wanted.)"
                scene pr0337 with dissolve
                bart "Here you go"



            "[gr]A cherry bomb":
                $ drinkGood = True
                $ drinkGot = True
                show screen textbox2 with dissolve
                scene pr0334 with dissolve
                bart "One cherry bomb, coming right up."
                scene black with fade
                mct "(Hope this is what Felicia wanted.)"
                scene pr0336 with dissolve
                bart "Here you go"


            "A tequila sunrise":
                $ drinkNeutral = True
                $ drinkGot = True
                show screen textbox2 with dissolve
                scene pr0334
                bar "A Tequila sunrise, coming right up."
                scene black with fade
                mct "(Hope this is what Felicia wanted.)"
                scene pr0338 with dissolve
                bart "Here you go"

        bart "Can I get you anything else, sir?"
        mc "No, that's it. Thank you."
        call screen prDiscoBar with fade

    if drinkGot == True:
        show black
        scene pr0334 with fade
        bart "Can I get you anything, sir?"
        scene pr0335
        mc "No, thank you."
        call screen prDiscoBar with fade

    if drinkGet == False and drinkGot == False:
        show black
        scene pr0334 with fade
        bart "Can I get you anything, sir?"
        scene pr0335
        mc "No, thank you."
        call screen prDiscoBar with fade

label discoDanceInspect:
    if discoDanceMina == True:
        scene pr0494 with fade
        "There she is. I should get to the dance floor."
        call screen prDiscoCenter with fade
    if discoDanceGroup == True and discoFelInvite == True:
        scene pr0494 with fade
        "Felicia and I should go to the dance floor."
        call screen prDiscoCenter with fade
    if discoDanceGroup == True and discoFelInvite == False:
        scene pr0494 with fade
        "I told Mina I'd invite Felicia to dance with us. Best go ask her.."
        call screen prDiscoCenter with fade

label discoDanceFun:
    play music "music/organic.mp3"
    if discoDanceMina == True:
        scene pr0441 with fade
        mina "Why are you so far away? I don't bite."
        scene pr0442 with dissolve
        mina "There! This is nice, yeah?"
        mina "Put your hands on my hips!"
        scene pr0443 with dissolve
        mc "I'm not so sure if--"
        mina "Don't worry about my jerk boyfriend! We're just having a good time! He won't mind!"
        scene pr0444 with dissolve
        mina "Hey [mcf]... Can I ask you a question?"
        mc "Sure!"
        scene pr0446 with dissolve
        mina "Does Ian ever talk about me?"
        mct "(Quite frankly, the answer to that is never, but I'm not sure if I should let her know that.)"
        hide screen textbox2 with dissolve
        menu:
            "Tell her the truth. [gr]\[Mina +1\] \[MinaKillian -1\] [red]\[Killian -1\]":
                $ Mina_Affection +=1
                $ Mina_Affection = clamp(Mina_Affection, 0, 40)
                $ Killian_Bromance -= 1
                $ Killian_Bromance = clamp(Killian_Bromance, 0, 40)
                $ Mina_KLove -= 1
                $ Mina_KLove = clamp(Mina_KLove, 0, 10)
                show screen textbox2 with dissolve
                mc "The truth? Not often!"
                scene pr0445 with dissolve
                mina "Oh..."
                mc "...but you know how Ian is! He's not very good at interpersonal things! He rarely talks about anyone!"
                scene pr0446 with dissolve
                mina "That's not true! He talks about you ALL the time!"
                mina "I swear, if I didn't have such intimate evidence that he's straight as an arrow, I'd be worried he was in love with you!"



            "Cover for your best friend. [gr]\[Killian +2\] [red]\[MinaKillian +1\]":
                $ Killian_Bromance += 2
                $ Killian_Bromance = clamp(Killian_Bromance, 0, 40)
                $ Mina_KLove += 1
                $ Mina_KLove = clamp(Mina_KLove, 0, 10)
                show screen textbox2 with dissolve
                mc "Yeah! All the time!"
                scene pr0447 with dissolve
                mina "Really?"
                scene pr0448 with dissolve
                mc "Absolutely! Why wouldn't he? You're a stunning woman!"
                mc "He doesn't go in for the girlfriend thing usually! That should tell you something about how he feels about you!"

        scene pr0449 with dissolve
        mina "What about you? Do you have a girlfriend?"
        scene pr0450 with dissolve
        mc "Me? No!"
        scene pr0451 with dissolve
        mina "Why not? That's such a waste! You're a good looking man!"
        scene pr0452 with dissolve
        mina "I have a friend I could set you up with -- {b}oh!{/b} Felicia!"
        mina "We totally ditched her like a bunch of assholes! We should head back up to her!"

        scene black with fade
        stop music fadeout 3.0
        "We made our way back upstairs and rejoined Felicia and Killian, who Mina was quick to forgive."

        $ discoDanceMina = False
        $ discoDanceGroup = False
        $ discoMinaBathroom = True
        $ discoFelUpper = True
        jump prDiscoGroupTalk

    if discoDanceGroup == True:

        scene pr0466 with fade
        mina "What are you doing way over there?"
        fel "Yeah, get over here!"
        scene pr0467 with dissolve
        mina "Tell me a little about yourself! Do you have a girlfriend, [mcf]?"
        mc "Nope, extremely single!"
        mina "Really? That's weird! You're a good looking man!"
        fel "It's not that weird! He's young! They'll be plenty of time to be tied down later!"
        scene pr0468 with dissolve
        mina "Geez! Don't you think that's a bit much, Felicia? You guys look like you're practically... you know."
        fel "Hahaha, you're so adorable you know that? It's just a bit of harmless dancing! See?"
        scene pr0469 with dissolve
        "......"
        "..."
        fel "Again? Get over here!"
        scene pr0470 with dissolve
        "..."
        scene pr0471 with dissolve
        mc "Hey! Nice of you to join us again!"
        kil "Hey yourself! I think I had a dream about this last week!"
        scene pr0472 with dissolve
        fel "You know, you're not like Killian's other friends!"
        mc "Is that a pick up line?"
        fel "No! I'm serious! You haven't tried to feel me up yet!"
        mc "Eh... huh?"
        fel "Seriously! Go ahead and do it! I insist!"
        scene pr0473 with dissolve
        kil "Great! You guys are already friends!"
        scene pr0474 with dissolve
        mina "...ngh~ah..."
        kil "Why don't we take it back upstairs? What do you say?"
        scene black with fade
        "......"
        stop music fadeout 3.0
        "..."

        $ discoFelUpper = True
        $ discoFelInvite = False
        $ discoDanceMina = False
        $ discoDanceGroup = False
        $ discoMinaBathroom = True
        jump prDiscoGroupTalk

label prDiscoGroupTalk:

    play music "music/edm-detection-mode.mp3"
    scene pr0454 with blinds
    "The night continued in good spirits."
    scene pr0455 with fade
    "...and {i}with{/i} good spirits."
    scene pr0456 with fade
    fel "Bottoms up, cutie."
    mina "No more! No more! I get mean after four."
    scene pr0533 with fade
    mc "Oh shit! That is you, from the soap commercial."
    mc "I'd never met a famous person before!"
    mina "Stop it! It's nothing special, just a commercial that gets regional play."
    scene pr0533 with fade
    mina "What was Ian like as a kid, [mcf]?"
    mc "He was afraid of his own shadow!"
    mina "What?! Really?!"
    mina "I can't even picture that!"
    "We ended up burning an hour, just shooting the shit."
    scene pr0457 with fade
    mina "Excuse me a minute, I need to visit the ladies room."
    scene pr0458 with fade
    mina "Don't. Run. Off. Again!"
    scene pr0459
    fel "You two make such a cute couple."
    mc "I agree."
    scene pr0460
    kil "Well, we are both pretty hot I suppose."
    scene pr0461
    fel "There's more to it than that."
    mc "That was absolutely not conceited in the least, Ian."
    kil "Hey! You know very well that my humbleness is just one of the many positive character traits that got me elected Mr. Congeniality for our highschool superlatives."
    scene pr0462 with dissolve
    kil "Anyway, next round of drinks is on me!"
    scene pr0463 with dissolve
    kil "...don't give me that look. I'm coming back this time, I swear!"
    scene pr0385 with fade
    fel "Looks like it's just the two of us..."
    scene pr0384
    "..."
    scene pr0386 with dissolve
    "Fwup."
    scene pr0385 with dissolve
    fel "That {b}was{/b} nice, right?"
    mina "{size=-15}...hands off, you jerk!{/size=-15}"
    scene pr0464 with dissolve
    mct "(Huh? That's Mina...)"
    fel "That guy doesn't look like he's taking no for an answer."
    mc "No, he doesn't..."
    scene pr0465 with dissolve
    mc "I'll be right back!"
    scene black with dissolve
    stop music fadeout 3.0
    "The way I look at it, I've got two options: either confront that meathead down there alone or (hopefully) find Ian at the bar for backup."
    play music "music/organic.mp3"
    call screen prDiscoTable with fade


label prDiscoMinaHarass:
    scene pr0496 with fade
    mc "There they are, but maybe I should get Killian first?"
    hide screen textbox2 with dissolve
    menu:

        "Help Mina.":
            show screen textbox2 with dissolve
            jump prDiscoMinaHarassSolo
        "This guy looks tough, get Ian as backup.":
            call screen prDiscoCenter with fade

label prDiscoMinaHarassSolo:
    "There's no time to look for Ian."
    scene pr0475 with dissolve
    mina "Don't you know what the word \"no\" means?!"
    asshole "Babe, this you're idea of playing hard to get?"
    mina "I'm {b}not{/b} your babe!"
    scene pr0476 with dissolve
    mc "Is there a problem, Mina?"
    scene pr0477 with dissolve
    mina "[mcf]! Will you tell this jerk I'm not interested? He's drunk and won't take a hint!"
    scene pr0478 with dissolve
    asshole "Don't tell me this limp wrist is your boyfriend?"
    hide screen textbox2 with dissolve
    scene pr0479 with dissolve
    menu:

        "Come at him from a friendly angle. [red]\[Toughness -1\]":
            $ toughness -= 1
            $ toughness = clamp(toughness, 0, 30)
            show screen textbox2 with dissolve
            scene pr0480 with dissolve
            mc "The lady isn't interested, but why don't you let me buy you a drink instead?"
            scene pr0481 with dissolve
            asshole "How about you fuck off, we're just having a nice conversation."

        "Tell him stove off. [gr]\[Toughness +1\]":
            $ toughness += 1
            $ toughness = clamp(toughness, 0, 30)
            show screen textbox2 with dissolve
            scene pr0480 with dissolve
            mc "The lady isn't interested, so {b}shove off{/b}, jack ass."
            scene pr0481 with dissolve
            asshole "Why don't you fuck off before I knock you on your ass?"
    hide screen textbox2 with dissolve
    scene pr0482 with dissolve
    menu prDiscoHarassChoice:
        "{color=#FF1493}\[Strongman]{/color} Try to intimidate him. [gr]\[Toughness +2\] \[Mina +2\] \[MinaKillian -1\] \[Killian +1\]" if perk_strongman == True:
            $ toughness += 2
            $ toughness = clamp(toughness, 0, 30)
            $ Mina_Affection += 2
            $ Mina_Affection = clamp(Mina_Affection, 0, 40)
            $ Mina_KLove -= 1
            $ Mina_KLove = clamp(Mina_KLove, 0, 10)
            $ Killian_Bromance += 1
            $ Killian_Bromance = clamp(Killian_Bromance, 0, 40)
            show screen textbox2 with dissolve
            scene pr0483 with dissolve
            "This kind of prick will only understand it in his own language."
            mc "Let go of her or I'm going to kick your shit in."
            scene pr0484 with dissolve
            asshole "You? I'd like to see you try!"
            play sound "sound effects/punch.wav"
            scene pr0485 with dissolve
            mina "Oh my god!"
            scene pr0486 with dissolve
            asshole "Fuck my ha--"
            play sound "sound effects/punch.wav"
            scene pr0487 with dissolve
            asshole "Gah!"
            scene pr0497 with dissolve
            "..."
            scene pr0493 with dissolve
            mc "We should go"
            mina "R-right."
            scene pr0498 with fade
            mina "Holy shit! He just attacked you!"
            scene pr0499 with dissolve
            mina "Thanks for sticking up for me, [mcf]!"
            scene pr0501 with dissolve
            fel "You okay, sweetie? We saw the whole thing."
            kil "Thanks for looking out for Mina, man."
            kil "I had just gotten back when I saw that guy try to sucker punch you. I was gonna rush down there to help, but you took care of things before I could."
            scene pr0502 with dissolve
            fel "That was so hot you know."
            scene pr0503 with dissolve
            kil "Why don't you say we get out of here just in case the cops get involved."
            fel "Good idea."
            kil "Let's go back to my place"
            jump prAfterParty


        "Well, you tried: sucker punch this prick. [gr]\[Toughness +3\] \[Killian +2\] [red]\[Mina -1\]":
            $ toughness += 3
            $ toughness = clamp(toughness, 0, 30)
            $ Mina_Affection -= 1
            $ Mina_Affection = clamp(Mina_Affection, 0, 40)
            $ Killian_Bromance += 2
            $ Killian_Bromance = clamp(Killian_Bromance, 0, 40)
            show screen textbox2 with dissolve
            scene pr0483 with dissolve
            "There's something I learned as a kid."
            scene pr0484 with dissolve
            asshole "What do you think you're--!"
            scene pr0488 with dissolve
            play sound "sound effects/punch.wav"
            asshole "Gaah!"
            scene pr0489 with dissolve
            asshole "My nose! You broke my nose!"
            mina "Oh my god!"
            "The best way to come at a bully is hard and fast and to make it {b}bloody{/b}."
            "People unaccustomed to the sight of their own blood tend to lose their nerve quick when they start gushing it from their nose."
            scene pr0493 with dissolve
            mc "We should go"
            mina "R-right."
            scene pr0498 with fade
            mina "Holy shit! You -- you just... hit that guy!"
            mc "Sorry you had to see that. I hope I didn't upset you."
            scene pr0500 with dissolve
            mina "No! Uh, thank you..."
            scene pr0501 with dissolve
            fel "You okay, sweetie? We saw the whole thing."
            kil "Thanks for looking out for Mina, man."
            kil "I had just gotten back with the drinks when I saw you lay the guy out from up here. Good fucking shit!"
            scene pr0502 with dissolve
            fel "That was so hot you know."
            scene pr0503 with dissolve
            kil "Why don't you say we get out of here in case that asshole wants to get the cops involved."
            fel "Good idea."
            kil "Let's go back to my place."
            jump prAfterParty


        "Stand up for Mina. [gr]\[Mina +2\] \[Killian +1\] [red]\[Toughness -2\] \[Felicia -1\]":
            $ Mina_Affection += 2
            $ Mina_Affection = clamp(Mina_Affection, 0, 40)
            $ toughness -= 2
            $ toughness = clamp(toughness, 0, 30)
            $ Felicia_Affection -= 1
            $ Felicia_Affection = clamp(Felicia_Affection, 0, 40)
            $ Killian_Bromance += 1
            $ Killian_Bromance = clamp(Killian_Bromance, 0, 40)
            show screen textbox2 with dissolve
            "This guy is drunk, belligerent as all hell, and twice my size... but it's not like I've got a choice here."
            scene pr0490 with dissolve
            mc "I'll fuck off once you leave her alone."
            asshole "Oh, yeah? What are you going to do about it?"
            scene pr0491 with dissolve
            "It all happened in a flash. That asshole shoved Mina out of the way, and while my attention was on her..."
            scene pr0492 with flash
            play sound "sound effects/punch.wav"
            "{b}*THWAP!*{/b}."
            scene black with pixellate
            "Lights out."
            jump prDiscoClocked

        "{color=#696969}\[Strongman] Try to intimidate him.{/color}" if perk_socialButterfly == True or perk_socialChameleon == True:
            jump prDiscoHarassChoice


label prDiscoClocked:
    "......"
    "..."
    mc "Ngh..."
    "A pleasant, womanly scent and a soft warm touch..."
    scene pr0514 with dissolve
    mc "Ugh..."
    scene pr0515 with dissolve
    "Not a bad way to come to."
    scene pr0516 with dissolve
    "I awoke to my friends looking down on me on the dance floor, being delicately cradled in Mina's lap."
    scene pr0517 with dissolve
    mina "Oh! You're coming too. I'm so glad!"
    scene pr0518 with dissolve
    mc "...the guy clocked me?"
    scene pr0519 with dissolve
    kil "If I were you, I'd sell it more as 'your face defended Mina's honor at great cost to itself.' You'll come out of the story sounding a {i}little{/i} less like a bitch."
    scene pr0520
    kil "But uh... thanks for looking out, bro. That was probably my punch to eat."
    scene pr0518 with dissolve
    mc "What happened to the blockhead?"
    scene pr0521 with dissolve
    fel "He got the fuck out of there, quick. Guess he didn't want to risk waiting around for the cops."
    show pr0518 with vpunch
    mc "Cops?!"
    scene pr0519 with dissolve
    kil "Relax! I paid off the bouncer to not call anyone - cop or ambulance."
    scene pr0518 with dissolve
    mc "Good... I couldn't afford a trip to the hospital."
    scene pr0522 with dissolve
    mina "How's your head?"
    scene pr0518 with dissolve
    mc "I feel like I got run over by a truck."
    scene pr0522 with dissolve
    mina "I'm so, {b}so{/b} sorry you got dragged into that."
    hide screen textbox2 with dissolve
    menu:
        "Deflect her concern.":
            show screen textbox2 with dissolve
            mc "Don't be. I can cross 'getting into a bar fight' off my bucket list."

        "Let her know it's cool. [gr]\[Mina +1\]":
            $ Mina_Affection += 1
            $ Mina_Affection = clamp(Mina_Affection, 0, 40)
            show screen textbox2 with dissolve
            mc "It's not your fault that guy was being an asshole."

    mc "I'm getting up now, okay?"
    scene pr0523 with fade
    "Ugh... head rush."
    scene pr0524 with dissolve
    fel "You sure you shouldn't go to the hospital? You got knocked out..."
    scene pr0525 with dissolve
    kil "Hell yeah, he's sure. My boy ain't going to let a little thing like getting floored by an asshole twice his size ruin the night's fun. Are you?"
    scene pr0526 with dissolve
    mc "...there's more?"
    kil "Let's get out of here and head back to my place."
    hide screen textbox2 with dissolve
    show screen textbox2 with dissolve
    scene pr0527 with dissolve
    mc "Alright, let's go back to your place."
    mina "Yaaay!"
    scene pr0532 with dissolve
    fel "We're going to have {i}a lot{/i} of fun, I promise."
    "......"
    scene black with dissolve
    "..."
    jump prAfterParty

label prDiscoMinaHarassDouble:
    $ toughness -= 1
    $ toughness = clamp(toughness, 0, 30)
    $ Killian_Bromance += 2
    $ Killian_Bromance = clamp(Killian_Bromance, 0, 40)
    $ Mina_KLove += 1
    $ Mina_KLove = clamp(Mina_KLove, 0, 10)

    scene pr0504 with fade
    kil "[mcf], What's uh--"
    scene pr0505 with dissolve
    mc "No time. Some major musclehead is being all pushy and handsy with Mina."
    kil "Shit, lead the way."
    scene pr0506 with dissolve
    kil "How big are we talking about?"
    scene pr0507 with dissolve
    mc "Magilla Gorilla big."
    kil "...what?"
    mc "It's a old... never, nevermind, he's {b}big!{/b}"
    kil "Shit. Get his attention when we roll up, okay?"
    mc "Uh... okay?"
    scene pr0508 with dissolve
    mina "Let go of me, you creep!"
    scene pr0509 with dissolve
    mina "[mcf]! Thank god!"
    scene pr0510 with dissolve
    hide screen textbox2 with dissolve
    menu:
        "Let go of the girl, she's not interested.":
            show screen textbox2 with dissolve
            scene pr0511 with dissolve
            mc "Hey! Let go of the girl! Can't you see she's not interested?"
            asshole "Huh? Who are you--"
            play sound "sound effects/breaking-glass.wav"
            scene pr0512 with flash

        "Hey, asshat!":
            show screen textbox2 with dissolve
            scene pr0511 with dissolve
            mc "Hey, asshat! Go find someone pathetic enough to buy what you're limpdick is selling!. "
            mc "The girl isn't interested!"
            asshole "What did--"
            play sound "sound effects/breaking-glass.wav"
            scene pr0512 with flash

    mina "Eeeh!"
    scene pr0513 with dissolve
    mina "H-holy shit!"
    kil "You okay?"
    mina "Y-yeah. Y-you just...!"
    kil "That guy would kick my ass 10 out of 10 times. What else could I do?"
    mina "Not that!"
    kil "What's done is done. We should get Felicia and get out of here, quick."
    jump prAfterParty

label prDiscofeliciaChatter:
    scene black with fade
    "..."
    scene pr0373 with fade
    fel "So, what do you study?"
    scene pr0374 with dissolve
    mc "I'm pre-med, so a bit of everything at the moment."
    scene pr0375 with dissolve
    fel "Oh? You want to be a doctor?"
    scene pr0374 with dissolve
    mc "It's the one thing in life I'm clear on."
    scene pr0376 with dissolve
    fel "What makes you want to be one? Is it the money?"
    scene pr0378 with dissolve
    if id_greed == True:
        mc "It's a decent part of it, I'm not going to lie."
    if id_power == True:
        mc "No, it's more... I like the idea of people putting their faith in me."
    if id_lust == True:
        mc "I just want to help people."

    mc "But there's also my father."
    scene pr0373 with dissolve
    fel "Is he a doctor?"
    scene pr0374 with dissolve
    mc "No, he died when I was a young boy. An accident."
    scene pr0377 with dissolve
    fel "I'm sorry, I--"
    scene pr0378 with dissolve
    mc "Don't be, I bring it up because I admire the trauma doctor that saw him through his last moments. She did her best for him."
    scene pr0379 with dissolve
    fel "..."
    scene pr0380 with dissolve
    fel "I'm a little jealous of people who know what they want."
    scene pr0379 with dissolve
    mc "..."
    fel "..."
    hide screen textbox2 with dissolve
    menu:
        "Suggest we do shots. [gr]\[Felicia +2\]":
            $ Felicia_Affection += 2
            $ Felicia_Affection = clamp(Felicia_Affection, 0, 40)
            scene pr0378 with dissolve
            show screen textbox2 with dissolve
            mc "Want to go do some shots?"
            scene pr0375 with dissolve
            fel "You want to get me drunk? Let's do it."
            jump prDiscofeliciaFun

        "Excuse yourself and check up on Mina. [gr]\[MinaConsole\]":
            $ discoMinaConsole = True
            scene pr0378 with dissolve
            show screen textbox2 with dissolve
            mc "I'm going to go see if Mina wants to join us."
            scene pr0375 with dissolve
            fel "Good idea."
            call screen prDiscoTable with fade


label prDiscofeliciaFun:

    scene pr0387 with blinds
    mc "Bottoms up."
    scene pr0360 with irisout
    "..."
    scene pr0381 with dissolve
    "I don't normally drink like this, in fact I'd even say I hate it, but what spurred me to knock back shot after shot should be fairly obvious."
    scene pr0382 with dissolve
    fel "Never?"
    fel "You've never done a body shot before?"
    scene pr0383 with dissolve
    "I am a man after all, all it takes is the right woman to grab and lead me by the dick to influence me to do any number of uncharacteristic things. "
    scene pr0385 with dissolve
    fel "Y'know, you're pretty cute when I'm buzzed."
    scene pr0386 with fade
    "*{b}Chup.{/b}*"
    scene pr0384 with dissolve
    fel "..."
    scene pr0384 with dissolve
    fel "Let's go dance."
    scene pr0388 with dissolve
    fel "You forfeited your right to say no when you got me lubed up!"
    scene black with fade
    "..."
    stop music fadeout 3.0
    scene pr0389 with blinds
    play music "music/organic.mp3"
    fel "WHAT ARE YOU DOING?"
    scene pr0390 with dissolve
    fel "DON'T BE A PUSSY, HOLD ME CLOSE!"
    scene pr0391 with dissolve
    fel "YOUR LITTLE FRIEND SEEMS TO HAVE MADE AN APPEARANCE!"
    fel "GLAD TO SEE ALL THE BOOZE HASN'T DAMPENED YOUR ENTHUSIASM!"
    hide screen textbox2 with dissolve
    menu:
        "I'll show her enthusiasm.":
            show screen textbox2 with dissolve
            mct "(Fortune favors the bold, right?)"
            scene pr0392 with dissolve
            fel "THAT'S THE SPIRIT!"
            hide screen textbox2 with dissolve
            jump prDiscofeliciaGrope1

        "Be respectful.":
            show screen textbox2 with dissolve
            fel "WHAT THE HELL ARE YOU DOING? GRAB MY HIPS LIKE YOU MEAN IT!"
            mc "UH, OKAY?"
            scene pr0392 with dissolve
            fel "THAT'S MORE LIKE IT!"
            hide screen textbox2 with dissolve
            jump prDiscofeliciaGrope1

    menu prDiscofeliciaGrope1:
            "Grope her tits. [gr]\[FeltTits\]":
                $ prDiscoFelTit = True
                scene pr0393 with dissolve
                show screen textbox2 with dissolve
                fel "Mmh...♥"
                fel "You like my tits?"
                hide screen textbox2 with dissolve
                jump prDiscofeliciaGrope2

            "Keep grinding.":
                show screen textbox2 with dissolve
                scene pr0396 with dissolve
                "As time passed, our dancing quickly fell out of tempo with the music and into a more pulse-like, need-driven pace."
                mct "(...shit! If I let her keep this up, I might just pop her on the dance floor.)"
                mct "(Time to make things more interesting...)"
                hide screen textbox2 with dissolve
                jump prDiscofeliciaGrope2

    menu prDiscofeliciaGrope2:

        "Neck her.":
            scene pr0394 with dissolve
            show screen textbox2 with dissolve
            fel "{b}Aawh~♥!{/i}"
            scene pr0402 with fade
            fel "You really know how to get a girl worked up. Why don't we find some place a little more private?"
            scene pr0403 with dissolve
            "..."
            jump prDiscoFeliciaBathroomSexStart

        "Grope her tits harder." if prDiscoFelTit == True:
            show screen textbox2 with dissolve
            scene pr0395 with dissolve
            fel "{b}Oh!{/i}"
            fel "I'll take that as a yes."
            scene pr0402 with blinds
            fel "You really know how to get a girl worked up. Why don't we find some place a little more private?"
            scene pr0403 with dissolve
            "..."
            jump prDiscoFeliciaBathroomSexStart

        "Grope her tits." if prDiscoFelTit == False:
            $ prDiscoFelTit = True
            show screen textbox2 with dissolve
            scene pr0393 with dissolve
            fel "Mmh...♥"
            fel "You like my tits?"
            jump prDiscofeliciaGrope2


        "Let you hand travel down south.":
            show screen textbox2 with dissolve
            if prDiscoFelTit == True:
                mc "That's not all..."
            scene pr0399 with dissolve
            fel "{b}Oh!{/i}"
            fel "You're--ah~ lot bolder than you look, y'know that cutie?"
            scene pr0402 with blinds
            fel "...and you know how to get a girl worked up. Why don't we find some place a little more private?"
            scene pr0403 with dissolve
            "..."
            jump prDiscoFeliciaBathroomSexStart

label prDiscoFeliciaBathroomSexStart:

    if _in_replay:
        show transitionfelicia01 with cmet
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

    stop music fadeout 1.5
    scene pr0404 with wipeleft
    show screen qmenu with dissolve
    mc "Hey! Wait a--"
    scene pr0405 with fade
    mc "This is the women's room!"
    fel "Keep walking, Romeo."
    scene pr0406 with dissolve
    "Felicia wasted no time. Within moments, she had me out of my clothes, pinned against the toilet like a cat who had cornered a mouse."
    scene pr0407 with dissolve
    play music "music/six-days-of-heat-pt2.mp3"
    fel "Damn, you're packing, huh?"
    fel "Hurry up and put this on."
    mc "Uh... o-okay."
    scene pr0408 with dissolve
    fel "We got no time for nice and easy, lover."
    fel "Now, shove that fat dick inside me!"
    scene pr0409 with Dissolve (0.3)
    play sound "sound effects/spurt.wav"
    with flash
    fel "--!"
    fel "Damn, you're thick."
    fel "Your face doesn't match the equipment, y'know?"
    mct "(I'm not sure what to make of that comment...)"
    scene pr0410 with dissolve
    scene pr0411 with dissolve
    scene pr0410 with dissolve
    scene pr0411 with dissolve
    "With those words, Felicia began riding me with a fervor and intensity I'd never experienced from a woman."
    scene pr0412 with dissolve
    scene pr0413 with dissolve
    mc "Ngg!"
    "With Felicia, there seemed to be no easing into things. She was fully gassed from the onset, rising and bottoming out on my dick in steady succession."
    "I on the other had, unable to find the right rhythm to match her relentless onslaught, could only weakly thrust back in a complacent fashion."
    scene pr0412 with dissolve
    scene pr0413 with dissolve
    scene pr0412 with dissolve
    scene pr0413 with dissolve
    "It was {b}her{/b} show and she knew how to run it. Each powerful downthrust was gingerly followed by a laid-back, teasing withdrawal until she once again vigorously speared herself back down to the base of my cock."
    scene pr0415 with dissolve
    fel "Aaah..! I'm so {b}fucking{/b} turned on right now."
    scene pr0414 with dissolve
    scene pr0415 with dissolve
    scene pr0414 with dissolve
    scene pr0415 with dissolve
    fel "Where did all that fire from the dance floor go, you chicken shit?"
    mct "(Did she just call me a 'chicken shit'...?)"
    scene pr0413 with dissolve
    scene pr0412 with dissolve
    scene pr0413 with dissolve
    scene pr0412 with dissolve
    mc "Geh...!" with flash
    "Every time she'd fall back down would send her toned ass on a collision course with my rapidly swelling balls, sending a jolt of pain coursing through my body."
    mc "S-slow down, you bitch!"
    scene pr0411 with dissolve
    scene pr0410 with dissolve
    fel "Ha! That's right: I'm a bitch fucking an almost complete stranger in the dirty bathroom of a nightclub."
    scene pr0411 with dissolve
    scene pr0410 with dissolve
    fel "...and you're-{b}Ah!{/b} You're the bastard giving it to me like a {b}limp-dick!{/b}"
    mct "(Shit, that had the opposite effect!)"
    scene pr0428 with dissolve
    play sound "sound effects/slap2.wav"
    with flash
    "A quick strike with the back of her hand sent a flush of heat spreading through my cheek."
    mct "(Did she just--)"
    play sound "sound effects/slap1.wav"
    with flash
    play sound "sound effects/slap2.wav"
    with flash
    scene pr0414 with dissolve
    scene pr0415 with dissolve
    fel "Come on! Don't make me do all the work!"
    scene pr0428 with dissolve
    play sound "sound effects/slap1.wav"
    with flash
    scene pr0415 with dissolve
    scene pr0414 with dissolve
    "One last wallop had sent me over the edge."
    "I was seething under the surface, spurred through irritation into wanting to turn the tables on the rude slut."
    hide screen textbox2 with dissolve
    menu prDiscoBathroomSexMenu:

        "Two can play that game: slap her tits.":
            show screen textbox2 with dissolve
            mc "You bitch!"
            scene pr0430 with dissolve
            play sound "sound effects/slap1.wav"
            with flash
            "Thwap!"
            "Instead of surprise, Felicia's face had widened into a smile. It seems I had finally given her what she wanted."
            fel "Yes! Again! {b}Harder!{/b}"
            play sound "sound effects/slap2.wav"
            with flash
            "Thwap!"
            "I was happy to comply."
            play sound "sound effects/slap2.wav"
            with flash
            play sound "sound effects/slap2.wav"
            with flash
            "Thwap! {b}Thwap!{/b}"
            "Another set of heavy-handed blows set the tanned whore's pendulous tits shaking, a trace of scarlet spreading at the site of every impact."
            hide screen textbox2 with dissolve
            jump prDiscoBathroomSexMenu2
        "{color=#FF1493}\[Strongman]{/color} She wants it rough? Use her like a ragdoll." if perk_strongman == True:
            show screen textbox2 with dissolve
            scene pr0435 with fade
            jump prDiscoBathroomSexStanding

        "Turn this bitch around and give it to her from behind.":
            show screen textbox2 with dissolve
            jump prDiscoBathroomSexDoggy

        "{color=#696969}\[Strongman] She wants it rough? Use Felicia like a ragdoll.{/color}" if perk_socialButterfly == True or perk_socialChameleon == True:
            jump prDiscoBathroomSexMenu


    menu prDiscoBathroomSexMenu2:

        "Pinch her nipples. [gr]\[FeliciaPinch\]":
            $ prDiscoFeliciaPinch = True
            show screen textbox2 with dissolve
            scene pr0431 with dissolve
            fel "{b}Ngah!{/b}" with flash
            "What had started as a reflex to Felicia's badgering had turned into clawing curiosity. I wanted to see just how much abuse these shameless milkbags can take."
            "Rolling the engorged points of her nipples between my fingers, Felicia's faced has transformed from plain amusement back to arousal."
            hide screen textbox2 with dissolve
            hide screen qmenu with dissolve
            jump prDiscoBathroomSexMenu3
        "{color=#FF1493}\[Strongman]{/color} Use her like a ragdoll." if perk_strongman == True:
            show screen textbox2 with dissolve
            scene pr0435 with fade
            jump prDiscoBathroomSexStanding

        "Give it to her from behind.":
            show screen textbox2 with dissolve
            jump prDiscoBathroomSexDoggy
        "{color=#696969}\[Strongman] Use Felicia like a ragdoll.{/color}" if perk_socialButterfly == True or perk_socialChameleon == True:
            jump prDiscoBathroomSexMenu2

    menu prDiscoBathroomSexMenu3:

        "Do it harder! [gr]\[Toughness +1\]" if prDiscoFeliciaPinch == True:
            $ toughness += 1
            $ toughness = clamp(toughness, 0, 30)
            $ prDiscoFeliciaPinch = False
            scene pr0440 with dissolve
            with flash
            show screen textbox2 with dissolve
            fel "Nggah! T-too hard!" with flash
            mc "Too hard? After all that?"
            mc "Fuck you, bitch. Keep bounching on that dick!"
            "I could hardly believe the words coming out of my mouth. I didn't normally talk like that, but I suppose this wasn't a normal encounter for me."
            "But rather than getting angry at my indictment, Felicia enthusiastically accepted my crass treatment."
            with flash
            fel "N-gh, Y-yes!"
            jump prDiscoBathroomSexCowgirl

        "Slap her tits.":
            $ prDiscoFeliciaPinch = False
            show screen textbox2 with dissolve
            scene pr0430 with dissolve
            play sound "sound effects/slap1.wav"
            with flash
            "Thwap!"
            hide screen textbox2 with dissolve
            jump prDiscoBathroomSexMenu3

        "Slap her face." if prDiscoFeliciaPinch == False:
            show screen textbox2 with dissolve
            scene pr0429 with dissolve
            play sound "sound effects/slap2.wav"
            with flash
            "Thwap!"
            scene pr0414 with dissolve
            fel "You bastard, yes!"
            jump prDiscoBathroomSexCowgirl

        "Continue fucking her like this.":
            jump prDiscoBathroomSexCowgirl

        "{color=#FF1493}\[Strongman]{/color} Use her like a ragdoll." if perk_strongman == True:

            scene pr0435 with fade
            jump prDiscoBathroomSexStanding

        "Give it to her from behind.":
            jump prDiscoBathroomSexDoggy
        "{color=#696969}\[Strongman] Use Felicia like a ragdoll.{/color}" if perk_strongman == False:
            jump prDiscoBathroomSexMenu3

label prDiscoBathroomSexCowgirl:
    show screen textbox2 with dissolve
    show screen qmenu
    scene pr0432 with Dissolve (0.3)
    with flash
    mc "Ghh-!"
    scene pr0433 with dissolve
    scene pr0432 with dissolve
    scene pr0433 with dissolve
    "Spurred on by the escalation, Felicia grabbed me by my throat and allowed her sharp nails to dig deep into the soft flesh of my neck."
    scene pr0432 with dissolve
    scene pr0433 with dissolve
    scene pr0432 with dissolve
    scene pr0433 with dissolve
    "Noticing me wince from the sudden rough contact, her voice softened and she retreated back from the lust-addled, slutty character she was putting on."
    fel "...hey-{b}ah!{/b}. Let me know if I'm going too far, okay?"
    scene pr0432 with dissolve
    scene pr0433 with dissolve
    scene pr0432 with dissolve
    scene pr0433 with dissolve
    "The sudden touch of concern in the midst ball-slapping, ugly sex caught me off guard and brought me back around to reality. Still, despite her words of worry, she continued on with the abject, impassioned bucking of her hips."
    "The dichotomy of those two conflicting displays, her tender concern over my comfort versus the unrelenting vulgar needs of her body, made this whole situation that much more incredibly hot to me."
    mc "It's okay, I'm fine, just keep shaking your hips!"
    scene pr0432 with dissolve
    scene pr0433 with dissolve
    scene pr0432 with dissolve
    scene pr0433 with dissolve
    "Content with my answer, Felicia launched into the final stretch. Her previously deliberate, powerful bouncing quickly devolving into a rapid, clumsy clapping of skin on skin."
    "As much as I would have enjoyed the sight of her breasts rising and falling in sync with our movement as I race toward orgasm, Felicia's iron grip on my throat and hair kept my eyeline firmly leveled on hers."
    "It was like she was boring a hole straight through me."
    scene pr0432 with dissolve
    scene pr0433 with dissolve
    scene pr0432 with dissolve
    scene pr0433 with dissolve
    "This carried on for another minute until Felicia was gulping down whispy, shallow breaths putting out the telltale signs that we were nearing the end of the fun."
    "Spurred on by the thought of making the bombshell cum, I pistoned my hips harder, desperately trying to reach the deepest part of her canal in an instinctual (but nonsensical) bid to make sure my soon-to-be release would successfuly reach her uterus."
    scene pr0432 with dissolve
    scene pr0433 with dissolve
    scene pr0432 with dissolve
    scene pr0433 with dissolve
    fel "You feel so fucking good, [mcf]."
    scene pr0432 with dissolve
    scene pr0433 with dissolve
    fel "Y-you're close, aren't you? I can - {b}ah!{/b} - tell!"
    "I would've liked to turn the observation around on her, but I could barely choke out the words thanks to her tight grasp on my vocal cards."
    scene pr0432 with dissolve
    scene pr0433 with dissolve
    scene pr0432 with dissolve
    scene pr0433 with dissolve
    "However, it didn't take long for me to be proven right."
    "Soon her pussy clamped down {b}hard{/b}, her inner walls greedily sucking me in and sending me on the way to my own climax."
    scene pr0434 with flash

    fel "Fuuuuuuck~!"
    play sound "sound effects/spurt.wav"
    with flash
    play sound "sound effects/spurt.wav"
    with flash
    play sound "sound effects/spurt.wav"
    with flash
    fel "Niiii-!"
    scene pr0453 with dissolve
    fel "...ha...aha...ha..."
    fel "That was... aha... {b}good{/b}."
    "There was little time for me to comfortably bask in the post-coital bliss, as the shuffling of feet outside the bathroom stall reminding me of just how open what we just did was."
    mc "*Huff*... *huff*... You didn't even try to be quiet."
    fel "Who cares? The louder it is, the more fun it is."
    scene black with fade
    "......"
    "..."
    $ renpy.end_replay()
    jump prDiscoCafeJump



label prDiscoBathroomSexStanding:
    show screen textbox2 with dissolve
    show screen qmenu
    fel "...huh?!"
    "Calling to life every muscle fiber in my legs and back, I scooped the lively bombshell into my arms and brought us to a standing position, pressing Felicia's back against the cold power coated steel frame of the bathroom stall. "
    fel "W-what are you doing?"
    scene pr0417 with dissolve
    fel "W-woah, I didn't know you could--"
    play sound "sound effects/spurt.wav"
    scene pr0418 with Dissolve(0.3)
    with flash
    fel "Shit!"
    "Without any ceremony or warning, I plunged my cock deep back into Felicia's warm insides."
    scene pr0417 with dissolve
    fel "This is so hot, I've never been handled like--"
    scene pr0418 with Dissolve(0.3)
    with flash
    fel "{b}THIS--!{/b}"
    scene pr0417 with dissolve
    "I'm fairly confident in my strength, but picking up a person who's not expecting to be picked up is a gamble."
    mct "(Glad that worked out... probably would kill the mood if I dropped her on her ass.)"
    fel "H-huh? Why aren't you moving? Come on! {b}Fuck me!{/b}"
    "Growing impatient with me, she followed her plea by weakly thrusting her hips to meet mine."
    "It was a cute, but futile attempt. The way I had her sandwiched against the wall left her with little leverage to swing her hips."
    "However, having a beautifully stunning woman impotently try to impale herself on my cock filled me with a twisted sense of conquest and made me want to tease her all the more."
    hide screen textbox2 with dissolve
    menu:
        "If you want something, all you've got to do is ask.":
            show screen textbox2 with dissolve
            mc "If you want something, you should ask nicely for it."
            fel "You got to be kidding me. Stop teasing me, you bastard!"
            "........."
            "......"
            "..."
            "After a few moments of letting the anticipation tantalizingly build, Felicia finally placated me with what I wanted to hear. Albeit a little sarcastically."
            fel "...{b}Fine!{/b}"
            fel "[mcf], will you please thrust that big, thick cock into me and fuck me stupid? Pretty please, with a cherry on top?"
            "...close enough."
            "Satisfied with her humoring me, I rolled my hips back and readied myself to give the slut in my arms the best fucking I could muster."

        "No need to be rude, give the lady what she wants.":
            show screen textbox2 with dissolve
            "There's no need to draw this out. It's clear that both of us {b}deeply{/b} wants this."
            "Wasting no time, I rolled my hips back and readied myself to give the slut in my arms the best fucking I could muster."

    scene pr0418 with dissolve
    play sound "sound effects/spurt.wav"
    fel "--Aah!♥" with flash
    scene pr0419 with dissolve
    scene pr0418 with dissolve
    scene pr0419 with dissolve
    "Slamming my hips forward and thrusting my cock as deep into Felicia as it would go, I withdrew and started to zealously jackhammer her cunt until I had developed a steady, vigorous rhythm."
    scene pr0418 with dissolve
    scene pr0419 with dissolve
    scene pr0418 with dissolve
    scene pr0419 with dissolve
    fel "So g-good!"
    mc "Should I slow down?"
    fel "No, don't you dare!"
    scene pr0418 with dissolve
    scene pr0419 with dissolve
    fel "Fuck me until I can't walk straight!"
    scene pr0418 with dissolve
    scene pr0419 with dissolve
    scene pr0418 with dissolve
    scene pr0419 with dissolve
    fel "Nn-Aaa-~♥ Uggha--♥"
    "No doubt anyone else in the restroom were now being treated to a cacophony of delirious expletives and the reverberation of flesh smacking against flesh.'"
    if history_voyeur == True:
        "I've got to admit: the thought of other people being in proximity to our fucking turned me on even more."
        "Felicia, for her part, was incredible."
    else:
        "The thought I was having sex in public was mortifying, almost to the point of making me want to stop - almost."
        "How could I even consider it? Felicia, for her part, was incredible."
    scene pr0418 with dissolve
    scene pr0419 with dissolve
    scene pr0418 with dissolve
    scene pr0419 with dissolve
    "She was so hot that it felt unreal that a woman like her would want anything to do with me, yet here she was actively trying to pull me in as deep as I'd go."
    "In the best way: she was real, bonafide slut."
    scene pr0418 with dissolve
    scene pr0419 with dissolve
    scene pr0418 with dissolve
    scene pr0419 with dissolve
    "I wish I could drag this out for as long as possible, but I knew I couldn't last."
    "If the tight strangle her body had on my cock wasn't enough to have me already precariously close to cumming, the strain this position was taking on my muscles had me on a clock."
    "Fuck it. I'm gonna be sore tomorrow anyway, let's just see how far I can push myself."

    if toughness > 21:
        mc "I'm going to finish now. Better brace yourself, slut!"
    else:
        mc "I'm picking up the pace now, okay?"

    fel "..ngh--huh?"

    scene pr0420 with flash
    "With that, I launched into the final stretch, hips violently bucking and hot air billowing out of my lungs, taking care to press Felicia's long legs as far back in order to get a better angle at her cunt."
    scene pr0421 with dissolve
    scene pr0420 with dissolve
    scene pr0421 with dissolve
    scene pr0420 with dissolve
    fel "Ggg--ah~!"
    fel "....fuck{w}fuck{w}Fuck{w}FUCK{w}{b}FUCK{/b}!"
    "If by some chance the other bathroom patrons had missed all of Felicia's fervent cries and lust-laced expletives, then the explosive quaking of the stall's steel frame painted a clear picture."
    scene pr0421 with dissolve
    scene pr0420 with dissolve
    scene pr0421 with dissolve
    scene pr0420 with dissolve
    "I was putting everything I had into fucking her. The muscles in my arms burned from keeping the hellcat aloft and a dull ache shot from my waist and up my back with each thunderous meeting of our hips."
    "But I didn't care -- I was too lost in my rut to give a damn about any public decency laws. All I cared about was driving my cock forward as deep as I could go in a bid to fulfill my biological imperative."
    "Of course, this was all illogical. I had protection on, but all my higher faculties had melted into images and animal compulsion by that point."
    scene pr0421 with dissolve
    scene pr0420 with dissolve
    scene pr0421 with dissolve
    scene pr0420 with dissolve
    fel "Ngh--Ngh--Nggah~♥!"
    "Any pretense of dirty talk from either of us had devolved into a series of weary grunts and other guttural babble."
    "At this point, a series of small orgasms had wracked Felicia's body, causing her inner walls to contract tightly around my member, but the final big one was what pushed me over the edge."
    scene pr0421 with flash
    "My body knowing I was at my limit, I made one last futile, robotic effort to bury my dick as far back as it'd go, kissing Felicia's cervix with its tip and sending Felicia's spasming in my arms."
    scene pr0438 with flash
    play sound "sound effects/spurt.wav"
    with flash
    mc "Fuuuuuck!"
    play sound "sound effects/spurt.wav"
    with flash
    play sound "sound effects/spurt.wav"
    with flash
    scene pr0934 with dissolve
    "My orgasm spelled the end of my strength, my arms and legs turned to jelly, and we tumbled to the floor."
    mc "*huff*...*huff*...a-are you okay?"
    fel "*huff*....*huff*...holy shit."
    fel "I didn't know you had that in you. You are full of surprises."
    fel "I'm going to be sore in the morning."
    scene black with fade
    "There was little time for me to comfortably bask in the post-coital bliss, as the shuffling of feet outside the bathroom stall reminding me of just how open what we just did was."
    "......"
    "..."
    $ renpy.end_replay()
    jump prDiscoCafeJump



label prDiscoBathroomSexDoggy:
    scene black with fade
    show screen textbox2 with dissolve
    show screen qmenu
    $ felPN = "Daddy"
    mc "Stand up."
    fel "...huh--"
    fel "HEY!"
    "Not waiting for her to comprehend my request, I gave Felicia a light shove off me and quickly spun her around, planting her against the cold frame of the bathroom stall."
    scene pr0422 with dissolve
    "By now she had an idea of what I wanted, and taking no issues with me being on top, assumed the best position to give me easy access to penetrate her from behind."
    fel "I've got no problem with you taking the lead, as long as you don't disappoint."
    "As if to underline her point, Felicia gave her ass a seductive wag."
    "Not wanting to leave the lady waiting, I did as she asked, bucking my hips forward and back in deep, tentative thrusts."
    scene pr0425 with dissolve
    fel "F-fuck! That's it."
    scene pr0422 with dissolve
    scene pr0423 with dissolve
    scene pr0422 with dissolve
    scene pr0423 with dissolve
    fel "I love how deep your fat dick can hit, especially at this angle."
    fel "Your cock is practically built for giving it to sluts from behind."
    scene pr0422 with dissolve
    scene pr0423 with dissolve
    scene pr0422 with dissolve
    scene pr0423 with dissolve
    "Felicia continued on with her audacious dirty talk, discarding any pretense of secrecy or hushed tones and putting it loud and plain for the whole bathroom to hear."
    scene pr0422 with dissolve
    scene pr0423 with dissolve
    mc "People can hear us..."
    scene pr0422 with dissolve
    scene pr0423 with dissolve
    scene pr0422 with dissolve
    fel "Ngg-s-so? People bang in club bathrooms all the time."
    fel "Stop thinking about other people and focus on me!"
    "She was right. I was already past the point of no return and I wasn't about to blue ball myself in the name of public decency."
    scene pr0425 with flash
    fel "--!"
    "Fighting past my apprehension, I decided to find a pace that would leave the mouthy slut in my grip speechless."
    scene pr0424 with dissolve
    scene pr0425 with dissolve
    scene pr0424 with dissolve
    scene pr0425 with dissolve
    fel "T-there it is!"
    "Felicia wasn't content in letting me do all the work. Matching my efforts, every time I withdrew she unsheathed herself and on the return, she sent her ass crashing back to meet my hips."
    "It was quite the ass too. Toned and shapely with a pleasant give. Of course, I didn't have to see her nude to know she takes care of herself."
    "That's something you can spot from across a room or just tell by the way she carries herself."
    scene pr0424 with dissolve
    scene pr0425 with dissolve
    scene pr0424 with dissolve
    scene pr0425 with dissolve
    scene pr0424 with dissolve
    "It boggles my mind that she's even interested in fucking someone like me, but I'm not going to squander the opportunity. I'm going to fuck so hard my bones will ache."
    "Full of myself, with machismo coursing through my veins, I uncharacteristically resolved to give her the best fucking of her life."
    scene pr0425 with flash
    play sound "sound effects/slap2.wav"
    "Thwap!"
    "Almost by instinct, I gave bombshell's ass a tentative smack."
    fel "--oh!"
    scene pr0424 with dissolve
    "The impact sent a shock through Felicia's body, causing her canal to pleasantly clamp down on my member. I had to do that again!"
    scene pr0425 with flash
    play sound "sound effects/slap2.wav"
    "Thwap!"
    mc "How's that for a limp dick, you slut?"
    scene pr0424 with flash
    play sound "sound effects/slap2.wav"
    "Thwap!"
    mc "You like that?"
    scene pr0425 with flash
    fel "Yes, daddy~!♥ It's so good!♥"
    scene pr0424 with dissolve
    fel "Shit! Ig-ignore that!"
    mct "(Daddy...?)"
    scene pr0425 with dissolve
    "That's a first for me. It has a nice ring to it, especially coming from an older woman."
    scene pr0426 with dissolve
    scene pr0427 with dissolve
    scene pr0426 with dissolve
    scene pr0427 with dissolve
    mc "Who's your daddy?"
    "As cheap and pornographic as it was, my arousal compelled me to latch onto Felicia's slip of tongue, letting me utter what I'd normally find embarrassing and extremely corny."
    scene pr0426 with dissolve
    fel "Y-you are?"
    scene pr0427 with flash
    play sound "sound effects/slap2.wav"
    "Thwap!"
    mc "WHO'S your daddy?"
    scene pr0426 with dissolve
    fel "You are!"
    scene pr0427 with dissolve
    mc "...and what's my name?"
    scene pr0426 with dissolve
    fel "[mcf]!"
    scene pr0427 with flash
    play sound "sound effects/slap2.wav"
    "Thwap!"
    mc "Say my name!"
    fel "[mcf]!"
    scene pr0426 with dissolve
    "At this point, a series of small orgasms had wracked Felicia's body, causing her inner walls to contract tightly around my member, but the final big one was what pushed me over the edge."
    scene pr0437 with flash
    mc "Take it you, whore!"
    play sound "sound effects/spurt.wav"
    "Knowing I was at my limit, I made one last effort to bury my dick as far back as it'd go, kissing Felicia's cervix with its tip and sending Felicia's spasming in my grip." with flash
    play sound "sound effects/spurt.wav"
    with flash
    mc "Fuuuuuck!"
    play sound "sound effects/spurt.wav"
    with flash
    play sound "sound effects/spurt.wav"
    with flash
    scene pr0936 with dissolve
    mc "*huff*...*huff*..."
    fel "*huff*...*huff*..."
    "Covered in sweat and lungs burning from exertion, it took some time before the two of us finally came crashing back to reality."
    "....."
    "..."
    scene pr0937 with dissolve
    mc "So... daddy?"
    fel "Shut up. It's an old... habit from my college days."
    mc "Got it..."
    fel "You didn't seem to mind."
    "She had me there."
    scene black with fade
    "There was little time for me to comfortably bask in the post-coital bliss, as the shuffling of feet outside the bathroom stall reminding me of just how open what we just did was."
    "......"
    "..."
    $ renpy.end_replay()
    jump prDiscoCafeJump


label prDiscoCafeJump:
    stop music fadeout 3.0
    scene pr0439 with fade
    if not persistent.felBathroomGallery:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.felBathroomGallery = True
    fel "That was fun, lover. We should probably get back now though"
    $ renpy.pause(0.5, hard=True)
    scene pr0926 with dissolve
    "Bleep!"
    scene pr0927 with dissolve
    mc "It's from Ian. Probably wondering where we are..."
    hide screen textbox2 with dissolve
    scene pr0928 with dissolve

    call phone_start_kil from _call_phone_start_kil
    call  message_start("Killian", "Sorry, had to leave. Mina's mad. TTYL.") from _call_message_start

    call phone_end_kil from _call_phone_end_kil
    show screen textbox2 with dissolve
    scene pr0929 with dissolve
    mct "(Short and to the point...)"
    fel"Looks like Ian and Mina bailed on us--"
    scene pr0930 with dissolve
    play sound "sound effects/door-openclose.wav"
    "{i}Creeeek{i}."
    mc "Uh, let's get out of here."
    "..."
    scene black with fade
    play music "music/organic.mp3"
    "Returning to the din of the club, I read Ian's brief text to Felicia."
    scene pr0931 with dissolve
    fel "All part of the stupid game they play. Don't get me wrong. I love Mina, but Ian makes her sink to his level."
    mct "(Funny she should say that...)"
    "My mind immediately drew a parallel to my recent employment at the Carnation Club."
    scene pr0932 with dissolve
    fel "I don't want to call it a night yet! Why don't we get something to eat? I'm fucking starving!"
    "A little bit of food to offset the alcohol didn't sound like a bad idea. Plus, I'd feel like a prick if I just fucked her in a bathroom and left."
    scene pr0933 with dissolve
    mc "Okay! I know a place!"
    scene black with fade
    stop music fadeout 3.0
    "......"
    jump prAfterPartyCafe
