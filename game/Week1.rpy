################################################################################
################################################################################
###                               PALE CARNATIONS                            ###
################################################################################
################################################################################


## The contents of day 1-5 of the first week go here.

label june01start:


    # correct typo in ch1
    if Sam_Friendship > 3 and perk_socialChameleon == True:
        $ Sam_Friendship = 4
    if prAfterParty == False:
        $ Felicia_Affection += 4
    if felPN == "Daddy":
        $ feliciaDaddy = True

## Opening Sequence ------------------------------------------------------------

    $ date = "intronight"

    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/page-turn.wav"
    scene titlecard_base with blinds
    $ renpy.pause(1.5, hard=True)
    scene titlecard_week1 with dissolve
    $ renpy.pause(3, hard=True)
    play music "music/Moonlight-Sonata.mp3"
    scene titlecard_week1full with dissolve
    $ renpy.pause(3, hard=True)
    scene w1_0001 with pixellate
    show screen textbox2 with dissolve
    show screen qmenu with dissolve
    cm "So, tell the viewers at home your name."
    scene w1_0002 with dissolve
    woman "My name is... Rebecca."
    scene w1_0001 with dissolve
    cm "Oh, c'mon. You're not being honest, are you? Tell them your {b}real{/b} one, sweetheart."
    scene w1_0003 with dissolve
    woman "..."
    scene w1_0002 with dissolve
    vic "...my name is Victoria."
    scene w1_0001 with dissolve
    cm "What are you here to do, {i}Vicky{/i}?"
    scene w1_0002 with dissolve
    vic "I'm here to have sex."
    scene w1_0001 with dissolve
    cm "That's great. You like big ones, right?"
    scene w1_0004 with pixellate
    stop music fadeout 2.0
    vic "Yes, I love {b}huge{/b} cock."


## Edwin gets a new apartment --------------------------------------------------

    $ date = "june01day"

    play music "music/crinoline-dreams.mp3"
    scene w1_0005 with pixellate
    vic "...and they're letting you live here, rent-free?"
    scene w1_0006 with dissolve
    $ statisticsunlock = True
    play sound "sound effects/notification.wav"
    show statsunlock with dissolve
    "The next two weeks leading into June proved uneventful, at least when compared to the excitement of what I had recently experienced."
    hide statsunlock with dissolve
    show june01day with squares
    "Ian had begun showing up more and more unannounced, but for the most part, it felt like the start of a normal summer."
    "All with the exception of one thing..."
    "After August had {b}firmly{/b} insisted I make use of one of the club's unused pieces of real estate, plus advanced me a month's paycheck, I found myself under a drastically different standard of living."
    "One that beats the crap out of living off ramen and stealing the neighbor's WIFI."
    scene w1_0007 with dissolve
    mc "My new boss said someone should take care of it since it was just sitting here."
    scene w1_0008 with dissolve
    pause 1.0
    scene w1_0009 with dissolve
    vic "..."
    "My mother levied a suspicious look I hadn't seen since I was a teen my way."
    scene w1_0010 with dissolve
    vic "You're not doing anything... {i}weird{/i}, right?"
    scene w1_0009 with dissolve
    hide screen textbox2 with dissolve
    menu:
        "Flatly deny it.":
            scene w1_0011 with dissolve
            show screen textbox2 with dissolve
            mc "They're really just waiting to flip this place."
            mc "I mean, it's me we're talking about. I barely leave my apartment. What kind of weird things would I get up to?"
            scene w1_0012 with dissolve
            vic "You're right I suppose."
            vic "You've got a good head on your shoulders."


        "Deflect with a joke.":
            scene w1_0011 with dissolve
            show screen textbox2 with dissolve
            mc "Not really, just working as a {b}rentboy{/b} to pay for college."
            scene w1_0010 with dissolve
            vic "Oh, is that all?"

    scene w1_0013 with dissolve
    vic "Well, if you're going to be house-sitting such a swanky place, I think we might be due for a change of scenery for our movie night..."
    play sound "sound effects/door-knock.wav"
    stop music fadeout 3.0
    scene w1_0014 with dissolve
    "*Knock, knock.*"
    kil "I'm coming in, better put your cock away--!"
    scene w1_0015 with dissolve
    play music "music/hotshot.mp3"
    kil "Oh, {b}hello{/b} Mrs. [mcl]. I didn't know you were here..."
    kil "I was saying, uh..."
    scene w1_0016 with dissolve
    vic "Relax, Ian. We've all heard the word before."
    scene w1_0017 with dissolve
    mc "Sorry, what word? I couldn't hear him through the door."
    vic "{b}Cock{/b}. He said to put your cock away I believe."
    kil "...eheh."
    "For whatever reason, my mom remains the only person who can make Ian feel embarrassed about his behavior."
    "It had developed into a well-oiled routine over the years, one I'm glad to see still works to this day."
    scene w1_0018 with dissolve
    vic "Oh, come here!"
    scene w1_0019 with dissolve
    vic "It's nice to see you, Ian."
    vic "I want to thank you for getting my son a job."
    scene w1_0020 with dissolve
    vic "It clearly comes with some perks."
    scene w1_0021 with dissolve
    kil "Uh... n-no problem..."
    scene w1_0022 with dissolve
    vic "So, you guys have something planned today?"
    scene w1_0023 with dissolve
    mc "He's actually giving me a ride to work. I mentioned it earlier, remember?"
    vic "Oh, yeah. You did say that..."
    scene w1_0024 with dissolve
    kil "[mcf] doesn't have a car, so it's up to me to bus him around. He really should be more grateful."
    scene w1_0025 with dissolve
    vic "Well, it's great he's got such a great friend to depend on. Don't you agree, [mcf]?"
    scene w1_0026 with dissolve
    mc "I think, if you're going to be so pleased with yourself about it, I'll just take the subway from now on..."
    play ambient "sound effects/city-night.wav"
    scene black with fade
    stop music fadeout 3.0
    "......"
    "..."
    scene club-fr-day with blinds
    "--later on, back at the club. After NOT taking the subway."
    stop ambient fadeout 1.5

## Theme: Service --------------------------------------------------------------

    scene w1_0027 with fade
    kat "Good, you're all here. I wanted to go over our inaugural week's theme."
    scene w1_0028 with dissolve
    ver "...ngh, before you start yakking our heads off, can you clarify something first?"
    scene w1_0029 with dissolve
    kat "What is it, Miss Lynch?"
    scene w1_0028 with dissolve
    ver "If we're just checking in for the week, WHY do we have to be dressed like this?"
    scene w1_0030 with slideleft
    play music "music/a-brand-new-start.mp3"
    kat "I wanted to see how you girls looked in this week's uniform."
    scene w1_0031 with dissolve
    kat "To figure out if I need to make any adjustments to it before Saturday."
    scene w1_0032 with dissolve
    fel "I think we look hot. What do you say, Rosie?"
    scene w1_0033 with dissolve
    rose "It's... a little embarrassing. Feels like a Halloween costume..."
    scene w1_0034 with dissolve
    fel "I know! Isn't that fun?"
    scene w1_0035 with dissolve
    kat "Well, I think all three of you girls look {b}wonderful{/b} in it. Without a doubt, it'll be a crowd pleaser."
    scene w1_0036 with dissolve
    kat "What say you, [mcf]? Killian?"
    scene w1_0037 with dissolve
    hide screen textbox2 with dissolve
    menu:
        "Hard to say. Ask the girls to give you a little spin. [gr]\[Felicia +1\] \[Killian +1\] [red]\[Veronica -1\]":
            scene w1_0038 with dissolve
            $ Felicia_Affection += 1
            $ Killian_Bromance += 1
            $ Veronica_Affection -= 1
            $ w1Spin = True
            show screen textbox2 with dissolve
            mc "I think I need to see more, before I can form an educated opinion."
            mc "Why don't you girls turn around? Give us a little spin."
            scene w1_0039 with dissolve
            kil "I say THAT's a scholarly idea if I've ever heard one."
            scene w1_0041 with dissolve
            ver "Pig."
            rose "..."
            fel "Heheh..."
            scene w1_0042 with dissolve
            fel "Ta~da!"
            scene w1_0043 with dissolve
            fel "Oh, c'mon ladies. You heard the boss woman. It's all part of the job, right?"
            scene w1_0044 with dissolve
            "Spurred on by Felicia's words, Rosalind followed Felicia's example."
            scene w1_0045 with dissolve
            ver "Whatever."
            scene w1_0046 with dissolve
            "Veronica gave a quick spin of her own."
            scene w1_0041 with dissolve
            ver "You take it all in, you perv?"
            kil "You bet!"


        "Don't be a pig about it. [red]\[Toughness -1\]":
            $ toughness -= 1
            show screen textbox2 with dissolve
            mct "(No point in objectifying the girls any further, right? I should just give Mrs. Pulman my answer.)"

    scene w1_0040 with dissolve
    "Well, who looks best in the uniform?"
    hide screen textbox2 with dissolve

    menu:

        "Rosalind is your favorite.":
            scene w1_0047 with dissolve
            show screen textbox2 with dissolve
            "I shot Rosalind another glance."
            "Yep, she's the one for sure. She's got a fuller, more motherly figure than the other two and she fills out the uniform in all the right places."
            scene w1_0048 with dissolve
            mc "It's Rosalind."
            kat "Why am I not surprised?"
            scene w1_0053 with dissolve
            kil "Hmmm... I say Felicia, but not that it isn't close. You other ladies look amazing too."
            scene w1_0054 with dissolve
            ver "What would we do without the pretty boy's approval?"
            ver "Can we move on to why we're here, please?"
            scene w1_0055 with dissolve
            kat "I suppose it's time. I did gather you here for a reason."


        "Felicia is your favorite. [gr]\[Felicia +1\]":
            $ Felicia_Affection += 1
            scene w1_0049 with dissolve
            show screen textbox2 with dissolve
            "I gave Felicia another look up and down."
            "Yep, she's the one for sure. She strikes the perfect balance between toned and shapely. Honestly, she makes the {b}perfect{/b} bunny rabbit, doesn't she?"
            mc "It's Felicia."
            scene w1_0050 with dissolve
            fel "Ha! I do look amazing, don't I?"
            scene w1_0053 with dissolve
            kil "I agree with [mcf]. Felicia takes it, not that it isn't close."
            scene w1_0054 with dissolve
            ver "What would we do without the pretty boy's approval?"
            ver "Can we move on to why we're here, please?"
            scene w1_0055 with dissolve
            kat "I suppose it's time. I did gather you here for a reason."


        "Veronica is your favorite. [red]\[Veronica -1\]":
            $ Veronica_Affection -= 1
            scene w1_0051 with dissolve
            show screen textbox2 with dissolve
            "My eyes were drawn back to Veronica."
            "Yep, she's the one for sure. There's something about a woman with muscles. It contrasts wonderfully with the bunny costume. Plus, those heels show off her long legs splendidly."
            mc "It's Veronica."
            scene w1_0052 with dissolve
            ver "Gee, {i}thanks.{/i}"
            scene w1_0053 with dissolve
            kil "Hmmm... I say it's Felicia, not that it isn't close."
            scene w1_0054 with dissolve
            ver "What would we do without the pretty boy's approval?"
            ver "Can we move on to why we're here, please?"
            scene w1_0055 with dissolve
            kat "I suppose it's time. I did gather you here for a reason."


        "This is stupid. They all look great. [gr]\[Veronica +2\] [red]\[Kathleen -1\]" if w1Spin == False:
            $ Veronica_Affection += 2
            $ Kathleen_Affection -= 1
            show w1_0056 with dissolve
            show screen textbox2 with dissolve
            mc "This is dumb. They all look great."
            scene w1_0057 with dissolve
            mc "Can't we just get to why we're here?"
            ver "I agree."
            scene w1_0036 with dissolve
            kat "Do lighten up, Mr. [mcl]."
            scene w1_0058 with dissolve
            kat "Oh, but I do suppose we should get started."

    scene w1_0027 with dissolve
    kat "I am a busy woman after all."
    scene w1_0035 with dissolve
    kat "This being the first week, it's only proper we introduce you girls to our members ahead of time."
    kat "Plus, I think it'll help loosen you up."
    scene w1_0028 with dissolve
    rose "Loosen us up?"
    scene w1_0059 with dissolve
    kat "To put it bluntly, two of you standing here have no experience with what you're walking into this week."
    scene w1_0060 with dissolve
    fel "I thought you've explained it pretty well, to be honest."
    fel "It's going to involve lots of sex, bondage, toys..."
    scene w1_0061 with dissolve
    fel "A little pain, humiliation, lots and LOTS of pleasure..."
    scene w1_0062 with dissolve
    fel "Anything you can throw at us to get a room of old men off, right? Ian said you guys don't fuck around. It sounds like it's going to be awesome."
    scene w1_0063 with dissolve
    kat "You are a unique woman aren't you, Mrs. Ford? Such an unusual request for your prize too..."
    scene w1_0084 with dissolve
    kat "I'm going to look forward to making you regret taking this so lightly."
    scene w1_0064 with dissolve
    fel "I believe you! Hehe...!"
    scene w1_0065 with dissolve
    mc " *Whisper* What did she ask for?"
    scene w1_0066 with dissolve
    kil "*Whisper* Beats me, but I {i}knew{/i} telling her about the club was a good idea."
    if feliciaSex == True:
        scene w1_0067 with dissolve
        kil "*Whisper* I know you got a taste of it, right? Experienced it first hand? Eh? Eh?"
    scene w1_0066 with dissolve
    kil "*Whisper* I don't know who to put my money on winning this thing. That freakish redhead or her."
    scene w1_0068 with dissolve
    kat "So, with those two goals in mind, I thought I'd get the three of you to help with this week's promotional material."
    scene w1_0069 with dissolve
    ver "You're going to market us like some kind of good?"
    scene w1_0068 with dissolve
    kat "...and why wouldn't I? That's what you three are now -- for the next four weeks, you are the Carnation's Club's {b}product{/b}."
    scene w1_0070 with dissolve
    rose "What are you going to have us do?"
    scene w1_0068 with dissolve
    kat "We're going to film something of a calling card for our members. The goal is to promote early engagement."
    kat "Get our members excited to meet you girls and encourage some early betting on this Saturday's outcome."
    scene w1_0071 with dissolve
    fel "Sounds fun! I'm game!"
    scene w1_0072 with dissolve
    rose "...I'll do whatever is asked of me."
    scene w1_0073 with dissolve
    ver "Let's do this."
    scene w1_0065 with dissolve
    mc "*Whisper* The club members bet on the outcome of the matches?"
    scene w1_0066 with dissolve
    kil "*Whisper* Of course they do. Anything that has a winner, will have people betting on it. That's basically a universal truth."
    kil "*Whisper* Money flows in and out of this place in a lot ways. Gambling is a big one this time of year."
    scene w1_0074 with dissolve
    kat "Mr. [mcl]! I'm going to let you have first pick."
    "Pulling me back to the matter at hand, Mrs. Pulman directed the conversation my way."
    scene w1_0075 with dissolve
    mc "What am I picking?"
    scene w1_0074 with dissolve
    kat "We'll be splitting up to film individual footage of each of the girls. I'll let you pick who you want to work with."
    scene w1_0075 with dissolve
    mc "I'm not a videographer, though..."
    scene w1_0076 with dissolve
    kil "You're not expected to be {i}Vittorio Storaro{/i} here. Just shoot and talk, the old men eat this gonzo-style shit up."
    scene w1_0075 with dissolve
    mc "So you just want me to interview one of them?"
    scene w1_0074 with dissolve
    kat "Exactly. Profile them. Ask them questions. Get them to open up and play to the camera. Maybe have them say some dirty things."
    scene w1_0077 with dissolve
    "I looked back over at Rosalind and the rest of the girls."
    kat "The goal is to sell the viewer on your Carnation, maybe tie it into this week's theme if you're creative enough."
    kil "You haven't told us what this week's theme is yet."
    scene w1_0058 with dissolve
    kat "I didn't? I got ahead of myself it seems."
    scene w1_0078 with dissolve
    kat "You see ladies, each exhibition night has it's own theme."
    scene w1_0079 with dissolve
    kat "Four weeks. Four saturdays. Four themes to center that night's activities around."
    scene w1_0078 with dissolve
    kat "This week's theme is an {i}understated{/i} one: {b}service{/b}."
    scene w1_0080 with dissolve
    ver "Understated?"
    scene felhandjobmotion with dissolve
    fel "She means like handjobs, blowjobs, {i}titjobs{/i}. Right, Kat?"
    scene w1_0083 with dissolve
    ver "That... actually doesn't sound too bad."
    "Considering what Veronica endured a couple of weeks ago, I suppose that does sound pretty tame in comparison."
    scene w1_0086 with dissolve
    kat "You'd both be mistaken. It's nothing as banal."
    kat "Service is about attitude. Hard work. The willing diminishment of the individual."
    scene w1_0085 with dissolve
    ver "I should've known better than to ask."
    ver "{size=-10}Turning sucking a dick into some greater purpose, what a crock of...{/size=-10}"
    "Ignoring Veronica's comment, Mrs. Pulman returned her attention back to me and asked the same question she had posed earlier."
    scene w1_0077 with dissolve
    kat "So, who will it be, Mr. [mcl]? I'll let you pick since you're our newest employee."
    "Who {b}do{/b} I want to work with here? I'll be filming and interviewing them. I could use this as a chance to get to know one of them better."

    if roseTakeAdvantage == True and roseSeduceFlag == False:
        "Rosalind seems easy to get along with, or at least she's amicable. Plus, we've already shared some of that {i}hands on{/i} experience already."
    if roseTakeAdvantage == True and roseSeduceFlag == True:
        "Rosalind seems easy to get along with, or at least she's amicable. Plus, she seemed pretty into me at the cafe."
    if roseTakeAdvantage == False and roseSeduceFlag == True:
        "Rosalind seems easy to get along with, or at least she's amicable. Plus, I like to think we shared something the night we met."
    if roseTakeAdvantage == False and roseSeduceFlag == False:
        "Rosalind seems easy to get along with, or at least she's amicable."

    "Veronica, on the other hand, is pretty prickly. Not that I blame her, considering where she stands and who I represent. Working together might be difficult, but maybe I could use this opportunity to show her I'm on her side?"
    "Then there's Felicia. She'd be the easiest to work with, considering our existing rapport."
    hide screen textbox2 with dissolve

    menu:
        "Partner with Rosalind":
            $ w1RoseGonzo = True
            jump w1roseinterviewpick
        "Partner with Felicia":
            $ w1FelGonzo = True
            jump w1felinterviewpick
        "Partner with Veronica":
            $ w1VeroGonzo = True
            jump w1verointerviewpick


label w1roseinterviewpick:
    show screen textbox2 with dissolve
    scene w1_0087 with dissolve
    mc "I'll take Rosalind."
    rose "Me...?"
    "She looked shocked that she was picked first."
    kat "Very well. Who do you want, Killian?"
    scene w1_0090 with dissolve
    kil "Hm..."
    scene w1_0094 with dissolve
    kil "Veronica."
    scene w1_0095 with dissolve
    fel "Way to make a girl feel wanted."
    scene w1_0096 with dissolve
    kil "Oh, don't be like that, Felish. You and I know each other pretty well, that kind of thing is pretty hard to hide on film."
    kil "Plus some of the questions will be pretty personal and I know you hate that shit, so better not me, right?"
    scene w1_0097 with dissolve
    stop music fadeout 3.0
    fel "*sigh* Guess I'm with Kat then."
    jump w1DaliaIntro


label w1felinterviewpick:
    show screen textbox2 with dissolve
    scene w1_0088 with dissolve
    mc "I'll take Felicia."
    if feliciaSex == False:
        fel "Hehe, I knew you were regretting the other night."
    else:
        fel "Aw, I must've made a real impression the other night, right stud?"
    "Felicia was looking like the proverbial cat that swallowed the canary."
    kat "Very well. Who do you want, Killian?"
    scene w1_0090 with dissolve
    kil "Hm..."
    scene w1_0098 with dissolve
    kil "Her and I haven't had the pleasure of getting to know one another yet."
    scene w1_0099 with dissolve
    fel "Not satisfied until you've sampled the whole menu, eh?"
    fel "Poor, poor Mina."
    scene w1_0100 with dissolve
    kil "Hey, don't bring her into this. Makes me feel like I'm doing something bad."
    stop music fadeout 3.0
    kat "Looks like I'll be taking Rosalind then."
    jump w1DaliaIntro


label w1verointerviewpick:
    show screen textbox2 with dissolve
    scene w1_0089 with dissolve
    "I'll take Veronica."
    ver "I suppose that suits me. Better you than the old bat."
    "Despite her precarious position, Veronica never seems to miss the opportunity to lay into the woman holding the purse strings."
    kat "Very well. Who do you want, Killian?"
    scene w1_0090 with dissolve
    kil "Hm..."
    scene w1_0091 with dissolve
    fel "Way to make a girl feel wanted."
    scene w1_0092 with dissolve
    kil "Oh, don't be like that, Felish. You and I know each other pretty well, that kind of thing is pretty hard to hide on film."
    kil "Plus some of the questions will be pretty personal and I know you hate that shit. It'd be less embarrassing with a stranger, yeah?"
    stop music fadeout 3.0
    scene w1_0093 with dissolve
    fel "*sigh* Guess I'm with Kat then."
    jump w1DaliaIntro

label w1DaliaIntro:
    play sound "sound effects/door-openclose.wav"
    scene w1_0101 with dissolve
    "While Ian and Felicia conversed, Mrs. Pulman had made a short call. Not a minute later, a woman I vaguely recognized from the past few weeks entered."
    "If I recall correctly, she was handing a large sum of money to August the first time I saw her."
    play music "music/i-knew-a-guy.mp3"
    scene w1_0102 with dissolve
    kat "[mcf], have you met Dalia?"
    scene w1_0103 with dissolve

    if perk_socialButterfly == True:
        mc "No, I haven't had the pleasure."
    else:
        mc "Afraid not."

    scene w1_0104 with dissolve
    kat "She's one of our house girls. The head girl, actually."
    scene w1_0105 with dissolve
    hide screen textbox2 with dissolve
    menu:
        "Head girl?":
            show screen textbox2 with dissolve
            mc "What does the head house girl do around here?"
            scene w1_0104 with dissolve
            kat "Administrative things, on top of her regular duties. She handles cash, keeps tabs on the other girls, and let's me or August know if any problems come up when one of the girls make a house call."
            scene w1_0106 with dissolve
            kil "She means she snitches on the other girls when they do something bad or smooths things over when a member gets pissed about something."
            scene w1_0107 with dissolve
            "Dalia looked unhappy to hear it put so bluntly."

        "Nice to meet you, Dalia. [red]\[Toughness -1\]":
            $ toughness -= 1
            show screen textbox2 with dissolve
            scene w1_0108 with dissolve
            mc "Nice to meet you, Dalia. I'm [mcf]."
            scene w1_0109 with dissolve
            dal "Same to you."
            scene w1_0105 with dissolve
            if perk_socialButterfly == True:
                mct "(She seems like a woman of few words.)"
            if perk_socialChameleon == True:
                mct "(She seems like a woman that knows the value of brevity.)"
            else:
                mct "(She seems... cold.)"


    scene w1_0110 with dissolve
    play sound "sound effects/notification.wav"
    $ met_dalia = True
    show bioadd with dissolve
    kat "Would you be a dear and take Mr. [mcl] to our sound proof set? I'd get Warren to do it, but I let Auggy borrow him for his meeting with those money grubbing friends of his."
    kat "He doesn't quite know his way around the hidden parts of the building yet."
    dal "Yes, Mrs. Pulman."
    kat "Good! I'll be filming here. Ian can use Charles' office."
    scene w1_0111 with dissolve
    mc "Before I go, I'm not exactly clear on what I should specifically be doing or asking..."
    stop music fadeout 3.0
    scene w1_0112 with dissolve
    kat "Oh, I think you know. You've seen your share of cheap pornos, right? If you haven't, you can always call home and ask for advice."
    scene w1_0113 with dissolve
    "..."
    kil "Huh...? I don't get it."
    mc "...yeah, I think I know what you're expecting."
    if toughness >= 14:
        mct "(Bitch.)"
    scene w1_0114 with dissolve
    kat "Don't forget the camera."
    kat "Oh, and if you do a good job on this task, expect a {b}nice{/b}, mind-blowing reward in your future."
    kat "I like to reinforce excellence."
    dal "Right this way, Mr. [mcl]. If you'll follow me."
    "......"
    scene black with fade
    "..."

    if w1RoseGonzo == True:
        jump w1RoseInterview
    if w1FelGonzo == True:
        jump w1FelInterview
    if w1VeroGonzo == True:
        jump w1VeroInterview

################################################################################
## Rosalind Gonzo --------------------------------------------------------------
################################################################################

label w1RoseInterview:
    if _in_replay:
        show transitionrosalind02 with cmet
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
        "Does Rosalind refer to the player character as Sir?"
        hide screen textbox2 with dissolve
        menu:
            "Yes, sir!":
                $ prYesSir = True
            "No.":
                pass
        show screen textbox2 with dissolve

    play music "music/thief-in-the-night.mp3"
    scene w1_0115 with blinds
    "Dalia did what was asked of her, leading Rosalind and I through the inner-workings of the unoccupied office building part of the club, until we finally arrived at our destination: a studio set, replete with a photography backdrop."
    mct "(You got to be kidding me. There's no end to this place's amenities...)"
    dal "Here we are. I'm sure you remember how to get back? If there's not anything else..."
    scene w1_0116 with dissolve
    rose "Thank you."
    "Rosalind beamed warmly and thanked Dalia for her time. The seasoned prostitute must've found the earnest display odd for the setting, as she looked tongue tied for the briefest moment."
    scene w1_0117 with dissolve
    dal "Yeah. No problem, hun."
    scene w1_0118 with dissolve
    dal "Oh, and welcome to the club. If you ever need access to any of the house girls, let me know."
    dal "I take care of scheduling for that sort of thing."
    scene w1_0119 with dissolve
    "Without waiting for a response, Dalia turned on the heels of her feet and left Rosalind and I alone in the vacant studio."

    if perk_socialButterfly == True or perk_socialChameleon == True:
        mct "(She hides it well, but I can tell that woman is a ball of nervous energy.)"
    else:
        mct "(Dalia seems nice enough I guess, if not a little to the point.)"

    scene w1_0120 with fade
    "While I was lost in thought, Rosalind made her way to the nearby couch and sat down."

    if prYesSir == True:
        rose "I'm ready to get started when you are, sir."
    else:
        rose "I'm ready to get started when you are."

    scene w1_0121 with dissolve
    "Straight to business, just like the first night we met."
    hide screen textbox2 with dissolve
    menu:
        "Ask her what's the hurry. [gr]\[Rosalind +1\]":
            scene w1_0122 with dissolve
            $ Rosalind_Affection += 1
            show screen textbox2 with dissolve
            mc "You seem like you're in a hurry."
            scene w1_0123 with dissolve
            rose "It's not like {i}that{/i}, but..."
            "Rosalind pauses a moment, as if to consider how much information she wants to divulge."
            scene w1_0124 with dissolve
            rose "My daughter will be out of school soon and, if I can help it, I'd prefer get home early enough to cook and not spend the money on takeout."
            scene w1_0126 with dissolve
            stop music fadeout 2.0
            mc "Alright. Let's get to it then, I know how important a family meal is."
            rose "Thank you."

        "Tell her she's an eager slut. [red]\[Rosalind -1\]" if toughness >= 20:
            scene w1_0122 with dissolve
            $ Rosalind_Affection -= 1
            show screen textbox2 with dissolve
            mc "You're quite the eager slut, aren't you?"
            scene w1_0123 with dissolve
            rose "..."
            scene w1_0125 with dissolve
            rose "Heh, you know it! I'll be anything you want Mr. [mcl]."
            stop music fadeout 2.0
            scene w1_0126 with dissolve
            rose "So let's get started, shall we?"

        "She has a point. Let's move things along.":
            scene w1_0126 with dissolve
            show screen textbox2 with dissolve
            stop music fadeout 2.0
            "No sense in easing into why we're here."
            mct "(As awkward as this will be for me, it's hundred times worse for Rosalind.)"

    hide screen textbox2 with dissolve
    scene black with fade
    show screen camcorder
    mc "Will you please tell our members your name?"
    image camcorder = Movie(play="camcorder_movie.webm", mask="camcorder_mask.webm")
    scene w1_0127 with pixellate

    if toughness >= 20:
        "{i}Our{/i} members. Somehow, that phrasing came naturally to me. I must've grown used to this place when I wasn't looking."
    else:
        "{i}Our{/i} members. The words still sounded alien to me, but I AM apart of this I guess."

    play music "music/a-lost-map-of-a-heaven.mp3"
    scene w1_0128 with dissolve
    rose "Sure! I'm Rosalind Carter, one of your summer Carnations."
    "Without much couching, Rosalind volunteered her full name and an eerily earnest salutation to the camera."
    scene w1_0129 with dissolve
    mct "(This woman is either a hell of an actor or she's got nothing between her ears.)"
    "Okay. Her {b}name{/b}. That was easy enough place to start, but what's next?"
    "I'm supposed to be introducing her, like in a cheap porno..."
    hide screen camcorder with dissolve
    scene w1_0152 with pixellate
    show screen textbox2 with dissolve
    vic "I'm thirty one."
    "Suddenly, a mental script formed in my head."
    hide screen textbox2 with dissolve
    scene w1_0129 with pixellate
    show screen camcorder
    mc "How old are you, Rose?"
    scene w1_0130 with dissolve
    rose "I'm 36 years old."
    mc "That makes you the oldest in this year's exhibition, doesn't it?"
    scene w1_0131 with dissolve
    rose "That's right. I'm practically over the hill for this kind of thing, aren't I?"
    scene w1_0129 with dissolve
    "I'm not sure if she actually knew how old the other two were, but she rolled with it."

    if perk_socialButterfly == True:
        mc "You got to be kidding? You're practically in your prime."
        mc "If anything, age has done nothing but added to your allure."
    else:
        mc "Don't be silly. You're a good-looking woman and you know it."

    scene w1_0130 with dissolve
    rose "Thank you! That's nice of you to say, but I know how attractive my opponents are."
    scene w1_0132 with dissolve
    rose "I'll have to work hard if I want to win."
    mct "(She's playing this like a natural. I doubt even Felicia could do better.)"
    scene w1_0129 with dissolve
    mc "Speaking of competition, tell us why you're here. More specifically, what have you picked as your prize"
    "Veronica's here to save her failing business. Lucy was trying to get her kid into a prestigious school."
    scene w1_0133 with dissolve
    rose "I have some money problems I need help with."
    scene w1_0134 with dissolve
    "It was a flat, disimpassioned, and obvious admission. One that didn't give much insight into her situation, but answered the question."
    "I could try and pry deeper. I'm curious about it, plus I'm sure these old freaks get off at the exploitive nature of these games."

    menu:
        "Ask her what kind of money troubles and make her squirm. [gr]\[Toughness +1\] \[Gonzo +1\]":
            $ toughness += 1
            $ w1GonzoScore += 1
            mc "What kind of money problems?"
            scene w1_0135 with dissolve
            rose "Debts. Heavy, heavy debt."
            scene w1_0136 with dissolve
            jump w1RoseInterviewPushIt


        "Just move onto a more thrilling direction. [gr]\[Rosalind +1\]":
            $ Rosalind_Affection += 1
            "I'm sure the people who will watch this would enjoy seeing a big-titted beauty squirm a little, but her pleading expression seemed to be practically asking me to drop it."
            "A silent request I'm happy to oblige."
            jump w1RoseInterviewNiceStrip


label w1RoseInterviewPushIt:

    "Rosalind's body began to fidget at the disclosure. So she's drowning in debt?"
    "Considering where she sits, I suspect she doesn't have many alternative avenues to come up with the sum of money she needs."

    menu :
        "Spice up the footage by using her admission against her. [gr]\[Toughness +1\] \[Gonzo +1\] [red]\[Rosalind -1\]":
            $ toughness += 1
            $ Rosalind_Affection -= 1
            $ w1GonzoScore += 1
            mc "So that means you really need to win this thing, huh?"
            scene w1_0137 with dissolve
            rose "Uh-huh.."
            scene w1_0136 with dissolve
            mc "That means you'll do ANYTHING to win this week?"
            scene w1_0137 with dissolve
            rose "I w-will, absolutely..."
            scene w1_0136 with dissolve
            if toughness >= 22:
                mc "Prove it then. Take that stupid costume off and get those dumb cow tits out."
            else:
                mc "Prove it then. Take off your costume and give the camera a glimpse of those beautiful breasts of yours."

            scene w1_0138 with dissolve

            if prYesSir == True:
                rose "Right away, sir."
            else:
                rose "Right away, Mr. [mcl]."

            scene w1_0142 with fade
            "Rosalind was quick to do as I asked, freeing her bountiful mounds from the restrictive confines of that cheap rabbit costume."
            jump w1RoseInterviewContinue


        "She clearly doesn't want to talk about it, be nice and let it go.":
            scene w1_0134 with dissolve
            "I shouldn't go down this path any further. It's making me feel too skeevy."
            jump w1RoseInterviewNiceStrip


label w1RoseInterviewNiceStrip:

    mc "Now, why don't you..."
    hide screen camcorder with dissolve
    scene w1_0153 with pixellate
    show screen textbox2 with dissolve
    cm "Why don't you give our viewers a look at the goods?"
    scene w1_0156 with dissolve
    vic "Okay..."
    scene w1_0154 with dissolve
    "..."
    scene w1_0155 with dissolve
    cm "Wow! Those puppies are massive!"
    hide screen textbox2 with dissolve
    scene w1_0129 with pixellate
    show screen camcorder

    menu:
        "(Not so) Subtly ask her if she's comfortable. [gr]\[Gonzo +1\]":
            $ w1GonzoScore += 1
            mc "You comfortable in that getup, Rose? The costume is looking a little tight from this side of things."
            scene w1_0139 with dissolve
            rose "Mr. [mcl], you're not suggesting that's a bad thing, are you? My breasts crammed into this small--"
            scene w1_0140 with dissolve
            rose "Oh! You asking me to undress? You want to see my {i}large{/i} tits."
            scene w1_0141 with dissolve
            rose "I'm sure the other members do as well. I'm all~too happy to oblige."

        "Tell her to take her tits out.":
            mc "Why don't you give our members a look at the goods."
            scene w1_0139 with dissolve
            rose "I'd be happy to, Mr. [mcl]."

    scene w1_0143 with fade
    rose "Aaah! It sure is nice to let the girls breath."
    scene w1_0142 with dissolve


label w1RoseInterviewContinue:

    mc "--!" with hpunch
    "The sight of Rosalind's bare chest in its unimpeded glory had me speechless. "

    if history_voyeur == True:
        "Adding to the eroticism of the situation was the voyeuristic feeling of sitting behind the camera. The feeling of being a powerful, distant observer."

    "It was enough to make the words stick in my throat, creating a lull in the back-and-forth Rosalind and I had developed."
    "She must've sensed the momentum being sucked out of the conversation, as she got the interview back on track with her own titillating question."
    scene w1_0144 with dissolve
    rose "Well, what do you think? I hope your members don't find them too obscene or ugly."
    scene w1_0145 with dissolve
    rose "I always hated my breasts growing up. I was a tomboy and they got in the way."
    rose "Plus, they resulted in a lot of unwanted attention from the boys. The girls in my class hated me because of that. They called me a slut."
    scene w1_0146 with dissolve
    mc "...*ahem* Is that so?"

    menu:
        "Tell her the girls in her class weren't wrong. [gr]\[Toughness +1\] \[Gonzo +1\]":
            $ toughness += 1
            $ w1GonzoScore += 1
            mc "Considering where you sit, I guess they weren't too far off, were they?"
            mc "You ARE a slut."
            scene w1_0143 with dissolve
            rose "You're right. I'm a dirty woman, sitting here with her breasts out out..."
            scene w1_0147 with dissolve
            rose "That's something your members will soon see in person for themselves."

        "Tell her they were just jealous. [red]\[Toughness -1\]":
            $ toughness -= 1
            mc "Your breasts look wonderful. Your classmates were just jealous."
            scene w1_0148 with dissolve
            rose "...hehe--"

    scene w1_0142 with dissolve
    "Thanks to Rosalind's timely interjection, I found myself focused on the task at hand once more."
    mc "They look so soft."
    scene w1_0150 with dissolve
    rose "They are, but they're also sooooo heavy."
    scene roseGonzoBoobSqueeze with dissolve
    "Adding theatrical touch, Rosalind took her fat tits in the cups of her hands and began indelicately kneading them."
    rose "Can you picture just how full and swollen they were when I was breastf--"
    scene w1_0151 with dissolve
    stop music fadeout 1.5
    rose "ng..."
    "For the first time since I started rolling, Rosalind's manufactured veneer momentarily wore thin."
    "Judging by the way she stopped in her tracks, she had accidently brought up a topic she probably wanted to avoid."
    "Namely..."
    hide screen camcorder with dissolve
    scene w1_0157 with pixellate
    show screen textbox2 with dissolve
    play music "music/leaving-home.mp3"
    bm "I heard you had a kid. Is that true, M'am?"
    scene w1_0158 with dissolve
    vic "I don't... I don't want to talk about that..."
    scene w1_0159 with dissolve
    tm "Oh...? Looks like we got a bonafide MILF in our mitts!"
    tm "Tell us, how old is he? Did his dad run out or something?"
    scene w1_0160 with dissolve
    bm "Is that why you're doing porn part time? Hehe..."
    vic "T-that's not, ngg--"
    hide screen textbox2 with dissolve
    show screen camcorder
    scene w1_0148 with pixellate
    hide screen textbox2 with dissolve
    "The subject of motherhood... that's likely a sensitive topic for Rosalind and why wouldn't it be?"
    "Still, as I looked at the MILFY woman, breasts openly bared for the camera..."
    "A potent mixture of sadistic desire and guilt billowed up in me like a big ball of fire."
    hide screen camcorder with dissolve
    scene w1_0161 with pixellate
    show screen textbox2 with dissolve
    "Guilt over the vivid, probably imagined parallels my mind was drawing."
    scene w1_0171 with dissolve
    bm "Oh, man! This bitch is squeezing down so hard!"
    scene w1_0162 with fade
    tm "Haha, I knew she was a dirty slut! Sex-starved older women are the best--!"
    "Is she enduring this humiliation for the same reason my own mother did?"
    bm "Get ready for my ball-juice you stupid skank!"
    scene w1_0163 with pixellate
    mc "Tkh..."
    stop music fadeout 3.0
    scene w1_0164 with dissolve
    scene w1_0165 with dissolve
    scene w1_0164 with dissolve
    scene w1_0165 with dissolve
    scene w1_0166 with dissolve
    mct "(Damn this place and the thoughts it's putting in my head.)"
    scene w1_0167 with dissolve
    "A beautiful woman like Rosalind is sitting topless in front of me. Why don't I focus on that instead of digging up old skeletons?"
    scene w1_0168 with dissolve
    mc "We've seen what's on top. Let's get a look at what's on bottom."

    if toughness >=20:
        mc "Stand up, slut."
    else:
        mc "Stand up for us, Rose."

    play music "music/philly-crew.mp3"
    hide screen textbox2 with dissolve
    show screen camcorder
    scene w1_0169 with irisin:
        subpixel True
        yalign 1.0
        xalign 0.6
    "Doing as I asked, Rosalind stood up with a level expression carefully etched on her face."
    scene w1_0169:
        subpixel True
        yalign 1.0
        xalign 0.6
        linear 6 yalign 0.1
    "She oozed womanly charm, that's for sure. That high waisted bunny costume accentuated her broad, breedable hips wondefully."
    scene w1_0170 with dissolve
    mc "Turn around and give us a look at that huge ass of yours."
    scene w1_0172 with dissolve
    rose "My pleasure."
    scene w1_0173 with dissolve

    if prYesSir == True:
        rose "Is this to your satisfaction, sir."
    else:
        rose "Is this to your satisfaction, Mr. [mcl]?"

    mc "Perfect, actually."
    scene w1_0174 with dissolve
    rose "You don't think it's too big? I've always been self-conscious about my rear."
    mc "No, not for any one with a lick of taste."
    scene w1_0173 with dissolve
    rose "That makes me happy to hear. I hope the other members feel that way too."
    mc "I don't think you have anything to worry about, Rose."
    mct "(At least as far as being attractive goes. The stuff you're going to be subjected to this weekend however...)"

    if toughness >= 20:
        mc "Face forward."
    elif toughness >= 11:
        mc "You can turn back around now."
    else:
        mc "Turn back around, please."

    scene w1_0170 with dissolve
    stop music fadeout 3.0
    "Hmm... Mrs. Pulman did tell me to ask some dirty questions. I should probably do that unless I want to disappoint her."
    mc "Get down on your knees."
    scene w1_0175 with fade
    "Rosalind did as I asked, falling to her knees at a lightning speed."
    play music "music/beginning-of-conflict.mp3"
    "As she peered up at me with unsure eyes, I drew closer to her, taking care to frame the shot in a way that suggested Rosalind's complete subservience and submission."
    mct "(I mean, that's appropriate for this week's theme after all.)"
    "Any job worth doing is worth doing well."
    mc "I'm going to ask you some questions and I want you to be honest."
    scene w1_0176 with dissolve
    rose "Alright."
    scene w1_0175 with dissolve
    mct "(Plus, Kat did say they'd be a reward if I did a good job, so...)"
    mc "No, I mean it. I'm going to be asking you some pretty embarrassing stuff here."
    mc "You're going to not want to answer them, but you must. The people at home deserve your honest answers. Not only that, but they'll want excruciatingly lurid details."
    mc "Do you think you can handle that?"
    scene w1_0177 with dissolve
    rose "Ask away. It's not like I'm not here to do much, {i}much{/i} more."
    scene w1_0178 with dissolve

    if toughness >= 20:
        mc "Spoken like a true whore. I'm going to hold you to that."
    elif toughness >= 11:
        mc "Good girl, I'm going to hold you to that."
    else:
        mc "Alright, then let's begin."

    "A laundry list of illicit questions had begun to write itself in my mind. I shouldn't ask all of them though."

    if kat_polite == True:
        "Three of them should provide enough footage to keep Mrs. Pulman happy."
    else:
        "Three of them should provide enough footage to keep that old lady happy."

    hide screen qmenu with dissolve

    menu rosalindGonzoQuestions:
        "Ask her about this week's theme." if roseGonzoTheme == False:
            $ roseGonzoTheme = True
            $ gonzoQuestions += 1

            mc "You're aware what this week's theme is."
            scene w1_0180 with dissolve
            rose "Yes, it's {i}service{/i}."
            scene w1_0182 with dissolve
            mc "Are you experienced with that?"
            scene w1_0188 with dissolve
            rose "Uh..."
            mct "(I know I said to be honest, but that was for the camera. Just lie!)"
            scene w1_0177 with dissolve
            rose "Not really, maybe not as much as my opponents, but I'm.. eager!"
            scene w1_0178 with dissolve
            mc "You mean you haven't given a lot of blowjobs?"
            scene w1_0179 with dissolve
            rose "I mean, I'd give my husband one from time to time when he got extra pushy, just to shut him up..."
            scene w1_0175 with dissolve

            if gonzoQuestions < 3:
                mct "(Crap. I doubt the club's member base wants to hear something pitiful like that, I should pivot.)"
                jump rosalindGonzoQuestions
            if gonzoQuestions == 3:
                mct "(Crap. I doubt the club's member base wants to hear something pitiful like that.)"


        "[gr]Ask about her sexual experience." if roseGonzoExperience == False:
            $ roseGonzoExperience = True
            $ gonzoQuestions += 1
            $ w1GonzoScore += 1

            mc "When was the first time you had sex, Rose?"
            scene w1_0180 with dissolve
            rose "I was twenty, in college."
            scene w1_0182 with dissolve
            mc "That late? You must've been a late bloomer."
            scene w1_0176 with dissolve
            rose "More like I grew up in a strict, religious household. College was the first time I had freedom."
            scene w1_0182 with dissolve
            mc "In that case, how many men have you had sex with?"
            scene w1_0181 with dissolve
            rose "Four. A couple of boyfriends in college, a one-night stand -- which I learned wasn't for me -- and then my husband."
            scene w1_0182 with dissolve
            mc "You're 36 years-old and you've only slept with four people?"
            mct "(I bet the perverts of the club are going to love that.)"
            scene w1_0176 with dissolve
            rose "Is that a absurdly small number?"
            scene w1_0175 with dissolve
            mc "{b}Absurd{/b}? Maybe not, but from where you sit..."
            scene w1_0183 with dissolve
            rose "Hehe... I guess you're right."
            scene w1_0184 with dissolve
            rose "I'm sure this will be a HUGE learning experience for me."
            "Rosalind gave a devilish wink to the camera. I got to hand it to her, she's doing her best to appeal to the crowd."
            scene w1_0178 with dissolve

            if gonzoQuestions < 3:
                mct "(The idea of a sexually inexperienced married woman facing down the depravity of the club should garner some interest with the club's patrons. I should use this momentum and pivot to another question.)"
                jump rosalindGonzoQuestions
            if gonzoQuestions == 3:
                mct "(The idea of a sexually inexperienced married woman facing down the depravity of the club? Not a bad note to end the interview on I think.)"


        "[gr]Ask about her sexual fantasies." if roseGonzoFantasy == False:
            $ roseGonzoFantasy = True
            $ gonzoQuestions += 1
            $ w1GonzoScore += 1

            mc "Do you have any sexual fantasies? Fetishes?"
            scene w1_0179 with dissolve
            rose "Hmmm, I don't know..."
            mc "C'mon, you have to have at least one or two, right? Everybody does."
            scene w1_0176 with dissolve
            rose "Well... I do have a {b}few{/b}, but they're kind of embarrassing."
            scene w1_0175 with dissolve
            mc "Tell the camera about them. Be explicit."
            scene w1_0176 with dissolve
            rose "I always liked the idea of being tied up."
            scene w1_0175 with dissolve
            mc "The idea? You never tried it, you mean?"
            scene w1_0176 with dissolve
            rose "I did. Once. My first college boyfriend was open to trying it."
            scene w1_0185 with dissolve
            rose "It was nice, but it was just a simple pair of handcuffs. I always wanted to know what a rope would feel like."
            rose "To have it roughly bite into your flesh..."
            scene w1_0186 with dissolve
            rose "Hung from the ceiling, to helplessly dangle, dance, and writhe in embarrassment..."
            scene w1_0187 with dissolve
            mc "You've really given some thought about this."
            scene w1_0188 with dissolve
            rose "Maaaaybe."
            mc "Well, I'd almost guarantee you'll get your chance to explore that sometime over the next month."
            scene w1_0175 with dissolve

            if gonzoQuestions < 3:
                mct "(She ended up giving a genuine, honest response to the question and it showed. I should use this momentum and pivot to another question.)"
                jump rosalindGonzoQuestions
            if gonzoQuestions == 3:
                mct "(She ended up giving a genuine, honest response to the question and it showed. Not a bad note to end the interview on I think.)"


        "[gr]Ask about her favorite sexual positions." if roseGonzoPositions == False:
            $ roseGonzoPositions = True
            $ gonzoQuestions += 1
            $ w1GonzoScore += 1

            mc "What's your favorite position to screw in?"
            scene w1_0179 with dissolve
            rose "Uh... I've never really thought about it. My husband usually just fucked me from behind."
            scene w1_0175 with dissolve
            mc "I didn't ask you how your limp-dick husband fucked you, did I?"
            "The words escaped my mouth, propelled by a bewildering feeling of irritation."
            scene w1_0188 with dissolve
            rose "N-no, I guess you didn't."
            mc "How do you like to be fucked, Rosalind?"
            scene w1_0183 with dissolve
            rose "Ehehe... I like the idea of being folded in half, looking my partner in his eyes as he rails me slowly."
            mc "You said you hadn't thought about it."
            scene w1_0182 with dissolve

            if gonzoQuestions < 3:
                mct "(She ended up giving a genuine, honest response to the question and it showed. I should use this momentum and pivot to another question.)"
                jump rosalindGonzoQuestions
            if gonzoQuestions == 3:
                mct "(She ended up giving a genuine, honest response to the question and it showed. Not a bad note to end the interview on I think.)"


        "Ask about her taste in men." if roseGonzoTaste == False:
            $ roseGonzoTaste = True
            $ gonzoQuestions += 1

            mc "What kind of men do you like?"
            scene w1_0176 with dissolve
            rose "...nice ones?"
            scene w1_0175 with dissolve
            mc "No, I mean what kind of men are you sexually attracted to?"
            scene w1_0179 with dissolve
            rose "I like the strong, silent type...?"
            "She said it like it was a question."
            scene w1_0175 with dissolve

            if gonzoQuestions < 3:
                mct "(I should pivot. I don't think I'll get much more out of her on this topic.)"
                jump rosalindGonzoQuestions
            if gonzoQuestions == 3:
                mct "(I should end it here. I don't think I'll get much more out of her on this topic.)"

    show screen qmenu with dissolve
    stop music fadeout 3.0
    scene w1_0189 with fade
    mc "I think that should do it for the questions."

    if w1GonzoScore >= 4:
        $ w1RosalindScore + 1
        $ w1GonzoReward = True
        mct "(I got some pretty good footage. I don't see how Mrs. Pulman will be disappointed.)"
        mct "(Should be good enough for the reward she mentioned, though I'm not entirely sure it'll be something I want...)"

    rose "You think so?"

    if kat_polite == True:
        mc "Yeah, it's not like Mrs. Pulman gave me explicit instructions."
    else:
        mc  "Yeah, it's not like Kathleen gave me explicit instructions."

    mc "I do think we should end it all proper like, though."
    rose "What do you have in mind...?"
    mc "A display of gratitude. Rich people have an ego the size of the moon. It's got to come across genuine though, I'm sure most of them can spot a fake."
    rose "How do I do that?"
    mc "Well, I have an idea..."

    scene w1_0190 with fade
    play music "music/a-lost-map-of-a-heaven.mp3"
    mc "Alright, you can begin talking when you're ready."
    rose "..."
    scene w1_0192 with dissolve
    rose "From the bottom of my heart, I would like to thank the Carnation Club and its members for giving me the opportunity to clear my debt."
    rose "I may be inexperienced when it comes to this world, but I hope you find me to your satisfaction. Thank you and I look forward to meeting all of you."
    scene w1_0191 with dissolve
    "The busty mother prostrated herself before the camera, bringing her forehead all the way down to touch the carpet. The kowtowing was my idea, but Rosalind sold it beautifully with the skill of an actor."
    "I learned something about Rosalind today. She is a woman able to act without ego, tenaciously inching toward a goal."
    "In the face of Veronica's force-of-will approach and Felicia's sexual temerity, she might just be akin to a sturdy oak-tree weathering the storm."
    "She may just win this thing."
    $ renpy.end_replay()
    hide screen camcorder
    scene black with fade
    if not persistent.roseGonzoGallery:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.roseGonzoGallery = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)
    $ history_rosalind = "One of the three Carnations picked for the summer event, I chose her to film and interview for Mrs. Pulman's task. She surprised me with how easily she's able to play the role."
    $ history_felicia = "One of the three Carnations picked for the summer event, Mrs. Pulman ended up being the one who interviewed her."
    $ history_veronica = "One of the three Carnations picked for the summer event, Killian seemed quite keen to interview her for Mrs. Pulman's task."
    $ unread_rosalind = True
    $ unread_felicia = True
    $ unread_veronica = True
    play sound "sound effects/notification.wav"
    show bioupdate with dissolve
    $ renpy.pause(3, hard=True)
    jump w1HanaDateConfirm

################################################################################
## Felicia Gonzo ---------------------------------------------------------------
################################################################################

label w1FelInterview:
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

    play music "music/thief-in-the-night.mp3"
    scene w1_0193 with blinds
    "Dalia did what was asked of her, leading Felicia and I through the inner-workings of the unoccupied office building part of the club, until we finally arrived at our destination: a studio set, replete with a photography backdrop."
    mct "(You've got to be kidding me. There's no end to this place's amenities...)"
    dal "Here we are. You remember how to get back? If there's not anything else..."
    scene w1_0194 with dissolve
    fel "This place has all sorts of hidden surprises, huh?"
    fel "Please tell me it also has a fully staffed spa."
    scene w1_0195 with dissolve
    dal "...no, but it does have a steam room, a pool, and various baths."
    dal "Those are for the {i}members{/i} and {i}management{/i} though..."
    scene w1_0196 with dissolve
    fel "Hehe, so you're saying I need to be accompanied"
    scene w1_0197 with dissolve
    fel "I'm sure [mcf] wouldn't mind the thought of the two of us enjoying a sauna together."
    dal "Riiight, I'm going to go now."
    scene w1_0198 with dissolve
    dal "Welcome to the club, by the way. If you ever need access to any of the house girls, let me know."
    dal "I take care of scheduling for that sort of thing."
    scene w1_0199 with dissolve
    "Without waiting for a response, Dalia turned on the heels of her feet and left Felicia and I alone in the vacant studio."

    if perk_socialButterfly == True or perk_socialChameleon == True:
        mct "(She hides it well, but I can tell that woman is a ball of nervous energy.)"
    else:
        mct "(Dalia seems nice enough, I guess, if not a little to the point.)"

    scene w1_0200 with dissolve
    fel "She's got a great ass, eh?"
    "Felicia made an offhanded, crude comment in Dalia's wake. She sounds like Killian..."
    scene w1_0201 with dissolve
    mct "(Then again, she's here by choice, isn't she?)"
    scene w1_0202 with fade

    if kat_polite == True:
        mc "Alright, let's get started. Mrs. Pulman said to--"
    else:
        mc "Alright, let's get started. Kathleen said to--"

    "Jumping the gun, Felicia laid down on the leather couch, legs splayed in a provocative pose, one hands fingertips working an exposed nipple as her other hand pawed at her clothed nether region."
    scene w1_0203 with dissolve
    mc "Save some for the camera, will you?"
    fel "I'm just getting myself warmed up. It wouldn't do for me not to be at my best for my big {i}exposé{i}."
    "Felicia seemed to be genuinely enjoying the prospect of being on camera."
    mc "I don't think you'll have any trouble getting your engine sputtering. Put your tits away, we'll get to that once we start shooting."
    scene w1_0204 with dissolve
    fel "Yes sir, Mr. Serious-Videographer, sir."
    stop music fadeout 3.0
    mct "(This should be an interesting experience to say the least...)"
    scene black with fade
    mc "...okay, rolling."
    hide screen textbox2 with dissolve
    scene w1_0205 with pixellate
    show screen camcorder
    play music "music/romantic-motivation.mp3"
    mc "Tell our club members your name, please."

    if toughness >= 20:
        "{i}Our{/i} members. Somehow, that phrasing came naturally to me. I must've grown used to this place when I wasn't looking."
    else:
        "{i}Our{/i} members. The words still sounded alien to me, but I AM apart of this I guess."

    scene w1_0206 with dissolve
    fel "My name is Felicia Ford. I'm a 34 year-old housew--"
    scene w1_0207 with dissolve
    stop music
    play sound "sound effects/record-scratch.wav"
    mc "Cut!"
    hide screen camcorder
    scene w1_0208 with irisout
    show screen textbox2
    fel "What? Why?!"
    mc "You're getting ahead of yourself. Just answer the questions as they're asked, alright?"
    scene w1_0209 with dissolve
    fel "What difference does it make?"
    mct "(Truth be told, probably not much. Part of me just wants to get this done as quickly as possible and get home, but another part...)"
    "{i}A job worth doing is worth doing right{/i}. That ever-present compulsion to make what I endeavor perfect."
    "Even if it is just filming a dirty interview, there's propriety to these things. A take and give."
    scene w1_0210 with dissolve
    mc "It helps to make it feel like the people watching at home are the ones asking the questions."
    scene w1_0211 with dissolve
    fel "You sound like you've given this a lot of thought."
    scene w1_0210 with dissolve
    mc "....let's just say I know what works and start over."
    hide screen textbox2 with dissolve
    scene w1_0213 with pixellate
    show screen camcorder
    play music "music/romantic-motivation.mp3"
    mc "...okay, rolling."
    mc "Tell our club members your name, please."
    scene w1_0214 with dissolve
    fel "My name is Felicia Ford."
    scene w1_0213 with dissolve
    mc "And how old are you, Felicia?"
    scene w1_0214 with dissolve
    fel "I'm thirty four years old."
    scene w1_0213 with dissolve
    mc "You're a married woman, correct?"
    scene w1_0215 with dissolve
    fel "That's right. I've been married for eight years, to a... {i}dutiful{/i} man."
    scene w1_0213 with dissolve
    mc "If he's so wonderful, why are you here?"
    scene w1_0216 with dissolve
    fel "I didn't say wonderful, did I? Don't go putting words in my mouth. Still, a woman has her needs, doesn't she?"
    scene w1_0213 with dissolve
    mc "So you're saying you're entering the exhibition for fun?"
    scene w1_0217 with dissolve
    fel "It seemed like a good alternative to being bored."
    scene w1_0218 with dissolve
    scene w1_0219 with dissolve
    scene w1_0218 with dissolve
    scene w1_0219 with dissolve
    scene w1_0218 with dissolve
    mc "If you're just here for fun, do you have anything in mind for your prize?"
    scene w1_0217 with dissolve
    fel "Of course I do. Wouldn't be nearly as interesting if there wasn't some stake to it."
    scene w1_0220 with dissolve
    fel "Say, you mind if I get more comfortable? You've seen them before Mr. Cameraman, but all the dirty bastards watching haven't and I'm rather proud of my tits."
    scene w1_0221 with dissolve
    "I don't know if it's a subconscious thing or on purpose, but she's back to trying to lead the interview."
    mc "You're enthusiastic, aren't you?"
    scene w1_0220 with dissolve
    fel "I'm {b}{i}so{/i}{/b} excited to be here that I can hardly keep my clothes on."
    scene w1_0221 with dissolve
    "I'll give her that, Felicia is an extremely vibrant woman. If I just let her be herself, that might be enough to win her a good share of fans."
    "At the same time, slowing things down and trying to knock her off balance might produce some interesting results."
    hide screen textbox2 with dissolve

    menu:
        "Ask some questions first. [gr]\[Gonzo +2\] [red]\[Felicia -1\]":
            $ Felicia_Affection -= 1
            $ w1GonzoScore += 2
            jump w1FelInterviewBackFoot

        "Let Felicia be herself. [gr]\[Felicia +1\] \[Gonzo +1\]":
            $ Felicia_Affection += 1
            $ w1GonzoScore += 1
            "No point in asking her questions she has no interest in answering. Probably best just to jump into the T&A."
            mc "Well, if that's the case, don't let me stop you."
            jump w1FelInterviewTakeCharge


label w1FelInterviewBackFoot:

    scene w1_0222 with dissolve
    mc "Slow down. There's no reason we need to rush things."
    scene w1_0223 with dissolve
    fel "You're not going to feed me the {i}somethings are worth waiting for{/i} line are you?"
    scene w1_0224 with dissolve
    mc "...no."
    mct "(I {b}was{/b}.)"
    mc "I just think the people at home would probably like to get to know you a little better first."
    scene w1_0223 with dissolve
    fel "How's that?"
    scene w1_0224 with dissolve
    mc "A beautiful, wealthy married woman volunteering to participate in this kind of debauchery is pretty unusual."
    scene w1_0225 with dissolve
    fel "Not really. My story isn't so uncommon. Perhaps volunteering for a brothel is a bit extreme, but on the surface it's nothing worth talking about."
    scene w1_0226 with dissolve
    mc "Sure it is. Do you have any children?"
    scene w1_0227 with dissolve
    fel "Yeah, 2.5 of them to be exact. They came with the white picket fence."
    scene w1_0226 with dissolve
    mc "Okay, well where are you from, then?"
    scene w1_0228 with dissolve
    fel "*sigh* Alright, I suppose a little talking won't hurt."
    scene w1_0227 with dissolve
    fel "I'm from a small town. You wouldn't know it, but I got out fast."
    scene w1_0226 with dissolve
    mc "What made you want to leave?"
    scene w1_0227 with dissolve
    fel "If I didn't leave after high school, I would've never. Those kind of towns are like blackholes."
    scene w1_0228 with dissolve
    fel "I would've got knocked up by some asshole, raised some hick children, and locked into a humdrum life of mediocrity. A fourth of my graduating class became hairdresses. Those are the girls who made something of themselves too."
    scene w1_0227 with dissolve
    fel "No, I got out the hell out of there as soon as I was able. Went to college in the big city, before getting married and moving out here to Morehead Hills."
    scene w1_0226 with dissolve
    mc "What did you study in college?"
    scene w1_0225 with dissolve
    fel "What does it matter?"
    scene w1_0226 with dissolve
    mc "Well, educated women are sexy for one. I'm sure the people watching at home think so too."
    scene w1_0227 with dissolve
    fel "I was a psychology major, what else? It's a clichéd story, one I told you it wasn't worth talking about."
    scene w1_0226 with dissolve
    "She's quick to belittle her past, but honestly I kinda want to know more."
    "At the same time, I've succeeded in slowing Felicia down, I could always move things along."

    menu:
        "Ask more about her husband. [gr]\[Felicia +1\]":
            $ Felicia_Affection += 1
            mc "What does your husband do? You're fairly well off, right?"
            scene w1_0227 with dissolve
            fel "Let's just say, his portfolio is large enough that he would fit in well here."
            scene w1_0226 with dissolve
            mc "...he's not actually a member, right?"
            scene w1_0229 with dissolve
            fel "Pffthaha, no. No. No. No. He's too serious for a place like this. Though..."
            scene w1_0230 with dissolve
            fel "Who REALLY knows the secrets of another person's heart. No one in your life would expect to find you working at a brothel, would they?"
            fel "My husband, however? What a surprise that would be!"
            scene w1_0231 with dissolve




        "Ask more about her reason for being here. [gr]\[Gonzo +1\]":
            $ w1GonzoScore += 1
            mc "Are you really here because you're bored? Don't you think you're taking this too lightly?"

            if kat_polite == True:
                "I echoed Mrs. Pulman's words from earlier, an opinion I couldn't help but agree with considering what I witnessed Veronica go through."
            else:
                "I echoed Kathleen's words from earlier, an opinion I couldn't help but agree with considering what I witnessed Veronica go through."

            mct "(I mean, really? Does she have any idea what she's signed up for?)"
            scene w1_0229 with dissolve
            fel "Heheh, I'm eager to find that out! The way Kathy explained it made it sound {b}hardcore{/b}."
            scene w1_0232 with dissolve
            fel "Just want to say to the people at home, by the way of a little challenge..."
            fel "You better not disappoint me over the next month. You hear?"
            "It was an outrageously cartoonish declaration, but Felicia sold it authentically."
            scene w1_0231 with dissolve
            "That kind of boldness should drum up interest in her from the club's membership."



        "Move things along.":
            "Satisfied the ball was back in my court, I decided now was the time to move things along."


    if toughness >= 20:
        mc "Alright, I've heard enough. On your feet, slut."
    elif toughness >= 11:
        mc "Alright. On your feet."
    else:
        "Would you stand up, please?"

    scene w1_0233 with dissolve
    fel "Oooh~"
    mc "Lose the top."
    scene w1_0234 with dissolve
    fel "Yes, sir. {b}Finally{/b}."
    jump w1FelInterviewContinue


label w1FelInterviewTakeCharge:

    scene w1_0233 with dissolve
    "Felicia sprung off the couch like a caged animal being set free, setting to the task of freeing herself from her outfit."
    "Instead of a simply removing the leotard, she imbued a theatrical flare to the process."
    scene w1_0235 with dissolve
    "First, leaning forward to give the camera one long glimpse of her cleavage."
    scene w1_0236 with dissolve
    scene w1_0235 with dissolve
    scene w1_0236 with dissolve
    scene w1_0235 with dissolve
    "For added emphasis, she gave them a little squeeze with both hands."
    scene w1_0237 with dissolve
    "Satisfied the camera had got one last fleeting glance at her front, Felicia spun around with a dance-like levity and arched her back."
    scene w1_0238 with dissolve
    fel "Tell me, Mr. Cameraman..."
    fel "What do you think is my best side? My froooont or..."
    scene w1_0239 with dissolve
    scene w1_0240 with dissolve
    scene w1_0239 with dissolve
    scene w1_0240 with dissolve
    mc "..."
    scene w1_0238 with dissolve
    fel "Well?"
    scene w1_0237 with dissolve

    menu:

        "Tell her you love her tits the most":
            $ w1FelTits = True
            mc "I've always been a tit-man and with you it's no exception."
            mc "Not to say that your ass isn't practically a work of art."
            scene w1_0241 with dissolve
            fel "Hehehe, so you prefer tits, huh? I'll have to remember that piece of information for {b}later{/b}!"


        "Tell her you love her ass the most":
            $ w1FelAss = True
            "If you plucked me off the street, put a gun to my head, and asked: {b}tits{/b} or {i}ass{/i}?"
            "I would say I was firmly a tit-man, but..."
            "Staring down the barrel of her callipygian backside had made me a believer in the power of the almighty buttock."
            mc "Your ass is practically a work of art."
            mc "Not to say there's not a piece of you that isn't... you certainly care of yourself."
            scene w1_0241 with dissolve
            fel "Hehehe, so you prefer asses, huh? I'll have to remember that piece of information for {b}later{/b}!"


    scene w1_0242 with dissolve
    "Satisfied with my answer, Felicia turned back around."
    stop music fadeout 3.0
    fel "Well, I think it's time to get out of this stuffy thing."



label w1FelInterviewContinue:

    scene black with fade
    "Without delay, Felicia nimbly began to remove her leotard."
    play music "music/philly-crew.mp3"
    hide screen textbox2 with dissolve
    show screen camcorder
    scene w1_0243 with dissolve:
        subpixel True
        yalign 1.0
        xalign 0.6
    "It wasn't long until the bunny costume laid at her feet, Felicia striking a statuesque pose, putting her well-toned physique and sun-kissed breasts on proud display."
    scene w1_0243:
        subpixel True
        yalign 1.0
        xalign 0.6
        linear 6 yalign 0.1
    "The high-waisted net pantyhose contrasted beautifully with her bronze skin, leading all the way up to her flat stomach and pert, full breasts."
    "Felicia practically had the body of a goddess, with the confidence of one to match."
    scene w1_0244 with dissolve
    "The only thing conspicuously missing from the scene was accompanying fanfare."
    scene w1_0245 with dissolve
    fel "All right, Mr. DeMille, I'm ready for my close up."
    scene w1_0244 with dissolve
    "--!"
    if history_voyeur == True:
        "Adding to the eroticism of the situation was the voyeuristic feeling of sitting behind the camera. The feeling of being a powerful, distant observer."

    scene w1_0246 with dissolve
    fel "God, how I {b}love{/b} that look on your face. Like I'm a glass of water and you're a man dying of thirst in a desert."
    fel "You got such honest expressions, Mr. Cameraman. I could just jump you right now."
    scene w1_0244 with dissolve
    "Coming back to my sense, I was reminded that I needed to get back to the task at hand - namely, I'm filming a dirty interview."
    mc "I got a better idea. Why don't you spin around and give the camera a good look at your ass?"
    scene w1_0245 with dissolve
    fel "Hehe, you're the boss."
    scene w1_0248 with fade
    fel "This what you had in mind?"
    scene w1_0247 with dissolve
    mc "Beautiful."
    "She certainly had no sense of shame. She was bent over in such a way that her asshole was practically winking hello to me."
    "Hmm... Mrs. Pulman wanted me to ask some dirty questions. I should probably get to that."
    mc "Alright, you can turn back around."
    scene w1_0245 with fade
    fel "What now, boss?"
    scene w1_0244 with dissolve
    mc "Now you're going to get down on your knees and place your hands behind your head."
    scene w1_0249 with dissolve
    "Felicia shot me a mischievous look before doing exactly what I asked."
    scene w1_0250 with fade
    stop music fadeout 3.0
    fel "Like this?"
    scene w1_0251 with dissolve
    mc "No, straighten your back out."
    scene w1_0252 with dissolve
    "I decided to mimic what Kathleen had Veronica and Lucy do in her office the week I begun working for the club."
    scene w1_0253 with fade
    play music "music/beginning-of-conflict.mp3"
    "As she peered up at me with come hither eyes, I drew closer to her, taking care to frame the shot in a way that suggested Felicia's complete subservience and submission."
    mct "(I mean, that's appropriate for this week's theme after all...)"
    scene w1_0254 with dissolve
    fel "Mmmh... what now?"
    scene w1_0253 with dissolve
    mc "Now, I've got some questions for you and I want you to answer them truthfully."
    mct "(Plus, Kat did say they'd be a reward if I did a good job, so...)"
    scene w1_0255 with dissolve
    fel "Really? More questions?"
    scene w1_0256 with dissolve
    mc "Don't pout, they're the fun variety."
    scene w1_0254 with dissolve
    fel "Well, I like the sound of that. Ask away!"
    scene w1_0253 with dissolve
    "A laundry list of illicit questions had begun to write itself in my mind. I shouldn't ask all of them though."

    if kat_polite == True:
        "Three of them should provide enough footage to keep Mrs. Pulman happy."
    else:
        "Three of them should provide enough footage to keep that old lady happy."
    hide screen qmenu with dissolve
    menu feliciaGonzoQuestions:
        "[gr]Ask her about this week's theme." if felGonzoTheme == False:
            $ w1GonzoScore += 1
            $ gonzoQuestions += 1
            $ felGonzoTheme = True

            mc "You've been told what this week's theme is, right?"
            scene w1_0254 with dissolve
            fel "Yup, and lemme say, I'm going to win."
            scene w1_0253 with dissolve
            mc "You sound pretty damn confident. What makes you so sure?"
            scene w1_0257 with dissolve
            fel "C'mon... between me, that mousey fat-titted brunette, or that stuck-up gym freak redhead, who do you think will take it?"
            scene w1_0259 with dissolve
            fel "Not to brag, but I'm a cock-sucking queen."
            if prAfterParty == True and feliciaSex == True:
                scene w1_0212 with pixellate
                mct "(I can't dispute that, going from personal experience...)"
            scene w1_0254 with dissolve

            if gonzoQuestions < 3:
                mct "(She's pretty convincing. I should use this momentum and pivot to another question.)"
                jump feliciaGonzoQuestions
            if gonzoQuestions == 3:
                mct "(That was a great question to end Felicia's profile on.)"




        "[gr]Ask about her wildest sexual encounter." if felGonzoWildest == False:
            $ w1GonzoScore += 1
            $ gonzoQuestions += 1
            $ felGonzoWildest = True

            mc "What's the wildest thing you've ever done sexually?"
            if prAfterParty == True:
                "I recalled the night three weeks ago when we played that drinking game, where she answered this exact question for Mina."
                mct "(If she tells that one - about riding a Sybian machine in front a frat house of college students - it should make for some good footage.)"

            scene w1_0258 with dissolve
            fel "Hm..."
            "Felicia seemed to give it some genuine thought, like she had a rolodex of stories to scroll through and pick from."
            scene w1_0254 with dissolve
            fel "It's difficult to narrow it down, especially considering my audience and all the fun that undoubtedly goes on between these walls."
            scene w1_0253 with dissolve
            mc "Don't think too hard about it and just pick one. I know you have to have a few juicy ones."
            scene w1_0254 with dissolve
            fel "Alright, well... I guess you could say I developed an exhibition streak in college."
            scene w1_0259 with dissolve
            fel "There is something... {i}enchanting{/i} about holding the attention of an entire room, doubly so when you do it without even saying a word."
            scene w1_0254 with dissolve
            fel "I first developed a taste for it during my initiation into my college sorority, the {b}ALPHA KAPPA ZETAs{/b}."
            scene w1_0255 with dissolve
            fel "Those girls had a reputation for knowing how to have a good time, but naturally a poor girl like me from a podunk town had no chance of fitting in with those rich skanks."
            scene w1_0253 with dissolve
            mc "Why did you even want to join them in the first place if you were unwanted?"
            scene w1_0254 with dissolve
            fel "Precisely because it was filled with the kind of two-faced, snobby bitches who would turn their noses up at me."
            scene w1_0253 with dissolve
            mc "I don't get it."
            scene w1_0255 with dissolve
            fel "Hmm, well to put it another way... have you ever been looked down on? Told you couldn't do something because you weren't good enough? Didn't that make you want to do it {b}more{/b}?"
            scene w1_0253 with dissolve
            "I immediately recalled the first time I went on vacation with Ian's family. I recalled Ian's father mentioning my home situation to Ian's grandmother and the blinding anger I felt at the assumption she made about her character because she was a single mother."
            "From then forward, I made it a point to visit her alongside Ian whenever I could. Relishing in the knowledge that my presence, even if minor, brought her some degree of displeasure and bitterness."
            mct "(It's a petty and childish memory, but I suppose that's what Felicia's talking about.)"
            mc "...Yeah, I think I understand what you mean."
            scene w1_0254 with dissolve
            fel "Well, it was like that. I was hellbent on sticking my nose where it didn't belong."
            fel "Anyway, during pledge week, they said if I wanted to join I'd have to do something {i}daring{/i} during a mixer. They didn't tell me what exactly, but I knew they thought that whatever they had planned would make me give up."
            scene w1_0257 with dissolve
            fel "Knowing that, all it did was motivate me. I rode a Sybian machine in front of a room of probably 80 people and in the process learned a lot about myself that night."
            scene w1_0254 with dissolve
            fel "Under the hungry gaze of dozens of people, I came for first time in my life."
            scene w1_0259 with dissolve
            fel "I went on to be the sorority president in my senior year."
            scene w1_0253 with dissolve
            mct "(Shit.)"
            if prAfterParty == True:
                "She definitely left out all those details three weeks ago."

            if gonzoQuestions < 3:
                mct "(How am I going to follow that up with another question? Still, I should use this momentum and pivot.)"
                jump feliciaGonzoQuestions
            if gonzoQuestions == 3:
                mct "(That was a great question to end Felicia's profile on.)"




        "Ask about her taste in men." if felGonzoTaste == False:
            $ gonzoQuestions += 1
            $ felGonzoTaste = True

            mc "What kind of man do you prefer?"
            scene w1_0255 with dissolve
            fel "The {b}rich{/b} kind, but I'll settle for one that knows how to work a stick. Or his tongue..."
            scene w1_0256 with dissolve
            "The growing silence told me she was through answering the question."

            if gonzoQuestions < 3:
                mct "(I should've known she wouldn't be so picky. I should pivot to another question.)"
                jump feliciaGonzoQuestions
            if gonzoQuestions == 3:
                mct "(Well, that's quite a lame question to end the interview on.)"

        "[gr]Ask about her sex life with her husband." if felGonzoSexLife == False:
            $ w1GonzoScore += 1
            $ gonzoQuestions += 1
            $ felGonzoSexLife = True

            mc "How often do you have sex with your husband?"
            "I figured this kind of question should go over well with the club's perverts."
            scene w1_0257 with dissolve
            fel "Mr. Cameraman, that's an awful question to ask a girl you've got naked and on her knees."
            scene w1_0254 with dissolve
            fel "I bet you're hoping I will say we no sex at all and that's what's driven me to this immoral life of pleasure seeking... or something else trite like that, am I right?"
            scene w1_0253 with dissolve

            if toughness >= 20:
                mc "Just answer the question you mouthy slut."
            elif toughness >= 11:
                mc "Just answer the question, Felicia."
            else:
                mc "Answer the question, please."

            scene w1_0254 with dissolve
            fel "Well, you'd be partially right. My husband's not interested in having sex with me like he used to, but he still has his needs and every few months I'm the most conveniently nearby hole he can bend over the kitchen table and fuck. If the nanny isn't around, that is."
            scene w1_0253 with dissolve

            if gonzoQuestions < 3:
                mct "(Oddly enough, there's a distinct lack of animosity behind her words. Part of me wants to pry further, but I should pivot to another question.)"
                jump feliciaGonzoQuestions
            if gonzoQuestions == 3:
                mct "(Oddly enough, there's a distinct lack of animosity behind her words.)"



        "Ask about her favorite way to have sex." if felGonzoPosition == False:
               $ gonzoQuestions += 1
               $ felGonzoSexPosition = True

               mc "What's your favorite way to have sex?"
               scene w1_0254 with dissolve
               fel "With another person."
               scene w1_0253 with dissolve
               mc "You can be more specific than that."
               scene w1_0259 with dissolve
               fel "Sometimes with other {b}persons{/}...?"
               scene w1_0254 with dissolve
               fel "I'm not a picky gal."
               scene w1_0253 with dissolve

               if gonzoQuestions < 3:
                   mct "(Well, that was a bit of a dud question. I should pivot to another one.)"
                   jump feliciaGonzoQuestions
               if gonzoQuestions == 3:
                   mct "(Well, that was a bit of a dud to end the interview on.)"

    stop music fadeout 3.0
    show screen qmenu with dissolve
    scene w1_0189 with fade
    mc "I think that should do it for the questions."

    if w1GonzoScore >= 4:
        $ w1FeliciaScore + 1
        $ w1GonzoReward = True
        mct "(I got some pretty good footage. I don't see how Mrs. Pulman will be disappointed.)"
        mct "(Should be good enough for the reward she mentioned, though I'm not entirely sure it'll be something I want...)"

    fel "That's your call, boss man."

    if kat_polite == True:
        mc "Yeah, it's not like Mrs. Pulman gave me explicit instructions. I think we stop here."
    else:
        mc  "Yeah, it's not like Kathleen gave me explicit instructions. I think we stop here."

    mc "I do think we should end it all proper like, though."
    fel "Hehehe, I like the sound of that. What do you have in mind...?"
    mc "Hmmm, how about a display of finesse? If the idea is to get people to bet on you, what better way than a demonstration of your skills."
    fel "Is that you trying to coax a blowjob out of me, [mcf]?"
    mc "No! I have something else in mind..."
    scene black with fade
    mc "Alright, you can begin when you're ready."
    scene w1_0260 with dissolve
    fel "..."
    scene w1_0261 with dissolve
    play music "music/romantic-motivation.mp3"
    fel "To encourage all you perverts sitting at home to put all your money on me, I'd like to put on a lil' presentation."
    scene w1_0260 with dissolve
    $ renpy.pause(1.5, hard=True)
    scene w1_0262 with dissolve
    "After shooting the camera a challenging look, Felicia brought the gold-colored dildo up to her lips in one smooth motion and began to inch it down her throat."
    scene w1_0267 with dissolve
    "Inch."
    scene w1_0266 with dissolve
    "By inch."
    scene w1_0263 with dissolve
    "Until the forearm length toy was firmly lodged in her gullet."
    scene w1_0266 with dissolve
    scene w1_0267 with dissolve
    "She then painstakingly withdrew the dildo at the same pace, making a point show her throat was making no attempt at expelling the foreign object."
    scene w1_0263 with vpunch
    "--before slamming the dildo's large length back down her throat in one straight shot."
    scene w1_0266 with dissolve
    scene w1_0267 with dissolve
    "She repeated the motion once more, for emphasis."
    scene w1_0263 with vpunch
    "Not a hint of discomfort had spread across her face during the demonstration. It was like her throat could swallow a dick as well as it could suck down water or breathe."
    scene w1_0264 with dissolve
    "Not that I was surprised. It was my idea to end the tape with a display of Felicia's dick sucking prowess."
    scene w1_0265 with dissolve
    if prAfterParty == True and feliciaSex == True:
        "I had experienced it first hand, after all."
    fel "Hehe, ta~da! My throat can take a dick just as good as a pussy."
    scene w1_0261 with dissolve
    fel "With that said, please put your money on me this weekend. I promise not to let you down!"
    stop music fadeout 3.0
    hide screen camcorder
    scene black with fade
    "....."
    "..."
    $ renpy.end_replay()
    $ history_felicia = "One of the three Carnations picked for the summer event, I chose her to film and interview for Mrs. Pulman's task, a task she masterfully handled."
    $ history_rosalind = "One of the three Carnations picked for the summer event, Mrs. Pulman ended up being the one to interview her for her introduction video."
    $ history_veronica = "One of the three Carnations picked for the summer event, Killian seemed keen to interview her for Mrs. Pulman's task."
    $ unread_rosalind = True
    $ unread_felicia = True
    $ unread_veronica = True
    if not persistent.felGonzoGallery:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.felGonzoGallery = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)
    $ unread_felicia = True
    play sound "sound effects/notification.wav"
    show bioupdate with dissolve
    $ renpy.pause(3, hard=True)
    jump w1HanaDateConfirm




################################################################################
## Veronica Gonzo --------------------------------------------------------------
################################################################################

label w1VeroInterview:
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

    play music "music/thief-in-the-night.mp3"
    scene w1_0268 with blinds
    "Dalia did what was asked of her, leading Veronica and I through the inner-workings of the unoccupied office building part of the club, until we finally arrived at our destination: a studio set, replete with a photography backdrop."
    mct "(You've got to be kidding me. There's no end to this place's amenities...)"
    dal "Here we are. I'm sure you remember how to get back? If there's not anything else..."
    scene w1_0269 with dissolve
    ver "A photography studio? You gonna tell me this place has a gym too?"
    scene w1_0270 with dissolve
    dal "...it does, actually."
    scene w1_0271 with dissolve
    ver "Who knew all it took to run a successful gym was to fill it with prostitutes."
    "In a surprising move, Veronica made a joke at her own expense. I didn't even know the steely woman was capable of cracking a joke."
    scene w1_0270 with dissolve
    dal "It's mostly used by the house girls. Dr. Kohler wants us {i}fighting fit{/i} as he says. You're welcome to use it though."
    dal "Anyway, I'm going to go now."
    scene w1_0272 with dissolve
    dal "Welcome to the club, by the way. If you ever need access to any of the house girls, let me know."
    dal "I take care of scheduling for that sort of thing."
    scene w1_0273 with dissolve
    "Without waiting for a response, Dalia turned on the heels of her feet and left Veronica and I alone in the vacant studio."

    if perk_socialButterfly == True or perk_socialChameleon == True:
        mct "(She hides it well, but I can tell that woman is a ball of nervous energy. She comes off like she's running on fumes.)"
    else:
        mct "(Dalia seems nice enough, I guess, if not a little to the point.)"

    scene w1_0274 with dissolve
    ver "That woman's got the presence of a cat backed into a corner."
    scene w1_0275 with dissolve
    mc "You think so? How can you tell?"
    scene w1_0276 with dissolve
    ver "That's just my impression, and I'm usually pretty good at reading people."
    scene w1_0277 with dissolve
    ver "I have a pretty good idea how that old bat expects this to go."
    scene w1_0278 with dissolve
    ver "It's like one of those porno-casting things, yeah?"
    scene w1_0279 with dissolve
    mc "That's the way it sounded."
    scene w1_0281 with dissolve
    mc "I'll ask you some personal questions, ask you to undress... that kinda thing."
    scene w1_0282 with dissolve
    ver "Heh, well I guess I shouldn't complain. It's child's play when compared to what's coming this weekend."
    ver "How do you want me?"
    scene w1_0280 with dissolve
    "I was struck by how surprisingly cooperative Veronica was being. I was expecting much more griping and pushback."
    scene w1_0281 with dissolve
    mc "Just sit down and get comfortable."
    scene w1_0283 with fade
    mc "I have to say, you seem a lot more agreeable than the last time we worked together."
    scene w1_0284 with dissolve
    ver "Oh, you noticed, eh? Well, don't let it go to your head. It's not because I suddenly think you're a swell guy, but can you blame me for being on edge a couple of weeks ago?"
    ver "I was in the middle of some pretty harrowing shit and that was before that bitch had me guzzle down a bucket full of semen."
    scene w1_0286 with dissolve
    mc "Fair enough."
    scene w1_0284 with dissolve
    ver "Now I've had time to compartmentalize what I have to do. No point in making a thing like this difficult, is there?"
    scene w1_0283 with dissolve
    mc "Well I'm glad to hear that. I was worried how this might go."
    scene w1_0285 with dissolve
    ver "If that's the case, why did you pick me over that blonde bimbo and Rose?"
    scene w1_0283 with dissolve
    "Why {i}did{/i} I choose to work with Veronica?"

    menu:
        "Tell her it's because you like her. [gr]\[Veronica +2\]":
            $ Veronica_Affection += 2
            scene w1_0287 with dissolve
            mc "I suppose it's because I like you."
            scene w1_0284 with dissolve
            ver "You... like me? That's your reason?"
            scene w1_0286 with dissolve
            mc "Good as any, right? You seem like a fine person in a tight spot and I'd simply like to work with you."

        "Tell her it's because you find her attractive [gr]\[Veronica +1\]":
            $ Veronica_Affection += 1
            scene w1_0288 with dissolve
            mc "Well, I picked you because you're the most attractive of the three."
            scene w1_0284 with dissolve
            ver "You got to be kidding me. That's your reason?"
            scene w1_0286 with dissolve
            mc "Good as any, right? Not like I know any of you well enough to have anything else to go off of."

        "Play it cool and say you don't know.":
            scene w1_0286 with dissolve
            mc "Beats me. Not like I know any of you well enough to have a preference."

    scene w1_0285 with dissolve
    ver "Well, I'm not going to bitch and moan. Better to work with you rather than with that old bag or that handsy pretty boy."
    scene w1_0283 with dissolve
    mct "(I don't think she has to worry about Ian trying a sneak attack, considering he witnessed her bust the last guy's nose.)"
    mc "I'll make sure this is working then we can get started."
    stop music fadeout 3.0
    scene black with fade
    "..."
    mc "Okay, rolling..."
    hide screen textbox2 with dissolve
    show screen camcorder
    scene w1_0289 with pixellate
    play music "music/jack-the-lumberer.mp3"
    mc "Please tell our members your name."

    if toughness >= 20:
        "{i}Our{/i} members. Somehow, that phrasing came naturally to me. I must've grown used to this place when I wasn't looking."
    else:
        "{i}Our{/i} members. The words still sounded alien to me, but I AM apart of this I guess."

    scene w1_0290 with dissolve
    ver "I'm Veronica."
    scene w1_0289 with dissolve
    "Short and to the point."
    "Okay. Her {b}name{/b}. That was easy enough place to start, but what's next?"
    "I'm supposed to be introducing her, like a porno vid..."
    "A mental script began forming in my head."
    scene w1_0289 with dissolve
    mc "How old are you, Veronica?"
    scene w1_0290 with dissolve
    ver "I'm 32 years-old."
    scene w1_0289 with dissolve
    mc "And what's your reason for entering the summer exhibition?"
    scene w1_0290 with dissolve
    ver "I'm here to win some money."
    scene w1_0289 with dissolve
    "She's coming off pretty stilted here..."
    mc "What's the money for?"
    scene w1_0290 with dissolve
    stop music fadeout 3.0
    ver "For my business."
    hide screen camcorder
    scene w1_0291 with slideleft
    show screen textbox2 with dissolve
    mc "Okay, I'm going to cut here for a second."
    scene w1_0292 with dissolve
    play music "music/thief-in-the-night.mp3"
    ver "Why, what's the matter?"
    scene w1_0293 with dissolve
    mct "(How can I say this...?)"
    hide screen textbox2 with dissolve

    menu:
        "Tell her she needs to loosen up. [red]\[Toughness -1\]":
            $ toughness -= 1
            scene w1_0294 with dissolve
            show screen textbox2 with dissolve
            mc "You're coming off pretty stiff to the camera."
            mc "Do you think you can loosen up, a little?"

        "Tell her she's about as sexy as a piece of wood right now. [gr]\[Toughness +1\]":
            $ toughness += 1
            scene w1_0294 with dissolve
            show screen textbox2 with dissolve
            mc "Well, you're as stiff as a board right now and about as sexy as one too."
            mc "We need to loosen you up a little."

    scene w1_0292 with dissolve
    ver "How the hell do you expect me to do that?"
    scene w1_0295 with dissolve
    ver "It's not like I've ever done something like this before, plus I'm wearing this ridiculous costume with a camera pointed in my face."
    scene w1_0293 with dissolve
    "She makes a good point. All things considered, a normal person would be clamming up completely right about now. Still..."

    if kat_polite == True:
        mct "(Mrs. Pulman mentioned something about a reward if I did a good job, though it's not like I'm entirely sure I want whatever it'll be in place.)"
    else:
        mct "(Kathleen mentioned something about a reward if I did a good job, though it's not like I'm entirely sure I want whatever it'll be in place.)"

    "Still, {i}a job worth doing is worth doing right{/i}. At least that's what the compulsive urge in the pit of my stomach tells me."
    scene w1_0294 with dissolve
    mc "I've got an idea that might help, if you're open to it..."
    stop music fadeout 3.0
    scene w1_0293 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "[gr]Offer to give her a shoulder massage.":
            $ Veronica_Horniness += 1
            $ Veronica_Affection += 1
            jump w1VeroInterviewMassage
        "Offer to take your clothes off.":
            $ Veronica_Affection += 2
            $ w1VeronicaPCUndress = True
            jump w1VeroInterviewEqualize




label w1VeroInterviewMassage:

    play music "music/covert-affair.mp3"
    show screen textbox2 with dissolve
    "I recalled something I heard a few times during old episodes of {i}Inside the Actors Studio{/i} that my mother would always watch."
    "A quick, but firm shoulder and neck massage does miracles to loosen you up when you're feeling physically stiff."
    scene w1_0296 with dissolve
    mc "How about I give you a massage?"
    scene w1_0297 with dissolve
    ver "This isn't you making a pathetic move on me, is it?"
    scene w1_0296 with dissolve
    mc "Absolutely not. I just want you to relieve some tension before we begin shooting again."
    mc "Wouldn't hurt to put your best foot forward for the club's members, would it?"
    scene w1_0297 with dissolve
    ver "Yeah, cause that's something I really give a shit about."
    scene w1_0294 with dissolve
    mc "You should, shouldn't you? I mean, you're here for a reason, right? You want to {b}win{/b}."
    scene w1_0298 with dissolve
    ver "...damn, I hate that you're right about that."
    scene w1_0285 with dissolve
    ver "Alright, we'll try it your way. Get over here and give me a massage."
    scene w1_0299 with dissolve
    mc "Right away, M'aam."
    scene black with fade
    stop music fadeout 3.0
    mc "If you'll get comfortable..."
    scene w1_0305 with blinds
    play music "music/study-and-relax.mp3"
    "I positioned myself above Veronica and set to work kneading, rubbing, squeezing, caressing, prodding, nudging or whatever terms you might attribute to an amateur masseuse working purely on a combination of what he's seen on TV and instinct."
    scene w1_0306 with dissolve
    scene w1_0307 with dissolve
    "Veronica had tensed up when my fingertips met the nape of speckled neck, but gradually became more comfortable as I developed a feel for what I was doing."
    scene w1_0306 with dissolve
    scene w1_0307 with dissolve
    "My digits worked their way from her collar down to her broad shoulder, digging tentatively into the rigid surface of her trapezius muscles."
    scene w1_0306 with dissolve
    scene w1_0307 with dissolve
    mct "(She really is built like a rock.)"
    scene w1_0308 with dissolve
    ver "Mmmh... you're not actually half-bad at this."
    scene w1_0309 with dissolve
    mc "Beginner's luck I guess."
    scene w1_0310 with dissolve
    ver "Don't tell me you offered to give me a massage when you've never done one before?"
    scene w1_0311 with dissolve
    mc "Heh, I guess I just popped off the first solution that entered my mind."
    scene w1_0312 with dissolve
    ver "Mmmh, that's the spot. Right there!"
    scene w1_0313 with dissolve
    "I doubled my efforts precisely where she instructed."
    scene w1_0314 with dissolve
    ver "For you being new at this, you got some magical hands."
    scene w1_0315 with dissolve
    ver "I wonder what else you can do with those bad boys."
    scene w1_0316 with dissolve
    "She shot me an out-of-character, flirtatious look."
    mc "I, uh.. ehh..."
    scene w1_0317 with dissolve
    ver "Hahaha, I'm just fucking with you. You're not exactly my type."
    if kat_polite == True:
        "Right. With the way she handled Mrs. Pulman, it's probably safe to say she bats for the other team."
    else:
        "Right. With the way she handled Kathleen, it's probably safe to say she bats for the other team."
    scene w1_0318 with dissolve
    mct "(Although, I don't necessarily have confirmation on that...)"
    mct "(I probably shouldn't let her being a tad friendlier spin into a dumb male fantasy.)"
    scene w1_0319 with dissolve
    ver "Okay, I think I'm sufficiently been {i}loosened up{/i}."
    ver "Let's get this over with. I've got a meeting in a couple of hours."
    stop music fadeout 3.0
    scene w1_0320 with dissolve
    mc "Alright, I'll get the camera."
    scene black with fade
    "..."
    mc "Okay, we're rolling again."
    jump w1VeroInterviewContinue


label w1VeroInterviewEqualize:

    play music "music/covert-affair.mp3"
    show screen textbox2 with dissolve
    "I've always heard the solution to stage fright was to {i}picture your audience in their underwear{/i}."
    "It might sound asinine, but taking it literally might help to equalize the situation for Veronica."
    scene w1_0296 with dissolve
    mc "What if I took my clothes off?"
    "Veronica cocked an eyebrow and gave me a dubious look."
    scene w1_0297 with dissolve
    ver "How would YOU taking your clothes off help ME loosen up?"
    mct "(Okay, it {b}does{/b} sound stupid, but...)"
    scene w1_0296 with dissolve
    mc "Just hear me out. Wouldn't it be easier if you weren't the only one embarrassing yourself? If we're both undressed, we're on equal footing."
    scene w1_0284 with dissolve
    ver "Yeah, except you won't have a camera pointed at you."
    scene w1_0294 with dissolve
    mc "Well, I did say it's only an idea..."
    scene w1_0300 with dissolve
    ver "Hmmh..."
    scene w1_0301 with dissolve
    "She carefully considered my words before shrugging."
    scene w1_0297 with dissolve
    ver "It sounds stupid, but getting to turn the tables a little could be {i}fun{/i}... assuming you're not some pervert who gets off on taking his clothes off?"
    scene w1_0302 with dissolve
    mc "Heh, n-not at all, trust me!"
    "I said, with the full cadence and expression of a person who couldn't be trusted "
    scene w1_0288 with dissolve
    mc "Three weeks ago I'd find a dark hole to crawl into and die of embarrassment for even thinking about this scenario, but this place does funny things to people. Listen, I'm trying to be helpful here..."
    scene w1_0283 with dissolve
    ver "..."
    scene w1_0303 with dissolve
    ver "Alright, then. Go ahead."
    ver "{b}Strip for me{/b}, stringbean."
    scene w1_0304 with dissolve
    mc "Right away, M'aam."
    scene black with fade
    stop music fadeout 3.0
    "For some inexplicable and dubious reason, I quickly began to undress -- all the way down to my underwear, until a pile of clothes laid in an untidy pile at my feet."
    scene w1_0321 with blinds
    play music "music/love-or-lust.mp3"
    mc "Well, like what you see?"
    "I struck a triumphant pose and cracked an awkward joke."
    scene w1_0323 with dissolve
    ver "Not so fast. Don't you think you're forgetting something?"
    scene w1_0322 with dissolve
    ver "You said equal footing, but you still have a little ways to go."
    ver "C'mon, stringbean. Don't hold out on me. Show me the goods."
    scene w1_0321 with dissolve
    "I had only planned to go this far, but... well, fair's fair."
    scene w1_0324 with dissolve
    "Before my embarrassment could get the best of me, I quickly slid out of that thin piece of fabric that separated my modesty from the redheaded amazon's curious gaze and bared it all for my (hopefully) future film star."
    scene w1_0325 with dissolve
    ver "Hmmh..."
    scene w1_0326 with dissolve
    ver "Shit, you look ridiculous."
    scene w1_0327 with dissolve
    mc "--ggh!" with hpunch
    mct "(Is she trying to be hurtful?!)"
    scene w1_0328 with dissolve
    ver "You surprisingly have pretty good definition and tone to your physique, but..."
    ver "The combination of your boy like face and that python you're packing in between your legs is absurd."
    scene w1_0327 with dissolve
    mct "(Err...)"
    mc "Thanks."
    mct "(I think.)"
    scene w1_0328 with dissolve
    ver "Don't get a big--"
    scene w1_0329 with dissolve
    "Before finishing her sentence, Veronica made her move. With a lightning quick lurch, she snatched the camcorder from my hands."
    ver "--head about it."
    hide screen textbox2 with dissolve
    scene w1_0330 with slideup
    show screen camcorder
    ver "Now, tell the camera your name please."
    scene w1_0331 with dissolve
    "Looking down the lens of the camera, I could feel my face flush in embarrassment."
    "I stopped myself from reflexively attempting to get the camera back, stymied by the lighthearted expression spread across the typically dour woman's face."
    mct "(She seems to have relaxed some, which was the whole point of this.)"
    "Should I play along?"

    menu:
        "Humor the woman. [gr]\[Veronica +1\]":
            $ Veronica_Affection += 1
            "She's actually smiling for once, why would I want to go and fuck that up?"

        "Get the interview back on track. [red]\[Veronica -1\]":
            $ Veronica_Affection -= 1
            scene w1_0332 with dissolve
            mc "Yeah, yeah... let's get back to why we're here."
            scene w1_0333 with fade
            ver "Sounds good to me."
            scene black with fade
            "She handed the camcorder back to me."
            mc "Okay, we're rolling again..."
            jump w1VeroInterviewContinue

    scene w1_0332 with dissolve
    mc "Hi, I'm [mcf] [mcl] and I'm happy to be here."
    scene w1_0331 with dissolve
    ver "How old are you, [mcf]?"
    scene w1_0332 with dissolve
    mc "I turn 22 this week."
    scene w1_0331 with dissolve
    ver "Oh? Looks like we got some young meat for the {b}grinder{/b}."
    hide screen camcorder
    scene w1_0334 with fade
    show screen textbox2 with dissolve
    ver "...Pfft, here take the camera. I feel stupid."
    ver "I've got someplace I need to be in a couple of hours."
    scene black with fade
    stop music fadeout 3.0
    "She handed the camcorder back to me with a smile. Looks like a little levity had built a rapport between us."
    "I hope that'll get her to relax a little more for her profile."
    mc "Okay, we're rolling again..."


label w1VeroInterviewContinue:
    play music "music/jack-the-lumberer.mp3"
    hide screen textbox2 with dissolve
    scene w1_0335 with pixellate
    show screen camcorder
    mc "Tell the people at home your name, please."
    scene w1_0336 with dissolve
    ver "My name is Veronica."
    scene w1_0335 with dissolve
    mc "Veronica what?"
    scene w1_0336 with dissolve
    ver "{b}Lynch{/b}. Veronica Lynch."
    scene w1_0335 with dissolve
    mc "How old are you, Veronica Lynch?"
    scene w1_0336 with dissolve
    ver "I'm thirty two."
    scene w1_0335 with dissolve
    mc "That puts you as the youngest of the Carnations."
    scene w1_0337 with dissolve
    ver "I'm not really worried about the other two."
    scene w1_0335 with dissolve
    mc "Oh? You don't see them as your competition?"
    scene w1_0338 with dissolve
    ver "Rosalind's a nice gal and all, but it only takes one look at her to see that she's out of her depth."
    scene w1_0335 with dissolve
    mc "What about Felicia?"
    scene w1_0337 with dissolve
    ver "Her...? Like I'm worried about a rich airhead who has never had to worry about money in her life."
    scene w1_0335 with dissolve
    "Got to say, whether or not she's underestimating the other Carnations, this kind of bravado might make her popular with the club's patrons. This is going pretty good."
    mc "Why are you here exactly?"
    scene w1_0336 with dissolve
    ver "To win money to save my business."
    scene w1_0335 with dissolve
    mc "Well, since you're so confident, let's get a good look at you then."

    if toughness >=11:
        mc "Stand up."
    else:
        mc "Stand up, please."

    scene w1_0339 with fade:
        subpixel True
        yalign 1.0
        xalign 0.6
    "The redheaded amazon did as I asked, taking to her feet with a burst of energy."

    scene w1_0339:
        subpixel True
        yalign 1.0
        xalign 0.6
        linear 6 yalign 0.1

    "The difficulty getting her into frame really drove home just how tall a woman Veronica is. With heels, she easily stood a head taller than me."
    scene w1_0340 with dissolve
    "That's not to say that her size detracted from her feminine appeal. It was quite the opposite."
    "She had broad hips and large breasts fitting for her stature, which created a unique contrast when compared to her absurdly defined six-pack and bulging arms."
    mc "Hey, say..."
    "It was a dichotomy I wanted to explore further."
    mc "I want to see you with your hair down."
    scene w1_0341 with dissolve
    ver "It's your show."
    scene w1_0342 with dissolve
    "With a concise motion, Veronica reached behind her head and removed the hair tie keeping her ponytail afloat."
    scene w1_0343 with dissolve
    "All at once, a cascade of fiery locks messily snaked down the amazon's shoulders and back, only to be rearranged by a vigorous headshake and tousling."
    mct "(Damn...)"
    "She looked like a warrior goddess, a flaming mane of luxurious hair accentuating her more fierce features. The only thing hampering that impression is that pesky costume..."
    mc "Let's get you out of that silly bunny costume. Lose all of it: the leotard and fishnets."
    scene w1_0344 with dissolve
    "Wordlessly she began to undress, setting to the task without any sense of panache. She may have a lot of confidence she'll win the exhibition, but the tepid half-hearted display would suggest otherwise."
    scene black with fade

    if kat_polite == True:
        "Then again, like Mrs. Pulman said, that kind of attitude has its own distinct charm."
    else:
        "Then again, like Kathleen said, that kind of attitude has its own distinct charm."

    scene w1_0345 with dissolve
    mc "--!"
    "Even though I've been inundated with the nude female form these past few weeks, I still couldn't help that breathless feeling coming over me at seeing Veronica's nude form in it's unimpeded glory."

    if history_voyeur == True:
        "Adding to the eroticism of the situation was the voyeuristic feeling of sitting behind the camera. The feeling of being a powerful, distant observer."

    scene w1_0346 with dissolve
    ver "You're starting to drool, stringbean."
    scene w1_0347 with dissolve
    ver "Although, I guess I do work hard for this body. Guess I can't blame you for using your peepers."

    if  w1VeronicaPCUndress == True:
        scene w1_0348 with dissolve
        ver "I can tell you're enjoying the view."
        "Veronica eyeline wandered down to my crotch..."
        "{i}Right{/i}. I had been so focused on her that I had forgot - I was nude and now she was eyeing my fully exposed, erect cock with a cocksure expression."

    scene w1_0349 with dissolve
    mct "(On second thought... maybe she isn't so tepid when it comes to this stuff.)"
    "I should get the ball rolling again on the interview, so let's..."

    menu:
        "Ask Veronica to demo her derriere. [gr]\[Gonzo +1\]":
            $ w1GonzoScore += 1
            "If she's so proud of her muscles, lets get a closer look at those glutes!"
        "Move onto the dirty questions.":
            "Let's wrap things up with some dirty questions."
            jump w1VeroInterviewContinue2

    mc "Give the camera a spin and let's get a look at your back."
    scene w1_0350 with dissolve
    ver "Is this what you want?"
    scene w1_0351 with dissolve
    "Veronica's got a fine ass, well-sculpted from a strenuous workout regime no doubt. I bet that thing has little to no give!"
    "Part of me wants to investigate that hypothesis..."

    menu:
        "Tell her that's perfect.":
            mc "Perfect, actually. Turn back around now."
            mc "We're going to move onto some dirty questions now."
            jump w1VeroInterviewContinue2

        "Get her to bend over even further. For science. [gr]\[Gonzo +1\]":
            $ w1GonzoScore += 1
            mc "Actually, could you bend over some more? Place you hands flat on the couch and really stick your butt out."

    stop music fadeout 3.0
    if  w1VeronicaPCUndress == True:
        hide screen camcorder with dissolve
        scene w1_0353 with irisout
        show screen textbox2 with dissolve
        ver "*sigh* This good?"

        if toughness >= 20:
            mc "Great, just keep that huge ass up in the air for a bit longer."
        else:
            mc "You got it. Just hold that position a little longer."

        play music "music/sneaky-snitch.mp3"
        "Just seeing her flared hips and taut ass buoyantly dangling in the air..."
        "How could I resist giving it a little smack?"
        scene pr1499 with pixellate
        mct "(Wait, is this really such a good idea?)"
        scene w1_0353 with pixellate
        hide screen textbox2 with dissolve

        menu:
            "Throw caution to the wind. Do what needs to be done! [gr]\[Gonzo +1\]":
                $ w1GonzoScore += 1
                $ Veronica_Affection -= 1
                $ Veronica_Horniness += 1
                scene w1_0355 with dissolve
                show screen textbox2 with dissolve
                mct "(I've come too far to back out now!)"

            "Disengage. It's too risky!":
                show screen textbox2 with dissolve
                "On second thought, I don't want to explain a busted nose to my mother."
                "I should just move the interview along."
                mc "Alright, you can turn back around."
                jump w1VeroInterviewContinue2

        play sound "sound effects/slap2.wav"
        scene w1_0357 with dissolve
        "*SMACK!*"
        "Disregarding the dangers, I stifled my sense of preservation and gave Veronica's ass a nice, solid smack. Nothing too hard of course, but with enough strength to discern its mettle. And as expected..."
        scene w1_0359 with dissolve
        ver "Ah! What the fu-"
        "It barely moved. This is an A+ ass, that's for sure."
        ver "Ghh... could've gave me some warning."
        mc "Sorry, I just couldn't help myself there. Like you said, you worked hard for your body....heh."
        scene w1_0353 with dissolve
        ver "Riiiight..."
        stop music fadeout 3.0
        mc "I think it's time we move onto some more questions though."
        mc "Alright, you can turn back around. I'm going to ask you some dirty questions now and I want you to answer truthfully."

    else:
        hide screen camcorder with dissolve
        scene w1_0352 with irisout
        show screen textbox2 with dissolve
        ver "*sigh* This good?"

        if toughness >= 20:
            mc "Great, just keep that huge ass up in the air for a bit longer."
        else:
            mc "You got it. Just hold that position a little longer."

        "Just seeing her flared hips and taut ass buoyantly dangling in the air..."
        "How could I resist giving it a little smack?"
        scene pr1499 with pixellate
        "Suddenly I remembered the last time Veronica was taken by surprise..."
        "Wait, is this really such a good idea?"
        scene w1_0352 with pixellate
        hide screen textbox2 with dissolve

        menu:
            "Throw caution to the wind. Do what needs to be done! [gr]\[Gonzo +1\]":
                $ w1GonzoScore += 1
                $ Veronica_Affection -= 1
                $ Veronica_Horniness += 1
                scene w1_0354 with dissolve
                show screen textbox2 with dissolve
                mct "(I've come to far to back out now!)"

            "Disengage. It's too risky!":
                show screen textbox2 with dissolve
                "On second thought, I don't want to explain a busted nose to my mother."
                "I should just move the interview along."
                mc "Alright, you can turn back around. I'm going to ask you some dirty questions now and I want you to answer truthfully."
                jump w1VeroInterviewContinue2

        play sound "sound effects/slap2.wav"
        scene w1_0356 with dissolve
        "*SMACK!*"
        "Disregarding the dangers, I stifled my sense of preservation and gave Veronica's ass a nice, solid smack. Nothing too hard of course, but with enough strength to discern it's mettle. And as expected..."
        scene w1_0358 with dissolve
        ver "Ah! What the fu-"
        "It barely moved. This is an A+ ass, that's for sure."
        ver "Ghh... could've gave me some warning."
        mc "Sorry, I just couldn't help myself there. Like you said, you worked hard for your body....heh."
        scene w1_0352 with dissolve
        ver "Riiiight..."
        stop music fadeout 3.0
        mc "I think it's time we move onto some more questions though."
        mc "Alright, you can turn back around. I'm going to ask you some dirty questions now and I want you to answer truthfully."



label w1VeroInterviewContinue2:

    scene black with fade

    if toughness >= 15:
        mc "Alright, on your knees."
    else:
        mc "Get low on the ground, all right?"

    play music "music/beginning-of-conflict.mp3"
    hide screen textbox2 with dissolve
    show screen camcorder
    scene w1_0361 with dissolve
    "As she peered up at me with come hither eyes, I drew closer to her, taking care to frame the shot in a way that suggested Veronica's complete subservience and submissions."
    mct "(I mean, that's fitting for this week's theme, right?)"
    "A laundry list of illicit questions had begun to write itself in my mind. I shouldn't ask all of them though."

    if kat_polite == True:
        "Three of them should provide enough footage to keep Mrs. Pulman happy."
    else:
        "Three of them should provide enough footage to keep that old lady happy."

    hide screen qmenu

    menu veronicaGonzoQuestions:

        "Ask her about this week's theme." if veroGonzoTheme == False:
            $ veroGonzoTheme = True
            $ gonzoQuestions += 1
            mc "How do you feel about this week's theme? You've been informed what it is, right?"
            scene w1_0363 with dissolve
            ver "It really doesn't matter what it is. I just got to do what that crazy old lady says."
            scene w1_0361 with dissolve
            mc "Veronica the pragmatist, huh?"
            scene w1_0365 with dissolve
            ver "That's one way of putting it, if you're feeling kind."
            scene w1_0361 with dissolve
            mc "You have a lot of experience sucking dick?"
            scene w1_0362 with dissolve
            ver "Probably less than average I imagine. It hasn't ever really been my thing."
            scene w1_0366 with dissolve
            "The growing silence suggested she was done talking."
            scene w1_0361 with dissolve

            if gonzoQuestions < 3:
                mct "(Eeeh, she's not giving me much here. I should pivot to another question.)"
                jump veronicaGonzoQuestions
            if gonzoQuestions == 3:
                mct "(Maybe not the biggest bang to end Veronica's profile on...)"

        "Ask about her sexual experience." if veroGonzoExperience == False:
            $ veroGonzoExperience = True
            $ gonzoQuestions += 1
            mc "Tell me about your sexual experience. How often do you have sex?"
            scene w1_0363 with dissolve
            ver "Not as much as I'd like, to be honest."
            scene w1_0361 with dissolve
            mc "That's not really an answer to the question."
            scene w1_0370 with dissolve
            ver "Sure it is, just a vague one."
            scene w1_0361 with dissolve
            mct "(She really has no refinement for this kind of thing...)"
            scene w1_0362 with dissolve
            ver "Sorry. You're right. It probably averages about once a month. Sometime twice, depending on how stressed I get."
            scene w1_0361 with dissolve
            mc "Who do you have sex with?"
            scene w1_0362 with dissolve
            ver "People at bars. Anyone who's bold enough not to be intimidated by a woman like myself."
            scene w1_0368 with dissolve
            if toughness <= 13:
                mct "(That must get pretty lonely...)"
            mc "So just casual encounters then?"
            scene w1_0362 with dissolve
            ver "Pretty much. I don't really have time for anything serious."
            scene w1_0368 with dissolve

            if gonzoQuestions < 3:
                mct "(Her matter of factness here isn't making for a sexy interview. I should pivot to another question.)"
                jump veronicaGonzoQuestions
            if gonzoQuestions == 3:
                mct "(Maybe not the biggest bang to end Veronica's profile on...)"

        "Ask about her sexual fantasies. [gr]\[Gonzo +1\]" if veroGonzoFantasy == False:
            $ veroGonzoFantasy = True
            $ gonzoQuestions += 1
            $ w1GonzoScore += 1
            mc "What's your dirtiest sexual fantasy or fetish?"
            scene w1_0366 with dissolve
            ver "Hm..."
            "She seems to be seriously considering it."
            scene w1_0367 with dissolve
            ver "It's kinda weird..."
            mct "(Wait a minute, is she blushing?!)"
            mc "What is it? C'mon, tell the camera."
            scene w1_0369 with dissolve
            ver "I like... {i}smells{/i}. You know like body odor and sweat."
            ver "That's the thing that turns me on the most."
            scene w1_0361 with dissolve
            mc "That's... interesting. Does that mean owning a gym gets you going?"
            mc "You ever find a closet to jill off in after a personal training session?"
            scene w1_0370 with dissolve
            ver "Of course not! I can't say I don't get horny after a goodwork out though."
            scene w1_0361 with dissolve

            if gonzoQuestions < 3:
                mct "(Wow! She was surprisingly frank with that question)"
                mct "(I should use this momentum and pivot to another question.)"
                jump veronicaGonzoQuestions
            if gonzoQuestions == 3:
                mct "(That was a pretty good question to end Veronica's profile on.)"

        "Ask about her taste in men. [gr]\[Gonzo +1\]" if veroGonzoTaste == False:
            $ veroGonzoTaste = True
            $ gonzoQuestions += 1
            $ w1GonzoScore += 1

            if kat_polite == True:
                "There's a question that came up when she picked Mrs. Pulman as her partner two weeks ago... {i}Veronica's taste in men{/i}. Namely, if she has any."
            else:
                "There's a question that came up when she picked Kathleen as her partner two weeks ago... {i}Veronica's taste in men{/i}. Namely, if she has any."

            mc "Talk about your taste in men. Who's your ideal partner?"
            scene w1_0365 with dissolve
            ver "I like the cute, {i}girly{/i} kind of men. Coincidently, that's also how I like my women."
            scene w1_0361 with dissolve
            mc "So, you're a bisexual then?"
            scene w1_0370 with dissolve
            ver "Sure, though I don't really think too much about it."
            scene w1_0365 with dissolve
            ver "I care more about my partner's appearance rather than what they've got under the hood."
            scene w1_0361 with dissolve
            mc "So anyone who's cute?"
            scene w1_0364 with dissolve
            ver "Nothing better than riding a dainty looking guy's face until it's gasping for air I say."
            ver "Plus, cute people make the ugliest faces when they cum."
            scene w1_0370 with dissolve
            ver "A fat slob blowing his load will look like a fat slob, no matter how twisted his face gets. A cute face however, provides that right kind of contrast."
            scene w1_0361 with dissolve
            mct "(...jeez. Who internalizes something like that?)"
            scene w1_0360 with dissolve
            mct "(Her for starters, I guess.)"
            scene w1_0365 with dissolve
            ver "Does that satisfactorily answer your question?"
            scene w1_0361 with dissolve
            mc "It certainly does."

            if gonzoQuestions < 3:
                mct "(Damn, I honestly didn't expect Veronica to be such a freak. I should use this momentum and pivot to another question.)"
                jump veronicaGonzoQuestions
            if gonzoQuestions == 3:
                mct "(That was a pretty hot way to end Veronica's profile on.)"


        "Ask about her relationship status." if veroGonzoRelationship == False:
            $ veroGonzoRelationship = True
            $ gonzoQuestions += 1
            mc "I recalled a piece of information I read a couple of weeks ago."
            mc "Your application said you're divorced?"
            scene w1_0363 with dissolve
            ver "...yeah, happily divorced. The institution of marriage is a crock of shit as far as I'm concerned."
            scene w1_0361 with dissolve
            mc "What kind of person was your...?"
            scene w1_0363 with dissolve
            ver "{b}Wife{/b}."
            scene w1_0365 with dissolve
            ver "She was a kind woman. Vibrant. Loved animals."
            scene w1_0370 with dissolve
            ver "Never got angry or raised her voice. It was fucking infuriating to be honest."
            scene w1_0361 with dissolve
            "She's being strangely candid here. Guess it isn't a sore spot for her."
            mc "Sounds like you have a good opinion of your ex."
            scene w1_0363 with dissolve
            ver "I do. Is that odd?"
            scene w1_0361 with dissolve
            mc "You know, I don't actually know..."
            mct "(I've only ever been through one serious breakup.)"
            mc "My gut says yes."
            scene w1_0366 with dissolve
            ver "..."
            scene w1_0362 with dissolve
            ver "Not everyone shares equal blame when things go south in a relationship. Sometimes no one's at fault. Other times, it rests solely on the back of one partner."
            scene w1_0368 with dissolve
            mc "Well, what was it in your case then?"
            scene w1_0370 with dissolve
            ver "What does this have to do with any of this? Shouldn't you be asking me about how many golf balls I can fit in my ass or something?"
            scene w1_0368 with dissolve

            if gonzoQuestions < 3:
                mct "(Shit, she's right. This is an unsexy line of questioning. I should pivot to another question.)"
                jump veronicaGonzoQuestions
            if gonzoQuestions == 3:
                mct "(Shit, she's right. This is an unsexy line of questioning to end the interview on...)"
    stop music fadeout 3.0
    show screen qmenu with dissolve
    scene w1_0189 with dissolve
    mc "I think that should do it for the questions."

    if w1GonzoScore >= 4:
        $ w1VeronicaScore + 1
        $ w1GonzoReward = True
        mct "(I got some pretty good footage. I don't see how Mrs. Pulman will be disappointed.)"
        mct "(Should be good enough for the reward she mentioned, though I'm not entirely sure it'll be something I want...)"


    ver "Good. My tits are getting cold just kneeling here."
    mc "I do think we should end it all proper like, though."
    ver "Of course you do. What do you want me to do?"
    mc "Well..."
    hide screen camcorder with dissolve
    scene black with fade
    show screen textbox2 with dissolve
    mc "You seem pretty flexible, right?"
    hide screen textbox2 with dissolve
    show screen camcorder
    scene w1_0371 with dissolve
    play music "music/jack-the-lumberer.mp3"
    mc "Ready when you are."
    scene w1_0372 with dissolve
    "Given the go ahead, Veronica began to stretch a protracted leg toward her core."
    scene w1_0373 with dissolve
    "A display of finesse that left that wet the viewer's imagination... at least, that's what I had in mind when I suggested it."
    scene w1_0374 with dissolve
    "Eventually her long, thick leg was pulled flush against her torso in an impressive display of elasticity."
    "I was honestly a little shocked that a woman so tall could be that flexible."
    scene w1_0375 with dissolve
    ver "How's that? Just imagine all the OTHER ways I can bend."
    ver "Don't forget to put your money on me this weekend, alright?"
    stop music fadeout 3.0
    hide screen camcorder with dissolve
    scene black with fade
    show screen textbox2 with dissolve
    "While Veronica may not have the sexual temerity of Felicia or Rosalind's soft femininity, she does have her opponents beat when it comes to willpower."
    "That's my limited take for the upcoming challenge."
    $ renpy.end_replay()
    if not persistent.veroGonzoGallery:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.veroGonzoGallery = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)

    $ history_veronica = "One of the three Carnations picked for the summer event, I chose her to film and interview for Mrs. Pulman's task, a task she wasn't really suited for, but gave me a chance to get to know her better."
    $ history_rosalind = "One of the three Carnations picked for the summer event, Killian opted to work with her after I picked to film Veronica for her introduction video."
    $ history_felicia = "One of the three Carnations picked for the summer event, she ended up being interviewed by Mrs. Pulman for her introduction video."
    $ unread_veronica = True
    $ unread_rosalind = True
    $ unread_felicia = True
    play sound "sound effects/notification.wav"
    show bioupdate with dissolve
    $ renpy.pause(3, hard=True)
    jump w1HanaDateConfirm


## Hana Flag Week 1 Flag -------------------------------------------------------

label w1HanaDateConfirm:

    play music "music/lobby-time.mp3"
    scene w1_0377 with blinds
    hana "Yo, hold up new guy."
    "On my way back to Kathleen's office to deliver the footage, I was stopped by a certain irreverent bartender."
    scene w1_0378 with dissolve
    hana "Coming back from digging up graves or whatever that soul-sucking crypt keeper has you doing?"
    scene w1_0379 with dissolve
    mc "Something like that."
    scene w1_0380 with dissolve
    hana "You know Harper, right?"
    mc "Yeah, we've met."
    scene w1_0376 with pixellate
    mct "(Sort of.)"
    scene w1_0381 with dissolve
    play sound "sound effects/notification.wav"
    $ met_harper = True
    show bioadd with dissolve
    harp "Hello."
    scene w1_0380 with dissolve
    hana "I was just telling her about a show my band is playing over at the Asp Hole this Thursday night. You know it?"
    scene w1_0382 with dissolve
    mc "...asshole?"
    scene w1_0383 with dissolve
    hana "No, {b}Asp{/b} Hole, you idiot."
    scene w1_0382 with dissolve
    mc "Sorry, never heard of it."
    scene w1_0384 with dissolve
    hana "That's not important. Come see us play. You tell them you're here because of our band and you'll get a free drink on the house."
    hana "Plus, they're more likely to invite us back. Do a girl a favor?"
    scene w1_0385 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Agree to help Hana out. [gr]\[Hana +1\]":
            $ hanaFlag = True
            $ Hana_Affection += 1
            scene w1_0386 with dissolve
            show screen textbox2 with dissolve
            $ history_hana = "Hana strikes me as a woman out of place in a place like the Carnation Club, but her offer of seeing her band play at a local watering hole should help me get a better picture of her."
            $ unread_hana = True
            play sound "sound effects/notification.wav"
            show bioupdate with dissolve
            mc "Sure, sounds like fun anyway, but when you put it that way how can I refuse?"
            scene w1_0387 with dissolve
            hana "Well, you could be lame like Jacob. Mother fucker said he has a bed time on the night he's off. Can you believe that? What is he, an old man?"
            mc "Could be a military habit."
            scene w1_0388 with dissolve
            hana "Thanks a ton. I'll text you the details later."
            hana "Don't worry, we're going to blow the roof off the place. You'll be thanking me one day, when you get to brag about seeing us live before we were famous."
            scene w1_0389 with dissolve
            harp "I'll be there too, Hana. I could use a night of loud noise."
            scene w1_0390 with dissolve
            hana "Good!"
            scene w1_0391 with dissolve
            hana "I'll see you two later, I got something to talk about with August."
            scene w1_0392 with dissolve
            harp "..."
            mc "..."
            scene w1_0393 with dissolve
            harp "... well, bye!"
            scene w1_0394 with dissolve
            "Harper akwardly left in a hurry."
            mct "(Did I do something to weird her out?)"
            stop music fadeout 3.0
            if kat_polite == True:
                mct "(Oh, well I should turn this footage into Mrs. Pulman and see if Ian can take me home.)"
            else:
                mct "(Oh, well I should turn this footage into Kathleen and see if Ian can take me home.)"

            if w1FelGonzo == True:
                jump w1InterviewKatRose

            if w1RoseGonzo == True:
                jump w1InterviewKatFel

            if w1VeroGonzo == True:
                jump w1InterviewKatFel


        "Tell her nightclubs aren't really your thing.":
            show screen textbox2 with dissolve
            mc "Sorry, night clubs aren't really my thing."

    scene w1_0387 with dissolve
    hana "C'mon dude. I'm not going to be pushy about it, but don't tell me you're some kind of shut in. You're working here, aren't you?"
    scene w1_0396 with dissolve
    hana "I'll owe you one!"
    scene w1_0386 with dissolve

    "If I agree, this could be the {b}start of something{/b}. Then again, do I even like Hana? She can be pretty abrasive. Maybe it's best if we keep our relationship strictly as co-workers."
    hide screen textbox2 with dissolve

    menu:
        "Change your mind and agree to go. [gr]\[Hana\]":
            $ hanaFlag = True
            show screen textbox2 with dissolve
            $ history_hana = "Hana strikes me as a woman out of place in a place like the Carnation Club, but her offer of seeing her band play at a local watering hole should help me get a better picture of her."
            $ unread_hana = True
            play sound "sound effects/notification.wav"
            show bioupdate with dissolve
            mc "Sure, why not? Could be fun."
            scene w1_0388 with dissolve
            hana "Thanks a ton. I'll text you the details later."
            hana "Don't worry, we're going to blow the roof off the place. You'll be thanking me one day, when you get to brag about seeing us live before we were famous."
            scene w1_0389 with dissolve
            harp "I'll be there too, Hana. I could use a night of loud noise."
            scene w1_0390 with dissolve
            hana "Good!"
            scene w1_0391 with dissolve
            hana "I'll see you two later, I got something to talk about with August."
            scene w1_0392 with dissolve
            harp "..."
            mc "..."
            scene w1_0393 with dissolve
            harp "... well, bye!"
            scene w1_0394 with dissolve
            "Harper akwardly left in a hurry."
            mct "(Did I do something to weird her out? I don't think so...)"

            if kat_polite == True:
                mct "(Oh, well I should turn this footage into Mrs. Pulman and see if Ian can take me home.)"
            else:
                mct "(Oh, well I should turn this footage into Kathleen and see if Ian can take me home.)"

            if w1FelGonzo == True:
                jump w1InterviewKatRose

            if w1RoseGonzo == True:
                jump w1InterviewKatFel

            if w1VeroGonzo == True:
                jump w1InterviewKatFel

        "Tell her you're really not interested.":
            show screen textbox2 with dissolve
            scene w1_0385 with dissolve
            mc "Sorry, it's just not for me."
            scene w1_0395 with dissolve
            hana "Well, {b}fine{/b}! Don't regret it that you missed the chance to see us live before we become famous."
            scene w1_0389 with dissolve
            harp "I'll go, Hana. I could use a night of loud noise."
            scene w1_0390 with dissolve
            hana "Good!"
            scene w1_0391 with dissolve
            $ history_hana = "Hana strikes me as a woman out of place in a place like the Carnation Club, but I had no interest in figuring out exactly why that is. She asked me to come see her band play, but I deciding not to have anything to do with her."
            $ unread_hana = True
            play sound "sound effects/notification.wav"
            show bioupdate with dissolve
            hana "Well, I'll see you two later. I got something to talk about with August."
            scene w1_0392 with dissolve
            harp "..."
            mc "..."
            scene w1_0393 with dissolve
            harp "... well, bye!"
            scene w1_0394 with dissolve
            "Harper akwardly left in a hurry."
            mct "(Did I do something to weird her out? I don't think so...)"
            stop music fadeout 3.0
            if kat_polite == True:
                mct "(Oh, well I should turn this footage into Mrs. Pulman and see if Ian can take me home.)"
            else:
                mct "(Oh, well I should turn this footage into Kathleen and see if Ian can take me home.)"

            if w1FelGonzo == True:
                jump w1InterviewKatRose

            if w1RoseGonzo == True:
                jump w1InterviewKatFel

            if w1VeroGonzo == True:
                jump w1InterviewKatFel




label w1InterviewKatRose:

    scene w1_0398 with dissolve
    mct "(I hope she's still here. This place is too big for me to reliably find her.)"
    play sound "sound effects/door-knock.wav"
    scene w1_0397 with dissolve
    "*Knock, knock.*"
    scene w1_0398 with dissolve
    kat "Whoooo is it?"
    "Kathleen's voice carried clearly through the door, with a song style cadence."
    scene w1_0399 with dissolve
    mc "It's [mcf]. I've finished Felicia's profile."
    scene w1_0398 with dissolve
    kat "Already? Come in!"
    play music "music/cello-suite-No-1-G-Major-Prelude.mp3"
    play sound "sound effects/door-openclose.wav"
    scene w1_0401 with fade
    mc "........."
    scene w1_0402 with fade
    mc "......"
    scene w1_0400 with fade
    mc "I'm not interrupting anything, am I?"
    scene w1_0403 with dissolve
    kat "No, I'm just introducing this fat ass cow to her future adoring fans."
    kat "Leave the camera on the table. You can go home, I don't think I need you for anything else today."
    scene w1_0404 with dissolve
    mc "Yeah, okay. One thing..."
    scene w1_0405 with dissolve
    kat "...what is it? Make it quick, you're killing the mood here."
    scene w1_0404 with dissolve
    mc "Has Ian finished yet?"
    scene w1_0405 with dissolve
    kat "No, he hasn't come by. Is that all?"
    scene w1_0406 with dissolve
    mct "(Great, guess I'm stuck waiting around unless I want to take a train.)"
    scene w1_0407 with dissolve
    mc "I'll be going now."
    scene w1_0408 with dissolve
    mc "Oh, and good work today I'm sure!"
    scene w1_0406 with dissolve
    hide screen textbox2 with dissolve
    menu:
        "Wish them fun. [gr]\[Kathleen +1\]":
            $ Kathleen_Affection += 1
            scene w1_0407 with dissolve
            show screen textbox2 with dissolve
            mc "You two have fun. Heh."
            scene w1_0406 with dissolve
            "I said -- stupidly"

        "Tell Rosalind to hang in there.":
            scene w1_0407 with dissolve
            show screen textbox2 with dissolve
            mc "Hang in there, Rose!"
            scene w1_0406 with dissolve
            "I said -- stupidly."

        "Just leave.":
            show screen textbox2 with dissolve
            pass

    stop music fadeout 2.0
    scene w1_0407 with dissolve
    mc "Bye!"
    play sound "sound effects/door-openclose.wav"
    scene w1_0418 with fade
    mct "(That wasn't even all that shocking to me, was it?)"
    mct "(I'll go wait at the bar until Ian finishes.)"
    scene black with fade
    "......"
    "It wasn't long until my friend made his reappearance and we headed back to my new apartment."
    jump w1SleepInterrupted

label w1InterviewKatFel:

    scene w1_0398 with dissolve
    mct "(I hope she's still here. This place is too big for me to reliably find her.)"
    play sound "sound effects/door-knock.wav"
    scene w1_0397 with dissolve
    "*Knock, knock.*"
    scene w1_0398 with dissolve
    kat "Whoooo is it?"
    "Kathleen's voice carried clearly through the door, with a song style cadence."
    scene w1_0399 with dissolve
    if w1RoseGonzo == True:
        mc "It's [mcf]. I've finished Rosalind's profile."
    if w1VeroGonzo == True:
        mc "It's [mcf]. I've finished Veronica's profile."
    scene w1_0398 with dissolve
    kat "Already? Come in!"
    play music "music/cello-suite-No-1-G-Major-Prelude.mp3"
    play sound "sound effects/door-openclose.wav"
    scene w1_0401 with fade
    mc "........."
    scene w1_0410 with fade
    mc "......"
    scene w1_0409 with fade
    mc "I'm not interrupting anything, am I?"
    scene w1_0412 with dissolve
    kat "No, I'm just introducing this prissy bitch to her future adoring fans."
    kat "Leave the camera on the table. You can go home, I don't think I need you for anything else today."
    scene w1_0411 with dissolve
    mc "Yeah, okay. One thing..."
    scene w1_0413 with dissolve
    kat "...what is it? Make it quick, you're killing the mood here."
    scene w1_0411 with dissolve
    mc "Has Ian finished yet?"
    scene w1_0413 with dissolve
    kat "No, he hasn't come by. Is that all?"
    scene w1_0414 with dissolve
    mct "(Great, guess I'm stuck waiting around unless I want to take a train.)"
    scene w1_0415 with dissolve
    mc "I'll be going now."
    scene w1_0416 with dissolve
    mc "Oh, and good work today I'm sure!"
    scene w1_0414 with dissolve
    hide screen textbox2 with dissolve
    menu:
        "Wish them fun. [gr]\[Kathleen +1\]":
            $ Kathleen_Affection +=1
            scene w1_0415 with dissolve
            show screen textbox2 with dissolve
            mc "You two have fun. Heh."
            scene w1_0414 with dissolve
            "I said -- stupidly"

        "Tell Felicia to hang in there. [gr]\[Felicia +1\]":
            $ Felicia_Affection +=1
            scene w1_0415 with dissolve
            show screen textbox2 with dissolve
            mc "Hang in there, Felicia."
            "I stupidly made a show of support."
            scene w1_0417 with dissolve
            fel "Hehe! See you later, [mcf]!"
            kat "Stupid girl. Focus on the camera lens, not over there!"

        "Just leave.":
            show screen textbox2 with dissolve
            pass

    stop music fadeout 2.0
    scene w1_0415 with dissolve
    mc "Bye!"
    play sound "sound effects/door-openclose.wav"
    scene w1_0418 with fade
    mct "(That wasn't even all that shocking to me, was it?)"
    mct "(I'll go wait at the bar until Ian finishes.)"
    scene black with fade
    "......"
    "It wasn't long until my friend made his reappearance and we headed back to my new apartment."

label w1SleepInterrupted:

    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionhana01 with blinds
    $ renpy.pause(6, hard=True)
    $ date = "june01night"
    scene w1_0422 with blinds
    show screen textbox2 with dissolve
    show screen qmenu with dissolve
    "Later that night, after a pleasant evening featuring a bad movie, some not-so-great Chinese takeout, and some light review of my studies, I was fast asleep."
    play music "music/sneaky-snitch.mp3"
    "Operative word being {i}was{/i}."
    play sound "sound effects/metal-door-slam.wav"
    $ renpy.pause(1.5, hard=True)
    scene w1_0423 with vpunch
    mc "--!"
    "A loud noise violently plucked me from my slumber."
    scene w1_0424 with fade
    play sound "sound effects/high-heel-footsteps.wav"
    mct "(What the hell was that...?)"
    mct "(Is that footsteps...?)"
    play sound "sound effects/woman-laugh.mp3"
    $ renpy.pause(1.5, hard=True)
    scene w1_0425 with dissolve
    mct "(What the fuck, what the fuck, what the fuck...?)"
    "Someone's downstairs. Giggling."
    play sound "sound effects/high-heel-footsteps.wav"
    show june01night with squares
    mct "(Am I being robbed?)"
    mct "(Considering this place is club property, who the hell knows who has access to it.)"
    mct "(Fucking idiot, I should've changed the locks!)"
    scene w1_0426 with cmet
    "Springing into action, I clumsily rolled off the bed looking for something, ANYTHING that would work well as an improvised weapon."
    scene w1_0427 with dissolve
    mct "(No...)"
    scene w1_0428 with dissolve
    mct "(Definitely not!)"
    scene w1_0429 with dissolve
    mct "(Oh, you've got to be kidding me...)"
    "The ping pong paddle being the best option potentially standing between me and danger, I gripped the ad-libbed cudgel so tight that my knuckles turned white."
    "The clacking of footsteps grew slighter."
    play sound "sound effects/door-slide.wav"
    scene w1_0430 with dissolve
    "Until finally petering out with the sound of a door closing shut."
    mct "(Did they leave...?)"
    scene w1_0431 with dissolve
    "Doing my best to keep low, crawling on my hands and knees to get a better look at the apartment."
    scene w1_0432 with dissolve
    "Peering through the railing, I paused to let me eyes adjust to the darkness."
    "Having only been here a little over a week, the geography of the place hadn't quite become ingrained in my mind yet. Not enough to pick out inconsistencies in the dark at least."
    scene w1_0433 with dissolve
    mct "(Door's closed...)"
    scene w1_0434 with fade
    "I got to take a closer look."
    scene w1_0435 with dissolve
    mct "(Someone's in the bathroom!)"
    "A light beamed from the crack in the door."
    mct "(I should try and make a dash for it and call the police...)"
    mct "(...but what if it's August or Charles or somebody really important connected to the club? Getting the police involved might not be a smart idea.)"
    "I hadn't really considered this consequence of working for the club. The fact that it could limit me on relying on the police."
    mct "(I'm part of a criminal enterprise now. What the fuck, [mcf]?)"
    scene w1_0436 with dissolve
    mct "(Shit, I got to be sure of the situation first!)"
    scene w1_0437 with dissolve
    "I reached for the door handle, a piece of wood separating me from the unknown."
    scene w1_0438 with dissolve
    "On the other side I could hear heavy, frantic breathing."
    mct "(Okay... whoever's on the other side, I should look like I mean business.)"
    scene w1_0439 with dissolve
    mct "(Yeah...)"
    scene w1_0440 with dissolve
    mct "(Okay...{w}Three...)"
    mct "(Two...)"
    mct "(One...! {w}Go!)"
    play sound "sound effects/door-slide.wav"
    scene w1_0441 with wiperight
    "Sliding the door open, I blitzed my way past the mouth of the bathroom. Ready to bring down ping-pong laced justice."
    scene w1_0442 with dissolve
    mc "......"
    stop music fadeout 3.0
    scene w1_0443 with dissolve
    "..."
    play sound "sound effects/record-scratch.wav"
    scene w1_0444 with vpunch
    "Only to find a strange woman parked against the bathtub, my womanizing friend's head planted squarely between her thighs."
    "Killian, either too drunk or too engrossed in his task, didn't notice or care. His lady friend on the other hand..."
    woman "Eeeeeh, who the fuck are you?!" with hpunch
    scene black with fade
    "That's a good question, lady."
    scene w1_0445 with circlewipe
    play music "music/thief-in-the-night.mp3"
    mc "Why did you pick my place to screw around? What's wrong with your apartment?"
    kil "Eeeeeh? Miiiina's s-there."
    "Best I could gather after sending Ian's lady friend home, was that he thought he'd just use my new place as a fuck pad."
    "Part of me wanted to bitch at him for the invasion or privacy, startling the hell out me, and just the lack of general common sense, but..."
    scene w1_0447 with fade
    "Honestly, it probably wouldn't stick even if he wasn't two sheets to the wind right about now."
    mc "Give me your feet."
    scene w1_0446 with dissolve
    kil "Huh? I can jhust go home. Miina's waiting."
    scene w1_0447 with dissolve
    mc "*sigh* I'm not letting you drive home plastered. Now, give me your feet."
    scene w1_0448 with dissolve
    kil "Sure thing, honey."
    kil "Heheh, you'll make a good wife someday."
    scene w1_0449 with dissolve
    mc "Other one please."
    scene w1_0450 with dissolve
    mc "Do you want me to call Mina?"
    scene w1_0451 with dissolve
    kil "N-no!"
    scene w1_0452 with dissolve
    mc "Then shut up. I'm kinda pissed right now."
    scene w1_0453 with dissolve
    kil "Eeeeh, lighten up. It's the club's apartment. I got you the job rhhhemember?"
    scene w1_0452 with dissolve
    mc "Listen here, It's MY home now and -- y'know what, never mind! You won't remember this in the morning anyway."
    scene w1_0453 with dissolve
    kil "Nhot a thing! Hehehe!"
    scene w1_0452 with dissolve
    mc "Just sleep it off, alright?"
    scene w1_0454 with dissolve
    kil "Hey [mcf]...?"
    mc "What is it now?"
    kil "Uh, shorry for the trouble."
    scene w1_0455 with dissolve
    if Killian_Bromance >= 16:
        mc "*sigh* What are friends for?"
    else:
        mc "Just don't make this a habit, please?"
    scene black with fade
    stop music fadeout 3.0
    "......"
    "..."

label june02start:
    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionmina02 with blinds
    $ renpy.pause(6, hard=True)
    $ date = "june02day"
    scene w1_0456 with sunshine
    show screen textbox2 with dissolve
    show screen qmenu with dissolve
    show june02day with squares
    play music "music/crinoline-dreams.mp3"
    "The next morning, Killian was gone, having evaporated as suddenly as he appeared the previous night."
    "In his place, was a plate of breakfast. Probably meant as a small token of apology."
    mct "(It's cold...)"
    play ambient "sound effects/shower.wav"
    scene w1_0457 with wet
    "My day's looking pretty open. I don't have anything I NEED to do or any place I need to be."
    "I'm effectively on call to the Carnation Club... I think. Despite it being explained to me, I'm not really sure when the actual work part will start happening."
    scene w1_0458 with dissolve
    mct "(Hmmm, my dick won't quit. I guess I didn't really get any release yesterday, despite...)"

    if w1FelGonzo == True:
        scene w1_0419 with pixellate
        "The sight of Felicia's tight throat ingesting that large gold dildo with ease."

    if w1RoseGonzo == True:
        scene w1_0420 with pixellate
        "Rosalind's supplicant display, her fat tits dangling heavily in front of her as she thanked her new patrons."

    if w1VeroGonzo == True:
        scene w1_0421 with pixellate
        "Veronica's display of flexibility, drawing her long muscular leg back and giving the camera a good glimpse of the womanly flower inbetween."

    "The sudden recollection just added fuel to the fire."
    scene w1_0458 with pixellate
    mct "(Maybe I should avail myself of the club's services sometime? Dalia mentioned that if I ever needed any of the house girl's services to give her a call.)"
    mct "(That'd be taking advantage though, wouldn't it?)"
    scene w1_0459 with dissolve
    mct "(I guess I'll just take care of it mys--)"
    play sound "sound effects/ringing-inbound.wav"
    stop music fadeout 3.0
    scene w1_0460 with dissolve
    "*Ring, ring. Ring, ring**"
    "Put a pin in that thought."
    stop ambient
    scene w1_0461 with fade
    stop sound
    mc "Mina...?"
    scene player-bathroom-blur with dissolve
    show mina-call with dissolve
    play music "music/happy-boy-end-theme.mp3"
    mc "Hello?"
    mina "[mcf]? It's Mina, Ian's gi--"
    mc "You don't have to explain who you are, Mina. How are you?"
    mina "Mmmmmh, well I'm fine. A little {b}stood up{/b} at the moment."
    mina "Sorry to bother you, but do you know where Ian is? We were supposed to go shopping today, but he hasn't turned up."
    mina "He didn't come home last night either, I'm getting a little worried..."
    mct "(Well, that's cause he was too busy getting blasted and giving out free face rides to strange women.)"
    mc "No, no, don't worry about Ian, he..."
    hide screen textbox2 with dissolve

    menu:
        "Comfort Mina with a half-truth. [gr]\[MinaKillian -1\]":
            $ Mina_KLove -= 1
            show screen textbox2 with dissolve
            mc "He got a little drunk last night and I had to take his car keys. He slept it off at my place."
            "Probably best if I leave out the bathroom cunnilingus."
            mc "I thought about calling you, but it was pretty late."
            mc "When I woke up, he had already left. Dunno where he is now. Probably forgot he had plans, knowing him."
            mina "Ugh, that does sound like him!"

        "Flat out lie for him. [gr]\[Killian +3\]":
            $ Killian_Bromance += 3
            $ w1MinaLie = True
            show screen textbox2 with dissolve
            mc "His uncle took us out and got us drunk last night. He ended up sleeping it off here, before leaving this morning to help Chuck with some work. You know his uncle, right?"
            "For whatever reason, I decided to cover for Ian and lie to poor Mina."
            mina "We haven't met. I actually haven't met any of his family..."
            mc "Ah, well he probably forgot to let you know about the change in plans. It sounded pretty important!"
            mina "Ugh, that does sound like him! He's always forgetting to call!"

    mina "*sigh* There goes my day..."
    mina "Say, you're not free, are you?"
    mina "You wouldn't want to sit around bored while a cute girl tries on clothes? Maybe a grab a bite to eat...?"
    mct "(Honestly that doesn't sound too bad, but...)"
    mct "(Should I really hang out with Mina without Ian being around? He might get the wrong idea. Then again, I'm not the one who had my face drunkenly buried in not-my-girlfriend's snatch last night.)"
    "If I agree, maybe Mina and I could {b}become friends{/b}. Then again, perhaps it's best if she remains {b}just my friend's girlfriend{/b}."

    hide screen textbox2 with dissolve

    menu:
        "Agree to accompany Mina shopping [gr]\[Mina +2\]":
            $ minaFlag = True
            $ Mina_Affection += 2

            show screen textbox2 with dissolve
            mc "I'm actually not doing jack squat today, so..."
            mc "That sounds like fun, Mina. Thank you for inviting me."
            mina "Yaaaaaaaaaaay!"
            "A shrill, jubilant cry emitted from my phone's speaker."
            mina "I'll pick you up then, just text me your address!"
            mina "Oh, and lunch is my treat today! As thank you for keeping me company."
            mct "(A cute model is paying for my lunch? Awesome.)"
            scene black with fade
            stop music fadeout 3.0
            "......"
            "..."
            jump w1MinaDateStart

        "(Lie) Tell her you have other plans. [red]\[Mina -1\]":
            $ Mina_Affection -= 1
            show screen textbox2 with dissolve
            $ history_mina = "My best friend's girlfriend, I decided to keep things strictly in those terms and not see her outside of Ian's company."
            $ unread_mina = True
            play sound "sound effects/notification.wav"
            show bioupdate with dissolve
            mc "Sorry, I've already made other plans today."
            mina "Awww, that's alright. Maybe some other time then?"
            "Mina's normally chipper disposition took on a plaintive quality, like the shrill whine of a puppy."
            mc "Yeah, some other time maybe."
            mina "Alright, I'll talk to you later [mcf]."
            mina "Thanks again for letting me know about Ian. Buh bye!"
            stop music fadeout 3.0
            jump w1MinaDateSkip




label w1MinaDateStart:

    scene w1_0462 with circlewipe
    "Lunch took us to a familiar place."
    scene w1_0463 with dissolve
    play music "music/ukulele-fun.mp3"
    mc "I'm surprised you wanted to come here."
    scene w1_0464 with dissolve
    mina "Why do you say that, [mcf]?"
    scene w1_0465 with dissolve
    mc "It's kind of a greasy place."
    scene w1_0466 with dissolve
    mina "Hey, don't you start on me too! Ian's always snipping at me with comments about eating and gaining weight."
    scene w1_0465 with dissolve
    mc "Sorry! I didn't mean it that way. Just that a pretty girl like you, in a place like this, sticks out like a sore thumb."
    scene w1_0467 with dissolve
    mina "Ah, well... it's not like I'm famous or anything. I don't really get any kind of big work..."
    mina "Heck, I wouldn't even call it regular work."
    scene w1_0468 with dissolve
    mc "I have 100 percent confidence that'll change some day soon."
    "It wasn't a line, I really did mean that. Mina was cute and bubbly, but she could also pull off sexy well. I honestly couldn't imagine her toiling as a struggling actress for long."
    scene w1_0469 with dissolve
    mina "I actually have an audition coming up, that's why I wanted to go shopping today. I need to find something to wear."
    scene w1_0470 with dissolve
    mc "That's awesome. I hope you get the role."
    scene w1_0471 with dissolve
    mina "Thanks! Ian is going to help me rehearse for it. Have you ever seen him try to act? He is {b}awful{/b}! But he tries for my sake."
    scene w1_0472 with dissolve
    mina "Sometimes..."
    scene w1_0473 with dissolve
    mina "Thanks for coming out with me again! Heh!"
    scene w1_0470 with dissolve
    "Mina was quick to hide her momentary lapse in cheer, overwriting it with an upbeat smile."
    mc "I didn't have anything to do today, so stop mentioning it."
    scene w1_0471 with dissolve
    mina "Right! That was the last time. I promise."
    scene w1_0474 with dissolve
    "......"
    "..."
    "A prominent lull fell over the conversation."
    scene w1_0475 with dissolve
    mina "Y'know this kind of feels a little lop-sided. I've heard so many stories about you from Ian, but you don't really know anything about me I bet."
    mct "(Stories BEFORE high-school she means. I don't really get Ian's fixation with that time in our life.)"
    mina "Go, ahead! Ask me some questions about myself. It's only fair."
    scene w1_0476 with dissolve
    mina "Plus, Not like I don't like being at the center of attention. Hehe!"
    scene w1_0470 with dissolve
    "Well, there has been one question that has been percolating in my head ever since we first met. Namely, what does a nice girl like her see in a blatant womanizer like my friend."
    mct "(I probably shouldn't actually ask that though, lest I end up offending her. Probably should pick something more benign.)"
    mc "Have you always wanted to be a model and actress?"
    scene w1_0471 with dissolve
    mina "Nope. I actually wanted to be a marine biologist growing up."
    scene w1_0470 with dissolve
    mc "You were a weird dolphin girl?"
    scene w1_0477 with dissolve
    mina "N-no! Don't make fun of me!"
    mina "Anyway... In high-school I started modeling as a part-time job - for stuff like teen magazines and fashion outlet catalogues - and I learned to love it."
    scene w1_0473 with dissolve
    mina "Some of it's boring. Ton of sitting, lotta preening... but there's these... uh, {b}bursts{/b}!"
    scene w1_0471 with dissolve
    mina "Bursts of action. Having to swap through dozens of poses back to back, all these spot lights and rim lights harshly bearing down on you, the machine-gun rapid clicks of the camera as it takes photo after photo..."
    scene w1_0478 with dissolve
    mina "I... I {b}love it{/b}! It's so easy to forget about yourself and your troubles during a shoot."
    scene w1_0479 with dissolve
    "All the while through Mina's impassioned explanation, a genuine smile found itself spread on her lips. It was radiant and natural, unlike the deliberate one she seems to always default to."
    mc "That actually sounds really exciting. To be honest, I always just thought people wanted to be models because of the fame and glamour, but it sounds like you really enjoy the procedure."
    scene w1_0478 with dissolve
    mina "Procedure...? I like that. That's a good way of putting it."
    scene w1_0479 with dissolve
    "Having passion for what you do is a very attractive trait for a woman, but should I say as much?"
    mct "(It could come across as me hitting on her.)"
    hide screen textbox2 with dissolve

    menu:
        "Just say what you're thinking. [gr]\[Mina +1\]":
            $ Mina_Affection += 1
            show screen textbox2 with dissolve
            "Mina seems like a straight forward woman. She probably wouldn't read too much into me sharing how I honestly feel."
            mc "It's great you're so passionate about your work. That's very attractive in a woman."
            scene w1_0480 with dissolve
            mina "You know, I don't usually get complimented on much more than my looks to be honest."
            scene w1_0481 with dissolve
            mina "Thank you, [mcf]."

        "Keep your thoughts to yourself":
            pass

    scene w1_0482 with dissolve
    show screen textbox2 with dissolve
    mc "So, what're you auditioning for?"
    scene w1_0483 with dissolve
    mina "Oh, it's just a dumb role in a silly TV soap opera. Nothing you'd know... it's called {i}Loving Days in Lafayette{/i}."
    scene w1_0484 with dissolve
    mc "Hey, work's work, right? I've heard that acting on those daily programs is pretty breakneck work. I bet it'll be a good chance to develop all kinds of skills."
    scene w1_0485 with dissolve
    mina "Heheh, that's a great way of looking at it. At any rate, I'll have to get the part first and... well, we'll see."
    scene w1_1763 with dissolve
    mina "I'll have to find a new gym if I get the part as well. My membership for my last one ran out last week and I don't want to renew. That place is brimming with pervs."
    scene w1_0485 with dissolve
    mina "Anyway, I'm counting on you to help me pick out the perfect dress for the occasion. Don't let me down!"
    mc "I suddenly feel a lot of pressure..."
    scene black with fade
    "For the next five minutes, we made light conversation as we finished our lunch before moving onto a clothes searching expedition."
    scene w1_0486 with circlewipe
    stop music fadeout 3.0
    "We went from shop to shop..."
    "After shop to yet another shop."
    "Mina had found many things to purchase, more than I thought would've fit in her tiny car, but the one particular outfit for her audition remained elusive. Or so she said."
    "Before I knew it, a few hours had passed... I'm starting to think Ian's forgetfulness might have been of the more convenient variety."
    scene w1_0487 with circlewipe
    play music "music/happy-whistling-ukulele.mp3"
    mina "Don't worry... I have the feeling this is going to be the store! They have the best selection!"
    mct "(Why didn't we start here then?!)" with hpunch
    mc "Well, I'm not in any rush, so take your time."
    "I said, in spite of myself."
    scene w1_0488 with dissolve
    clerk "Welcome to {i}Kitty Kallen{/i}. Is there anything I can assist you with today?"
    "The store clerk, pulled away from whatever magazine she was reading when we entered, got up and greeted us with the bearing of someone who's worked in customer service for years."
    scene w1_0489 with dissolve
    mina "I'm looking for something cute or sexy to wear to an audition. I don't know quite which yet..."
    clerk "I can help with that. Allow me to take you around the store and pick out and accessorize a few outfits."
    mina "That'd be helpful, thanks."
    scene w1_0490 with dissolve
    clerk "If he wants, your boyfriend can have a seat in the back while we look."
    clerk "We have some chairs next to the dressing rooms."
    scene w1_0491 with dissolve
    mina "Why don't you do that, [mcf]? This might take awhile."
    mc "I think I'll do that then."
    scene w1_0492 with dissolve
    "Excusing myself, I made a beeline toward the dressing room and found a seat."
    scene w1_0493 with dissolve
    mct "(I hope this is the last store...)"
    scene w1_0494 with dissolve
    mct "(Not that I mind the company of a woman like Mina. Definitely beats sitting around that way-too-big-for-me apartment and jerking it.)"
    mct "(I think I'll shut my eyes for a moment...)"
    scene black with fade
    mct "(...boyfriend? I guess neither of us cared enough to correct her.)"
    "......"
    "..."
    mina "[mcf]...?"
    "A warm, light touch caressed my cheek."
    mct "(Zzzzzz, that feels nice...)"
    mina "Hey, [mcf]! wake up!"
    hide screen textbox2 with dissolve
    scene w1_0497 with dissolve
    show blank at blink
    $ renpy.pause(3.0, hard=True)
    show blank at blink
    scene w1_0498 with dissolve
    $ renpy.pause(1.5, hard=True)
    scene w1_0495 with dissolve
    show screen textbox2 with dissolve
    "Mina had switched tactics on me, trading a gentle caress for a more vigorous prodding."
    mc "Ngg, sorry. I must've accidently drifted off..."
    mc "I got a little less sleep last night than I would've liked."
    scene w1_0496 with dissolve
    mina "Sorry if I took too long, hehe. I found a few options though."
    mina "Could I model them for you and get your opinion?"
    mc "I'd love to see them, but I don't really think I know what'll catch a casting director's eye..."
    scene w1_0499 with dissolve
    mina "Oooh, I think you do. It's not like it's complicated. Just give me your opinion as a man."
    scene w1_0500 with dissolve
    mc "Well, I'm certainly qualified to do that. Heh."
    scene w1_0501 with irisout
    mina "Great! I'll be out in a jiffy~"
    scene w1_0502 with dissolve
    "With a sing-song declaration, Mina disappeared behind the dressing room's partition."
    scene w1_0503 with dissolve
    mc "Aaannnaghhh!"
    scene w1_0504 with w24
    mct "(I'm going to sleep good tonight!)"
    mina "Hey, [mcf]? What's Ian's uncle like?"
    scene w1_0505 with dissolve
    mc "Dr. Chuck you mean? Why do you want to know?"
    scene w1_0506 with dissolve

    if w1MinaLie == True:
        mina "Well, like I told you I've never met him."
        mina "Just like this morning, he's always running off at the oddest times to help him with something or another."
    else:
        mina "I've never actually met him, but he's always running off at the oddest times to help him with something or another."

    scene w1_0504 with dissolve
    mc "..."
    mct "(This is getting kinda slippery. I should feel out what Mina knows before I accidently tell her something contrary to what she's been told or let slip something about the club.)"
    scene w1_0507 with dissolve
    mc "Well, what has Ian told you about him?"
    scene w1_0506 with dissolve
    mina "He said that -- ngha, damn zipper! -- he said that his uncle owned a dusty old jazz-piano bar."
    scene w1_0507 with dissolve
    mc "Yeah, I've uh... been there, dusty is one way to describe it."
    scene w1_0506 with dissolve
    mina "Thing is -- ah, perfect fit -- thing is he never wants to take me. I said {i}a jazz bar sounds cool{/!} and he tells me it's just a boring place for old farts to reminisce about the old days and pretend like they're cool."
    mina "Anyway, I just want to know, what kind of person he is. He seems pretty important to Ian."
    scene w1_0507 with dissolve
    mc "Hmm.... he's a interesting guy. He's really loud for one and he laughs a lot. Smart too, he used to be an aerospace engineer."
    mc "It made him a ton of money, as far as I can tell. I used to go on vacations with Ian's family when we were in middle school. Dr. Chuck was one of the few people that treated me warmly."
    mc "He's... decent folk."
    scene w1_0504 with dissolve
    "--that is what I had always believed, at least. Now, I'm experiencing a bit of cognitive dissonance there. Deep down I'm not so sure, when I compare the image of Dr. Chuck the jovial Physics Club Advisor and uncle to my friend and..."
    "Dr. Chuck part owner of the Carnation Club, a place where women do degrading things for the entertainment of a bunch of old assholes."
    "Could both images be authentic and true at the same time...?"
    scene w1_0506 with dissolve
    mina "He sounds like a nice guy. I hope to meet him one day."
    scene w1_0508 with dissolve
    mina "~allllright, all finished."
    scene w1_0509 with dissolve
    mina "~tada! What do you think? This is the more professional looking option."
    scene w1_0510 with dissolve
    "Mina give herself a little spin, to emphasize the skirt's hipline."
    scene w1_0512 with dissolve
    mc "You know you're pretty good at wearing clothes."
    mc "You should do that for a job."
    scene w1_0511 with dissolve
    mina "Har har, very funny [mcf]. Tell me what you think?"
    scene w1_0512 with dissolve
    mct "(What I think? Well...)"
    hide screen textbox2 with dissolve
    menu:
        "Talk about the skirt, without restraint. [gr]\[Mina +2\]":
            $ Mina_Affection += 2
            scene w1_0513 with dissolve
            show screen textbox2 with dissolve
            mc "The skirt looks wonderful on you. It brings out the contours of your hips very nicely."
            mc "It also {i}skirts{/i} the line between conservative looking and sexy. Not quite too short to be garish, but also not so long to be considered drab."
            scene w1_0514 with dissolve
            mina "Wow, I'm so glad you came along. That's way better an answer than Ian ever gives me. The most I ever get out of him is..."
            scene w1_0515 with dissolve
            mina "{i}That's hot, babe{/i}! Or... {i}could show a little more skin{/i}!"
            "She said, doing her best to conceal her mouse-like voice in a gruff affectation."
            mc "Yeah, I can picture that..."
            scene w1_0516 with dissolve
            mina "That's the kind of reaction I was hoping for, but I still have two more outfits to try on."


        "Talk about the blouse, respectfully.":
            scene w1_0513 with dissolve
            show screen textbox2 with dissolve
            mc "I like the way the blouse looks on you. It's professional looking, but it shows off your toned arms nicely."
            scene w1_0515 with dissolve
            mina "Hmm... I'm not so sure that's the kind of reaction I was looking for from a man. Let's see how you like the other two outfits."
            scene w1_0516 with dissolve

    mina "Be right back!"
    scene w1_0505 with dissolve
    mc "So, what do you do besides modeling?"
    scene w1_0506 with dissolve
    mina "What do you mean?"
    scene w1_0507 with dissolve
    mc "You said your work wasn't regular, I was just wondering if you worked as a waitress or something. That's what struggling actors and models do, right?"
    scene w1_0506 with dissolve
    mina "Oh...! Uh, no. I go part-time to school, but I'm... I'm fortunate enough not to have to work. You could say my parent's are pretty well off."
    "She sounded kind of embarrassed about it."
    scene w1_0505 with dissolve
    mc "What are you studying?"
    scene w1_0506 with dissolve
    mina "I haven't really picked a major yet. I don't really know what I want to do, I just know I should have something to fall back on if acting doesn't work out."
    scene w1_0504 with dissolve
    mina "My mom says that college for a girl like me should be less about building a career and more about finding myself a well-to-do husband. Can you believe that?!"
    mina "Who the hell still talks like that in this day and age?"
    scene w1_0517 with dissolve
    "Before I had a chance to answer, Mina had reappeared in front of me."
    scene w1_0518 with dissolve
    mina "Gah! It makes me so angry!"
    scene w1_0519 with dissolve
    mc "Well, it sounds like you're doing the smart thing about your future."
    scene w1_0520 with dissolve
    mina "Thank you! Well, what do you think about this one? This is the cuter of the three in my opinion."
    scene w1_0521 with dissolve
    "Once again, Mina did a little spin to let me a good look at the back."
    scene w1_0519 with dissolve
    "Hmm... what are my thoughts here?"
    hide screen textbox2 with dissolve

    menu:
        "Tell her it's cute, just like her. [red]\[Mina -1\]":
            $ Mina_Affection -= 1

            scene w1_0522 with dissolve
            show screen textbox2 with dissolve
            mc "I think it's pretty on brand. It's cute, just like you."
            "That was honestly the extent of my appraisal. What else could I say?"
            scene w1_0523 with dissolve
            mina "Nggh... I didn't bring you here to feed me lines. That's really not much to go off of."
            scene w1_0525 with dissolve
            mina "Let's try the last one then."

        "Tell her it projects a pretty strong impression. [gr]\[Mina +2\]":
            $ Mina_Affection += 2

            scene w1_0522 with dissolve
            show screen textbox2 with dissolve
            mc "I like it. It projects a girl-next-door sort of look. Which, depending on the role you're auditioning for, might help a casting director see just how well you'll fit."
            scene w1_0524 with dissolve
            mina "Hm... you might be right. The part I'm auditioning for is a college student, so this does seem kind of appropriate..."
            scene w1_0525 with dissolve
            mina "Let me get your opinion on the last one before I make a decision."

    scene w1_0526 with dissolve
    "With that, she disappeared behind the partition for a third time, accidently leaving the door ajar."
    scene w1_0527 with dissolve
    "Instinctually I reached out to close it, before I could realize what it might look like to Mina or any outside observers."
    scene w1_0528 with dissolve
    mct "(Ah--!)"
    scene w1_0529 with dissolve
    "I was stopped in place by a glimpse of the naked flesh of Mina's back, as she removed the top of her pink-jean jacket ensemble."
    if prAfterParty == True:
        "Not like I didn't get a fair look at her a couple of week's ago when we played that drinking game, but I got to admit the accidental glimpse adds something lurid to the equation."

    "I should probably just shut the door and stop looking..."
    hide screen textbox2 with dissolve
    stop music fadeout 3.0
    menu:

        "Don't be a creep, look away. [red]\[Toughness -1\]":
            $ toughness -= 1
            play music "music/ukulele-fun.mp3"
            show screen textbox2 with dissolve
            "Yeeeeah, let's not be a creepy asshat with no respect for a woman's privacy."


        "Let your eyeline linger a little longer. [gr]\[Toughness +1\]":
            $ toughness += 1
            show screen textbox2 with dissolve
            "No harm in looking a little longer, right? How could I not?"
            "Mina is just so... beautiful."
            play music "music/sneaky-snitch.mp3"
            mct "(I know it's kinda fucked up, but how could I not?)"
            jump w1MinaDatePerv

    scene w1_0539 with dissolve
    mc "..."
    scene w1_0541 with dissolve
    mina "So are you a film buff too?"
    scene w1_0540 with dissolve
    mc "Uh, what do you mean?"
    scene w1_0542 with dissolve
    mina "Well, Ian likes all those old Italian murder movies."
    scene w1_0543 with dissolve
    mc "The ones where killers wear black gloves, yeah?"
    scene w1_0542 with dissolve
    mina "Yeah, those!"
    scene w1_0540 with dissolve
    mc "No... not, not really. Though, I think you can thank my mother for getting him interested in those."
    mc "She used to let us watch them as kids, but they were never really my thing."
    scene w1_0543 with dissolve
    mc "{i}They never let plot get in the way of their stories{/i}, she always said."
    scene w1_0540 with dissolve
    mc "Me? I just like dumb action movies where people get thrown out windows..."
    jump w1MinaLookAway


label w1MinaDatePerv:

    scene w1_0530 with dissolve
    "Giving into temptation, I watched Mina begin to fidget out of her pants."
    "Taking the fabric and sliding them down her long ivory legs."
    "All the way down until all she had on were her bra and panties."
    scene w1_0531 with dissolve
    mina "So are you a film buff too?"
    mc "--!"
    scene w1_0539 with dissolve
    "Mina's attempt at continuing the conversation caused me to retreat, from fear of getting caught."
    scene w1_0540 with dissolve
    mc "Uh, what do you mean?"
    scene w1_0541 with dissolve
    mina "Well, Ian likes all those old Italian murder movies."
    scene w1_0543 with dissolve
    mc "The ones where killers wear black gloves, yeah?"
    scene w1_0542 with dissolve
    mina "Yeah, those!"
    scene w1_0540 with dissolve
    mc "No... not, not really. Though, you can thank my mother for getting him interested in those."
    mc "She used to let us watch them as kids, but they were never really my thing."
    scene w1_0543 with dissolve
    mc "{i}They never let plot get in the way of their stories{/i}, she always said."
    scene w1_0540 with dissolve
    mc "Me? I just like dumb action movies where people get thrown out windows."
    scene w1_0544 with dissolve
    "A lull in the conversation presented another opportunity to look, but do I really want to risk it again?"
    hide screen textbox2 with dissolve
    menu w1MinaVouyeur:
        "Don't be greedy, it's too risky":
            jump w1MinaLookAway

        "{color=#FF1493}\[Voyeur]{/color} Risk it, take another peek. [gr]\[Toughness +1\]" if history_voyeur == True:
            $ toughness += 1
            $ w1MinaCaught = True
            scene w1_0539 with dissolve
            show screen textbox2 with dissolve
            "Despite the potential disastrous results, the fear of getting caught looking felt more like a thrill to me than a deterrent."

        "{color=#696969}\[Voyeur] Risk it, take another peek.{/color}." if history_firestarter == True or history_stickyFingers == True:
            jump w1MinaVouyeur

    scene w1_0532 with dissolve
    "Craning my neck to peek through the door once more, I was fortunate to find Mina in an even more exposed state than before."
    mct "(Guess that last outfit must be strapless if she took her bra off. Lucky me!)"
    scene w1_0533 with dissolve
    "Suddenly, Mina lurched forward, giving me a generous view of side boob."
    mct "(--gh! The women in my life are so fucking stacked.)"
    "Too distracted by the visual feast in front of me, I failed to notice one critical element..."
    scene w1_0534 with dissolve
    "Mina had noticed me from the corner of her eye and now had it firmly planted on me."
    mc "..."
    scene w1_0535 with dissolve
    mina "..."
    scene w1_0536 with dissolve
    "Mina stood up and gave me an unadulterated view of her bare breasts."
    scene w1_0537 with dissolve
    mina "Can I help you with something?"
    scene w1_0536 with dissolve
    mc "Uh... the door was cracked and... uh..."
    mc "...and I was just transfixed by your beeeauuuuty?"
    "I gave an incredibly lame excuse, said with a comically untruthful inflection. "
    mina "..."
    scene w1_0538 with dissolve
    mina "Go back to waiting outside, idiot. Before someone else sees you peeping and mistakes you for a criminal."
    scene w1_0536 with dissolve
    mc "Sorry!"
    scene w1_0545 with cmet
    stop music fadeout 3.0
    mct "(Shit, I can't believe I let her catch me. What am I saying? I can't believe I even peeped in the first place!)"
    "...wait a minute."
    mct "(Is she not angry at me?)"
    mct "(She sounded more concerned with how it {b}looks{/b} from the outside than the impropriety of me sneaking a look.)"
    scene w1_0546 with dissolve
    "While I was contemplating my fuck-up, Mina appeared before me for a third time."
    play music "music/happy-whistling-ukulele.mp3"
    jump w1MinaDateOutfit


label w1MinaLookAway:
    stop music fadeout 3.0
    show screen textbox2 with dissolve
    scene w1_0541 with dissolve
    mina "Me too! Give me a gruff reluctant hero, some big lug of a villian, car chases, and exploding buildings any day of the week."
    scene w1_0545 with dissolve
    mina "Die hard is like the {b}best{/f} film ever! That or {i}Terminal Action{/i}?"
    scene w1_0543 with dissolve
    mc "What? The Samson Garcia one? You like that shitty movie? Me too!"
    mc "You know I've actually met him once?"
    scene w1_0542 with dissolve
    mina "For real?!"
    scene w1_0540 with dissolve
    mc "Yeah, he lives in town. I... uh, he gave a speech at my university."
    mc "The man loves talking about himself."
    scene w1_0546 with dissolve
    "While I was not-so-truthfully recounting my run in with the has-been Carnation Club patron, Mina appeared before me for a third time."
    play music "music/happy-whistling-ukulele.mp3"

label w1MinaDateOutfit:
    scene w1_0547 with dissolve
    mina "I have a feeling you'll be a fan of this one. What do you think? This is the sexiest of the three options."
    scene w1_0548 with dissolve
    "A vivid image of a cartoon wolf whistling materialized in my head."
    "She had emerged from the dressing room looking like a race queen."
    scene w1_0549 with dissolve
    "She gave me a better look at the back."
    mc "That looks great on you."
    "I said, without hesitation."
    scene w1_0550 with dissolve
    mina "Yeah, but which one do you think I should wear to the audition?"
    scene w1_0551 with dissolve
    mc "What's the role exactly?"
    scene w1_0550 with dissolve
    mina "I'm going to be playing a college student who is having an affair with her professor."
    scene w1_0551 with dissolve
    mc "Hm..."
    scene w1_0552 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Tell her she should go the professional route. [gr]\[MinaProfessional\]":
            $ MinaOutfitPro = True
            show screen textbox2 with dissolve
            mc "I'd go with the first option, the business-looking attire."
            scene w1_0553 with dissolve
            mina "Why that one?"
            scene w1_0552 with dissolve
            mc "It's a good blend of stylish and conservative. It's also just the right amount of sexy."
            mc "Leaves a lot to the imagination."
            scene w1_0554 with dissolve
            mina "You make a good point, I think I'll go with that one."

        "Tell her she should go the cute route. [gr]\[MinaCute\]":
            $ MinaOutfitCute = True
            show screen textbox2 with dissolve
            mc "I'd go with the second outfit, the girl-next-door-look."
            scene w1_0553 with dissolve
            mina "Why that one?"
            scene w1_0552 with dissolve
            mc "I think it'll help the casting director envision you in the role more easily. You'll look the part."
            scene w1_0554 with dissolve
            mina "You make a good point, I think I'll go with that one."

        "Tell her she should go the sexy route. [gr]\[MinaSexy\]":
            $ MinaOutfitSexy = True
            show screen textbox2 with dissolve
            mc "I'd go with the current outfit, you look stunning in it."
            scene w1_0555 with dissolve
            mina "I can probably already guess, but why that one?"
            scene w1_0552 with dissolve
            mc "Well, if the reading doesn't go so well... he won't notice because you look so good, y'know?"
            mc "You'll turn a lot of heads wearing that."
            scene w1_0554 with dissolve
            mina "You make a good point, I think I'll go with this one."


    mina "Thanks for your opinion, [mcf]. I'm glad I brought you along."
    if w1MinaCaught == True:
        scene w1_0555 with dissolve
        mina "I'll consider the little peep show you stole payment."
        scene w1_0552 with dissolve
        "I averted my eyes in shame."
        "Mina simply giggled at my consternation."
        scene w1_0556 with dissolve
        mina "Oh, lighten up. It's enough you feel bad about it."
        scene w1_0557 with dissolve
        "Mina, it turns out, is an extremely cool lady."

    else:
        mina "I owe you one!"
        scene w1_0552 with dissolve
        mc "No you don't, you're pleasant company and I'm having fun."
        scene w1_0556 with dissolve
        mina "Mmmmh, nope! I'll definitely pay you back one day. "

    scene w1_0558 with dissolve
    mina "Alright, I'll go change back into my clothes and then we can checkout."
    scene black with fade
    "..."
    if  MinaOutfitPro == True:
        scene w1_0561 with ccirclewipe
        clerk "Will this be all for today, Miss?"
        "Back at the register, Mina was paying for her new outfit."
        clerk "That'll be $397."
    if MinaOutfitCute == True:
        scene w1_0559 with ccirclewipe
        clerk "Will this be all for today, Miss?"
        "Back at the register, Mina was paying for her new outfit."
        clerk "That'll be $309"
    if MinaOutfitSexy == True:
        scene w1_0560 with ccirclewipe
        clerk "Will this be all for today, Miss?"
        "Back at the register, Mina was paying for her new outfit."
        clerk "That'll be $319"

    mct "(Excuse me?! For a single outfit?!)"
    mina "Yup! That'll be it! Thank you so much for your help earlier."
    "As I was distracted by the difference in our lifestyles, I failed to notice the click-clacking of rapidly approaching heels."
    scene w1_0562 with w21
    woman "Boo! Guess who, stud~♥"
    "A pair of hands clamped themselves over my eyes, followed by a familiar voice."
    "A voice belonging to..."
    hide screen textbox2 with dissolve

    menu:
        "Rosalind":
            show screen textbox2 with dissolve
            mc "...Rose, is that you?"
            fel "Really...? Wait, are you fucking with me?"


        "Felicia":
            show screen textbox2 with dissolve
            mc "Fancy running into you here, Felicia."
            fel "It's a small city."

        "Killian":
            show screen textbox2 with dissolve
            mc "Very funny, Ian."
            fel "Harhar, very funny."


    scene w1_0563 with w20
    mc "Nice to see you, Felicia."
    scene w1_0564 with dissolve
    mina "...oh?"
    scene w1_0565 with dissolve
    mina "Felish! Good to see you!"
    fel "You too, girl. Although I must say I'm surprised."
    scene w1_0566 with dissolve
    fel "To find the two of you together, alone..."
    fel "Heheh, [mcf] moves fast, doesn't he? And with his friend's woman too?"
    fel "Although I must say, I didn't expect you to be the kind of girl to play around."
    scene w1_0567 with dissolve
    mina "Stop projecting, slut. [mcf] was kind enough to keep me company today after Ian disappeared on me."
    scene w1_0568 with dissolve
    fel "For real? Again? You know, with your looks you could have any man wrapped around your finger. I don't know why you waste your time on immature boys."
    scene w1_0569 with dissolve
    mina "You're starting to sound like my mother."
    mina "{size=-10}About as old as her too...{/size=-10}"
    scene w1_0570 with dissolve
    fel "Yeesh, kitten has claws. Sorry!"
    scene w1_0571 with dissolve
    mina "No harm done. I know you mean well."
    mct "(I feel like I just experienced the emotional up-and-down of a three act play in the span of a minute...)"
    scene w1_0572 with dissolve
    "The clerk, who had been waiting for a break in conversation to make her move, finally spoke."
    clerk "It's nice to see you today, Mrs. Ford. We have your monthly order ready."
    clerk "Shall I go get it?"
    fel "Please do."
    scene w1_0573 with dissolve
    "With that, the clerk disappeared into the back."
    scene w1_0574 with dissolve
    fel "I'm glad I ran into you, [mcf]."
    fel "This saves me the trouble of calling you. I wanted to ask you out to dinner as way of an apology."
    scene w1_0575 with dissolve
    mc "Apology? For what?"
    scene w1_0576 with dissolve
    fel "I feel a little bad about surprising you the other day, despite knowing about our mutual connection to {i}that{/i} place."
    "Felicia not-so-deftly played the pronoun game, likely for Mina's benefit."
    scene w1_0577 with dissolve
    mina "Huh...? No fair, you guys got a secret...?"
    scene w1_0576 with dissolve
    fel "What do you say? You want to go out tomorrow night?"
    scene w1_0578 with dissolve
    "Felicia's a wild card. Having dinner with her might be fun."
    "Then again, maybe it'd be best if I decline and {b}limit my interaction with her to solely the club{/b}. Getting involved with a Carnation could be problematic down the road."
    hide screen textbox2 with dissolve

    menu:
        "Accept Felicia's dinner invitation. [gr]\[Felicia +1\]":
            $ Felicia_Affection += 1
            $ feliciaFlag = True

            show screen textbox2 with dissolve
            scene w1_0579 with dissolve
            $ history_felicia = "While on an outing with Mina, we ran into Felicia and she asked me out to dinner. I accepted."
            $ unread_felicia = True
            play sound "sound effects/notification.wav"
            show bioupdate with dissolve
            mc "Yeah, sure."
            "Despite her involvement with the club, I'd be lying if I said I didn't enjoy spending time with her."
            if toughness >= 18:
                "Plus, who would turn down the chance to score with a beautiful woman?"


        "Decline Felicia's dinner invitation. [red]\[Felicia -3\]":
            $ Felicia_Affection -= 3
            $ feliciaDinnerDecline = True

            show screen textbox2 with dissolve
            scene w1_0580 with dissolve
            $ history_felicia = "While on an outing with Mina, we ran into Felicia and she asked me out to dinner. I declined, deciding to limit my interaction with the Carnation strictly to club business."
            $ unread_felicia = True
            play sound "sound effects/notification.wav"
            show bioupdate with dissolve
            mc "Tomorrow's no good for me sorry."
            scene w1_0581 with dissolve
            fel "What about Friday?"
            scene w1_0580 with dissolve
            mc "Sorry."
            scene w1_0582 with dissolve
            fel "...I get it, I get it."
            fel "Strictly business, eh?"
            mina "I don't get it!"

    scene w1_0583 with dissolve
    clerk "Ah, Mrs. Ford. We had a little ordering issue with the sizing of one of the items, would you like to try it on or should I just remove it from the order?"
    scene w1_0584 with dissolve
    fel "I'll see if it fits, first."
    scene w1_0585 with dissolve
    fel "It was nice running into you two. You two love birds don't get into too much trouble without me, okay?"

    if feliciaFlag == True:
        fel "As for [mcf], I'll see you tomorrow night, stud."
    else:
        fel "As for [mcf], I'll see you this weekend, {i}Sir{/i}."

    scene w1_0586 with dissolve
    mina "I'm a little confused about some of that, but I gather you two have become pretty close! That's great."
    scene w1_0588 with dissolve
    mina "Just be careful not to get hurt, [mcf]. She's married, you know?"
    scene w1_0587 with dissolve
    "Oh, I {i}know{/i}."
    scene w1_0588 with dissolve
    mina "Normally I'd have a problem with that, but her husband's a... eugh."
    scene w1_0589 with dissolve
    mina "What I'm trying to say is just don't get any big ideas about her."
    scene w1_0587 with dissolve
    mc "Where's this coming from?"
    scene w1_0589 with dissolve
    mina "What do you mean? The two of you are my friends. It's only natural to be concerned about either of you."
    scene w1_0587 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Tell Mina she's worrying for nothing.":
            show screen textbox2 with dissolve
            mc "You don't have anything to worry about."
            mc "I know whatever Felicia and I are doing is frivolous."

        "Thank Mina for her concern. [gr]\[Mina +1\]":
            $ Mina_Affection += 1
            show screen textbox2 with dissolve
            mc "Thanks, Mina. Thanks for looking out."
            scene w1_0590 with dissolve
            mina "Of course!"

    scene w1_0591 with dissolve
    mina "I'll drive you home now, if you don't mind. I've got to be at my folks for a dumb dinner thing later."
    mc "Sure, let me carry your bags."
    stop music fadeout 3.0
    scene black with fade
    "......"
    "..."
    mct "(I got to get a car of my own...)"
    scene w1_0592 with blinds
    play music "music/a-brand-new-start.mp3"
    mina "Thanks again for today."
    mc "You said you'd stop it with that, remember?"
    scene w1_0593 with dissolve
    mina "Hehehe, what can I say, I'm a little liar. You didn't know that about me?"
    scene w1_0594 with dissolve
    "Mina struck an innocent looking pose, one that if she so inclined, could be used for terrible evil against men."
    mc "I'll keep that in mind for the future."
    scene w1_0595 with dissolve
    mina "Heheh~♥"
    scene w1_0594 with dissolve
    mc "Well, I hope your audition goes well. You'll let me know?"
    scene w1_0596 with dissolve
    mina "Of course! You'll be the first I call. Anyway, I should go..."
    scene w1_0594 with dissolve
    mc "......"
    scene w1_0597 with dissolve
    mina "..."
    scene w1_0598 with dissolve
    mina "Awww, c'mere!"
    scene w1_0599 with dissolve
    play sound "sound effects/notification.wav"
    $ Mina_Relations = "Friend"
    show relationmina with dissolve
    "With a sprightly hop, Mina launched herself into me with abandon, pressing her soft body firmly into mine."
    scene w1_0600 with dissolve
    "She smelled of an oddly pleasant mixture of lavender shampoo and sweat."
    mct "(Man, she's warm and soft... this is nice.)"
    hide screen textbox2 with dissolve

    default dynamicChoice2 = ""
    if Mina_Affection < 16:
        $ dynamicChoice2 = "{color=#f00}[Mina -1]"
    else:
        $ dynamicChoice2 = "{color=#0f0}[Mina +1]"

    menu:
        "Keep it to a chaste touch.":
            show screen textbox2 with dissolve
            mc "......"
            mina "..."
            scene w1_0599 with dissolve
            "After ten or so seconds, the hug came to an end."
            scene w1_0605 with dissolve
            mina "Heh, I see you're a hugging person too."
            scene w1_0607 with dissolve
            mina "See you around, [mcf]!"
            scene black with fade

        "Rest your hand on her tush [dynamicChoice2]":
            scene w1_0601 with dissolve
            show screen textbox2 with dissolve
            "I slowly creeped my hands down the small of her back and brought them to a stop at her waist."
            scene w1_0602 with dissolve
            "After allowing a few moments to pass, I let my hands dip down a little further until they rested shamelessly on her ass."

            if Mina_Affection < 16:
                $ Mina_Affection -= 1
                scene w1_0603 with dissolve
                mina "Hands a little too low there, mister. Knock it off."
                "Shit, she noticed..."
                scene w1_0599 with dissolve
                "After ten or so seconds, the hug came to an end."
                scene w1_0605 with dissolve
                mina "Heh, I see you're a hugging person too."
                scene w1_0607 with dissolve
                mina "See you around, [mcf]!"
                scene black with fade

            else:
                $ Mina_KLove -= 1
                scene w1_0604 with dissolve
                mina "Mmmhh..."
                "I could be imagining things, but I swear Mina let out a little coo."
                scene w1_0609 with dissolve
                "After ten or so seconds, the hug came to an end."
                scene w1_0606 with dissolve
                mina "Heh, I see you're a hugging person too."
                scene w1_0608 with dissolve
                mina "See you around, [mcf]!"
                scene black with fade

    stop music fadeout 3.0
    $ history_mina = "Mina and I had a nice evening out. Despite it being me just mostly sitting around, it was a pleasant experience. Feeling like she's more a and headed inside my apartment, unsure of how exactly to spend the rest of my time."

    if roseSeduceFlag == True:
        hide screen textbox2 with dissolve
        hide screen qmenu with dissolve
        play sound "sound effects/sting-bluesy-vibes.wav"
        scene transitionrosalind03 with blinds
        $ renpy.pause(6, hard=True)
        jump w1RoseFlag

    else:
        jump w1June02End

label w1MinaDateSkip:

    play sound "sound effects/call-end.wav"
    hide mina-call with dissolve
    scene w1_0624 with dissolve
    mct "(Alright, just turned down an afternoon outing with a model...!)"
    mc "......"
    mc "..."
    scene w1_0610 with dissolve
    mct "(Guess I'll just go jerk off in the shower now?)"
    scene black with wet
    "--so that's exactly what I did."
    scene w1_0611 with fade
    "I whiled away the rest of the day by attempting to cook a couple of recipes I found online, failing, and then ultimately settled on ordering takeout."

    if roseSeduceFlag == True:
        jump w1RoseFlag
    else:
        jump w1June02End

label w1RoseFlag:

    $ date = "june02night"
    if _in_replay:
        show transitionrosalind03 with cmet
        show screen textbox2 with dissolve
        "Please set [mcf]'s personality (toughness score) for this replay."
        hide screen textbox2 with dissolve
        menu:
            "Nice guy (Toughness: 0)":
                $ toughness = 0
            "Mischievous (Toughness: 18)":
                $ toughness = 18
            "Asshole (Toughness: 30)":
                $ toughness = 30
        show screen textbox2 with dissolve
        "Did [mcf] take advantage of Rosalind when they first met?"
        hide screen textbox2 with dissolve
        menu:
            "Yes.":
                $ roseTakeAdvantage = True
            "No.":
                pass
        show screen textbox2 with dissolve

    scene w1_0612 with circlewipe
    play sound "sound effects/door-bell.wav"
    show screen textbox2 with dissolve
    show screen qmenu with dissolve
    "*Ding, dong!*"
    show june02night with squares
    play music "music/george-street-shuffle.mp3"
    "Later that night, in the midst of nothing in particular, someone was at the door."
    scene w1_0613 with dissolve
    mct "(Who could that be? Ian?)"
    scene w1_0614 with dissolve
    mct "(No, if it was him, he'd just barge right in.)"
    scene w1_0615 with dissolve
    mct "(Mom would call first, so... someone from the club? A neighbor maybe?)"
    scene w1_0616 with dissolve
    mc "Who is it?"
    rose "It's Rosalind. I'm feeling kind of  embarrassed out here, could you let me in please?"
    mct "(Why would she be embarrassed?)"
    "From behind the door, I could sense a sliver of panic in her voice."

    scene w1_0617 with fade:
        subpixel True
        yalign 0.1
        xalign 0.6

    play sound "sound effects/door-open.wav"
    "Once allowed in, she practically tripped over herself to get past the door's threshold."
    "Not that I didn't instantly understand why. It seemed she had made the trek up to my apartment in a rather conspicuous indigo dress, no doubt drawing the attention of anyone she passed by in the building."

    scene w1_0617:
        subpixel True
        yalign 0.1
        xalign 0.6
        linear 5 yalign 1.0

    mct "(They probably mistook her for a prostitute, which... I guess she kind of is for this month.)"
    scene w1_0619 with dissolve
    rose "Thanks! Uh, I hope I'm not interrupting anything by arriving out of the blue like this."
    scene w1_0618 with dissolve
    hide screen textbox2 with dissolve
    menu:
        "Reassure her that you weren't doing anything.":
            scene w1_0621 with dissolve
            show screen textbox2 with dissolve
            mc "No, you're good. I wasn't really doing much of... anything, really."
            scene w1_0619 with dissolve
            rose "Good! When Mr. Beaufort gave me your address earlier, he told me to surprise you."

        "Ask her how she got your address.":
            scene w1_0620 with dissolve
            show screen textbox2 with dissolve
            mc "How do you know where I live?"
            scene w1_0619 with dissolve
            rose "Oh...! Uh, Mr. Beaufort gave it to me. He's the one who told me not to call first."


    scene w1_0622 with dissolve
    mc "He did, did he?"
    scene w1_0619 with dissolve
    rose "Mind if we sit down?"
    scene w1_0623 with dissolve
    mc "Sure. Let's go to the living room. You want something to drink?"
    scene black with fade
    rose "You got any wine?"
    mc "You're in luck. I'm not much of a drinker, but this place came stocked."
    scene w1_0626 with cwside
    rose "You're not having any?"
    scene w1_0628 with dissolve
    mc "Just tea for me. It's better for my sleep."
    scene w1_0629 with dissolve
    rose "You've got a nice home."
    "Rosalind's eyeline passed around the expansive room, as if silently commenting on the square footage a single college student like me has no use for."
    scene w1_0627 with dissolve
    mc "To be honest, it doesn't really feel like home to me. Not sure if it ever will."
    scene w1_0626 with dissolve
    rose "That's a difficult feeling to capture, in my experience."
    scene w1_0628 with dissolve

    if toughness >=18:
        mc "So... why are you here, Rose?"
    elif toughness >= 11:
        mc "If you don't mind me asking, what do I owe this visit too?"
    else:
        mc "So, how can I help you?"

    scene w1_0625 with dissolve
    "I may have asked the question, but just taking in the sight of Rosalind in that revealing outfit, breathing in the thick perfume she had spritzed on, and the time of night for the visit - had given me a {i}certain{/i} expectation."
    "I recalled our outing to the coffee shop, Rosalind's little game of footsy, and the case of blue balls she left me with - a scene from which I hadn't exactly grasped her motivation for yet."
    scene w1_0630 with dissolve
    rose "Well, uh..."
    scene w1_0631 with dissolve
    rose "*GLUG GLUG GLUG*"
    "Rosalind nervously tossed back her glass, sucking down its contents in one brisk motion."
    scene w1_0632 with dissolve
    rose "Can I have another glass, please?"
    scene w1_0633 with dissolve
    mc "Sure, let me get that for you..."
    scene w1_0634 with dissolve
    "I poured Rosalind another glass."
    scene w1_0635 with dissolve
    rose "Thank you, Mr. [mcl]."
    scene w1_0625 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Tell her to use your first name. [gr]\[Rosalind +1\]":
            $ Rosalind_Affection += 1
            scene w1_0627 with dissolve
            show screen textbox2 with dissolve
            mc "You can just call me [mcf]."
            mc "I mean you've got 15 years on me. You're almost old enough to be my mom. It's kind of weird for you to be calling me mister."
            scene w1_0626 with dissolve
            rose "...thank you for the wine, [mcf]."
            scene w1_0628 with dissolve
            mc "You're welcome, Rose."


        "Let it pass. You like the deference.":
            $ rosePolite = True
            scene w1_0628 with dissolve
            show screen textbox2 with dissolve
            mc "You're welcome, Rose."

    mc "Now, back to why you're here..."
    scene w1_0631 with dissolve
    rose "*GLUG GLUG*"
    "Again she took another swig of wine, this time in a more conservative fashion."
    scene w1_0626 with dissolve
    stop music fadeout 3.0
    rose "I wanted to see you."
    "She said it matter-of-factly, in a suggestive tone that played like honey to my ears."
    scene w1_0627 with dissolve

    if perk_socialButterfly == True:
        mc "You wanted to {i}see{/i} me?"
    else:
        mc "Is that... so?"

    scene w1_0630 with dissolve
    rose "Yeah, about where we left off..."
    scene w1_0631 with dissolve
    rose "*GLUG GLUG GLUG*"
    scene w1_0636 with dissolve
    "Rosalind tilted her head and knocked back the remainder of her glass before setting it aside."
    rose "If I recall correctly, I worked you up and split, right?"
    scene w1_0637 with dissolve
    play music "music/philly-crew.mp3"
    rose "I felt really bad about it for a whole week. That was unkind of me."
    "The tail-end of her personal indictment came out in a hushed, beguiling tone."
    scene w1_0638 with dissolve
    rose "Hehe~♥"

    if rosePolite == True:
        rose "Seems you're a healthy man, Mr. [mcl]. You're already growing hard."
    else:
        rose "Seems you're a healthy man, [mcf]. You're already growing hard."

    scene w1_0639 with dissolve
    mc "Don't act surprised. You know exactly what you're doing."
    mct "(What's her game here?)"
    "Despite her hold on my reptilian brain, something didn't feel right."
    scene w1_0640 with dissolve
    rose "You don't mind a girl taking a peek, right?"
    scene black with fade
    "Without waiting for me to reply, Rosalind tugged at my boxer shorts, my body lifting itself up to accommodate her request despite my uncertainty."
    scene w1_0641 with fade

    if roseTakeAdvantage == True:
        rose "Wow! That's much bigger than I remember it..."
        mc "Guess you had other things on your mind at the time."

    else:
        rose "Wow, you're... huge!"

    scene w1_0642 with dissolve
    "Softly taking my half-flaccid cock in her lotion-smooth hand, she began to gently jerk it in an effort coax out an erection."
    scene w1roseSoftHJ with dissolve
    "Naturally, it didn't take her long to succeed in her mission. Soon my cock was standing at full mast, twitching eagerly in anticipation for what's to come."
    scene w1_0645 with dissolve
    mc "Rose, not that I'm opposed to ANY of this, but... why are you doing this?"
    scene w1_0646 with dissolve
    rose "Because I want this? Because you want to...?"

    if rosePolite == True:
        rose "Don't think too much about it, Mr. [mcl]."
    else:
        rose "Don't think too much about it, [mcf]."

    "Her whispered words were carried on a puff of hot breath, sending a shiver that started from my ear canal and extended all the way down to my toes."
    scene w1RoseSeduce1 with dissolve
    "Rosalind, picking up on my reaction, immediately began to attack and nibble at my earlobe."
    "Meanwhile her hand continued to caress my cock at an unhurried pace. Some might call it an agonizing pace, but..."
    "There was a tenderness to her touch that warmed my body and put my mind in a dream-like stupor. It was a safe feeling of comfort."
    scene w1_0650 with dissolve
    "Soon, she moved from my ear down to my neck."
    mc "--ah!"
    "My body gave an honest response to her efforts."
    scene w1_0651 with dissolve
    rose "Mmm, I love a man who's not afraid to moan."
    mc "I didn't do it on purpose."
    rose "Either way, it's so hot..."
    scene w1RoseSeduce2 with dissolve
    "Encouraged by my response, Rosalind shifted her efforts to a more steady pace."
    mc "--gha!"
    mct "(She's so damn slutty, way more than she lets on...!)"
    scene w1_0655 with dissolve
    "I felt like putty in Rosalind's hands, as she easily cradled the back of my head and tilted it toward her."
    "There she locked her unblinking eyes on mine, with an expression that was a mystifying mixture of lust and affection."
    rose "You don't have anything to worry about, just relax and let me take care of you, [mcf]."
    scene w1RoseSeduce3 with dissolve
    "She used my name like a savory punctuation mark to a lewd promise."
    "The paranoid part of me thought it felt strategic, like a move made to pull me even deeper into the loving fantasy she was authoring."
    "One that, to be honest, didn't feel like such a bad illusion to get lulled into."
    rose "You're a kind person."

    if roseTakeAdvantage == True:
        rose "If you weren't, you wouldn't have apologized for acting on your feelings the night we met."
    else:
        rose "You could've taken advantage of me the night we met, but you didn't."

    rose "I like you, [mcf]. Do you like what I'm doing?"
    "She asked me fully knowing the answer already, boring into my eyes with her own."
    mc "{size=-10}You know I do...{/size=-10}"
    "My voice came out wispy, dulled by sexual desire and stimulation."
    rose "Good... I only want to make you happy."
    "Her voice, on the other hand, was melodic."
    rose "I want you to cum for me. You'll do that for me, won't you baby?"
    rose "I can make you feel this good anytime you want, if you'll just do me a favor..."
    mc "H-huh?"
    "Confidant she had me ensnared, she sprung her trap."
    rose "I need your help with winning the exhibition."
    scene w1_0658 with flash
    stop music
    mct "{size=+30}Stop!{/size=+30}" with vpunch
    "In a fit of anger, I reflexively pushed the scheming woman off of me."
    play music "music/leaving-home.mp3"
    mct "{size=+20}You fucking...!{/size=+20}" with vpunch
    "With my very last ounce of control, I swallowed the uglier part of what I wanted to say."
    rose "I-I-I d-didn't mean to--"
    scene w1_0659 with fade
    mc "You thought you'd try and manipulate me, is that it?"
    scene w1_0660 with dissolve
    rose "It's not like that! Not... not exactly..."
    scene w1_0659 with dissolve
    mc "I wonder what Mrs. Pulman would have to say about you trying to cheat?"
    scene w1_0661 with dissolve
    rose "Oh, no no NO! Please, please, please, please, PLEASE don't tell her!"
    scene w1_0662 with dissolve
    "Rosalind looked up at me with pleading eyes and such a panic stricken-expression that I began to feel {i}guilty{/i} over feeling what should be a normal reaction to getting played."
    mct "(Wait... why am I getting so irrationally mad here?)"
    hide screen textbox2 with dissolve

    menu w1RoseGovernor:
        "{color=#FF1493}\[Governor]{/color} Try to productively manage your anger. [gr]\[Rosalind +2\]" if trait_governor == True:
            $ Rosalind_Affection += 2
            scene w1_0663 with dissolve
            show screen textbox2 with dissolve
            "Before I could further speak without thinking, I stopped and took a deep breath."
            mc "Inhale..."
            mc "Exhale..."
            scene w1_0664 with dissolve
            mc "{size=-10}Inhale... exhale... Now, calm down [mcf]. Take it easy.... take it easy.{/size=-10}"
            "It was a small mantra my mother had taught me when I was a child to help calm myself down whenever I felt angry."

            if kat_polite == True:
                "Once I thought about it rationally, I had no reason to be this heated. In a disinterested sense, I know the way the world is and how desperate Rosalind must be to participate in Mrs. Pulman's game."
            else:
                "Once I thought about it rationally, I had no reason to be this heated. In a disinterested sense, I know the way the world is and how desperate Rosalind must be to participate in Kathleen's game."

            "It's only natural she'd try to win, in whatever way she could."
            scene w1_0665 with dissolve
            "Plus, a personal level, Rosalind is nothing to me. Just an acquaintance I had met a few times. It's not like her scheming is a personal betrayal."
            mct "(It only {i}feels{/i} that way because on some level, I like her. She reminds me of...)"
            stop music fadeout 3.0
            scene w1_0666 with dissolve
            mc "*sigh* I'm sorry for yelling at you."
            rose "B-but--"
            mc "Don't worry, I'm not going to mention this to Mrs. Pulman."
            scene w1_0667 with dissolve
            rose "I'm sorry too!"
            scene w1_0668 with dissolve
            mc "I don't blame you. I don't know your exact circumstances, but I probably would do the same if I were in your shoes."


        "Speak your feelings.":
            scene w1_0669 with dissolve
            show screen textbox2 with dissolve
            mc "You are aware that I like you, right? Of course you are."
            mc "It was obvious when I asked you out for coffee. That's the reason you said yes in the first place."
            mc "You just saw a chance to get ahead, with no regard for my feelings. Am I right?"
            rose "..."
            mc "Well?!" with vpunch
            scene w1_0670 with dissolve
            rose "It's not like that. I do think you're nice, but, but, aarg...!"
            stop music
            scene w1_0671 with flash
            rose "Don't get sanctimonious with me, you brat!"
            "She rose to her feet in a fit of anger that matched my own, scolding me like a child."
            rose "You're on the payroll of a vile witch that profits off of desperate women!"
            if roseTakeAdvantage == True:
                rose "Need I remind you that you fucked my face the first time we met?"
            rose "It's not like I'm taking part in this because I want to!"
            rose "Boo-hoo! Your feelings are hurt? So what? I have to endure utter humiliation JUST FOR A CHANCE to get my goddamn life back....!" with vpunch
            rose "So yeah, I thought I'd try to take advantage of the situation. Not like you weren't getting anything out of it!"
            scene w1_0672 with dissolve
            mc "..."
            rose "..."
            "I was speechless. The rational part of my brain knew she had a point."
            "I knew the way the world is and how troubled Rosalind must be to participate in this game."
            "It's only natural she'd try to win, in whatever way she could."
            scene w1_0668 with dissolve
            mc "*sigh* I'm sorry for yelling at you."
            scene w1_0673 with dissolve
            rose "... and I'm sorry too."
            scene w1_0668 with dissolve


        "{color=#696969}\[Governor] Try to productively manage your anger. {/color}" if trait_tireless == True or trait_inquisitive == True:
            jump w1RoseGovernor

    mc "Let's sit back down."
    mct "(First, I should put my pants on.)"
    "You can't really have a serious conversation with your dick hanging out, can you?"
    scene w1_0674 with circlewipe
    play music "music/a-lost-map-of-a-heaven.mp3"
    rose "Please understand, I wouldn't have tried this if I didn't need to. The woman sitting here, it's... it's not me."
    scene w1_0675 with dissolve
    mc "I can appreciate that."
    scene w1_0676 with dissolve
    "It was true, I could."
    "I feel like I'm going to become an entirely different person by the end of this summer."
    scene w1_0675 with dissolve

    if w1RoseGonzo == True:
        mc "I know you're in debt, but what kind of trouble are you exactly in, Rose?"
    else:
        mc "What kind of trouble are you exactly in, Rose?"

    scene w1_0677 with dissolve
    rose "The bad kind. I owe money to some very serious men."
    scene w1_0675 with dissolve
    mc "How did that happen?"
    scene w1_0677 with dissolve
    rose "Before he split, my piece of shit husband borrowed money from loan sharks."
    rose "Used it to invest into the bottom rung of a Ponzi scheme, right before the whole thing collapsed."
    rose "That was just one in a long series of shitty investments. He had already squandered what little savings we had by that point."
    rose "He went as far as even taking out a second mortgage on our home, but... the most amazing feat of his idiocy was borrowing money from criminals for his latest get rich scheme."
    scene w1_0678 with dissolve
    mc "Oh..."
    scene w1_0677 with dissolve
    rose "When he realized how screwed he was, he bailed."
    scene w1_0678 with dissolve
    mc "Leaving you on the hook."
    scene w1_0679 with dissolve
    rose "Not just me. If it was just me I'd just..."
    scene w1_0680 with dissolve
    rose "I have my daughter to worry about!"
    scene w1_0681 with dissolve
    "She looked me straight in the eye as she said this, brimming with determination."

    if kat_polite == True:
        mc "So you turned to Mrs. Pulman's charity, only to find your way here..."
    else:
        mc "So you turned to Kathleen's charity, only to find your way here..."

    scene w1_0682 with dissolve
    rose "It's disgusting what she's doing, but in her messed up offer lies a chance to give my daughter a normal life."
    scene pr0036 with pixellate
    rose "Even if it means I have to whore myself out to that awful place...!"
    scene w1_0681 with pixellate
    "Rosalind was a good woman. A good mother. This much I was certain of, despite her attempt to seduce me. That said..."
    mc "Here's the thing, it's not like I don't want to help you... I feel for you, honestly."
    scene w1_0683 with dissolve
    mc "It's just I don't see how I CAN help you. For one, I'm new at the club. Secondly, I don't even know if I have the power to affect ANYTHING during the exhibition."
    mc "What would you have me do?"
    scene w1_0684 with dissolve
    rose "..."
    scene w1_0685 with dissolve
    rose "I... just be my {b}ally{/b}. Try to find ways you can help me if you can."
    rose "You don't have to make any promises besides that. If you do that..."
    rose "I'll do whatever you want me to do."
    scene w1_0681 with dissolve
    mct "(Hold up, she still wants to make the deal even with zero guarantee?)"
    mct "(No shit, [mcf]. She's desperate.)"
    "I'm at a crossroads here. If I flat out refuse her, it's likely she {b}won't ever want to see me outside the club{/b}."
    "...but do I really want to potentially stick my neck out for her?"
    hide screen textbox2 with dissolve

    menu:
        "Tell Rosalind you accept her deal. [gr]\[Toughness +3\]":
            $ toughness += 3
            $ roseDealFullAcceptance = True
            $ roseFlag = True
            show screen textbox2 with dissolve
            mc "Alright, I accept your deal. If there's anything I can do, I'll help you."
            scene w1_0686 with dissolve
            mc "In exchange, you'll be my personal slut for the next four weeks until the exhibition is ov--."


        "Tell Rosalind you'll help her for free. [gr]\[Rosalind +5\] [red]\[Toughness -2\]":
            $ toughness -= 2
            $ Rosalind_Affection += 5
            $ roseFlag = True
            show screen textbox2 with dissolve
            mc "Alright, I'll help you, but... I'm not going to take advantage of the situation."
            scene w1_0686 with dissolve
            mc "You don't have to do anything for my help."
            scene w1_0687 with dissolve
            rose "Thank you for being so kind, but..."
            rose "I have to. The terms are non-negotiable."
            scene w1_0688 with dissolve
            mc "You {i}have{/i} to whore yourself out to me? Don't be ridiculous."
            scene w1_0687 with dissolve
            rose "I'm sure this seems crazy to you, but it's a matter of pride for me."
            rose "I don't want to come out of this feeling like I owe a debt to anyone else or... give you room to change your mind."
            scene w1_0688 with dissolve
            mc "You're right, that sounds real, {b}real{/b} dumb. Like incredibly stupid."
            scene w1_0687 with dissolve
            rose "What's the problem? You find me attractive, don't you?"
            scene w1_0688 with dissolve
            mc "Obviously."
            scene w1_0687 with dissolve
            rose "Then there should be no issue if I say it's okay."
            scene w1_0689 with dissolve
            rose "Not to mention, you're an attractive and nice man. I wouldn't really mind fooling around with you."
            scene w1_0690 with dissolve
            mc "...fine, alright."
            mc "I accept your deal. If there's anything I can do, I'll help you."
            mc "In exchange, you and I will have some fun together over the next month, until the summer exhibition concludes."
            mc "The stipulation being that fun is anything I determine it to be, which might just mean us grabbing dinner or watching a crappy movie. I hope you're okay with--"



        "Tell Rosalind there's nothing you can do. [red]\[Rosalind -10\]":
            $ Rosalind_Affection -= 10
            jump w1RoseFlagDeny

    stop music
    scene w1_0692 with cmet
    with hpunch
    rose "Thank you...! Just do what you can, anything!"
    play music "music/covert-affair.mp3"
    play sound "sound effects/notification.wav"
    $ Rosalind_Relations = "Partner in Crime"
    show relationrose with dissolve
    "In a fit of happiness, Rosalind surged forward and pulled me into her arms."
    rose "Thank you, thank you, thank you!"
    scene w1_0693 with dissolve
    "All the nervous energy that had been simmering under the surface during our previous conversation had finally found an outlet, taking the form of a deep and intimate hug that pulled my head deeper and deeper into the soft valley on her chest."
    mc "mmhn, mho ghuaranteesh, rhembemrh?"
    "I tried to remind Rosalind to keep her expectations in check, but all I managed to do was mumble a bunch of gibberish into her breasts. Not the worst way of shouting into the wind, I'll admit."
    "With such an intimate embrace, naturally it wasn't long before the embers of our previous encounter reignited into full blown sexual desire. I could feel myself once again growing hard once more."
    scene w1_0694 with dissolve
    rose "Oh...? What's this?"


    if roseDealFullAcceptance == False:
        rose "For someone who didn't want to take advantage of little me, you sure have a funny way of showing it."
    else:
        rose "Looks like you're ready to cash in on our deal. You said something about me being your personal slut?"

    "Rosalind adopted a playful and mirth-filled tone, one that I thought keenly suited her more than the gloom and misery it was replacing."

    if roseDealFullAcceptance == False:
        mct "(Maybe I'm just imagining this, but could she actually be enjoying this? Or is that just a wishful male fantasy on my part to make me feel better about our arrangement...?)"
        mct "(Oh damn it, just stop thinking and kiss her you moron.)"

    else:
        mct "(Maybe I'm just imagining this, but could she actually be into this? Or is that just me thinking with my dick...?)"
        mct "(Guess I'll just have to find out.)"

    scene w1_0695 with dissolve
    rose "--mh!"
    "I brought the teasing woman closer and pulled her into a kiss."
    scene w1_0696 with dissolve
    rose "Mmmh..."
    "She was quick to return my affection, parting her lips and allowing my tongue unimpeded entry into her mouth."
    "However, Rosalind wasn't content in just being a passive observer in our kiss. For her part, she intertwined her own tongue with mine, fighting to gain passage into my mouth."
    scene w1_0697 with dissolve
    "The tight grip she had on me during our hug had all but vanished. In its place, the full figured woman took on an odd sense of weightlessness in my arms."
    "Not just her, but me too. As our kiss intensified, my heartbeat quickened and my perception began to dull. Maybe it was simply due to the blood going to my dick, but I felt a sense of buoyancy in our embrace."
    "Even in the throes of lust, Rosalind had a calming influence that took me to a safe place. I wanted our kiss to go on forever..."
    scene w1_0698 with dissolve
    "...but she had other ideas."
    scene w1_0699 with dissolve
    rose "Let's {i}shake{/i} on our deal, [mcf]."
    scene w1_0698 with dissolve
    "She peered at me with eyes full of desire, giving life to my honest thoughts."
    scene w1_0700 with dissolve
    mc "...you're so beautiful, Rose."
    scene w1_0698 with dissolve
    mct "(Her deadbeat husband's a fucking moron to give this up.)"
    scene w1_0699 with dissolve
    rose "Let me get out of this ridiculous dress first."
    scene black with fade
    "With a light touch she parted from our embrace, creating an agonizing distance between us. What had been so acutely warm and reassuring was now cold. Not that I could really complain, since..."
    scene w1_0701 with curtains
    rose "It's too embarrassing... I don't know if I can turn around."
    scene w1_0702 with dissolve
    "Rosalind was playing coy, using the flesh of her bare back and as a barricade to conceal her nakedness."
    "Of course, it was all an charade, an act of showmanship preceding the big reveal."

    scene w1_0703 with dissolve
    if toughness >= 18:
        mc "Cut the bashful bride act. Turn around. Let me get a good look at you."
    else:
        mc "It's not nice to tease a boy. Let me get a good look at you."

    scene w1_0704 with w20
    mct "(Not that I wasn't enjoying the view from behind.)"
    scene w1_0705 with dissolve
    "Shooting me a smile from over her shoulder, Rosalind shifted position, giving me a hard look at her naked body in profile."
    rose "Impatient, aren't you?"
    rose "You see something you want?"
    scene w1_0706 with dissolve
    "I raised my finger and signaled for Rosalind to come closer."
    scene w1_0707 with dissolve
    "Rosalind was happy to oblige, the shrinking divide between us growing smaller and smaller until..."
    scene w1_0708 with dissolve
    "She was close enough to touch, which is exactly what I did."
    scene w1_0709 with dissolve
    "Methodically, I made my way up her body. First, planting kisses on her soft tummy."
    rose "Hehe, that tickles..."
    scene w1_0710 with dissolve
    "Peck by peck I made my way up to her breasts, kissing the tops and bottoms of the bountiful mounds with an utmost sense of worship."
    scene w1_0711 with dissolve
    "Finally, we stood face to face, eyes honed in on one another like there was nothing else in the world."
    rose "Don't make a gal beg now..."
    "As if I even needed the encouragement..."
    scene w1_0712 with dissolve
    "Lifting Rosalind into the air, I spun on the heels of my feet and gently laid her down on the couch."
    scene w1_0713 with dissolve
    "Positioned beneath me, she matched my gaze with a need-filled stare of her own." with vpunch
    "It was a look that made me forget my own pleasure for the moment."
    scene w1_0714 with dissolve
    "With that clear goal in mind, I started on the task of unveiling her sex..."
    scene w1_0715 with dissolve
    "...sliding her panties past her milky white thighs, down to her ankles, until they slipped effortlessly off her feet."
    scene w1_0716 with dissolve
    rose "Looks like you've got me fully unwrapped, Mr. [mcl]."

    if rosePolite == False:
        scene w1_0717 with dissolve
        mc "I told you to just call me [mcf]."
        scene w1_0716 with dissolve
        rose "Ever consider I enjoy calling you that? You don't mind it occasionally, I hope..."

    scene w1_0718 with dissolve
    rose "{b}Oh...?{/b} You're not just going to stick it in. My husband never really cared to..."
    stop music fadeout 3.0
    hide screen textbox2 with dissolve

    menu:
        "Tell her not to mention her husband.":
            scene w1_0719 with dissolve
            show screen textbox2 with dissolve
            mc "Maybe don't bring up other guys when I'm about to eat you out, eh?"
            scene w1_0720 with dissolve
            rose "Hehe... sorry."

        "Insult her husband. [gr]\[Toughness +1\] \[Rosalind +1\]":
            $ toughness += 1
            $ Rosalind_Libido += 1

            scene w1_0719 with dissolve
            show screen textbox2 with dissolve
            mc "No offense, but your husband is a pussy who ran out on you. It's a low bar."
            scene w1_0721 with dissolve
            rose "Heh, good point..."

        "Let her comment pass":
            show screen textbox2 with dissolve
            pass

    scene w1_0722 with dissolve
    play music "music/guiton-sketch.mp3"
    mc "*Schlick, schlup...!*"
    rose "Kh...!"
    "Suddenly, I began to lap at Rosalind's inner folds, tracing an invisible pattern with my tongue."
    mc "*Schlick, schlup...!*"
    "She had clearly come here expecting to be fucked, if the aroma of freshly applied banana-scented soap was any indicator to go by."
    scene w1_0723 with dissolve
    rose "Mmmhhh..."
    "My efforts didn't produce much of a response from my co-conspirator at first, beyond some squirming and almost imperceptible vocalizations."
    mc "*Schlick, schlup...!*"
    mc "*Schlick, tchk, schlup...!*"
    rose "{size=-20}That's nice...{/size=-20!}{w} {size=-10}That's nice...{/size=-10}"
    "Slowly but surely though, as the minutes passed, that began to change."
    scene w1_0724 with dissolve
    rose "That feels good, baby."
    "Clear words of encouragement and a building, pulsating heat from her sex were the signs that my efforts weren't for nothing."
    rose "You're doing a good job, you're doing so so so {size=+10}SO{/size=+10} good!."
    "I had to admit, there was something charming and wholesome about Rosalind's idea of pillow talk."
    "For awhile, I simply let my tongue gently probe the slutty mother's cunny, lapping up the pooling juices and enjoying the sweet sounds that were escaping Rosalind's soft lips."
    mc "*Schlick, schlup...!*"
    mc "*Schlick, tchk, schlup...!*"
    "While I was happy to take it slow and wile away the minutes basking in Rosalind's pleasured sighs and cute twitches, it seemed she had other plans."
    rose "Aaah, oooh...!"
    scene w1_0727 with dissolve
    "The pace proving too slow and agonizing, the matronly woman took matters into her own hands." with vpunch
    rose "C-c'mon, come on, r-right there!"
    "She began guiding my head in an attempt to steer my tongue to the places she wanted it to go."
    mct "(Oh, she wants more? I'll give her more!)"
    scene w1_0728 with dissolve
    "Seeing as she wasn't content with just my mouth, I brought a hand up to plush woman's entrance and began to tenderly trace the petals of her engorged vulva before sinking them into the damp fuckhole."
    rose "nnnNney...?!"
    "The sudden intrusion caused Rosalind to yelp in surprise, as I worked my finger in conjunction with my tongue, searching for new ways to draw out whorish moans from her throat."
    scene w1_0729 with dissolve
    mc "*Schlick, schlup...!* *Schlick, tchk, schlup...!* *Schlick, schlup...!*"
    rose "Oh, [mcf]... oh, fuck... oh, [mcf]...!"
    mc "*Schlick, schlup...!* *Schlick, tchk, schlup...!* *Schlick, schlup...!* *Schlick, tchk, schlup...!* "
    "In between the nonesensical babbling, Rosalind started to call out my name."
    rose "Oh, [mcf], fuck, fuck, FUCK... oh, [mcf]...!"
    "Again and again, like a broken record."
    rose "That's--that's--that's...!"
    rose "{b}St-st-stoooop! Wait a minute!{/b}"
    scene w1_0730 with dissolve
    "Her abrupt refusal brought me to a commanding halt."
    scene w1_0732 with dissolve
    mc "...huh? What's the matter? Why'd you tell me to stop?"
    mc "You sounded like you were getting close."
    scene w1_0731 with dissolve
    rose "Y-yes! I was about to cum!"
    scene w1_0732 with dissolve
    mc "That's a problem for you...?"
    "She had me thoroughly confused with her reaction."
    scene w1_0733 with dissolve
    rose "Don't look at me like I'm a weirdo, it's just... it's j-just..."
    scene w1_0731 with dissolve
    rose "The tingling, the itchiness... it was weird."
    scene w1_0732 with dissolve
    "...hold up."
    mc "Are you saying you've never orgasmed before?"
    scene w1_0731 with dissolve
    rose "No, I've orgasmed... with toys... by myself, it was j-just... ngh! It's just... it never felt like this!"
    scene w1_0734 with dissolve
    rose "...w-what? Why are you grinning like an idiot?"
    scene w1_0735 with dissolve
    scene w1_0725 with dissolve
    mc "For one, you just checked off the ridiculous fantasy of pretty much every dude."
    scene w1_0726 with dissolve
    mct "(Then again, she could just be playing me here. Considering her previous attempt to seduce me, this could all be lip service for my ego.)"
    scene w1_0725 with dissolve
    mc "For another, well..."
    scene w1_0726 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Tell her you're grinning because she's adorable. [red]\[Toughness -1\]":
            $ toughness -= 1

            scene w1_0725 with dissolve
            show screen textbox2 with dissolve
            mc "I was also just thinking you're adorable. That's all."

        "Tell her you're grinning because you're not going to stop. [gr]\[Toughness +1]":
            $ toughness += 1

            scene w1_0725 with dissolve
            show screen textbox2 with dissolve
            mc "I was also just thinking I'm going to fuck a VERY good memory tonight. One you won't be able to forget."
            scene w1_0726 with dissolve
            mct "(Christ, since when did I get so damn cocky?)"

    scene w1_0739 with dissolve
    rose "You...!"

    if rosePolite == True:
        rose "You shouldn't tease an older woman, Mr. [mcl]. It's not nice."
    else:
        rose "You shouldn't tease an older woman, [mcf]. It's not nice."

    mc "I disagree!"
    scene w1_0736 with dissolve
    rose "--eh?!" with vpunch
    "Rosalind's cute reaction had invigorated me, sending me diving back into the previous task with a renewed mission: making this motherly, but surprisingly inexperienced woman cum her brains out until she's just a quivering puddle of sex."
    mc "*Schlick, schlup...!*"
    rose "Don't just so suddenly...!"
    mc "*Schlick, tchk, schlup...!*"
    scene w1_0737 with dissolve
    rose "Oooh-- eh, that does feel nice..."
    "The embarrassed expression Rosalind had fixed on her face during our conversational intermission instantly transformed into a dopey, glassed over look."
    "This new angle allowed my tongue new access to previously unexplored parts of Rosalind's slick love tunnel."
    mc "*Schlick, schlup...!* *Schlick, tchk, schlup...!* *Schlick, schlup...!*"
    "Feverishly, I scrapped and lashed at her insides, seeking just the right combination of movements in a bid to get Rosalind's vocal cords humming like a dollar-store slide whistle."
    rose "Aha-- *huff* *huff* Don't stop this time, alright?"
    rose "I'm ready for you..."
    rose "I {i}want{/i} you."
    "She beckoned me with a whisper-like, honeyed tone that practically caused my heart to skip a beat."
    mc "*Schlick, schlup...!* *Schlick, tchk, schlup...!* *Schlick, schlup...!* *Schlick, tchk, schlup...!*"
    "I doubled and tripled my efforts, so singularly focused on eating her out that breathing became an optional thing that I only sometimes remembered to do."
    "I stretched and strained my tongue so far out of my mouth that it was starting to hurt."
    scene w1_0738 with dissolve
    rose "Gghee, you're practically making out with my lower mouth...!"
    mc "*Schlick, schlup...!* *Schlick, tchk, schlup...!* *Schlick, schlup...!*"
    mc "*Schlick, schlup...!* *Schlick, tchk, schlup...!* *Schlick, schlup...!* *Schlick, tchk, schlup...!*"
    rose "There it is, there it is, there it is...♥!"
    "I could feel Rosalind begin to tense up in my arms, reeling back like a spring being primed."
    rose "Ehaaa~♥, I'm feeling it again, baby...♥ That itching sensation...!"
    rose "Ah...! Ah...!"
    scene w1_0743 with vpunch
    with flash
    with vpunch
    with flash
    with vpunch
    with flash
    rose "Gaeeeeeah--!"
    "Rosalind's climax was a funny thing, full of sound and bluster in the build up, but taking a sharp turn into a body-trembling silence at its peak."
    scene w1_0744 with fade
    "A dumb looking grin had spread on the lethargic woman's painted lips, repeatedly broken and reformed as she gulped down air at an erratic rate."
    rose "*huff* *huff* Ehee... That was nice..."
    stop music fadeout 3.0
    rose "You're... REALLY good at that, oh geez. You kids today pick up things quick."
    mc "That was all you, I couldn't help but go all out when your reactions were just too cute."
    scene w1_0745 with dissolve
    rose "Mmhh..."
    scene w1_0746 with dissolve
    play music "music/Moonlight-Sonata.mp3"
    rose "You know... this seems awfully lopsided so far. I get good head and the benefit of your support when..."
    rose "You haven't had your fill yet."
    rose "It's hard to call this a tit-for-tat arrangement if I get all the tat and you don't enjoy the tit."
    scene w1_0747 with dissolve
    mc "I've been working my way to that..."
    mc "Lie back straight on the couch and spread your legs."
    scene w1_0748 with dissolve
    rose "Hmmm, like this?"
    scene w1_0749 with dissolve
    rose "Is this to your satisfaction, {i}Mr. [mcl]{/i}?"
    scene w1_0750 with dissolve
    "She added a playful, teasing edge to the question."
    mc "No {i}Miss Carter{/i}, it's not. Spread them {b}wide{/b}."
    scene w1_0751 with dissolve
    rose "Is this more to your liking, {i}Sir{/i}?"
    scene w1_0752 with dissolve
    mc "I think this should speak for itself."
    "I climbed over Rosalind and positioned myself between the waiting woman's legs, presenting her with my cock."
    "I had been painfully hard for a long while, long before Rosalind had stripped nude. By now, I was {i}aching{/i} for release and the perfect outlet was right in front of me: her eager, drooling quim."
    scene w1_0754 with dissolve
    rose "...go, ahead."
    scene w1_0753 with dissolve
    mc "Here I..."
    hide screen textbox2 with dissolve
    play sound "sound effects/static.wav"
    scene w1_0740 with Pixellate(0.4, 5)
    $ renpy.pause(0.5, hard=True)
    play sound "sound effects/static.wav"
    scene w1_0741 with hpunch
    $ renpy.pause(0.5, hard=True)
    play sound "sound effects/static.wav"
    scene w1_0742 with vpunch
    $ renpy.pause(0.5, hard=True)
    scene w1_0753 with Pixellate(0.4, 5)
    show screen textbox2 with dissolve
    mc "..."
    scene w1_0755 with dissolve
    rose "Is something wrong?"
    scene w1_0756 with dissolve
    "Nearly unable to resist the temptation of plunging my cock inside Rosalind, my conscience nevertheless gave me a brief moment of pause."
    "Even if this is her idea..."
    if roseDealFullAcceptance == False:
        "Even if she refused my offer of no-strings-attached help in lieu of this arrangement..."
    "She's a woman desperately backed into a corner, just like my mother was."
    hide screen textbox2 with dissolve

    menu:
        "Ask Rosalind if she's truly okay with this. [gr]\[Rosalind +1\] [red]\[Toughness -2\]":
            $ toughness -= 2
            $ Rosalind_Affection += 1
            show screen textbox2 with dissolve
            mc "You're... sure about this?"
            scene w1_0757 with dissolve
            rose "Oh... sweetie."
            rose "Thank you, but... we've already come pretty far to be asking that now."
            scene w1_0758 with dissolve
            mc "There's still time to stop."
            scene w1_0759 with dissolve
            rose "Does it look like I want to stop? You've got me REALLY fired up right about now..."
            mc "..."
            "I gave her an unconvinced look."
            rose "*sigh* You're a nice kid... the fact that you're even asking proves that."
            rose "You're better than anyone else I've met at that club at least."
            scene w1_0758 with dissolve
            mc "Not like that's a stiff competition."
            scene w1_0759 with dissolve
            rose "Oh, hush! Stop overthinking things and stick that fat dick in me before I do it myself."
            scene w1_0758 with dissolve
            mc "How am I to argue with that?"
            scene w1_0760 with vpunch
            stop music fadeout 3.0
            "With a not-so-gentle shove, I forced Rosalind back down flat on the couch."


        "Don't let your conscience get in the way of a good time. [gr]\[Toughness +1\]":
            $ toughness += 1
            show screen textbox2 with dissolve
            mc "Absolutely not. Just taking a breath before I fuck you stupid."
            scene w1_0754 with dissolve
            stop music fadeout 3.0
            rose "Hurry up and stick that fat dick in me before I do it myself."

    scene w1_0761 with flash
    play music "music/guiton-sketch.mp3"
    "Firmly gripping her calves with my hands, I unceremoniously speared myself to the hilt inside Rosalind's dripping slit."
    rose "--ah! Yes, yes... finally"
    mc "Why don't you ask for it like a good girl?"
    rose "Please, give it--"
    scene w1RoseSofuk1 with dissolve
    "Without waiting for her to indulge me, I rolled my hips back and began to fuck the slutty mother without restraint."
    rose "Eh?"
    "The look on her face told me she wasn't expecting the sudden violent movement."
    "Combined that with how easy it was to slide in and out of her slavering hole, I knew one thing: she was feeling this, no matter the underlying circumstances that brought her here."
    "I could confidently put aside any lingering compunctions and fully enjoy myself."
    rose "Ah... so sudden, eeeh... you're being so... SO rough..."
    hide screen textbox2 with dissolve

    menu w1RoseMissonary:
        "Tease Rosalind with dirty talk. [gr]\[Rosalind +1\]":
            $ Rosalind_Libido += 1
            show screen textbox2 with dissolve
            mc "Better brace yourself, because I'm not slowing down."
            mc "Sluts don't get a say in how they get fucked."
            rose "Eeeh...? I'm not..."
            mc "You're not a slut? Could've fooled me, with the way your squeezing down on my cock right now."
            rose "That's...--eh, it just... just feels so nice."
            mc "Not to mention, you're fucking me for your own gain. That makes you more than just a slut, it also makes you a whore. A paid for whore."
            rose "I--but, ah-- it feel so SO nice..."
            mc "See you can't even argue against it, when your lower half is being honest. All you can do is drool over my cock and say {i}thank you{/i} for fucking me."
            rose "Ah... AH, yes... thank you for f-fucking me!"
            mc "I don't think I heard you clearly, say it again."

            if rosePolite == True:
                rose "Ggg-- I said, THANK YOU. Thank you for fucking me, Mr. [mcl]."
            else:
                rose "Ggg-- I said, THANK YOU. Thank you for fucking me."

            "Rosalind was definitely feeling this kind of treatment. She had slipped into the role obedient whore rather seamlessly. I'm sure part of it was her simply playing to my tastes, but she was definitely feeling this kind of dirty talk."
            "I could feel the effect in both the feverish way she moved her hips and the feeling of inner walls squeezing hungrily around my rod."

            mc "Good girl... that's right..."
            rose "Aaaeeeh, thank you, thank you, THANK YOU...!"
            rose "Thank you for fucking me!"
            mc "Gng-- good, good fucking whore."
            rose "Aaah... I'm a whore... I'm a whore...!"
            rose "{b}Fuck{/b} me like a whore, [mcf]. I need this...!"

        "Shower Rosalind with praise. [gr]\[Rosalind +2\]":
            $ Rosalind_Affection += 2
            show screen textbox2 with dissolve
            mc "That's because you're so beautiful. I can't help myself."
            rose "You really think so? I'm almost a middle-aged lady."
            mc "Do I think so? Can't you tell by how I'm fucking you?"
            mc "Everything about you is charming, Rose. Your voluminous ocean-blue eyes, your gentle countenance, your sweet song-like voice..."
            mc "You've got such a calming smile too, not to mention your figure."
            rose "What about my figure?"
            mc "You've got the most amazing, full-looking tits I've ever laid eyes on and an ass that would be at home on a donkey."
            rose "Pfft-shut up! You're supposed to be fucking me, not making jokes."
            mc "That's what I'm doing. You're so beautiful it makes me want to mess you up."
            rose "I like the sound of that, [mcf]."
            rose "Go ahead and mess me up. Stir me up with that young cock of yours."
            "Rosalind knew {i}exactly{/i} how to encourage me."
            mc "Ah! You beautiful, fat-assed bitch!"
            "My head was beginning to swell with the feeling of conquest."
            "One that was a product of taking a fine woman like Rosalind, prying her legs apart, and zealously fucking her like an animal."
            "It was a feeling serendipity, of having the dumb luck of a woman like Rosalind fall into my lap."
            rose "This feels so..."
            rose "I-- ah, this feels so SO nice...!"

        "{color=#FF1493}\[Recall Interview]{/color} Use your eyes, not your words [gr]\[Rosalind +4\]." if w1RoseGonzo == True and roseGonzoPositions == True:
            $ Rosalind_Affection += 3
            $ Rosalind_Libido += 1
            show screen textbox2 with dissolve
            "I recalled what Rosalind admitted to me during her introduction video."
            scene w1_1764 with pixellate
            rose "Ehehe... I like the idea of being folded in half, looking my partner in his eyes as he rails me slowly."
            scene w1RoseSofuk1 with dissolve
            mc "Nevermind about that. Look me in the eyes when I fuck you, Rose."
            "I mustered my best authoritarian tone, careful not to let my voice crack from the incredible pleasure Rose's lower mouth was giving me with its kiss.."
            rose "Eeeh, ..w-what?"
            "Instead of answering her, I did my best to let my eyes lead by example, looking down at Rosalind's face and trying to stare a hole right through her."
            "To my surprise, she didn't burst out laughing at my experimental, dorkish attempt at seduction. Instead she..."
            rose "Ah... you're looking at me so..."
            rose "This feels so..."
            rose "I-- ah, this feels so SO nice...!"
            "Throughout her carnal affirmations, I didn't say a word. Instead, I just left my unblinking eyes locked onto hers, my face tightly composed as my hips continuously battered her into hers."
            scene w1_0765 with dissolve
            "Her crystal blue eyes were clouded over with razor-sharp desire, returning my own gaze with equal intensity, trading verbal communication for a wordless rutting punctuated by the occasional involuntary moan."
            "In a way, it was a bizarre, dirty staring contest."
            mct "({b}Fuck{/b}, she's so damn beautiful.)"
            "The kind of beautiful that makes you want to, in equal measure, both exalt in admiration and fuck into the dirt."
            scene w1RoseSofuk1 with dissolve
            rose "Aah... no fair! You just went somewhere else for a second."
            mc "Sorry, I just got lost in thought."
            rose "Don't. {b}Focus one me{/b}, baby."
            rose "It's just you and me in the world right now. Nothing else...♥"
            mct "(Right. It's just Rosalind and I, fucking like animals. Our hips moving in unison, thrusting with full abandon.)"

        "{color=#696969}\[Recall her interview] Use your eyes, not your words.{/color}" if w1RoseGonzo == True and roseGonzoPositions == False:
            jump w1RoseMissonary

        "{color=#696969}\[Recall her interview] Use your eyes, not your words.{/color}" if w1RoseGonzo == False and roseGonzoPositions == False:
            jump w1RoseMissonary


    "Each thrust was like a tug of war. My cock found no resistance in the act of sheathing itself to the base, but each retraction was a renewed struggle to free myself from the slutty mother's cum-hungry tunnel."
    mct "(I don't know if it's our chemistry of if Rosalind is simply in need a good dicking, but her cunt is so damn receptive to pleasure.)"
    "Fucking a woman like Rosalind is bigger, more twisted rush than I could've ever hoped for."
    "Her loving personality, her present circumstances... it all mingled together to paint an irresistible dichotomy. On one side, the chaste image of a self-sacrificing mother."
    "On the other side a woman with abundant sexual desire, currently slavishly howling and moving her lips like a senseless animal. Two seemingly contradictory pictures, but {i}shit{/i} when combined they form one hell of a depraved composite image."
    scene w1_0766 with dissolve
    rose "Oh.. eeh....what... AAAAAH, fugheee--♥!" with flash
    "Soon that struggle became even more intense. A sudden intense tightness coupled wit a whorish outpouring of garbled nonsense told me Rosalind's body had been racked by a second, sudden orgasm."
    scene w1_0767 with dissolve
    rose "Eeeeeeeh....! I fheel sho, ng--!" with flash
    "...and then another, Rosalind's body once again tensing up and uncoiling itself in pleasure." with flash
    scene w1_0766 with dissolve
    rose "Ghheee--"
    "Again and again, and with a diminishing return, I fought through Rosalind's back-to-back mini-orgasms, jackhammering my hips with a galvanized intensity." with flash
    "I was getting close. I could feel it in my balls."
    scene w1RoseSofuk2 with dissolve
    "Any sense of higher self was now replaced by a singular fuck-driven urge."
    rose "Gggh-a, I'm fheeling so weird-right now..."
    rose "Your dick, I can feel it... eeeh..."
    rose "Y-you're close, right? Come on, baby. Give it to me."
    rose "Eeeh, It's safe to-- to cum inside."
    rose "--A----"
    rose "---s-f-S-fg---d---"
    "By this point her words were barely reaching me at all, my mind had been voided of anything but my impeding release. I..."
    hide screen textbox2 with dissolve

    menu:
        "Cum Inside [gr]\[Rosalind +1\]":
            $ Rosalind_Libido += 1
            show screen textbox2 with dissolve
            "By this point, I was on auto-pilot. Operating solely on instinct."
            "And my instincts told me to shove my cock as deep as I possibly could and blow my load straight into her womb."
            scene w1_0772 with hpunch
            "So that's what I did, folding the slutty mother in half like a toy and extending my hips until it hurt."
            mc "Ggg--! Take it, you bitch!"
            play sound "sound effects/spurt.wav"
            mc "--!" with flash
            play sound "sound effects/spurt.wav"
            rose "Ghheee--! There's so much, I'm... eeeh, I'm..." with flash
            play sound "sound effects/spurt.wav"
            rose "--ggggggggggggeeeeeh...!" with flash
            "Rosalind was shook by one last orgasm, squeezing down on my dick hard, causing it to be rooted to the base."
            "Her lower mouth was going to make sure it drunk down all my baby batter."
            scene w1_0773 with fade
            stop music fadeout 3.0
            mc "Ggghaaa--!"
            mc "*Huff, huff* *Huff, huff*"
            rose "There's so much....egn."
            jump w1RoseSexCleanCuddleTime

        "Pull out and ejaculate on Rosalind's stomach and tits.":
            show screen textbox2 with dissolve
            "By this point, I was on auto-pilot. Operating solely on instinct."
            "And my instinct told me I wanted to let Rosalind personally see ALL the spunk she had worked so hard to get out of me."
            scene w1_0774 with dissolve
            mc "Ggg--! Take it, you bitch!"
            play sound "sound effects/spurt.wav"
            mc "--!" with flash
            play sound "sound effects/spurt.wav"
            rose "Eeeh, there's so much..." with flash
            play sound "sound effects/spurt.wav"
            mc "ng--!" with flash
            "Gripping my dick, I lackadaisically pointed it in the general direction of the slutty mother's torso."
            "Spurt after spurt spattered Rosalind's pale stomach. Not just there either, the intensity and the amount was surprising."
            "Some even made its way to Rosalind's large, heaving breasts."
            scene w1_0775 with fade
            stop music fadeout 3.0
            mc "*Huff, huff* *Huff, huff*"
            rose "Geez... that's so... that's a lot..."
            rose "You've made an awful mess of me. I'm going to smell like you all night..."
            jump w1RoseSexDirtyCuddleTime




label w1RoseSexCleanCuddleTime:
    scene w1_0784 with dissolve
    play music "music/a-lost-map-of-a-heaven.mp3"
    rose "Hey, [mcf]..."
    rose "If it's not too much trouble..."
    rose "Would you mind holding me for a minute while I wait for the feeling to return to my legs?"
    "Rosalind hit me with an adorable request."
    scene w1_0785 with dissolve
    mc "You're a post-coital cuddle kind of gal?"
    scene w1_0784 with dissolve
    rose "I take what I can get."
    scene w1_0786 with dissolve
    mc "I like a little physical intimacy myself."
    scene w1_0787 with dissolve
    "An oddly comfortable silence came over us for a few moments, before Rosalind drew attention to the mess I made of her nether regions."
    scene w1_0788 with dissolve
    rose "Eeeh-hehe, I feel so full."
    mc "Take it as a compliment."
    scene w1_0789 with dissolve
    mct "(Mmmnn... Rose is so soft and warm. I... I...)"
    scene w1_0790 with dissolve
    mc "*Yawn* Muhahhaaaa."
    scene w1_0789 with dissolve
    mct "(I'll just shut my eyes a little bit...)"
    scene w1_0791 with dissolve
    "I let myself drift off to sleep, enjoying the feeling of having another person beside me as I did."
    "For me, it was a rare occurrence. One I was happy to indulge in."
    stop music fadeout 3.0
    "........."
    scene black with fade
    "......"
    $ renpy.end_replay()
    jump w1RoseEnd




label w1RoseSexDirtyCuddleTime:
    scene w1_0776 with dissolve
    play music "music/a-lost-map-of-a-heaven.mp3"
    rose "Hey, [mcf]..."
    rose "If it's not too much trouble..."
    rose "Would you mind holding me for a minute while I wait for the feeling to return to my legs?"
    "Rosalind hit me with an adorable request."
    scene w1_0777 with dissolve
    mc "You're a post-coital cuddle kind of gal?"
    scene w1_0776 with dissolve
    rose "Mmmhm, I take what I can get."
    scene w1_0779 with dissolve
    mc "I like a little physical intimacy myself."
    scene w1_0778 with dissolve
    "An oddly comfortable silence came over us for a few moments, before Rosalind drew attention to the mess I made of her chest.."
    scene w1_0780 with dissolve
    rose "Eeeh-hehe, there's so much of it and it's so thick."
    mc "You should take it as a compliment."
    scene w1_0781 with dissolve
    mct "(Mmmnn... Rose is so soft and warm. I... I...)"
    scene w1_0782 with dissolve
    mc "*Yawn* Muhahhaaaa."
    scene w1_0781 with dissolve
    mct "(I'll just shut my eyes a little bit...)"
    scene w1_0783 with dissolve
    "I let myself drift off to sleep, enjoying the feeling of having another person beside me as I did."
    "For me, it was a rare occurrence. One I was happy to indulge in."
    stop music fadeout 3.0
    "......"
    scene black with fade
    "..."
    $ renpy.end_replay()
    jump w1RoseEnd


label w1RoseEnd:
    rose "Good night, [mcf]."
    play sound "sound effects/door-openclose.wav"
    "..."
    scene w1_0792 with dissolve
    $ history_rosalind = "I allowed myself to knowingly fall prey to Rosalind's seduction, agreeing to help her gain an advantage in the exhibition if the opportunity arises."
    $ unread_rosalind = True
    play sound "sound effects/notification.wav"
    show bioupdate with dissolve
    "......"
    mc "Mmmgh..."
    scene w1_0793 with dissolve
    play music "music/ill-remember-you.mp3"
    "A couple of hours later, I opened my eyes and found myself alone."
    "Rosalind had put a blanket over me and left a glass of water on the table while I slept."
    scene w1_0794 with dissolve
    mct "(Ghh...)"
    "I slept way longer than I intended, shattering all hope of getting to bed at a decent time tonight."
    "It was most definitely worth it though. Rosalind is an interesting woman, if not difficult to read."
    "I wonder how much of what she showed me tonight was manufactured and how much of it was her honest reaction."
    mct "(The way she was carrying on at the end seemed real, but then again, what the hell do I know? Smarter men than I have fallen prey to the affectations of beautiful women.)"
    mct "(I can't believe I agreed to help her win the summer exhibition.)"
    mct "(Well, I did say I would only help her if the opportunity presented itself, but...)"
    mct "(I should probably make a genuine effort in looking for one, huh? Still, doing so might jeopardize my newly minted place at the club...)"
    "Why {i}did{/i} I agree to help her?"
    hide screen textbox2 with dissolve

    menu:
        "It was the promise of sex, obviously.":
            $ roseHelpSex = True
            show screen textbox2 with dissolve
            mct "(Well, what other reason could there be?)"
            "She had me really worked up there, and my side of the deal was so vague and noncommittal..."

        "It's because she needs the help.":
            $ roseHelpNeed = True
            show screen textbox2 with dissolve
            mct "(It's because it really sounded like she needed the help.)"
            "She's fighting not only for her own livelihood, but for her daughters as well."
            "Veronica on the other hand is only trying to keep her failing business afloat. Felicia, well..."
            mct "(I think she might just be crazy.)"

        "It's because she reminds you of a certain woman.":
            $ roseHelpMom = True
            show screen textbox2 with dissolve
            mct "(There's no way around it, is there?)"
            "She reminded me of my own mother, after my father's death."
            "Obviously the circumstances are different, but she's fighting not only for her own livelihood, but her daughters as well."
            "It's a situation I can deeply empathize with. Unbeknownst to her, I was actually the perfect mark for her conspiracy."
            mct "(I'm more sentimental than I thought.)"

    scene w1_0795 with dissolve
    mct"(I should brush my teeth and try to get some more shut-eye. Don't want fall into poor sleeping habits.)"
    scene black with fade
    stop music fadeout 3.0
    if not persistent.roseW1SexGallery:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.roseW1SexGallery = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)
    jump w1June02End

label w1RoseFlagDeny:
    show screen textbox2 with dissolve
    scene w1_0796 with dissolve
    mc "Sorry, I don't think I can or should help."
    scene w1_0797 with dissolve
    rose "But...!"
    scene w1_0796 with dissolve
    mc "It wouldn't be fair to Veronica or Felicia, not to mention I might be putting my own place at the club at risk."
    scene w1_0684 with dissolve
    rose "..."
    scene w1_0798 with dissolve
    rose "I... understand. Would you please keep this between us at least?"
    scene w1_0684 with dissolve
    mc "Of course. This stays right here. It never happened."
    mc "I just wish there was more I could do for you."
    scene w1_0680 with dissolve
    rose "That's okay... I'll win this thing regardless, no matter what. I have to do. If I don't, who knows what..."
    scene w1_0684 with dissolve
    "She trailed off, with what was left unsaid having a sobering implication."
    scene w1_0798 with dissolve
    rose "I'm... I feel very ridiculous right now. I think it's best if I leave.."
    scene w1_0799 with fade
    rose "S-sorry for all of this."
    scene w1_0800 with dissolve
    mc "...that's okay. Take care of yourself, Rose."
    scene w1_0801 with dissolve
    "I wish I could've offered her some comforting words, but the cruel reality is nothing I could say could save her from the soul crushing predicament she's currently in."
    "It would all be inadequate. In this world, we all are ultimately alone and we have to save ourselves. Is that not what my own mother learned the hard way after my father died?"
    "So instead, I left her with nothing but cold parting words."
    scene w1_0802 with dissolve
    rose "I'll see you this weekend."
    scene black with fade
    stop music fadeout 3.0
    $ history_rosalind = "Rosalind tried to seduce me into helping her win the exhibition, but I turned her down out of fairness to the other Carnations and my sense of self-preservation. I don't think I'll be seeing her outside of the club from now on."
    $ unread_rosalind = True
    play sound "sound effects/notification.wav"
    show bioupdate with dissolve
    "......"
    "..."
    $ renpy.end_replay()
    scene black with fade
    jump w1June02End


label w1June02End:
    $ date = "june02night"
    scene w1_0804 with cmet
    "Later, as I laid in bed waiting for the curtain to be drawn on my day, my head was oddly devoid of thoughts."
    "Gradually, I felt the weight of sleep begin to wash over me."
    scene w1_0817 with dissolve
    "........."
    "......"
    scene w1_0803 with dissolve
    play sound "sound effects/sms-chime.wav"
    "*Chirp, chirp.* --!"
    play music "music/thief-in-the-night.mp3"
    mct "(Fuck.)"
    mct "(That's probably Ian, considering the time.)"
    scene w1_0805 with fade
    mct "(Yep. That's two for two, the past couple of nights.)"
    hide screen textbox2 with dissolve
    scene player-bedroom-dark blur with dissolve
    if w1MinaLie == True:
        $ Mina_Affection -= 3
        $ Killian_Bromance += 1

        call phone_start_kil from _call_phone_start_kil_4
        call message_start("Killian", "Hey, Doc!") from _call_message_start_15
        call message ("Killian", "Thanks for getting Mina pissed at both of us!") from _call_message_41

        call screen phone_reply("I'm sorry, what?","w1June02EndPissed1","Uh, what the hell did I do?.","w1June02EndPissed2")

    else:
        $ Killian_Bromance += 1

        call phone_start_kil from _call_phone_start_kil_5
        call message_start("Killian", "Hey, Doc!") from _call_message_start_16
        call message ("Killian", "Thanks for getting Mina pissed at me!") from _call_message_42

        call screen phone_reply("What did I do?","w1June02EndPissed3","You made your own bed.","w1June02EndPissed4")



label w1June02EndPissed1:
    call phone_after_menu from _call_phone_after_menu_10
    call message_start("[mcf]", "I'm sorry, what?") from _call_message_start_17
    call message("Killian", "The cover story, you idiot! You told her I was with my uncle today.") from _call_message_43
    call reply_message ("Oh, I thought that was a pretty reasonable one...") from _call_reply_message_11
    call message("Killian", "It would be... if you gave me a heads up so we could co-ordinate our stories!") from _call_message_44
    call reply_message ("...ah. She knows I lied?") from _call_reply_message_12
    call message("Killian", "Yep. On the bright side, that's taken some of the heat off me. Silver lining.") from _call_message_45
    call message("Killian", "Thanks for being a bro though, I'm glad to know you have my back. Just, take it from a professional, if you're going to lie, never be too specific! It'll blow up in your face.") from _call_message_46
    call reply_message ("Thanks, Professor Asshole.") from _call_reply_message_13
    call message("Killian", "Anytime. Night, bro!") from _call_message_47
    call phone_end_kil from _call_phone_end_kil_5
    jump w1June02EndForReal


label w1June02EndPissed2:
    call phone_after_menu from _call_phone_after_menu_11
    call message_start("[mcf]", "Uh, what the hell did I do?") from _call_message_start_18
    call message("Killian", "The cover story, you idiot! You told her I was with my uncle today.") from _call_message_48
    call reply_message ("Oh, I thought that was a pretty reasonable one...") from _call_reply_message_14
    call message("Killian", "It would be... if you gave me a heads up so we could co-ordinate our stories!") from _call_message_49
    call reply_message ("...ah. She knows I lied?") from _call_reply_message_15
    call message("Killian", "Yep. On the bright side, that's taken some of the heat off me. Silver lining.") from _call_message_50
    call message("Killian", "Thanks for being a bro though, I'm glad to know you have my back. Just, take it from a professional, if you're going to lie, never be too specific! It'll blow up in your face.") from _call_message_51
    call reply_message ("Thanks, Professor Asshole.") from _call_reply_message_16
    call message("Killian", "Anytime. Night, bro!") from _call_message_52
    call phone_end_kil from _call_phone_end_kil_6
    jump w1June02EndForReal


label w1June02EndPissed3:

    call phone_after_menu from _call_phone_after_menu_12
    call message_start("[mcf]", "What did I do?") from _call_message_start_19
    call message("Killian", "You told her I got so wasted I had to sleep it off at your place.") from _call_message_53
    call reply_message ("That's only the truth. I did conveniently leave out the part where you were eating out a strange woman in my bathroom.") from _call_reply_message_17
    call message("Killian", "You know what? Fair enough. It was me that fucked up here.") from _call_message_54
    call reply_message ("That's a surprisingly self-cognizant response for you.") from _call_reply_message_18
    call message("Killian", "Still, for future reference, I would've prefer a simple 'I don't know' if she ever asks you where I am.") from _call_message_55
    if minaFlag == True:
        call message("Killian", "Uh, thanks for performing my boyfriend duties by the way. I really mean it.") from _call_message_56
        call message("Killian", "This might seem insincere since I'm the one who forgot about our date, but I'm glad she didn't spend the day alone.") from _call_message_57
        call reply_message ("Yeah, no problem. Just get a date-book or something, yeah?") from _call_reply_message_19
        call message("Killian", "Hehe, maybe I should. Anyway, night bro!") from _call_message_58
    else:
        call message("Killian", "Night!") from _call_message_59
    call phone_end_kil from _call_phone_end_kil_7
    jump w1June02EndForReal


label w1June02EndPissed4:

    call phone_after_menu from _call_phone_after_menu_13
    call message_start("[mcf]", "You made your own bed.") from _call_message_start_20
    call reply_message ("I did conveniently leave out the part where you were eating out a strange woman in my bathroom.") from _call_reply_message_20
    call message("Killian", "You know what? Fair enough. It was me that fucked up here.") from _call_message_60
    call reply_message ("That's a surprisingly self-cognizant response for you.") from _call_reply_message_21
    call message("Killian", "Still, for future reference, I would've prefer a simple 'I don't know' if she ever asks you where I am.") from _call_message_61
    if minaFlag == True:
        call message("Killian", "Uh, thanks for performing my boyfriend duties by the way. I really mean it.") from _call_message_62
        call message("Killian", "This might seem insincere since I'm the one who forgot about our date, but I'm glad she didn't spend the day alone.") from _call_message_63
        call reply_message ("Yeah, no problem. Just get a date-book or something, yeah?") from _call_reply_message_22
        call message("Killian", "Hehe, maybe I should. Anyway, night bro!") from _call_message_64
    else:
        call message("Killian", "Night!") from _call_message_65
    call phone_end_kil from _call_phone_end_kil_8
    jump w1June02EndForReal



label w1June02EndForReal:
    ## Transition back to the image of Edwin holding the phone up to his face
    scene w1_0805 with dissolve
    mc "..."
    ## Edwin puts the phone back down
    scene w1_0806 with dissolve
    mct "(He's such a moron.)"
    if Killian_Bromance >= 20:
        mct "(...but he's my moron.)"
    scene black with fade
    "It took me another hour to get back to sleep."
    "This time I remembered to put my phone on silence."
    stop music fadeout 3.0
    "........."
    "....."
    "..."
    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionfelicia04 with blinds
    $ renpy.pause(6, hard=True)
    jump june03start


label june03start:
    scene black with blinds
    play sound "sound effects/door-bell.wav"
    show screen textbox2 with dissolve
    show screen qmenu with dissolve
    $ date = "june03day"
    "*Ding dong!*"
    scene w1_0807 with sunshine
    mc"Unmmgh... eh?"
    mct "(Who could that be...? Maybe if I ignore it they'll just go away...)"
    play sound "sound effects/door-bell.wav"
    show june03day with squares
    "*Ding dong!*"
    mct "(There it is again...)"
    "The irritating, sleep-rending noise known as a doorbell DID NOT stop like I had hoped."
    play sound "sound effects/door-bell.wav"
    "*Ding dong!*"
    mct "(Nggg... fuck!)"
    scene w1_0808 with fade
    mc "I'm coming!"
    scene black with fade
    mc "It's a bit early, don't you--"
    play sound "sound effects/door-openclose.wav"
    "The person at the door was most definitely not who I expected."
    scene w1_0809 with fade
    play music "music/thief-in-the-night.mp3"
    chuck "Hiya, lad. Going by your lack of clothes, I'm guessin' I caught you in the middle of catching some z's."
    chuck "Late night?"
    chuck "Oh, to be young again."
    scene w1_0810 with dissolve
    chuck "I brought you some coffee."

    scene w1_0811 with fade
    if chuck_polite == True:
        mc "What do I owe this visit to, sir?"
    if chuck_uncle == True:
        mc "What do I owe this visit to, Uncle Chuck?"
    else:
        mc "What do I owe this visit to, Dr. Chuck?"

    scene w1_0812 with dissolve
    chuck "I wanted to check in on you, see how you're adjusting to things."
    chuck "For one, how's the new bachelor pad treating you? I see you still haven't found the hidden cameras."
    scene w1_0811 with dissolve
    mc "Uh... w-what? Hidden cameras?"
    scene w1_0813 with dissolve
    chuck "Bahahahaha! Oh, you should see the look on your face, lad. I'm kidding, I'm kidding! There's no cameras... that I know of, at least."
    scene w1_0812 with dissolve
    chuck "Wouldn't put it past Kathy to have Warren install a few though. She's a bit of a {i}voyeur{/i}, if you couldn't tell from the way she conducted the show a couple of weeks ago."
    scene w1_0811 with dissolve
    mc "Heh, good one..."
    mct "(Note to self: do an internet search on how to look for hidden cameras.)"
    scene w1_0812 with dissolve
    chuck "Anyway, the apartment. It's to your liking?"
    scene w1_0814 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Tell him it's too big.":
            show screen textbox2 with dissolve
            mc "To be honest, it's a little too big for just me."
            mc "Not to say I don't appreciate moving out of my old place. It was way too small."
            scene w1_0815 with dissolve
            chuck "I think you'll find it'll be nice to have the space when you need it. After all, you may have to occasionally entertain some of our clientele."

        "Tell him you're loving it here.":
            show screen textbox2 with dissolve
            mc "To be honest, I'm loving it. It's huge."
            mc "It's nice to be able to stretch your legs without needing to go out."
            scene w1_0815 with dissolve
            chuck "I'm glad you feel that way. Plus, you may find the extra space useful if you're called on to entertain some of our clientele in the future."

    scene w1_0814 with dissolve
    mc "That's part of my job description?"
    scene w1_0816 with dissolve
    chuck "Oh, of course. This isn't the kind of job you put down when you leave the workplace. It will occasionally bleed over into your personal time."
    chuck "That's not a problem, is it?"
    scene w1_0814 with dissolve
    mc "No... that's fair, considering what you're paying me."
    scene w1_0815 with dissolve
    chuck "Good! Cause, like it or not, you're part of the family now."
    chuck "You're stuck with us."
    scene w1_0818 with dissolve
    chuck "You haven't found anything weird have you?"
    scene w1_0819 with dissolve
    chuck "The lad who had your job before you, Darius, used to live here as well - before he suddenly disappeared on us, that is."
    chuck "We tried to clean the place up, but you may find some of his personal effects laying around. If you do, just throw them away."
    scene w1_0820 with dissolve
    mc "What if he comes back looking for them?"
    scene w1_0821 with dissolve
    chuck "Oh, he {b}won't{/b}."
    scene w1_0822 with dissolve
    chuck "I mean seriously, what lad your age walks away from an all you can eat pussy buffet? I'll never understand rich kids like Darius... or my nephew even."
    scene w1_0823 with dissolve
    chuck "I suspect you feel the same way, after all you and I are cut from a similar cloth."
    scene w1_0825 with dissolve
    mc "A similar cloth? Your entire family's loaded."
    scene w1_0826 with dissolve
    chuck "Not true. My sister and I come from meager beginnings, actually. She married into money and as you know I came into my fortune the honest way."
    chuck "All those snobby assholes you met growing up were on my brother-in-law's side."
    scene w1_0824 with dissolve
    mc "I see, I guess I always figured Ian's whole family was rich."
    scene w1_0822 with dissolve
    chuck "Anyway, as I was saying... lads like Darius, who've never done without, they take things for granted. They don't have the proper appreciation for the good fortune that falls into their laps."
    scene w1_0823 with dissolve
    chuck "That's another reason I'm glad to have you. God knows August needs at least one person beside himself with a good head on his shoulders."
    scene w1_0825 with dissolve
    mc "That sounds like a pretty low bar, but I'll take that as a compliment I guess."
    scene w1_0822 with dissolve
    chuck "Bahahaha! Take it as you will, lad. It's only the truth."
    scene w1_0827 with dissolve
    chuck "Getting into the main reason I popped in this morning..."
    scene w1_0828 with dissolve
    "Dr. Chuck placed a hand on my shoulder and gave me an uncharacteristically serious look."
    scene w1_0827 with dissolve
    chuck "I just want to communicate to you..."
    chuck "If you ever have anything bothering you or giving you trouble, club related or elsewise, my door is always open."
    scene w1_0828 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Thank Dr. Chuck for his kindness. [gr]\[Chuck +1\]":
            $ Chuck_Friendship +=1
            show screen textbox2 with dissolve
            scene w1_0829 with dissolve
            mc "Just like your old policy for the physics club, huh? Well, minus the rich, underground sex parties..."
            scene w1_0830 with dissolve
            chuck "Exactly, lad. If you ever need anything, I'm here to help."
            scene w1_0831 with dissolve

            if chuck_polite == True:
                mc "Thanks, Sir."
            if chuck_uncle == True:
                mc "Thanks, Uncle Chuck."
            else:
                mc "Thanks, Dr. Chuck."

            mc "I may take advantage of that one day."


        "Unenthusiastically tell him you'll keep that in mind.":
            show screen textbox2 with dissolve
            mc "Yeah, sure. I'll keep that in mind."
            scene w1_0827 with dissolve
            chuck "Please do, lad."
            chuck "We're all in this together, after all."
            scene w1_0828 with dissolve
            mct "(How magnanimous.)"

    scene w1_0832 with dissolve
    chuck "That's all I wanted to say. I'll stop taking up time from your precious summer break."
    chuck "I need to get to the club anyway, there's a little fire I need to put out."
    scene w1_0833 with dissolve
    mc "Anything I can help with? I'm not really engaged in anything right now, so ..."
    scene w1_0832 with dissolve
    chuck "Oh, no lad. Thanks for offering, but there's nothing you can do."
    chuck "One of the girls got a little spooked making a house call last night. I'm going to talk her down from the ledge, so to speak."
    scene w1_0833 with dissolve
    mc "Oh..."
    "I decide not to ask any more details about the situation, not wanting to be privy to any information that might destroy my currently rocky acceptance of the club."
    mc "Thanks again for the coffee then."
    scene w1_0834 with dissolve
    chuck "No problem, lad. You take care now."
    chuck "...and remember, my door is always open!"
    scene black with fade
    play sound "sound effects/door-openclose.wav"
    "Dr. Chuck let himself out."
    scene w1_0835 with fade
    mct "(Is this going to be the norm from now on? People showing up unannounced?)"
    mct "(Now, what should I do today...?)"

    if feliciaFlag == True:
        mct "(Oh, yeah! Felicia wanted to take me out to dinner and I agreed.)"
        mct "(She didn't tell me a time or place though, I should give her a call and get the details.)"
        scene black with fade
        stop music fadeout 3.0
        "......"
        "..."
        jump w1FeliciaDateStart

    if feliciaFlag == False and feliciaDinnerDecline == False:
        jump w1FeliciaFlag


    if feliciaFlag == False and feliciaDinnerDecline == True:
        mct "(I turned down having dinner with Felicia tonight. So unless something comes up, I guess it's a lazy Wednesday for me.)"
        jump w1FeliciaFlagDeny




label w1FeliciaFlag:
    play sound "sound effects/ringing-inbound.wav"
    "*Ring, ring.*"
    mct "Hmm? Who's this?"
    scene player-livingroom with dissolve
    show unknown-call with dissolve
    mc "Hello?"
    fel "[mcf]? That you? Good. I got your number from Ian."

    if perk_socialButterfly == True:
        mc "Felicia, what do I owe the pleasure?"
        fel "The pleasure is my company over dinner."
    else:
        mc "Hey, Felicia. What's up?"
        fel "Hopefully you accepting a dinner invitation."

    mc "You want to get dinner?"
    fel "I do. Think of it as an apology for surprising you the other day. The whole me being a Carnation business."
    mc "That was... two weeks ago. I'm well past the shock."
    fel "Still, it's a pretty good pretense for getting dinner with a beautiful woman, right? It'll be my treat."
    mct "(Hmmm... Felicia's a wild card. Having dinner with her might be fun.)"
    "Then again, maybe it'd be best if I decline and {b}limit my interaction with her to solely the club{/b}. Getting involved with a Carnation could be problematic down the road."
    if roseFlag == True:
        "Not that I have a leg to stand on there, considering my involvement with Rose already..."

    hide screen textbox2 with dissolve

    menu:
        "Accept Felicia's dinner invitation. [gr]\[Felicia +1\]":
            $ Felicia_Affection += 1
            $ feliciaFlag = True
            show screen textbox2 with dissolve
            $ history_felicia = "Felicia called me out of the blue and asked me out to dinner. I accepted."
            $ unread_felicia = True
            play sound "sound effects/notification.wav"
            show bioupdate with dissolve
            mc "Yeah, sure."
            "Despite her involvement with the club, I'd be lying if I said I didn't enjoy spending time with her."
            if toughness >= 18:
                "Plus, who would turn down the chance to score with a beautiful woman?"
            fel "Great! I knew you'd say yes, so I've already made reservations. I'll text you the location and time."
            fel "Don't be late!"
            mc "Alright, thanks for asking me out."
            fel "See you tonight, bye."
            play sound "sound effects/call-end.wav"
            ## Transition to Edwin holding the phone
            "Well, I guess I got something to do today."
            mct "(A date with Felicia. Knowing her, this should be interesting.)"
            scene black with fade
            "......"
            "..."
            jump w1FeliciaDateStart





        "Decline Felicia's dinner invitation. [red]\[Felicia -3\]":
            $ Felicia_Affection -= 3
            show screen textbox2 with dissolve
            $ history_felicia = "Felicia called me out of the blue and asked me out to dinner. I declined, deciding to limit my interaction with the Carnation strictly to club business."
            $ unread_felicia = True
            play sound "sound effects/notification.wav"
            show bioupdate with dissolve
            mc "Ah, tonight's no good for me. Sorry."
            fel "What about Friday?"
            mc "Sorry, no can do."
            fel "...I get it, I get it. I won't take it TOO personally."
            fel "Strictly business, eh?"
            fel "Well, can't blame a girl for being friendly."
            mc "Sorry, I think that's for the best."
            fel "I guess I'll see you around the club then, stud."
            mc "Take care of yourself, Felicia."
            fel "You too, [mcf]. Bye bye."
            play sound "sound effects/call-end.wav"
            "Well, just turned down dinner with a beautiful woman, but it's for the best, right?"
            scene black with fade
            "......"
            "..."
            jump w1FeliciaFlagDeny



label w1FeliciaDateStart:

    $ date = "june03night"

    "Later that night, I arrived at the restaurant. It wasn't too far from my new apartment, so Felicia and I made plans to meet inside."
    "The second I laid eyes on the building, panic set in. The kind of panic that follows once one becomes acutely aware of being out of place in an unfamiliar location."
    scene w1_0858 with blinds
    play music "music/sneaky-snitch.mp3"
    mct "(I am so, so, SO underdressed for this place.)"
    scene w1_0836 with dissolve
    host "Can I help you, sir...?"
    scene w1_0837 with dissolve
    mc "Yeah, um... I'm meeting someone here tonight. We have a reservation."
    scene w1_0838 with dissolve
    "The maître d gave me a not-so-subtle look over, before returning her eyes to her computer."
    host "Name of the reservation, please."
    mc "Mmmmh... Ford, I guess."
    scene w1_0839 with dissolve
    host "You're telling me {i}you're{/i} a guest of {b}Mrs. Ford{/b}?"

    if feliciaSex == True and prAfterParty == False:
        "She said it with such deference and a particular, incredulous-like emphasis that I began to doubt we were speaking of the same woman I had railed in a dirty club bathroom."
    else:
        "She said it with such deference and a particular, incredulous-like emphasis that I began to doubt we were speaking of the same woman."

    mc "Yeah... {i}Felicia{/i} Ford?"
    stop music fadeout 3.0
    scene w1_0840 with dissolve
    host "..."
    scene w1_0841 with dissolve
    host "Sir, if it's not too much trouble, would you mind waiting in the garden until Mrs. Ford gets here? It's our policy not to seat guests until the full party arrives."
    mct "(Huh...? That sounds like an odd policy...)"
    mct "(Oh, I get it. She doesn't want me stinking up the place.)"
    scene w1_0842 with dissolve
    fel "*A-hem!*"
    "The sound of a woman clearing her throat brought my attention to a figure that had evidently snuck up behind the maître d while we were conversing."
    play music "music/romantic-motivation.mp3"
    scene w1_0843:
        subpixel True
        yalign 1.0
        xalign 0.6
        linear 4 yalign 0.1
    "It was Felicia, looking stunning in a daring, black little number."
    scene w1_0844 with dissolve
    fel "Really? I had no idea Nicholas had updated restaurant policy since the last time I had guests."
    scene w1_0845 with dissolve
    fel "When was that again? Just a week ago, I think."
    mc "Ah, M-Mrs. Ford, I didn't know you had arrived..."
    scene w1_0844 with dissolve
    fel "Oh, I snuck in the back to give my regards to the chef."
    host "I..."
    "The maître d was at a clear loss of words, as she began to fidget uncomfortably under Felicia's scrutinizing gaze."
    "It was a look at odds with the capricious image I had developed in my mind of the blonde beauty."
    host "I'm so sorry, I didn't think--"
    scene w1_0846 with dissolve
    fel "You didn't think I'd catch you making my nephew wait outside while you snuck away to confirm if he actually belonged?"
    mct "(Nephew...?)"
    fel "...or did you not think being a snooty bitch would come back to bite you in the ass doing your {i}hospitality{/i} job of all things?"
    host "I'm... I'm SO sorry, Mrs. Ford. Please don't tell Chef Nicholas. I really didn't mean--"
    scene w1_0847 with dissolve
    fel "I don't really think I'm the one you should be apologizing to in this situation."
    host "Oh..! Right! Um, I'm sorry, sir."
    "The maître d turned to me and offered an apology made under duress, in a bid for self-preservation."
    "Due to second hand embarrassment, a part of me oddly sympathized with the woman."
    scene w1_0848 with dissolve
    mc "We can just put it all behind us, okay? I'd like to sit down and eat soon. I'm starving."
    "I decided to diffuse the situation, instead of making things more awkward."
    scene w1_0849 with dissolve
    fel "Well, you heard the man. Is our table ready?"
    host "Oh...! If you'll just wait here a moment, I'll go make sure your table is set."
    scene w1_0850 with dissolve
    fel "You do that."
    "Felicia made room for the maître d to scurry by, until it was just the two of us remaining in the reception area."
    scene w1_0851 with dissolve
    fel "Sorry about that, stud. I hope I didn't embarrass you too much."
    fel "That kind of attitude just pisses me off."
    scene w1_0852 with dissolve
    mc "It was kind of cool, actually. Can't say I've ever had a beautiful woman stand up for me like you just did."
    mc "You practically had her shaking in her heels."
    scene w1_0853 with dissolve
    "Felicia leaned in and turned her head, inviting me to politely kiss her cheek."
    fel "Well then, how about a kiss for your hero?"
    scene w1_0854 with dissolve
    "Sliding my hands around Felicia's waist, I planted a chaste kiss just below her eye."
    scene w1_0852 with dissolve
    mc "You look great tonight, by the way."
    scene w1_0855 with dissolve
    fel "Thanks, [mcf]."
    scene w1_0852 with dissolve
    mc "You could've give me a heads up about wearing something a little more appropriate though."
    mc "I was bound to look out of place anyway, but now next to you, I'm going to like an absolute slob."
    scene w1_0856 with dissolve
    fel "Aw, you look fine. I've had enough of men in penguin suits to last a lifetime, trust me."
    scene w1_0852 with dissolve
    mc "You really know the chef here?"
    scene w1_0857 with dissolve
    fel "I know a lot of people in this city. Too many."
    fel "Hell, I knew Kathleen even before Ian told me about the club. Well not personally, but I saw her speak once at a fundraiser for her dead sister's charity."
    scene w1_0852 with dissolve
    mc "You got to be kidding me?"
    scene w1_0856 with dissolve
    fel "You could imagine how fucking surprised I was about seeing her pimping girls at a cathouse. You know her husband's a judge?"
    scene w1_0852 with dissolve
    mc "You know, as much as it should, that doesn't surprise me."
    scene w1_0859 with dissolve
    host "Mrs. Ford and party, if you'll follow me right this way."
    "Just then, as our conversation was starting to meander, the maître d reappeared and invited us into the dinning room."
    scene w1_0860 with dissolve
    fel "By the way, just a heads up..."
    fel "Tonight, at least while we're having dinner, treat me like a lady. As in, don't get too handsy."
    fel "Unlike {i}Circus{/i}, I'm pretty well-known here."
    scene w1_0861 with dissolve
    "Felicia's words reminded me of the bitter fact that she's a married woman."
    mc "Right, appearances. We're basically just friends anyway, right?"
    if feliciaSex == True:
        "Even if we fucked around a little, that was all it was."
    scene w1_0862 with dissolve
    stop music fadeout 3.0
    "Our little side conversation finished, we turned and regarded the patiently waiting maître d, who was conspicuously trying her best not to make eye contact with either of us."
    scene w1_0863 with fade
    play music "music/cello-suite-No-1-G-Major-Prelude.mp3"
    waitress "Good evening, Mrs. Ford. Mr...?"
    scene w1_0864 with dissolve
    "The cute waitress looked at me expectantly, waiting for me to fill her in on how to address me."
    mc "Oh, uh.."
    scene w1_0865 with dissolve
    fel "[mcf] Barnes. He's my nephew, visiting from out of town."
    "Felicia added a little subterfuge to the mix."
    scene w1_0866 with dissolve
    waitress "I see... Well, welcome to the city, [mcf]."
    waitress "...and welcome both of you to {i}Il Piacere{/i}. My name is Jane and I'll be serving you tonight."
    scene w1_0865 with dissolve
    fel "You're new, aren't you?"
    scene w1_0863 with dissolve
    jane "That's right, Ma'am. I started this Monday."
    scene w1_0867 with dissolve
    fel "You're certainly a cute girl. You know, my nephew doesn't know anyone in town. Maybe you could show him around some time?"
    jane "I, uh..."
    "The waitress began to stammer, unsure of how to reply to such a shameless suggestion from a customer."
    scene w1_0868 with dissolve
    fel "Sorry! I'm kidding! I've got a terrible sense of humor."
    scene w1_0865 with dissolve
    fel "It's nice to meet you, Jane."
    scene w1_0863 with dissolve
    jane "You too, Mrs. Ford. I'm a big fan of your husband. I saw him speak at a seminar I took for my MBA program."
    scene w1_0867 with dissolve
    fel "...oh? I'll be sure to tell Elias there's a cute waitress at Nicholas' restaurant that's dying to meet him."
    scene w1_0869 with dissolve
    jane "You sure have a colorful sense of humor, Mrs. Ford. H-heh..."
    mct "(Hmm... Elias...)"
    mct "(Elias Ford? That sounds familiar. Where do I know that name...?)"
    scene w1_0863 with dissolve
    jane "Can I start you with a nice Cabernet Sauvignon tonight?"
    scene w1_0865 with dissolve
    fel "No, we'll have a bottle of Merlot I think."
    fel "You had some bottles of Petrus last week, if memory serves."
    scene w1_0870 with dissolve
    jane "We do have a couple remaining I believe. I'll bring it right out, Ma'am."
    stop music fadeout 3.0
    fel "Thank you, Jane."
    scene w1_0871 with dissolve
    "Following a curt bow, the waitress scurried off to the kitchen, leaving Felicia and I alone."
    play music "music/covert-affair.mp3"
    mc "So... nephew, huh?"
    scene w1_0872 with dissolve
    fel "You like that? Me pretending to be your {i}naughty{/i} aunt?"
    scene w1_0873 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Play along with her teasing. [gr]\[Felicia +1\]":
            $ Felicia_Affection += 1
            show screen textbox2 with dissolve
            mc "I suppose we could use that to spice things up later."
            scene w1_0874 with dissolve

            if feliciaSex == True:
                fel "Ohoho, pretty confident, aren't you? Just because you got lucky once doesn't necessarily mean I'm inclined to give you a repeat performance."
            if feliciaSex == False:
                fel "Ohoho, pretty confident, aren't you? You turned me down once, what makes you think I'm inclined to let you repeat the same mistake again?"

            fel "This is just an apology dinner for my little lie of omission, remember?"
            scene w1_0871 with dissolve
            mc "Right, straightly platonic."

        "Ask about the fake last name.":
            scene w1_0875 with dissolve
            show screen textbox2 with dissolve
            mc "Barnes, though?"
            scene w1_0876 with dissolve
            fel "It's my maiden name."
            scene w1_0871 with dissolve
            mc "I see... Felicia Barnes, huh?"
            scene w1_0877 with dissolve
            fel "It's a name I was happy to leave behind."


    scene w1_0878 with dissolve
    fel "Anyway, {i}nephew{/i}. It's plausible enough. I am older than you after all."
    scene w1_0875 with dissolve
    mc "Makes sense to me."
    scene w1_0879 with dissolve
    fel "I'll be right back. I need to hit the ladies room. Don't go anywhere, alright stud?"
    "Felicia got up and excused herself from the table."
    scene w1_0880 with circlewipe
    mct "(Hm... now's a pretty good time to answer that nagging question of where I'd heard Felicia's husbands name before.)"
    scene w1_0881 with dissolve
    "Pulling out my phone, I fingered the keypad and typed out {i}Elias Ford{/i} into the search engine and hit enter."
    scene w1_0882 with dissolve
    mct "(...wait, WHAT?!)"
    scene w1_0883 with dissolve
    show elias-search at Position (ypos=0.94)
    "I immediately got the answer I was looking for."
    mct "(Felicia's husband is that Elias Ford?!)"
    mct "(I knew Felicia was well off, but I had no idea she was THAT well off.)"
    "Elias Ford, while not a household name, was a man of wealth and means."
    "Heir to a (defunct) railway fortune, he cut his teeth in the logistics division of a major manufacturing company before branching out and starting a lucrative talent agency of all things."
    scene w1_0882 with dissolve
    mct "(...or that's what the internet says. What I know his name from is an initiative he personally sponsored around Morehead Hills to lower the city's carbon footprint.)"
    mct "(He leveraged his family's history in the rail freight business as if it was some kind personal impetus to make a change for the better.)"
    mct "(I remember thinking he looked pretty fucking smug in those city-wide ads...)"
    mct "(What am I doing mixed up with the wife of a local celebrity...?)"
    mct "(More still, what's a woman like that doing wrapped up in the Carnation Club?)"
    play sound "sound effects/sms-chime.wav"
    "*Chirp, chirp.*"
    mct "(Huh...? It's a message from Felicia...)"
    scene w1_0883 with dissolve
    hide screen textbox2 with dissolve
    call phone_start_fel from _call_phone_start_fel
    call message_img("Felicia", ";)","felicia01") from _call_message_img_2
    call phone_end_fel from _call_phone_end_fel
    scene w1_0884 with dissolve
    show screen textbox2 with dissolve
    mct "(Geez, this woman is shameless.)"
    mct "(...isn't that great?)"
    scene w1_0883 with dissolve
    hide screen textbox2 with dissolve
    call phone_start_fel from _call_phone_start_fel_1
    call message_img("Felicia", ";)","felicia01") from _call_message_img_3
    call screen phone_reply("Show me more.","felDateBathroomMore","What did I do to deserve this?","felDateBathroomDeserve")


label felDateBathroomMore:
    $ Felicia_Affection += 1
    call phone_after_menu from _call_phone_after_menu_14
    call message_start("[mcf]", "Got any more to show me?") from _call_message_start_21
    call message("Felicia", "Oh you greedy, greedy boy. Hold on a sec.") from _call_message_66
    call phone_end_fel from _call_phone_end_fel_1
    scene w1_0886 with dissolve
    show screen textbox2 with dissolve
    "Waiting... {w}Waiting..."
    play sound "sound effects/sms-chime.wav"
    "*Chirp, chirp.*"
    scene w1_0887 with dissolve
    "I scooped up the phone from the table, eager to see Felicia's next selfie."
    scene w1_0883 with dissolve
    hide screen textbox2 with dissolve
    call phone_start_fel from _call_phone_start_fel_2
    call message_img("Felicia", "Guess it can't hurt to spoil you. This is all you get, though... for now. ;)","felicia02") from _call_message_img_4
    call phone_end_fel from _call_phone_end_fel_2
    scene w1_0885 with dissolve
    show screen textbox2 with dissolve
    mct "(Nice...)"
    "In a rather impressive feat of dexterity, Felicia sent a selfie of her ass sticking out."
    scene w1_0888 with hpunch
    stop music
    play sound "sound effects/record-scratch.wav"
    fel "You should be careful. Anyone could just see that by looking over your shoulder."
    mc "-eh, --! Felicia!"
    scene w1_0889 with dissolve
    mc "You startled the crap out of me!"
    fel "You're lucky it was me. What if it was poor Jane who caught you looking at porn in public? You would've blown your chances with her."
    scene w1_0890 with dissolve
    mc "I think that would be the least of her issues, considering she would think I was looking at a nude-selfie of my aunt."
    fel "I see our cute waitress brought the wine already."
    jump w1FeliciaDateContinue

label felDateBathroomDeserve:
    call phone_after_menu from _call_phone_after_menu_15
    call message_start("[mcf]", "Not that I'm complaining, but what did I do to deserve this?") from _call_message_start_22
    call message("Felicia", "Just felt like sharing, stud.") from _call_message_67
    call phone_end_fel from _call_phone_end_fel_3
    scene w1_0891 with dissolve
    show screen textbox2 with dissolve
    mct "(Well, feel free to share more often.)"
    scene w1_0892 with fade
    fel "Miss me, nephew?"
    fel "I see our cute waitress brought the wine already. She didn't catch you peeking at nude photos of your 'aunt', did she?"
    scene w1_0893 with dissolve
    mc "...no, but to be honest I don't even remember her dropping the bottle and glasses off..."
    scene w1_0892 with dissolve
    stop music fadeout 3.0
    fel "You're kind of helpless aren't you?"
    "Felicia playful teased me, before returning to her seat."
    jump w1FeliciaDateContinue



label w1FeliciaDateContinue:
    scene w1_0894 with fade
    play music "music/jazz-piano-bar.mp3"
    fel "You like wine, [mcf]?"
    scene w1_0895 with dissolve
    mc "To be honest, I'm not a big drinker to begin with. Less so when it comes to wine."
    mc "This isn't half bad though."
    scene w1_0896 with dissolve
    fel "Well, I would hope so! That's one of the best red-- ah, who am I kidding?"
    fel "I was more of a liquor kind of gal when I was your age. Even now I'm not even sure if I really like this stuff."
    scene w1_0897 with dissolve
    fel "... but fake it until you make it, as they say. Getting blitzed on wine is pretty much part and parcel for the occupation of trophy wife."
    scene w1_0898 with dissolve
    fel "*Glug, glug*"
    scene w1_0899 with dissolve
    fel "It's important to fit in, you see."
    "Felicia spoke in a facetious manner, but there was something contemplative in her words."
    scene w1_0900 with dissolve
    mc "Is {i}trophy wife{/i} honestly how you view yourself?"
    scene w1_0901 with dissolve
    fel "I've got no qualms with it. It is what I am, after all. Didn't just happen into it either, I had to work for it."
    fel "Maybe it's not something to admit to in polite company, but there's no harm in being honest with you."
    scene w1_0900 with dissolve
    mc "You got to want more out of life than just being arm candy, right?"
    scene w1_0902 with dissolve
    fel "I think I've done alright for myself. Look at it at it this way, I'm the one treating you to dinner here, at one of the nicest places in town I might add."
    scene w1_0900 with dissolve
    mc "Yeah, but there's more to life than just comfort. For example, there's the fulfillment that comes from professional success or the joy of helping other people."
    scene w1_0901 with dissolve
    fel "Self-actualization, you mean? That's the very tippy-top of Maslow's hierarchy of needs. Are you familiar with that theory?"
    scene w1_0900 with dissolve
    mc "No, I've never heard of it."
    scene w1_0903 with dissolve
    fel "Well, it's a motivational theory that a person's needs can be broken up into five distinct categories and that each previous category has to be satisfactory fulfilled before moving onto the next."
    scene w1_0900 with dissolve
    mc "Basically, people are less concerned about job satisfaction when they're living paycheck-to-paycheck?"
    scene w1_0904 with dissolve
    fel "Exactly. What you're talking about is self-fulfillment, which comes not only after your basic needs of things like food and safety, but also after the need of love and self-esteem."
    scene w1_0902 with dissolve
    fel "Not a lot of people hit the peak you're talking about. Most just get hung up on paying their mortgage or dumb family bullshitery. I mean, how many people short of a sociopath can really even confidently say they love themselves?"
    scene w1_0903 with dissolve
    fel "As far as I'm concerned, security... comfort... {i}pleasure{/i}, that's the stuff a good life is made up of. Anything more is simply being greedy."
    scene w1_0900 with dissolve
    "As Felicia touted her hedonistic philosophy, I couldn't help but..."
    hide screen textbox2 with dissolve

    menu:
        "Crack a joke to lighten the conversation. [gr]\[Felicia +1\]":
            $ Felicia_Affection += 1
            show screen textbox2 with dissolve
            mc "Christ, you're not even drunk yet, are you?"
            scene w1_0905 with dissolve
            fel "Pfhahahaha...! You asshole."
            fel "We share a sense of humor. I like you, [mcf]."
            scene w1_0900 with dissolve
            mc "I like you too, Felicia. You're fun to be around."
            scene w1_0906 with dissolve
            fel "Hehehe, and sexually available too, yeah? That has something to do with it I bet."

        "Tell her you're impressed.":
            show screen textbox2 with dissolve
            mc "Sounds like you've given a lot of thought to this."
            scene w1_0902 with dissolve
            fel "I've had time. Don't forget I've got like 10 years of life on you, kid."


    scene w1_0903 with dissolve
    fel "Thanks for accepting my invitation, by the way."
    if feliciaSex == False:
        scene w1_0902 with dissolve
        fel "Especially after you shut a girl down last time. I would've felt real foolish if you turned me down a second time."
    scene w1_0900 with dissolve
    mc "It's weird you're thanking me, when I'm the one who should be..."
    scene w1_0907 with dissolve
    mc "Oh, is that our food? We didn't even order, did we?"
    scene w1_0908 with dissolve
    fel "That's because Il Piacere's menu is table d’hôte."
    scene w1_0909 with dissolve
    mc "Sure, yeah... table dowhotay. Of course. Duh."
    mc "...sorry, I've got no idea what that means."
    scene w1_0910 with dissolve
    fel "It means you don't get to choose what you're served."
    scene w1_0911 with dissolve
    mc "That seems odd for a restaurant. What if I don't like what they're serving?"
    scene w1_0912 with dissolve
    fel "{i}Trust{/i} me. You'll like it."
    scene w1_0913 with dissolve
    fel "So, what do you have here?"
    scene w1_0914 with dissolve
    jane "The first course is fettuccine alfredo topped with roasted baby tomatoes."
    scene w1_0915 with dissolve
    mc "Uh... {i}first{/i} course?"
    "I said, staring down a heap of food."
    scene w1_0916 with dissolve
    fel "Yep, you better have room."
    fel "Chef Nicholas comes from a traditional Italian family. Which is to say, he prides himself in making sure all of his customers are well fed."
    scene w1_0917 with dissolve
    stop music fadeout 3.0
    mc "Heh... I guess bring it on."
    scene black with fade
    "3 courses of food later..."
    scene w1_0918 with dissolve
    play music "music/thief-in-the-night.mp3"
    mc "Mmgnng..."
    "Having scarfed down everything that had been put in front me, I felt like I was about to die."
    scene w1_0919 with dissolve
    mc "I don't think I've ever had a more delicious meal. Ever."
    mc "Seriously Like, for real. {b}Ever{/b}."
    scene w1_0920 with dissolve
    fel "I will say, I thought you might enjoy it. You don't need to tell me though, I can see by the look on your face."
    fel "Only two things leave a man looking like that."
    scene w1_0921 with dissolve
    fel "Food is one of them."
    scene w1_0922 with dissolve
    mc "I mean, who knew food could taste like this? I didn't."
    mc "To be honest though, this was my first time trying fine dining."
    scene w1_0923 with dissolve
    fel "Well, I'm glad to hear it. You look as happy as a pig in muck, as my granny used to say."
    scene w1_0924 with dissolve
    "A slight accent colored the end of Felicia's figure of speech, eliciting a curious look from me."
    mc "Was that a drawl in your speech I just heard?"
    scene w1_0925 with dissolve
    fel "Oh... don't pay any attention to that."
    fel "The southern girl in me slips out from time-to-time."
    fel "A well-timed glimpse of it can be charming, but going full-on country in Morehead Hills makes people look at you like you're a hick so I try to keep it to a minimum."
    scene w1_0926 with dissolve
    mc "That sounds... exhausting."
    "Felicia clearly puts a lot of effort into they way she presents herself. No surprise given how beautiful she is, but it seems to extend to all the way to the minutia."
    scene w1_0927 with dissolve
    fel "Not really. You speak differently with Ian than you do with your own mother, I'm sure. It's like that."
    scene w1_0928 with dissolve
    jane "How was everything tonight? Was everything satisfactory?"
    "The waitress reappeared to check on us, following the conclusion of our meal."
    scene w1_0929 with dissolve
    fel "It was. Pass my compliments along to the chef, please."
    scene w1_0928 with dissolve
    jane "I'll be certain to do that."
    scene w1_0930 with dissolve
    fel "Your service was excellent too. I'll be sure to pass that along myself."
    scene w1_0931 with dissolve
    jane "Thank you, Mrs. Ford. I appreciate it."
    scene w1_0928 with dissolve
    jane "Will that be all for the night?"
    scene w1_0929 with dissolve
    fel "It will."
    scene w1_0932 with dissolve
    jane "We were happy to have both you and Mr. Barnes here tonight. Thank you for dining with us."
    scene w1_0933 with dissolve
    "With a polite bow, the waitress dismissed herself for a final time, leaving us to figure out where to go from here."
    scene w1_0934 with dissolve
    fel "So, what's next?"
    scene w1_0935 with dissolve
    mc "You wanted to do something else?"
    scene w1_0934 with dissolve
    fel "Naturally. How does taking a walk and enjoying the night air sound?"
    scene w1_0935 with dissolve
    mc "Sure, I suppose I could do with walking off some of this food."
    scene w1_0936 with fade
    mc "Where to though?"
    fel "There's a nice park nearby. Should be the perfect place."
    fel "At this time of night, we'll have a little privacy too."
    mc "Alright, sounds good. Lead the way."
    stop music fadeout 3.0
    scene black with dissolve
    "......"
    "..."
    scene w1_0937 with blinds
    play music "music/Moonlight-Sonata.mp3"
    "After leaving Il Piacere, we did as Felicia suggested and found our way to a park that was connected to the restaurant's plaza."
    "Joining us on our leisurely walk was a gleaming full moon, hanging fat in the sky and graciously providing us with a nice backdrop for our idle chatter."
    scene w1_0938 with dissolve
    stop ambient
    mc "It's nice out tonight."
    "I said, painfully pointing out the obvious to get the ball rolling between us."
    fel "It is. The city  takes on a whole new character bathed in the moonlight, don't you think?"
    scene w1_0939 with dissolve
    "We both stopped for a moment to silently take in the night's atmosphere."
    scene w1_0940 with dissolve
    "While Felicia peered past the concrete-coated skyline and into the interminable inky-black sky, I found myself stealing a glance at my dinner companion."
    "Stunning as she may be in that dress, I couldn't help but notice she looked a little cold."
    scene w1_0941 with dissolve
    fel "...?"
    hide screen textbox2 with dissolve

    menu w1FelClose:
        "Pull Felicia closer to you. [gr]\[Felicia +1\]":
            $ Felicia_Affection +=1
            scene w1_0942 with dissolve
            show screen textbox2 with dissolve
            "Without saying a word, I drew closer to the moonlit beauty, wrapping my arm around her shoulder and pulling her closer to me."
            scene w1_0943 with dissolve
            "Quickly grasping my intention, Felicia nuzzled her face on my chest and let one of her hands snake around the small of my back to complete the embrace."
            if feliciaDaddy == True:
                scene w1_0944 with dissolve
                fel "You know just what a girl needs, when she needs it, {i}daddy{/i}."
                "Felicia indelicately teased me, harkening back to our encounter in Circus' bathroom. Hearing that line outside the throes of sexual passion immediately made my ears go red in embarrassment."
            else:
                scene w1_0944 with dissolve
                fel "You know just what a girl needs, when she needs it, Casanova."

            scene w1_0943 with dissolve
            "Felicia took a moment to snuggle more intimately, rubbing her soft cheek against the warmth of my chest, before silently pulling me toward a nearby park bench."



        "Suggest we sit down.":
            scene w1_0945 with dissolve
            show screen textbox2 with dissolve
            mc "You look a little cold just standing there."
            scene w1_0946 with dissolve
            mc "Why don't we sit down?"
            scene w1_0947 with dissolve
            fel "You're suggesting we snuggle in the park like a pair of lovers?"
            scene w1_0948 with dissolve
            mc "...really, you look cold."
            if feliciaDaddy == True:
                scene w1_0949 with dissolve
                fel "Thanks for your concern, {i}daddy{/i}."
                "Felicia indelicately teased me, harkening back to our encounter in Circus' bathroom. Hearing that line outside the throes of sexual passion immediately made my ears go red in embarrassment."
            else:
                scene w1_0949 with dissolve
                fel "Thanks for your concern, stud."


    scene w1_0950 with dissolve
    fel "You'd think I'd learn by now to bring a sweater whenever I go out."
    scene w1_0951 with dissolve
    fel "No complaints, I hope."
    "Felicia not-so-subtly tugged on my upper arm, sandwiching it between the warmth of her pendulous, sun-kissed breasts."
    scene w1_0952 with dissolve
    mc "You won't hear any from me."
    "Though, Felicia's affection did put a certain question forefront in my mind."
    scene w1_0953 with dissolve
    fel "What is it?"
    scene w1_0954 with dissolve
    "If I'm honest with myself, Felicia's blatant interest in me is an anomaly that strikes me as odd. I've never had a beautiful woman show a strong interest in me."

    if roseSeduceFlag == True:
        "Sure, most recently, there was Rose... but she was angling for an advantage at the club. Ostensibly, that isn't the case here with Felicia."
        "...I think."

    scene w1_0955 with dissolve
    mc "Why did you invite me out to dinner tonight? It wasn't really because you wanted to apologize, was it?"
    scene w1_0956 with dissolve
    fel "Aw, you figured me out. You're right, I don't really feel bad about my little surprise."
    fel "That look on your face was priceless. I loved it."
    fel "That was just a pretense to have dinner."
    scene w1_0959 with dissolve
    mc "Yeah, but... why then?"
    scene w1_0957 with dissolve
    fel "I had fun with you the other night, with Ian and Mina. What else?"
    scene w1_0958 with dissolve
    "She had said it simply, as a matter of genuine fact not to be disputed."
    "It left no room for doubt."
    scene w1_0957 with dissolve
    fel "That was a silly question."
    scene w1_0955 with dissolve
    mc "Sorry, it's just most guys would be a little dubious of a beautiful woman's advances."
    scene w1_0956 with dissolve
    fel "Right, because guys should be the one to do the chasing, right? Screw that. Life is too short not to go after what you want."
    scene w1_0959 with dissolve
    mc "No... it's more like you're a rich, classy woman with the world at her fingertips and I'm a broke college student with, let's be honest, passable looks."
    scene w1_0960 with dissolve
    "Felicia narrowed her brow in a similar fashion I had just previously seen with the rude maître d."
    mct "(Shit, did I say something to make her mad?)"
    scene w1_0961 with dissolve
    "Surprisingly, Felicia firmly took my head in her hands and brought her face to mine like she was about to kiss me."
    mct "({i}Is{/i} she about to kiss me...?)"
    scene w1_0962 with dissolve
    fel "[mcf]..."
    scene w1_0963 with dissolve
    mc "Yeah...?"
    scene w1_0962 with dissolve
    fel "Shut. {w}The.{w} {b}Fuck{/b}. {w}Up with that shit."
    scene w1_0961 with dissolve
    "It was a forceful command that left no room for refusal."
    scene w1_0963 with dissolve
    mc "...okay."
    scene w1_0961 with dissolve
    mct "(No harm in listening to the lady.)"
    scene w1_0964 with dissolve
    fel "...good!"
    scene w1_0965 with dissolve
    "Staring Felicia straight in the eye like this, nose tickled with her perfume, and her glossy lips within reach..."
    "It made me want to..."
    hide screen textbox2 with dissolve

    default dynamicChoice3 = ""
    if Felicia_Affection >= 22:
        $ dynamicChoice3 = "{color=#0f0}[Felicia +1]"
    else:
        $ dynamicChoice3 = "{color=#f00}[Felicia -1]"

    menu:
        "Kiss Felicia. [gr]\[Toughness +1\] [dynamicChoice3]":
            $ toughness += 1
            show screen textbox2 with dissolve
            "With Felicia so close that I could feel her wine-scented breath on my skin, it was a trifling matter to steal a kiss."
            scene w1_0966 with dissolve
            "One slight, forward movement found our lips pressing together, in a chaste like fashion that was more skin on skin rather than a proper kiss."

            if Felicia_Affection >= 22:
                $ Felicia_Affection +=1
                scene w1_0967 with dissolve
                fel "Mmh...?"
                scene w1_0968 with dissolve
                "After a moment's pause, Felicia parted her lips, pushing her tongue forward and using it to coax me into doing the same."
                "In a mishmash of action, the muscles in our mouth intertwined, coiled , and snaked their way past each other in an eager bid to probe each other's oral cavity as deeply and inimately as possible."
                scene w1_0969 with dissolve
                fel "Mmh... *Smack, chup*"
                "Felicia embraced me like a lover."
                "Tongues lashed against the inside of cheeks, scrapped against the surface of teeth, and brushed against the roof of mouths. It was so thorough that I was practically brought back to the world class dinner both of us just consumed."
                scene w1_0970 with dissolve
                fel "Mhwah...!"
                "Finally, Felicia was the one that dared to break the kiss."
                scene w1_0971 with dissolve
                fel "Who needs a sweater when you can just do {b}that{/b}?"

            else:
                $ Felicia_Affection -= 1
                fel "Mmh...?"
                scene w1_0977 with dissolve
                "...and that was all it remained, with Felicia pulling back from my gesture of intimacy."
                scene w1_0972 with dissolve
                fel "Guess I pretty much invited you to do that, huh?"
                fel "Sorry. I don't really like kissing unless we're screwing."


        "Boop her nose. [gr]\[Felicia +1\] [red]\[Toughness -1\]":
            $ Felicia_Affection +=1
            $ toughness -= 1
            show screen textbox2 with dissolve
            "That's right, a cute button nose like that, there's only one thing to do in this scenario...!"
            scene w1_0973 with dissolve
            mc "Boop!"
            "I quickly brought my finger to bare and pushed on Felicia's nose with tactical precision."
            scene w1_0974 with dissolve
            fel "......."
            fel "...pfft--"
            scene w1_0975 with dissolve
            fel "Hahahaha, what are you, a child? You know how to surprise a gal, that's for sure."
            scene w1_0976 with dissolve
            fel "Maybe there's the answer to your question."

    scene w1_0978 with dissolve
    "As Felicia pulled away, I was suddenly aware of the space the blonde beauty no longer occupied.."
    scene w1_0979 with dissolve
    fel "How are you liking the club, by the way? I know you're new there, right?"
    fel "Ian told me as much, when he first wanted to introduce us."
    scene w1_0980 with dissolve

    if id_greed == True:
        mc  "It's a {i}new{/i} experience, that's for sure. A profitable one too."
    else:
        mc "It's a {i}new{/i} experience, that's for sure."

    mc "That's how I've come to think about it at least, once I got over the initial shock."
    scene w1_0981 with dissolve
    fel "I was surprised to learn about it, myself. At first, I thought Ian was just drunk and bullshitting me."
    scene w1_0980 with dissolve
    mc "Did he really just... let it casually slip out like that?"
    scene w1_0978 with dissolve
    "I know I may just be the new guy, but the old adage {i}loose lips sink ships{/i} seems to be a relevant one for an underground prostitution ring."
    "Just a feeling."
    scene w1_0979 with dissolve
    fel "Yeah, he did. Told me about what kind of place it is, said he thought I'd fit in and have a good time."
    scene w1_0980 with dissolve
    mc "Okay, yeah... I'm glad you brought this up, because this has been a huge curiosity for me."
    mc "Did you really join up just for... {b}fun{/b}?"
    scene w1_0982 with dissolve
    "Felicia paused, appearing to be mulling over her answer."
    scene w1_0981 with dissolve
    fel "Hehehe, yep! I have high hopes for this place, too."
    scene w1_0983 with dissolve
    "Felicia's seemingly frivolous response had me in pure awe."
    scene w1_0984 with dissolve
    fel "...you're looking at me like I have a few screws loose. I don't appreciate it."
    scene w1_0985 with dissolve
    mc "I mean, it does sound odd."
    scene w1_0986 with dissolve

    if feliciaDaddy == True:
        fel "Odd...? Allow me to illustrate something for you, {i}daddy{/i}."
    else:
        fel "Odd...? Allow me to illustrate something for you, stud."

label w1FelFantasy:
    if _in_replay:
        show screen textbox2 with dissolve
    scene w1_0987 with fade
    "Within an instant, Felicia had thrown herself on top of me."
    scene w1_0988 with dissolve
    mc "Gneh...?"
    scene w1_0989 with dissolve
    "The feeling of my back being firmly pressed against the hard, wooden surface of the bench coaxed out a surprised groan from my vocal cords."
    "She had me pinned like cougar holding down its prey, in every sense."
    fel "You like the feeling of me pressed against you like this?"
    scene w1_0990 with dissolve
    mc "Uh..."
    scene w1_0991 with dissolve
    mc "Well..."
    scene w1_0989 with dissolve
    "Without really processing what she was asking me, my head swiveled back and forth in an anxious motion, concerned that someone might just be nearby."
    fel "Don't be so tense. I'll ask you again..."
    scene w1_0992 with dissolve
    fel "You like having your face jammed into my tit flesh, right?"
    scene w1_0993 with dissolve
    mc "Nng... of course I do."
    "No sense in lying to the woman. It's be like trying to tell her the sky isn't blue."
    fel "Good, now close your eyes for me, will you? I want you to imagine something..."
    mc "What if someone..."
    fel "Sssh! Close your eyes and imagine what I tell you."
    mc "..."
    "It's hard to argue with a woman like Felicia, she has a certain indiscernible effect on me."
    "Perhaps for obvious reasons, like her being a beautiful and sexy woman, but there was a primal element to her personality that made refusing her feel like a futile effort."
    "Basically, saying no to her felt like I'd be pissing into the wind."
    mc "Okay."
    scene black with fade
    stop music fadeout 3.0
    "Doing as she asked, I closed my eyes."

    if feliciaDaddy == True:
        fel "Thanks for humoring me, Daddy."
    else:
        fel "Thanks, stud."

    fel "I promise, you're going to like the picture I'm about to paint for you."
    fel "But first... we've got to lay down a little {i}primer{/i}."
    "The last bit of her metaphor was carried under a whisper, hot breath pitched directly into my earlobe like some kind of auditorial foreplay."
    "I shivered in anticipation and Felicia pressed on, dotting my neck with little kisses while craning a hand down past my stomach and onto the crotch of my jeans."
    scene w1_1001 with radio
    play music "music/leaving-home.mp3"
    fel "Picture this: we're center stage at the club. You and me, stud."
    fel "I'm helplessly locked into place. You're off to the side, taking in the sight."
    scene w1_0994 with Dissolve(2.0)
    fel "All you see in front of you is a mewling bitch, grunting and whining, having been teased for nearly an hour without release."
    fel "It's a {b}pathetic{/b} sight, isn't it? A woman my age, of my social standing, shaking her hips like a wanton whore, instinctually trying to entice you to ram your fat cock into my twat and give me what I desperately crave."
    fel "You and I, we're not alone though..."
    play sound "sound effects/zipper.wav"
    "*Ziiiiiip*"
    "At this junction of whatever batshit crazy scenario that Felicia was building for me, I felt a tugging sensation at the mouth of my jeans, followed by the loud sound of my fly being unzipped."
    scene w1_0995 with dissolve
    mct "(Huh...?)"
    "What naturally followed was the warm sensation of Felicia gripping my erect cock in her soft hands."
    mct "(Don't you--)"
    scene w1_0996 with dissolve
    fel "{b}Sssh! Close your eyes!{/b}"
    scene black with fade
    "I did as I was bid, unable to resist the blond bombshell as she gently began to stroke my cock out in the open air."
    fel "Now, where were we...? Right."
    fel "You and I, we're not alone. Out past the stage, is a number of familiar faces. Patrons of the club."
    scene w1_0997 with radio
    fel "People of worldly influence, admired and looked up to."
    fel "Men of good moral standing... fathers, community leaders, philanthropists..."
    fel "Right now though, they're no longer those things, are they? No, they're {i}paying customers{/i}, vulgar and base, eager to view what {b}you{/b} are about to do to me."
    scene w1_0998 with dissolve
    fel "It's the same for me, too. You're looking at me, but you're no longer seeing the woman you had dinner with tonight. No."
    fel "I'm not Felicia anymore, I'm just a cock-hungry bitch, drooling and babbling for release."
    fel "Not a single soul in the room is what they seem, are we? In this room, we've all changed into something else, dragged down into the muck."
    mc "---gh!"
    "I cried out, as Felicia intensified her efforts at getting me to climax with her hands and words."
    fel "You're not immune to the transformation, either."
    fel "You're no longer a student right now. All that studying, that stressful daily grind to establish yourself as a respectable adult, that's out the window."
    fel "All you know right now is what's in front of you... a drooling cunt and ripe, fuckable asshole completely at your mercy."
    fel "The only question is: what are you going to do with them?"
    scene w1_0999 with fade
    mct "...huh? Eh...?"
    scene w1_1000 with dissolve
    fel "Close your eyes! I {b}said{/b{}...!"
    mc "---Gha...!"
    "Felicia emphasized her question by jerking my cock at a furious, mind-melting pace."
    scene w1_0994 with radio
    fel "What are you going to do to me, [mcf]?"
    fel "You're not going to fuck my cunt. Not yet, anyway. That'll be giving me what I want."
    fel "...but maybe you'll fuck my ass, or perhaps even that is too much satisfaction for a despicable slut in front of you."
    "Felicia had me utterly charmed, enraptured in the fantasy she was curating. She spoke directly to the dirty impulses housed in the deep recesses of my brain, driving them out of me and compelling me to give them a voice."
    fel "C'mon, tell me! What do I deserve?"
    "For that reason, I gave her an answer."
    mc "I'm going to fuck that ass!"
    "I was now actively taking part in Felicia's erotic story, hanging off every word and uttering ridiculous declarations."
    scene w1_1002 with dissolve
    fel "That's right! You're going to fuck my ass, again and again."
    fel "No lube needed either, I'm already {i}flooding{/i} out of my other hole. All you got to do is reach down and slather your cock with what's freely available."
    fel "You'll push into me, down to the base in one quick motion, causing me to squeal incoherently."
    fel "You'll give me a proper spanking while you're at it, won't you? Enjoying the way my ass spams with every blow."
    fel "Mmmh... you enjoy watching it bounce, don't you?"
    mc "ng...! I do! How can such a tight ass shake like that?!"
    scene w1_1003 with fade
    "As I had quickly discovered, Felicia had a talent for this, using her words to tease and cajole, ushering me closer toward a climax."
    "Every obscene line was delivered in a saccharine tone, hitting their mark in between kisses and nibbles to my chest, neck, hands..."
    mct "(How the hell did it suddenly end up like this...?)"
    scene w1_1004 with radio
    fel "How many times have you cummed now? Twice, three times...?"
    fel "By now, you've packed my bowels with your jizz, every thrust displacing more and more of the thick cum."
    fel "Anything even approaching a coherent thought has been fucked out of my head. All that's left is pure carnal delight."
    mc "Ngghah--!"
    "Soon, I was feeling the recognizable signs of impeding orgasm, my balls beginning to churn and tighten, ready to fire..."
    play sound "sound effects/spurt.wav"
    scene w1_1005 with flash
    mc "--!"
    "I felt my cock rapidly swell and bloat, inducing a mind-racking pleasure that shook my entire nervous system."
    play sound "sound effects/spurt.wav"
    scene w1_1006 with flash
    "Felicia's tight grip now felt like pure fire on my overly sensitive prick, but I wasn't done yet...!"
    mc "Gguuuh!"
    play sound "sound effects/spurt.wav"
    scene w1_1007 with flash
    "Using just her hand and the power of her imagination, Felicia had extracted from me what I felt like was the biggest orgasm of my life."
    mct "(Ghh-what the fuck, is she some kind of succubus?)"
    scene black with fade
    "......."
    fel "Jeez, that was a ton! You could fill a glass mug with all that jizz."
    mc "*Pant* *Pant* Heheh..."
    scene w1_1008 with dissolve
    mc "Wha- where did that come from? That was out of fucking no where."
    scene w1_1009 with dissolve
    fel "I wanted to prove a point is all, after you looked at me funny."
    scene w1_1010 with dissolve
    mc "Huh...?"
    "I felt utterly scatterbrained, unable to really recollect what proceeded this burst of sexual energy."
    scene w1_1011 with dissolve
    fel "You were thinking there was something wrong with me for participating in the club out of personal enjoyment."
    scene w1_1010 with dissolve
    mc "Oh, right..."
    "Our conversation had drifted that way."
    scene w1_1011 with dissolve
    fel "This was my refutation of that."
    scene w1_1012 with dissolve
    mc "I'm not--"
    scene w1_1013 with dissolve
    fel "--you had a blast, didn't you?"
    scene w1_1015 with dissolve
    fel "Picturing yourself sinking that low, imagining fucking me silly to in front of a bunch of old men who were jealous of your youthful stamina. You enjoyed it, right?"
    fel "I enjoyed it too. For the same reasons as you. Being debased by another person can be {b}fun{/b}. Debasing yourself through the act of debasing another person can be {i}freeing{/i}."
    scene w1_1013 with dissolve
    fel "My point is, it isn't unnatural to lean into your desires. That's why I'm participating in Kathleen's little game, to answer the question."
    scene w1_1014 with dissolve
    "I couldn't deny that her words did have an effect on me. The fantasy she was dealing me, along with the physical affection she doled out, had pushed me easily over the edge."
    "Still... the operative word there is {b}fantasy{/b}. There's a clear delineation from finding something hot, to actually wading gung-ho into those depraved waters."
    "Then again, I guess I've already cannonballed into those depths to begin with. Is there any harm in enjoying the swim?"
    hide screen textbox2 with dissolve

    menu:
        "Admit to Felicia she made a convincing point. [gr]\[Felicia +1\] \[Toughness +2\]":
            $ Felicia_Affection += 1
            $ toughness += 2
            scene w1_1016 with dissolve
            show screen textbox2 with dissolve
            mc "If my partner was you, I can't deny that the exhibition might be fun for me too."
            scene w1_1018 with dissolve
            fel "Hehehe, you like me that much? Thanks for the compliment, stud!"


        "Tell her it stills seems extreme to you. [red]\[Toughness -2\]":
            $ toughness -= 2
            scene w1_1017 with dissolve
            show screen textbox2 with dissolve
            mc "I don't know if I agree with that. It seems extreme to me. Sure, I got off, but..."
            mc "I could get off to a bloated clown corpse if you were the one whispering the description in my ear while stroking my cock."
            scene w1_1019 with dissolve
            fel "Is that so...? Well, I guess thanks for the compliment... I think, but I'm not sure if I one hundred percent buy it."

    scene w1_1020 with dissolve
    $ history_felicia = "I had dinner with Felicia, which granted me with more than a few interesting insights into her character. It turns out her husband is Elias Ford, a wealthy businessman well-known around the city. It's a revelation that gives me a sinking feeling. This could mean trouble..."
    $ unread_felicia = True
    play sound "sound effects/notification.wav"
    show bioupdate with dissolve
    fel "You walked, right? I'll give you a ride home."
    fel "I've got some stuff in the morning, unfortunately. So I'm going to call it here."
    scene w1_1021 with dissolve
    mc "Yeah, I'd appreciate that."
    stop music fadeout 3.0
    "....."
    "..."
    $ renpy.end_replay()
    scene black with fade
    if not persistent.felW1FantasyGallery:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.felW1FantasyGallery = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)
    "Just like that, our date had concluded with a whirlwind of a bizarre ending."
    "Despite learning a lot about Felicia, she still felt unquantifiable - unable to be neatly fit into pre-packaged terms."
    mct "(Perhaps that's because she's insane...?)"
    jump w1June03End


label w1FeliciaFlagDeny:
    stop music fadeout 3.0
    scene w1_1022 with dissolve
    "With nothing to do for the day, I whiled away my time watching movies."
    "One of them was a fantasy story about three adventurers tasked with saving the realm from ancient, outside forces."
    "It had everything from action to gratuitous fan service."
    jump w1June03End



label w1June03End:

    scene w1_0804 with fade

    if feliciaFlag == True:
        mct "(What a day, treated to a fine meal and a handjob in a park from a wealthy, married woman.)"

        if hanaFlag == True:
            mc "(What's tomorrow going to look like...? Oh, yeah. I told Hana I'd come to the Asp Hole and see her band play. Live music isn't really my thing, but it should be fun. I'm enjoying getting out of the house more than I used to.)"
            scene w1_0817 with dissolve
            mct "(At any rate, today's events tuckered me out...)"
            scene w1_0422 with dissolve
            "......"
            scene black with fade
            "..."
            jump w1HanaDateStart

        else:
            mct "(Hana had asked me to come see her play tomorrow, but I turned her down. Looks like I'll be taking it easy tomorrow, which isn't a bad thing.)"
            mct "(A {i}me{/i} day evey now and then is good for the mental health.)"
            scene w1_0817 with dissolve
            mct "(At any rate, today's events tuckered me out...)"
            scene w1_0422 with dissolve
            "......"
            scene black with fade
            "..."
            hide screen textbox2 with dissolve
            hide screen qmenu with dissolve
            play sound "sound effects/sting-bluesy-vibes.wav"
            scene transitionhana02 with blinds
            $ renpy.pause(6, hard=True)
            jump w1June05Start


    else:
        mct "(I did absolutely nothing productive today. These kind of days are rare, and necessary for my mental health, but I always feel guilty about the wasted time.)"

        if hanaFlag == True:
            mct "(What's tomorrow going to look like...? Oh, yeah. I told Hana I'd come to the Asp Hole and see her band play.)"
            mct "(Should be fun. Live music isn't really my thing, but getting out and experiencing life occasionally could do me some good.)"
            scene w1_0817 with dissolve
            mct "At any rate, I'm surprisingly sleepy..."
            scene w1_0422 with dissolve
            "......"
            scene black with fade
            "..."
            jump w1HanaDateStart

        else:
            mct "(Tomorrow is probably going to be the same, unless something comes up. Hana had asked me to come see her play, but I turned her down.)"
            scene w1_0817 with dissolve
            mct "At any rate, I'm surprisingly sleepy..."
            scene w1_0422 with dissolve
            "......"
            scene black with fade
            "..."
            hide screen textbox2 with dissolve
            hide screen qmenu with dissolve
            play sound "sound effects/sting-bluesy-vibes.wav"
            scene transitionhana02 with blinds
            $ renpy.pause(6, hard=True)
            jump w1June05Start




label w1HanaDateStart:

    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionhana01 with blinds
    $ renpy.pause(6, hard=True)
    $ date = "june04day"
    scene black with blinds
    play sound "sound effects/alarmclock-digital.wav"
    scene w1_1023 with sunshine
    $ renpy.pause(2, hard=True)
    play sound "sound effects/bacon-sizzle.wav"
    scene w1_1025 with dissolve
    $ renpy.pause(3, hard=True)
    play ambient "sound effects/shower.wav"
    play sound "sound effects/teeth-brush.wav"
    scene w1_1024 with dissolve
    $ renpy.pause(5, hard=True)
    stop ambient
    stop sound
    scene w1_1026 with dissolve
    show screen textbox2 with dissolve
    show screen qmenu with dissolve
    mc "Hmmh~ mmhh~"
    scene black with blinds
    $ date = "june04night"
    play sound "sound effects/door-openclose.wav"
    "After a day of relative routine, I made my way to the Asp Hole."
    "Thanks solely to the help of the almighty internet I might add, as Hana's directions proved to be utterly indecipherable."
    scene w1_1027 with fade
    show june04night with squares
    play music "music/heavy-trailer-1.mp3"
    "What I found was a rather open venue, grimy and made to look like it had been carved into a rockface."
    "What I didn't find, amongst the sparse crowd, was Hana."
    mct "(I guess I'll go ask the bartender.)"
    scene w1_1028 with fade
    mc "Hey! Is Hana around? I was told she's playing here with her band tonight."
    scene w1_1029 with dissolve
    "The bartender looked up from the glass she seemed to be perpetually cleaning, and gave me a quick look up and down."
    scene w1_1030 with dissolve
    bar "You're not some kind of crazy stalker-fan type, are you?"
    scene w1_1031 with dissolve
    mc "Would I tell you if I were?"
    scene w1_1032 with dissolve
    bar "..."
    scene w1_1033 with dissolve
    mc "I'm a co-worker of hers. Hana asked me to come see her play tonight."
    scene w1_1034 with dissolve
    bar "Oh! That's a shame."
    scene w1_1035 with dissolve
    bar "This is about the usual Thursday night crowd."
    scene w1_1036 with dissolve
    "The bartender directed me to look behind me, where a thin assembly of people were milling about, slamming back cheap bears, or just otherwise NOT gathering around the simply constructed sound stage."
    mct "(Oh...?)"
    scene w1_1037 with dissolve
    "Off in a corner, I spotted two familiar faces. Harper and Jacob, chatting idly amongst themselves away from the crowd, if you could call it that."
    bar "No one's really {i}here{/i} for them. They could really use a fan or stalker or two."
    scene w1_1038 with dissolve
    bar "I like 'em, though. They got a lot of spirit, which is why I throw a gig their way every now and then, at least on the slow nights."
    scene w1_1039 with dissolve
    mc "You know where she's at? I'd like to say hi."
    scene w1_1040 with dissolve
    bar "In the back, with the rest of the band. They're on in five."
    scene w1_1039 with dissolve
    mc "I guess I'll say hello after then."
    scene w1_1041 with dissolve
    mc "I'm not..."
    scene w1_1042 with dissolve
    bar "First one's on the house, since you're a guest of the band."
    scene w1_1043 with dissolve
    mc "Alright, thanks."
    scene w1_1044 with dissolve
    "..."
    scene w1_1045 with dissolve
    mct "(--gh!)" with hpunch
    mct "(Yeah, no shit it's on the house. This tastes like water downed piss.)"
    scene w1_1046 with dissolve
    mct "(Maybe I should go over and say hello to Jacob and Harper? After finding a place to set down and conveniently forget my drink somewhere, of course.)"
    scene w1_1047 with dissolve
    mct "(Wait a minute...)"
    scene w1_1048 with dissolve
    mc "That's Mr. Byrnes, what the hell is he doing here?"
    "Standing be himself in the back of the club, was August."
    scene w1_1049 with dissolve
    "One would assume, on first and second glance, that the old man would look painfully out of place against the dingy backdrop wearing his yellow shirt and grey leisure suit, but that wasn't the case."
    "Instead, he stood there with an inscrutable expression on his face, calm and comfortable, looking like he was part of the building itself."
    mct "(Thinking back to Veronica's audition, blow up aside, the two did sit together. Maybe they're close?)"
    scene w1_1050 with dissolve
    mc "Hm..."
    mct "(Who should I go over and see?)"
    hide screen textbox2 with dissolve
    stop music fadeout 3.0

    menu:
        "Walk over and say hello to your boss. [gr]\[August +1\]":
            $ August_Friendship +=1
            jump w1HanaDateAugust
        "Walk over and say hello to Jacob and Harper. [gr]\[Jacob +1\] \[JacobHarperVouch\]":
            $ Jacob_Friendship +=1
            $ jacobHarpVouch = True
            jump w1HanaDateJH

label w1HanaDateAugust:
    play music "music/big-rock.mp3"
    show screen textbox2 with dissolve
    "I decided that saying hello to my boss would be the most prudent and conscientious thing to do."
    scene w1_1051 with cmet
    aug "Hiya, kid. Would've kept talking to the hot bartender if I were you."
    scene w1_1052 with dissolve
    mc "Hey, Mr. Byrnes, uh..."
    scene w1_1053 with dissolve
    aug "August. Drop the mister unless you want me to dock your pay."
    scene w1_1054 with dissolve
    "While he smiled widely, he sounded like he wasn't kidding..."
    scene w1_1052 with dissolve
    mc "{i}August{/i}, right. I just wanted to come by and say hello. I'm surprised to see you here."
    scene w1_1051 with dissolve
    aug "Too old for the place, you mean?"
    scene w1_1055 with dissolve
    mc "No, uh... it's just..."
    mc "It's just you're such a perfect fit for the Carnation Club that seeing you outside of it at all, let alone at a punk bar is a little surreal."
    scene w1_1053 with dissolve
    aug "I'll have you know, my generation {b}invented{/b} punk."
    scene w1_1056 with dissolve
    aug "...I just left my mohawk in another decade, that's all."
    scene w1_1057 with dissolve
    mc "Heh, I guess I'm one to talk here."
    scene w1_1051 with dissolve
    aug "To answer the question you were about to get to... I'm only here for the same reason I assume you are. To see our girl play."
    aug "She didn't ask me to come though, so don't tell her you saw me, alright?"
    scene w1_1054 with dissolve
    "August said something a little concerning. Does Hana not want him here or something?"
    scene w1_1058 with dissolve
    aug "Keep it a secret, between men."
    scene w1_1059 with dissolve
    mc "Sure, but this place isn't packed, she's going to spot you..."
    scene w1_1060 with dissolve
    aug "I'll duck out before she even knows I was here."
    scene w1_1061 with dissolve
    mc "Why do you have to do that?"
    scene w1_1062 with dissolve
    aug "Let's just say that girl isn't the biggest fan of mine right now, try as I might to get her to come around on me."
    scene w1_1063 with dissolve
    mct "(That's... vague.)"
    mc "Alright, sure. You were never here."
    scene w1_1064 with dissolve
    aug "Good, good! Do that. It'll be nice to know {b}someone{/b} can keep a damn secret amongst the staff."
    "August narrowed his gaze and looked past me, clearly having a person or two in mind with that statement."
    scene w1_1063 with dissolve
    hide screen textbox2 with dissolve

    menu w1HanaDateAugustMenu:
        "{color=#FF1493}\[Social Chameleon]{/color} Emphasize your trustworthiness to your boss. [gr]\[August +2\]" if perk_socialChameleon == True:
            $ August_Friendship += 2
            $ w1AugustTrust = True
            show screen textbox2 with dissolve
            "Maybe I could use this to score a few brownie points?"
            "This is a gamble, but I'm pretty sure he's referring to either Ian or the guy who had my job before me..."
            mc "You don't have anything to worry about there, August. Not for this small matter, nor any other size. I'm {i}very{/i} good at keeping my mouth shut."
            mc "Not like my predecessor, right? Don't worry, I'm not like him."
            scene w1_1065 with dissolve
            aug "...huh? Wait, did Kathy te--"
            scene w1_1066 with dissolve
            aug "Oooooh! Ha, you're an astute kid, aren't you?"
            scene w1_1061 with dissolve
            mc "I just put two-and-two together, from what I've heard."
            scene w1_1064 with dissolve
            aug "You're right, we had some troubles there. A little with Killian too. Both of them could get a little loose lipped when they got shitfaced. You can understand how problematic that can be for an extralegal business like ours"
            scene w1_1063 with dissolve
            mc "Yeah, I can see how that might cause some headaches."
            scene w1_1062 with dissolve
            aug "Thankfully it was never {i}too{/i} serious, but it proved to me I couldn't really rely on either of them for delicate work."
            scene w1_1066 with dissolve
            aug "Darius may have quit on us, but Killian is still there, so be a correcting influence on the boy, yeah?"
            scene w1_1061 with dissolve
            mc "You can count on me."

        "Tell August he can trust you. [gr]\[August +1\]":
            $ August_Friendship += 1
            $ w1AugustTrust = True
            show screen textbox2 with dissolve
            mc "No worries there, August. You can trust me."
            scene w1_1061 with dissolve
            mc "Considering the business I'm now in, and the plans I have for my future, I can't afford any kind of fucks up, y'know? Mums the word, for more than just this small thing."
            scene w1_1066 with dissolve
            aug "You got a level head on you, kid. I like that."
            aug "I've got a good feeling about you."


        "Don't make any future promises.":
            show screen textbox2 with dissolve
            "Sure, I might be able to use this moment to ingratiate myself to my boss, but I don't know what the future may hold. Best not to build up any expectations, in case I can't meet them."


        "{color=#696969}\[Social Chameleon] Emphasize your trustworthiness to your boss.{/color}." if perk_socialChameleon == False:
            jump w1HanaDateAugustMenu

    scene w1_1067 with dissolve
    aug "Any--"
    "As we spoke, the band began to take the stage."
    scene w1_1068 with dissolve
    "I counted three people. There was Hana, a woman with vibrant pink hair, and a funny looking man in an eye-catching red jacket."
    scene w1_1069 with dissolve
    $ history_august = "To my surprise, I ran into the old man at Hana's show - a secret he insisted I keep from her. Just what's going on there?"
    $ unread_august = True
    play sound "sound effects/notification.wav"
    show bioupdate with dissolve
    aug "Scram, kid. Better get to the dance floor and cheer you head off. That's an order."
    mc "Right, guess you're staying back here. See you."
    scene w1_1070 with dissolve
    "After bidding goodbye to August, I made me way to the open area in front of the stage."
    stop music fadeout 3.0
    "It being so lightly packed, I picked a spot near my fellow co-workers, prompting a friendly wave from Jacob and absolutely nothing at all from Harper."
    mct "(I get the feeling she doesn't like me.)"
    jump w1HanaDatePerformance


label w1HanaDateJH:
    play music "music/big-rock.mp3"
    show screen textbox2 with dissolve
    "I decided to greet my fellow co-workers instead of my boss, as quite honestly, it's a more pleasant prospect than trying to make small talk with the enigmatic grandpa."
    scene w1_1071 with dissolve
    mc "Hey, guess Hana roped all of us into seeing her play, eh?"
    scene w1_1072 with dissolve
    jacob "Yep, I turned her down the first time. And the second time. The third, the fourth... well, you get the picture. I relented on the fifth. The little missy can be {i}endearingly{/i} insistent."
    scene w1_1073 with dissolve
    harp "Mh..."
    "Where the two of them had looked rather chatty as I approached, Harper had now fallen awkwardly silent."
    scene w1_1074 with dissolve
    mc "Eh...? I hope I'm not interrupting anything."
    scene w1_1075 with dissolve
    jacob "Don't worry about that."
    scene w1_1076 with dissolve
    jacob "Lighten up, Harps. [mcf] is cool, aren't you [mcf]?"
    scene w1_1077 with dissolve
    mc "Yeah, I'm cool."
    scene w1_1078 with dissolve
    jacob "Hana invited him, remember?"
    scene w1_1079 with dissolve
    harp "...sorry. You're right, Jacob. We're all here to have fun."
    scene w1_1080 with dissolve
    harp "Nice to see you, [mcf]."
    mc "You too, Harper."
    scene w1_1081 with dissolve
    harp "I'm going to get a beer, either of you want one?"
    scene w1_1082 with dissolve
    jacob "Negative."
    mc "Nope."
    "We were both quick to turn down her offer."
    scene w1_1083 with dissolve
    jacob "Alright, I'll be right back."
    scene w1_1084 with dissolve
    mc "I get the feeling she doesn't like me..."
    mc "Not sure what I possibly could've done, I've barely said a word to her."
    scene w1_1085 with dissolve
    jacob "It's nothing personal, you're just... {b}management{/b}."
    scene w1_1084 with dissolve
    mc "I'm management...? No I'm not, {i}am I{/i}?"
    "First I was hearing of it. In fact, I had just been considering myself a gopher."
    scene w1_1086 with dissolve
    jacob "Yep, you're management alright. Hell, you're the establishment even, at least where she stands."
    scene w1_1085 with dissolve
    jacob "If you told her to jump, she'd have to jump, else you could bring the heat down on her. Even if he doesn't look like it, bossman is a strict disciplinarian like that."
    scene w1_1084 with dissolve
    mc "You talking about Mr. Byrnes or...?"
    scene w1_1086 with dissolve
    jacob "Mr. Byrnes mainly, he handles that stuff. Dr. Kohler is more hands off, but you especially don't want to cross....eh."
    scene w1_1087 with dissolve
    "Jacob stopped himself mid-sentence, probably remembering my close connection to Dr. Chuck."
    scene w1_1086 with dissolve
    jacob "Anyway, what I'm saying... cut Harps a break if she's a little standoffish. As far as she's concerned, you're on the opposite side of the fence."
    scene w1_1084 with dissolve
    mc "Ah, shit. That makes sense, but I wish it didn't."
    scene w1_1088 with dissolve
    jacob "Hey, for what it's worth, you're alright with me - just as long you keep the girls safe."
    scene w1_1084 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Thank Jacob":
            show screen textbox2 with dissolve
            mc "Thanks, Jacob."

        "Tell him he doesn't need to worry about that. [gr]\[Jacob +1\]":
            $ Jacob_Friendship +=1
            show screen textbox2 with dissolve
            mc "You don't have to even mention that last part, I don't think I could rationalize doing this job otherwise."
            scene w1_1089 with dissolve
            mc "I'll do everything I can to keep the girl's safe and healthy."
            scene w1_1090 with dissolve
            jacob "Great, we understand each other! I'm the same way."
            scene w1_1085 with dissolve
            jacob "That's something I learned about myself in the military, I guess. I can only stomach so much dirty business if I feel like I'm doing some good, somehow, somewhere at least."


    scene w1_1091 with dissolve
    $ history_jacob = "It seems like my hunch of Jacob being a decent guy was correct. We shared a brief conversation at Hana's show."
    $ unread_jacob = True
    $ history_harper = "A conversation with Jacob revealed why Harper seemed so standoffish at the club. Apparently, she regards me as management, which is news to me. Jacob did his best to vouch for me."
    $ unread_harper = True
    play sound "sound effects/notification.wav"
    show bioupdate with dissolve
    harp "Oh hey, look. Look like they're on."
    "As Harper reappeared, it seems the band was taking the stage."
    scene w1_1068 with dissolve
    "I counted three people. There was Hana, a woman with vibrant pink hair, and a funny looking man in an eye-catching red jacket."
    scene w1_1092 with dissolve
    stop music fadeout 3.0
    harp "Let's get out there and show our support. Looks like they could use it..."
    mc "Agreed."
    jump w1HanaDatePerformance


label w1HanaDatePerformance:
    scene w1_1093 with curtains
    phg "Hi, fuck you. We're going to play some music now."
    hide screen textbox2 with dissolve
    play music "music/pure-energy-9.mp3"
    scene w1_1094 with snake
    pause
    scene w1_1095 with snake2
    pause
    scene w1_1096 with snakes
    pause
    scene w1_1097 with goslow
    pause
    scene w1_1094 with w4
    pause
    scene w1_1095 with snake2
    pause
    scene w1_1098 with irisout
    pause
    scene w1_1098 with vpunch
    pause
    scene w1_1098 with vpunch
    pause
    scene w1_1098 with vpunch
    pause
    scene w1_1099 with w19
    pause
    scene w1_1099 with vpunch
    pause
    scene w1_1099 with vpunch
    pause
    scene w1_1099 with vpunch
    pause
    scene w1_1099 with vpunch
    pause
    scene w1_1098 with vpunch
    pause
    scene w1_1098 with vpunch
    pause
    scene w1_1099 with vpunch
    stop music fadeout 4.0
    $ renpy.pause(4.0, hard=True)
    play sound "sound effects/applause-small.wav"
    scene w1_1100 with fade
    show screen textbox2 with dissolve
    "I half-expected them to collapse on the spot once the last song concluded - Hana and her two bandmates were wholly coated in a thick sheen of sweat, a veneer of physical anguish written plainly on their faces."
    "The band hadn't stopped for even a few seconds in between each song. After the first song was over, they immediately went into their next, not even stopping once their set had fully concluded, going on to do an encore that no one had asked for."
    "The whole thing felt like one large arrangement, rather than a musical set that could be broken down into distinct, individual pieces."
    scene w1_1101 with dissolve
    jacob "Haha, way to go guys!"
    "Jacob let out an overwhelming hurrah following the end of their performance, bringing his large hands together in a thunderous applause that eclipsed Harper and mine's pitiful attempt."
    phg "Thanks, we're {i}Eros Massacre{/i}. Don't tell your friends."
    scene w1_1102 with dissolve
    hana "Woohoo!"
    "With what could be characterized as a victory cry punctuating a hard-fought battle, Hana let out a howl before darting off the stage in a flash in front of her adoring fans."
    "That is, all three of them: Me, Jacob, and Harper."
    scene w1_1103 with dissolve
    play music "music/take-the-lead.mp3"
    hana "Ha! To be honest, I half-expected you guys not to show."
    scene w1_1104 with dissolve
    harp "You guys are great! Just my kind of energy."
    scene w1_1105 with dissolve
    jacob "It was, uh... something else alright. Right, [mcf]?"
    scene w1_1106 with dissolve
    hide screen textbox2 with dissolve
    menu:
        "Agree with Jacob.":
            scene w1_1107 with dissolve
            show screen textbox2 with dissolve
            mc "Yeah, what he said. I've never seen anything quite like that."
            scene w1_1109 with dissolve
            hana "Hell, I'll take that as a compliment. "

        "Tell Hana they kick ass. [gr]\[Hana +1\]":
            $ Hana_Affection +=1
            scene w1_1108 with dissolve
            show screen textbox2 with dissolve
            mc "You guys {i}really{/i} kicked ass up there."
            mc "I mean, musicality aside, you guys looked like demons. I don't know how you have that much stamina."
            scene w1_1110 with dissolve
            hana "Hehe, that's right. I'm amazing, right? Yeah, yeah... I'm amazing."
            "Despite Hana's normally cool demeanor, she clearly enjoys being praised."

    scene w1_1111 with dissolve
    phg "Hana! Who's the nerd, hunk, and old lady?"
    harp "{i}Old{/i} lady...?! Listen here...!"
    scene w1_1112 with dissolve
    flp "Yeah... when you said you were inviting some friends, I didn't expect a.."
    scene w1_1113 with dissolve
    jacob "Motley crew?"
    scene w1_1114 with dissolve
    flp "Yeah... that's what I was going to say."
    flp "You're not a cop, right? You look like a cop..."
    scene w1_1115 with dissolve
    phg "Of course he's not, look at these arms. He's too big to be a cop..."
    phg "When was the last time you saw a MHPD pig that didn't look like a pig?"
    scene w1_1116 with dissolve
    hana "Jeez, will you two shut the fuck up and let me introduce you? Shit."
    hana "These guys are from work."
    scene w1_1117 with dissolve
    hana "[mcf]."
    scene w1_1118 with dissolve
    hana "That's Jacob."
    scene w1_1119 with dissolve
    hana "She's Harper, she's a bad bitch that'll kick your teeth out. FYI, Jerrica."
    scene w1_1120 with dissolve
    hana "This is Jerrica and Spider."
    scene w1_1121 with dissolve
    spid "Yo!"
    scene w1_1122 with dissolve
    jer "Co-workers, eh? Since when do you have a fucking job, Hana?"
    scene w1_1123 with dissolve
    hana "Some of us don't live in a van and mooch off friends, Jer."
    scene w1_1124 with dissolve
    mc "Uh... nice to meet you guys."
    "I decided to interject, before things got more noisy."
    scene w1_1125 with dissolve
    jacob "Likewise. Any friend of Hana is cool with me."
    scene w1_1126 with dissolve
    jer "Think we could be friends, big guy?"
    scene w1_1127 with dissolve
    spid "I'm standing right here! You know, me, your boyfriend?"
    if jacobHarpVouch == True:
        scene w1_1128 with dissolve
        harp "*Whisper* Somehow, Hana's the least lively one of the band..."
        "Harper leaned in and whispered in my ear, sharing in an observation I was independently making myself."

    scene w1_1129 with dissolve
    hana "I'm glad you three came. Seriously, thanks. Jerrica may enjoy playing to near empty crowds--"
    scene w1_1130 with dissolve
    jer "It's called being an artist!"
    scene w1_1131 with dissolve
    hana "--but I like a little feedback, good or bad, y'know?"
    mct "(Not just the three of us...)"
    scene w1_1132 with dissolve

    if jacobHarpVouch == True:
        $ history_august = "To my surprise, I ran into the old man at Hana's show, but didn't get a chance to speak to him. Strangely, he slipped out before the show ended without even saying a word to Hana."
        $ unread_august = True
        play sound "sound effects/notification.wav"
        show bioupdate with dissolve
        "I quickly looked around in search of August, only to find him vanished. Wonder why he didn't stick around...?"
    else:
        "I quickly looked around in search of August, only to find him vanished, just like he said he would."

    scene w1_1133 with dissolve
    mc "Well, we're co-workers, right? We should get along."
    scene w1_1134 with dissolve
    spid "Right! Right! Let's all get along and have a drink, eh?"
    scene w1_1135 with dissolve
    hana "Here? No way am I paying $7 for what's basically a mug of water. I do know another place, though..."
    hana "Plenty of top shelf stuff, all for the price of free... plus, it's got a private pool."
    scene w1_1136 with dissolve
    jacob "Uh, I don't think that's a good idea, Hana. Your--"
    harp "Yeah, August isn't going to be happy if you bring in outsiders to the building."
    scene w1_1137 with dissolve
    hana "What the old man doesn't know won't hurt him, and if he does find out... {b}fuck him{/b}. Not like that sad sack has it in him to fire me, anyway."
    scene w1_1138 with dissolve
    jer "I think I'm a bit lost here, but you mentioned something about endless booze?"
    stop music fadeout 3.0
    if jacobHarpVouch == False:
        $ history_jacob = "Jacob was at Hana's show, but we didn't get a chance to talk one-on-one."
        $ unread_jacob = True
        $ history_harper = "Harper was at Hana's show, but she remains conspicuously tight-lipped."
        $ unread_harper = True
        play sound "sound effects/notification.wav"
        show bioupdate with dissolve
    "......"
    scene black with fade
    "..."
    scene w1_1139 with blinds
    play music "music/sneaky-snitch.mp3"
    spid "Yo, this place is creepy. What was with all those empty cubicles?"
    hana "It used to be an office building. Don't ask me why it's still that way, I just serve drinks here occasionally."
    scene w1_1140 with dissolve
    jer "Seriously though, you'd never know this place was here. What kind of bar is hidden from the world?"
    scene w1_1141 with dissolve
    hana "The exclusive, fuddy duddy 'you-must-oppress-the-poor' to drink here kind of bar?"
    scene w1_1142 with dissolve
    spid "Hehe, so what you're telling me is, we're redistributing the wealth by stealing the booze here?"
    "Following Hana's extremely bad suggestion, both Jacob and Harper bailed on us."
    scene w1_1143 with fade
    "Jacob's excuse was that it was past his bed time, and Harper understandably had no desire to spend her free time here."
    "I would've bailed myself, but Jacob privately suggested I tag along and made sure Hana didn't spill the beans, damage the place, or just otherwise get in trouble."
    scene w1_1144 with dissolve
    jer "Shit, this place is seriously swanky. How the hell did YOU get a job at a place like this?"
    scene w1_1145 with dissolve
    hana "The owner is a family friend."
    scene w1_1144 with dissolve
    mct "(...is that true, I wonder? Is that why she works here, despite acting like she hates the place?)"
    scene w1_1146 with dissolve
    jer "Bullshit. Since when does your mom have friends?"
    scene w1_1147 with dissolve
    spid "Hey buddy, you don't say much, do you?"
    scene w1_1148 with dissolve
    mc "You guys are doing enough talking for all of us."
    scene w1_1147 with dissolve
    spid "Ah, the strong and silent type? I dig it, I dig it."
    scene w1_1148 with dissolve
    mc "Not really..."
    scene w1_1149 with dissolve
    spid "So... Hana, yeah?"
    scene w1_1150 with dissolve
    spid "Coming to see us play, tagging along... you're trying to hit that, am I right?"
    mct "(...is he seriously asking me that?)"
    scene w1_1151 with dissolve
    hana "Of course he is. Who the fuck wouldn't? At least he's not creepy about it though."
    hana "Unlike you, you jackass."
    scene w1_1152 with dissolve
    hana "--catch!"
    "With next to no warning, Hana abruptly tossed a bottle of rum my way."
    scene w1_1153 with dissolve
    mc "...eh, wha--?"
    "As I watched the bottle arc through the air, panic set in as I envisioned the bottle smashing violently into the bar room's floor..."
    scene w1_1154 with dissolve
    hana "Nice catch, [mcf]."
    scene w1_1155 with dissolve
    mc "--gh, what if I dropped that?"
    scene w1_1156 with dissolve
    hana "There's about four more bottles. I'm sure you would've caught at least one of them."
    scene w1_1155 with dissolve
    mc "What about the mess? August would know that we snuck in..."
    scene w1_1157 with dissolve
    hana "Oh, you don't have to worry about that. He'll know. You think this place doesn't have cameras? That paranoid bastard checks 'em every morning too."
    scene w1_1158 with dissolve
    mc "..."
    "Somehow, in my infinite capacity for being a stick in the mud and a habitual worry-wart, that obvious fact had snuck into my blind spot."
    scene w1_1159 with dissolve
    jer "Huh, wait, for real? You're not going to get in trouble for this, are you?"
    scene w1_1160 with dissolve
    hana "Naaaaaah, probably not."
    hana "Anyway, now that we're fully loaded, let's get wet."
    mc "What do you mean by..."
    stop music
    play sound "sound effects/water-splash.wav"
    scene w1_1161 with wet2
    "*Kachunk*"
    scene w1_1162 with dissolve
    mct "(Okay, this is borderline ridiculous.)"
    mct "(So the club has a bar, sauna, multiple baths, photography studio, gym, multiple private rooms, private offices, an underground sex hall... and now also giant-sized indoor pool?)"
    scene w1_1163 with dissolve
    mct "(Whatever.)"
    scene w1_1164 with dissolve
    play music "music/happy-whistling-ukulele.mp3"
    "After snatching some alcohol from the bar - and then availing ourselves of the club's selection of swim suits - we found our way here."
    "The club itself, I learned, has a veritable warehouse worth of costumes, clothes, underwear, and swimming garments."
    scene w1_1165 with dissolve
    spid "Eh? You're not getting in?"
    scene w1_1166 with dissolve
    mc "I will, in a bit."
    scene w1_1167 with dissolve
    mc "..."
    scene w1_1168 with dissolve
    mc "*Glug, glug, glug."
    "The rum, surprisingly, had a refreshing effect. It's sweet, tannin-enriched flavor smoothly slid down my gullet with next to no resistance from my taste buds."
    scene w1_1167 with dissolve
    mct "(Well, I'm already in the midst of a poor choice. Might as well revel in it.)"
    scene w1_1169 with dissolve
    mc "So... why Spider?"
    scene w1_1170 with dissolve
    spid "What do you mean {i}why{/i} Spider?"
    scene w1_1171 with dissolve
    mc "I mean, why are you called that. You got a tattoo of a Spider or something?"
    scene w1_1170 with dissolve
    spid "I just thought it sounded cool."
    scene w1_1171 with dissolve
    mc "Wait... you mean you gave yourself a nickname? Not only that, but it was... {i}spider{/i}?"
    scene w1_1172 with dissolve
    spid "Yeah, what's wrong with that?!"
    scene w1_1170 with dissolve
    mc "It's just... {w}it's just..."
    scene w1_1173 with dissolve
    mc "--pfthahaha."
    scene w1_1174 with dissolve
    mc "Hahahahahahaha--"
    scene w1_1175 with dissolve
    mc "HAHAHAHAHAHAHA! Oh, no. That's..."
    scene w1_1176 with dissolve
    mc "Sorry. Sorry... that's just too fucking funny."
    spid "Yeah?! What's so damn funnny about it?!"
    scene w1_1177 with dissolve
    mc "Well, it's just... you know..."
    if toughness <= 17:
        mct "(Shit, I'm kind of being a jerk here, huh? I probably shouldn't say it...)"
    hana "I know, right? It's like something a kid do."
    scene w1_1178 with dissolve
    mc "Ehehe...heh..."
    "Hana had rejoined us, putting my exact thoughts about the punk rocker's self-given nom de plume into words."
    spid "*Whistle* Fhweeeeeeeeeooooo!"
    scene w1_1179 :
        subpixel True
        yalign 1.0
        xalign 0.6
        linear 6 yalign 0.1
    "I was in total agreement with my wolf-whistling Spider friend, doing my own silent cat-calling inside my head."
    "The cut of the girls' swimsuits were {i}extremely{/i} revealing, but both wore it boldly; full at ease wearing it as if it was only a church-Sunday smock."
    scene w1_1181 with dissolve
    jer "Well...?"
    hana "Yeah, yeah... get it out of your system."
    scene w1_1180 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Don't say anything, just whistle.":
            show screen textbox2 with dissolve
            "Rather than say anything, I took a cue from my male counterpart."
            mc "*Whistle* Cwhoooooeeeooooo!"
            scene w1_1182 with dissolve
            hana "One Spider is more than enough, thanks."
            scene w1_1183 with dissolve
            mc "*Glug, glug, glug*."
            scene w1_1184 with dissolve
            hana "Fwhaa! That's the stuff."
            scene w1_1191 with dissolve

        "Admire Hana's tattoos. [gr]\[Hana +1\]":
            $ Hana_Affection += 1
            scene w1_1185 with dissolve
            show screen textbox2 with dissolve
            mc "Your tattoos look amazing."
            "Not that I hadn't gotten a good look at them already, but seeing them almost entirely in the buff on one big canvas gave me a finer appreciation for their beautiful detail."
            scene w1_1186 with dissolve
            hana "Oh ho, is that what's got your eyes?"
            scene w1_1187 with dissolve
            mc "Not the only thing, but it's the one that's polite to mention."
            scene w1_1188 with dissolve
            hana "You ever think about getting inked?"
            scene w1_1189 with dissolve
            mc "No, never."
            scene w1_1190 with dissolve
            hana "You should consider it. Skinny men with tattoos is sexual catnip. You'd pull a lot more tail."
            scene w1_1189 with dissolve
            mc "Thanks for the tip, but I'm not that kind of guy."
            scene w1_1190 with dissolve
            hana "You mean the kind that's looking to to get laid?"
            scene w1_1192 with dissolve

    stop music fadeout 3.0
    jer "Woo!"
    play sound "sound effects/water-splash.wav"
    scene w1_1193 with dissolve
    "*Kachunk*"
    scene w1_1194 with dissolve
    "..."
    scene w1_1195 with dissolve
    jer "Mnhaaa~! The water's great!"
    scene w1_1196 with dissolve
    jer "{b}This{/b} is exactly what's needed after a gig. Get your asses in here!"
    scene w1_1197 with dissolve
    hana "Good idea!"
    scene w1_1198 with dissolve
    hana "Well...?"
    scene w1_1199 with dissolve
    mc "Ladies first."
    scene w1_1200 with dissolve
    hana "Don't dawdle, new guy or I'll tell August this was your idea."
    mct "(Ehehe... please don't do that.)"
    scene w1_1201 with dissolve
    "Shooting me one last conspiratorial look, Hana moved to the edge of the water's surface, held her nose, and..."
    play sound "sound effects/water-splash.wav"
    scene w1_1202 with dissolve
    "*Fwphoo*"
    "Took the plunge."
    scene w1_1203 with dissolve
    "I wasn't far behind, following her example."
    scene black with wet2
    play sound "sound effects/water-splash.wav"
    "*Kachunk*"
    "..."
    scene w1_1204 with circlewipe
    play music "music/hotshot.mp3"
    "Over the next half hour or so, we messed around."
    scene w1_1205 with fade
    "We drank."
    play sound "sound effects/water-splash.wav"
    scene w1_1206 with wet2
    "Fucked around."
    scene w1_1207 with fade
    "Drank some more..."
    scene w1_1208 with wiperight
    "Had some friendly competition."
    scene w1_1209 with fade
    "Drank {b}EVEN{/b} more, to the point of belligerence."
    scene w1_1210 with w19
    "Which turned into some not-so-friendly competition."
    jer "Put yer goddamn back into it!"
    hana "C'mon, c'mon, c'mon...!"

    if perk_strongman == True:
        $ Hana_Affection += 1
        scene w1_1211 with curtains
        hana "Wahahaha! Suck it, losers! You better pay up, Jer."
        jer "Grr....!"
    else:

        scene w1_1212 with curtains
        jer "Yes, yes, yes! You owe me twenty bucks, Hana!"
        hana "Mmmhg....!"

    scene w1_1213 with circlewipe
    "Until we found ourselves divided into groups, thanks to an overly amorous development."
    jer "Hehehe, never done it in a fancy pool before."
    spid "Fuck...! You look so good in that swimsuit...!"
    scene w1_1214 with dissolve
    hana "Bah! Those two are fucking animals. I always end up the third wheel."
    hana "Thankfully, that's not the case tonight, though this is still slightly awkward in its own way."
    scene w1_1215 with dissolve
    mc "Pretty sure this won't be the first time someone's screwed in this pool."
    scene w1_1216 with dissolve
    hana "Don't get any fresh ideas. I'm starting to like you, but I'm not entirely sold on you just yet."
    scene w1_1217 with dissolve

    if perk_socialButterfly == True or perk_socialChameleon == True:
        mc "Don't worry, I can read the room. Let's just talk."
    else:
        mc "That's alright with me. Let's just talk a bit."

    mc "Let me get a chance to fully sell myself."
    scene w1_1218 with dissolve
    hana "Fair enough, new guy. Why don't you start?"
    scene w1_1219 with dissolve
    stop music fadeout 3.0
    mc "Hmmm, well..."
    hide screen textbox2 with dissolve
    scene w1_1226 with dissolve

    menu:
        "Talk about Hana's band.":
            $ w1HanaBandPath = True
            jump w1HanaTalkBand
        "Talk about Hana's motorcycle. [gr]\[Hana +1\]":
            $ w1HanaBikePath = True
            $ Hana_Affection +=1
            jump w1HanaTalkBike


label w1HanaTalkBand:

    play music "music/horrible.mp3"
    show screen textbox2 with dissolve
    mc "So... how did you all meet?"
    "I decided to go with the most obvious, at-hand line of conversation."
    scene w1_1221 with dissolve
    hana "Jerrica and Spider? I've known them since we were all kids. We grew up in the same building, and even went to the same school."
    mc "Childhood friends, then?"
    hana "Not exactly. Jerrica and I were friends for about all that time, but we didn't really start hanging with Eric -- sorry, {b}Spider{/b} - until high school, when we put up a notice looking for a bassist."
    hana "He turned up, was cool enough. There was a small hitch, though: he had never even picked up a single musical instrument in his life."
    scene w1_1226 with dissolve
    mc "You guys let him join your band despite that?"
    scene w1_1225 with dissolve
    hana "Had to, Jerrica immediately had a crush on him. Plus, not like her or I were much more than beginners at that point anyway."
    scene w1_1226 with dissolve
    mc "It makes for a pretty good story I guess."
    scene w1_1223 with dissolve
    hana "Yeah, that's a little {i}Behind the Music: Eros Massacre{/i} for ya."
    scene w1_1226 with dissolve
    "The conversation came to a natural pause, sending my mind in different directions and causing me to..."
    hide screen textbox2 with dissolve
    menu:
        "Ask about band dynamics.":
            jump w1HanaTalkBand2

        "Zero in on the band name. [gr]\[Hana +1\]":
            $ Hana_Affection +=1
            jump w1HanaTalkMovies

label w1HanaTalkBand2:
    show screen textbox2 with dissolve
    mc "What's it like being in a band with your friends? I imagine that has it own unique frustrations."
    scene w1_1227 with dissolve
    hana "Eh, you would think, but nooooot really. Jerrica and Spider are both pretty chill, but none of us are afraid to speak our minds."
    scene w1_1228 with dissolve
    mc "Really? There's no friction at all?"
    scene w1_1227 with dissolve
    hana "Sure there is, but whenever Jerrica gets on my nerves with her fucking loud-ass chewing or Spider goes off {i}off script{/i} in his playing, I let them know how annoyed or pissed off I am."
    scene w1_1222 with dissolve
    hana "They do the same for me. Keeps things from ever boiling over. It's liberating, airing your shit. It works as long as no one takes things too personally."
    scene w1_1226 with dissolve
    mc "Sounds like you've got it figured out."
    scene w1_1225 with dissolve
    hana "Hmmm, maybe. It's not like it's the secret to world peace or anything, but it works for us. I'm not naive enough to suggest it would work everywhere."
    scene w1_1259 with dissolve
    hana "Try telling Kathleen she's acting {i}real{/i} cuntish next time she goes full depraved bitch mode, for example. That wouldn't go over as smooth as it would with Jer. Not everyone is as awesome as she is."
    scene w1_1226 with dissolve
    mc "So, you and her are like best friends then?"
    scene w1_1223 with dissolve
    hana "If you want to put a label on it. I don't."
    scene w1_1229 with dissolve
    hana "What about you and Ian, eh? You guys are tight, right?"
    scene w1_1231 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Tell Hana you are. [gr]\[Killian +1\]":
            $ Killian_Bromance +=1
            show screen textbox2 with dissolve
            mc "Yeah, we are. Hope you won't hold that against me."
            scene w1_1230 with dissolve
            hana "I'll reserve my judgement. Your friend's a mega-asshole, but you haven't sent up any red flags yet."
            scene w1_1252 with dissolve
            mc "Gee, thanks. How gracious of you, oh magnanimous one."
            scene w1_1253 with dissolve
            hana "Hehe, I totally agree."
            scene w1_1254 with dissolve
            mc "At any rate, even if we weren't, I'd have to be now. He landed me the job here at the club after all."

        "Tell Hana your relationship with Ian is complicated. [gr]\[Hana +1\]":
            $ Hana_Affection += 1
            show screen textbox2 with dissolve
            mc "It's complicated. We go way back, y'know? Kinda hard to shake him, even if I wanted to. You can't choose your friends."
            scene w1_1230 with dissolve
            hana "Huh? What? The saying is... {i}you can't choose your family, but you {b}can{/b} choose your friends.{/i}."
            scene w1_1231 with dissolve
            mc "Yeah, I know. I guess what I'm saying is, it just {b}feels{/b} that way sometimes. Especially now, after I owe him for landing me the job here at the club."

    scene w1_1230 with dissolve
    hana "Is this shitty place really such a big deal for you?"
    scene w1_1232 with dissolve
    mc "..."
    scene w1_1233 with dissolve
    mc "Yes. It's going to pay for my school. What about you? Why are you here?"
    scene w1_1250 with dissolve
    hana "Ah, well..."
    scene w1_1223 with dissolve
    hana "We're in a similar boat. Leave it at that."
    scene w1_1226 with dissolve
    "Even if she says that, she still has me curious..."
    hide screen textbox2 with dissolve

    menu:
        "Pry into Hana's situation. [red]\[Hana -2\]":
            $ Hana_Affection -= 2
            jump w1HanaTalkPry

        "Leave it alone. Have some fun in the pool. [gr]\[Hana +1\]":
            $ Hana_Affection += 1
            jump w1HanaTalkFun



label w1HanaTalkPry:

    scene w1_1237 with dissolve
    show screen textbox2 with dissolve
    mc "Come on, now you've got me curious."
    scene w1_1259 with dissolve
    hana "I don't want to talk about it."
    scene w1_1237 with dissolve
    mc "Whatever it is, you--"
    scene w1_1238 with dissolve
    hana "I said... {size=+20}I DON'T WANT TO TALK ABOUT IT.{/size=+20}. Cork it!"
    scene w1_1239 with dissolve
    mc "..."
    scene w1_1240 with dissolve
    "Things got more than a little awkward between us, as a result of me putting my foot in my mouth."
    "That wasn't the worse of it though, as..."
    jump w1HanaDateInterrupt

label w1HanaTalkFun:

    show screen textbox2 with dissolve
    "Enough blathering! Having reached the end of the converstaional thread, there was only one thing for me to do..."
    play sound "sound effects/water-splash.wav"
    scene w1_1245 with dissolve
    "*Kachunk*"
    hana "...huh?"
    scene w1_1246 with dissolve
    hana "What are you do--"
    scene w1_1247 with dissolve
    hana "Eeeeh?!"
    "Even from underwater, I could pick up the uncharacteristically cute, shrill cry that escaped Hana's lips."
    scene black with fade
    play sound "sound effects/water-splash.wav"
    "After my sneak attack, we splashed around in the water like children, so preoccupied that we didn't hear our reckoning sneak up on us."
    hana "Ah, crap."
    $ w1HanaTalkPlay = True
    jump w1HanaDateInterrupt

label w1HanaTalkMovies:

    show screen textbox2 with dissolve
    mc "Eros Massacre...?"
    "Right, the name had struck me as familiar back at the Asp Hole, but I was so focused on my surroundings that I didn't immediately connect it."
    mc "You named your band after a movie?"
    scene w1_1241 with dissolve
    hana "Huh...?!"
    scene w1_1242 with dissolve
    hana "You actually know it?!"
    scene w1_1243 with dissolve
    mc "Surprisingly, yeah."
    "Eros + Massacre was the name of a Japanese film from the late 60s. It is {i}very{/i} long, and not exactly my cup of tea, but I had seen it in my teenage years during my mother's cinematic schooling."
    scene w1_1242 with dissolve
    hana "That's awesome! You're the first person to get that."
    scene w1_1243 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Talk about your mother. [gr]\[Hana +1\]":
            $ Hana_Affection +=1
            show screen textbox2 with dissolve
            mc "It's all thanks to my mother."
            scene w1_1249 with dissolve
            hana "Your mother?"
            jump w1HanaTalkMother
        "Talk about movies.":
            jump w1HanaTalkMovies2

label w1HanaTalkMother:

    $ w1HanaSingleMother = True
    scene w1_1248 with dissolve
    show screen textbox2 with dissolve
    mc "Yep, she's responsible for all the weird shit I watched growing up."
    scene w1_1249 with dissolve
    hana "Sounds like a cool lady."
    scene w1_1248 with dissolve
    mc "She is, for a lot of reasons. She kicks a lot of ass. Actually, she reminds me a little of you."
    scene w1_1244 with dissolve
    mc "She does?"
    scene w1_1248 with dissolve
    mc "Well, she doesn't dress like you, talk like you, and she isn't as scary as you... but she doesn't let anything stand in her way."
    scene w1_1227 with dissolve
    hana "Gotta say, this is the first time a boy's brought up his own mother so emphatically while on a not-date with me."
    scene w1_1228 with dissolve
    mc "Heh, is that weird?"
    scene w1_1227 with dissolve
    hana "A little, but it's also kinda sweet. I can tell by the sound of your voice and the look on your face that you care about her."
    scene w1_1224 with dissolve
    hana "I'm a little jealous, to be honest."
    scene w1_1220 with dissolve
    mc "Of what?"
    scene w1_1225 with dissolve
    hana "Of that kind of parental relationship. Don't get me wrong, I'd scratch someone's fucking eyes out if they hurt my mom, but..."
    scene w1_1226 with dissolve
    mc "...but?"
    scene w1_1223 with dissolve
    hana "Ah, I got a lot of baggage there. I'm not going to get into it. You wouldn't want to hear it. "
    scene w1_1231 with dissolve
    mc "I might!"
    scene w1_1230 with dissolve
    hana "No, you don't. I want to hear about your mom, though. Tell me about her. What's she like?"
    scene w1_1231 with dissolve
    mc "She's... very patient, but also impatient at the same time."
    scene w1_1253 with dissolve
    hana "How's that?"
    scene w1_1252 with dissolve
    mc "For example: she always opens the microwave with a few seconds to go, but she'll cheerfully stand idly by while her old neighbor goes on and on about the rising price of newspapers."
    scene w1_1254 with dissolve
    mc "That's not to mention the patience she had with me and my bad behavior growing up."
    scene w1_1230 with dissolve
    hana "Your dad's out of the picture?"
    scene w1_1231 with dissolve
    mc "Yeah, she raised me herself."
    scene w1_1230 with dissolve
    hana "Same, it was just me and my mom too. Though, in my case, it was better that way."
    scene w1_1231 with dissolve
    mc "Why do you say that?"
    scene w1_1259 with dissolve
    hana "My dad's a {i}real{/i} piece of shit - that said, before it becomes awkward, keep going."
    scene w1_1226 with dissolve
    mc "Right, uh... well, there's a ton else I could say, but I'll just keep it to one."
    mc "She endured a lot of nasty shit for my sake, when she could've just split."
    scene w1_1250 with dissolve
    hana "You sound very lucky."
    scene w1_1251 with dissolve
    mc "Yeah, I guess--"
    scene w1_1250 with dissolve
    hana "Ah, crap."
    jump w1HanaDateInterrupt

label w1HanaTalkMovies2:

    show screen textbox2 with dissolve
    mc "When I'm not studying, I spend a lot of time watching movies I guess."
    scene w1_1224 with dissolve
    hana "That's cool. You're not the type to self-describe as a {i}cinephile{/i} are you?"
    scene w1_1252 with dissolve
    mc "No, no... I only {b}look{/b} obnoxious."
    scene w1_1253 with dissolve
    hana "Ha! You're a funny fucker aren't you, new guy?"
    scene w1_1254 with dissolve
    mc "It accidently happens from time to time."
    scene w1_1253 with dissolve
    hana "So, what kind of movies are you into?"
    scene w1_1236 with dissolve
    mc "Dumb action movies, mostly. The stupider the better."
    scene w1_1235 with dissolve
    hana "Kung fu?"
    scene w1_1236 with dissolve
    mc "Yeah, who doesn't like a little 36 Chambers of Shaolin?"
    scene w1_1235 with dissolve
    hana "What else?"
    scene w1_1236 with dissolve
    mc "I grew up watching a lot of world cinema too. Giallo horror, giant monster movies, yakuza flicks."
    mc "To be honest, Ian and I watched things we were definitely not old enough to view, let alone appreciate."
    scene w1_1229 with dissolve
    hana "You guys go that way back? You must be pretty tight then."
    scene w1_1226 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Tell Hana you are. [gr]\[Killian +1\]":
            $ Killian_Bromance +=1
            show screen textbox2 with dissolve
            mc "Yeah, we are. Hope you won't hold that against me."
            scene w1_1225 with dissolve
            hana "I'll reserve my judgement. Your friend's a mega-asshole, but you haven't sent up any red flags yet."
            scene w1_1220 with dissolve
            mc "Gee, thanks. How gracious of you, oh magnanimous one."
            scene w1_1224 with dissolve
            hana "Hehe, I totally agree."
            scene w1_1226 with dissolve
            mc "At any rate, even we weren't, I'd have to be now. He landed me the job here at the club after all."

        "Tell Hana your relationship with Ian is complicated. [gr]\[Hana +1\]":
            $ Hana_Affection += 1
            show screen textbox2 with dissolve
            mc "It's complicated. We go way back, y'know? Kinda hard to shake him, even if I wanted to. You can't choose your friends."
            scene w1_1223 with dissolve
            hana "Huh? What? The saying is... {i}you can't choose your family, but you {b}can{/b} choose your friends.{/i}."
            scene w1_1226 with dissolve
            mc "Yeah, I know. I guess what I'm saying is, it just {b}feels{/b} that way sometimes. Especially now, after I owe him for landing me the job here at the club."

    scene w1_1222 with dissolve
    hana "You know, I think I get you."

    if w1HanaBandPath == True:
        scene w1_1250 with dissolve
        hana "Ah, crap."
        jump w1HanaDateInterrupt

    if w1HanaBikePath == True:
        scene w1_1226 with dissolve
        mc "What about you? What kind of movies do you like?"
        scene w1_1223 with dissolve
        hana "What makes you think I like movies?"
        scene w1_1226 with dissolve
        mc "Everyone likes movies."
        scene w1_1223 with dissolve
        hana "No they don't, but..."
        scene w1_1255 with dissolve
        hana "This gal sure as shit does."
        hana "The weirder the better."
        scene w1_1220 with dissolve
        hide screen textbox2 with dissolve

        menu:
            "Tell her it sounds like she has the same taste as your mother. [gr]\[Hana +1\]":
                $ Hana_Affection +=1
                show screen textbox2 with dissolve
                mc "Sound like you have similar tastes to my mother."
                scene w1_1244 with dissolve
                hana "Your mother?"
                jump w1HanaTalkMother

            "Continue the movie talk.":
                jump w1HanaTalkMovies3


label w1HanaTalkBike:

    play music "music/horrible.mp3"
    scene w1_1241 with dissolve
    show screen textbox2 with dissolve
    mc "How long have you and Suzie Q been a couple?"
    scene w1_1242 with dissolve
    hana "--! You actually remembered my baby's name?"
    scene w1_1256 with dissolve
    hana "Ah, let's see... We've been together a little over two years ago. I bought her as a present for myself for my 21st birthday."
    hana "First expensive thing I've ever owned. I always wanted a motorcycle, ever since I was a little girl. I was weird like that I guess."
    scene w1_1257 with dissolve
    "Hana's eyes were practically sparkling at this point. I clearly touched on a favorite topic of hers."
    mc "That's not so weird. Bikes are badass, right?"
    scene w1_1249 with dissolve
    hana "You bet your ass they are."
    scene w1_1256 with dissolve
    hana "Anyway, I started putting money back for it from the part-time jobs I had in high school. I scrimped and saved for years, until finally...!"
    scene w1_1250 with dissolve
    hana "I know it's just a dumb inanimate object, but... it's one of the few things in my life that I'm proud of."
    scene w1_1258 with dissolve
    "Am I seeing things, or is Hana looking a little... {i}embarrassed{/i}?"
    mct "(It's a cute look on her.)"
    hide screen textbox2 with dissolve

    menu:
        "Share your observation.":
            show screen textbox2 with dissolve
            mc "Y'know... you're pretty cute when you're embarrassed."
            scene w1_1259 with dissolve
            hana "Cram it! Don't feed me that shitty line. It's patronizing."
            scene w1_1237 with dissolve
            mc "I'm not {i}feeding{/i} you a line, I'm just giving you my earnest thoughts."
            scene w1_1259 with dissolve
            hana "Well, your earnest thought is a trite pickup line."
            scene w1_1226 with dissolve
            mc "My bad. Sorry!"
            scene w1_1225 with dissolve
            hana "Ah, don't worry. I'm not too fussed about it. I just like giving you a hard time."


        "Admire her tenacity. [gr]\[Hana +1\]":
            $ Hana_Affection +=1
            show screen textbox2 with dissolve
            mc "It's not just an inanimate object, it's a symbol of your independence. You wanted something and you worked hard to get it. You should be proud."
            scene w1_1224 with dissolve
            hana "Heh, I suppose it sounds less frivolous your way. You're pretty good at spinning things, aren't you?"
            scene w1_1220 with dissolve
            mc "Eh, I wouldn't say that... I was just sharing my earnest thoughts."
            scene w1_1224 with dissolve
            hana "Well, thanks. It's cool hearing it put that way. That money could've been used for {b}other things{/b}, so I feel silly sometimes about it."

    scene w1_1229 with dissolve
    hana "Anyway... what about you? Hobbies?"
    scene w1_1226 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Tell Hana you pretty much just study. [gr]\[Hana +1\]":
            $ Hana_Affection +=1
            jump w1HanaTalkDoctor
        "Tell Hana you watch a lot of movies.":
            jump w1HanaTalkMovies2


label w1HanaTalkDoctor:

    scene w1_1231 with dissolve
    show screen textbox2 with dissolve
    if toughness >= 18:
        mc "Until recently, I mostly just used my time to study. Hell, even my old job was helping snobby brats hit the books."
    else:
        mc "Until recently, I mostly just used my time to study. Hell, even my old job was helping other people hit the books."

    scene w1_1230 with dissolve
    hana "What's all that studying for?"
    scene w1_1231 with dissolve
    mc "To get into med school."
    scene w1_1253 with dissolve
    hana "You're going to be a doctor?"
    scene w1_1252 with dissolve
    mc "Without a doubt."
    scene w1_1253 with dissolve
    hana "Yeesh, turn it down some, will ya? That kinda confidence is enough to give a girl butterflies."
    scene w1_1236 with dissolve
    mc "You're teasing me.... What about you? You gonna be a rockstar?"
    scene w1_1250 with dissolve
    hana "Fat chance. We fucking suck. We just do this for fun."
    scene w1_1225 with dissolve
    hana "Well, not Jerrica. That crazy bitch thinks there's an artistry to us wailing and jumping around."
    scene w1_1226 with dissolve
    mc "Then what do you picture your future like?"
    scene w1_1223 with dissolve
    hana "Fuck if I know, dude. I don't really think about it too much."
    scene w1_1226 with dissolve
    mc "Really? I can't image... how does that not stress you out? I'd be on the floor with anxiety."
    scene w1_1222 with dissolve
    hana "Guess I'm not built that way. Still, even if I did have a dream career..."
    scene w1_1251 with dissolve
    "Hana trailed off, clearly thinking better of what she was about to say. She had me curious."
    mc "What?"
    scene w1_1223 with dissolve
    hana "Ah, forget it. I'm not in a sharing mood."
    scene w1_1226 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Insist that she tell you. [red]\[Hana -2\]":
            $ Hana_Affection -= 2
            jump w1HanaTalkPry

        "Let it go. Have some fun in the pool. [gr]\[Hana +1\]":
            $ Hana_Affection += 1
            jump w1HanaTalkFun



label w1HanaTalkMovies3:

    show screen textbox2 with dissolve
    mc "What's your favorite {i}weird{/i} movie then?"
    scene w1_1224 with dissolve
    hana "Easy! Have you ever seen {i}Testuo: The Iron Man{/i}?"
    scene w1_1220 with dissolve
    mc "I have. It's pretty good."
    scene w1_1244 with dissolve
    hana "Pretty good? Pretty good?! It's fucking awesome! It's like one big hypnotic metal fever dream!"
    scene w1_1249 with dissolve
    hana "What's not to like? From the trippy stop motion animation, to the high contrast black and white... it even has a giant metal drill penis! It's pure kino!"
    scene w1_1248 with dissolve
    mc "You're geeking out pretty hard right now, you know?"
    scene w1_1244 with dissolve
    hana "Yeah, what of it?"
    scene w1_1248 with dissolve
    "Well..."
    hide screen textbox2 with dissolve

    menu:
        "Tell her you like this side of her. [gr]\[Hana +1\]":
            $ Hana_Affection += 1
            show screen textbox2 with dissolve
            mc "I like it. It's a change of pace from how I picture you."
            scene w1_1227 with dissolve
            hana "How do you picture me, exactly?"
            scene w1_1228 with dissolve
            mc "Cool, motorcycle riding chick who doesn't take anyone's shit? Something like that?"
            scene w1_1227 with dissolve
            hana "I'll take it."
            scene w1_1220 with dissolve
            mc "Flattery aside--"

        "Joke with Hana about being lame.":
            show screen textbox2 with dissolve
            mc "It's just nice to know that beneath that unflappable badass exterior, is a giant geek."
            scene w1_1237 with dissolve
            mc "It's just nice to know that you can be lame too."
            scene w1_1229 with dissolve
            hana "Hey! You asked, alright?! Don't be a jerk."
            scene w1_1226 with dissolve
            mc "Teasing aside--"

    scene w1_1250 with dissolve
    hana "Ah, crap."
    jump w1HanaDateInterrupt

label w1HanaDateInterrupt:

    stop music
    play sound "sound effects/record-scratch.wav"
    scene w1_1260 with fade
    hana "The jigs up."
    scene w1_1261 with dissolve
    war "Oh, for fuck's sake."
    scene w1_1262 with dissolve
    hana "Hiya, Warren. How's things?"
    scene w1_1261 with dissolve
    war "I'd expect this from Mr. Beaufort, but you?"
    scene w1_1263 with dissolve
    war "Your father is going to blow a fucking gasket when he finds out about this."

    if w1HanaTalkPlay == True:
        scene w1_1264 with fade
        mc "......."
        mc "..."
        play sound "sound effects/surprise.wav"
        mct "(...huh?!)" with vpunch
        scene w1_1265 with dissolve
        mc "Uh, Hana..."
        scene w1_1266 with dissolve
        hana "Yeah, new guy?"
        scene w1_1265 with dissolve
        mc "Is... is Mr. Byrnes your {i}dad{/i}?"
        scene w1_1267 with dissolve
        hana "That fucker now likes to pretend he is."
        scene w1_1268 with dissolve
        mct "(Eh? EH?! Could NO ONE have freakin' mentioned this to me earlier?!)"

    else:
        scene w1_1269 with dissolve
        mc "......."
        mc "..."
        play sound "sound effects/surprise.wav"
        mct "(...huh?!)" with vpunch
        scene w1_1270 with dissolve
        mc "Uh, Hana..."
        scene w1_1271 with dissolve
        hana "Yeah, new guy?"
        scene w1_1270 with dissolve
        mc "Is... is Mr. Byrnes your {i}dad{/i}?"
        scene w1_1272 with dissolve
        hana "Fucker now like to pretend he is, at least."
        scene w1_1273 with dissolve
        mct "(Eh? EH?! Could NO ONE have freakin' mentioned this to me earlier?!)"

    scene black with w24
    play sound "sound effects/notification.wav"
    $ met_spider = True
    $ met_jerrica = True
    show bioadd with dissolve
    "..."
    scene w1_1274 with blinds
    play music "music/leaving-home.mp3"
    war "Seriously, what were you thinking, little Miss? I'll cut [mcf] a little slack since he's new, but you know the club's policy about outsiders VERY well."
    "After Warren's interruption, Spider and Jerrica were briskly sent packing. Hana and Spider made some fuss, but Jerrica was astute enough to pick up on how seriously scary Warren was about them leaving."
    scene w1_1275 with dissolve
    hana "First of all, drop the {i}little Miss{/i} bullshit, okay? Second of all..."
    scene w1_1276 with dissolve
    war "There's no second of all, Hana! This place represents a lot of money for dangerous people. You know the people who your father...auhg!"
    hana "...eh?"
    scene w1_1277 with hpunch
    war "THIS AIN'T NO FUCKIN' PLAYGROUND!"
    scene w1_1278 with dissolve
    "All at once, Warren exploded into a projection of pure rage, bearing down on Hana an unadulterated anger that had been pressure cooked."
    "At the molecular level, my body was telling me to be wary. That {b}this{/b} was a dangerous man. Something my mind already knew, but now my very body was in total agreement with."
    "The reaction carved into Hana's face told me she was feeling the same. Despite her usual gumption, she was still a woman facing down what was basically an angry man the size of a gorilla."
    scene w1_1279 with dissolve
    mc "...cooler heads prevail, yeah?"
    scene w1_1280 with dissolve
    stop music fadeout 3.0
    "Reflexively, I put myself between the beleaguered Hana and towering Warren, despite the self-preservation part of my brain telling me to stay the fuck out of it."
    war "..."
    scene w1_1281 with curtains
    play music "music/called-upon.mp3"
    kat "Mr. [mcl] is right."
    "I don't know how long Kathleen had been standing there, but she picked just the right time to cut the tension."
    scene w1_1282 with dissolve
    kat "You're scaring the poor girl, Warren."
    scene w1_1283 with dissolve
    hana "{size=-10}Not really.{/size=-10}"
    scene w1_1284 with dissolve
    kat "You can forgive a young lady her foibles I hope."
    scene w1_1285 with dissolve
    war "*sigh* If that's what you want, Mrs. P."
    scene w1_1286 with dissolve
    kat "It is. Not only that, but... August doesn't really have to know about this, does he?"
    "To my utter disbelief, instead of brow beating Hana, Kathleen had swooped in to diffuse the situation."
    scene w1_1287 with dissolve
    hana "Let him, I don't care if he--"
    scene w1_1288 with dissolve
    kat "I know you don't, dear. Honestly, I might be trying to accomplish the same thing if I was in your position."
    kat "No, that's not right. I would've already burned this place to the ground."
    scene w1_1289 with dissolve
    war "Don't give her any ideas."
    "I didn't understand what they were talking about, but the cold-blooded woman I called my boss was nowhere to be found, instead she had a caring and almost maternal affectation to her demeanor."
    scene w1_1290 with dissolve
    kat "A {b}year{/b} is a long time when there's no real end in sight, isn't it?"
    kat "I know you're angry, and you have every right to be, but you've got to find someway to ground yourself. Think of your {b}mother{/b}."
    scene w1_1291 with dissolve
    hana "..."
    "At the mention of Hana's mom, all color drained from the would be rockstar's face."
    "It was a pitiful look, resembling a deflated balloon."
    hana "You...! Don't...!"
    scene w1_1292 with dissolve
    hana "...!"
    scene w1_1293 with dissolve
    hana "Whatever."
    scene w1_1294 with dissolve
    stop music fadeout 3.0
    "Without saying a word, Hana left the room. Before I could even react, Kat turned to me and said..."
    scene w1_1295 with dissolve
    kat "Go after her and make sure she's okay."
    hide screen textbox2 with dissolve
    scene w1_1296 with dissolve

    menu:

        "Tell Kathleen I was already going to do that. [red]\[Toughness -1\]":
            $ toughness -= 1
            scene w1_1297 with dissolve
            show screen textbox2 with dissolve
            mc "Right, you don't have to tell me."
            scene w1_1295 with dissolve
            kat "Then get to it."
            scene w1_1299 with dissolve
            "..."

        "Tell Kathleen she would probably rather be left alone. [gr]\[Toughness +1\]":
            $ toughness += 1
            scene w1_1297 with dissolve
            show screen textbox2 with dissolve
            mc "Don't you think she would probably rather be left alone?"
            scene w1_1295 with dissolve
            kat "No, you idiot. What she needs is a friend. So, go be that."
            scene w1_1298 with dissolve
            mc "Alright... I'll go check on her."
            scene w1_1299 with dissolve
            "..."

    scene w1_1300 with dissolve
    war "This is what happens when you hire kids."
    scene w1_1301 with dissolve
    kat "Hush."
    scene w1_1302 with slideleft
    play music "music/sneaky-snitch.mp3"
    mc "Hmm...? Where'd she go...?"
    "Hana was nowhere to be found outside the exhibition hall."
    play sound "sound effects/elevator-bell.wav"
    scene black with fade
    "The elevator came from the mid-level."
    mct "(Maybe she ducked into one of the rooms?)"
    play sound "sound effects/door-open.wav"
    scene club-bdsm with cmet
    "The first room I tried: nothing."
    play sound "sound effects/door-open.wav"
    scene club-bedroom1 with fade
    mct "(Not in here...)"
    play sound "sound effects/door-open.wav"
    scene w1_1303 with fade
    "Third time's the charm. There Hana was, looking rather small in the corner of one of the more over-the-top rooms."
    scene w1_1304 with dissolve
    mc "You sure picked a gaudy place to sulk in."
    mc "I mean, who the hell would want to screw in a purple room? Makes my eyes want to bleed."
    stop music fadeout 3.0
    scene w1_1305 with dissolve
    hana "...I'd call it a magenta."
    hana "Hey, by the way."
    scene w1_1306 with dissolve
    play music "music/st-francis.mp3"
    mc "You okay?"
    scene w1_1307 with dissolve
    hana "Mmm, eh. Yeah."
    hana "Just kicking myself for getting worked up. Pretty fucking lame..."
    scene w1_1308 with dissolve

    if kat_polite == True:
        mc "What was Mrs. Pulman talking about?"
    else:
        mc "What was kathleen talking about?"

    scene w1_1309 with dissolve
    hana "I don't really want to tell you. Shit, even Jerrica doesn't know..."
    scene w1_1306 with dissolve
    mc "Sometimes it's easier to unburden yourself to a stranger rather than a friend."
    scene w1_1308 with dissolve
    mc "That said, I'll drop it if you want."
    scene w1_1310 with dissolve
    hana "*sigh* No... it'd be more awkward if I didn't explain myself."
    scene w1_1311 with dissolve
    hana "..."
    "I kept my mouth shut, letting Hana quietly gather her thoughts before speaking."
    scene w1_1312 with dissolve
    hana "The old man may be my father, but he ain't my dad. You know what I'm saying?"
    scene w1_1306 with dissolve

    if w1HanaSingleMother == True:
        mc "You mentioned you were raised by your mother, so..."
        scene w1_1307 with dissolve
        hana "Exactly."

    else:
        mc "You mean he wasn't around?"
        scene w1_1307 with dissolve
        hana "Bingo."

    scene w1_1309 with dissolve
    hana "The way my mom tells it, the old man used to direct commercials and she worked as his assistant at the time."
    scene w1_1308 with dissolve
    mc "The way she tells it? You mean, that's not the truth?"
    scene w1_1310 with dissolve
    hana "No, it's complete bullshit. The fucked up thing is, after all this time, I actually think she believes it."
    scene w1_1306 with dissolve
    mc "How did the two of them meet then?"
    scene w1_1312 with dissolve
    hana "The old bastard used to make scuzzy porn vids and my mom was one of his performers, before becoming his lover."
    scene w1_1313 with dissolve
    mc "Really...?"
    scene w1_1314 with dissolve
    hana "Uh huh. She got pregnant with me and the asshole split on my mom as soon as she started showing."
    hana "The fucker told me the truth himself, can you believe that? His excuse: she wasn't supposed to be off the pill."
    scene w1_1315 with dissolve
    mc "That's..."
    scene w1_1316 with dissolve
    hana "Yeah, there's no word for it other than shameless. I lived 21 years of my life without hearing a damn word from him and I was fine with that."
    hana "Then one day he contacts me out of the blue and drops all that on me, all to serve as a shitty preamble for wanting to get to know me."
    scene w1_1317 with dissolve
    mc "What did you tell him?"
    scene w1_1318 with dissolve
    hana "I told him to fuck off, of course. It wasn't my job to give a crap about his later-life crisis  - but he..."
    scene w1_1319 with dissolve
    hana "..."
    scene w1_1320 with dissolve
    mc "Take your time."
    hana "..."
    scene w1_1321 with dissolve
    hana "My mom is chronically ill. She has been, for awhile."
    hana "It's a degenerative thing. It was mild for years, but... she needs live-in care now. Expensive live-in care that I'm not exactly equipped to provide. Do you see where this is going?"
    scene w1_1322 with dissolve
    mc "You got to be kidding me? He bartered your mother's health to get you back into his life?"
    scene w1_1323 with dissolve
    hana "Not in any explicit terms. At first, he offered to help out financially, full stop. Of course, I accepted."
    scene w1_1321 with dissolve
    hana "I wouldn't let my pride get in the way of my mom's health. I got enough sense for that at least."
    scene w1_1323 with dissolve
    hana "Then after a couple of months of paying for a nurse, he mentions needing a bartender..."
    scene w1_1322 with dissolve
    mc "--and here you are"
    scene w1_1321 with dissolve
    hana "Here I am."
    scene w1_1322 with dissolve
    "A blanket of mutual silence fell over the room."
    "For my part, I was processing what Hana had told me. Of August's callous use of her mother's failing health to wedge himself back in his daughter's life."
    scene w1_1324 with dissolve
    "Hana's silence, on the other hand, was apprehensive. She was fidgeting uncomfortably in place."
    mct "(No shit, she's feeling exposed right now...)"
    "It might sound stupid, but maybe sharing an uncomfortable part of my past will help her feel less vulnerable."
    scene w1_1325 with dissolve
    mc "...my mom did porn too!"
    "I blurted it out, in the most inelegant way possible."
    scene w1_1326 with dissolve
    hana "...what?"
    scene w1_1327 with dissolve
    mc "You're the first person I've met that I've had that in common with, so I just wanted you to know."
    scene w1_1326 with dissolve
    hana "...for real?"
    if w1HanaSingleMother == True:
        scene w1_1327 with dissolve
        mc "Yeah, I told you she endured a lot for my sake. Well..."
    scene w1_1328 with dissolve
    mc "After my father died, it was just the two of us. My mother didn't have anyone."
    mc "For a brief time after that, she made a living on her back."
    scene w1_1329 with dissolve
    hana "..."
    scene w1_1330 with dissolve
    hana "That's a pretty fucking glib way of putting it."
    scene w1_1331 with dissolve
    mc "Shut up!"
    scene w1_1332 with dissolve
    "We shared another round of silence between us, but this time it felt less bitter."
    "I was content in enjoying the sensation of Hana's head resting on my shoulder, enjoying the physical warmth and the thick smell of chlorine that had entangled itself in the roots of her hair."
    "........."
    "......"
    "..."
    scene w1_1333 with dissolve
    play sound "sound effects/notification.wav"
    $ Hana_Relations = "Friend... I think."
    show relationhana with dissolve
    hana "Since we're both in a sharing mood, {b}how{/b} did you find out about your mom?"
    scene w1_1334 with dissolve
    mc "Uh... well... you see..."
    mc "I was browsing the internet one night, in the way a teenager that's going through puberty--"
    scene w1_1335 with dissolve
    hana "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEWWWWWW!"
    scene black with fade
    hana "How are you not like... LEATHERFACE after that?"
    "After that, Hana and I didn't really say or do much else. We just sat there in shared contemplation, enjoying a quiet kind of intimacy that I've never really had the chance in my life to enjoy."
    scene w1_1336 with dissolve
    hana "ZzZzZzzzz...."
    "It was, without a doubt, the most intimate moment I've ever shared in a tacky purple sex room."
    stop music fadeout 3.0
    scene black with fade
    "......"
    "..."
    hana "Thanks for being cool, [mcf]."
    scene w1_1337 with circlewipe
    play music "music/leaving-home.mp3"
    $ history_hana = "To my surprise, I learned that Hana is August's daughter and is only working as the Carnation Club's bartender due to him holding the purse strings for her sick mother's medical care. Turns out her mother used to do porn, a commonality that isn't lost on me."
    $ unread_hana = True
    play sound "sound effects/notification.wav"
    show bioupdate with dissolve
    war "The little Missy just left the building."
    war "She looked like she was in a better mood."
    scene w1_1338 with dissolve
    kat "I saw."
    scene w1_1339 with dissolve
    war "......."
    war "..."
    scene w1_1340 with dissolve
    kat "You're hovering. What is it?"
    scene w1_1341 with dissolve
    war "Sooner or later, she'll act out again."
    scene w1_1340 with dissolve
    kat "I know."
    scene w1_1341 with dissolve
    war "What should we do?"
    scene w1_1340 with dissolve
    kat "You tell me, Warren."
    scene w1_1342 with dissolve
    war "I don't know. She's August's daughter."
    scene w1_1341 with dissolve
    war "Our hands are tied."
    scene w1_1343 with dissolve
    kat "Well, we could always give her a spanking or put her in the corner for a time out."
    scene w1_1344 with dissolve
    war "You're joking, but... she's got a pretty fine ass. Spending a few days turning it out would fix her attitude problem."
    war "Wouldn't mind going that route."
    scene w1_1345 with dissolve
    kat "I know you wouldn't, but alas..."
    scene w1_1346 with dissolve
    war "Our hands are tied?"
    scene w1_1347 with dissolve
    kat "No. There's always a path."
    scene w1_1348 with fade
    kat "Life is one big shell game. You just got to know where to move the nutshells."
    scene black with fade
    stop music fadeout 3.0
    "......"
    "...."
    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionhana02 with blinds
    $ renpy.pause(6, hard=True)

label w1June05Start:

    $ date = "june05day"
    play sound "sound effects/alarmclock-digital.wav"
    scene black with fade
    show screen textbox2 with dissolve
    show screen qmenu with dissolve
    "*BEEP. BEEP. BEEP.*"

    if hanaFlag == True:
        scene w1_1349 with fade
        show june05day with squares
        mc "Ngg..."
        mct "(My head...)"
        play sound "sound effects/alarmclock-digital.wav"
        scene w1_1350 with dissolve
        mct "(Ugg--! What {b}genius{/b} drunkenly sets an alarm before conking out...?)"
        mct "(Me, that's who! {b}What an asshole{/b}!)"
        play sound "sound effects/alarmclock-digital.wav"
        scene w1_1351 with dissolve
        mc "{size=+15}SHUT UP!{/size=+15}"
        stop sound
        scene w1_1352 with dissolve
        mct "(I've drunk more in the past month than I have in my entire life.)"
        "This is probably a portent of things to come..."
        scene w1_1353 with dissolve
        mc "*Yaaaaaaaaaawn*"
        scene w1_1354 with dissolve
        mct "(Oh...?)"
        "One Missed Call - Work."

    if hanaFlag == False:
        scene w1_1355 with dissolve
        show june05day with squares
        "Yesterday felt like it flew by."
        "Not a single word from Killian, no contact with the club..."
        scene w1_1356 with dissolve
        mct "(Man, I feel refreshed.)"
        scene w1_1353 with dissolve
        mc "*Yaaaaaaaaaawn*"
        scene w1_1354 with dissolve
        mct "(Oh...?)"
        "Guess I jinxed myself there."
        "One Missed Call - Work."


    scene black with fade
    play sound "sound effects/call-end.wav"
    vm "You have one new message. Message 1."
    scene w1_1357 with dissolve
    kat "Mr. [mcl]."

    if hanaFlag == True:
        kat "I figured you're probably be sleeping in after the little party you had on the premises last night."
        kat "Don't worry, this call isn't about that. I don't blame you for that {i}indiscretion{/i}."

    if w1RoseGonzo == True:
        kat "I'm calling to let you know about how well your interview with Mrs. Carter was received by our patrons."

    if w1FelGonzo == True:
        kat "I'm calling to let you know about how well your interview with Mrs. Ford was received by our patrons"

    if w1VeroGonzo == True:
        kat "I'm calling to let you know about how well your interview with Miss Lynch was received by our patrons."


    if w1GonzoReward == True:
        $ Kathleen_Trust += 3
        kat "She was the crowd favorite."
        kat "Her owns charms had a role in it of course, but so did you."
        kat "You knew exactly what to ask and how to ask it. Excellent work."
        kat "That means you're due a reward. Drop by the club at noon sharp."
        kat "{b}Don't{/b} be late."
        play sound "sound effects/call-end.wav"
        vm "End of message."
        scene w1_1358 with dissolve
        "{i}Right{/i}. She did mention a reward the other day..."
        "Whatever it is, she didn't make it sound optional. Noon is just an hour from now."
        "I better get ready."
        scene black with fade
        "......"
        "..."
        jump w1GonzoRewardStart


    if w1GonzoReward == False:
        kat "She failed to garner the most attention."
        kat "She earned her own share of fans from the video, but she's not the crowd favorite by far."
        kat "It was in part due to her own appeal, but you failed to bring the most out of your subject."
        kat "Do better next time. Oh, and give me a call. I've got some work for you."
        play sound "sound effects/call-end.wav"
        vm "End of message."
        if toughness >= 18:
            mct "(Do better...? What a crock of shit.)"
        else:
            mct "(Do better...? Yeah, lemme just google how to best conduct a porn interview.)"

        mct "(Guess that means the reward she mentioned is off the table.)"
        mct "(Can't say I'm too disappointed. Hell, I might've dodged a bullet.)"
        jump w1NoGonzoReward


label w1GonzoRewardStart:
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

    scene club-fr-day with blinds
    play music "music/cold-sober.mp3"
    "I arrived at the Carnation Club, suspicious as to what this 'reward' could possibly be."
    scene w1_1359 with cmet
    "Kathleen had stressed such strict punctuality over the phone that it had me anxious and curious in equal parts."
    mct "(I mean, what even qualifies as an reward in that woman's mind?)"
    scene w1_1360 with fade
    "Well, I'm about to find out."
    mct "(I'm a little early, but that shouldn't be a problem...)"
    scene w1_1361 with dissolve
    kat "{size=-10}You girls ready?{/size=-10}"
    "I could hear chatter behind Kathleen's office door, one was a feminine voice I could distinctly pick out as belonging to the office's owner. It rang out loud and clear, with perfect enunciation that was fitting for a woman who clearly enjoyed the sound of her own voice."
    woman "hh--- mhh--"
    "The voice that came in response was faint and muffled."
    hide screen textbox2 with dissolve

    menu w1GonzoListen:
        "Announce your presence by knocking.":
            play sound "sound effects/door-knock.wav"
            scene w1_1363 with dissolve
            show screen textbox2 with dissolve
            "*Knock, knock.*"


        "{color=#FF1493}\[Voyeur/Inquisitive]{/color} Wait a moment and eavesdrop first." if history_voyeur == True or trait_inquisitive == True:
            show screen textbox2 with dissolve
            "My curiousity getting the better of me, I decided to listen a little before I entered."
            harp "{size=-15}Are you--{/size=-15}"
            scene w1_1362 with dissolve
            harp "Are you sure he'll be okay with this?"
            kat "What? Of course he will. You gals are professionals, and as professionals, you're well aware of the most fundamental axiom of our business."
            kat "That is: once you pull back the veneer of civility, all men are the same. Sure, some you have to pull a little harder at than others, but at their core they're just dumb, horny animals that can be led around by their baser instincts."
            harp "I'm still not sure about this--"
            dal "Shush. It's just business as usual. You can do that, right Harp?"
            harp "...yes."
            scene w1_1361 with dissolve
            mct "(Oooookay...)"
            "Part of me just wanted to turn around and go back the way I came, but I knew that wasn't a viable option."
            "Bailing would just hurt my position with Kathleen, and by extension, the club itself."
            "So, I knocked."
            play sound "sound effects/door-knock.wav"
            scene w1_1363 with dissolve
            "*Knock, knock.*"

        "{color=#696969}\[Voyeur/Inquisitive]{/color} Wait a moment and eavesdrop first." if history_voyeur == False and trait_inquisitive == False:
            jump w1GonzoListen

    scene w1_1364 with dissolve
    stop music fadeout 3.0
    if toughness >= 17:
        mc "It's [mcf]. I'm coming in."
    else:
        mc "It's [mcf]. Sorry, I'm a little early. May I come in?"
        scene w1_1360 with dissolve
        kat "Yes, it's open."

    play music "music/philly-crew.mp3"

    scene w1_1365 with fade:
        subpixel True
        xpan -60
        yalign 0.38
        linear 3 xalign 0.14

    "As soon as I entered, I was treated to the most beatific sight I had ever seen."
    "Four sets of pendulously heavy tits, exposed bare in the open daylight."

    scene w1_1365:
        subpixel True
        yalign 0.38
        xalign 0.5865
        linear 3 yalign 0.1

    mc "........."
    mc "......"
    mc "..."

    scene w1_1367 with dissolve
    mc "Uh... 'sup?"

    if kat_polite == True:
        "Lucy, Dalia, Harper, and even Mrs. Pulman herself stood in the center of the office, eyes fixed on me with a near diabolical look - practically in the nude, spare for some erotic flourishes."
    else:
        "Lucy, Dalia, Harper, and even Kathleen herself stood in the center of the office, eyes fixed on me with a near diabolical look - practically in the nude, spare for some erotic flourishes."

    "The three whores all wore a simple set of stockings that accentuated their legs splendidly, with chokers clasped snugly around their necks that invited all sorts oral-fixated ideas."
    "Dalia took it a step further than the other two, with long red gloves that extended up the length of her arms and gave her a more refined air than her peers."

    if kat_polite == True:
        "Mrs. Pulman, on the other hand, stood in stark contrast to her employees. She donned a full-body stocking and a garishly gold belt-like adornment that looped around her waist and extended up her torso to better accentuate her breasts."
    else:
        "Kathleen, on the other hand, stood in stark contrast to her employees. She donned a full-body stocking and a garishly gold belt-like adornment that looped around her waist and extended up her torso to better accentuate her breasts."

    "It all came together to make a sight that had me near stupefied, the end-result being the awkward pause that currently hung in the air."
    scene w1_1368 with dissolve
    kat "This is what good boys who live up to my expectations get."
    scene w1_1367 with dissolve
    "All I could muster in response was dumb silence."
    "It wasn't like the words were catching in my throat, no. The firing pins in my brain weren't even going off to form the words."
    scene w1_1369 with dissolve
    kat "Girls... unburden Mr. [mcl] of his clothes, would you?"
    scene w1_1370 with dissolve

    if kat_polite == True:
        "At Mrs. Pulman's bidding, the three whores sprung into action."
    else:
        "At Kathleen's bidding, the three whores sprung into action."

    scene w1_1371 with fade
    stop music fadeout 3.0
    mct "(Woah, woah, woah... wait a minute...!)"
    scene w1_1372 with dissolve
    "--is what I should {i}probably{/i} exclaim, but..."
    scene w1_1373 with dissolve
    play music "music/guiton-sketch.mp3"
    mct "{b}(Fuck that{/b}! I'm in!)"
    scene w1_1374 with dissolve
    mct "(There is just one thing, though...)"
    scene w1_1375 with dissolve
    mc "What is Lucy doing here?"
    scene w1_1376 with dissolve
    kat "It was Isaak's idea. Such a kind heart, he agreed to let her son enter St. Ives anyway, despite her failure."
    kat "All she has to do is a little moonlighting."
    scene w1_1377 with dissolve

    if kat_polite == True:
        "Circling behind me, Mrs. Pulman abruptly dropped to her knees and clung to the lower half of my body."
    else:
        "Circling behind me, Kathleen abruptly dropped to her knees and clung to the lower half of my body."

    "The maneuver, whether by happy accident or an intentional provocation, had her large breasts firmly pressed into my back."
    "The sheer body stocking she wore did nothing to lessen the feeling of skin-on-skin contact. I could feel the point of the older woman's right breast stiffen, poking into my backside and signaling to me that on some level, she found this situation exciting."
    scene w1_1378 with dissolve
    mc "Eh..?"
    "Abruptly taking my half-flaccid cock in the palm of her hand, she gently massaged it at the base, coaxing it to full mast."
    scene w1_1379 with dissolve
    kat "Tell me: once you shoot, how long does it typically take you to reload?"
    scene w1_1380 with dissolve
    mc "{i}What{/i}...?"
    "I knew what she meant, but the question itself wasn't something I'd ever thought about, much less tested."
    mc "I don't know."
    scene w1_1379 with dissolve
    kat "Fifteen minutes is the average refractory period for a college-age male."
    scene w1_1380 with dissolve
    mc "Okay...?"
    "This had suddenly taken a distinctly unsexy, clinical-like turn."
    scene w1_1381 with dissolve
    kat "I'm going to help you push past your limits today. You're about to experience more pleasure in one hour than you have had in your entire short life."
    "She spoke words that {i}should{/i} sound like an exaggeration, but whose cold delivery had me wholly believing their veracity. She intended to make good on her promise."
    kat "How does that sound?"
    scene w1_1384 with dissolve
    "If I'm being honest, the way she said it sent a chill up my spine."
    scene w1_1382 with dissolve
    hide screen textbox2 with dissolve

    menu:

        "Tell Kathleen that sounds a little scary. [red]\[Toughness -1\]":
            $ toughness -= 1

            scene w1_1383 with dissolve
            show screen textbox2 with dissolve
            mc "That sounds... extreme."
            scene w1_1384 with dissolve
            kat "Maybe, but that's what makes it {b}exciting{/b}."


        "Tell Kathleen that sounds exciting. [gr]\[Toughness +1\]":
            $ toughness +=1

            scene w1_1385 with dissolve
            show screen textbox2 with dissolve
            mc "That sounds like... fun."
            scene w1_1386 with dissolve
            kat "We'll call it a promise then."

        "Daringly tell Kathleen to bring it on. [gr]\[Toughness +1\] \[Kathleen +1\]":

            if toughness >= 19:
                $ toughness +=1
                $ Kathleen_Affection +=2

                scene w1_1387 with dissolve
                show screen textbox2 with dissolve
                mc "It sounds ridiculous, like you're just flapping your gums."
                scene w1_1386 with dissolve
                kat "I'm a woman of my word, [mcf]."
                scene w1_1387 with dissolve
                mc "Then why don't you put your money where your mouth is and start jerking my cock."
                scene w1_1386 with dissolve
                "I mean, who could blame me for being overly eager? With a veritable smorgasbord of tit flesh and round, fat asses within reach, I'm rearing to go."
                scene w1_1391 with dissolve
                kat "In due time, Mr. [mcl]."

            else:
                $ toughness +=1
                $ Kathleen_Affection +=1

                scene w1_1385 with dissolve
                show screen textbox2 with dissolve
                mc "It sounds to me like you're just speaking words."
                scene w1_1386 with dissolve
                kat "Does it now?"
                scene w1_1387 with dissolve
                mc "Then go ahead and prove it to me. {b}Put your money where you mouth is{/b}."
                "I couldn't lie. With a feast of tit flesh and fat asses so close, I'm more than eager to go."
                scene w1_1392 with dissolve
                kat "Oh, it'll be my pleasure."

    scene black with fade
    kat "Over here. Give me your hands."
    mc "Why?"
    kat "You're about to get your dick polished by three women, two of which are the club's best whores, and you're going to waste time arguing?"
    scene w1_1388 with dissolve
    "Finding her argument persuasive, I let Kathleen tie my hands behind my back with a handkerchief and sat down as instructed in a nearby chair that had been pulled out."
    "Just for curiosity sake, I gave my bindings a tentative jostle, checking to see the give I had to work with."

    if kat_polite == True:
        "It turned out to be very little, actually. Seems Mrs. Pulman has a knack for tying knots."

    else:
        "It turned out to be very little, actually. Seems Kathleen has a knack for tying knots."

    scene w1_1389 with dissolve
    mc "You sure got it tight."
    scene w1_1390 with dissolve
    kat "One of the few skills that stuck with me from when I was a girl scout."
    scene w1_1389 with dissolve
    mc "You gotta be kidding..."
    scene black with fade
    "Things went abruptly dark as something or other was stretched around my eyes and pulled tightly against my face."
    mc "Eh...?"
    scene w1_1393 with dissolve
    mc "What are you doing?"
    scene w1_1394 with dissolve
    kat "Blindfolding you."
    scene w1_1395 with dissolve
    mc "I can see that, but why?"
    scene w1_1396 with dissolve
    "Losing both my hands and my eyes made me deeply uncomfortable on a instinctual level."
    "It wasn't an entirely unwelcomed situation. There was, of course, an underlying sense of excitement inherent to being so openly vulnerable in a room full of sexy women with dirty intentions."
    "It was still cut with a sense of uneasiness, however."
    scene w1_1397 with dissolve
    kat "To spice things up. For some people, being unable to see allows them to more acutely enjoy physical sensation."
    "Suddenly, I could feel the weight of a human body in my lap."
    scene w1_1398 with dissolve
    kat "The touch of a lover becomes more pronounced and the sting of whip more intolerable. That said, for others... not so much. Everyone's wired a bit different when it comes to audio-visual stimulation."
    "She felt so astonishingly soft, so incredibly warm..."
    kat "Men tend to be more {b}visually{/b} oriented in their arousal, but..."
    kat "That's not the case with you, I suspect?"
    scene w1_1399 with dissolve
    "As she spoke, Kathleen blew a gust of hot air into the inner reaches of my ear canal, eliciting a pleasurable shudder from my body."
    scene w1_1398 with dissolve
    kat "That felt better than it usually would, am I right?"
    scene w1_1400 with dissolve
    mc "You might be onto something."
    "I couldn't deny it. It did."
    scene w1_1398 with dissolve
    kat "Thank you for your honesty. Some men will deny simple physiological truths, if it doesn't slot neatly into their sexual self-schema."
    kat "You, however, are honest. Capable of keeping an open mind..."
    scene w1_1401 with dissolve
    "A wet, warm sensation enveloped the side of my head as Kathleen set to probing the contour's of my ear with her tongue."
    mc "Nga..!"
    "It was simple act, at odds with the sheer pleasure it produced."
    scene w1_1402 with dissolve
    "Each bite, each nibble, each brush with the older woman's wiry tongue sent wave after wave of physical thrill coursing through my nervous system."
    "The ways she moved her tongue were deliberate. Economical. Every little lash a step in a greater waltz of pleasure."
    scene w1_1403 with dissolve
    "I couldn't believe I was feeling this good from just my {b}ear{/b} of all things. Just a small dish of cartilage and nerves, yet she was squeezing pleasure out of it like a man in a desert desperately trying to extract water from a cactus."
    "She mentioned Dalia and Harper being the club's best whores, but... I was started to wonder if there wasn't another woman above them when it came to carnal instinct."
    scene w1_1404 with dissolve
    kat "Honest boys get a reward."
    scene w1_1405 with dissolve
    kat "Dalia!"
    dal "Yes, Mrs. Pulman?"
    scene w1_1406 with dissolve
    kat "Get Mr. [mcl] started with your breasts."
    scene w1_1407 with fade
    "Rather than a verbal response, Dalia's reply came in the form of action, as the next thing I experienced was the feeling of soft hands prying my legs apart and the intuitive feeling that someone was now positioned directly at my feet."
    scene w1_1408 with dissolve
    dal "If you'll excuse me..."
    scene w1_1409 with dissolve
    "With those words followed a pleasant sensation, as I felt my cock enveloped in the supple flesh of Dalia's soft breasts."
    scene w1_1410 with dissolve
    dal "I'll now begin."
    scene w1_1411 with dissolve
    "In a well-practiced motion, Dalia flexed her shoulders, firmly pushing her breasts together to form a tight squeeze and slowly began to work her magic."
    "The feeling of my dick being swaddled in the experienced prostitutes all-consuming tit flesh was enough by itself to put me on edge, but this..."
    show w1DaliaPaizuri with dissolve
    image w1DaliaPaizuri= Movie(play="w1DaliaPaizuri.webm")
    mc "Ahh...!"
    "I didn't even try to conceal my abject pleasure, letting out an audible moan for the whole room to hear."
    "Slowly, Dalia moved her breasts up and down the length of my meat pole in a concentrated effort."
    dal "You have such a naughty dick, Mr. [mcl]."
    dal "It's already leaking so much and dirtying my breasts... I bet you wish you could see for yourself."
    dal "Since you're blindfolded, me describing it in detail will have to do."
    scene w1_1412 with dissolve
    kat "That's so considerate of you Dalia."
    scene w1_1413 with dissolve
    lucy "It's so filthy looking..."
    "Another whore's voice was added to the growing peanut gallery."
    scene w1_1414 with dissolve
    kat "Lucy! I know you're new, but you should know better."
    scene w1_1415 with dissolve
    dal "You need to treat every patron's cock with reverence. Worship it, breathe it, live for it..."
    scene w1_1416 with dissolve
    harp "Fake it until you make it."
    "For my part, I was too engrossed in the spiraling pleasure growing in my nutsack to give any heed to the ridiculous lesson playing out before me."
    show w1DaliaPaizuri with dissolve
    mct "(Dalia's breasts... are SO amazing...!)"
    "By now, a generous amount of pre-cum had dribbled from the tip of my dick like a leaky faucet and coated the valley of Dalia's mammaries."
    "Unable to see the beautiful sight for myself, I made do with pairing the {i}feeling{/i} of Dalia's fervent service with the vivid fantasies of my mind's eye."
    "In my head, I could see my cock spearing open the seasoned whore's cunt, while her tattooed co-worker slavishly ate my asshole out like it was the first bite of food she had all week."
    "Thoughts of that nature kept playing over and over in my head, my imagination utterly inflamed by my lack of sight."
    dal "*SQUEELCH* *SQUELCH*"
    dal "*SQUEELCH* *SQUELCH* *SQUELCH*"
    dal "*SQUEELCH* *SQUELCH*"
    dal "*SQUEELCH* *SQUELCH* *SQUELCH*"
    scene w1_1417 with dissolve
    dal "You hear that, Mr. [mcl]? That's the sound of your naughty dick gliding through my tits!"
    "*SQUEELCH* *SQUELCH*"
    dal "It's so fucking obscene...!"
    dal "*SQUEELCH* *SQUELCH* *SQUELCH*"
    show w1DaliaPaizuri with dissolve
    dal "You really do have a beautiful cock. So big, so meaty..."
    dal "You could split a gal open with this monster."
    "Dalia showered me with the words of a practiced whore, supplementing her skilled ministrations with pure verbal sex fantasy."
    dal "*SQUEELCH* *SQUELCH*"
    dal "*SQUEELCH* *SQUELCH* *SQUELCH*"
    dal "*SQUEELCH* *SQUELCH*"
    dal "*SQUEELCH* *SQUELCH* *SQUELCH*"
    dal "It's so hot...! Your dick is on fire...!"
    "Dalia made short work of me. My balls clenched with that familiar tightness and then I..."
    mc "Ah~! AH!"
    dal "It's a little early to be making a mess..."
    scene w1_1418 with flash
    play sound "sound effects/spurt.wav"
    mc "AAAAAAH!"
    "With practiced precision, Dalia engulfed my pole with her mouth right as I began to ejaculate."
    play sound "sound effects/spurt.wav"
    mc "--!" with flash
    play sound "sound effects/spurt.wav"
    dal "mph...!" with flash
    "From a pinpoint in the darkness, flashes of light exploded as it felt like I was pushing my very soul out from the tip of my dick."
    stop music fadeout 3.0
    scene w1_1419 with dissolve
    mc "Gah..."
    scene black with fade
    kat "You see Harper? That's why Dalia's the best."
    scene w1_1420 with curtains
    "Abruptly, my sight was returned to me as someone removed my blindfold."
    scene w1_1421 with dissolve
    dal "Aaawwwh~♥!"
    "Only to be suddenly greeted with the beautiful sight of Dalia presenting herself to me with a mouthful of my cum."
    dal "-ooouh~cahm~SO~'UCH!"
    scene w1_1422 with dissolve
    dal "-aht-shwould-eye-dew-'ith'et?"
    scene w1_1420 with dissolve
    mc "Huh...?"
    kat "She's asking what she should do with it."
    mct "(What she should do with it...? Oh...!)"
    "I have a couple of ideas..."
    hide screen textbox2 with dissolve

    menu:
        "Tell Dalia to swallow it.":
            show screen textbox2 with dissolve
            mc "Swallow it."
            scene w1_1422 with dissolve
            dal "'ith-phweasure!♥"
            scene w1_1423 with dissolve
            dal "*GULP*"
            scene w1_1424 with dissolve
            "..."
            mc "Now show me."
            scene w1_1425 with dissolve
            dal "AAAAAAAAWH!"
            mct "(Amazing...)"

        "Tell Dalia to share it.":
            show screen textbox2 with dissolve
            mc "Good girls know how to share."
            scene w1_1426 with dissolve
            dal "Hehe..."
            scene w1_1427 with fade
            dal "Ah-swha~♥"
            "Without missing a beat, Dalia pulled her tattooed comrade into her arms and locked lips in a passionate display of cumsluttery."
            harp "Mmm--!"
            "Harper, while not as eager, dutifully accepted my load as the contents of Dalia's mouth was tranferred into hers."
            scene w1_1428 with dissolve
            dal "That was delicious, sir."

    scene w1_1429 with fade
    play music "music/covert-affair.mp3"
    kat "You're still hard, as expected of someone so young."

    if kat_polite == True:
        "As I was fixated by the beautiful sight that had just played out in front of me, Mrs. Pulman had repositioned herself and was now closely examining my penis like one would a piece of ripened fruit."
    else:
        "As I was fixated by the beautiful sight that had just played out in front of me, Kathleen had repositioned herself and was now closely examining my penis like one would a piece of ripened fruit."

    kat "Let's see if I can get you back to one hundred percent though..."
    scene w1_1430 with dissolve

    if kat_polite == True:
        "Not given even a moment to bask in post-orgasmic bliss, Mrs. Pulman took my half-stiffy in her soft, lotioned hand once more."
    else:
        "Not given even a moment to bask in post-orgasmic bliss, Kathleen took my half-stiffy in her soft, lotioned hand once more."

    mc "Eyh...!"
    "The sudden cool touch on my overly sensitive post-orgasm prick sent a small shock to my body."
    scene w1_1431 with dissolve
    kat "Sorry. I bet the nerves in your dick are still tingly a little, right?"
    scene w1_1432 with dissolve
    mc "A little..."
    scene w1_1431 with dissolve
    kat "Then, allow me to comfort and clean you up a little..."
    scene w1_1433 with dissolve

    if kat_polite == True:
        "In a swift, fluid motion Mrs. Pulman threaded my meatpole past her cushiony lips and took it to the base."
    else:
        "In a swift, fluid motion Kathleen threaded my meatpole past her cushiony lips and took it to the base."

    scene w1_1434 with dissolve
    "There, she held the position, the tip of my dick kissing the back of her throat with nary a peep of discomfort from the Carnation Club matron."
    "The feeling of my aching prick being holstered in the old hag's mouth for an extended period of time proved oddly soothing, like her throat was giving my cock a big comforting hug."
    "At the same time, she used tongue to gently vigorously massage the underside of my shaft."
    "Needless to say, it didn't take long for my cock to reach full tumescence once more."
    scene w1_1435 with dissolve
    kat "--mwah~♥"
    "She pulled herself off me with an audible {b}plop{/b}."
    scene w1_1436 with dissolve
    kat "Mmmh... I love young men. Such an honest reaction..."
    scene w1_1437 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Share an observation of your own. [red]\[Kathleen -1\]":
            $ Kathleen_Affection -= 1
            scene w1_1438 with dissolve
            show screen textbox2 with dissolve
            mc "...and I love the look of my dick in your mouth."
            mct "(That's the longest time I've been in a room with this women without her moving her mouth endlessly.)"
            mc "It suits you."
            scene w1_1439 with dissolve
            kat "Don't get too cheeky now. If you want to treat someone like a common whore, well..."


        "Ask Kathleen for a repeat performance. [gr]\[Kathleen +1\]":
            $ Kathleen_Affection +=1
            scene w1_1440 with dissolve
            show screen textbox2 with dissolve
            mc "Why'd you stop? That felt so good..."
            scene w1_1436 with dissolve
            kat "That's what I'm talking about, [mcf]! So very honest. So needy. I love it."
            kat "Don't worry. That was just a little maintenance, for the next part..."

    scene w1_1441 with dissolve
    kat "Harper! Lucy! You're up. Give Mr. [mcl] a double dose of attention."
    harp "Yes, Ma'am."
    scene w1_1442 with dissolve
    harp "Come on, Luce. Follow my lead."
    stop music fadeout 3.0
    scene black with circlewipe
    hl "*Fwhup.* *Chup~!*"
    hl "*Fwhup.* *Chup~!* *Khwup!*"
    scene w1_1443 with cmet
    play music "music/FeelinIt.mp3"
    "Soon, the pair was making good on Kathleen's order."
    "Flanked on both sides, the two whores had set to work spit-shining my cock."
    hl"*Fwhup.* *Chup~!*"
    hl"*Fwhup.* *Chup~!* *Khwup!*"
    "Kiss after kiss dotted the length of my shaft, leaving little dabs of saliva that glistened in the open daylight."
    hl"*Fwhup.* *Chup~!*"
    hl"*Fwhup.* *Chup~!* *Khwup!*"
    scene w1_1444 with dissolve
    harp "Mmmhaaa~♥ It's got such a lewd, meaty scent...!"
    scene w1_1445 with dissolve
    lucy "I-it, does?"
    scene w1_1446 with dissolve
    harp "Even when it isn't true, it's your job to make it the {b}patron's truth{/b}, got it?"
    scene w1_1445 with dissolve
    lucy "I need to say lewd things and play to customer's vulgar ego?"
    scene w1_1446 with dissolve
    harp "You got it. Give it a try."
    "The two carried on like I was a mere prop. Something that should probably be more frustrating, but it was hard to get too worked up about since the physical affection they were dolling on my cock was very, very real and very, very pleasurable."
    scene w1_1447 with dissolve
    lucy "The stench is so thick and manly~♥"
    scene w1_1448 with dissolve
    kat "I can appreciate the teachable moment girls, but don't leave Mr. [mcl]. He's starting to look frustrated."
    scene w1_1449 with dissolve
    hl"*Fwhup.* *Chup~!*"
    "Thankfully, Kathleeen put them back on track."
    hl"*Fwhup.* *Chup~!* *Khwup!*"
    scene w1_1450 with dissolve
    "This time, the point of attack where my engorged testes, hard at work producing another load for the soon-approaching, inevitable climax."
    hl"*Fwhup.* *Chup~!*"
    "The pair divided my family jewels evenly between them, each of them delicately cupping my nuts with their lips - sucking, kissing, gently caressing them with their tongues."
    hl"*Fwhup.* *Chup~!* *Khwup!*"
    "Every little lash of tongue had my balls tightening, every small kiss sent a jostle of excitement that extended to the glans of my penis."
    scene w1_1451 with dissolve
    harp "Never, ever neglect the balls."
    harp "That said... the fastest way to milk a man is through his prostate."
    mct "(Uh, hold up...)"
    harp "Snake a finger far enough in to find that magic love bean, you have a direct line to making a man cum his fucking brains out whenever you want."
    scene w1_1452 with dissolve
    mc "Now, wait a minute..."
    scene w1_1453 with dissolve
    harp "Reeeelax. You should see that look on your face."
    scene w1_1454 with dissolve
    kat "Hurry things along girls. [mcf] has a lot to sample and we don't have all day."
    scene w1_1455 with dissolve
    harp "You heard Mrs. Pulman, it's time to move things along."
    scene w1_1456 with dissolve
    lucy "Me...?"
    scene w1_1457 with dissolve
    harp "Yeah, you. There's two of us and only one dick. Since you're the newbie, you should listen to your senior."
    scene w1_1458 with dissolve
    harp "Don't worry, big sis Harper will still give you a helping hand."
    scene black with fade
    lucy "I don't really need help. Besides, I'm pretty sure I'm older--mphffg!"
    scene w1_1459 with dissolve
    lucy "*Slurrrrrrp!*"
    "The scene that was now playing out, like the ones before it, was an entirely {b}new{/b} experience for me. Another to add to the growing pile of sexual exploits that I had only previously dreamed of."
    lucy "Mmmmmm--!"
    scene w1GonzoRewardGuidedBJ with dissolve
    "Harper was using Lucy's mouth like a sex toy, guiding it up and down the length of my shaft with a degree of well-measured control that was indifferent to Lucy's comfort."
    "From my vantage point, I could spot tears of discomfort welling up at the corner the school teacher's eyes, a by product of having my cock playing speed ball with her uvula."
    hide screen textbox2 with dissolve

    menu:
        "Show some concern for Lucy's comfort. [red]\[Toughness -1\]":
            $ toughness -= 1
            show screen textbox2 with dissolve
            mc "You might be doing it a little too rough, Harper."
            lucy "*Gwhup~fwup--!*"
            scene w1_1464 with dissolve
            harp "Don't worry, she can take it. This isn't really anything special for this line of work."
            scene w1_1465 with dissolve
            harp "You alright, Lucy?"
            lucy "Mmmhppg--hhyeha~*fmphup*"
            scene w1_1464 with dissolve
            harp "See?"
            scene w1GonzoRewardGuidedBJ with dissolve
            "I'm not so sure the raven-haired woman's unintelligible response was reassuring. Still..."


        "Just sit back and enjoy the oral attention. [gr]\[Toughness +1\]":
            show screen textbox2 with dissolve
            $ toughness +=1
            pass


    lucy "*Gwhup~fwup--!*"
    "It was a dazzling sight."
    lucy "*Slurrrrrrp!*"
    "A viscous combination of pre-cum and spittle was forming at the edge of Lucy's lips, each pass up and down my cock displacing and creating more."
    lucy "Mmmmm~! *Gwhup~*"
    lucy "*Slurrrrrrp!*"
    "Erotic sucking sounds filled the room, all the while my boss and Dalia were content to watch from the side lines."
    scene w1_1466 with blinds

    if kat_polite == True:
        "Mrs. Pulman had a pleased look on her face, while the head girl had an expression that seemed to suggest {i}business as usual{/i}."
    else:
        "Kathleen had a pleased look on her face, while the head girl had an expression that seemed to suggest {i}business as usual{/i}."

    scene w1_1467 with blinds
    lucy "*Slurrrrrrp!*"
    "Harper was taking a parodoxically tender approach. On one hand, she was using the fledgling whore's face like a tool, in the other she was now nibbling on the school teacher's ear."
    lucy "*Gwhup~fwup--!*"
    "Groping her full, heavy breasts."
    lucy "Mmmmmm--!"
    "Offering near imperceptible words of encouragement directly in the cock sucker's ear."
    "Whether the show was being put on for my benefit or hers, I couldn't say. Either way, the sensual sight was helping spur me closer to orgasm."

    if kat_polite == True:
        "Suddenly, I was very glad Mrs. Pulman didn't bother to put the blindfold back on."
    else:
        "Suddenly, I was very glad Kathleen didn't bother to put the blindfold back on."

    scene w1_1468 with dissolve
    harp "You're pretty wet down here, huh?"
    "While using one hand to maintain the pace of the ferocious face fucking, Harper dipped another down Lucy's midsection and straight to her crotch."
    lucy "*Slurrrrrrp!* *Fwhup~chup~!*"
    "It was true. A quick glance at the floor revealed a fine, thin stand of femcum trailing down from her quim and pooling on her thigh."
    kat "Oh? My, my. You're taking to the job pretty well, Mrs. Long."
    lucy "Mmmmmm--! {b}Mmmmm--!{/b}"
    kat "By summer's end, you're bound to be a club favorite."

    if kat_polite == True:
        "At this point, I'm pretty sure the school teacher turned whore wasn't even registering Mrs. Pulman's offhanded taunting as words."
    else:
        "At this point, I'm pretty sure the school teacher turned whore wasn't even registering Kathleen's offhanded taunting as words."
    scene w1GonzoRewardGuidedBJ2 with dissolve
    "All it looked like she had on her mind was the process of inhaling and exhaling of dick, or more precisely, stealing as many breaths as she could in between the rapid, heavy thrusts of Harper's hand."
    "Gradually Lucy's eyes became dull and unfocused and the staccato-like murmuring gave way to the raw wet sounds of sloppy frenetic fellatio "
    mc "Eh... *huff* *huff*"
    "In no time at all, I could feel my balls once again swell in anticipation. A notable feat, I thought, considering I had already spent a load not too long ago."
    mc "Oh, shit..."
    scene w1_1473 with dissolve
    harp "Sounds like you're ready to blow."
    play ambient "sound effects/fel1.wav"
    scene w1GonzoRewardGuidedBJ3 with dissolve
    "Seeing that, Harper doubled her efforts. Taking Lucy's heads with both heads, she commenced a face fucking unlike the previous pace."
    lucy "*Fwpop* *Slurrrrrp!* *Fwchup~!!!*"
    "The image of Harper using the school teacher's face with reckless abandon became my sole focal point as the cum began to pool at the base of my dick. "
    lucy "*Slurrrrrrp!* *Fwhup~chup~!*"
    "All extraneous thought not related to my immediate sexual release vacated from my mind, as I felt myself cresting over the hill toward gratification."
    mc "Oh, shi--"
    stop music
    stop ambient
    play sound "sound effects/spurt.wav"
    scene w1_1474 with flash
    mc "Gaaaaawh!!!!"
    "With a sudden sharp outburst, my mind was completely blanketed by a tsunami of pleasure as rope after rope of semen forced it's way through my urethra with dizzying force."
    play sound "sound effects/spurt.wav"
    scene w1_1475 with flash
    lucy "Mmmmph--? Mmmppp--!!!"
    mc "Nngg-!!"
    mct "(It's still going?!)"
    play sound "sound effects/spurt.wav"
    scene w1_1476 with flash
    lucy "{b}MMMMPPPGGGFFFFFH--!{/b}"
    scene w1_1477 with fade
    lucy "eeh, what deh fhuck?"
    lucy "Dhat wus sho~mhuch."
    scene w1_1478 with w20
    mc "Ummmhpf.... what..."
    mc "I'm feeling... a bit..."
    scene w1_1479 with dissolve
    kat "Lightheaded? Here, sit down."
    scene black with fade

    if kat_polite == True:
        "Mrs. Pulman lent me her shoulder and guided me to a nearby chair. "
    else:
        "Kathleen lent me her shoulder and guided me to a nearby chair."

    scene w1_1480 with dissolve
    mc "If I knew all {b}THIS{/b} was going to happen today, I probably wouldn't have skipped breakfast this morning, ugh..."
    "Once my butt was firmly planted in the seated position, my bout of vertigo quickly dissipated."
    scene w1_1481 with dissolve
    mc "Still, {b}damn{/b}... that was awesome."
    kat "Don't make it sound like it's over."
    mc "I don't exactly have much gas left in the tank..."
    scene w1_1482 with dissolve
    kat "No...?"
    scene w1_1483 with dissolve
    "My boss locked eyes on me with a steadfast gaze."
    mct "(If I'm being honest with myself...)"
    "Despite the age gap and her callous attitude, as well as her reprehensible and predatory use of her charity..."
    scene w1_1484 with dissolve
    mct "(She's kinda hot for an old lady.)"
    "That said, I'm spent."
    mc "I'm worn out after going back-to-back like that."
    scene w1_1485 with dissolve
    kat "I got something that can remedy that."
    scene w1_1486 with dissolve

    if kat_polite == True:
        "Mrs. Pulman's face twisted into an impish expression, abruptly pulling my attention to the odd pose she held at my feet."
    else:
        "Kathleen's face twisted into an impish expression, abruptly pulling my attention to the odd pose she held at my feet."

    "This whole time, she had kept one of her hands behind her back, looking like a sommelier in the process of pouring wine."

    if toughness >= 14:
        mc "Uh... could you untie my hands?"
    else:
        mc "Uh... could you untie my hands, please?"

    scene w1_1487 with dissolve
    play music "music/leaving-home.mp3"
    kat "I will, in a minute."
    kat "Dalia."
    scene w1_1492 with dissolve
    dal "Look at me, [mcf]."
    mc "...huh?"
    scene w1_1493 with dissolve
    mc "Mmmmmh...!"
    "Dalia pulled me into a deep kiss, pressing her soft lips firmly into mine."
    mc "Mmmm..."
    kat "Don't be alarmed. {b}This{/b} is going to make things a whole lot more fun."
    mc "Mmmhwhu-arr-ou?"
    mct "(What is she talking about?)"
    scene w1_1494 with flash
    mc "--?!"
    "I felt a sharp pinprick on my inner thigh, quickly followed by a mild cramping feeling as a warmth radiated up my spine." with flash
    mct "(Wait... did she just inject me with something...?)"
    mc "What the fuck?!" with hpunch
    "As I was about to vocalize my anger and confusion, I found I couldn't get the words out."
    "As the air deflated from my lungs, a chill rocked my body."
    mc  "Mmmh...wha?"
    scene w1_1495 with dissolve
    "My dick immediately swelled with blood, becoming {i}painfully{/i} turgid in a split instant."
    mct "(Nggg...!)"
    "Having experienced this before, I immediately understood what was going on. The bitch had just shot me up with an aphrodisiac."
    "Or atleast I {i}should{/i} be seething mad right about now, but... the overriding feeling of the moment was unbridled arousal."
    scene w1_1496 with dissolve
    mc "*huff* *huff* ...you just drugged me!"
    scene w1_1497 with dissolve
    kat "I did. Don't be mad."
    scene w1_1496 with dissolve
    mc "*huff* *huff* How could I not be mad?"
    scene w1_1499 with dissolve
    kat "Don't fuss. What I just injected you with is a {b}harmless{/b}, AMAZING little concoction."
    scene w1_1498 with dissolve
    mc "Oh, yeah. Extensive clinical trials and FDA approval! I'm sure!"
    "As much as I tried to muster up the indignation appropriate for the situation, deep down, I wasn't really feeling it."
    "Instead, all I could focus on was my skin of all things. It was burning and flushed, bloods vessels opening wide and filling to the brink."
    "The result was..."
    play sound "sound effects/whoosh.wav"
    scene w1_1500 with dissolve
    mc "Aaahh...!"
    mct "Seriously...? This damn chair felt amazing!"
    "Whatever is in that drug, it's made even the feeling of cold leather feel provocative against my over-wrought skin."
    scene w1_1501 with dissolve
    kat "It's already fully activated, I'll be damned! Van Doren really outdid himself with this one."
    mct "(She's SURPRISED?!)"
    kat "The science and the effects of that concoction is astounding, but I won't bore you with details."
    kat "Quite simply, it makes you {i}want{/i} to fuck."
    kat "It gives you the energy {i}to{/i} fuck."
    kat "It makes your body {i}capable{/i} of fucking."
    "She wasn't telling me anything I hadn't already figured out. The sheer sexual desire that was welling up in me had already reached its melting point."
    "The urge to mate and rut was so strong that I was sick to my stomach from the sheer physiological stress."
    "I had gone from feeling like a depleted battery, to being supercharged within sixty seconds."
    kat "Don't look so pensive about it. Just enjoy fucking yourself into a coma."
    scene w1_1502 with dissolve
    mc "I..."
    "I {b}NEED{/b} to fuck."
    scene w1_1503 with dissolve
    mc "Untie me."
    scene w1_1504 with dissolve
    kat "With pleasure."
    stop music fadeout 3.0
    scene black with fade
    lucy "...huh? Wha-are you...?"
    lucy "Oooomf!"
    play music "music/time-piece.mp3"
    scene w1HshakeReward01 with cmet
    "*CHUP!* *CHUWP! *FHUP!*"
    "In a bid to halt my growing sexual frustration, I grabbed the first whore within reach."
    mc "(Fuuuuck!)"
    "Just a little while ago, Dalia gave me my first ever titjob. Now I was kneeling on top of Lucy, in a half-conscious state with a brain addled by lust, thrusting wildly into the cavernous valley of the schoolteacher's breasts."
    mc "Ah, what the {b}fuck{/b}! This feels so... so... AMAZING!"
    kat "That's a good boy. Chisel the pleasure of this afternoon into your memory."
    mct "(Aaah~♥ Lucy's tits! Lucy's fat cow tits-!♥)"
    mct "(So SOFT, WARM, PLIABLE to touch...)"
    lucy "Woah..."
    "No matter how firm I grip Lucy's breasts, no matter how hard I dig the tips of my fingers into the malleable, alabaster flesh..."
    lucy "It's like you're trying to mate with my breasts..."
    "They still had even more give to them. Her soft, pillow-like tits..."
    mc "(It's not enough... I want to {b}RUIN{/b} them.)"
    "*CHUP!* *CHUWP! *FHUP!*"
    "Using my hands, I gripped her breasts even tighter, pressing the voluminous orbs together in a desperate attempt to create a cunt-like grip for my penis to glide through."
    "*CHUP!* *CHUWP! *FHUP!* *CHUP!* *CHUWP! *FHUP!*"
    lucy "Ngg-!"
    "*CHUP!* *CHUWP! *FHUP!* *CHUP!* *CHUWP! *FHUP!* *CHUP!* *CHUWP! *FHUP!*"
    "With wanton abandon, I rocked my hips forward with an even greater momentum, ripping a path through the schoolteacher's expansive cleavage."
    kat "My. She's right. You look like you're trying to get impregnate her breasts."
    "*CHUP!* *CHUWP! *FHUP!* *CHUP!* *CHUWP! *FHUP!*"
    harp "Trying to knock up her knockers... ha!"
    mc "Ah...!"
    dal "That's a terrible one, Harp."
    "Brimming with vim and vigor, I felt tireless, like I'd never run out of stamina. The drug had me on an entirely different stratum."
    "*CHUP!* *CHUWP! *FHUP!* *CHUP!* *CHUWP! *FHUP!*"
    mc "That's it...!"
    stop ambient
    scene w1_1510 with flash
    play sound "sound effects/spurt.wav"
    mc "--!"
    scene black with fade
    mct "(What the hell...? I'm still so horny!)"
    "Paradoxically, cumming didn't bring relief I had expected. Instead, my dick remained bloated, while an even stronger fuck-hungry desire swelled in the pit of my stomach."
    "Despite ejaculating three times, it felt like I had only just whet my appetite."
    "{b}I needed more{/b}."
    scene w1HshakeReward02 with cmet
    dal "Ah~♥ Eeeeh, fuck! That's deep!"
    "The rut had only just begun, as I tossed Dalia to the floor and began to frantically mash my hips into hers with bone-creaking speed."
    dal "Ngh...♥ I, aaaah... I can't stop moving my hips! Do it harder!♥"
    "*SMACK* *SCHLICK* *THWIP*"
    mc "You want it harder, slut?"
    dal "Yes♥ Yes♥! Give it to me! Give me that fat cock!"
    "The two of us fucked like amphetamine fueled rabbits, Dalia bucking her hips in time with my maniacal pace like the well-seasoned whore she was, effortlessly keeping pace with my dicking as I gave no thought to the rhythm and consistency of my strokes."
    dal "Ngh... fuh... fuh...♥"
    kat "Geez. Watching you two screw is making my hips hurt."
    mc "...ngh! ....ngh!"
    kat "You know... you might just get addicted to this and not be able to have the normal-kind of sex."
    dal "Ughhh...! Haaah... hahh...!"
    kat "No worries, though. Do as I say and you can have as much of the stuff as you want. Imagine, back-to-back-to-back orgasms whenever you want..."
    mc "Aaaaah, ngh--!"
    scene w1_1511 with flash
    play sound "sound effects/spurt.wav"
    dal "Ah, fuck fuck fuck FUCK FuCK fuuuuuuuuck...!"
    play sound "sound effects/spurt.wav"
    dal "Aah~♥ Cumming~! Haaah! Let it out...!" with flash
    play sound "sound effects/spurt.wav"
    mc "Aaaaagh, you bitch!" with flash
    scene w1HshakeReward03 with w24
    mc "Stick your ass out more!"
    play sound "sound effects/butt-slap.wav"
    scene w1HshakeReward04 with flash
    "*SMACK*"
    harp "Right--!"
    play sound "sound effects/butt-slap.wav"
    "*SMACK*" with flash
    lucy "Yes--!"
    scene w1HshakeReward05 with dissolve
    "*SHLICK* *SHLICK* *SHLICK*"
    mct "(I don't...!)"
    mct "(I don't feel like...!)"
    "*SHLICK* *SHLICK* *SHLICK*"
    mct "(I don't feel like...!)"
    scene w1_1508 with w22
    play sound "sound effects/spurt.wav"
    mc "(I don't feel like stopping!)" with flash
    play sound "sound effects/spurt.wav"
    harp "Ugghhh...! HAAAAAH...♥ AAAAAAAAAAAH!" with flash
    play sound "sound effects/spurt.wav"
    mc "(I can fuck forever!)"
    play sound "sound effects/spurt.wav"
    scene black with flash
    play sound "sound effects/spurt.wav"
    ".........!"
    play sound "sound effects/spurt.wav"
    "......!" with flash
    stop music fadeout 3.0
    play sound "sound effects/spurt.wav"
    "...!" with flash
    scene w1_1509 with wet
    mc "Nggh... {w}I'm... {w}I'm tapped out..."
    "By the end of it all, an hour had passed and I lost count of the number of times I had ejaculated."
    mct "(Six times? Seven times...?)"
    "Whatever the number, the result was me collapsed on the floor like a desiccated corpse, in an office that reeked of sex, sweat, and other bodily fluids."
    kat "Now that's the look I like to see on a man's face. Foot half-way into the door of a sex coma."
    "Finally, the boundless sexual desire in me had been quelled, replaced by a feeling of outright emptiness."
    "All form of coherence had completely left me, dulled by physical and mental exhaustion."
    "For the first time in recent memory, not a single worry filtered out through my mind and into consciousness."
    $ renpy.end_replay()
    scene black with fade
    if not persistent.gonzoRewardGallery:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.gonzoRewardGallery = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)
    "As I drifted off to sleep, one word sat firmly in my mind: {b}contentment{/b}."
    $ history_kathleen = "Mrs. Pulman's reward turned out to be a sex-fueled foursome with Dalia, Harper, and Lucy. I lost count of the number of times I came, thanks to whatever that she-devil injected me with."
    $ unread_kathleen = True
    $ history_lucy = "I learned Lucy is now working at the club as one of the regular prostitutes, thanks to some slimy back-dealing by Isaak. Guess what she endured during her audition wasn't enough to deter her from her goal of getting her son into a prestigious school."
    $ lucyProstitute = True
    $ unread_lucy = True
    $ history_dalia = "Dalia more or less played second fiddle during Mrs. Pulman's reward, where I learned just how experienced the Carnation Club's head girl actually is. "
    $ unread_dalia = True
    play sound "sound effects/notification.wav"
    show bioupdate with dissolve
    "......"
    play sound "sound effects/water-splash2.wav"
    "..."
    scene w1_1514 with wet2
    play music "music/jazz-apricot.mp3"
    mc "Ah...!"
    mct "(My body feels like lead...)"
    mct "(I've never been this physically exhausted before. I have a feeling that my back and hips will be killing me when I wake up tomorrow.)"
    mct "(I'm guessing this is one of the unique perks Dr. Chuck was eluding too. What a {b}fucking{/b} day, literally...)"
    scene w1_1515 with dissolve
    mc "Ah, man! The water feels so nice..."
    scene w1_1516 with dissolve
    kat "Mind if I join you?"
    scene w1_1517 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Tell Kathleen not at all. [gr]\[Kathleen +1\]":
                $ Kathleen_Affection += 1
                show screen textbox2 with dissolve
                mc "Not at all. After all that, there's nothing left to be shy about."
                scene w1_1518 with dissolve
                kat "{b}No{/b}, there isn't."
                scene w1_1519 with fade
                kat "You and I will be getting to know each other quite well during your tenure here."
                scene w1_1520 with dissolve
                if kat_polite == True:
                    "Despite saying that, my eyeline couldn't help but be drawn over the contours of Mrs. Pulman's fully nude form."
                else:
                    "Despite saying that, my eyeline couldn't help but be drawn over the contours of Kathleen's fully nude form."

        "Flippantly tell Kathleen she owns the place.":
            show screen textbox2 with dissolve
            mct "(After all that I was hoping for a little privacy, but...)"
            mc "Well, you own the place, so..."
            scene w1_1518 with dissolve
            kat "Partially. A small portion."
            scene w1_1519 with fade
            kat "Especially considering I'm the life-blood of the club."
            scene w1_1520 with dissolve

            if kat_polite == True:
                "Mrs. Pulman either completely missed or more likely ignored the displeasure in my voice."
                "That said, my eyeline couldn't help but be drawn over the contours of Mrs. Pulman's fully nude form as she stepped into the bath."
            else:
                "Kathleen either completely missed or more likely ignored the displeasure in my voice."
                "That said, my eyeline couldn't help but be drawn over the contours of Kathleen's fully nude form as she stepped into the bath."

    "Come to think of it, this was the first time I had seen her stark naked."
    "She was mostly clothed when she partnered with Veronica a few weeks ago, and sure, she barely left anything to the imagination with the sheer body stocking she had on just moments ago."
    scene w1_1525 with dissolve
    mc "This place has got a hundred million baths, doesn't it...?"
    scene w1_1521 with dissolve
    kat "I needed to talk to you and I also needed to clean up after your sex marathon, so two birds with one stone."
    scene w1_1524 with dissolve
    kat "It's gonna take a day to air out my office, you know."
    scene w1_1526 with dissolve
    mc "Probably should've thought of that before your sex ambush."
    scene w1_1521 with dissolve
    kat "Truth to be told, I don't really mind a little stink."
    scene w1_1525 with dissolve
    mc "What did you want to speak with me about?"
    scene w1_1524 with dissolve
    kat "Ah, straight to the point. I thought maybe all that sex would soften you up a bit."
    scene w1_1522 with dissolve
    hide screen textbox2 with dissolve
    menu:

        "Apologize and tell Kathleen you're just tired. [red]\[Toughness -2\]":
            $ toughness -=2
            scene w1_1525 with dissolve
            show screen textbox2 with dissolve
            mc "Sorry, guess I'm just a little worn out and to the point right now."
            "I decided not to voice my outrage of having been drugged against my will. It would just fall on deaf ears anyway."
            scene w1_1523 with dissolve
            kat "Worn out? Well, you certainly would be. I've never seen a man go that many times."

        "Tell Kathleen you're angry about being drugged. [gr]\[Toughness +1\] [red]\[Kathleen -1\]":
            $ toughness +=1
            $ Kathleen_Affection -= 1
            scene w1_1527 with dissolve
            show screen textbox2 with dissolve
            mc "To be frank, I didn't think I'd be drugged when I walked into the building today. I'm kinda pissed off here."
            scene w1_1523 with dissolve
            kat "Don't complain, you had your fun."
            "She simply dismissed my objection like I was being unreasonable."
            mct "(Seriously though, who the fuck knows what's in that stuff? Not to mention any potential unwanted side-effects...)"
            kat "I've never seen a man go that many times."

    kat "The new formula the old man cooked up is really something special."
    scene w1_1522 with dissolve
    "She said something that would normally invite further inquiry, but..."
    mct "(I feel like it's best I don't even know.)"
    scene w1_1525 with dissolve
    mc "Yeah, I could say there was a lot of firsts for me today..."
    scene w1_1521 with dissolve
    kat "Quite. Anyway, I need you to check up on Miss Lynch."
    scene w1_1525 with dissolve
    mc "Veronica? What's wrong?"
    scene w1_1524 with dissolve
    kat "She's fallen out of touch the past few days. She hasn't been returning my calls."
    scene w1_1525 with dissolve
    mc "You think something's wrong?"
    scene w1_1521 with dissolve
    kat "That's what I want you to find out. It's part of your job, after all."
    scene w1_1525 with dissolve
    mc "Making sure the girls are... how did Dr. Chuck put it...?"
    mc "Making sure the girls are {i}fighting fit{/i}?"
    scene w1_1524 with dissolve
    kat "That sounds like him. He has a knack for obscuring the ugly side of the business with understatement and pithy aphorisms."
    scene w1_1521 with dissolve
    kat "--but yes, it's precisely that. Go check on her well-being. Dig around. Find out if there's a problem, and if there is, remedy it in one way or another."
    scene w1_1525 with dissolve
    mc "So it's time for me to actually earn my keep?"
    scene w1_1524 with dissolve
    kat "Precisely. You have a problem with that?"
    scene w1_1522 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Tell Kathleen you honestly don't. [gr]\[Kathleen +1\] \[Toughness +1\]":
            $ Kathleen_Trust +=1
            $ toughness += 1
            scene w1_1526 with dissolve
            show screen textbox2 with dissolve
            mc "Honestly, no. The new apartment, the paycheck, the promise of tuition... it was a matter of time before the bill came due."
            mc "Plus sitting on my hands just makes me anxious. Even if the job itself isn't morally tenable, I like to feel like I'm pulling my weight."
            scene w1_1523 with dissolve
            kat "Good to hear, you're giving me confidence that you'll actually work out."


        "Tell Kathleen you aren't sure [red]\[Toughness -1\]":
            $ toughness -= 1
            scene w1_1525 with dissolve
            show screen textbox2 with dissolve
            mc "I'm not sure, to be honest. This place is still new to me."
            scene w1_1524 with dissolve
            kat "You'll do fine. I doubt you'll even have to work very hard. She's probably just being moody with tomorrow looming over her head."
            scene w1_1525 with dissolve
            mc "Or maybe she lost her phone?"
            scene w1_1521 with dissolve
            kat "Yeah, point is... just check up on her."

    kat "I'll text you the address of her gym."
    scene w1_1527 with dissolve
    mc "What if she's not there? What about her home address?"
    scene w1_1521 with dissolve
    kat "That is her home address. She lives there."
    scene w1_1525 with dissolve
    mc "Oh, I see..."
    scene w1_1524 with dissolve
    kat "Yeah, that's about where she's at mentally. That gym is the only place she has left, so use it if you have to."
    scene w1_1522 with dissolve
    mct "(Jeez, that's fucked up...)"
    scene w1_1525 with dissolve
    mc "Alright, I'll head over there as soon as I leave."
    scene w1_1521 with dissolve
    kat "Great. Tomorrow needs to go off without a hitch, and having {b}three{/b} carnations is an important part of that."
    scene w1_1528 with dissolve
    stop music fadeout 3.0
    kat "Take care of it."
    jump w1VeroPrep

label w1NoGonzoReward:

    if kat_polite == True:
        mc "(Reward aside, Mrs. Pulman mentioned having some work for me.)"
    else:
        mct "(Reward aside, Kathleen mentioned having some work for me.)"

    mct "(I should see what's that about.)"
    play sound "sound effects/ringing-outbound.mp3"
    "......"
    "..."
    stop sound
    scene player-bedroom blur with dissolve
    show kat-call with dissolve
    kat "[mcf]. Good, I'm glad you called."
    mc "You mentioned you had something for me to do?"
    kat "That's right. I need you to check up on Miss Lynch."
    mc "Veronica? What's wrong?"
    kat "She's fallen out of touch the past few days. She hasn't been returning my calls."
    mc "You think something's wrong?"
    kat "That's what I want you to find out. It's part of your job, after all."
    mc "Making sure the girls are... how did Dr. Chuck put it...?"
    mc "Making sure the girls are {i}fighting fit{/i}?"
    kat "That sounds like him. He has a knack for obscuring the ugly side of the business with understatement and pithy aphorisms."
    kat "--but yes, it's precisely that. Go check on her well-being. Dig around. Find out of if there's a problem, and if there is, remedy it in one way or another."
    mc "So it's time for me to actually earn my keep?"
    kat "Precisely. You have a problem with that?"
    hide screen textbox2 with dissolve

    menu:
        "Tell Kathleen you honestly don't. [gr]\[Kathleen +1\] \[Toughness +1\]":
            $ Kathleen_Trust +=1
            $ toughness += 1
            show screen textbox2 with dissolve
            mc "Honestly, no. The new apartment, the paycheck, the promise of tuition... it was a matter of time before the bill came due."
            mc "Plus sitting on my hands just makes me anxious. Even if the job itself isn't morally tenable, I like to feel like I'm pulling my weight."
            kat "Good to hear, you're giving me confidence that you'll actually work out."


        "Tell Kathleen you aren't sure [red]\[Toughness -1\]":
            $ toughness -= 1
            show screen textbox2 with dissolve
            mc "I'm not sure, to be honest. This place is still new to me."
            kat "You'll do fine. I doubt you'll even have to work very hard. She's probably just being moody with tomorrow looming over her head."
            mc "Or maybe she lost her phone?"
            kat "Yeah, point is... just check up on her."

    kat "I'll text you the address of her gym."
    mc "What if she's not there? What about her home address?"
    kat "That is her home address. She lives there."
    mc "Oh, I see..."
    kat "Yeah, that's about where she's at financially and mentally. That gym is her whole life and just about the only place she has left, so use it if you have to."
    mct "(Jeez, that's fucked up...)"
    mc "Alright, I'll head over there as soon as I leave."
    kat "Great. Tomorrow needs to go off without a hitch, and having {b}three{/b} carnations is an important part of that."
    kat "Take care of it. Talk to you later."
    play sound "sound effects/phonemenu.wav"
    scene w1_1358 with dissolve
    mc "Hm..."
    mct "(Veronica...)"

    jump w1VeroPrep

label w1VeroPrep:
    play music "music/lobby-time.mp3"
    scene w1_1530 with circlewipe
    "I decided the best way to approach the situation with Veronica, who I suspect will be unhappy to see me, was to go there with a secondary goal."
    "Physical fitness."
    "I checked her website, and her gym offered free walk-in consultation and personal training session for prospective members."
    "If I approach her conditionally, under the guise of personal fitness, I may get a chance to glean where her headspace is at without being pushy about it."
    "After that, I can go from there."

    if perk_strongman == True:
        mct "(Plus, I've been really letting myself go since high-school. A little exercise will do me some good.)"
    else:
        mct "(Plus, a little exercise might do me some good.)"

    if minaFlag == True:
        scene w1_1529 with pixellate
        mina "I'll have to find a new gym if I get the part. My membership for my last one ran out last week and I don't want to renew. That place is brimming with pervs."
        scene w1_1530 with dissolve
        mct "(Hmm...)"
        scene w1_1531 with dissolve
        "I recalled what Mina mentioned earlier this week and an idea formed in my head."
        mct "(Maybe I could invite her to tag along? Having a cute girl alongside me might make Veronica trust me more on an instinctual level.)"
        mct "(Jesus. Am I listening to myself? I sound like a sociopath...)"
        hide screen textbox2 with dissolve

        menu:
            "Invite Mina to the gym. [gr]\[Toughness +1\] \[Mina +2\]":
                $ toughness += 1
                $ Mina_Affection += 2
                $ minaGym = True

                show screen textbox2 with dissolve
                mct "(Well, she did say she needed a new gym and it sounds like Veronica could use the business...)"
                scene w1_1532 with dissolve

                mct "(This is me doing a good deed and bringing people together.)"
                "Definitely."
                play sound "sound effects/ringing-outbound.mp3"
                scene black with fade
                "......"
                "..."
                jump w1VeroMinaStart

            "Go to the gym by yourself. [red]\[Toughness -1\]":
                $ toughness -= 1
                scene w1_1533 with dissolve
                show screen textbox2 with dissolve
                mct  "(No, better go alone. It's club business anyway, probably shouldn't get Mina involved in it, even if it's on the peripheral.)"
                scene black with fade
                "......"
                "..."
                jump w1VeroSoloStart

    else:
        scene w1_1533 with dissolve
        mct "(I guess I'll head out now.)"
        scene black with fade
        "......."
        jump w1VeroSoloStart


label w1VeroMinaStart:
    stop sound
    stop music fadeout 3.0
    scene w1_1534 with fade
    mina "Oh, this place looks nice! It seems kinda empty, though..."
    mc "That just means more privacy when you work out."
    mina "Hmmmm.... yeah! That sounds awesome!"
    "Thankfully, Mina was free for the afternoon, and was even delighted I'd remembered what she had said in passing earlier in the week."
    "That was what I was starting to find most appealing about her. She read like an open book, genuine and quick to express happiness."

    if perk_socialButterfly == True or perk_socialChameleon == True:
        mct "(That, or it's a deliberate effort. Man, that would be tiring...)"

    play music "music/jack-the-lumberer.mp3"
    scene w1_1535 with dissolve
    ver "New faces...? Welcome to BForg--!"
    scene w1_1536 with dissolve
    ver "Oh. [mcf]."
    ver "What are {i}you{/i} doing here?"
    scene w1_1537 with dissolve
    mina "...?"
    scene w1_1538 with dissolve
    mc "I brought a friend that's looking for a gym. Know one I could recommend?"
    scene w1_1539 with dissolve
    "The wheels began to quickly turn in Veronica's head, as she looked at me, gave Mina an up and down, and finally looked back at me."
    "She was clearly wary, and I was beginning to be afraid she'd express as much, but..."
    scene w1_1540 with dissolve
    ver "It just so happens I do, as long as your pretty friend is serious about fitness and isn't looking for photo opportunities to post on the internet."
    scene w1_1541 with dissolve
    mina "You think I'm pretty?"
    scene w1_1542 with dissolve
    ver "Don't get me wrong, take as many photos as you want. It's free advertising. I just need to know you're serious about staying in shape - cause {b}clearly{/b} you already take care of yourself."
    "Veronica shot Mina another quick look up and down, but this time it was distinctly lascivious in flavor."
    scene w1_1543 with dissolve
    mc "She's very serious, aren't you Mina?"
    scene w1_1544 with dissolve
    mina "Aye aye! I don't do anything half-hearted!"
    scene w1_1545 with dissolve
    ver "Hmm, Mina is it? I'll have to take your word for it. Just know you may be singing a different tune by the end of your free consultation."
    scene w1_1546 with dissolve
    ver "Now, I assume you brought a change of clothes. Hurry up and get changed."
    ver "Changing room is that way."
    scene w1_1547 with dissolve
    mina "Aye! Aye!"
    scene w1_1548 with dissolve
    "..."
    scene w1_1549 with dissolve
    ver "Judging by the way you're dressed, you're here for a free consultation too?"
    scene w1_1550 with dissolve
    "Veronica leveled a scrutinizing gaze my way."
    hide screen textbox2 with dissolve

    menu:
        "Tell her {b}you{/b} want to get in shape. [gr]\[Veronica +2\]":
            $ Veronica_Affection += 2
            show screen textbox2 with dissolve
            mc "Well, I'd like to more proactive about my physical fitness. Could use a boost of energy too."
            scene w1_1551 with dissolve
            ver "Oh...?"
            scene w1_1552 with dissolve
            mc "It's the truth."
            scene w1_1553 with dissolve

            if perk_strongman == True:
                ver "Well, you're not bad, but you could use a little work I suppose."
            else:
                ver "Well, you {b}certainly{/b} could use it I suppose."

            scene w1_1549 with dissolve
            ver "It's the same deal as with her. You're serious about this, right?"
            scene w1_1550 with dissolve
            mc "Absolutely."

        "Tell her you're sticking around for Mina [gr]\[Veronica +1\]":
            $ Veronica_Horniness += 1
            show screen textbox2 with dissolve
            mc "I figured Mina would do better with a workout partner."
            scene w1_1549 with dissolve
            ver "That's... true enough. People are better at building good habits and a stronger work ethic when they have someone to account to."
            ver "Are you and her dating?"
            scene w1_1550 with dissolve
            mc "No. We're just friends."
            scene w1_1549 with dissolve
            ver "So you're saying she's single?"
            scene w1_1550 with dissolve
            mc "That's not at all what I'm saying, she's just not MY girlfriend. You know Killian."
            scene w1_1554 with dissolve
            ver "Him...? Oh, even better. So you're saying there's a chance for me."
            scene w1_1555 with dissolve
            "That same lascivious look returned to her face."

    scene w1_1557 with dissolve
    mct "(She seems to be feeling relatively normal...? Not that I have a baseline, but she certainly doesn't look stressed about tomorrow night.)"
    scene w1_1556 with dissolve
    ver "What are you staring for?"
    scene w1_1557 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Mention tomorrow night and see how she reacts. [red]\[Veronica -1\]":
            $ Veronica_Affection -=1
            scene w1_1558 with dissolve
            show screen textbox2 with dissolve
            mc "Just thinking you look rather composed, with the exhibition around the corner."
            scene w1_1559 with dissolve
            ver "Why would you bring that up?"
            scene w1_1560 with dissolve
            mc "It's just an honest observation. Nothing to it."
            scene w1_1561 with dissolve
            "Veronica narrowed her gaze even further."
            scene w1_1559 with dissolve
            ver "I'd appreciate it if you didn't bring the subject of {b}that{/b} place up here."
            scene w1_1561 with dissolve
            mct "(That didn't go so well, but I at least know she's touchy about the subject.)"
            mct "(Though I guess there's no surprise there.)"
            hide screen textbox2 with dissolve
            jump w1VeroPushIt

        "Deflect by apologizing and mentioning how close she is. [gr]\[Veronica +1\]":
            $ Veronica_Horniness += 1
            scene w1_1562 with dissolve
            show screen textbox2 with dissolve
            mc "Well, you're standing pretty close..."
            scene w1_1563 with dissolve
            ver "Huh...?"
            scene w1_1562 with dissolve
            mc "Just saying,  you take excellent care of yourself."
            mc "It can be hard not to get sidetracked by that occasionally."
            scene w1_1564 with dissolve
            mc "Sorry."
            scene w1_1565 with dissolve
            ver "That's okay. Looking's free I guess."
            if w1VeronicaPCUndress == True:
                ver "Not like I didn't get a {b}good{/b} look at you last Monday."
            jump w1VeroMinaExercise


    menu w1VeroPushIt:
        "{color=#FF1493}\[Social Chameleon]{/color} Express admiration and try to gain ground. [gr]\[Toughness +1\] \[Veronica +3\]" if perk_socialChameleon == True:
            $ toughness += 1
            $ Veronica_Affection += 2
            $ Veronica_Horniness += 1
            scene w1_1564 with dissolve
            show screen textbox2 with dissolve
            mc "Sorry. It's just I'm a little amazed. Most people would be visibly perturbed, but I guess you aren't like most people."
            scene w1_1562 with dissolve
            mc "You seem very strong, I admire that."
            "I decided to play to her pride here. To what end I'm not entirely sure."
            scene w1_1566 with dissolve
            ver "Damn straight, I'm not! I'm glad you recognize that, but it doesn't mean I'm going to go any easier on you today."
            mc "I wouldn't dream of it."

        "Just drop it and get to the exercise.":
            show screen textbox2 with dissolve
            if kat_polite == True:
                mct "(Best not to push her here. It's a subject she doesn't want to talk about. I'll wait for a better opportunity to figure out why she hasn't been returning Mrs. Pulman's calls.)"
            else:
                mct "(Best not to push her here. It's a subject she doesn't want to talk about. I'll wait for a better opportunity to figure out why she hasn't been returning Kathleen's calls.)"

        "{color=#696969}\[Social Chameleon] Express admiration and try to gain ground.{/color}" if perk_socialChameleon == False:
            jump w1VeroPushIt

label w1VeroMinaExercise:

    scene w1_1567 with dissolve
    mina "Alright, I'm ready to rock~!"
    scene w1_1568 with dissolve
    ver "I'd say you are..."
    scene w1_1569 with dissolve
    "Again, Veronica held her gaze a little too long while giving her appraisal."
    scene w1_1570 with dissolve
    mina "So what's the deal?"
    scene w1_1571 with dissolve
    ver "Prospective members get a free consultation and personal training session, so we can get to know each other better."
    scene w1_1572 with dissolve
    mina "We can't just sign up?"
    scene w1_1573 with dissolve
    ver "I believe a gym and its members should have a special relationship. As the owner, it's my duty to feel new members out and make sure everything fits."
    ver "I couldn't in good conscience take your money if you're not serious about working out."
    mct "(Maybe that's one of the reasons this place is failing?)"
    scene w1_1574 with dissolve
    mina "That's SO awesome!"
    ver "I-it is?"
    scene w1_1575 with dissolve
    mina "Hell yeah! I can tell how serious you take your work. You're so cool!"
    scene w1_1576 with dissolve
    ver "I, uh..."
    mct "(Is she... blushing?)"
    scene w1_1577 with dissolve
    ver "I think you might just have the right attitude for this place."
    "She may just be more easily handled than I originally suspected..."
    mct "(Then again, Mina might just be a special case.)"
    scene w1_1578 with dissolve
    ver "[mcf], on the other hand, remains to be seen."
    scene w1_1579 with dissolve
    stop music fadeout 3.0
    mina "We won't let you down, General!"
    scene w1_1580 with fade
    "We started with some simple and not-so-simple stretches."
    "I started with a basic back extension, while Veronica pushed Mina toward a more hands-on partner stretch."
    ver "That's perfect, Mina. We're going to do 30 seconds per side."
    mct "(I swear she's a dirty old man in the body of a beautiful amazon...)"
    scene w1_1581 with dissolve
    play music "music/swagger.mp3"
    ver "Good, good. You've got good form. Did you do gymnastics growing up?"
    scene w1_1582 with dissolve
    mina "Nope! I did do a little dance though. Some tumbling too, but I {i}blossomed{/i} a little too strongly to keep at it seriously. Things started getting in the way."
    scene w1_1581 with dissolve
    ver "Those things cause a lot of problems, don't they?"
    scene w1_1583 with dissolve
    mina "Eheheh, a little..."
    scene w1_1584 with dissolve
    "To be honest, I was pretty content just watching the pair of them stretch and Veronica seemed to be having a good time."
    scene w1_1585 with dissolve
    mina "I love your muscles! You've got strong hands!"
    scene w1_1586 with dissolve
    ver "Thank you. It took a ton of hard work."
    scene w1_1587 with dissolve
    mina "I can tell! I'm actually a little envious."
    scene w1_1586 with dissolve
    ver "Why? You're adorable."
    scene w1_1588 with dissolve
    mina "Yeah, but you're SO cool! Like a... a movie star!"
    scene w1_1586 with dissolve
    ver "Flip."
    scene w1_1589 with dissolve
    "Mina's natural exuberance seemed to have fully disarmed the thorny woman."
    mct "(Good call with inviting her, [mcf].)"
    "I patted myself on the back."
    mct"(Maybe I should ask her to come over? See if we can become a little friendlier?)"
    "Then again, maybe she'd be more content stretching with Mina."
    hide screen textbox2 with dissolve

    menu:
        "Ask Veronica for some help stretching. [gr]\[Veronica +3\]":
            $ Veronica_Horniness += 1
            $ Veronica_Affection += 2

            scene w1_1590 with dissolve
            show screen textbox2 with dissolve
            mc "Teacher, could I get a hand over here?"
            scene w1_1591 with dissolve
            ver "Don't call me that."
            scene w1_1592 with dissolve
            ver "Do some passive stretching, Mina."
            scene black with fade
            mc "You want me like THIS...?"
            scene w1_1593 with dissolve
            ver "Exactly like that. All you got to do is stand there and let me do all the work, {b}errand boy{/b}."
            mc "Errand boy?"
            ver "That is what you are, right? That's your job, for the club."
            ver "So, just stand there and take it. All you have to do is keep your foot firmly planted."
            "She's... enjoying this."
            scene w1_1594 with dissolve
            "Grabbing my hips, Veronica began to slowly pull on my pelvis, stretching out my legs and spin."
            scene w1_1595 with dissolve
            ver "This position suits you."
            scene w1_1596 with dissolve
            mc "You sexual harass all your members?"
            scene w1_1595 with dissolve
            ver "Never. I was just flirting with Mina. No harm in that."
            scene w1_1596 with dissolve
            mc "And all the innuendo with me, just now?"
            scene w1_1595 with dissolve
            ver "I don't know what you're talking about, errand boy."
            scene w1_1597 with irisout
            mina "Uh..."
            mina "...the heck?"

        "Just enjoy the show [gr]\[Veronica +2\] \[MinaBi +1\]":
            $ Veronica_Horniness += 2
            $ Mina_BiCurious += 1
            show screen textbox2 with dissolve
            "I think I'll just let Veronica enjoy herself. She's clearly into Mina."
            scene w1_1598 with dissolve
            "Veronica positioned herself behind Mina and took both of her arms in hand."
            ver "I'm just going to need you to hold this, while I put pressure on your hips and chest, alright?"
            mina "S-sure, I can do that!"
            scene w1_1599 with dissolve
            mina "Ehe..."
            mina "Kinda..."
            scene w1_1600 with dissolve
            mina "....mh."
            ver "Is something the matter, Mina?"
            mina "No..."
            scene w1_1601 with dissolve
            "I could see from here that Mina was blushing."
            mct "(Is she being... conscientious of the pose?)"
            scene w1_1602 with dissolve
            ver "Minutes up."
            scene w1_1603 with dissolve
            mina "...o-oh? Already...?"

    stop music fadeout 3.0
    scene w1_1604 with circlewipe
    ver "Alright... stretching's done."
    scene w1_1605 with dissolve
    play music "music/jack-the-lumberer.mp3"
    ver "Normally a consultation would involve discussion of nutrition and tailoring a workout to your specific needs, but..."
    scene w1_1606 with dissolve
    ver "Let's just shred some muscle!"
    scene w1_1607 with dissolve
    mina "Uh, [mcf]... she looks..."
    mc "Evil."
    scene w1_1608 with cmet
    mc "Ghh...!"
    ver "Good, {b}good{/b}! Like that. Allow your elbows to follow the line to the top range."
    mina "Oooh, that looks fun!"
    scene w1_1609 with cmet
    mina "*huff...!* *huff...!* Nggyeeeeh!"
    ver "I got you. Just hold that pose as long as you can."
    scene w1_1610 with cmet
    ver "Don't try to bite off more than you can chew. There's nothing wrong with using as few discs as necessary!"
    scene w1_1611 with cmet
    mct "(Ugh...! I... I want to...)"
    stop music fadeout 3.0
    scene w1_1612 with w20
    mina "I've... I've *huff* *huff* I've never..."
    scene w1_1613 with dissolve
    mina "I want to diiiiiie!"
    mc "Nghhhhhh...."
    "I couldn't find the energy to form a reply."
    scene w1_1614 with dissolve
    ver "You two did great. You can freely call yourselves members here, if you want."
    mina "Uggh..."
    scene w1_1615 with dissolve
    ver "Aw, don't give me that look. We'll come up with a more flexible regimen for you two."
    ver "Going this hard every day would just damage your body. It'd do more harm than good."
    scene w1_1616 with dissolve
    "With great effort, and a couple of false starts, Mina dragged herself into a standing position."
    scene w1_1617 with dissolve
    mina "Thank you. This place is so much cooler than my last gym!"
    scene w1_1618 with dissolve
    ver "You two go shower and I'll get the contract."
    jump w1VeroExhibitionTalkMina

label w1VeroSoloStart:

    stop music fadeout 3.0
    scene w1_1619 with dissolve
    mct "(Hmm... this is a pretty nice place. However, considering I'm the only one here)"
    "Veronica's gym comprised an entire floor of a down-town office building"
    mct "(The rent is probably what's killing her.)"
    play music "music/jack-the-lumberer.mp3"
    scene w1_1620 with dissolve
    ver "Greetings! Welcome--"
    scene w1_1621 with dissolve
    ver "Oh. It's you."
    ver "What are you doing here?"
    scene w1_1622 with dissolve
    "Veronica fixed a circumspect look my way."
    scene w1_1623 with dissolve
    mc "Well, this is a gym. I'm in my workout clothes..."
    scene w1_1624 with dissolve
    ver "There's a lot of gyms in the city, but you walk into mine?"
    scene w1_1625 with dissolve
    "Naturally, Veronica was suspicious of me being here. Not that I could blame her, considering club business was indeed what brought me here in the first place."
    hide screen textbox2 with dissolve

    menu w1VeroConvince:
        "{color=#FF1493}\[Social Chameleon]{/color} Play shamelessly to Veronica's ego. [gr]\[Veronica +2\]" if perk_socialChameleon == True:
            $ Veronica_Affection += 1
            $ Veronica_Horniness += 1
            scene w1_1626 with dissolve
            show screen textbox2 with dissolve
            mc "I understand this might be weird, considering how we're acquainted, buuuuuut..."
            scene w1_1627 with dissolve
            mc "Look at me! I could use some time in the gym."
            scene w1_1626 with dissolve
            mc "Sure, I could go to any other gym, but I've got a pretty good reason to choose this one."
            scene w1_1624 with dissolve
            ver "And what's that?"
            scene w1_1629 with dissolve
            mc "You look amazing! Why would I want to go anywhere else?"
            scene w1_1630 with dissolve
            ver "..."
            scene w1_1631 with dissolve
            mc "{b}Seriously!{/b} I looked you up! A podium finish at the Olympics eight years ago in shot putting."
            scene w1_1630 with dissolve
            "That piece of information was actually gleaned from the dossier I received on all the Carnations, but saying that outright would be weird."
            scene w1_1629 with dissolve
            mc "You haven't competed since, but to keep a body like yours takes a lot of blood, sweat, and tears."
            scene w1_1632 with dissolve
            ver "Damn right it does."
            scene w1_1633 with dissolve
            mc "Well {b}fuck{/b} franchise gyms. All they do is take your money. They don't give a shit about what their members do after that."
            scene w1_1634 with dissolve
            mc "I'd  rather be a part of a gym owned by a {b}person like you{/b}, who actually cares."
            scene w1_1635 with dissolve
            ver "...you're REALLY here because you want to get in shape?"
            scene w1_1636 with dissolve
            mc "I am."
            "I wasn't strictly telling a lie."
            "Keeping my head in a book for over three years had softened me up. Not to mention the boost of energy from being healthier will be useful once I'm a resident physician."
            mc "I could definitely use it."
            scene w1_1637 with dissolve

            if w1VeronicaPCUndress == True:
                ver "Hmm.... I suppose you do. I did get a {b}good{/b} look at you last Monday after all. With some bulking up, you might just transition from cute to handsome."
            else:
                "No kidding. You're built like one of those inflatable flailing arm men."
                mct "(...gh!)" with hpunch

            scene w1_1639 with dissolve
            ver "I don't see the harm in giving you a consultation. Everyone needs exercise in their life."
            ver "It's not like I'm in any position to be turning down the business either. That said, I will if you don't meet my #1 rule."
            scene w1_1638 with dissolve


        "Express to Veronica a genuine interest in your physical health. [gr]\[Veronica +2\]":
            $ Veronica_Affection += 2
            scene w1_1626 with dissolve
            show screen textbox2 with dissolve
            mc "I know it's kinda weird, considering how we're acquainted, but..."
            scene w1_1624 with dissolve
            ver "That's a BIG understatement."
            scene w1_1626 with dissolve
            mc "I'd like to take my health more seriously and get in shape."
            scene w1_1625 with dissolve
            "I wasn't strictly telling a lie."
            "Keeping my head in a book for over three years had softened me up. Not to mention the boost of energy from being healthier will be useful once I'm a resident physician."
            scene w1_1624 with dissolve
            ver "You can do that anywhere."
            scene w1_1626 with dissolve
            mc "True, but..."
            scene w1_1640 with dissolve
            mc "You got a lot of strict membership requirements on your website. I think that's really cool."
            mc "You're clearly care about the physical fitness of your customers, which you won't get that at a franchise gym."
            scene w1_1641 with dissolve
            ver "No, you wouldn't. Those places are {b}soulless{/b}."
            scene w1_1642 with dissolve
            mc "That was my line of thinking as well."
            scene w1_1644 with dissolve
            ver "I don't see the harm in giving you a consultation. Everyone needs exercise in their life, no matter where they may work."

            if w1VeronicaPCUndress == True:
                scene w1_1646 with dissolve
                ver "Plus, I did get a real {b}good{/b} look at you last Monday after all. With some bulking up, you might just transition from cute to handsome."
            scene w1_1644 with dissolve
            ver "It's not like I'm in any position to be turning down the business either. That said, I will if you don't meet my #1 rule."
            scene w1_1645 with dissolve


        "{color=#696969}\[Social Chameleon] Play to Veronica's ego.{/color}." if perk_socialChameleon == False:
            jump w1VeroConvince

    mc "What's the number one rule?"
    scene w1_1643 with dissolve
    ver "I refuse to take anyone's money who's not committed to their physical health journey."
    scene w1_1644 with dissolve
    ver "So here's the deal: prospective members get a free consultation and personal training session, so we can get to know each other better."
    scene w1_1643 with dissolve
    ver "I believe a gym and its members should have a special relationship. As the gym's owner, it's my duty to feel new members out and make sure everything fits."
    scene w1_1645 with dissolve
    mct "(I have a feeling that's one of the reasons this place is failing...)"
    scene w1_1644 with dissolve
    ver "Is that acceptable to you?"
    scene w1_1645 with dissolve
    mc "It is. As you can see, I came ready."
    scene w1_1646 with dissolve
    ver "I'm going to wipe that smile off your face."
    scene w1_1647 with fade
    "We started with some simple, hands-on partner stretches."
    ver "We're going to do 30 seconds per side."
    mc "Alright."
    scene w1_1648 with dissolve
    ver "You have any experience with stretching?"

    if perk_strongman == True:
        scene w1_1649 with dissolve
        mc "Soccer stretches. Quads, calfs, hamstrings, lower back stuff..."
        mc "I played in high-school."
        scene w1_1648 with dissolve
        ver "Good, then you already know the importance of stretching before you exercise."
    else:
        scene w1_1649 with dissolve
        mc "Uh, just whatever we did in gym class."
        scene w1_1648 with dissolve
        ver "Well, you want to always stretch the main muscle group you plan on working. It decreases the risk for injury by increasing your flexibility."
        scene w1_1649 with dissolve
        mc "Makes sense."

    scene w1_1650 with dissolve
    ver "This is known as a supine hamstring stretch. Normally you'd stretch by yourself, but this gives a chance to get my hands on what we're working with."
    scene w1_1651 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Tell Veronica you wouldn't mind this being an every day thing. [red]\[Veronica -2\]":
            $ Veronica_Affection -= 1
            $ Veronica_Horniness -= 1
            scene w1_1652 with dissolve
            show screen textbox2 with dissolve
            mc "We could do this every session. If you want."
            scene w1_1653 with dissolve
            mc "---ng! Hey!"
            "Veronica put a little more force into the stretch."
            scene w1_1654 with dissolve
            mc "Message received."

        "Ask Veronica what she thinks. [gr]\[Veronica +1\]":
            scene w1_1655 with dissolve
            show screen textbox2 with dissolve
            mc "Well, what do you think?"
            scene w1_1656 with dissolve
            if perk_strongman == True:
                $ Veronica_Horniness += 2
                ver "I think you've got some deceptively dense muscle mass in your legs. No surprise there, given what you just said."
            else:
                $ Veronica_Horniness += 1
                ver "I think I have my work cut out for me."

    scene w1_1657 with dissolve
    mct "(With the way we're casually talking, she seems to be feeling relatively normal...? Not that I have a baseline, but she certainly doesn't look stressed about tomorrow night.)"
    scene w1_1659 with dissolve
    ver "Oi! You're losing focus!"
    scene w1_1658 with dissolve
    mc "Oh, sorry. It's just..."
    hide screen textbox2 with dissolve
    menu:
        "Mention tomorrow night and see how she reacts. [red]\[Veronica -1\]":
            $ Veronica_Affection -=1
            show screen textbox2 with dissolve
            mc "Just thinking you look rather composed, with the exhibition around the corner."
            scene w1_1660 with dissolve
            ver "Why would you bring that up?"
            scene w1_1661 with dissolve
            mc "It's just an honest observation. Nothing to it."
            "Veronica peered down at me with a scrutinizing gaze."
            scene w1_1660 with dissolve
            ver "I'd appreciate it if you didn't bring the subject of {b}that{/b} place up here."
            scene w1_1661 with dissolve
            mc "Sorry. I just know I wouldn't be able to focus on my job if I were you."
            scene w1_1660 with dissolve
            ver "Well, I'm {b}not{/b} you. I'm good at compartmentalizing."


        "Deflect by apologizing and saying you're feeling flustered. [gr]\[Veronica +1\]":
            $ Veronica_Horniness += 1
            show screen textbox2 with dissolve
            mc "Well, all this touching..."
            scene w1_1662 with dissolve
            ver "Huh...?"
            scene w1_1663 with dissolve
            mc "Just saying, you got your hands on me and you take excellent care of yourself too."
            mc "It can be hard not to get sidetracked."
            mc "It was accident. I'll try to keep better focus! Sorry!"
            scene w1_1662 with dissolve
            ver "It happens to all of us. God knows that I..."
            scene w1_1664 with dissolve
            ver "What I'm saying that's a normal reaction for people not used to working out in a gym"
            ver "Y'know, lotta sweat. Lotta half-clothed, muscular bodies. Eventually you get used to it, or you just work yourself so hard that you can't even think."


    scene w1_1665 with dissolve
    ver "That's 30 seconds.."
    scene w1_1666 with dissolve
    "Signaling that the stretching was over, Veronica peered down at me with what might be mistaken for a malicious look."
    scene w1_1667 with dissolve
    "Let's see what you're made of, errand boy."
    scene black with fade
    mc "(Errand boy...?)"
    scene w1_1668 with cmet
    mc "Mmmh...."
    scene w1_1669 with dissolve
    ver "Good, good. You got it."
    scene w1_1670 with dissolve
    ver "Keep your chin up and your chest high."
    scene w1_1674 with dissolve
    mc "Okay..."
    scene w1_1670 with dissolve
    ver "Stomach braced and stomach down"
    scene w1_1674 with dissolve
    mc "Three...!"
    scene w1_1672 with dissolve
    ver "This is what's known as an isolateral bench press."
    scene w1_1673 with dissolve
    ver "What it's doing is working your chest and shoulders, your pectoralis major and your..."
    scene w1_1671 with dissolve
    mc "Anterior deltoid. Yeah, I know."
    scene w1_1669 with dissolve
    ver "Good, so you know the names of things?"
    scene w1_1671 with dissolve
    mc "I know a little bit anatomy."
    scene w1_1673 with dissolve
    ver "Watch it. Don't get distracted."
    scene w1_1672 with dissolve
    ver "Your elbow should follow the line of the handle to top range."
    scene w1_1674 with dissolve
    mc "Right! Sorry, coach."
    scene w1_1670 with dissolve
    "With that the prattle ceased and I found myself falling into a rhythm."
    scene w1_1669 with dissolve
    mct "(Follow the line of the handle to top range....)"
    scene w1_1670 with dissolve
    mct "(Control the back down.)"
    scene w1_1669 with dissolve
    mct "(Follow the line of the handle to top range....)"
    scene w1_1670 with dissolve
    mct "(Control the back down.)"
    scene w1_1669 with dissolve
    "Slowly, but surely I began to feel the strain."
    "My muscles began to feel the burn, requiring more oxygen from the body."
    scene w1_1675 with dissolve
    mc "*huff* *huff*"
    stop music
    play sound "sound effects/metal-drop.wav"
    scene w1_1676 with hpunch
    man "Annng--fUUUUUCK!!!!!!"
    scene w1_1677 with w12
    ver "Markus...?"
    "A pained cry cut my workout short."
    mark "GOD DAMN IT!"
    scene w1_1678 with fade
    play music "music/beginning-of-conflict.mp3"
    ver "What's wrong?"
    mark "I don't know. S-something popped!"
    ver "You dislocated your shoulder?"
    mark "I d-don't know! Yes?!"
    scene w1_1679 with dissolve
    ver "Get on the floor and I'll pop it back--"
    scene w1_1680 with dissolve
    mc "Don't do that. Leave it alone."
    scene w1_1681 with dissolve
    mark "Why the hell not? This hurts like a bitch, kid."
    scene w1_1682 with dissolve
    mc "Because you might make it worse."
    mc "Just haphazardly popping it back in place can result in blood vessel, ligament, or nerve damage."
    mc "You don't want to cause any more damage and have Markus sue you, do you?"
    scene w1_1683 with dissolve
    ver "...eh?"
    mc "Let me take a look."
    scene w1_1684 with dissolve
    mark "Eegh!"
    scene w1_1685 with dissolve
    mc "Stop being a baby."
    scene w1_1686 with dissolve
    mc "Hmmm..."
    scene w1_1687 with dissolve
    mc "It's a good thing you didn't try and pop it back into place. This isn't a dislocation. It's a tear."
    mc "All you would've accomplished is a lot more pain and screaming."
    scene w1_1688 with dissolve
    ver "How do you know that?"
    scene w1_1689 with dissolve
    mc "If you dislocated you shoulder, you'd be unable to move it."
    mc "They'd also be an indentation here, below the shoulder. Instead..."
    scene w1_1690 with dissolve
    mark "Ngg--!"
    scene w1_1689 with dissolve
    mc "The top of his shoulder is all jacked up."
    scene w1_1692 with dissolve
    mark "W-what the hell does that mean?"
    scene w1_1691 with dissolve
    stop music fadeout 3.0
    mc "It means you've separated it. You've damaged the ligaments around your acromioclavicular joint."
    mc "Pretty bad too. Your shoulder blade and collar bone are totally detached from each other. Yeesh!"
    mc "Something this severe isn't something that just abruptly happens either. You were working out with an injury."
    scene w1_1693 with dissolve
    ver "Ah, you dumbass!"
    mark "Ehehe, it was just a little pain..."
    scene w1_1691 with dissolve
    mc "*sigh* Pain is your body telling you something is wrong. You're going to need to go get this x-rayed."
    scene w1_1694 with dissolve
    ver "I  guess I'll call you a cab?"
    mark "Ehehe... please do, Miss Lynch."
    jump w1VeroExhibitionTalkSolo

label w1VeroExhibitionTalkMina:
    play music "music/study-and-relax.mp3"
    scene w1_1695 with circlewipe
    $ history_mina = "I remembered Mina mentioning over lunch that she was looking for a new gym, so I invited her along to Veronica's gym. We both ended up members there and Veronica seemed quite taken by her."
    $ unread_mina = True
    play sound "sound effects/notification.wav"
    show bioupdate with dissolve
    "After filling out the membership form and getting our dues squared away, Mina and I parted ways."
    "Meanwhile, I stuck around the gym. After all, I hadn't fully settled my primary purpose for being here."
    scene w1_1696 with dissolve
    ver "Your friend is a sweet girl. Does she know what her boyfriend does for a living?"
    scene w1_1697 with dissolve
    mc "Not at all."
    scene w1_1696 with dissolve
    ver "Ah, tough luck. I suppose a girl's got to make a few mistakes though."
    scene w1_1698 with dissolve
    mc "Speaking from experience?"
    scene w1_1701 with dissolve
    ver "Where else would I be speaking from?"
    scene w1_1700 with dissolve
    mc "Fair enough. I guess that was a stupid question."
    scene w1_1703 with dissolve
    ver "You surprised me today. Truth be told, I didn't think you had it in you, errand boy."
    ver "The two of you lasted the whole consultation and showed a promising attitude. Good job."
    scene w1_1702 with dissolve
    mc "That's good, cause my legs feel like jello."
    scene w1_1706 with dissolve
    ver "Enjoy it! That's the feeling of hard work!"
    jump w1VeroExhibitionTalk


label w1VeroExhibitionTalkSolo:

    $ Veronica_Affection += 5
    play music "music/study-and-relax.mp3"
    scene w1_1696 with circlewipe
    ver "Shit. I'm actually a little impressed, errand boy."
    scene w1_1695 with dissolve
    "After seeing the injured gym rat off, I stuck around. After all, I hadn't fully settled my primary purpose for being here."
    scene w1_1698 with dissolve
    mc "Errand boy?"
    scene w1_1696 with dissolve
    ver "That's your job, right? That's what you do for that crazy old bat."
    scene w1_1699 with dissolve
    mc "Eheh, I suppose that's not {b}inaccurate{/b}."
    scene w1_1701 with dissolve
    ver "How do you know all that stuff about shoulder injuries."
    scene w1_1700 with dissolve
    mc "Like I said, I know a little bit of anatomy..."
    scene w1_1704 with dissolve
    ver "...?"
    "The fiery redhead looked at me curiously, not satisfied with my vague answer."
    mc "I'm studying for the MCATs next year."
    scene w1_1705 with dissolve
    ver "What's that?"
    scene w1_1704 with dissolve
    mc "It's a test, the medical college admission--"
    scene w1_1701 with dissolve
    ver "Oh. Doctor college. Gotcha."
    scene w1_1703 with dissolve
    ver "Well, as I was saying, that was pretty cool what you did back there. When I was training for the olympics, I saw a teammate set another shot putter's arm back in place."
    ver "Had no clue that could do any harm. I about jumped out of my skin when you mentioned being sued."
    scene w1_1702 with dissolve
    mc "So, how did my consultation go?"
    scene w1_1701 with dissolve
    ver "Hmm, I didn't really get a chance to see your commitment, but I think in this case..."
    scene w1_1706 with dissolve
    ver "I'll take your word for it."
    jump w1VeroExhibitionTalk


label w1VeroExhibitionTalk:

    scene w1_1707 with dissolve
    mc "By the way, Mrs. Pulman is concerned you haven't been in contact since last Monday."
    scene w1_1708 with dissolve
    ver "*sigh* Here I was just finding talking to you pleasant."
    scene w1_1709 with dissolve

    if toughness >=18:
        mc "It's part of my job to ask."
    else:
        mc "Sorry, but this is part of my job."

    scene w1_1708 with dissolve
    ver "Is she worried I'm going to bail on her sick little game?"
    scene w1_1709 with dissolve
    mc "You've hit the nail on the head pretty much."
    scene w1_1710 with dissolve
    "Veronica narrowed her gaze, looking past me as if she was searching for a suitable response."
    scene w1_1711 with dissolve
    ver "I'd be full of it if I said I wasn't dreading tomorrow, but she doesn't have to worry about me flaking."
    ver "After the shit I endured a couple of weeks ago, I'm not going to let all of that be for nothing."
    scene w1_1712 with dissolve
    mct "(That's a sunk cost fallacy, buuuuut I probably shouldn't mention that to Veronica...)"
    scene w1_1709 with dissolve
    mc "So you'll be there tomorrow night?"
    scene w1_1708 with dissolve
    ver "Duh."
    scene w1_1713 with dissolve
    ver "You see this, errand boy?"
    scene w1_1714 with dissolve
    mc "An empty gym?"
    scene w1_1715 with dissolve
    ver "Not quite. It's my fucking dream. I'm not going to get into it, but some shit's really been working against me lately."
    ver "I'm going to fight tooth and nail to keep this place afloat."
    scene w1_1716 with dissolve
    "An overbearing feeling of purpose was written on the amazon's face."
    "For a moment, I didn't quite know how to respond, stricken by her determination. Eventually I found the words to get back to the point."
    scene w1_1717 with dissolve
    mc "Then why haven't you returned Mrs. Pulman's calls? Only asking, because... she'll want to know."
    scene w1_1718 with dissolve
    ver "Hmm... let's see. Tons of reasons, but the most relevant one..."
    ver "Talking to her will piss me off and life's too short to be in a bad mood."
    scene w1_1719 with dissolve
    mc "Heh, fair enough."
    scene w1_1720 with dissolve
    mct "(Not like I blame her.)"
    "Furthermore, I believed what she was saying and could confidently tell the boss she doesn't have to worry about Veronica being a no-show for tomorrow's inaugural exhibition."
    scene w1_1721 with dissolve

    if minaGym == True:
        ver "You didn't bust your ass today just so you could ask me that simple question, did you?"
    else:
        ver "You didn't just join my gym so you could ask me that simple question, did you?"


    scene w1_1719 with dissolve
    mc "It was part of it. I was honest about needing to find a place to work out, but I'd be lying if I didn't have an additional motive for coming here today."
    scene w1_1722 with dissolve
    ver "That's so stupid!"
    ver "You could have just asked me, but here you are saddled with a gym membership! I'm not going to let you slack off either!"
    scene w1_1719 with dissolve
    mc "No offense, but you're a difficult and scary woman. You probably would've told me to fuck off if I opened with that."
    scene w1_1723 with dissolve
    play sound "sound effects/slap2.wav"
    ver "Most likely!" with hpunch
    mc "--geh?!"
    "Veronica slapped my arm with startling force, breaking the near silence of the now completely empty gym."
    scene w1_1724 with dissolve
    ver "You're alright in my book."

    if minaGym == True:
        ver "You brought a cute new girl to my gym after all."
    else:
        ver "It'd be nice to have a {i}doctor{/i} around the place."
        mc "I'm not a..."

    scene w1_1725 with dissolve
    ver "I'm going to expect you here at least a few times a week, to work on your fitness goals."
    scene w1_1726 with dissolve
    ver "Don't worry! I'll help you develop a personal fitness plan suitable for a skinny errand boy!"
    scene w1_1727 with dissolve
    stop music fadeout 3.0
    mct "(Gee, thanks...)"
    scene black with fade
    if minaGym == False:
        $ history_veronica = "Turns out Mrs. Pulman had nothing to worry about. Veronica is just as determined to win the exhibition as she was two weeks ago. I ended up getting a gym membership out of the equation and she seemed pretty impressed by me recognizing what was wrong with her idiot member."
    else:
        $ history_veronica = "Turns out Mrs. Pulman had nothing to worry about. Veronica is just as determined to win the exhibition as she was two weeks ago. Bringing Mina worked like a charm. She seemed really into her."
    $ unread_veronica = True
    play sound "sound effects/notification.wav"
    show bioupdate with dissolve
    "......"
    "..."

label june05End:

    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionveronica01 with blinds
    $ renpy.pause(6, hard=True)
    $ date = "june05night"
    play sound "sound effects/shower.wav"
    scene w1_1728 with fade
    show screen textbox2 with dissolve
    show screen qmenu with dissolve
    mct "(It's already Friday night, huh? That mean's tomorrow is...)"
    scene w1_1729 with dissolve
    show june05night with squares
    mct "(The innaguration night of the summer exhibition.)"
    mct "(I've already been given a taste of what to expect. It'll be like a couple of weeks ago, but on a grander scale.)"
    mct "(More patrons. Higher stakes. Both of which probably means a higher degree of cruelty.)"
    stop sound
    play music "music/leaving-home.mp3"
    scene pr0979 with pixellate
    if kat_polite == True:
        "I remembered the video footage Mrs. Pulman handed me my first week at the club."
    else:
        "I remembered the video footage Kathleen handed me my first week at the club."

    "The one that was conspicuously titled {i}Week 3 - public use.{/i}."
    scene w1_1731 with Dissolve(1.0)
    "The content of which was exactly as billed, featuring an excess of non-stop sexual indulgence that lasted hours on end."

    scene w1_1732 with dissolve
    if kat_polite == True:
        mct "(I'm going to stand on that stage and partake in whatever fucked up designs Mrs. Pulman has in store.)"
    else:
        mct "(I'm going to stand on that stage and partake in whatever fucked up designs Kathleen has in store.)"

    mct "(I wonder how the girls are feeling right about now? Nervous? Terrified...?)"
    "My mind turned to the three women whose well-being I'm purportedly supposed to look after."

    scene w1_1733 with fade
    "Felicia. A vivacious woman who says she's in it for the kicks."
    scene w1_1744 with pixellate
    "A bombshell I spent an evening with getting to know."

    if prAfterParty == False:
        scene w1_1745 with dissolve
        "Pretty intimately."
        scene w1_1746 with dissolve
        "Which lead to discussing the ugly under pinnings of romance over offensively greasy food."

    if prAfterParty == True:
        scene w1_1747 with dissolve
        "Played games with."

        if feliciaSex == True:
            scene w1_1748 with dissolve
            "Became intimate with."

    if w1FelGonzo == True:
        scene w1_1749 with dissolve
        "Got to know more personally than I really had any right to."

    if feliciaFlag == True:
        scene w1_1750 with dissolve
        "Who I later went on to have dinner with this week."

    scene w1_1733 with pixellate
    "I wonder what's in store for her? Will she get what she's after? Will she find the thrills she's looking for?"
    mct "(I have a feeling she'll come to regret it.)"
    scene w1_1734 with fade
    "Then there's Rosalind. Sweet, warm, caught between a rock-and-a-hard-place Rosalind."
    scene w1_1751 with pixellate
    "A woman that was dangled in front of me like bait."

    if roseTakeAdvantage == True:
        scene w1_1752 with dissolve
        "Which I lecherously accepted."

    if roseTakeAdvantage == False:
        scene w1_1753 with dissolve
        "A woman I inadvertently blathered my anxieties too, who listened to me with a motherly-like patience."

    if roseSeduceFlag == True:
        scene w1_1754 with dissolve
        "Who, for a reason I didn't understand at the time, tried to seduce me over coffee."

    if w1RoseGonzo == True:
        scene w1_1755 with dissolve
        "Who I pried intimate details from."

    if roseSeduceFlag == True:
        scene w1_1756 with dissolve
        "A woman whose amorous advances turned out to be a ploy, born of a bleak situation."

    if roseFlag == True:
        scene w1_1757 with dissolve
        "A ploy I let myself fall victim to."

    scene w1_1734 with pixellate
    "Unlike Felicia, she has something on the line here."
    "What will happen to her if she doesn't win? What will happen to her if she does?"
    "Even if she squares away one debt, she'll have accrued a liability of a different nature."
    scene w1_1735 with fade
    "The last on the chopping block: Veronica."
    "What a soldier."
    scene w1_1758 with pixellate
    "Paraded in front of me for that old hag's amusement."
    if prVero_Facial == True:
        scene w1_1759 with dissolve
        mct "(Eheh...)"
    scene w1_1760 with dissolve
    "Who endured a long, arduous night to just participate in tomorrow's game."
    scene w1_1761 with dissolve
    "Who at least found some satisfaction I suppose."
    scene w1_1762 with dissolve
    mct "(Is four walls and a bunch of over-engineered equipment really worth all this?)"
    scene w1_1729 with pixellate
    "I had no right to look down on these women."
    scene w1_1730 with dissolve
    "After all, what was I doing here?"
    stop music fadeout 3.0
    scene black with fade
    "......"
    "..."
    play music "music/cello-suite-No-1-G-Major-Prelude.mp3"
    scene w1_1737 with curtains
    if w1GonzoReward == True:
        kat "I had occasion to test out the new formula before tomorrow night."
        man "How did you find it?"
        scene w1_1736 with dissolve
        kat "You've really outdone yourself, Sir."


    else:
        kat "The testing for the new formula will begin tomorrow night."
        man "I look forward to seeing the results."
        scene w1_1736 with dissolve
        kat "As do I."

    man "I wish the board had a tenth of enthusiasm for my project as you do, young lady. All they see is in this project is a stimulant."
    man "Can you imagine? Turning such a wonderful philter into an energy drink? Bah! They lack the imagination you have."
    scene w1_1738 with dissolve
    kat "Fortunately for me, the world is full of fools and men of limited vision and initiative."
    scene w1_1739 with dissolve
    man "Men like your partners?"
    scene w1_1740 with dissolve
    kat "Oh, Abel. You said it, not me."
    scene w1_1739 with dissolve
    abel "They have any objections to our partnership?"
    scene w1_1738 with dissolve
    kat "No, I haven't told them. I don't plan to."
    scene w1_1741 with dissolve
    abel "That may bite you in your delectable ass if you're not careful, Kat."
    scene w1_1742 with dissolve
    kat "It's best they don't know what our goals are. August is nothing but a gangster, all he understands is money and ego. And Charles..."
    kat "For all his brilliance, is a child. He wouldn't be happy with his sacred playground being tainted by outside interests."
    scene w1_1743 with dissolve
    kat "{b}No{/}, this is our deal."
    kat "I'll get you the data you need."
    stop music
    play sound "sound effects/sting-mumbaieffect.wav"
    scene black with fade
    "........."
    "......"
    "..."
    jump June06Start



















































################################################################################
## START HERE, GIL -------------------------------------------------------------
################################################################################
################################################################################
## STOP HERE, GIL --------------------------------------------------------------
################################################################################
