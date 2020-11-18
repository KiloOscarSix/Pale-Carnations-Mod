###                               PALE CARNATIONS                            ###
################################################################################
################################################################################


## The contents of day 6 and 7 of the first week go here.



## Edwin wakes up --------------------------------------------------------------

label June06Start:
    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionhousegirls with blinds
    $ renpy.pause(6, hard=True)
    $ date = "june06day"

    scene w1_1765 with sunshine
    show screen textbox2 with dissolve
    show screen qmenu with dissolve
    play music "music/lobby-time.mp3"
    mct "(Can it be...?)"
    scene w1_1766 with dissolve
    mct "(Did I just...)"
    scene w1_1767 with dissolve
    show june06day with squares
    "Get a whole night of quality, uninterrupted shut eye?"
    mct "(No Killian bursting in with a booty call in the middle of the night or an unannounced visitor buzzing at my door?)"
    scene w1_1768 with dissolve
    play sound "sound effects/phonemenu.wav"
    mct "(Yep.)"
    mct "(It's just too bad that...)"
    scene w1_1769 with fade
    mc "Eugh..."

    if w1GonzoReward == True:
        "Between my \"reward\" and working out at Veronica's gym yesterday, my body feels like it's operating on a 3 second delay."
    else:
        "The workout I did yesterday has caught up to me."

    "Still, my mind is amazingly..."
    scene w1_1770 with dissolve
    "Settled."
    mct "(All that thinking last night helped put things into perspective. I'm not the one who's going to have a hard time tonight.)"
    mct "(I should do something for the girls. Some kind of gesture of goodwill so they won't feel so alone.)"
    mct "(Hmm... yeah. I might just end up looking like a jackass, but I think my heart is in the right place.)"
    stop music fadeout 3.0
    scene black with fade
    "Plus, this falls within the purview of my new job, doesn't it?"

## Carnation Meeting #1 --------------------------------------------------------

    scene w1_1771 with circlewipe
    mc "You're all here. Great."
    scene w1_1772 with dissolve
    play music "music/hep-cats.mp3"
    mc "Thanks for accepting my invitation."
    scene w1_1773 with dissolve
    ver "Invitation? You said this had to do with tonight. Did I have a choice?"
    ver "This place was out of my way."
    scene w1_1774 with dissolve
    mc "I thought it'd be nice if we all grabbed lunch together before the exhibition."
    "I did my best to deliver the line with a warm smile."
    scene w1_1775 with dissolve
    ver "Huh? You what?"
    scene w1_1776 with dissolve
    rose "Yeah, I thought this was important. I had to call the sitter to come a little earlier. Thankfully, she was available."
    scene w1_1777 with dissolve
    mct "(Ah, crap...)"
    scene w1_1778 with dissolve
    fel "Aw, c'mon girls."
    scene w1_1779 with dissolve
    fel "I'm sure [mcf] has his reasons."
    scene w1_1780 with dissolve
    fel "...uh, right?"
    scene w1_1781 with dissolve
    "With all three looking at me expectantly, I was starting to feel more than a little stupid for calling them here for such an ostensibly flimsy reason."
    "I should..."
    hide screen textbox2 with dissolve

    menu:
        "Just be honest with them and speak from the heart. [gr]\[Rosalind +1\] [red]\[Toughness -1\]":
            $ toughness -= 1
            $ Rosalind_Affection += 1
            scene w1_1782 with dissolve
            show screen textbox2 with dissolve
            mc "It's exactly what I said. I thought it'd be nice if we all grabbed lunch together."
            scene w1_1785 with dissolve
            ver "You gotta be kidding me..."
            scene w1_1787 with wipeleft
            mc "Well, there is a little more behind it than that..."
            scene w1_1788 with dissolve
            fel "Tell us, [mcf]."
            scene w1_1789 with dissolve
            mc "My mom once told me that sitting down and sharing a meal with another person is an excellent first step in becoming friends."
            mc "Food is something everyone has in common, so it's a good place to start in bridging the gap between two parties."
            scene w1_1783 with dissolve
            rose "What gap are you trying to bridge...?"
            scene w1_1784 with dissolve
            mc "The one that exists between the three of you as competitors."
            ver "What are you babbling about?"


        "Remind them of the relationship dynamic at play here first. [red]\[Veronica -1\] [gr]\[Felicia +1\] \[Toughness +2\]":
            $ toughness += 2
            $ Felicia_Affection += 1
            $ Veronica_Affection -= 1

            scene w1_1790 with dissolve
            show screen textbox2 with dissolve
            mc "You're in my charge over the next month."

            if toughness >= 20:
                mc "I don't give a shit if it's out of the way or if you have to pay your babysitter a little more."
                mc "If I tell you to get your ass somewhere, {b}you get your ass somewhere{/b}."
            else:
                mc "I don't care if it's out of the way or if you have to pay your babysitter a little more."
                mc "If I tell you to show up somewhere, {b}you show up somewhere{/b}."

            mc "Your time over the next month belongs exclusively to me."
            scene w1_1785 with dissolve
            ver "Oh? Is this what this is all about? You're having a power trip?"
            scene w1_1786 with dissolve
            mc "No, this is about it being my job to get the three of you through the month, of making sure of your {b}well-being{/b}."
            mc "To that end, we need to bridge the gap between the three of you. As competitors."
            scene w1_1785 with dissolve
            ver "What the hell are you talking about?"

    scene w1_1791 with dissolve
    mc "Let me put it this way. You guys are stepping into a quagmire over the next four weeks, facing down a heap of nastiness. To make things even more excruciating, it's going to feel like you're facing it alone."
    mc "That is because the three of you are competitors and only one of you can win the exhibition. Naturally, you want to see each other fail, because an opponent's loss is your gain."
    mc "To add to this, everyone at the club will want to see you writhe and suffer. They're counting on and looking forward to it."
    scene w1_1792 with dissolve
    ver "Yeah, and...?"
    scene w1_1793 with dissolve
    mc "What I'm trying to say is... you guys should rely on each other over the next month, because when you get down to it, no one else will be your friend."
    scene w1_1794 with dissolve
    fel "Not even you, [mcf]?"
    scene w1_1795 with dissolve
    mc "I work there, remember? Even if I care about you three, which I do I might add, they're paying me a lot of money to {i}handle{/i} you."
    scene w1_1796 with dissolve
    rose "Is that what you're doing by telling us this? Handling us?"
    scene w1_1791 with dissolve
    mc "I'm trying to help you by telling you what you need to hear."
    scene w1_1792 with dissolve
    ver "And what makes you think any of us needs to hear this?"
    scene w1_1793 with dissolve
    mc "You guys are going to be continually worn down over the next month and when you're under the stage lights, sweating your asses off, stressed and shaking like a cornered rabbit..."
    mc "Being able to rely on each other might just make a difference in getting through the night."
    scene w1_1797 with dissolve
    rose "This isn't something I want to hear just hours before we're supposed to be at the club."
    scene w1_1798 with dissolve
    mc "I know, but I thought this was important to talk about."
    mc "What I'm ultimately getting at is... look after each other. You'll find no help anywhere else tonight."
    mc "Even if you three are competitors, you shouldn't be enemies. I hope you can see the wisdom in having a shoulder to lean should you need it, because the moment you lose your wits and your resolve falters, your chances of winning plummets along with it."
    scene w1_1788 with dissolve
    fel "So we're going to share a meal and become best friends?"
    scene w1_1789 with dissolve
    mc "No, of course not. It's something though."
    mc "We're going to meet up every Saturday before the exhibition. No exceptions."
    scene w1_1799 with dissolve
    ver "........."
    scene w1_1800 with dissolve
    rose "......"
    scene w1_1801 with dissolve
    fel "..."
    scene w1_1802 with dissolve
    fel "That sounds great, [mcf]. Seriously."
    ver "It makes... {b}some{/b} sense. I guess."

    if roseFlag == True:
        scene w1_1803 with dissolve
        rose "I'm glad you're in our corner, Mr. [mcl]."
    else:
        scene w1_1804 with dissolve
        rose "..."

    scene w1_1805 with dissolve
    fel "Let's eat!"
    scene black with fade
    "......"
    "..."
    scene w1_1806 with fade
    play sound "sound effects/phonemenu.wav"
    fel "Awwww, she's adorable! She's got your eyes!"
    scene w1_1807 with dissolve
    ver "I want see."
    "At the start of our meal, conversation was sparse and awkward, but by the end of it, the girls seemed to be warming to each other."
    scene w1_1808 with dissolve
    ver "Felicia's right, she's a cutie pie."
    scene w1_1809 with dissolve
    ver "You want see, [mcf]?"
    mc "Sure."
    scene w1_1810 with dissolve
    if roseSeduceFlag == True:
        mct "(So this is Rosalind's daughter...)"
        mct "(The one she's doing all this for.)"
    mc "Felicia wasn't kidding. She really does have your eyes."
    scene w1_1811 with dissolve
    rose "What about you two? You have any kids...?"
    scene w1_1812 with dissolve
    fel "I got two stepsons. What about you, Big Red?"
    scene w1_1813 with dissolve
    ver "Don't call me that and... no, it never happened for me."

    if perk_socialButterfly == True or perk_socialChameleon == True:
        "Veronica's attitude took a noticeable dip at being redirected that question."
        "Must be a prickly topic for her."

    scene w1_1814 with dissolve
    fel "Still time, maybe one of the guys at the club tonight will be nice enou--"
    scene w1_1815 with dissolve
    rose "Those kind of jokes aren't funny, Felicia."

    if perk_socialButterfly == True or perk_socialChameleon == True:
        "Rosalind quickly jumped in to cut Felicia's bad joke off. She must've picked up on the same change of mood I did."
    else:
        "Rosalind quickly jumped in to cut Felicia's bad joke off."

    scene w1_1816 with dissolve
    fel "Sorry. Sometimes I fire off my mouth before my brain catches up."
    "It seems Felicia was quick to catch on as well."
    ver "That's okay. I run my mouth too much as well."
    scene w1_1817 with dissolve
    fel "You should share something about yourself, [mcf]."
    scene w1_1818 with dissolve
    mc "I should?"
    scene w1_1819 with dissolve
    rose "Yeah, it's not fair for you to be the only one not sharing. Tell us what you were like as a child."
    scene w1_1820 with dissolve
    ver "Hmmph, I bet he was a brat."
    scene w1_1821 with dissolve
    fel "How about something embarrassing?"
    scene w1_1822 with dissolve
    mct "(Hmm...)"
    scene w1_1823 with dissolve
    mc "Okay, fair's fair."
    stop music fadeout 3.0

    if trait_inquisitive == True:
        jump w1InquisitiveStory
    if trait_tireless == True:
        jump w1TirelessStory
    if trait_governor == True:
        jump w1GovernorStory

label w1InquisitiveStory:

    scene w1_1824 with dissolve
    mc "What I was like as a child, eh...?"
    scene w1_1825 with dissolve
    play music "music/sneaky-snitch.mp3"
    "In the interest of building trust, I decided to speak at length about my intense curiosity streak growing up."
    scene w1_1826 with dissolve
    mc "I was a very curious and inquisitive child when I was young. Still am to some degree I guess, but it doesn't get me in the same kind of trouble it used to."
    scene w1_1827 with dissolve
    rose "What kind of trouble is that?"
    scene w1_1828 with dissolve
    mc "Usually, it had me taking things apart and failing to put it back together. Other times, it had me pushing people's buttons to discover what was and wasn't acceptable behavior."
    scene w1_1829 with dissolve
    rose "Sounds precocious."
    scene w1_1830 with dissolve
    mc "That's just another word for pain in the ass. My mother will attest to that."

    if history_firestarter == True:
        scene w1_1837 with pixellate
        mc "The biggest example was my penchant for starting fires when I was kid. I had such a keen interest in watching things burn for some reason."
        rose "Oh, no."
        fel "Oh yeah! That was one of the few things Ian told me about you that ended up being true."
        mc "It started out with just smaller items. Plastic cups, shoeboxes, old toys that I thought I was too cool to play with anymore."
        scene w1_1838 with dissolve
        mc "It wasn't something I could easily hide from my mother. I don't know if it was because as a child if I simply didn't have the presence of mind to hide my misdeeds or if I simply didn't care, but.."
        mc "One way or another, either through a new burn or ashes on my clothes, she'd always give me a stern lecture about the dangers of what I was doing."
        ver "She should've whipped your ass with a belt."
        mc "That's not my mother."
        scene w1_1839 with dissolve
        mc "Anyway, naturally I got more daring and wanted to try something bigger. Large."
        mc "Maybe something belonging to a neighbor who always gave my mother a hard time about how the grass looked."
        scene w1_1840 with dissolve
        rose "You didn't--"
        ver "Burn down his house?"
        mc "Oh, no. No, no, no... nothing {i}that{/i} extreme..."
        scene w1_1841 with dissolve
        play ambient "sound effects/fire.wav"
        mc "I {b}DID{/b} burn down a wooden gardening shed of his though... without it occurring me that it would likely be full of nasty fire accelerants..."
        scene w1_1842 with dissolve
        stop ambient fadeout 3.0
        stop music fadeout 3.0
        "A frown spread across the collectively faces of everyone listening."
        scene w1_1843 with dissolve
        mc "So, yeah. All the sirens, the giant plume of black smoke... our tiny neighborhood hasn't had anything as exciting happen since."
        scene w1_1844 with dissolve
        ver "You can't just stop it there. What happened to you?"
        scene w1_1843 with dissolve
        mc "An investigation happened, police got involved, I was discovered. There was talks of negligence on my mother's part, but nothing really came of it."
        mc "Just property damage she wasn't really in a good position to pay back comfortably and..."

    elif history_voyeur == True:
        mc "The worst example of my curiosity getting the better of me was my burgeoning interest in the opposite sex."
        scene w1_1845 with dissolve
        fel "That doesn't seem so bad. Growing boys get curious, what'd you do? Peep a little?"
        scene w1_1846 with dissolve
        mc "A little? No. Not a little. Try a whole lot."
        scene w1_1847 with dissolve
        ver "You were a little pervert!"
        scene w1_1845 with dissolve
        fel "What, you get caught one day?"
        scene w1_1848 with dissolve
        mc "You could say that, but a more accurate description would be I got caught taking {i}secret{/i} photos."
        scene w1_1849 with dissolve
        ver "You were a HUGE pervert!"
        scene w1_1850 with dissolve
        fel "Oh yeah! That was one of the few things Ian told me about you that ended up being true."
        fel "You can't just leave it at that! You've got to give us the details."
        scene w1_1848 with dissolve
        mc "I guess I'll start at the beginning."
        scene w1_1827 with dissolve
        rose "Please do."
        scene w1_1828 with dissolve
        "Rosalind seemed strangely as curious about the details as Felicia did."
        scene w1_1851 with pixellate
        mc "It started out innocent enough. Just like Felicia said, my curiosity got the better of me one day, and I ended up peeping on a neighborhood boy's mom while she was changing."
        mc "Deviant, but probably within the periphery of {i}boys-will-be-boys{/i} behavior."
        ver "How did you go from that to taking peep shots?"
        scene w1_1863 with dissolve
        mc "It was a gradual process, built up over a couple of years. Like I said, I started out peeping every now and then, through cracks in doors. Through outside windows..."
        mc "Only when the opportunity presented itself when playing with the neighborhood kids. I didn't exactly seek it out in the beginning, but my taste for it gradually grew."
        ver "How can you possibly speak so plainly about this?"
        mc "Well, this was about... {b}a decade ago{/b}?"
        scene w1_1831 with dissolve
        ver "Still!"
        scene w1_1832 with dissolve
        mc "It's also less embarrassing to tell you three, considering our relationship and what I've seen you guys do. Specifically you, Veronica. Like with that Gob--"
        scene w1_1861 with dissolve
        ver "You were saying your taste for it gradually grew?"
        scene w1_1862 with dissolve
        mc "That's right. Human memory is not so great and I begun to want a more tangible reminder of my newfound hobby."
        scene w1_1864 with dissolve
        mc "So I started taking pictures and cataloguing all the neighborhood MILFs, sometimes using the flimsiest of excuses to be at their house. I showed Ian one day and he couldn't keep his mouth shut about it, so word got out."
        fel "And that's how you got caught?"
        mc "No. That's how I started {b}selling them{/b}."
        scene w1_1852 with dissolve
        rose "Oh my gosh! YOU SOLD THEM?!" with vpunch
        scene w1_1865 with dissolve
        mc "Yeah... in hindsight, it was pretty fucked up on multiple levels. I eventually got caught of course. It was an enterprising idea, but you can't really expect a group of boys to keep their mouths shut."
        scene w1_1866 with dissolve
        stop music fadeout 3.0
        ver "You can't just stop it there. What happened to you?"
        scene w1_1867 with dissolve
        mc "An investigation happened, police got involved. Nothing really came of it surprisingly, besides the backlash in the neighborhood and some therapy my mom wasn't exactly in a good place to pay for."
        mc "My mother faced a lot of scorn and outright animosity around the neighborhood after that. It eventually died down, but..."

    elif history_stickyFingers == True:
        mc "The worst example of me testing the waters of what I could get away with was when I defrauded a school fundraiser."
        scene w1_1831 with dissolve
        ver "Wait, how old were you?"
        scene w1_1832 with dissolve
        mc "This was a about a decade ago, so about 12."
        scene w1_1850 with dissolve
        fel "Oh yeah! That was one of the few things Ian told me about you that ended up being true."
        scene w1_1868 with dissolve
        rose "How does a 12 year old even think to do that?"
        scene w1_1869 with dissolve
        mc "I don't know. It seemed like such an easy way to make money for some video games and I was curious if it'd work."
        scene w1_1874 with dissolve
        ver "What did you do exactly?"
        scene w1_1870 with pixellate
        mc "You see, the school was selling boxes of some expensive, yet-nondescript chocolate bars."
        mc "I saw an opportunity to make some money there."
        mc "No one really pays attention to what they order from a fundraiser, right? They usually just order a box or two out of obligation without paying attention to any of the details."
        scene w1_1871 with dissolve
        mc "So what I did was take the orders placed by my neighbors and my mom's co-workers and used a third of what they gave me to buy a cheaper, discounted candy bar."
        ver "That doesn't sound very smart."
        mc "It wasn't. For the reasons you'd probably expect. Sure most people didn't notice, but you only need a couple to before the game is up."
        rose "What happened after that?"
        scene w1_1865 with dissolve
        stop music fadeout 3.0
        mc "An investigation happened. The school got involved, police got involved... it was a whole thing."
        scene w1_1867 with dissolve
        mc "At first, they thought it was my mother's doing. I came clean pretty quick when I realized that, but they didn't immediately believe me."
        mc "Ultimately, nothing really came of it. My mother reimbursed what I spent from the funds out of her own pocket and gritted through the shame and gossip around the neighborhood and her workplace."
        mc "Then there was the..."

    jump w1DinerConclusion

label w1TirelessStory:

    scene w1_1824 with dissolve
    mc "What I was like as a child, eh...?"
    scene w1_1825 with dissolve
    "I decided to speak at length about the boundless energy I had as a child, in interest of building trust."
    scene w1_1826 with dissolve
    play music "music/sneaky-snitch.mp3"
    mc "Well, I was an active kid. Not really hyper, but I could never tolerate a moment of inactivity or boredom. Still do to some degree, but I've got better outlets for it now."
    mc "At any rate, it often found me getting into trouble."
    scene w1_1827 with dissolve
    rose "That sounds normal."
    scene w1_1828 with dissolve
    mc "For the most part, it was. I got into the trouble a young boy typically would. Neighborhood scraps or creating disturbances at school."
    scene w1_1829 with dissolve
    rose "Yeah, that's normal."
    scene w1_1830 with dissolve
    mc "It manifested in some nasty ways too though, my mother will attest to that."
    scene w1_1831 with dissolve
    ver "What kind of nastiness can a kid get up to?"
    scene w1_1832 with dissolve
    mc "You'd be surprised..."

    if history_firestarter == True:
        scene w1_1837 with pixellate
        mc "The biggest example was my penchant for starting fires when I was kid. It was a good outlet from the boredom."
        rose "Oh, no."
        fel "Oh yeah! That was one of the few things Ian told me about you that ended up being true."
        mc "It started out with just smaller items. Plastic cups, shoeboxes, old toys that I thought I was too cool to play with anymore."
        scene w1_1838 with dissolve
        mc "It wasn't something I could easily hide from my mother. I don't know if it was because as a child if I simply didn't have the presence of mind to hide my misdeeds or if I simply didn't care, but.."
        mc "One way or another, either through a new burn or ashes on my clothes, she'd always give me a stern lecture about the dangers of what I was doing."
        ver "She should've whipped your ass with a belt."
        mc "That's not my mother."
        scene w1_1839 with dissolve
        mc "Anyway, naturally I got more daring and wanted to try something bigger. Large."
        mc "Maybe something belonging to a neighbor who always gave my mother a hard time about how the grass looked."
        scene w1_1840 with dissolve
        rose "You didn't...?"
        ver "Burn down his house?"
        mc "Oh, no. No, no, no... nothing {i}that{/i} extreme..."
        scene w1_1841 with dissolve
        play ambient "sound effects/fire.wav"
        mc "I {b}DID{/b} maybe burn down a wooden gardening shed of his though... without it occurring me that it would likely be full of nasty fire accelerants..."
        scene w1_1842 with dissolve
        stop ambient fadeout 3.0
        stop music fadeout 3.0
        "A frown spread across the collectively faces of everyone listening."
        scene w1_1843 with dissolve
        mc "So, yeah. All the sirens, the giant plume of black smoke... our tiny neighborhood hasn't had anything as exciting happen since."
        scene w1_1844 with dissolve
        ver "You can't just stop it there. What happened to you?"
        scene w1_1843 with dissolve
        mc "An investigation happened, police got involved, I was discovered. There was talks of negligence on my mother's part, but nothing really came of it."
        mc "Just property damage she wasn't really in a good position to pay back comfortably and..."

    elif history_voyeur == True:
        mc "The worst example was when all that excess energy and need for stimulation combined with my burgeoning interest in the opposite sex."
        scene w1_1845 with dissolve
        fel "That doesn't seem so bad. Growing boys get curious, what'd you do? Peep a little?"
        scene w1_1846 with dissolve
        mc "A little? No. Not a little. Try a whole lot."
        scene w1_1847 with dissolve
        ver "You were a little pervert!"
        scene w1_1845 with dissolve
        fel "What, you get caught one day?"
        scene w1_1848 with dissolve
        mc "You could say that, but a more accurate description would be I got caught taking {i}secret{/i} photos."
        scene w1_1849 with dissolve
        ver "You were a HUGE pervert!"
        scene w1_1850 with dissolve
        fel "Oh yeah! That was one of the few things Ian told me about you that ended up being true."
        fel "You can't just leave it at that, though! You've got to give us the details."
        scene w1_1848 with dissolve
        mc "Fine, fine. I guess I'll start at the beginning."
        scene w1_1827 with dissolve
        rose "Please do."
        scene w1_1828 with dissolve
        "Rosalind seemed strangely as curious about the details as Felicia did."
        scene w1_1851 with pixellate
        mc "It started out innocent enough. Just like Felicia said, my hormones got the better of me one day, and I ended up peeping on a neighborhood boy's mom while she was changing."
        mc "Deviant, but probably within the periphery of {i}boys-will-be-boys{/i} behavior."
        ver "How did you go from that to taking peep shots?"
        scene w1_1863 with dissolve
        mc "It was a gradual process, built up over a couple of years. Like I said, I started out peeping every now and then, through cracks in doors. Through outside windows..."
        mc "Only when the opportunity presented itself when playing with the neighborhood kids. I didn't exactly seek it out in the beginning, but my taste for it gradually grew."
        ver "How can you possibly speak so plainly about this?"
        mc "Well, this was about... {b}a decade ago{/b}?"
        scene w1_1831 with dissolve
        ver "Still!"
        scene w1_1832 with dissolve
        mc "It's also less embarrassing to tell you three, considering our relationship and what I've seen you guys do. Specifically you, Veronica. Like with that Gob--"
        scene w1_1861 with dissolve
        ver "You were saying your taste for it gradually grew?"
        scene w1_1862 with dissolve
        mc "That's right. Human memory is not so great and I begun to want a more tangible reminder of my new found hobby."
        scene w1_1864 with dissolve
        mc "So I started taking pictures and cataloguing all the neighborhood MILFs, sometimes using the flimsiest of excuses to be at their house. I showed Ian one day and he couldn't keep his mouth shut about it, so word got out."
        fel "And that's how you got caught?"
        mc "No. That's how I started {b}selling them{/b}."
        scene w1_1852 with dissolve
        rose "Oh my gosh! YOU SOLD THEM?!" with hpunch
        scene w1_1865 with dissolve
        mc "Yeah... in hindsight, it was pretty fucked up on multiple levels. I eventually got caught of course. It was an enterprising idea, but you can't really expect a group of boys to keep their mouths shut."
        scene w1_1866 with dissolve
        ver "You can't just stop it there. What happened to you?"
        scene w1_1867 with dissolve
        stop music fadeout 3.0
        mc "An investigation happened, police got involved. Nothing really came of it surprisingly, besides the backlash in the neighborhood and some therapy my mom wasn't exactly in a good place to pay for."
        mc "My mother faced a lot of scorn and outright animosity around the neighborhood after that. It eventually died down, but..."

    elif history_stickyFingers == True:
        mc "The worst example of my endless search of stimulation was when I defrauded a school fundraiser for the fun of it."
        scene w1_1831 with dissolve
        ver "Wait, how old were you?"
        scene w1_1832 with dissolve
        mc "This was a about a decade ago, so about 12."
        scene w1_1850 with dissolve
        fel "Oh yeah! That was one of the few things Ian told me about you that ended up being true."
        scene w1_1868 with dissolve
        rose "How does a 12 year old even think to do that?"
        scene w1_1869 with dissolve
        mc "I don't know. It seemed like such an easy way to make money for some video games and I was curious if it'd work."
        scene w1_1874 with dissolve
        ver "What did you do exactly?"
        scene w1_1870 with pixellate
        mc "You see, the school was selling boxes of some expensive, yet-nondescript chocolate bars."
        mc "I saw an opportunity to make some money there."
        mc "No one really pays attention to what they order from a fundraiser, right? They usually just order a box or two out of obligation without paying attention to any of the details."
        scene w1_1871 with dissolve
        mc "So what I did was take the orders placed by my neighbors and my mom's co-workers and used a third of what they gave me to buy a cheaper, discounted candy bar."
        ver "That doesn't sound very smart."
        mc "It wasn't. For the reasons you'd probably expect. Sure most people didn't notice, but you only need a couple to before the game is up."
        rose "What happened after that?"
        scene w1_1865 with dissolve
        stop music fadeout 3.0
        mc "An investigation happened. The school got involved, police got involved... it was a whole thing."
        scene w1_1867 with dissolve
        mc "At first, they thought it was my mother's doing. I came clean pretty quick when I realized that, but they didn't immediately believe me."
        mc "Ultimately, nothing really came of it. My mother reimbursed what I spent from the funds out of her own pocket and gritted through the shame and gossip around the neighborhood and her workplace."
        mc "Then there was the..."

    jump w1DinerConclusion

label w1GovernorStory:
    scene w1_1824 with dissolve
    mc "What I was like as a child, eh...?"
    scene w1_1825 with dissolve
    "I decided to speak at length about the anger I felt as a child, in interest of building trust."
    scene w1_1826 with dissolve
    play music "music/sneaky-snitch.mp3"
    mc "I was an angry kid growing up."
    scene w1_1831 with dissolve
    ver "What did you have to be angry about?"
    scene w1_1832 with dissolve
    mc "My father died when I was very young. That was when it started."
    scene w1_1833 with dissolve
    mc "I'd look at the other kids in the neighborhood and they'd have dads and it felt unfair."
    scene w1_1834 with dissolve
    rose "Oh, I'm so sorry."
    scene w1_1835 with dissolve
    fel "Me too.."
    scene w1_1836 with dissolve
    mc "That's okay. Don't be."
    mc "As I was saying, I was an angry kid and that caused me to act out in some nasty ways."
    scene w1_1831 with dissolve
    ver "What kind of nastiness can a kid get up to?"
    scene w1_1832 with dissolve
    mc "You'd be surprised..."

    if history_firestarter == True:
        scene w1_1837 with pixellate
        mc "The biggest example was my penchant for starting fires when I was kid. It was a good outlet for my anger."
        rose "Oh, no."
        fel "Oh yeah! That was one of the few things Ian told me about you that ended up being true."
        mc "It started out with just smaller items. Plastic cups, shoeboxes, old toys that I thought I was too cool to play with anymore."
        scene w1_1838 with dissolve
        mc "It wasn't something I could easily hide from my mother. I don't know if it was because as a child if I simply didn't have the presence of mind to hide my misdeeds or if I simply didn't care, but.."
        mc "One way or another, either through a new burn or ashes on my clothes, she'd always give me a stern lecture about the dangers of what I was doing."
        ver "She should've whipped your ass out with a belt."
        mc "That's not my mother."
        scene w1_1839 with dissolve
        mc "Anyway, naturally I got more daring and wanted to try something bigger. Large."
        mc "Maybe something belonging to a neighbor who always gave my mother a hard time about how the grass looked. The bastard."
        scene w1_1840 with dissolve
        rose "You didn't...?"
        ver "Burn down his house?"
        mc "Oh, no. No, no, no... nothing {i}that{/i} extreme..."
        scene w1_1841 with dissolve
        play ambient "sound effects/fire.wav"
        mc "I {b}DID{/b} maybe burn down a wooden gardening shed of his though... without it occurring me that it would likely be full of nasty fire accelerants..."
        scene w1_1842 with dissolve
        stop ambient fadeout 3.0
        stop music fadeout 3.0
        "A frown spread across the collectively faces of everyone listening."
        scene w1_1843 with dissolve
        mc "So, yeah. All the sirens, the giant plume of black smoke... our tiny neighborhood hasn't had anything as exciting happen since."
        scene w1_1844 with dissolve
        ver "You can't just stop it there. What happened to you?"
        scene w1_1843 with dissolve
        stop music fadeout 3.0
        mc "An investigation happened, police got involved, I was discovered. There was talks of negligence on my mother's part, but nothing really came of it."
        mc "Just property damage she wasn't really in a good position to pay back comfortably and..."

    if history_voyeur == True:
        scene w1_1853 with dissolve
        mc "The worst example was when all that anger combined with my burgeoning interest in the opposite sex."
        scene w1_1854 with dissolve
        fel "That sounds... bad."
        scene w1_1855 with dissolve
        mc "It was. The neighborhood was filled with a lot of pretty moms. Pretty moms who talked shit about my mother behind her back."
        scene w1_1856 with dissolve
        rose "Why did they gossip about your mother?"
        scene w1_1857 with dissolve
        mc "Who knows, but those two things caused a plan to hatch in my head."
        mc "I was going to humiliate them without them ever knowing."
        scene w1_1858 with dissolve
        ver "I'm almost afraid to ask, but how did you plan to do that?"
        scene w1_1859 with dissolve
        mc "I started a side business selling {i}stolen{/i} photos, so to speak."
        scene w1_1856 with dissolve
        rose "Stolen?"
        scene w1_1857 with dissolve
        mc "Peep shots."
        scene w1_1860 with dissolve
        ver "Oh! You were a little pervert!"
        scene w1_1850 with dissolve
        fel "Oh yeah! That was one of the few things Ian told me about you that ended up being true."
        fel "You can't just leave it at that, though! You've got to give us the details."
        scene w1_1851 with pixellate
        mc "I always had even the flimsiest excuse to be at the neighbors house. Once there, I simply waited for the opportunity to sneakily take some photos with my phone."
        ver "How can you possibly speak so plainly about this?"
        mc "Well, this was about... {b}a decade ago{/b}?"
        scene w1_1831 with dissolve
        ver "Still!"
        scene w1_1832 with dissolve
        mc "It's also less embarrassing to tell you three, considering our relationship and what I've seen you guys do. Specifically you, Veronica. Like with that Gob--"
        scene w1_1861 with dissolve
        ver "You were saying your waited for the opportunity?"
        scene w1_1862 with dissolve
        mc "That's right. I got pretty good at it."
        scene w1_1863 with dissolve
        mc "Anyway, so I started taking pictures and cataloguing all the neighborhood MILFs. Once I had enough, I opened up shop and spread them around."
        ver "That couldn't have lasted long."
        mc "Yeah, it didn't. Naturally a bunch of boys can't keep their mouths shut about something like that, but that wasn't the point. Ultimately, I just wanted to take those haughty bitches down a peg."
        scene w1_1865 with dissolve
        mc "In hindsight, it was pretty fucked up on multiple levels. "
        scene w1_1866 with dissolve
        ver "You can't just stop it there. What happened to you?"
        scene w1_1867 with dissolve
        stop music fadeout 3.0
        mc "An investigation happened, police got involved. Nothing really came of it surprisingly, besides the backlash in the neighborhood and some therapy my mom wasn't exactly in a good place to pay for."
        mc "My mother faced a lot of scorn and outright animosity around the neighborhood after that. It eventually died down, but..."

    if history_stickyFingers == True:
        mc "The worst example of me acting out was when I defrauded a school fundraiser."
        scene w1_1831 with dissolve
        ver "Wait, how old were you?"
        scene w1_1832 with dissolve
        mc "This was a about a decade ago, so about 12."
        scene w1_1850 with dissolve
        fel "Oh yeah! That was one of the few things Ian told me about you that ended up being true."
        scene w1_1868 with dissolve
        rose "How does a 12 year old even think to do that?"
        scene w1_1869 with dissolve
        mc "I don't know. It seemed like such an easy way to make money for some video games."
        scene w1_1874 with dissolve
        ver "What did you do exactly?"
        scene w1_1870 with pixellate
        mc "You see, the school was selling boxes of some expensive, yet-nondescript chocolate bars."
        mc "I saw an opportunity to make some money there."
        mc "No one really pays attention to what they order from a fundraiser, right? They usually just order a box or two out of obligation without paying attention to any of the details."
        scene w1_1871 with dissolve
        mc "So what I did was take the orders placed by my neighbors and my mom's co-workers and used a third of what they gave me to buy a cheaper, discounted candy bar."
        ver "That doesn't sound very smart."
        mc "It wasn't. For the reasons you'd probably expect. Sure most people didn't notice, but you only need a couple to before the game is up."
        rose "What happened after that?"
        scene w1_1865 with dissolve
        stop music fadeout 3.0
        mc "An investigation happened. The school got involved, police got involved... it was a whole thing."
        scene w1_1867 with dissolve
        mc "At first, they thought it was my mother's doing. I came clean pretty quick when I realized that, but they didn't immediately believe me."
        mc "Ultimately, nothing really came of it. My mother reimbursed what I spent from the funds out of her own pocket and gritted through the shame and gossip around the neighborhood and her workplace."
        mc "Then there was the..."

    jump w1DinerConclusion

label w1DinerConclusion:

    scene w1_1872 with dissolve
    vic "*Sob* *Sob* I'm sorry... you shouldn't see me..."
    scene w1_1873 with dissolve
    vic "I just wish your father..."
    "I remembered my mother breaking down from the stress I had piled on her, face wrought with such a pronounced loneliness that even a stupid kid like me could understand it."
    mct "I {b}did{/b} that to her. In that instance, her misery was my doing. My kind, smiling mother....)"
    scene w1_1875 with dissolve
    mc "...heartbreak."
    scene w1_1876 with dissolve
    ver "..."
    scene w1_1877 with dissolve
    rose "..."
    scene w1_1878 with dissolve
    fel "..."
    scene w1_1879 with dissolve
    play music "music/crinoline-dreams.mp3"
    fel "Hey..."
    fel "You were a kid."
    scene w1_1880 with dissolve
    mc "Yeah, it's in the past."
    scene w1_1881 with dissolve
    ver "Geez! No offense, but I'm starting to feel vindicated in my choice not to have kids..."
    scene w1_1882 with dissolve
    rose "I can understand where you're coming from, but you don't know just how wonderful it is to be a parent until it happens. It's scary... your life is no longer your own, but..."
    scene w1_1883 with dissolve
    rose "You have two lives that are now your own."
    scene w1_1884 with dissolve
    ver "Also no offense, but that's what the people with kids usually tell their childless friends, in order to trick 'em into having them so they're not alone in their irrational decision."
    mct "(Geez...)"
    scene w1_1885 with dissolve
    rose "Why would that be offensive? You're only suggesting my love for the most important person in my life is senseless."
    "To my surprise, the normally congenial woman bared her teeth with an eerie smile."
    scene w1_1884 with dissolve
    ver "Hey! Don't put words in my mouth, I didn't mean anything bad--"
    scene w1_1886 with dissolve
    fel "I think Rosie is right. I love my stepsons. They've been apart of my life for 11 years, ever since they were babies."
    scene w1_1887 with dissolve
    fel "It's so hard relating to them though. They just have different problems than I did growing up."
    scene w1_1888 with dissolve
    ver "You mean they're spoiled brats?"
    scene w1_1889 with dissolve
    fel "Bingo."
    scene w1_1890 with dissolve
    mc "You don't want kids of your own?"
    scene w1_1891 with dissolve
    fel "No. It was never in the cards... or the pre-nup."
    scene w1_1892 with dissolve
    mct "(Is she trying to say she {b}contractually{/b} can't have kids...? What the fuck?)"
    "Oddly enough, no one else beside me seemed to find the remark curious."
    scene w1_1893 with dissolve
    fel "Suits me just fine."
    scene w1_1894 with dissolve
    ver "Hm..."
    scene w1_1895 with dissolve
    ver "I don't know if this is such a good idea."
    mc "What isn't?"
    scene w1_1896 with dissolve
    ver "Humanizing you two. I'm going to feel bad when you gals lose later."
    scene w1_1897 with dissolve
    mc "No one's going to feel like a winner."
    scene w1_1898 with dissolve
    ver "*sigh* You're right."
    rose "So, should we go up and pay?"
    scene w1_1899 with dissolve
    "A quick look at my phone revealed it was a couple of hours before we had to report to the club."
    "We had spent roughly an hour chatting."
    scene w1_1900 with dissolve
    mc "We should. I need to go home and get changed."
    scene w1_1901 with dissolve
    mc "Next week, we'll get together earlier. Deal?"
    ver "You're the boss."
    fel "Sure thing."
    rose "The sitter shouldn't mind the extra money..."
    mc "Good. It's settled then."
    ver "Yeah, it's a regular lunch club."
    scene w1_1902 with dissolve
    mc "Alright, well today's lunch is on me. It's only fair after I suddenly inconvenienced you."
    scene w1_1903 with dissolve
    fel "Such a gentleman."
    scene black with fade
    stop music fadeout 3.0
    "With that, the four of us said our parting words, destined to reconvene in only a couple of hours under more sobering circumstances."

    if roseFlag == False and MinaOutfitPro == True:
        jump w1MinaAuditionResultsPro
    if roseFlag == False and MinaOutfitCute == True:
        jump w1MinaAuditionResultsCute
    if roseFlag == False and MinaOutfitSexy== True:
        jump w1MinaAuditionResultsSexy
    if minaFlag == False:
        jump w1ExhibitionChange

## Rosalind Reassurance --------------------------------------------------------

    scene w1_1904 with wipeleft
    mct "(This went surprisingly well...)"
    play music "music/i-knew-a-guy.mp3"
    scene w1_1905 with dissolve
    mct "(Huh...?)"
    scene w1_1906 with dissolve
    mc "You're still here?"
    rose "I wanted to speak with you one-on-one."
    scene w1_1907 with dissolve
    mc "What about?"
    scene w1_1908 with dissolve
    rose "Well, all that talk about only having the other girls to rely on..."
    scene w1_1907 with dissolve
    mc "Yeah?"
    scene w1_1908 with dissolve
    rose "I still have you to rely on, right? We're still allies?"
    scene w1_1909 with dissolve
    "Ah. She's worried about the deal we made Tuesday night."
    scene w1_1908 with dissolve
    rose "You promised to do what you can if the opportunity to help me arises."
    scene w1_1909 with dissolve
    stop music fadeout 3.0
    "She asked me directly, in an anxious tone."
    hide screen textbox2 with dissolve

    menu w1RoseReassurance:
        "Reassure Rosalind you're still in her corner. [gr]\[Rosalind +2\] [red]\[Toughness -1\]":
            $ toughness -= 1
            $ Rosalind_Affection += 2
            play music "music/i-knew-a-guy.mp3"
            scene w1_1910 with dissolve
            show screen textbox2 with dissolve
            mc "Don't worry, I'll do what I can."
            scene w1_1911 with dissolve
            rose "Thank you!"
            scene w1_1912 with dissolve
            mc "No promises, remember?"
            scene w1_1908 with dissolve
            rose "I know..."
            scene w1_1907 with dissolve
            mc "By the way, I was wondering. Don't you feel bad for the other two?"
            scene w1_1908 with dissolve
            rose "No."
            scene w1_1909 with dissolve
            "She said coldly, with zero hesitation."
            scene w1_1908 with dissolve
            rose "You must think I'm awful, but..."
            scene w1_1907 with dissolve
            mc "No, I get it. Your situation is serious. There's no room for moral baggage."
            scene w1_1913 with dissolve

            if rosePolite == True:
                mc "Thank you, Mr. [mcl]."
            else:
                mc "Thank you, [mcf]."

            scene w1_1914 with dissolve
            mc "You can stop thanking me now."
            scene w1_1915 with dissolve
            rose "Yes, sir."
            scene w1_1916 with dissolve
            mc "I've got you back."
            scene w1_1917 with dissolve
            rose "Yes, sir!"
            stop music fadeout 3.0
            scene black with fade


        "{b}Show{/b} Rosalind that the deal is still on. [gr]\[Toughness +1\] \[RoesLibido +1\]":
            $ toughness += 1
            $ Rosalind_Libido += 1
            play music "music/helping-hands.mp3"
            scene w1_1918 with dissolve
            show screen textbox2 with dissolve
            rose "Mmmmh...?!"
            "Instead of using something as inadequate as words, I decided to {b}show{/b} Rosalind that our deal was still on."
            "Caught by surprise, I had to forcefully pry my co-conspirator's lips apart with my own in order to snake my tongue into her mouth."
            scene w1_1919 with dissolve
            rose "Mmm....sfweh..."
            "Rosalind was quick to catch on, quickly falling into her agreed upon role of {b}toy{/b}."
            "The kiss was meant to say: {i}of course the deal is still on and I'll do whatever I please with you."
            scene w1_1920 with dissolve
            rose "Ngh...♥"
            "Not fully satisfied I was getting the message across, I brought a hand to her right breast and gave it a rough squeeze."
            scene w1_1921 with dissolve
            "What had come over me? Normally, even a small amount of PDA made me embarrassed, but here I was publicly groping and abusing Rose's breasts."
            "Not only that, but it felt... AMAZING. Her complete surrender to me per our deal had made me feel bold."
            scene w1_1922 with dissolve
            mc "I'll see you in a couple of hours."
            mc "Don't be late or Mrs. Pulman will be pissed."
            scene black with fade
            stop music fadeout 3.0
            "Without waiting for Rosalind to give me a proper reply, I headed home."



        "{color=#FF1493}\[Full Deal]{/color} Make her prove herself to you. [gr]\[Toughness +2\] \[RoesLibido +1\]" if roseDealFullAcceptance == True:
            $ toughness += 2
            $ Rosalind_Libido += 1
            $ w1RosalindPhoto = True
            play music "music/leaving-home.mp3"
            show screen textbox2 with dissolve
            "For all my good intentions in calling this meeting, sitting here now and seeing Rosalind peer at me with those anxiety-ridden blue orbs of hers..."
            "Filled me with a growing sadistic desire. She was on the hook, to me of all people."
            scene w1_1923 with dissolve
            mc "That depends on you, Rose."
            scene w1_1924 with dissolve
            rose "..."
            "She considered my words before speaking."
            scene w1_1925 with dissolve
            rose "What do you want me to do?"
            scene black with fade
            "With a smile, I wrote some instructions on a napkin and headed home."
            "Rosalind didn't look happy."
            stop music fadeout 3.0


        "{color=#696969}\[Full Deal] Make her prove herself to you.{/color}" if roseDealFullAcceptance == False:
            jump w1RoseReassurance


    "......"
    "..."

    if MinaOutfitPro == True:
        jump w1MinaAuditionResultsPro
    if MinaOutfitCute == True:
        jump w1MinaAuditionResultsCute
    if MinaOutfitSexy== True:
        jump w1MinaAuditionResultsSexy
    if minaFlag == False:
        jump w1ExhibitionChange

## Mina Audition Results -------------------------------------------------------

label w1MinaAuditionResultsPro:

    "I need to change into my penguin suit before heading to the club."
    scene w1_1926 with blinds
    mct "(Is that...?)"
    "As I was approaching my apartment, Mina was coming out of it."
    scene w1_1927 with dissolve
    play music "music/ukulele-fun.mp3"
    mina "Oh! [mcf]! I was just cursing my luck for you not being home, but here you are!"
    scene w1_1929 with dissolve
    mc "Mina!"
    scene w1_1928 with dissolve
    "Mina had on the outfit we bought together last Tuesday."
    "The simple, chic business assemble that displayed her toned arms nicely."
    mct "(That must mean...)"
    scene w1_1929 with dissolve
    mc "You had your audition today?!"
    "And judging by the smile pastered on her face..."
    scene w1_1930 with dissolve
    mina "I got it! Didn't even need to wait for a callback!"
    scene w1_1931 with dissolve
    mc "Haha, that's great! Just remember the little people now that you've made it."
    scene w1_1932 with dissolve
    mina "Hardly! It's only a small role."
    mc "Still, it's a stepping stone. You're going to be on TV right?"
    mina "Ohmygosh! I am!"
    scene w1_1933 with dissolve
    mina "Wow! I mean, I knew that, but that was before I got the part. The reality of it just now hit me!"
    mc "Let me be the second to congratulate you."
    scene w1_1934 with dissolve
    mina "Second? You're the first."
    scene w1_1935 with dissolve
    mc "You haven't told Ian yet?"
    scene w1_1936 with dissolve
    mina "Nope! Remember, I said you'd be the first to know and here I am."
    scene w1_1937 with dissolve
    mc "Well, let me be the first to congratulate you then."
    scene w1_1936 with dissolve
    mina "Thanks, [mcf]."
    scene w1_1935 with dissolve
    mc "You want to come in? I got some place to be in a couple of hours, but I can offer you a drink."
    scene w1_1936 with dissolve
    mina "No, I got to skidaddle. I was nearby after the audition, so I thought I'd drop by and see if you were around to tell you the good news."
    scene w1_1937 with dissolve
    mc "Thanks for telling me. I'm glad you got the part."
    scene w1_1938 with dissolve
    mina "Me too! Thanks for your help."
    "Mina launched into yet another hug, firmly pressing her large breasts into my chest with zero self consciousness."
    scene w1_1939 with dissolve
    "I would've been content to let her carry on as long as she liked, as I couldn't help but find the sensation pleasant and her joy {b}infectious{/b}."
    "However..."
    scene w1_1940 with dissolve
    kil "You guys are looking pretty friendly."
    scene w1_1941 with dissolve
    "Ian had showed up a little earlier than expected."
    mina "Oh... {i}Ian{/i}. This is where you had to be tonight?"
    kil "..."
    "There was an air of tension between the two for the briefest moment."
    scene w1_1942 with dissolve
    kil "Yeah. I'm taking [mcf] to a networking thing my uncle set up. What are you doing here?"
    scene w1_1943 with dissolve
    mina "I dropped by to tell [mcf] that I got the part on--"
    scene w1_1944 with dissolve
    kil "You got the part?! That's awesome!"
    "Ian stepped forward with a burst of energy."
    mina "Yep! With [mcf]'s help, of course!"
    "The tone of the conversation had abruptly turned on its head yet again."
    scene w1_1945 with dissolve
    kil "Ah! Thanks, man! I'm glad the two of you are becoming fast friends, it's awesome to know the two most important people in my life get along."
    mc "I mean, I didn't really DO anything..."
    mct "(For real... Mina could've worn a trash bag and could've had a successful audition I bet.)"
    scene w1_1946 with dissolve
    kil "You always said the same thing when we were kids too, when you gave me half your lunch after the bullies stole mine..."
    scene w1_1947 with dissolve
    mina "You were bullied that bad as a kid? You always told me stories of the trouble you two got into, but you never mentioned..."
    kil "Oh, yeah. I had a pretty big target on my back due to how well off my parents were. Everything changed when [mcf] took me under his wing."
    scene w1_1948 with dissolve
    mc "Okay, now you're being hyperbolic."
    scene w1_1949 with dissolve
    kil "No, that's exactly how I remember it."
    scene w1_1950 with dissolve
    "Killian looked at me with an eerily genuine face of affection. In part, I couldn't fathom where he was coming from. All that was {b}years{/b} ago."
    hide screen textbox2 with dissolve
    menu:
        "Tease Ian about his childhood. [gr]\[Killian +1\]":
            $ Killian_Bromance += 1
            scene w1_1951 with dissolve
            show screen textbox2 with dissolve
            mc "I guess I couldn't help myself. You were such sad sack, that I couldn't just stand by and let you get picked on."
            scene w1_1952 with dissolve
            kil "I know, right?."

        "Tell Ian that's all in the past. [red]\[Killian -1\]":
            $ Killian_Bromance -= 1
            scene w1_1951 with dissolve
            show screen textbox2 with dissolve
            mc "Ah, well... that's all in the past. It's not important. You should let it go."
            scene w1_1953 with dissolve
            kil "Don't say that. It's important to me. I feel like I'll always owe you."

    scene w1_1954 with dissolve
    kil "You're meeting your mother tonight, right?"
    "Killian turned his attention away from me and back to Mina."
    scene w1_1955 with dissolve
    mina "Ah...! No need to remind {b}me{/b}. She'll suck all the excitement out of the day like some kind of fun vampire."
    kil "That's a shame. You might've finally been able to meet my uncle tonight."
    mina "Yeah... I should go..."
    scene w1_1956 with dissolve
    mina "I'll see you two later I guess."
    scene w1_1957 with dissolve
    kil "You too. I'll probably be late tonight."
    scene w1_1958 with dissolve
    mina "Just don't get too drunk."
    kil "I won't, I won't..."
    "With that, Mina parted ways and left Killian and I alone."
    jump w1ExhibitionChange

label w1MinaAuditionResultsCute:

    scene w1_1959 with dissolve
    "I need to change into my penguin suit before heading to the club."
    mct "(Is that...?)"
    "As I was approaching my apartment, Mina was coming out of it."
    scene w1_1960 with dissolve
    play music "music/ukulele-fun.mp3"
    mina "Oh! [mcf]! I was just cursing my luck for you not being home, but here you are!"
    scene w1_1961 with dissolve
    mc "Mina!"
    "Mina had on the outfit we bought together last Tuesday."
    "The coral tinted, girl-next-door assemble with the puffy shorts."
    mct "(That must mean...)"
    mc "You had your audition today?!"
    "And judging by the smile pastered on her face..."
    scene w1_1962 with dissolve
    mina "I got it! Didn't even need to wait for a callback!"
    scene w1_1963 with dissolve
    mc "Haha, that's great! Just remember the little people now that you've made it."
    scene w1_1964 with dissolve
    mina "Hardly! It's only a small role."
    mc "Still, it's a stepping stone. You're going to be on TV right?"
    mina "Ohmygosh! I am!"
    scene w1_1965 with dissolve
    mina "Wow! I mean, I knew that, but that was before I got the part. The reality of it just now hit me!"
    mc "Let me be the second to congratulate you."
    scene w1_1966 with dissolve
    mina "Second? You're the first."
    scene w1_1967 with dissolve
    mc "You haven't told Ian yet?"
    scene w1_1968 with dissolve
    mina "Nope! Remember, I said you'd be the first to know and here I am."
    scene w1_1969 with dissolve
    mc "Well, let me be the first to congratulate you then."
    scene w1_1968 with dissolve
    mina "Thanks, [mcf]."
    scene w1_1967 with dissolve
    mc "You want to come in? I got some place to be in a couple of hours, but I can offer you a drink."
    scene w1_1968 with dissolve
    mina "No, I got to skidaddle. I was nearby after the audition, so I thought I'd drop by and see if you were around to tell you the good news."
    scene w1_1969 with dissolve
    mc "Thanks for telling me. I'm glad you got the part."
    scene w1_1970 with dissolve
    mina "Me too! Thanks for your help."
    "Mina launched into yet another hug, firmly pressing her large breasts into my chest with zero self consciousness."
    scene w1_1971 with dissolve
    "I would've been content to let her carry on as long as she liked, as I couldn't help but find the sensation pleasant and her joy {b}infectious{/b}."
    "However..."
    scene w1_1972 with dissolve
    kil "You guys are looking pretty friendly."
    scene w1_1973 with dissolve
    "Ian had showed up a little earlier than expected."
    mina "Oh... {i}Ian{/i}. This is where you had to be tonight?"
    kil "..."
    scene w1_1974 with dissolve
    "There was an air of tension between the two for the briefest moment."
    kil "Yeah. I'm taking [mcf] to a networking thing my uncle set up. What are you doing here?"
    scene w1_1975 with dissolve
    mina "I dropped by to tell [mcf] that I got the part on--"
    scene w1_1976 with dissolve
    kil "You got the part?! That's awesome!"
    "Ian stepped forward with a burst of energy."
    mina "Yep! With [mcf]'s help, of course!"
    "The tone of the conversation had abruptly turned on its head yet again."
    scene w1_1977 with dissolve
    kil "Ah! Thanks, man! I'm glad the two of you are becoming fast friends, it's awesome to know the two most important people in my life get along."
    mc "I mean, I didn't really DO anything..."
    mct "(For real... Mina could've worn a trash bag and could've had a successful audition I bet.)"
    scene w1_1978 with dissolve
    kil "You always said the same thing when we were kids too, when you gave me half your lunch after the bullies stole mine..."
    scene w1_1979 with dissolve
    mina "You were bullied that bad as a kid? You always told me stories of the trouble you two got into, but you never mentioned..."
    kil "Oh, yeah. I had a pretty big target on my back due to how well off my parents were. Everything changed when [mcf] took me under his wing."
    scene w1_1948 with dissolve
    mc "Okay, now you're being hyperbolic."
    scene w1_1949 with dissolve
    kil "No, that's exactly how I remember it."
    scene w1_1950 with dissolve
    "Killian looked at me with an eerily genuine face of affection. In part, I couldn't fathom where he was coming from. All that was {b}years{/b} ago."
    hide screen textbox2 with dissolve

    menu:
        "Tease Ian about his childhood. [gr]\[Killian +1\]":
            $ Killian_Bromance += 1
            scene w1_1951 with dissolve
            show screen textbox2 with dissolve
            mc "I guess I couldn't help myself. You were such sad sack, that I couldn't just stand by and let you get picked on."
            scene w1_1952 with dissolve
            kil "I know, right?."

        "Tell Ian that's all in the past. [red]\[Killian -1\]":
            $ Killian_Bromance -= 1
            show screen textbox2 with dissolve
            scene w1_1951 with dissolve
            mc "Ah, well... that's all in the past. It's not important. You should let it go."
            scene w1_1953 with dissolve
            kil "Don't say that. It's important to me. I feel like I'll always owe you."

    scene w1_1980 with dissolve
    kil "You're meeting your mother tonight, right?"
    "Killian turned his attention away from me and back to Mina."
    scene w1_1981 with dissolve
    mina "Ah...! No need to remind {b}me{/b}. She'll suck all the excitement out of the day like some kind of fun vampire."
    kil "That's a shame. You might've finally been able to meet my uncle tonight."
    mina "Yeah... I should go..."
    scene w1_1982 with dissolve
    mina "I'll see you two later I guess."
    scene w1_1983 with dissolve
    kil "You too. I'll probably be late tonight."
    scene w1_1984 with dissolve
    mina "Just don't get too drunk."
    kil "I won't, I won't..."
    "With that, Mina parted ways and left Killian and I alone."
    jump w1ExhibitionChange

label w1MinaAuditionResultsSexy:

    scene w1_1985 with fade
    "I need to change into my penguin suit before heading to the club."
    mct "(Is that...?)"
    "As I was approaching my apartment, Mina was coming out of it."
    scene w1_1986 with dissolve
    play music "music/ukulele-fun.mp3"
    mina "Oh! [mcf]! I was just cursing my luck for you not being home, but here you are!"
    scene w1_1987 with dissolve
    mc "Mina!"
    "Mina had on the outfit we bought together last Tuesday."
    "The sex-kitten assemble with pleated skirt."
    mct "(That must mean...)"
    mc "You had your audition today?!"
    "And judging by the smile pastered on her face..."
    scene w1_1988 with dissolve
    mina "I got it! Didn't even need to wait for a callback!"
    scene w1_1989 with dissolve
    mc "Haha, that's great! Just remember the little people now that you've made it."
    scene w1_1990 with dissolve
    mina "Hardly! It's only a small role."
    mc "Still, it's a stepping stone. You're going to be on TV right?"
    mina "Ohmygosh! I am!"
    scene w1_1991 with dissolve
    mina "Wow! I mean, I knew that, but that was before I got the part. The reality of it just now hit me!"
    mc "Let me be the second to congratulate you."
    scene w1_1992 with dissolve
    mina "Second? You're the first."
    scene w1_1993 with dissolve
    mc "You haven't told Ian yet?"
    scene w1_1994 with dissolve
    mina "Nope! Remember, I said you'd be the first to know and here I am."
    scene w1_1995 with dissolve
    mc "Well, let me be the first to congratulate you then."
    scene w1_1994 with dissolve
    mina "Thanks, [mcf]."
    scene w1_1993 with dissolve
    mc "You want to come in? I got some place to be in a couple of hours, but I can offer you a drink."
    scene w1_1994 with dissolve
    mina "No, I got to skidaddle. I was nearby after the audition, so I thought I'd drop by and see if you were around to tell you the good news."
    scene w1_1995 with dissolve
    mc "Thanks for telling me. I'm glad you got the part."
    scene w1_1996 with dissolve
    mina "Me too! Thanks for your help."
    "Mina launched into yet another hug, firmly pressing her large breasts into my chest with zero self consciousness."
    scene w1_1997 with dissolve
    "I would've been content to let her carry on as long as she liked, as I couldn't help but find the sensation pleasant and her joy {b}infectious{/b}."
    "However..."
    scene w1_1998 with dissolve
    kil "You guys are looking pretty friendly."
    "Ian had showed up a little earlier than expected."
    scene w1_1999 with dissolve
    mina "Oh... {i}Ian{/i}. This is where you had to be tonight?"
    kil "..."
    scene w1_2000 with dissolve
    "There was an air of tension between the two for the briefest moment."
    kil "Yeah. I'm taking [mcf] to a networking thing my uncle set up. What are you doing here?"
    scene w1_2001 with dissolve
    mina "I dropped by to tell [mcf] that I got the part on--"
    scene w1_2002 with dissolve
    kil "You got the part?! That's awesome!"
    "Ian stepped forward with a burst of energy."
    mina "Yep! With [mcf]'s help, of course!"
    "The tone of the conversation had abruptly turned on its head yet again."
    scene w1_2003 with dissolve
    kil "Ah! Thanks, man! I'm glad the two of you are becoming fast friends, it's awesome to know the two most important people in my life get along."
    mc "I mean, I didn't really DO anything..."
    mct "(For real... Mina could've worn a trash bag and could've had a successful audition I bet.)"
    scene w1_2004 with dissolve
    kil "You always said the same thing when we were kids too, when you gave me half your lunch after the bullies stole mine..."
    scene w1_2005 with dissolve
    mina "You were bullied that bad as a kid? You always told me stories of the trouble you two got into, but you never mentioned..."
    kil "Oh, yeah. I had a pretty big target on my back due to how well off my parents were. Everything changed when [mcf] took me under his wing."
    scene w1_1948 with dissolve
    mc "Okay, now you're being hyperbolic."
    scene w1_1949 with dissolve
    kil "No, that's exactly how I remember it."
    scene w1_1950 with dissolve
    "Killian looked at me with an eerily genuine face of affection. In part, I couldn't fathom where he was coming from. All that was {b}years{/b} ago."
    hide screen textbox2 with dissolve
    menu:
        "Tease Ian about his childhood. [gr]\[Killian +1\]":
            $ Killian_Bromance += 1
            scene w1_1951 with dissolve
            show screen textbox2 with dissolve
            mc "I guess I couldn't help myself. You were such sad sack, that I couldn't just stand by and let you get picked on."
            scene w1_1952 with dissolve
            kil "I know, right?."

        "Tell Ian that's all in the past. [red]\[Killian -1\]":
            $ Killian_Bromance -= 1
            scene w1_1951 with dissolve
            show screen textbox2 with dissolve
            mc "Ah, well... that's all in the past. It's not important. You should let it go."
            scene w1_1953 with dissolve
            kil "Don't say that. It's important to me. I feel like I'll always owe you."

    scene w1_2006 with dissolve
    kil "You're meeting your mother tonight, right?"
    "Killian turned his attention away from me and back to Mina."
    scene w1_2007 with dissolve
    mina "Ah...! No need to remind {b}me{/b}. She'll suck all the excitement out of the day like some kind of fun vampire."
    kil "That's a shame. You might've finally been able to meet my uncle tonight."
    mina "Yeah... I should go..."
    scene w1_2008 with dissolve
    mina "I'll see you two later I guess."
    scene w1_2009 with dissolve
    kil "You too. I'll probably be late tonight."
    scene w1_2010 with dissolve
    mina "Just don't get too drunk."
    kil "I won't, I won't..."
    "With that, Mina parted ways and left Killian and I alone."
    jump w1ExhibitionChange

## Changing for the Club -------------------------------------------------------

label w1ExhibitionChange:

    stop music fadeout 3.0
    scene black with fade
    if hanaFlag == True:
        $ history_mina = "Mina dropped by and delivered some good news. She got the soap opera role she auditioned for! I might just be able to say I know someone famous."
        $ unread_mina = True
        play sound "sound effects/notification.wav"
        show bioupdate with dissolve
    "..."
    scene w1_2011 with wiperight
    play music "music/hotshot.mp3"
    mc "By the way, you're like an hour early."
    kil "Is that a problem?"
    mc "No, it's just an observation."
    scene w1_2012 with dissolve
    kil "I didn't want to sit around. I'm always get antsy before these things."
    scene w1_2013 with dissolve
    mc "You? Antsy?"
    scene w1_2014 with dissolve
    kil "We're technically part of the show tonight, so we're subject to Kat's whims more than you might think. You never know what you're going to get with her."
    kil "Don't misunderstand me, I'm not trying to scare you. It's the opposite. We're never on the {b}bad end{/b} of her games, it's more like being a kid waiting on Christmas morning."

    if w1GonzoReward == True:
        scene w1_2015 with dissolve
        kil "Speaking of which, I heard you really impressed her this week. Good work."
        kil "Which is awesome, since after Darius I'm pretty sure I'm on thin ice with her. Maybe you kicking ass will cause her to cut me some slack..."
    else:
        kil "That's what Darius used to say at least."

    "Right, Darius. His name always seems to come up."
    scene w1_2013 with dissolve
    mc "What happened with him by the way?"
    scene w1_2012 with dissolve
    kil "Ah, don't ask me. Guy was a little unhinged. Too many designer drugs."
    scene w1_2016 with dissolve
    mc "He was your friend, right? You've got to be pretty worried."
    scene w1_2017 with dissolve
    kil "Eh..."
    "Killian gave me a quick shrug."
    kil "We partied together, but it's not like we were close."
    "He said it without an ounce of camaraderie."
    scene w1_2014 with dissolve
    kil "Aw, don't look at me like that. It's just I know the guy, alright? I'm pretty sure he just split to Hawaii. His family has a business up there and he was always talking about going back."
    scene w1_2015 with dissolve
    kil "If you went missing, I'd be a little more concerned."
    scene w1_2013 with dissolve
    mc "Oh, that's good to know, thanks."
    scene w1_2018 with dissolve
    mc "I'm going to go change. Make yourself home."
    "I said, sarcastically as if he wouldn't have."
    scene w1_2019 with wipeleft
    mc "Aaaaah...!"
    scene w1_2020 with dissolve
    mct "(I'm getting pretty comfortable in these clothes.)"
    "Growing up, I didn't have many occasions to dress up. My father's funeral, my high-school graduation, and some college networking events have been about it."
    "While it felt stuffy at first, I'm starting to feel confident in them. It feels good to look good."
    mct "(I should send mom a picture. She'd get a kick out of it.)"
    stop music fadeout 3.0

    if w1RosalindPhoto == True:
        jump w1RosalindSelfies
    else:
        scene w1_2029 with dissolve
        jump w1ExhibitionPregame


label w1RosalindSelfies:

    play sound "sound effects/sms-chime.wav"
    "*Chirp, chirp.*"
    scene w1_2021 with dissolve
    mc "(Oh...?)"
    "That must be Rosalind. Hopefully she followed the instructions I wrote down for her at the diner."
    scene w1_2022 with dissolve
    "With burgeoning excitement, I made my way over to the bed to check. My dick already swelling in anticipation."
    play music "music/leaving-home.mp3"
    scene player-bedroom blur with dissolve
    hide screen textbox2 with dissolve
    call phone_start_rose from _call_phone_start_rose

    if rosePolite == True:
        call message_img("Rosalind", "As you asked, sir.","rosalind01") from _call_message_img_5
    else:
        call message_img("Rosalind", "As you asked...","rosalind01") from _call_message_img_6

    call message_img("Rosalind", "What if I can't get these off by tonight?","rosalind02") from _call_message_img_7
    call message_img("Rosalind", "This is so humiliating.","rosalind03") from _call_message_img_8

    call phone_end_rose from _call_phone_end_rose
    scene w1_2023 with fade
    show screen textbox2 with dissolve
    mct "(Awesome...!)"
    "She {b}had{/b} followed my instructions, to a T."
    "Scrawled across her body, in her own hand-writing, were various demeaning phrases and words."
    scene w1_2024 with dissolve
    "Phrases like {i}whore mother{/i}, {i}debt slave{/i}, and {i}cow tits{/i}"
    mct "(She had actually done it. Had she no sense of shame?)"
    scene w1_2025 with dissolve
    "What's more is she had added her own creative input to the wording. {i}Please milk me{/i}. {i}Certified milf cumdumpster{/i}. That woman...!"
    "Ah, picturing Rosalind obediently writing each degrading letter one by one in a mirror at my behest had me drunk with a perverse glee."
    "As did the thought of what came next. Rosalind would soon be frantically scrubbing every trace of the marker off her skin in preparation for tonight's game, her pale skin turning a beautiful hue of red from the rough friction."
    scene player-bedroom blur with fade
    hide screen textbox2 with dissolve
    call phone_start_rose from _call_phone_start_rose_1
    call message_img("Rosalind", "This is so humiliating.","rosalind03") from _call_message_img_9
    call screen phone_reply("You're a good girl.","w1RoseGoodGirl","That was the point, whore.","w1RoseWhore")


label w1RoseGoodGirl:
    $ Rosalind_Libido += 1
    call phone_after_menu from _call_phone_after_menu_16
    call message_start("[mcf]", "I know, but you did everything I asked, Rose. Thank you. You're a good girl.") from _call_message_start_23
    if rosePolite == True:
        call message("Rosalind", "Is there nothing else, sir?") from _call_message_68
    else:
        call message("Rosalind", "Is there nothing else?") from _call_message_69
    call reply_message ("No. I'll see you tonight.") from _call_reply_message_23
    call phone_end_rose from _call_phone_end_rose_1
    show screen textbox2 with dissolve
    scene w1_2026 with dissolve
    mct "(That was... exhilarating.)"
    "The ideal had abruptly come to me in a sadistic flash of cruelty that I had found myself more than happy to indulge in."
    scene w1_2027 with dissolve
    if not persistent.roseBodyWritingText:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ persistent.roseBodyWritingText = True
    "I knew that self-reflection on this troubling fact would be unproductive, so I pushed it out of mind and turned my attention to tonight."
    "Deep down, despite my good intentions at the start of the day, I'm going to enjoy watching the girls squirm, aren't I?"
    scene w1_2028 with dissolve
    $ renpy.end_replay()
    stop music fadeout 3.0
    jump w1ExhibitionPregame

label w1RoseWhore:
    $ Rosalind_Libido -= 1
    call phone_after_menu from _call_phone_after_menu_17
    call message_start("[mcf]", "I know, that was the point. To remind you that you're a whore. Good job.") from _call_message_start_24
    if rosePolite == True:
        call message("Rosalind", "Is there nothing else, sir?") from _call_message_70
    else:
        call message("Rosalind", "Is there nothing else?") from _call_message_71
    call reply_message ("No. I'll see you tonight.") from _call_reply_message_24
    call phone_end_rose from _call_phone_end_rose_2
    show screen textbox2 with dissolve
    scene w1_2026 with dissolve
    if not persistent.roseBodyWritingText:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ persistent.roseBodyWritingText = True
    mct "(That was... exhilarating.)"
    "The ideal had abruptly come to me at the diner in a sadistic flash of cruelty."
    scene w1_2027 with dissolve
    "I knew that reflecting on how fucked up it was to make her do that would be unproductive, so I pushed it out of mind and turned my attention to tonight."
    "Deep down, despite my good intentions at the start of the day, I'm going to enjoy watching the girls squirm, aren't I?"
    scene w1_2028 with dissolve
    $ renpy.end_replay()
    stop music fadeout 3.0
    jump w1ExhibitionPregame

label w1ExhibitionPregame:

    if w1RosalindPhoto == True:
        $ history_rosalind = "I took advantage of the deal I made with Rose and had her write degrading things on her body for my amusement."
        $ unread_rosalind = True
        play sound "sound effects/notification.wav"
        show bioupdate with dissolve

    kil "Oh, by the way, before I forget...!"
    "Ian called out from below."
    scene w1_2031 with dissolve
    play music "music/cold-sober.mp3"
    mc "Yeah?"
    scene w1_2032 with dissolve
    kil "I've got some paperwork to drop off with my mom tomorrow morning. Wanna come with?"
    scene w1_2031 with dissolve
    mc "What do you need me for? Sounds like a one person job."
    scene w1_2033 with dissolve
    kil "She wants to see you, so I thought I'd knock out two birds with one stone here."
    scene w1_2030 with dissolve
    mc "Huh...?"
    mct "({b}She{/b} wants to see me? That's weird. As far as I know, she never {b}ever{/b} liked me.)"
    mct "(In her defense, it wasn't because of the snooty, elite attitude the rest of Ian's family took, it was because she saw me as a poor influence on him.)"
    "Hard to fault her for that."
    scene w1_2031 with dissolve
    mc "The last time I saw her was our commencement ceremony. Why would she want to catch up all of a sudden?"
    scene w1_2032 with dissolve
    kil "I mentioned you were studying hard to become a doctor and she got curious about you."
    scene w1_2030 with dissolve
    mc "Oh...?"
    scene w1_2036 with pixellate
    mct "(Ian's mother was a well respected pediatrician, a specialization that was always funny to me considering her chilly personality.)"
    mct "(The thought of THAT woman tricking children to get shots with lollipops is hilarious to me.)"
    scene w1_2031 with pixellate
    mc "Not that I'm saying no, but tomorrow's my birthday. I'm having lunch with my mom."
    scene w1_2034 with dissolve
    kil "Come on. You think I don't know that? This will be in the morning. I promise it won't take too long and then I'll drop you off where you need to be afterwards."
    kil "You'll make her happy."
    scene w1_2030 with dissolve
    mct "(Since when does he care about that? Still...)"
    scene w1_2031 with dissolve
    mc "Alright, sure, but tell me one thing first."
    scene w1_2032 with dissolve
    kil "What is it?"
    scene w1_2031 with dissolve
    mc "Your mom seeing anyone right now?"
    scene w1_2032 with dissolve
    kil "Yeah, my dad!"
    scene w1_2031 with dissolve
    mc "He's out of the country right now, right?"
    scene w1_2035 with dissolve
    kil "Fuck you!"
    "After spending an hour shooting the shit, we made our way to my first official exhibition night."
    scene black with fade
    stop music fadeout 3.0
    "A night that would prove to surpass even my wildest imagination."
    "......"
    "..."
    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionkathleen01 with blinds
    $ renpy.pause(6, hard=True)
    $ date = "june06night"
    play ambient "sound effects/city-night.wav"
    scene pr0042 with blinds
    show screen textbox2 with dissolve
    show screen qmenu with dissolve
    "After a brief pit spot, we arrived at the Carnation Club."
    scene w1_2037 with wiperight
    stop ambient
    "The walk up to Mrs. Pulman's office was filled with both familiar and unfamiliar faces, as patrons were already beginning to arrive."
    play sound "sound effects/door-knock.wav"
    scene w1_2038 with wipeleft
    "*Knock, knock*"
    scene w1_2039 with dissolve
    kat "It's open."
    play sound "sound effects/door-openclose.wav"
    scene w1_2040 with fade
    play music "music/george-street-shuffle.mp3"
    kil "Checking in a little early, boss."
    kat "Should I be impressed by that, Ian?"
    mct "(Wait a minute, isn't that old man...)"
    kil "It was actually [mcf]'s idea--"
    scene w1_2041 with dissolve
    "Letting the impulse get the better of me, I stepped forward to confirm my suspicion."
    mc "Hey, you wouldn't happen to be..."
    mc "Ah, sorry! Don't want to be rude. I'm [mcf] [mcl]. You're Dr. Abel Van Doren, right?"
    scene w1_2042 with dissolve
    abel "That's right."
    abel "You know of me?"
    scene w1_2043 with dissolve
    mc "I would think so. Waller Scientific International has pioneered many advancements in medical science. From equipment, to pharmaceuticals, to even techniques."
    mc "Just last year your company developed a revolutionary debridement apparatus."
    scene w1_2044 with dissolve
    kat "Looks like you got a fan, Abel."
    scene w1_2045 with dissolve

    if w1GonzoReward == True:
        abel "It's nice to meet you in the flesh, [mcf]."
    else:
        abel "It's nice to meet you, [mcf]."

    scene w1_2046 with dissolve
    abel "Although I will say it's a little unusual for a boy your age to be abreast of the current trends in medical equipment."
    scene w1_2047 with dissolve
    kil "[mcf] is studying to get into med school."
    scene w1_2046 with dissolve
    abel "Oh? Is that so? Have you ever considered going into research after your residency?"
    scene w1_2048 with dissolve
    mc "That's such a long way away but... I'm hoping to become a clinician."
    scene w1_2046 with dissolve
    abel "I understand. Research is a thankless job, but you should consider it when the time comes."
    scene w1_2050 with dissolve
    abel "One great discovery and you can leverage that into a lifetime of developing treatments and cures that'll help more people than you ever would in a clinical setting."
    scene w1_2048 with dissolve
    mc "Thank you for the advice Dr. Van Doren, it's certainly something to keep in mind."
    scene w1_2049 with dissolve
    mct "(Running into a great man like him here...)"
    "If a great man like Abel Van Doren is a member of a place like this, maybe my concern about working here is simple naivety?"
    scene w1_2051 with dissolve
    kat "Since you two are here early, you can get started on some work."
    kat "[mcf]. Go find Warren and get him to magnetize you an access card. He'll know what you mean. The card will grant you free access to the more limited parts of the building, bar a few specific rooms."
    scene w1_2052 with dissolve
    mc "Okay, simple enough."
    scene w1_2053 with dissolve
    kat "After that, get him to point you in the direction of both the VIP lounge and the Carnation's dressing room."
    scene w1_2051 with dissolve
    kat "First, pop into the lounge and make your face known. Socialize a bit. I'll give you a proper introduction later tonight during the exhibition itself."
    scene w1_2052 with dissolve
    mc "Got it. What about the dressing room?"
    scene w1_2053 with dissolve
    kat "After you're finished at the lounge, go to the dressing room, confirm the girls are ready for tonight, and lead them to the exhibition hall."
    scene w1_2052 with dissolve
    mc "As ready as they humanly can be, you mean?"
    scene w1_2053 with dissolve
    kat "Just make sure they step onto the stage, Mr. [mcl]. Once the spotlight is on them, the momentum of the night will keep them there."
    scene w1_2052 with dissolve
    mc "Understood."
    scene w1_2054 with dissolve
    kat "You. Go to the equipment room and bring the items posted on the door to the adjoining hall of the exhibition room."
    scene w1_2055 with dissolve
    kil "Yep, heavy lifting... no surprise there."
    kil "Come on [mcf], let's go."
    scene w1_2056 with dissolve
    mc "It was nice meeting you, Dr. Van Doren."
    abel "The pleasure was mine."
    scene black with fade
    "......"
    "..."


label w1ExhibitionFreeRoamStart:

    scene w1_2057 with cmet
    "After leaving the boss' office, we made our way to the main hallway. "
    kil "Welp, off to do the non-fun part of the job. With you here, I was hoping we'd split the mule duties, buuuuut..."
    scene w1_2058 with dissolve
    mc "Sorry. Trade you if I could. Moving some equipment from point A to point B might be more palatable than rubbing elbows with..."
    scene w1_2059 with dissolve
    "..."
    scene w1_2060 with dissolve
    kil "Oh, you've got no idea yet bud. I won't ruin the surprise, but some of the patrons are..."
    scene w1_2061 with dissolve
    "Killian trailed off in a dramatic fashion."
    scene w1_2062 with dissolve
    mc "Some of them are what?"
    scene w1_2060 with dissolve
    kil "Some are lions and some are kitty cats."
    kil "You'll see. That said..."
    scene w1_2063 with dissolve
    kil "Knowing you, you'll have no trouble fitting in."
    "I wasn't quite sure what he meant by that."
    scene w1_2062 with dissolve
    mc "Thanks, I think?"
    scene w1_2064 with dissolve
    kil "Duty calls. Best go find Warren unless you want to make Granny Kat angry with you."
    scene w1_2065 with dissolve
    stop music fadeout 3.0
    mct "(Right. The first order of business was to find Warren and get him to magnetize me an access card.)"
    mct "(Might not hurt to look around and familiarize myself with some of the new faces, though.)"
    jump w1ExHallway


################################################################################
## Week 1 Exhibition Pregame Screens -------------------------------------------
################################################################################

screen w1ExNavMenu:

    imagemap:
        idle "gui/screens/imagemaps/w1ExNavMenu_idle.png"
        hover "gui/screens/imagemaps/w1ExNavMenu_hover.png"
        ground "gui/screens/imagemaps/w1ExNavMenu_ground.png"

        hotspot (736,56,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w1ExBar")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
        if w1ExSecurityRoomUnlock == True:
            hotspot (311,367,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w1ExSecurityRoom")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
        hotspot (777,367,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w1ExHallway")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
        hotspot (1237,367,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w1ExKatOffice")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
        if w1ExTimeBlock == "B":
            hotspot (311,668,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w1ExDressingRoom")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
        if w1ExTimeBlock == "B":
            hotspot (777,668,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w1ExVIPLounge")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
        hotspot (1238,668,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w1ExStage")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
        hotspot (10, 22, 180, 180) action [Play("menu_click","sound effects/page-turn.wav"), Return()] hovered [ Play ("hover_extra", "sound effects/click.wav") ]

label w1ExNavMenu:
    call screen w1ExNavMenu with pixellate

label w1ExStage:
    scene club-exhibition with cmet
    "I have no reason to be here until the exhibition starts."
    "I should explore another part of the building."
    call screen w1ExNavMenu with pixellate

screen w1ExHallway:

    imagemap:

        imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w1ExNavMenu")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]

        if w1ExTimeBlock == "A":

            idle "gui/screens/imagemaps/w1ExHallwayA_idle.png"
            hover "gui/screens/imagemaps/w1ExHallwayA_hover.png"
            ground "gui/screens/imagemaps/w1ExHallwayA_ground.png"
            if w1ExBusinessRepeat == False:
                hotspot (29,413,600,600) action Jump("w1ExBusiness")
            hotspot (1086,411,400,400) action Jump("w1ExJacobA")
            if w1ExTenorRepeat == False:
                hotspot (1544,411,500,500) action Jump("w1ExTenor")

        if w1ExTimeBlock == "B":
            idle "gui/screens/imagemaps/w1ExHallwayB_idle.png"
            hover "gui/screens/imagemaps/w1ExHallwayB_hover.png"
            ground "gui/screens/imagemaps/w1ExHallwayB_ground.png"

            if w1ExHarrassmentRepeat == False:
                hotspot (361,410,600,600) action Jump("w1ExHarrassment")
            if w1ExHarrassmentRepeat == False:
                hotspot (1035,398,500,500) action Jump("w1ExJacobB")


label w1ExHallway:
    show black
    $ renpy.music.play("music/cello-suite-No-1-G-Major-Prelude.mp3", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    call screen w1ExHallway with fade


screen w1ExKatOffice:

    imagemap:

        imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w1ExNavMenu")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]

        if w1ExTimeBlock == "A":

            idle "gui/screens/imagemaps/w1ExKatOffice_idle.png"
            hover "gui/screens/imagemaps/w1ExKatOffice_hover.png"
            ground "gui/screens/imagemaps/w1ExKatOffice_ground.png"

            hotspot (960,218,500,500) action Jump("w1ExAbel")
            hotspot (75,336,500,500) action Jump("w1ExKat")

        else:
            idle "gui/screens/imagemaps/w1ExKatOffice_idle.png"
            hover "gui/screens/imagemaps/w1ExKatOffice_hover.png"
            ground "gui/screens/imagemaps/w1ExKatOffice_ground.png"




label w1ExKatOffice:
    show black
    $ renpy.music.play("music/cello-suite-No-1-G-Major-Prelude.mp3", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    call screen w1ExKatOffice with fade


screen w1ExBar:

    imagemap:

        imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w1ExNavMenu")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]

        if w1ExTimeBlock == "A":

            idle "gui/screens/imagemaps/w1ExBarA_idle.png"
            hover "gui/screens/imagemaps/w1ExBarA_hover.png"

            if w1ExDickhead == False:
                ground "gui/screens/imagemaps/w1ExBarA1_ground.png"
            else:
                ground "gui/screens/imagemaps/w1ExBarA2_ground.png"

            hotspot (177,273,120,250) action Jump("w1ExHana")
            if w1ExDickhead == False:
                hotspot (308,265,550,900) action Jump("w1ExDickhead")
            if w1ExDaliaEntertain == False:
                hotspot (856,239,500,500) action Jump("w1ExDalia")
            hotspot (1522,392,300,300) action Jump("w1ExChuck")


        if w1ExTimeBlock == "B":
            imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w1ExNavMenu")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]

            idle "gui/screens/imagemaps/w1ExBarB_idle.png"
            hover "gui/screens/imagemaps/w1ExBarB_hover.png"
            ground "gui/screens/imagemaps/w1ExBarB_ground.png"

            hotspot (571,244,1000,1000) action Jump("w1ExChuckB")
            hotspot (1314,341,500,500) action Jump("w1ExMamaBoy")





label w1ExBar:
    show black
    $ renpy.music.play("music/jazz-apricot.mp3", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    call screen w1ExBar with fade

screen w1ExSecurityRoom:
    if w1ExWarrenGoneScore <= 1:
        imagemap:
            idle "gui/screens/imagemaps/w1ExSecurityRoomWarren_idle.png"
            hover "gui/screens/imagemaps/w1ExSecurityRoomWarren_hover.png"
            ground "gui/screens/imagemaps/w1ExSecurityRoom_ground.png"

            imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w1ExNavMenu")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            hotspot (801,374,300,800) action Jump("w1ExWarren")

    if w1ExWarrenGoneScore >= 2:
        imagemap:
            idle "gui/screens/imagemaps/w1ExSecurityRoomMonitor_idle.png"
            hover "gui/screens/imagemaps/w1ExSecurityRoomMonitor_hover.png"
            ground "gui/screens/imagemaps/w1ExSecurityRoom_ground.png"

            imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w1ExNavMenu")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            hotspot (890,394,300,300) action Jump("w1ExSecurityRoomSpying")

label w1ExSecurityRoom:
    if w1ExTimeBlock == "A" and w1ExWarrenGoneScore <= 1:

        jump w1ExBehindTheseWalls

    if w1ExTimeBlock == "B" and w1ExWarrenGoneScore <= 1:
        show black
        $ renpy.music.play("music/i-knew-a-guy.mp3", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
        call screen w1ExSecurityRoom with fade

    if w1ExTimeBlock == "B" and w1ExWarrenGoneScore >= 2:
        show black
        $ renpy.music.play("music/sneaky-snitch.mp3", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
        call screen w1ExSecurityRoom with fade

screen w1ExDressingRoom:

    imagemap:
        idle "gui/screens/imagemaps/w1ExDressingRoom_idle.png"
        hover "gui/screens/imagemaps/w1ExDressingRoom_hover.png"
        ground "gui/screens/imagemaps/w1ExDressingRoom_ground.png"

        imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w1ExNavMenu")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
        hotspot (378,156,300,500) action Jump("w1ExVeronica")


label w1ExDressingRoom:

    $ renpy.music.play("music/covert-affair.mp3", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)

    if w1ExVeroRepeat == False:
        show black
        jump w1ExVeronica

    else:
        show black
        call screen w1ExDressingRoom

screen w1ExVIPLounge:

    imagemap:
        idle "gui/screens/imagemaps/w1ExVIPLounge_idle.png"
        hover "gui/screens/imagemaps/w1ExVIPLounge_hover.png"
        ground "gui/screens/imagemaps/w1ExVIPLounge_ground.png"

        imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w1ExNavMenu")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
        hotspot (378,156,1500,1500) action Jump("w1ExVIPSamson")


label w1ExVIPLounge:
    show black
    call screen w1ExVIPLounge




################################################################################
## YOU ARE HERE GIL ------------------------------------------------------------
################################################################################

label w1ExBusiness:

    $ w1ExBusinessRepeat = True
    scene w1_2100 with fade
    mct "(This is my first time seeing this place lively like this.)"
    mct "(All the previous mention of illustrious and well-connected patrons and now I finally get to put faces to the club's customer base beyond that creepy school administrator and washed up actor.)"
    scene w1_2101 with dissolve
    "Those two for example."
    mct "(Even from here I can tell they have a different gravity to them than than Isaak and Samson.)"
    "That is to say..."
    mct "(They look like fuckin' Die Hard villains.)"
    scene w1_2102 with dissolve
    man1 "Have you had a chance to speak to Van Doren yet?"
    scene w1_2103 with dissolve
    man2 "No, but I was shocked to hear he joined. He seemed to me a serious man in our dealings."
    scene w1_2102 with dissolve
    man1 "You've met him previously?"
    scene w1_2103 with dissolve
    man2 "I did some intermediary work for one of Waller Scientific's subsidiaries. Getting the shipment of typhoid vaccine across an embargoed country's borders."
    scene w1_2102 with dissolve
    man1 "WSI supplies the black market?"
    scene w1_2104 with dissolve
    man2 "No, that's the damnedest thing. The medicine went straight to field hospitals. I couldn't figure out what his angle was."
    scene w1_2099 with dissolve
    man1 "That's an interesting piece of information, thank you {b}Frank{/b}. I..."
    scene w1_2105 with dissolve
    mct "(Ack-!)"
    "One of the men directed a look my way."
    scene w1_2106 with dissolve
    man1 "Let's go find a corner somewhere and talk shop."
    mct "(I've been staring too long and got caught!)"
    man2 "Sure, we've got time before that hag's show."
    scene w1_2107 with dissolve
    "The two of them, with house girl in tow, peeled off down one of the side corridors and ducked into a private room."
    "I... should try be more inconspicuous if I'm going to gawk like an idiot."
    jump w1ExHallway


label w1ExJacobA:
    if w1ExJacobRepeat == False:
        $ w1ExJacobRepeat = True
        scene w1_2108 with fade
        jacob "How's it going?"
        "As soon as I approached, Jacob extended a warm greeting my way."
        scene w1_2109 with dissolve
        "He had a hell of a grip to be sure, strong and firm, but considerate of my much smaller hand."
        jacob "First big night, huh?"
        mc "Uh huh, that's one way to put it."
        scene w1_2110 with dissolve
        jacob "This is the one time of the year the club's members find the room in their busy schedules to congregate like a pack of jackals."
        jacob "You picked quite the time to start, to be honest. The other seasons are pretty boring, relatively speaking."
        scene w1_2111 with dissolve
        mc "Will you be there tonight? On the exhibition floor I mean."
        scene w1_2112 with dissolve
        jacob "Not if I can help it. Between Warren and I, one of us needs to be on the show floor and the other needs to be on the monitors."
        jacob "I happily leave the first one to him when I can. He's more suited to it anyway. He enjoys it."
        scene w1_2113 with dissolve

        if kat_polite == True:
            mc "Speaking of Warren, I need to find him to get an access card. Mrs. Pulman said he'd most likely be at the bar?"
        else:
            mc "Speaking of Warren, I need to find him to get an access card. Kathleen said he'd most likely be at the bar?"

        scene w1_2114 with dissolve
        jacob "Besides hiding behind the big lady's skirt, you mean?"
        jacob "I haven't seem him go up, but the bar would be the first place I'd look. Check with Hana if he's not. He might have slipped into the service area to get to the security room."
        scene w1_2113 with dissolve
        mc "Aight, thanks Jacob."
        scene w1_2115 with dissolve
        jacob "No problem. Keep you head high and your eyes peeled tonight, eh?"
        mc "Will do."
        jump w1ExHallway


    else:
        scene w1_2110 with dissolve
        jacob "Still looking for Warren, [mcf]? If he's not at the bar, try asking Hana what direction he went off in."


    jump w1ExHallway

label w1ExTenor:

    $ w1ExTenorRepeat = True
    scene w1_2116 with fade
    man "I've never seen you before, dearie. You new?"
    scene w1_2117 with dissolve
    hgirl "I started this spring."
    scene w1_2116 with dissolve
    man "You haven't been added to the take out menu yet, have you? I would've remember seeing your beautiful face in the catalogue."
    scene w1_2117 with dissolve
    hgirl "Not yet, Mr. Bianchi. Mr. Byrnes wanted me to ease into things by only taking customers here."
    scene w1_2118 with dissolve
    man "Oh~hoho. You know who I am?"
    scene w1_2119 with dissolve
    hgirl "Of course. {b}Everyone{/b} knows the world famous tenor, Vincenzo Bianchi."
    mct "(Who the fuck is Vincenzo Bianchi?)"
    scene w1_2120 with dissolve
    vinc "Is that right, dearie? You're just flattering a fat old man. That'd be very {b}naughty{/b}..."
    play sound "sound effects/slap2.wav"
    scene w1_2121 with dissolve
    hgirl "Oh-!" with hpunch
    "The fat man gave the prostitute a playful swat."
    scene w1_2122 with dissolve
    vinc "I think I might have to punish that fat ass of yours."
    scene w1_2123 with dissolve
    hgirl "Oh, no. Mr. Bianchi. Please don't... hehe~♥. I'll be a good girl~♥"
    scene w1_2124 with dissolve
    "......"
    scene w1_2125 with dissolve
    "..."
    mct "(Well, whoever he is, he seems easily managed.)"
    jump w1ExHallway


label w1ExKat:
    if w1ExKatRepeat == False:
        $ w1ExKatRepeat = True
        scene w1_2127 with fade
        kat "Was there something you needed, Mr. [mcl]?"
        scene w1_2128 with dissolve
        mc "I have some questions about tonight, if you have the time for it."
        scene w1_2129 with dissolve
        kat "Oh...?"
        scene w1_2130 with dissolve

        if kat_polite == True:
            "Mrs. Pulman looked past me, to Dr. Van Doren."
        else:
            "Kathleen looked past me, to Dr. Van Doren."

        abel "Go ahead and answer the boy's questions, Kat. I don't mind waiting to finish our discussion."
        scene w1_2129 with dissolve
        kat "How can I help you, [mcf]?"
        scene w1_2131 with dissolve
        "Well..."
        hide screen textbox2 with dissolve

        menu w1ExhibitionKatQuestions:
            "What is my role in tonight?" if w1KatQuestionsRole == False:
                $ w1KatQuestionsRole = True
                $ w1KatQuestionScore += 1
                show screen textbox2 with dissolve
                mc "What is expected of me tonight?"
                scene w1_2132 with dissolve
                kat "During the exhibition, you mean?"
                scene w1_2131 with dissolve
                mc "Yes."
                scene w1_2133 with dissolve
                kat "Just like me, you'll be part of the show. You'll be my right hand. My aid. The cock that I don't have. Whatever you want to call it."
                scene w1_2131 with dissolve
                mc "That's vague."
                scene w1_2132 with dissolve
                kat "Well, they'll be a lot of twists and turns. There's no time to get into the minutia of it. You'll be asked to do a lot of things, all of which should be {i}pretty fun{/i} for a man your age."
                scene w1_2134 with dissolve
                kat "Put the exact details out of your mind and just enjoy the ride."
                scene w1_2131 with dissolve
                mct "(That... didn't really satisfactorily answer my question, but it seems the boss isn't inclined to say anything more.)"
                hide screen textbox2 with dissolve
                jump w1ExhibitionKatQuestions

            "What exactly did you mean by pop into the lounge and socialize?" if w1KatQuestionsSocialize == False:
                $ w1KatQuestionsSocialize = True
                $ w1KatQuestionScore += 1
                show screen textbox2 with dissolve
                mc "When you said you wanted me to socialize you meant...?"
                scene w1_2135 with dissolve
                kat "That wasn't exactly a complicated instruction, was it? I'd hope you'd be able to execute such a simple request."
                kat "I want you to politely put your face in the middle of other people's conversations. Smile. Suck up."
                scene w1_2132 with dissolve
                kat "You're new here and some of our patrons are slow to trust. You've got to start climatizing them to that inoffensive face of yours."
                scene w1_2131 with dissolve
                mc "Right. Understood. Sorry for the dumb question."
                hide screen textbox2 with dissolve
                jump w1ExhibitionKatQuestions

            "How will the winner tonight be determined?" if w1KatQuestionsScoring == False:
                $ w1KatQuestionsScoring = True
                $ w1KatQuestionScore += 1
                show screen textbox2 with dissolve
                mc "How will you pick a winner tonight? For that matter, how is the winner of the whole contest determined?"
                scene w1_2134 with dissolve
                kat "Ah, that's an astute question. We do it different every year, but the priority is always to have things remain competitive."
                scene w1_2133 with dissolve
                kat "Our second year, we had a clear winner by week 3's exhibition. It sucked all the fun out of the last week."
                scene w1_2131 with dissolve
                mc "So what are you doing this year?"
                scene w1_2132 with dissolve
                kat "It'll all be explained tonight, don't worry. No sense in saying it twice."
                scene w1_2136 with dissolve
                kat "You're not asking because you're trying to influence who ultimately wins, are you?"
                scene w1_2137 with dissolve
                mc "Why would I want to do that? What difference does it make to me?"
                scene w1_2136 with dissolve
                kat "Well, you've got a unique position with the girls. It'd be understandable if you felt sympathetic to one particular sob story or another."
                kat "You're only human and you're young; you haven't had the kindness beat out of you yet. Plus, it wouldn't be unheard of for those whores to try to unduly influence the exhibition's outcome."
                scene w1_2137 with dissolve

                if roseFlag == True:
                    mct "(Gh-! Does she know about me and Rose?)" with hpunch
                else:
                    mct "(Gh-! Does she know what Rose tried to do?)" with hpunch

                scene w1_2133 with dissolve
                kat "If that DOES happen.... feel free to indulge their little fantasy and string them along. Whatever it takes to keep them motivated until the end."
                scene w1_2131 with dissolve
                mct "(Man, she's truly merciless...)"
                scene w1_2132 with dissolve
                kat "Anything else, Mr. [mcl]?"
                scene w1_2131 with dissolve
                hide screen textbox2 with dissolve
                jump w1ExhibitionKatQuestions

            "That's all I wanted to ask." if w1KatQuestionScore >=1:
                show screen textbox2 with dissolve
                mc "That's all I wanted to ask. Thank you for your time, Mrs. Pulman."
                scene w1_2133 with dissolve
                kat "Good. Get to the tasks I've asked of you then."
                jump w1ExKatOffice


    else:
        scene w1_2129 with dissolve
        kat "What are you still doing here? My instructions were extremely simple. Get to it, Mr. [mcl]."
        jump w1ExKatOffice

label w1ExAbel:

    scene w1_2157 with dissolve
    mct "(That's Dr. Van Doren and his nurse. I've got no reason to bother them.)"
    jump w1ExKatOffice

label w1ExHana:
    if w1ExHanaRepeat == False:
        $ w1ExHanaRepeat = True
        $ w1ExSecurityRoomUnlock = True

        if hanaFlag == True:
            scene w1_2155 with dissolve
            hana "Heeeeey, [mcf]. What can I do for you?"
            scene w1_2139 with dissolve
            mct "(...dear, {b}lord{/b}.)"
            "Naturally, as you'd expect from a bartender, I found Hana behind the bar. What was unexpected, however..."
            ## Pan of Hana's outfit from behind the bar.
            scene w1_2138 with dissolve:
                subpixel True
                yalign 1.0
                xalign 0.6
                linear 4 yalign 0.15
            "Was the red outfit she had on."
            "Sure, she she didn't exactly dress modestly to begin with and her bathing suit the other night left much less to the imagination, but..."
            ## Zoom out from pan
            scene w1_2139 with dissolve
            mct "(Seeing her in high-class looking lingerie was something new. Plus, it was a color other than black.)"
            ## Hana blushes a little.
            scene w1_2140 with dissolve
            hana "If you're going to stare so hard, don't make it so obvious."
            scene w1_2141 with dissolve
            mc "Sorry, but can you blame me? I wasn't expecting you to be dressed like this."
            scene w1_2142 with dissolve
            hana "Why's that?"
            scene w1_2143 with dissolve
            mc "Well, for one, it's kind of weird, right? Your father works here."
            scene w1_2144 with dissolve
            hana "You kidding? As if me working here wasn't weird to begin with?"
            scene w1_2145 with dissolve
            hana "The old man ain't got a fucking problem with it. It was his idea."
            scene w1_2144 with dissolve
            hana "He says we got to maintain a certain atmosphere for the clientele. Which means anyone without a dick has to have a pretty face and their ass hanging out."
            scene w1_2146 with dissolve
            hide screen textbox2 with dissolve

            menu:
                "Tell Hana you're sorry she has to put up with that. [gr]\[Hana +1\]":
                    $ Hana_Affection += 1
                    scene w1_2147 with dissolve
                    show screen textbox2 with dissolve
                    mc "Sorry you have to put up with that. I know you don't want to be here. I know you wouldn't..."
                    scene w1_2148 with dissolve
                    hana "It is what it is! I would appreciate if you didn't mention what we talked about the other night anymore, especially around here. Understood?"
                    scene w1_2143 with dissolve
                    mc "Sorry."
                    scene w1_2144 with dissolve
                    hana "No, no. We're friends, I'm not mad. Just telling you to shut your damn yap!"
                    scene w1_2142 with dissolve
                    hana "...thanks though, I appreciate the sentiment."

                "Tell Hana she looks good in the outfit at least.":
                    scene w1_2147 with dissolve
                    show screen textbox2 with dissolve
                    mc "Well, at least you look good in it."
                    scene w1_2144 with dissolve
                    hana "You don't have to tell me. I know I do!"

            scene w1_2149 with dissolve
            "Hana shot me a smile."
            scene w1_2150 with dissolve
            hana "What can I get you?"
            scene w1_2146 with dissolve
            mc "What, like a drink?"
            scene w1_2144 with dissolve
            hana "Well, I am a bartender and you've approached my bar..."
            scene w1_2146 with dissolve
            "Ah!"
            scene w1_2147 with dissolve
            mc "I'm looking for Warren. You know where I can find him?"
            scene w1_2151 with dissolve
            hana "Yeah, it just so happens I do. He ducked into the security room about 30 minutes ago. He's probably still holed up there."
            hana "Take a left when you go back through the curtains and you'll find the service area. Take the stairs down and hook a right."
            scene w1_2150 with dissolve
            hana "You'll know it when you see it. It's got SECURITY ROOM etched onto a silver placard."
            scene w1_2143 with dissolve
            mc "Thanks Hana, I appreciate it."
            scene w1_2152 with dissolve
            hana "No problem, [mcf]"
            scene w1_2154 with dissolve
            mct "(I should head to the security room, although I could look around the building a little more if I wanted.)"



        else:
            scene w1_2155 with dissolve
            hana "Hey, new guy. Want something?"
            scene w1_2139 with dissolve
            mct "(...dear, {b}lord{/b}.)"
            "Naturally, as you'd expect from a bartender, I found Hana behind the bar. What was unexpected, however..."
            ## Pan of Hana's outfit from behind the bar.
            scene w1_2138 with dissolve
            "Was the red number she had on."
            "Sure, she didn't exactly dress modestly to begin with, but..."
            ## Zoom out from pan
            scene w1_2139 with dissolve
            mct "(Seeing her in high-class looking lingerie was something new. Plus, in a color that's not black!)"
            scene w1_2155 with dissolve
            hana "Yeah, yeah. Take it in. Looking is free - and so is the drinks for that matter."
            scene w1_2156 with dissolve
            mc "Sorry, but can you blame me? I wasn't expecting you to be dressed like this."
            scene w1_2142 with dissolve
            hana "Why's that?"
            scene w1_2143 with dissolve
            "You're just the bartender, right?"
            scene w1_2145 with dissolve
            hana "Doesn't matter. The old man is fucking anal about maintaining the appropriate atmosphere. Which means anyone without a dick has to have a pretty face and their ass hanging out."
            hana "Anyway, what can I get you?"
            scene w1_2146 with dissolve
            mc "..."
            scene w1_2144 with dissolve
            hana "I'm a bartender. You've approached my bar..."
            scene w1_2146 with dissolve
            "Ah!"
            scene w1_2147 with dissolve
            mc "No, no. I'm looking for Warren. It seems he isn't here though, you know where I can find him?"
            scene w1_2151 with dissolve
            hana "Yeah, it just so happens I can. He ducked into the security room about 30 minutes ago. He's probably still holed up there."
            hana "Take a left when you go back through the curtains and you'll find the service area. Take the stairs down and hook a left."
            scene w1_2150 with dissolve
            hana "You'll know it when you see it. It's got SECURITY ROOM etched into a silver placard."
            scene w1_2143 with dissolve
            mc "Thanks Hana, I appreciate it."
            scene w1_2148 with dissolve
            hana "No problem, new guy."
            scene w1_2154 with dissolve
            mct "(I should head to the security room, although I could look around the building a little more if I wanted.)"

    else:
        scene w1_2142 with dissolve
        hana "Not that I mind the company, but didn't you have something to do?"

    jump w1ExBar

label w1ExDickhead:
    $ w1ExDickhead = True
    scene w1_2158 with dissolve
    hgirl "Can I get you something to drink, Sir?"
    scene w1_2159 with dissolve
    man "Hmm..."
    scene w1_2160 with dissolve
    "The silver-haired man gave her a chastising look up-and-down."
    scene w1_2161 with dissolve
    man "With you? I'd think not. Kathleen usually has a higher standard than this."
    hgirl "Tck...!"
    "For the briefest moment, a flash of anger was plainly written on the prostitute's face."
    scene w1_2162 with dissolve
    hgirl "Sorry to bother you, Mr. Waylon."
    scene w1_2163 with dissolve
    "The dickhead waved a dismissive hand before..."
    scene w1_2164 with dissolve
    "Walking off, just like that."
    scene w1_2165 with dissolve
    hgirl "..."
    hide screen textbox2 with dissolve

    menu:
        "Ask what that asshole's problem is. [gr]\[Toughness +1\]":
            $ toughness += 1
            scene w1_2166 with dissolve
            show screen textbox2 with dissolve

            if toughness >= 20:
                mc "What's his fucking deal?"
            else:
                mc "What's his problem?"

            scene w1_2167 with dissolve
            hgirl "Oh...?"
            hgirl "Don't...  {size=-10}don't say that so loud...{/size=-10}"
            scene w1_2166 with dissolve
            mc "Sorry, my bad. Who was that?"
            scene w1_2168 with dissolve
            hgirl "That's Eric Waylon, CEO of the Aubade Group."
            scene w1_2166 with dissolve
            mc "I don't know what that is."
            scene w1_2169 with dissolve
            hgirl "Hehe, you know... come to think of it, me neither! I've got absolutely no clue!"
            scene w1_2166 with dissolve
            mc "I'm [mcf]."
            scene w1_2168 with dissolve
            hgirl "I know who you are. All the girls do. A few of them are pretty nervous - new employees can be scary."
            scene w1_2170 with dissolve
            emma "I'm Emma, by the way."
            scene w1_2166 with dissolve
            mc "It's nice to meet you, Emma."
            scene w1_2168 with dissolve
            emma "I should get back to hunting. On the clock."
            scene w1_2170 with dissolve
            emma "See you around, [mcf]."
            mct "(She seems like a nice girl.)"

        "Just go about your business. [red]\[Toughness -1\]":
            $ toughness -= 1
            show screen textbox2 with dissolve
            "Probably not a good idea to say anything negative about a patron."

    jump w1ExBar

label w1ExDalia:
    $ w1ExDaliaEntertain = True
    scene w1_2171 with fade
    dal "Ah, Mr. Chatterjee and my favorite lick! How are you two tonight?"
    scene w1_2172 with dissolve
    man1 "Sssh...! Not here! Save it for the..."
    scene w1_2173 with dissolve
    dal "Are you telling me what to do? Hmm...?"
    man1 "No, Mistres--"
    scene w1_2174 with dissolve
    dal "I think you and I need to go somewhere!"
    man1 "I--"
    "Dalia forcefully grabbed the bald man by the hand."
    dal "Shut your fucking mouth, clit dick."
    man1 "...!"
    scene w1_2175 with dissolve
    dal "Would you like to join us, Mihir? I know you like to sit in when I punish this pathetic sack of crap."
    mihir "Absolutely. I love to see you work, Dalia."
    dal "Excellent. You're both coming with me then."
    scene black with fade
    "Leading both patrons by the hand, Dalia forcefully ushered the pair out of the bar."
    scene w1_2176 with dissolve
    mct "(Clit dick...?)"
    mct "(The girls have to be equipped to cater to different tastes, it seems.)"

    jump w1ExBar

label w1ExChuck:
    if w1ExChuckRepeat == False:
        $ w1ExChuckRepeat = True
        scene w1_2177 with fade
        "Spotting Dr. Chuck sitting idly by and enjoying a drink, I absent mindedly approached my former mentor to say hello."
        scene w1_2178 with dissolve
        chuck "Ah, lad! Good to see you."
        scene w1_2179 with dissolve

        if chuck_polite == True:
            mc "Good evening, Sir. How are you?"

        if chuck_uncle == True:
            mc "Good evening, Uncle Chuck. How are you?"
        else:
            mc "Good evening, Dr. Chuck. How are you?"

        scene w1_2180 with dissolve
        chuck "If I'm honest... I'm feelin' like a kid in a candy store, baha!"
        scene w1_2179 with dissolve
        mc "That good, eh?"
        scene w1_2178 with dissolve
        chuck "I couldn't ask for a better way to spend my retirement."
        scene w1_2181 with dissolve
        chuck "Why don't you join me for a little bit? Keep an old man company?"
        scene w1_2182 with dissolve
        mct "(Sitting down and talking a little bit shouldn't hurt. There's enough time before the exhibition starts for me to do what's been tasked of me.)"
        scene w1_2183 with dissolve
        mc "Sure, why not?"
        scene w1_2184 with dissolve
        chuck "Good! You want a beer? I'll get Hana to--"
        scene w1_2185 with dissolve
        mc "No, thanks. It's a little early for that. Maybe as the night goes on."
        scene w1_2186 with dissolve
        chuck "Suit yourself."
        scene w1_2187 with dissolve
        mc "What is it about tonight that has you so excited?"
        "I decided to ask a question that sat at the forefront of my mind."
        scene w1_2196 with dissolve
        "Even with a few weeks to grapple with the cognitive dissonance between who I thought my high school mentor to be and what he actually is, I still hadn't come to terms with my new view of the man."
        scene w1_2189 with dissolve
        chuck "Hmm..."
        "In a lot of ways, he still seems like the person I remember him. The only thing that has changed is the setting."
        scene w1_2194 with dissolve
        chuck "I'm a simple man, [mcf]."
        scene w1_2192 with dissolve
        chuck "Growing up, I was an extremely serious person. In the army, in my studies, and in my career. Don't get me wrong - I enjoy the challenge of my work. The first NASA contract my firm won, oh boy..."
        scene w1_2194 with dissolve
        chuck "There really have been few feelings in life that have compared. Still..."
        scene w1_2189 with dissolve
        "Dr. Chuck let his trail off as he gathered his thoughts."
        scene w1_2191 with dissolve
        mc "Still?"
        scene w1_2192 with dissolve
        chuck "Life is short. Something we all know of course, but its truth is only felt the closer you get to the grave."
        scene w1_2194 with dissolve
        chuck "The truth of the matter, the truth about me is, I'm an unrepentant pervert. Always have been, lad."
        scene w1_2190 with dissolve
        chuck "I managed it, bottled it up, explored it over my years, but now I'm finally free to indulge in it."
        scene w1_2189 with dissolve
        "Dr. Chuck admitted pointily to something outrageous."
        scene w1_2191 with dissolve
        mc "Is it really that simple?"
        scene w1_2192 with dissolve
        chuck "The sad reality of life is that doing what you want doesn't guarantee happiness. However, pushing your true self aside makes the prospect hopeless."
        scene w1_2196 with dissolve
        "What he was saying to me, generally speaking, was sound. On the face of it, it was hard to argue with. However..."
        scene w1_1873 with pixellate
        mct "(Is there not such a thing as common decency? To thine own self be true sounds nice, but what if at the core, you're a toxic, vile and destructive person?)"
        "Wouldn't it be better to stifle yourself?"
        scene w1_2196 with dissolve
        "Despite the questions I was asking myself, I chose not to dispute what he proclaimed. There was no point in challenging an old man's entrenched world view."
        scene w1_2194 with dissolve
        chuck "What's going on in your head, lad?"
        scene w1_2195 with dissolve

        if chuck_polite == True:
            mc "Sorry. Your words gave me a lot to think about, Sir."

        if chuck_uncle == True:
            mc "Sorry. Your words gave me a lot to think about, Uncle Chuck.."
        else:
            mc "Sorry. Your words gave me a lot to think about, Dr. Chuck."

        scene w1_2194 with dissolve
        chuck "I'm happy to hear that."
        scene w1_2193 with dissolve

        if kat_polite == True:
            mc "I should get back to Mrs. Pulman's task now. Thanks for the brief talk."
        else:
            mc "I should get back to Kathleen's task now. Thanks for the brief talk."

        chuck "Sure. I'd hate to be the one who'd caused you to get an earful."
        chuck "We'll speak later tonight."
        jump w1ExBar


    else:
        scene w1_2197 with dissolve
        mct "(I've already spoken to Dr. Chuck. I should find something else to do.)"


    jump w1ExBar

label w1ExBehindTheseWalls:
    $ w1ExTimeBlock = "B"
    stop music fadeout 3.0
    scene w1_2066 with fade
    war "Hiya, kid."
    "Warren hit me with a curt greeting as soon as I stepped through the door to the security room."
    war "Don't go thinking you snuck up on me. I saw you coming."
    mc "Yeah, I can see that."
    "In front of the broad shouldered man was an array of monitors, displaying a security feed of the various nooks and crannies of the building."
    scene w1_2067 with dissolve
    play music "music/i-knew-a-guy.mp3"
    war "Welcome to the best seat in the building."
    "My attention was immediately scattered about the deceptively spacious room."
    scene w1_2068 with dissolve
    "It had a distinctly earthy, manly odor to it. A result of its occupants hygienic shortcomings and chain smoking habit, I gathered."
    scene w1_2069 with dissolve
    "In the opposite corner, laid unsecure and ready to be grabbed at a moment's notice, was a menacing looking shotgun. Even a layperson like myself could tell it was well cared piece of equipment, shining with faint traces of a recent treatment of gun oil."
    scene w1_2070 with dissolve
    mc "You've got eyes on the place, huh?"
    scene w1_2072 with dissolve
    war "You've got no idea. I've got eyes on {b}every single room{/b} in this building."
    scene w1_2071 with dissolve
    mc "Even the bedrooms?"
    scene w1_2073 with dissolve
    war "The 'private' rooms are the most vulnerable spots in the building, for both our girls and our clients, kid."
    scene w1_2071 with dissolve
    mc "Do they know they're being filmed? The customers, I mean."
    scene w1_2073 with dissolve
    war "It's no secret."
    scene w1_2071 with dissolve
    mc "Some of them are pretty important people, right? Aren't they worried about blackmail?"
    scene w1_2074 with dissolve
    war "Most of the men here tonight aren't concerned with the simple, trifling matter of being caught on tape doing something they shouldn't."
    scene w1_2078 with dissolve
    mc "You mean the rich and powerful get away with anything."
    scene w1_2075 with dissolve
    war "Ha! It's more than that... here, look."
    scene w1_2076 with dissolve
    "With a button press, one of the monitors turned over to a new image featuring a balding, dumpy looking man getting blown in some corner of the building."
    war "Recognize him?"
    mc "No. Should I?"
    war "That tube of lard is Jim O'Doherty, the esteemed and venerable Chief of Police of the MHPD."
    ## Zoom back out
    mc "Oh, yeah. I think I remember Mr. Byrnes mentioning him..."
    war "Not only that, but..."
    scene w1_2077 with dissolve
    "Again Warren switches over and brings my attention to a new image."
    war "You wouldn't know this head case, but he's one of Mrs. P's lawyers. A pretty fucking terrible one if we're judging him for his legal mind, but that mama's boy is the district attorney's dear baby brother."
    mc "That woman's ... {b}pregnant{/b}."
    "I said, ignoring the man on the monitor's affiliations and zeroing in on the obvious."
    scene w1_2072 with dissolve
    war "Some of these fucks will pay a lot of money for a woman who's knocked up. We used to have one girl who went through three pregnancies while working here."
    scene w1_2071 with dissolve
    mc "Three?! Seriously?"
    scene w1_2072 with dissolve
    war "Every time she popped one out, a couple of months later, Mrs. P would throw a party to knock her up again. $5,000 per creampie. Some of those bastards went 4 or 5 times."
    war "Then they'd wager on whose paternity the baby would share!"
    scene w1_2071 with dissolve
    mc "You've got to be kidding me, that's so fucked."
    "I was incapable of putting it any more eloquently. Fucked was exactly what it was."
    scene w1_2074 with dissolve
    war "Hahaha! Oh, you've got a lot of acclimating to do if that weirds you out, kid."
    scene w1_2078 with dissolve
    mc "What happened to the woman? She's not here anymore?"
    scene w1_2073 with dissolve
    war "She's gone. She may have made both the club and herself a bunch of money, but back-to-back pregnancies is hell on a body."
    war "We had to fire her. No one wanted to book her anymore."
    scene w1_2071 with dissolve
    "I couldn't believe someone would willingly do that..."
    "That's..."
    hide screen textbox2 with dissolve

    menu:
        "Tell Warren this place is interesting. [gr]\[Warren +1\]":
            $ Warren_Friendship += 1
            show screen textbox2 with dissolve
            mc "This place really is something unique, isn't it?"
            scene w1_2080 with dissolve
            war "That's the truth. This place is so much... fun."
            war "The most fun job I've ever held, after Hoarfrost."
            scene w1_2078 with dissolve
            mc "The private military contractor?"
            scene w1_2079 with dissolve
            war "The one and only."
            scene w1_2078 with dissolve
            mct "(Guess that's a pretty typical security background for a place like this.)"


        "Openly express your disgust. [red]\[Warren -1\]":
            $ Warren_Friendship -= 1
            show screen textbox2 with dissolve
            mc "This place is awful."
            scene w1_2079 with dissolve
            war "You've got a lot of growing up to do if that's how you feel, kid."
            mc "There's worst places in the world than what goes on between these four walls."
            war "Trust me, I've seen them."
            scene w1_2071 with dissolve
            mct "(Yeah... right. Sounds like bullshit bravado.)"

        "Keep your thoughts to yourself.":
            show screen textbox2 with dissolve
            mct "(It what it is. I'm here to pay for college, not pass down judgement.)"

    scene w1_2081 with dissolve
    war "Anyway, you're looking for this, right?"
    scene w1_2082 with dissolve
    mc "What does this give me access to exactly?"
    war "Various parts of the building, mostly the lower levels."
    scene w1_2083 with dissolve
    war "The VIP lounge, the exhibition hall, the equipment rooms..."
    scene w1_2085 with dissolve
    mc "Things I'll need free access to, basically."
    scene w1_2084 with dissolve
    war "Keep in mind that doesn't let you in everywhere in the building. Some doors are off limits."
    scene w1_2085 with dissolve
    mc "Like what?"
    scene w1_2086 with dissolve
    war "..."
    scene w1_2087 with dissolve
    war "I doubt you'd stumble across them even if you looked."
    scene w1_2086 with dissolve
    mct "(Okay...?)"
    "Warren got really scary all of a sudden."
    if kat_polite == True:
        mc "Oh, Mrs. Pulman told me to ask you for directions to the lounge and dressing room."
    else:
        mc "Oh, Kathleen told me to ask you for directions to the lounge and dressing room."

    scene w1_2088 with dissolve
    war "Sure, kid. Both of them are on the same floor as the exhibition hall. You just need to..."
    scene black with fade
    "Warren laid out some simple directions for me. I should be able to find them now."
    scene w1_2089 with fade
    war "You good?"
    mc "Yeah, thanks--"
    scene w1_2090 with dissolve
    mct "(Hmm...?)"
    scene w1_2091 with dissolve
    mct "(Is that Hana?)"
    "It looked like that slime ball Isaak was giving her a hard time."

    if hanaFlag == True:
        scene w1_2092 with dissolve
        mc "Does that asshole know she's August's daughter?"
        scene w1_2093 with dissolve
        war "It's no secret, but It's not like there's a rule you can't socialize with her. Most patrons respect him enough not to bark up that tree."

    else:
        scene w1_2092 with dissolve
        mc "Hana's not on the menu, right?"
        scene w1_2093 with dissolve
        war "You mean the boss' daughter?"
        scene w1_2094 with dissolve
        mc "What...?"
        scene w1_2095 with dissolve
        war "Oh? No one told you? She's August's daughter and no, she just serves drinks here. Most patrons respect him enough not to bark up that tree."
        scene w1_2094 with dissolve
        mc "Well, shit..."
        "That... makes some semblance of sense, I guess. Considering her open disdain for this place."

    scene w1_2096 with dissolve
    mc "Well, it looks like one dumb dog doesn't know better. See?"
    scene w1_2095 with dissolve
    war "Ah, Isaak. That's not surprising. He's a horny fool."
    scene w1_2094 with dissolve
    mc "She looks uncomfortable. Shouldn't you do something about it?"
    scene w1_2097 with dissolve
    war "Me? It's not my job to protect the princess' honor. People getting handsy is part of working here. He hasn't crossed the line... {b}yet{/b}."
    scene w1_2098 with dissolve
    mct "(Hmm... maybe he's right. Part of me wanted to immediately storm down there and insert myself into the situation, but if Warren isn't concerned, is it really my place to be?)"
    mct "(Whatever I decide to do, my business here is finished.)"
    jump w1ExSecurityRoom

label w1ExWarren:
    scene w1_2198 with dissolve
    mct "(Hmm, I've got no more business here, but maybe I could come back later and check out the feeds?)"
    jump w1ExSecurityRoom

label w1ExJacobB:

    scene w1_2199 with fade
    hana "I told you to step off, fatso! I'm not interested in having a drink with you!"
    scene w1_2200 with dissolve
    isak "I was only--"
    scene w1_2201 with dissolve
    hana "Fuck. Off. Old man!"
    scene w1_2202 with dissolve
    jacob "Mmmh..."
    scene w1_2203 with dissolve
    mc "You look conflicted."
    scene w1_2204 with dissolve
    jacob "I'm not sure what to do to be honest. I should probably step in, before the little Miss gets too heated. For everyone's sake..."
    scene w1_2205 with dissolve
    mc "What do you mean?"
    scene w1_2206 with dissolve
    jacob "Well, Hana can handle herself, but if she belittles him too much or worse, {i}clocks{/i} him, our reputation would take a hit."
    jacob "That would land the three of us in hot water by extension."
    scene w1_2205 with dissolve
    mc "Me too?"
    scene w1_2204 with dissolve
    jacob "Well, you're party to it now."
    scene w1_2205 with dissolve
    mc "Right..."
    "Jacob looks hesitant, like he doesn't know how to best handle the situation. Maybe I should offer to step in in his stead?"
    hide screen textbox2 with dissolve

    menu:
        "Tell Jacob you'll diffuse the situation. [gr]\[Jacob +2\]":
            $ Jacob_Friendship += 2
            scene w1_2207 with dissolve
            show screen textbox2 with dissolve
            mc "Tell you what--"
            scene w1_2208 with dissolve
            hana "I don't GIVE A FUCK how much money you bring in for the club." with hpunch
            scene w1_2207 with dissolve
            mc "...I'll take care of it, all right?"
            scene w1_2209 with dissolve
            jacob "I'd appreciate it. I'm good for yanking somebody by the arm, but I still don't have a handle on this tongue-in-cheek shit."
            scene w1_2210 with dissolve
            mc "Don't thank me just yet..."
            scene w1_2211 with dissolve
            mc "I'm going in..."
            jump w1ExHarrassment


        "Let Jacob break it up. [gr]\[WarrenGoneScore +1\] \[HarrassmentRepeat\]":
            $ w1ExHarrassmentRepeat = True
            $ w1ExWarrenGoneScore += 1
            scene w1_2212 with dissolve
            show screen textbox2 with dissolve
            hana "I don't GIVE A FUCK how much money you bring the club." with hpunch
            mc "..."
            scene w1_2206 with dissolve
            jacob "I should get in there."
            scene w1_2205 with dissolve
            stop music fadeout 3.0
            mc "Good luck."
            scene w1_2213 with fade
            jacob "Mr. Miller, would you like--"
            scene w1_2214 with dissolve
            play music "music/swagger.mp3"
            isak "Jacob! Do you hear the way this WHORE is talking to me?"
            "Even from here, I could see a twitch of anger flash across Jacob's face."
            scene w1_2215 with dissolve
            jacob "There's no need to speak to {b}Mr. Byrne's{/b} daughter like that."
            scene w1_2214 with dissolve
            isak "She's the one being rude. Do you know how much Lucy alone will make this place? This bitch can't even have a drink with me?"
            jacob "..."
            scene w1_2216 with dissolve
            "Instead of immediately responding, Jacob slid one of his large hands up onto the square of Isaak's neck."
            scene w1_2217 with dissolve
            jacob "I think... both of you need to cool off. Why don't you go down to the VIP lounge? Everyone is starting to gather there."
            scene w1_2218 with dissolve
            isak "I'm not goin--"
            scene w1_2217 with dissolve
            jacob "Leave the little Miss alone."
            scene w1_2219 with dissolve
            "Jacob said it flat, using his body language to give the creep no quarter to refuse."
            scene w1_2220 with dissolve
            isak "--gh! Ah... you're right, Jacob. I share a quarter of the responsibility here. The onus is on me to remove myself from rude company instead of letting it propagate. I need to be the bigger person."
            mct "(Jeez, that halfwit has no shame.)"
            scene w1_2221 with dissolve
            isak "I'll be on my way to the lounge then..."
            scene black with fade
            stop music fadeout 3.0
            "With that, Isaak scampered off like a rat."
            scene w1_2222 with dissolve
            jacob "Sorry, I know you're probably mad I stepped in..."
            hana "The impulse did cross my mind, but..."
            scene w1_2223 with dissolve
            hana "That'd be bratty of me. So, thanks Jacob."
            jacob "Don't mention. Just didn't want you to kick him in the nuts"
            scene w1_2224 with dissolve
            hana "I wouldn't have done that. I would've taken his head clean off."
            scene black with fade
            "After a short exchange, the two went their separate ways to parts of the building unknown."
            "All well that ends well, I guess."
            jump w1ExHallway


label w1ExHarrassment:

    $ w1ExHarrassmentRepeat = True
    $ w1ExWarrenGoneScore += 1

    scene w1_2225 with fade
    "I saddled my way up to the arguing pair."
    isak "What? You're too good to have a drink with me? Is that it?"
    scene w1_2226 with dissolve
    hana "It doesn't matter what my reason is. Get out of my face, creep."
    scene w1_2227 with dissolve
    isak "You're out of your goddamn mind. You think I'm a creep?! I'm--"
    scene w1_2228 with dissolve
    "Suddenly, the bookish man noticed my presence."
    scene w1_2229 with dissolve
    isak "Oh... it's you. What was your name again?"
    scene w1_2230 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Be professional.":
            scene w1_2231 with dissolve
            show screen textbox2 with dissolve
            mc "[mcf], Sir."
        "Curtly remind Isaak of your name.":
            scene w1_2231 with dissolve
            show screen textbox2 with dissolve
            mc "[mcf]."

    scene w1_2229 with dissolve
    isak "Ah, right. Yes. [mcf], was it?"
    scene w1_2230 with dissolve
    mct "(What an {b}annoying{/b} man...)"
    scene w1_2232 with dissolve
    isak "Did you hear the way this whore is talking to me?"
    scene w1_2233 with dissolve
    "A quick glance over at Hana told me she was seething at his comment, doing everything in her willpower not to claw the squawking man's eyes out on the spot."
    "I should set to work defusing the situation, but the question is how?"
    stop music fadeout 3.0
    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve

    menu w1ExHarrassmentMenu:
        "{color=#FF1493}\[Social Chameleon]{/color} Speak the creep's language to get him to go away. [gr]\[Kathleen +1\] \[Hana +1\]" if perk_socialChameleon == True:
            $ Kathleen_Trust += 1
            $ Hana_Affection += 1

            scene w1_2234 with dissolve
            show screen textbox2 with dissolve
            show screen qmenu with dissolve
            play music "music/swagger.mp3"
            mc "Mr. Miller, my friend."
            scene w1_2235 with dissolve
            mc "You'll excuse us a second, won't you, doll?"
            hana "Eh? Doll...?"
            scene w1_2236 with fade
            mc "I know. It's totally impertinent. I'm so sorry about her attitude."
            "I gently guided the bastard away from the situation, giving him an earful of what I thought he might want to hear. A mixture of deference and agreement wrapped in a tone of friendship."
            scene w1_2237 with dissolve
            isak "She has no right to talk to me like that!"
            isak "Do you know how much Lucy will bring the club this summer? I think I deserve a little respect, don't you?"
            scene w1_2238 with dissolve
            mc "Oh, you have it. From everyone on the staff. Hana's just a bit stuck up. You know how bitches are, right? She thinks because she's the boss' daughter she gets to act how she wants."
            scene w1_2236 with dissolve
            mc "It puts all of us in a difficult situation. Surely you can sympathize?"
            scene w1_2239 with dissolve
            isak "Ah, I'm not the only one who has it tough, huh?"
            scene w1_2238 with dissolve
            mc "Thanks for cutting us some slack, Mr. Miller. Besides..."
            scene w1_2240 with dissolve
            mc "Why are you barking up that tree for when there's enough company to be had from any of the other number of beautiful girls here?"
            scene w1_2239 with dissolve
            isak "Hehehe, you're right."
            "I had to stop myself from visibly grimacing from sheer annoyance."
            scene w1_2238 with dissolve
            mc "A VIP like you should head down to the VIP lounge, don't you think?"
            scene w1_2239 with dissolve
            isak "Right again! There's only so much time in the night, I shouldn't waste it on... unpleasant things."
            scene w1_2238 with dissolve
            mc "Thanks for being the bigger man here."
            scene w1_2239 with dissolve
            isak "I'll be sure mention to Mrs. Pulman how impressed with your professionality I am."
            scene w1_2240 with dissolve
            mc "I appreciate that, Mr. Miller. Enjoy yourself."
            scene black with fade
            stop music fadeout 3.0
            "With that, the creepozoid headed off to his own devices."
            scene w1_2242 with fade
            mc "Jeez, I feel so fucking dirty. Sorry about the doll thing, by the way."
            scene w1_2243 with dissolve
            play music "music/hep-cats.mp3"
            hana "You're quite the diplomat, aren't you?"
            scene w1_2244 with dissolve
            mc "I was just handling a {b}stupid{/b} man."
            scene w1_2245 with dissolve
            hana "Well, whatever you call it..."

            if hanaFlag == True and Hana_Affection >= 14:

                scene w1_2247 with dissolve
                "*Smooch*"
                "With a quick hop, she planted a kiss on my cheek."
                scene w1_2248 with dissolve
                hana "Thanks for the assist."
                scene w1_2249 with dissolve
            else:
                scene w1_2246 with dissolve
                hana "Thank you."

            mc "Don't mention it."
            scene w1_2250 with dissolve
            hana "Well, I need to get off to lower levels. I guess I'll probably be seeing you at this thing tonight."
            "With a quick wave, Hana headed toward the stairs."
            scene w1_2253 with fade
            jacob "You handled that much more smoothly than I would've. Thanks"
            scene black with fade
            "......"
            "..."
            jump w1ExHallway




        "{color=#FF1493}\[Social Buttefly]{/color} Keep your cool and respectfully redirect Isaak elsewhere. [gr]\[Kathleen +1\] \[Hana +1\]" if perk_socialButterfly == True:
            $ Kathleen_Trust += 1
            $ Hana_Affection += 1

            scene w1_2234 with dissolve
            show screen textbox2 with dissolve
            show screen qmenu with dissolve
            mc "Mr. Miller. Can I speak to you in private, Sir?"
            scene w1_2251 with dissolve
            isak "Sure, but know I'm not happy about the way I'm being treated here."
            scene w1_2236 with fade
            play music "music/swagger.mp3"
            "In an effort to diffuse the situation, I guided the bastard away from Hana and spoke to him man-to-man."
            mc "I know and I'm very sorry about that."
            scene w1_2237 with dissolve
            isak "Do you know how much Lucy will bring the club this summer? I think I deserve a little respect, don't you?"
            scene w1_2238 with dissolve
            mc "You contributions are felt by everyone in the club, Sir. You absolutely have it."
            mct "(I can't believe I could say that without bursting into laughter.)"
            scene w1_2241 with dissolve
            isak "Then what's the bitch's problem? A drink is the least I'm {b}owed.{/b}."
            "I had to stop myself from visibly grimacing from sheer annoyance."
            scene w1_2236 with dissolve
            mc "Hmm, well... that's just how Hana is, y'know? She's not quite a good fit for this place, but she's the boss' daughter."
            scene w1_2237 with dissolve
            isak "Right. I got you, what can you do? Men have a blind spot when it comes to their daughters."
            isak "Even a man like Mr. Byrnes I guess..."
            scene w1_2238 with dissolve
            mc "Yes, exactly! That's what I'm saying. I'd knew you'd understand."
            scene w1_2236 with dissolve
            mc "Let me reiterate: I am {i}so{/i}, {b}so{/b} sorry and I'm hoping you can look past this treatment, Sir."
            scene w1_2239 with dissolve
            isak "Well, I suppose no harm is done..."
            scene w1_2240 with dissolve
            mc "I think a VIP like you should head down to the VIP lounge."
            scene w1_2239 with dissolve
            isak "You're onto something there. There's only so much time in the night, I shouldn't waste it on unpleasant things."
            scene w1_2238 with dissolve
            mc "I'm relieved one of you could be the bigger person here."
            scene w1_2237 with dissolve
            isak "Quite right! A man needs to know when to be able to look past things."
            scene w1_2239 with dissolve
            isak "I'll be sure mention to Mrs. Pulman how impressed with your professionality I am."
            scene w1_2240 with dissolve
            mc "I appreciate that, Mr. Miller. Enjoy yourself. Enjoy yourself tonight."
            scene black with fade
            stop music fadeout 3.0
            "With that, the creepozoid headed off to his own devices."
            scene w1_2252 with dissolve
            hana "How does his asshole taste, by the way?"
            mc "*sigh* Don't hold that against me, okay?"
            scene w1_2243 with dissolve
            play music "music/hep-cats.mp3"
            hana "No, I think I get what you were doing. You're quite the diplomat, aren't you?"
            scene w1_2244 with dissolve
            mc "I wouldn't call any of that diplomacy. Just handling a {b}stupid{/b} man."
            scene w1_2245 with dissolve
            hana "Well, whatever you call it..."

            if hanaFlag == True and Hana_Affection >= 14:
                scene w1_2247 with dissolve
                "*Smooch*"
                "With a quick hop, she planted a kiss on my cheek."
                scene w1_2248 with dissolve
                hana "Thanks for the assist."
                scene w1_2249 with dissolve
            else:
                scene w1_2246 with dissolve
                hana "Thank you."

            mc "Don't mention it."
            scene w1_2250 with dissolve
            hana "Well, I need to get off to lower levels. I guess I'll probably be seeing you at this thing tonight."
            "With a quick wave, Hana headed toward the stairs."
            scene w1_2253 with fade
            jacob "Good stuff, [mcf]. You handled that well. Thanks."
            jump w1ExHallway


        "Lie and say Hana is needed elsewhere. [gr]\[Hana +1\]":
            $ Hana_Affection += 1

            show screen textbox2 with dissolve
            show screen qmenu with dissolve
            "I only need to remove one of them to diffuse the situation and Hana would be the easiest."
            scene w1_2254 with dissolve
            play music "music/thief-in-the-night.mp3"
            mc "Ah, Hana! There you are!"
            "I made a point to ignore the creepozoid's question."
            mc "Mrs. Pulman needed to see you."
            scene w1_2255 with dissolve
            hana "She does?"
            scene w1_2256 with dissolve
            "I not-so-inconspicuously shot a wink her way. If Isaak managed to catch it, fuck him."
            scene w1_2257 with dissolve
            hana "Ooooooh, okay. She does?"
            "She said in a tone that suggested an understanding of what I was doing."
            hana "Did it sound important?"
            scene w1_2258 with dissolve
            mc "Yes. She needs to see you now. She seemed pissed. Something about your attitude recently."
            scene w1_2259 with dissolve
            hana "Oh, give me a fucking break..."
            scene w1_2260 with dissolve
            mc "C'mon. She told me to make sure you got there."
            scene w1_2261 with dissolve
            "Without waiting for her reply, I pulled Hana in the direction of Mrs. Pulman's office and left Isaak to standing there, ignored and mouth hanging open like a stupid fish suffocating on air."
            scene w1_2262 with fade
            hana "That was a smooth one."
            scene w1_2263 with dissolve
            mc "Sorry about butting in."
            scene w1_2264 with dissolve
            hana "No, that's okay. I could see Jacob sweating his ass off trying to figure out how best to handle the situation. You did it clean."
            hana "Plus, I appreciate the assist. I was about to blow the gasket."
            stop music fadeout 3.0

            if hanaFlag == True and Hana_Affection >= 14:
                scene w1_2267 with dissolve
                "*Smooch*"
                "With a quick hop, she planted a kiss on my cheek."
                scene w1_2268 with dissolve
                hana "Thanks for the assist."
                scene w1_2269 with dissolve
            else:
                hana "Thank you."
                scene w1_2265 with dissolve

            mc "Don't mention it."
            scene w1_2266 with dissolve
            hana "Well, I need to get off to lower levels, but I'll wait here a little while just in case that lard ass sticks around the hallway."
            mc "Good idea."
            scene black with fade
            "With a quick wave, I headed back to the hallway."
            jump w1ExHallway



        "Call this loser out on his shit. [red]\[Kathleen -2\] [gr]\[August +1\] \[Hana +2\]":
            $ Kathleen_Trust -= 2
            $ August_Friendship += 1
            $ Hana_Affection += 2

            scene w1_2270 with dissolve
            show screen textbox2 with dissolve
            show screen qmenu with dissolve
            mc "With how you're acting, is it any wonder?"
            isak "Huh?"
            scene w1_2271 with dissolve
            play music "music/take-the-lead.mp3"
            mc "Hana serves drinks here. She's not one of the prostitutes, she isn't obliged to entertain you for the evening."
            scene w1_2272 with dissolve
            isak "You're talking to me like that after all I've done for the club? I have you know, not even counting Lucy, I've helped recruit quite a few girls over the years."
            isak "I think I deserve a little more respect!"
            scene w1_2273 with dissolve
            mc "Respect? Why would I respect an over-excited, greasy asshole like you?"
            scene w1_2274 with dissolve
            isak "Excuse me?!"
            "Isaak looked at me with an extremely bewildered look plastered on his face, filling me with an immense satisfaction."
            scene w1_2275 with dissolve
            hana "Pftt--hahahahaha!"
            scene w1_2276 with dissolve
            isak "You think you can talk to me like that? Wait until Mrs. Pulman hears--"
            scene w1_2277 with dissolve
            mc "Tell her. Let Dr. Chuck and {b}Mr. Byrnes{/b} know too."
            mc "I'm sure he in particular will be thrilled that you {b}aggressively harassed{/b} his daughter."
            scene w1_2278 with dissolve
            isak "Eh-heh?! I d-did nothing of the sort! We were just talking. Isn't that right, {i}dear{/i}...?"
            scene w1_2279 with dissolve
            hana "Sure. That was all it was, [mcf]. You asked me to have a drink, I declined, and you were about to respectfully walk way before this turned into a big misunderstanding."
            "Hana surprisingly moved the conversation to a more pleasant resolution, giving Isaak a clear out here."
            scene w1_2280 with dissolve
            isak "Yes... that's all this is. A misunderstanding."
            scene w1_2281 with dissolve
            stop music fadeout 3.0
            mc "Oh, my mistake then. Sorry!"
            scene w1_2282 with dissolve
            isak "I'll uh, I'll be..."
            "Without saying much else, Isaak hobbled off in the direction of the stairs, tail tucked between his legs."
            scene w1_2242 with dissolve
            play music "music/hep-cats.mp3"
            mc "He's easily handled, huh?"
            mct "(Some are lions and some are kitty cats. That's what Ian said.)"
            scene w1_2283 with dissolve
            hana "Yeeesh, I feel like I need a shower after that."
            scene w1_2284 with dissolve
            mc "Sorry for butting in, by the way."
            scene w1_2245 with dissolve
            hana "No, that's okay. I could see Jacob sweating his ass off trying to figure out how best to handle the situation. You did it clean."
            hana "Plus, I appreciate the assist. I was about to blow the gasket."

            if hanaFlag == True and Hana_Affection >= 14:

                scene w1_2247 with dissolve
                "*Smooch*"
                "With a quick hop, she planted a kiss on my cheek."
                scene w1_2248 with dissolve
                hana "Thanks for the assist."
                scene w1_2249 with dissolve
            else:
                scene w1_2246 with dissolve
                hana "Thank you."

            mc "Don't mention it."
            scene w1_2285 with dissolve
            hana "Plus, it was fucking awesome to see somebody besides me stand up to one of those entitled assholes for once. Weren't you worried about getting into trouble?"
            mc "Sometimes it's worth drawing a line in the sand."
            hana "Right, the look on that fatso's face was priceless."
            scene w1_2250 with dissolve
            hana "Well, I need to get off to lower levels. I guess I'll probably be seeing you at this thing tonight."
            "With a quick wave, Hana headed toward the stairs."
            scene w1_2253 with fade
            stop music fadeout 3.0
            jacob "That was one way to handle it. This will probably get back to the bosses in some shape of form, knowing Mr. Miller. If it does, I'll make sure a little bit of the truth gets added into the mix."
            jacob "Mrs. Pulman probably won't be too mad and I think Mr. Byrnes will be surprisingly grateful."
            scene w1_2286 with dissolve
            mc "I'd appreciate that Jacob, thank you."
            jump w1ExHallway

        "{color=#696969}\[Social Chameleon] Speak the creep's language to get him to go away.{/color}." if perk_socialChameleon == False:
            jump w1ExHarrassmentMenu
        "{color=#696969}\[Social Butterfly]  Keep your cool and respectfully redirect Isaak elsewhere.{/color}." if perk_socialButterfly == False:
            jump w1ExHarrassmentMenu



label w1ExChuckB:
    if w1ExChuckBRepeat == False:
        $ w1ExChuckBRepeat = True
        $ w1ExWarrenGoneScore += 1
        scene w1_2300 with fade
        "Doubling back to the bar, it seemed most people had cleared out by now, in a deliberate exodus toward some other part of the building if I had to guess."

        if w1ExBusinessRepeat == True:
            "One of the few people remaining was Dr. Chuck, sharing a beer with the large, older man who had caught my gaze lingering on him in the main hallway."
        else:
            "One of the few people remaining was Dr. Chuck, sharing a beer with the large, older man I had previously seen in the main hallway."

        scene w1_2287 with dissolve
        "Dr. Chuck noticed me as I entered."
        chuck "[mcf]! Come on over here, lad. I want to introduce you to an old friend."
        scene w1_2288 with dissolve
        chuck "This is..."
        scene w1_2289 with dissolve
        man "Kristoff Jostad Jameson."
        "The man said simply, holding out his hand."
        scene w1_2290 with dissolve
        mc "[mcf] [mcl]. Nice to meet you."
        "Kristoff was a surprisingly well-built man, considering his age. His tall, lithe frame looked like it held a lot of power just waiting to be uncoiled."
        "Despite looking positively {b}ancient{/b}, his posture was like that of an oak and his hand grip like iron."
        scene w1_2291 with dissolve
        chuck "Kristoff is the chief of operations at Hoarfrost Risk Management. You familiar with them?"
        "--ah, yeah. That makes sense."
        scene w1_2292 with dissolve
        mc "Yeah, nominally. From what little I've heard in the news."
        "Hoarfrost was a private military contractor - which meant, anytime they made headlines, it wasn't because of a flattering reason."
        "In fact, If I did an internet search, I'm sure I'd easily find a fountain of information that I don't want to know considering I'm now making his acquaintance."
        scene w1_2291 with dissolve
        chuck "Kristoff and I go a ways back."
        scene w1_2293 with dissolve
        chuck "[mcf] here is a long time friend of the family and our newest employee."
        scene w1_2294 with dissolve
        jiji "Good to meet you, son."
        scene w1_2295 with dissolve
        mc "How do you two know each other exactly?"
        scene w1_2296 with dissolve
        "The pair silently exchanged a suspicious look, before Dr. Chuck was the one to speak."
        scene w1_2297 with dissolve
        chuck "I did some consulting once upon a time for Kristoff's company.."
        mc "I see."
        scene w1_2298 with dissolve
        "I stopped myself from asking {i}consulting for what?{/i}"
        mc "Ah, wish I could stay and chat, but..."
        scene w1_2297 with dissolve
        chuck "Of course, you've got things to tend to."
        "I excused myself from the conversation."

    else:
        scene w1_2299 with dissolve
        mct "(I've already been introduced to the man with the ridiculously long name. No reason to butt into their conversation again.)"


    jump w1ExBar

label w1ExMamaBoy:
    if w1ExMamaBoyRepeat == False:
        $ w1ExMamaBoyRepeat = True
        $ w1ExWarrenGoneScore += 1
        scene w1_2301 with dissolve
        "In the corner of the bar, was one of the men Warren had pointed out from the security feed. The lawyer, if I recall correctly."
        "The one chatting up the pregnant prostitute. Well..."
        scene w1_2302 with dissolve
        "He was certainly doing more than chatting now."
        "Indeed, now he was suckling zealously at the woman's darkened teats, a trickle of breast milk running down his chin."
        "There was not an ounce of gentleness in his approach. The woman wore a complicated expression, a mixture of glassed over complacency and a uncomfortableness over the rough and greedy treatment."
        scene w1_2303 with dissolve
        pp "--!"
        pp "Eeeh, not so rough, Tom."
        "Instead of heeding her request, the milk-fixated lawyer gave her puffy nipples another pinch, sending yet another spurt of breast milk raining down onto her gravid belly."
        scene w1_2304 with dissolve
        "Only to return back to her suckling, a magical and content look on his face."
        mct "(Eh... that's enough of that. This is just too weird for me.)"
        "I decided I had seen enough."
    else:
        scene w1_2304 with dissolve
        mct "(He looks like he's going to be at it for awhile...)"
    jump w1ExBar

label w1ExSecurityRoomSpying:
    if w1ExSecurityRoomSpyingRepeat == False:
        scene w1_2308 with dissolve
        mct "(Looks like Warren stepped out.)"
        mct "(His slideshow earlier got me a little curious about what else goes on within these walls...)"
        "Do I want to take a look at the security feed?"
        hide screen textbox2 with dissolve

        menu:
            "Take a look at the feed. [gr]\[SecurityRoomSpyingRepeat\]":
                $ w1ExSecurityRoomSpyingRepeat = True
                show screen textbox2 with dissolve
                pass
            "Nah, I don't need to see other people fucking.":
                show screen textbox2 with dissolve
                mct "(Better not. I have other things I should be doing anyway.)"
                jump w1ExSecurityRoom

        mct "(Yeah, let's take a look at what some of the rich perverts are getting up to.)"

    else:
        scene w1_2308 with dissolve
        mct "(I've already wasted enough time here.)"
        jump w1ExSecurityRoom

    scene w1_2305 with pixellate
    mct "(That's... Dalia.)"
    "She's with two men, having one grovel at her boot while the other sits outside, looking in."
    "The man is emphatically shining her leather boots with his tongue."
    "To be honest, I didn't expect this kind of activity from a member of this club, but it makes sense."
    "If you had a high-stress job that required utter control, letting go of it in the bedroom must be pretty freeing."
    mct "(Now, let us see what's going in another room.)"
    scene w1_2306 with pixellate
    "The next image was of a fat man, spanking a busty, beautiful redhead dressed in a schoolgirl uniform."
    mct "(To be honest, this seems so...)"
    "Mundane. Common place. A little boring even."
    scene w1_2307 with pixellate
    mc "What the fu..."
    "The next screen was more of what I expected from this place, causing me to mutter audibly in confusion."
    "A tall, bald man was watching two prostitutes wrestle, dick hard in his hand as he called out words of encouragement."
    "After the man had decided the match was concluded, his emptied his bladder on the loser as some kind of parting punishment."
    scene black with fade
    mct "(That's enough for now. I don't think I want to dig any further.)"
    jump w1ExSecurityRoom


label w1ExVeronica:
    if _in_replay:
        show screen textbox2 with dissolve
    if w1ExVeroRepeat == False:
        $ w1ExWarrenGoneScore += 1
        $ w1ExVeroRepeat = True
        scene w1_2309 with dissolve
        $ renpy.music.play("music/sonatina-in-c-minor.mp3", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
        "I decided to pop into the dressing room and see if the girls were already here."
        "Instead of three, I found only one."
        "Veronica stood in the center of the room, stark naked, peering back at herself through a mirror. So entranced with whatever's going on in her mind that she didn't hear me enter."
        "Or if she did, she didn't care, though I figured the first is far more likely."
        scene w1_2311 with dissolve
        mct "(Even from the back, I'm picking up on some really intense vibes right now...)"
        "Should I announce my presence?"
        hide screen textbox2 with dissolve

        menu:
            "Clear your throat and get Veronica's attention. [red]\[Toughness -1\]":
                $ toughness -= 1
                scene w1_2310 with dissolve
                show screen textbox2 with dissolve
                mc "*Ahem*"
                "I cleared my throat to get the statuesque woman's attention."
                ver "...eh?"


            "Watch Veronica in silence.":
                show screen textbox2 with dissolve
                "I decided to watch the red-headed amazon for at least a little while longer."
                "There was something about the way she stood, back straight and shoulders evenly squared, that held my attention."
                "Veronica, at the moment, seemed so sky-high and impervious to the humiliation she was facing in just a few hours."
                scene w1_2312 with dissolve
                ver "Hmm..."
                scene w1_2313 with dissolve
                "To my surprise, the brawny woman began to... {b}preen{/b}?"
                scene w1_2314 with dissolve
                "Followed by a deep, heavy sigh."
                scene w1_2315 with dissolve
                ver "You got this, Veronica."
                ver "Just put everything {b}else{/b} out of your mind."
                scene w1_2316 with dissolve
                ver "You've got what it takes to win this..."
                "She was talking herself up...?"
                scene w1_2317 with dissolve
                ver "Hmm....?"
                "Suddenly noticing my present, Veronica began to turn and face me."

        scene w1_2318 with dissolve
        ver "[mcf]..."
        ver "How long were you standing there?"
        scene w1_2319 with dissolve
        "A hint of red spread across her cheeks."
        scene w1_2320 with dissolve
        mc "Not long. I just got here."
        scene w1_2321 with dissolve
        ver "Good."
        scene w1_2322 with dissolve
        "......"
        "..."
        "A few, awkward moments passed by uninterrupted."
        scene w1_2323 with dissolve
        ver "So? You're here to perv or something?"
        scene w1_2324 with dissolve
        mc "No, just thought I'd check in and see if anyone had arrived."
        scene w1_2323 with dissolve
        ver "Y'know, that doesn't refute what I asked, right?"
        scene w1_2324 with dissolve
        mc "Heh, I guess it doesn't."
        scene w1_2325 with dissolve
        mc "Well, I guess I should leave you--"
        stop music fadeout 3.0
        scene w1_2326 with dissolve
        "As I turned to leave, Veronica put a hand on my shoulder to stop me."
        ver "I want to ask you something, errand boy."
        scene w1_2327 with dissolve
        mc "Yeah...?"
        scene w1_2328 with dissolve
        ver "You find me attractive, of course."
        scene w1_2329 with dissolve
        mct "(...huh? Was that a question or a statement?)"
        scene w1_2330 with dissolve
        "Veronica stepped forward, shrinking the distance between us."
        mc "What are you...?"
        scene w1_2331 with dissolve
        play music "music/jack-the-lumberer.mp3"
        "Before I could get the words out, Veronica took me by the wrist and placed both of my hands on her chest."
        scene w1_2332 with dissolve
        mc "Can I help you with something?"
        scene w1_2333 with dissolve
        "Her answer came in the form of an action, as she slid both hands down to my crotch and vigorously rubbed my groin." with vpunch
        "Naturally, my lower half began to react."
        ver "I'm just checking something."
        scene w1_2334 with dissolve
        "Veronica leveled her eyes with mine, curling her lips into a half-parted, seductive smirk."
        mc "Umm..."
        "Her strong, calloused hands had a firm grip on my cock. It wasn't unpleasant, to say the least."
        scene w1_2335 with dissolve
        ver "Well...?"
        scene w1_2334 with dissolve
        hide screen textbox2 with dissolve

        menu:
            "Manhandle Veronica's tits. [gr]\[Veronica +1\]":
                $ Veronica_Horniness +=1
                scene w1_2337 with dissolve
                show screen textbox2 with dissolve
                "Throwing caution to the wind, I sank my fingers deeper into the freckled flesh of her breasts."
                ver "Ah..."
                "It was quite something to find something so soft and pliant on the amazon's rock-solid physique."
                scene w1ExVeroGrope with dissolve
                "Greedily, I snaked my hands to the side of her breasts, and gave them a big squeeze, pressing the sizable orbs together and creating a beautiful display of cleavage."
                scene w1_2338 with dissolve
                ver "Oh... yeah. You do."
                scene w1_2345 with dissolve
                "One of my hands, with a mind of its own, worked its way down to the front of her left breast."
                ver "I can--"
                scene w1_2346 with hpunch
                "--and gave it a great, big tug."
                ver "Ngg~! Hmhheha..."
                if Veronica_Horniness >= 4:
                    "To my surprise, Veronica didn't stop the rough treatment. Instead, she let out a honeyed cry."
                    "Well, she WAS the one who initiated this."
                    scene w1_2336 with dissolve
                    mc "*Slurp*"
                    ver "Hmm?"
                    "I decided to get greedy, bringing my mouth to one of her nipples and latching on."
                    mc "*Slurp* *Slurp*"
                    scene w1_2348 with dissolve
                    "Almost instantly, the soft tips of her breasts hardened into tiny, rosy pebbles."
                    ver "Ehehe--! W-what are you, a baby?"
                    scene w1_2350 with dissolve
                    "I decided to answer her question with a more voracious attack."
                    ver "Ughh...! Haah... {size=-2}Haah... {/size=-2}{size=-4}F-feels... {/size=-4}{size=-6}good~♥{/size=-6}"
                    if w1ExMamaBoyRepeat == True:
                        mct "(Shit, maybe that breast feeding lawyer is onto something. This is great!)"
                    scene w1_2349 with hpunch
                    ver "S-stop!"

                else:
                    scene w1_2347 with dissolve
                    ver "You do."
                    ver "I can compete."

            "Let your hands linger as you make sense of what's going on.":
                show screen textbox2 with dissolve
                mc "...?"
                ver "Hmm..."
                "She continued to run a hand over my increasingly hardening cock."
                scene w1_2335 with dissolve
                ver "Yeah. You do."
                ver "I can compete."

        scene w1_2351 with dissolve
        "Just as quickly as her advance began, Veronica pulled back. Leaving me worked up, but not as confused as I expected to be."
        ver "Yep. That blonde doesn't have anything on me."
        mct "(Ah, she was worried about the competition...)"
        scene w1_2352 with dissolve

        if Veronica_Horniness >= 4:
            ver "Sorry, for getting up in your space like that. You REALLY didn't seem to mind though."
            mct "(Yeah, neither did you...)"
        else:
            ver "Sorry, for getting up in your space like that. You didn't seem to mind though."

        scene w1_2353 with dissolve
        mc "Happy to help, I think. But..."
        scene w1_2354 with dissolve
        mct "(Part of my job here is to keep the girls motivated. I should say something encouraging.)"
        hide screen textbox2 with dissolve

        menu:
            "Tell her she doesn't have anything to worry about.":
                scene w1_2355 with dissolve
                show screen textbox2 with dissolve
                mc "You don't have anything to worry about, y'know? In the looks department, I mean..."
                scene w1_2354 with dissolve
                ver "..."

            "Tell her not to get complacent. [gr]\[Toughness\] \[Veronica +1\]":
                $ toughness += 1
                $ Veronica_Affection += 1

                scene w1_2356 with dissolve
                show screen textbox2 with dissolve
                mc "You're an attractive woman, but you better not get complacent."
                mc "You know better than the other two that there's more to this competition than just looking good."
                scene w1_2357 with dissolve
                ver "...I do."
                scene w1_2358 with dissolve
                mc "Use that to your advantage."
                mc "The most important thing is to keep your motivation up. If you can do that, you'll win the exhibition."
                scene w1_2359 with dissolve
                ver "You don't have to worry about that, errand boy."

        scene w1_2352 with dissolve
        $ history_veronica = "I caught Veronica preening in front of a mirror, seemingly concerned about the competition. After some hands on reassurance, I did my best to encourage her."
        $ unread_veronica = True
        play sound "sound effects/notification.wav"
        show bioupdate with dissolve
        ver "You were about to leave, right? Don't let me stop you."
        scene w1_2351 with dissolve
        if not persistent.veroEx1Grope:
            play sound "sound effects/notification.wav"
            show memoryunlock with dissolve
            $ persistent.veroEx1Grope = True
        mct "(Right, guess she got what she wanted from me.)"
        scene w1_2360 with dissolve
        mc "Alright then, see you soon."
        $ renpy.end_replay()
        jump w1ExDressingRoom

    else:
        scene w1_2384 with dissolve
        mct "(I've already had quite the interesting encounter here. I should go do something else.)"
        jump w1ExDressingRoom


label w1ExVIPSamson:

    scene w1_2383 with dissolve
    mct "(If put myself in the middle of all this, I probably won't be able to slip away until it's time to retrieve the girls.)"
    "Am I ready to continue?"
    hide screen textbox2 with dissolve

    menu:
        "Yes, continue.":
            pass
        "No, let's look around some more.":
            show screen textbox2 with dissolve
            jump w1ExVIPLounge

    show screen textbox2 with dissolve
    "The first thing that hit me about the VIP lounge was the smell."
    "It smelled what I imagined {i}class{/i} to smell like: a medley of wood polish, cigar smoke, and hops."
    scene w1_2361 with dissolve
    "At the bar, stood August, idly waiting with a service-quality smile permanently etched on his face."
    "The consummate picture of a perfect bartender, in his hand was a glass being perpetually polished to a sheen."
    scene w1_2362 with dissolve
    "Off to his side, sitting at the end of the bar and gazing up at the stage with a distant look, was the woman accompanying Dr. Van Doren."
    "She looked dispassionate as she was beautiful. Uninterested in anything in particular or perhaps just doing her best to be a part of the background and go unnoticed."
    scene w1_2363 with dissolve
    "On the stage at the back of the room was Harper, her lithe body twisting and blurring as she danced with the bronze pole."
    "She was putting on quite the enthusiastic display of her athletic talents, one that nearly no one seemed to be paying attention to."
    scene w1_2364 with dissolve
    "Seated in front of the stage, was a mixture of both familiar and unfamiliar faces. At the center of the men, face down and writhing uncomfortably was..."
    mct "(Is that Lucy...?)"
    scene w1_2366 with dissolve
    lucy "Gh..!"
    "Gagged and blindfolded, the school teacher turned whore's stifled moans was muddled by the dull mechanical whirling of numerous sex toys."
    scene w1_2367 with dissolve
    "She was propped up on the table like she was a piece of art, while the men around her casually chatted and enjoyed a smoke."
    scene w1_2364 with dissolve
    mct "(Man, how do I even naturally interject myself into a scene like that...?)"
    "Thankfully, it turned out I didn't have to find my own opening."
    scene w1_2365 with dissolve
    sam "Hey, kid. Get over here. We were just discussing this summer's carnations."
    "Samson immediately recognized me and called me over."
    scene w1_2368 with dissolve
    man "A new face. Who's this, Sam?"
    scene w1_2369 with dissolve
    sam "The kid is Kat's new assistant -- or whatever she calls 'em."
    scene w1_2370 with dissolve
    mc "[mcf]. Nice to meet you all."
    scene w1_2371 with dissolve
    sam "Ah, right. Let's be quick with the introductions."
    scene w1_2372 with dissolve
    sam "This bald bastard is Frank."
    scene w1_2373 with dissolve
    frank "Kat's new assistant, eh? My sympathies."
    "He shot me an odd, knowing smirk and left it at that."
    scene w1_2374 with dissolve
    sam "The tubby, shifty looking fellow in presidential blue is Jim."
    scene w1_2375 with dissolve
    "The man gave me a lazy, simple wave in turn and gave me a scrutinizing look."
    mct "(That's the chief of police that I spied on in the security room.)"
    scene w1_2376 with dissolve
    sam "The {i}friendly{/i} face next to him belongs to Eric Waylon. Say hello, Eric."
    scene w1_2377 with dissolve
    "*Gulp*"
    scene w1_2378 with dissolve
    eric "Hello, Eric."
    scene w1_2379 with dissolve
    sam "Wha-- pfhahaha, was that a joke? From you? Bahaha! Ah, where was I? Next is..."
    scene w1_2380 with dissolve
    abel "We've already had the pleasure of being introduced."
    scene w1_2381 with dissolve
    sam "You have? Well, great! We all know each other now! So, sit down and talk a little with us, kid."
    "The former actor gestured to the empty seat across from him, a plush leather armchair positioned at Lucy's head."
    scene w1_2382 with dissolve
    mct "(No reason to refuse, it's what I'm here for.)"
    scene w1_2388 with dissolve
    frank "Now that [mcf]'s here, you're just an old man like the rest of us, Sam. You can drop the attitude now."
    scene w1_2389 with dissolve
    sam "I don't know what you're talking about, Frank."
    scene w1_2390 with dissolve
    abel "This is my first summer as a member myself."
    scene w1_2391 with dissolve
    "Dr. Van Doren spoke directly to me with a soft, grandfatherly voice."
    scene w1_2392 with dissolve
    abel "This place was known to me, but I'm an old man. I thought these days were past me."
    scene w1_2393 with dissolve
    mc "What made you change your mind?"
    scene w1_2394 with dissolve
    "The old researcher paused, stretching his lips into a thin smile."
    scene w1_2395 with dissolve
    abel "I've known Kat for some time. She does wonderful charity work."
    scene w1_2396 with dissolve
    lucy "Ah... EEEEhhhee~hee...!"
    "The grandfatherly looking man paused, letting the worst of Lucy's sudden outburst pass before continuing."
    scene w1_2397 with dissolve
    abel "I guess my curiosity about her {b}other{/b} work finally got the better of me."
    scene w1_2398 with dissolve
    "It was peculiar to hear Dr. Van Doren speak about {i}wonderful charity work{/i}, while Lucy groaned and writhed from over-stimulation just a few feet away."
    "Not a single man was giving her a single thought, paying her no more mind than they would an ashtray."
    scene w1_2399 with dissolve
    mc "What's this?"
    scene w1_2400 with dissolve
    "Instead of answering me, she gestured toward the bar with an overt motion."
    scene w1_2401 with dissolve
    "August had a glass raised in a silent toast."
    mct "(He's saying: let loose and fit in.)"
    "For what it was, it felt like a nice gesture. A senior co-worker providing a gentle nudge to a new hire."
    scene w1_2402 with dissolve

    if toughness >= 15:
        mc "Thank you."
    else:
        mc "Thank you, Miss."

    scene w1_2403 with dissolve
    "I raised the glass in acknowledgement and silently returned the toast."
    scene w1_2404 with dissolve
    mct "(Damn...!)" with vpunch
    "The contents of the glass was an extravagantly smooth whiskey, with notes of vanilla, oak, and caramel."
    scene w1_2405 with dissolve
    mct "(If I had to guess, this has gotten be the most expensive liquid I've tasted.)"
    "It was certainly an acquired taste, but it was something I could see myself getting used to."
    scene w1_2406 with dissolve
    sam "Eh, now where were we just a minute ago?"
    scene w1_2407 with dissolve
    eric "We were discussing who we thought had the best chance of winning tonight."
    scene w1_2406 with dissolve
    sam "Ah, yeah. That's right."
    scene w1_2408 with dissolve
    mc "You were talking about the girls?"
    scene w1_2409 with dissolve
    jim "Hmmm, it just hit me, your voice..."

    if w1VeroGonzo == True:
        jim "Ah! You were the one who filmed that muscular tart's interview."
        scene w1_2410 with dissolve
        mc "Veronica, you mean? Yeah, that was me."
        scene w1_2409 with dissolve
        if w1GonzoReward == True:
            jim "I ended up putting my money on her. Lets hope that freak show doesn't disappoint."
        else:
            jim "She seemed... interesting, but I ended up putting my money on that blonde bombshell."


    if w1FelGonzo == True:
        jim "Ah! You were the one that filmed that blonde bombshell's interview."
        scene w1_2410 with dissolve
        mc "Felicia, you mean? Yeah, that was me."
        scene w1_2409 with dissolve
        if w1GonzoReward == True:
            jim "I ended up putting my money on her. Lets hope that dumb slut doesn't disappoint."
        else:
            jim "She seemed like a proper bitch, but I ended up putting my money on that freak show."


    if w1RoseGonzo == True:
        jim "Ah! You were the one who filmed that busty brunette's interview."
        scene w1_2410 with dissolve
        mc "Rosalind, you mean? Yeah, that was me."
        scene w1_2409 with dissolve
        if w1GonzoReward == True:
            jim "I ended up putting my money on her. Lets hope that fat tittied slut doesn't disappoint."
        else:
            jim "She certainly has the body for this, but I ended up putting my money on that freak show."

    scene w1_2411 with dissolve
    "Oddly enough, the possessive part of me felt irritated at his words."

    if w1RosalindPhoto == True:
        "Even if just hours earlier I made Rosalind write similarly degrading things on her body, these girls were my charge and he was speaking about them as if they weren't even people."
    else:
        "These girls were my charge and he was speaking about them as if they weren't even people."

    scene w1_2412 with dissolve
    eric "That Felicia woman is going to win this."
    "The dour looking man who had been mostly silent up to this point volunteered his thoughts."
    scene w1_2413 with dissolve
    frank "Oh? Do tell, Waylon. What makes you say that?"
    scene w1_2414 with dissolve
    eric "It's simple. She's the first woman in club history to {i}volunteer{/i} for this. Plus, you can tell she's confident."
    eric "I don't mean bravado, like that red-head. I mean the genuine, self-assured article."
    scene w1_2415 with dissolve
    "Satisfied that he had said he piece, he leaned back and once more adopted a disinterested look."
    scene w1_2416 with dissolve
    frank "Nonsense. She's in over her head. She's got no foundation."
    frank "Nothing to draw from and keep her going. Rosalind's going to take this thing."
    scene w1_2417 with dissolve
    "The bald man confidently offered his refutation. It would seem that they're all at least passingly familiar with each of the carnation's personal situation."
    scene w1_2418 with dissolve
    sam "You two are both way off the mark, it--"
    scene w1_2419 with dissolve
    lucy "Ah... k-kahah... aaaah...!"
    "A shrill cry interrupted the aging actor's thought, as an orgasm rocked Lucy's body."
    play sound "sound effects/thud-floor.mp3"
    scene w1_2420 with vpunch
    sam "You two are both way off the mark, it's {i}Nicki{/i} that's going to win."
    scene w1_2421 with dissolve
    frank "You really have confidence in your scheme."
    mct "(Scheme...?)"
    scene w1_2422 with dissolve
    mc "What does he mean by scheme?"
    "I couldn't help myself from asking."
    scene w1_2423 with dissolve
    sam "That's right. You don't know, huh?"
    scene w1_2424 with dissolve
    abel "It seems [mcf] and I are both in the dark on this."
    scene w1_2425 with dissolve
    jim "Yeah, what is Frank talking about?"
    scene w1_2426 with dissolve
    sam "You dirty old bastards are going to love this."
    scene w1_2427 with dissolve
    "Samson lurched forward, a clear gleam of excitement in his eyes. Whatever he was about to say, this was undoubtedly a chance for him to brag and he seemed intent on relishing it."
    scene w1_2428 with dissolve
    sam "Well Nicki, that fine slab of muscle, she's here because her gym's failing, yeah?"
    scene w1_2429 with dissolve
    mc "What about it?"
    scene w1_2426 with dissolve
    sam "I had a direct hand in that. Dumb bitch doesn't even realize."
    scene w1_2429 with dissolve
    mct "(Is that pompous jerkward saying...?)"
    scene w1_2430 with dissolve
    jim "You set her up? That's rich."
    scene w1_2431 with dissolve
    sam "Hehehe, that's right. The details aren't important, but you'd be impressed."
    sam "Her business is in the hole and it's all because of me. After that, it was easy to send that one-track minded idiot running into Kathy's arms."
    scene w1_2432 with dissolve
    jim "Yeah, yeah, yeah..."
    scene w1_2433 with dissolve
    sam "I'll say it took a lot more finesse to get her here than this whore though. Ha!"
    "There was something about seeing that idiot's face twist vulgarly into a laugh that ticked me off. What was it?"
    scene w1_2385 with pixellate
    ver "You see this, errand boy?"
    scene w1_2386 with dissolve
    mc "An empty gym?"
    scene w1_2387 with dissolve
    ver "Not quite. It's my fucking dream. I'm not going to get into it, but some shit's really been working against me lately."
    ver "I'm going to fight tooth and nail to keep this place afloat."
    scene w1_2434 with dissolve
    mc "......"
    mc "..."
    scene w1_2435 with dissolve
    mct "(He's trampling over another's person dream.)"
    "I don't know her very well, but I can tell Veronica is a hard worker. That much is very obvious."
    mct "(He's shitting on a dream she's working hard toward.)"
    "Every fiber of empathy I had in my body stood on edge in agitation."
    "I thought of my own goals, of how fucked it'd be for some unseen hand to callously sabotage that. I felt sick to my stomach."
    "At that moment, I resolved to do one thing."
    hide screen textbox2 with dissolve

    menu:
        "Help Veronica get her business back on track. [gr]\[VeroFlag\] \[Sam +1\]":
            $ VeroFlag = True
            $ Sam_Friendship += 1
            show screen textbox2 with dissolve
            "That's right. If her business troubles are Samson's doing, whatever he did, perhaps they can be undone."
            scene w1_2436 with dissolve
            "I could take a look into, perhaps even leverage my proximity to the man to get him to spill the beans. It's not a guarantee, but..."
            scene w1_2435 with dissolve
            "Even if she loses at the end of the month, she might still be able to get what she wants."
            "I'm pretty sure the bosses wouldn't look too kindly on my interference, but if I'm careful, they don't have to know."
            scene w1_2437 with dissolve
            $ history_samson = "Samson admitted to having a hand in Veronica's business woes, a revelation that pisses me off to no end. If I want to help her, the first step should be finding out exactly what he did to sabotage her."
            $ unread_samson = True
            play sound "sound effects/notification.wav"
            show bioupdate with dissolve
            mc "You're really impressive, Mr. Garcia."
            scene w1_2439 with dissolve
            sam "Well, I like to make myself useful to the club."
            sam "I'm at your service, after all. Ha!"


        "Ignore your feelings, it could jeopardize your own dream.":
            show screen textbox2 with dissolve
            "Putting myself in the middle of the affairs of a club patron and one of the club's money makers doesn't seem smart."
            scene w1_2438 with dissolve
            "This job needs to work out. Totally free of student debt..."
            mct "(Yeah, no. I shouldn't stick my nose into it.)"
            scene w1_2440 with dissolve
            $ history_samson = "Samson admitted to having a hand in Veronica's business woes, a revelation that pisses me off, but I ultimately decided wasn't any of my business."
            $ unread_samson = True
            play sound "sound effects/notification.wav"
            show bioupdate with dissolve
            jim "That doesn't mean she's going to win, you oaf."
            scene w1_2441 with dissolve
            sam "Nah, I'm saying, I know how to pick 'em..."

    scene w1_2442 with dissolve
    sam "Ah, Isaak! Didn't see you slip in."
    mct "(It seems that he had finally creeped in following the confrontation with Hana.)"
    scene w1_2443 with dissolve
    sam "You look angry, something wrong?"
    isak "Shut up."
    mct "(He still seems to be stewing about it too.)"
    sam "Aw, don't be like that..."
    scene w1_2444 with dissolve
    kat "Good evening, gentleman. Sorry to interrupt."
    kat "You all look well tonight."
    scene w1_2445 with dissolve

    if kat_polite == True:
        "Mrs. Pulman had slipped in unnoticed while Samson pestered Isaak."
    else:
        "Kathleen had slipped in unnoticed while Samson pestered Isaak."

    "She had since changed into a tight-fitted, strikingly gold dress."
    scene w1_2446 with dissolve
    sam "You don't look half bad yourself, Kathy."
    scene w1_2445 with dissolve
    jim "Yeah, why don't you come over here and sit in my lap? Hehehe."

    if kat_polite == True:
        "There was a little laughter shared between the two, but Mrs. Pulman seemed to pay no mind."
    else:
        "There was a little laughter shared between the two, but Kathleen seemed to pay no mind."

    scene w1_2447 with dissolve
    kat "As handsome as you are Mr. O'Doherety, I'm afraid there isn't much time for that."
    scene w1_2448 with dissolve
    kat "All the Carnations have arrived. If you'll see to them [mcf], the exhibition will start in 30 minutes."
    scene w1_2449 with dissolve
    mc "Yes, Ma'am."
    "She was telling me to head to the dressing room."
    scene black with fade
    stop music fadeout 3.0
    mct "(The shoe is about to drop.)"
    kat "If I could get everyone to join us in the stage room..."
    "......"
    "..."
    play sound "sound effects/door-openclose.wav"
    scene w1_2450 with fade
    play music "music/horrible.mp3"
    "All three sets of the dressing room occupants' eyes fell on me as soon as I entered."
    fel "Hey, boss man!"
    "Felicia was the only one who greeted me, voice overflowing with an excited, chipper song-like energy."
    "Rose only mustered a weak, anxiety-ridden smile."
    "While Veronica simply stood there like a stone statue, looking like her mind was already in the midst of the exhibition."
    scene w1_2451 with dissolve
    mc "Everyone's gathering in the exhibition hall right now, but before we head there..."
    scene w1_2452 with dissolve
    mc "How are you three?"
    scene w1_2453 with dissolve
    fel "Little anxious, but ready to get out there."
    scene w1_2454 with dissolve
    ver "You're anxious? You?"
    scene w1_2455 with dissolve
    fel "It's the first night. Who knows what to expect?"
    fel "It's exciting, but I'd be lying if I said I'm not a little nervous."
    scene w1_2456 with dissolve
    ver "..."
    "Veronica looked at her incredulously."
    scene w1_2457 with dissolve
    fel "Hehe, I'm not a robot..."
    scene w1_2458 with dissolve
    fel "Oh...!"
    scene w1_2459 with dissolve
    fel "You already had a taste of this place, right? A couple of weeks ago? That's what the boss lady said..."
    fel "What did they make you do?"
    scene w1_2460 with dissolve
    ver "..."
    scene w1_2461 with dissolve
    fel "Aw, c'mon. Tell me. It'll break the ice."
    fel "If you guys go out there like that, you won't have any fun. You look like you're about to shit a diamond."
    scene w1_2462 with dissolve
    ver "Fun...? Get out of my face, blondie."
    scene w1_2463 with dissolve
    fel "..."
    scene w1_2464 with dissolve
    fel "Sorry, I'm being an ass. Chalk it up to pre-game jitters."
    "Thankfully Felicia read the room and reeled herself in. For being as seemingly shameless as she is, she at least had that degree of emotional intelligence."
    fel "I know we are all here for different reasons..."
    scene w1_2465 with dissolve
    ver "Eugh, whatever..."
    scene w1_2466 with dissolve
    ver "It's no big deal. All I'm going to say though is it sucked."
    scene w1_2467 with dissolve
    mc "What about you, Rose? How you feeling?"
    scene w1_2468 with dissolve
    "I turned my attention to the one Carnation that had been conspicuously silent."
    scene w1_2470 with dissolve
    "The look she gave me in return said it all before she even had to."
    scene w1_2469 with dissolve
    rose "I'm ready."
    scene w1_2470 with dissolve
    "Looking directly at me with her beautiful baby blues, she seemed firm and absolute."
    scene w1_2471 with dissolve
    mc "Alright, seems you guys are all ready, then."
    mc "Don't be afraid to rely on each other tonight."
    scene w1_2472 with dissolve
    fel "You don't need to say it twice!"
    "Felicia response came without delay, while the other two..."
    "Seemed less convinced now that it was showtime. The red-headed amazon and desperate mother simply looked away and didn't say anything."
    scene black with fade
    stop music fadeout 3.0
    mc "You can follow me to the stage."
    "......"
    "..."
    jump w1ExFinallyActuallyStart


label w1ExFinallyActuallyStart:

    scene w1_2473 with curtains
    "After some standing around waiting out the remaining time, the exhibition finally came to a start."
    "Everyone had gathered on the exhibition hall's floor, patron and house girl intermingling, as they looked up expectantly at the stage, where Mrs. Pulman waited to address them."
    "We were positioned at the back, waiting to be introduced, so we could each individually march up the aisle like a prize fighter making his introduction."
    scene w1_2474 with dissolve

    if kat_polite == True:
        "A gentle, subtle nod from Mrs. Pulman signaled to me she was about to begin."
    else:
        "A gentle, subtle nod from Kathleen signaled to me she was about to begin."

    scene w1_2475 with wipeleft
    "I resisted the temptation to shoot the girls one last anxious look."
    scene w1_2476 with fade
    play music "music/epic-battle-speech.mp3"
    kat "......"
    kat "..."
    scene w1_2477 with dissolve
    kat "Gentlemen! Welcome to the Carnation Club's fifth annual summer exhibition."
    scene w1_2478 with dissolve
    kat "My... how time does fly, doesn't it? It's been five years since I first had the pleasure to stand up on this stage before you."
    kat "Our numbers were few then, but we all shared a common appetite, one that went unfulfilled in the daily pursuit of unchallenged excellence and success."
    scene w1_2479 with dissolve
    kat "Five years, yet from up here, not a single one of you looks a day older. The only thing that's changed about your faces is the {b}number{/b}."
    kat "I can't tell you how much your presence here tonight means to me personally. It gives me a certainty of purpose, that breaking in desperate sluts for your viewing pleasure is a worthwhile calling."
    scene w1_2480 with dissolve
    play sound "sound effects/applause-small.wav"
    "With that, the murmuring crowd gave way to a round of applause, seemingly pleased by Mrs. Pulman's ridiculous pat on the back."
    "To me, it sounded like a lip service, but they seemed satisfied with her words."
    stop sound
    scene w1_2481 with dissolve
    kat "Before we bring out this year's Carnations, I want to make a special introduction."
    mc "Come up here, [mcf]."
    scene w1_2482 with dissolve
    mct "(Ah, shit...)"
    scene w1_2483 with dissolve
    "I suppose it was inevitable I make a formal introduction."
    "I had personally met about half of them already, but this was only proper I guess."
    scene w1_2484 with fade
    "Once on stage, I became all too aware of the leering crowd settled in front of the stage."
    scene w1_2485 with dissolve
    "My eyes didn't focus on any one face in particular, but the shape and form of their collective mass."
    "It was grotesque. More than a dozen faces twisted in a imitation of a human smile, but whose true nature was utterly betrayed by vacant, animal-like eyes."
    scene w1_2486 with dissolve
    kat "As some of you know, Darius has left our employ under amicable terms. He'll be missed, but we wish him all the well. Replacing him is Mister..."
    scene w1_2487 with dissolve
    "Kathleen made a gesture toward me, prompting me to introduce myself."
    scene w1_2488 with dissolve
    hide screen textbox2 with dissolve

    menu w1ExhibitionPCIntro:

        "Match Kathleen's example and show deference to the crowd. [gr]\[Kathleen +1\]":
            $ Kathleen_Trust += 1
            show screen textbox2 with dissolve
            "I figured the quickest way to ingratiate myself to the crowd was to follow my boss' example."
            scene w1_2489 with dissolve
            mc "Hello. My name is [mcf] [mcl] and I'll be in your service both tonight and well into the future."
            mc "I've had the pleasure of being introduced to some of you already, but it's nice to meet you all."
            scene w1_2490 with dissolve
            sam "He's certainly more polite than that last prick!"
            "A few in the crowd quietly chuckled at the in-joke."
            scene w1_2491 with dissolve
            kat "Yes... he does seem more suitable for the role, doesn't he?"
            "She seemed pleased with my ass-kissing."
            scene w1_2499 with dissolve
            kat "Now, let's move onto why you're here."


        "Introduce and share a little bit about yourself. [gr]\[Chuck +1\]":
            $ Chuck_Friendship += 1
            show screen textbox2 with dissolve
            "Put on the spot, my default reaction was a genuine one."
            scene w1_2492 with dissolve
            mc "Hey. I'm [mcf] and I'm a college student. My hobbies are watching movies and studying..."
            mc "Uh, I'm still learning the ropes of this place, so bare with me please."
            scene w1_2493 with dissolve
            jim "Where'd you find this kid, Kathy? He seems so earnest."
            scene w1_2494 with dissolve
            kat "Oh, you're going to find out tonight that looks can be deceiving."
            mct "(What does she mean by that...?)"
            scene w1_2495 with dissolve
            chuck "There's nothing wrong with being a little earnest, Jim."
            scene w1_2496 with dissolve
            aug "Yeah, you should try it sometime, you cop bastard!"
            "The crowd livened up at Mr. Byrne's joke."
            jim "Ah, fuck you, you second-rate gangster."
            scene w1_2499 with dissolve
            kat "Let's move onto why you're here, shall we?"
            if kat_polite == True:
                "Mrs. Pulman ushered the focus back on her, reeling the crowd in before they could get too rowdy."
            else:
                "Kathleen ushered the focus back on her, reeling the crowd in before they could get too rowdy."



        "Be concise with your introduction [gr]\[August +1\]":
            $ August_Friendship += 1
            show screen textbox2 with dissolve
            mct "(No point in dragging it out. I've already been introduced to half of them anyway.)"
            scene w1_2497 with dissolve
            mc "You guys aren't here for me, right? So I'll be brief."
            mc "I'm [mcf]. Nice to meet you."
            scene w1_2498 with dissolve
            frank "The boy's right. Bring out the sluts!"
            "The crowd made noise in agreement."
            scene w1_2499 with dissolve
            kat "Hmm, very well..."

    scene w1_2500 with dissolve
    kat "Now that you've met the newest member of our family, it's my pleasure to introduce to you this summer's Carnations, live and in person."
    stop music fadeout 3.0
    kat "Come on up, Mrs. Carter. Greet the men whose patronage will possibly pull you out of the hole you're in."
    scene w1_2501 with dissolve
    "For a brief moment, Rosalind looked like a deer caught in the headlights."
    rose "Oh, uh..."
    mct "(She must've not expected to go first.)"
    scene w1_2502 with fade
    play music "music/doll-dancing.mp3"
    "However, quickly coming to her senses, she took a moment to fix her fishnet stockings before marching up the center aisle at a brisk pace."
    "The room was eerily silent as she made her advance. Each man giving a silent, lecherous appraisal with their eyes."
    scene w1_2503 with dissolve
    "Until she finally stood at the center of the stage. Not knowing where to look, her eyeline darted around the room, taking in everything but the crowd in front of her."
    scene w1_2504 with dissolve
    kat "Isn't she cute, gentlemen? Doesn't know what to do with herself."
    scene w1_2505 with dissolve
    kat "Stand up straight, dear."
    rose "S-sorry."
    scene w1_2506 with dissolve
    play sound "sound effects/slap2.wav"
    scene w1_2507 with vpunch
    "*SLAP!*"
    scene w1_2508 with dissolve

    if w1RoseGonzo == True and w1GonzoReward == True:
        kat "This piece of ass may already a fan favorite to win, but let's formally introduce the slut. State your name for the crowd, please."
    else:
        kat "State your name for the crowd, whore."

    scene w1_2509 with dissolve
    "Rosalind briefly paused, shutting her eye-lids tight, and took a deep breath."
    "A second passed."
    "Then another."
    scene w1_2510 with dissolve
    "Until finally, in a confident voice that carried clearly across the room, she spoke."
    scene w1_2511 with dissolve
    rose "My name is Rosalind Carter."
    scene w1_2512 with dissolve
    kat "Why are you here, Rosalind?"
    scene w1_2511 with dissolve
    rose "For your viewing pleasure."
    scene w1_2513 with dissolve
    kat "Ha, clever, but that's not what I meant. Tell the crowd what you seek for your prize."
    scene w1_2514 with dissolve
    rose "Well..."
    scene w1_2513 with dissolve
    kat "It isn't a difficult question, Rose. Spit it out."
    scene w1_2515 with dissolve
    rose "I'm here to clear up some personal debt."
    scene w1_2513 with dissolve
    kat "So you're just another whore willing to trade her dignity for money, then."
    scene w1_2514 with dissolve
    rose "..."
    scene w1_2516 with dissolve
    kat "A boring reason, but a tried and true one."

    if roseSeduceFlag == True:
        "Rosalind's situation had more painful nuance to it than simple cash debt, so I wonder why she's not pressing her on it?"
        "Surely the details behind her desperation would get these sick fucks salivating even more."
        mct "(Maybe she's saving it for later?)"

    kat "There you have it, Mrs. Rosalind Carter."
    scene w1_2517 with dissolve
    "Oddly enough, not a sound came from the crowd. Not from applause, nor crude comment."
    "Instead, they leered. Long and unflinchingly. Eagerly waiting for their host to introduce the next piece of meat for their salivating chops."
    scene w1_2518 with dissolve
    kil "*whispering* I've seen her grill a woman for five minutes before, looks like she's keeping it brief tonight."
    scene w1_2500 with dissolve

    if w1VeroGonzo == True and w1GonzoReward == True:
        kat "You're next, Miss Lynch. Come greet your adoring fans."
    else:
        kat "You're next, Miss Lynch. Come up to the stage, please."

    scene w1_2519 with dissolve
    fel "Remember to shake a leg!"
    scene w1_2520 with wipeleft
    "Veronica immediately sprung into action, jaunting down the aisle with a deliberate and sexy pace."
    "Back straight, she sashayed her hips like she was on a cat-walk, taking long strides that showed off her toned legs in action."
    scene black with fade
    "Just the same as with Rosalind, the room maintained a suffocating silence, as the red-headed amazon found her place on stage."
    scene w1_2521 with dissolve
    kat "What a contrast compared to plump, soft Rosalind."
    kat "I have a special one for you this summer. We've never had a Carnation this hard bodied before."
    "Veronica simply kept her head held high, eyes scanning back and forth across the crowd."
    scene w1_2522 with dissolve
    kat "It may not be to everyone's taste, but you can't deny it will be fun to work her like a horse and see just how much she can take."
    scene w1_2523 with dissolve
    sam "She can take anything you throw at her!"
    "While the rest of the pack murmured and hummed at Kathleen's lewd promise, Samson assuredly staked his claim."
    scene w1_2524 with dissolve
    kat "We'll certainly find out, won't we?"
    scene w1_2525 with dissolve
    ver "I can take anything you throw at me. I'm going to win."
    scene w1_2526 with dissolve
    "The crowd buzzed positively at Veronica's direct challenge of the club's matron."
    frank "Is it too late to change my bet?"
    scene w1_2527 with dissolve
    mc "*Whisper* I'm getting déjà vu from a few weeks ago."
    kil "I {i}love{/i} this woman."
    scene w1_2528 with dissolve
    kat "First, let's just follow Mrs. Carter's example. State your name for the crowd."
    scene w1_2529 with dissolve
    ver "Veronica Lynch."
    scene w1_2528 with dissolve
    kat "And what sad reason brings you to grace our stage tonight?"
    scene w1_2529 with dissolve
    ver "I need money to save my business."
    scene w1_2530 with dissolve
    kat "Just like her opponent. Another whore for money."
    scene w1_2531 with dissolve
    ver "This is a brothel, isn't it? Whoring is what you make your money off of too."
    scene w1_2532 with dissolve
    kat "There's a difference between you and I, dear. One that you'll soon learn."
    scene w1_2533 with dissolve
    kat "Mrs. Carter and Miss Lynch are here for similar reasons, but you gentlemen are in for a real treat. Our last Carnation isn't as banal."
    "Concluding Veronica's introduction, Kathleen stepped forward and called the last Carnation up."
    scene w1_2534 with dissolve
    kat "Make your way to the stage, Mrs. Ford."
    scene w1_2535 with dissolve
    stop music fadeout 3.0
    "Felicia stepped out as soon as she was called."
    "Unlike Veronica, there was nothing measured in her entrance."
    "Instead, she simply strolled to the stage all natural like, chest stuck out with confidence."
    scene w1_2536 with fade
    play music "music/victim-to-victor.mp3"
    "Once on stage, and able to get a full view of the crowd, Felicia smiled."
    scene w1_2537 with dissolve
    "Then that smile turned into pure elation. She was... unabashedly happy to be here."
    scene w1_2538 with wipeleft
    mc "*Whisper* How the hell can she look like that?"
    kil "Beats me."
    scene w1_2539 with dissolve
    fel "My name is Felicia Ford."
    "Instead of waiting for the question, Felicia was the first to speak, volunteering her name."
    scene w1_2540 with dissolve
    kat "Eager, aren't you?"
    scene w1_2541 with dissolve
    fel "Very."
    scene w1_2542 with dissolve
    kat "Like I said, gentlemen. Felicia is an interesting one."
    kat "She's the first time in exhibition history that we had a Carnation volunteer gleefully. She's not here because she's in dire straights, no..."
    kat "In fact, some of you may even know her. She's the wife of Elias Ford."
    scene w1_2543 with dissolve
    "There was a commotion at this news. It felt like the whole room leaned forward in excitement."
    scene w1_2544 with dissolve
    jim "I'll be fucked. That self-righteous bastard's wife is on our stage?"
    scene w1_2545 with dissolve
    eric "I told you she was going to win this."
    scene w1_2546 with dissolve
    abel "I actually knew your husband's father, Miss."
    "Dr. Van Doren directly addressed Felicia over the brouhaha."
    scene w1_2547 with dissolve
    fel "You did, Mister?"
    scene w1_2548 with dissolve
    abel "That's right. Years ago my company used his railroad for deliveries."
    scene w1_2549 with dissolve
    fel "I never got to know him that well. He passed before our wedding."
    scene w1_2550 with dissolve
    abel "Yes, he went before his time. It was a shame what happened to his company."
    scene w1_2551 with dissolve
    "Felicia just smiled at Van Doren, before returning to her place on the stage."
    scene w1_2552 with dissolve
    kat "Now, Mrs. Ford... share with the club's benefactors what you chose for your prize."
    scene w1_2551 with dissolve
    mct "(Ah, there it is. The moment I've been curious about. What would a woman like Felicia ask for?)"
    scene w1_2553 with dissolve
    fel "I want to become a member of the Carnation Club."
    scene w1_2554 with dissolve
    kat "Now THAT is an interesting stake."
    scene w1_2555 with dissolve
    kil "Hahahaha...! Ah, fuck. That woman surprises even me."
    mc "You've got to be kidding me..."
    scene w1_2556 with dissolve
    frank "What a cheeky slut!"
    jim "A woman in our ranks?"
    scene w1_2557 with dissolve
    chuck "Amazing!"
    scene w1_2558 with dissolve
    ver "What the fuck? Is she for real?"
    rose "..."
    "The two other Carnations had a look of disbelief written plainly on their faces. I can only imagine how contemptable Felicia must look to them."
    scene w1_2559 with dissolve
    kat "That's right, Felicia wishes to be counted amongst our members."
    scene w1_2560 with dissolve
    jim "Ha! As if!"
    scene w1_2561 with dissolve
    mihir "Interesting!"
    scene w1_2562 with dissolve
    "Felicia maintained a nonplussed expression throughout the commotion."
    stop music fadeout 3.0
    kat "It's a condition I happily accept. The prospect of inviting our first female member is an exciting one. However..."
    scene w1_2563 with dissolve
    fel "...?"
    scene w1_2564 with dissolve
    play music "music/leaving-home.mp3"
    kat "Mrs. Ford is under the illusion this will be fun and games, but she needs to understand something."
    scene w1_2565 with dissolve
    fel "Eh...?"
    scene w1_2564 with dissolve
    kat "Over the next month, your social status means jack shit. You're no longer Mrs. Elias Ford, you're just another pig whore deserving of contempt."
    scene w1_2566 with dissolve
    "A small smirk spread across Felicia's beautiful face."
    scene w1_2564 with dissolve
    kat "Oh, you think I'm joking...?"
    scene w1_2567 with dissolve
    scene w1_2568 with dissolve
    scene w1_2569 with dissolve
    "In a quick, rough motion Mrs. Pulman pulled down the top of Felicia's costume, exposing her breasts to the open air."
    scene w1_2570 with dissolve
    kat "Get down on your hands and knees."
    scene w1_2571 with dissolve
    fel "What?"
    scene w1_2570 with dissolve
    kat "Pigs don't stand on two legs, do they? Get down on your hands and knees, {b}pig{/b}."
    scene w1_2572 with dissolve
    fel "...sure, kinda weird, but I'm game."
    scene w1_2573 with fade
    "After a brief moment of confusion, Felicia complied. Sprawling out on all fours like an animal."
    "She made sure to look good while doing it, arching her back and hiking her ass high up in the air."
    scene w1_2574 with dissolve
    fel "Like this? You want--"
    hide screen textbox2 with dissolve
    play sound "sound effects/thud-floor.mp3"
    scene w1_2575 with vpunch
    fel "--een!"
    scene w1_2576 with dissolve
    show screen textbox2 with dissolve
    if kat_polite == True:
        "Mrs. Pulman abruptly dug the point of her right heel into Felicia's upper back, placing her full weight on it and forcing the volunteer whore's cheek to the ground with an audible plop."
    else:
        "Kathleen abruptly dug the point of her right heel into Felicia's upper back, placing her full weight on it and forcing the volunteer whore's cheek to the ground with an audible plop."

    scene w1_2577 with dissolve
    hide screen textbox2 with dissolve
    kat "Let's get a few things straight."
    scene w1_2578 with dissolve
    kat "I need to make sure we have an understanding before we commence the night's games."
    fel "What--"
    scene w1_2579 with dissolve
    scene w1_2580 with instantdissolve
    play sound "sound effects/slap2.wav"
    scene w1_2581 with vpunch
    "*SMACK*"
    "The cruel woman delivered a thundering smack onto Felicia's perfect, raised ass."
    scene w1_2582 with dissolve
    fel "Eeeh?!"
    kat "Pigs don't talk either, they oink and squeal. So lets get one thing straight, pig."
    "Felicia quickly caught on, resisting the urge to say anything."
    scene w1_2583 with dissolve
    kat "On this stage, you're not a person. You're club property. You belong to me."
    kat "You exist only for our magnanimous patron's viewing pleasure. That's what you signed up for."
    kat "I've no doubt you're accustomed to a certain level of respect in your daily life, but you'll get none of that here."
    scene w1_2584 with dissolve
    show screen textbox2 with dissolve

    if kat_polite == True:
        "Mrs. Pulman was going hard on Felicia. It seemed cruel, but I could also see the reason for the display."
    else:
        "Kathleen was going hard on Felicia. It seemed cruel, but I could also see the reason for the display."

    "If she was under the impression this would be some libertine party, she was sorely mistaken and in need of a primer of what she signed up for."
    "The fact this callous reasoning sprung to mind so easily to me was concerning, but I couldn't argue with how her treatment was making me feel."

    if toughness >= 20:
        scene w1_2585 with dissolve
        "Seeing the rich woman face down in the dirt like a worm was exciting."

    elif toughness <= 19 and feliciaFlag == True:
        scene w1_2586 with dissolve
        "Seeing the woman who had treated me to dinner and stuck up for me this week, forced face down into the dirt like she wasn't even human exasperated me. Made me feel a little angry."

    elif toughness <= 19 and feliciaFlag == True:
        scene w1_2587 with dissolve
        "Seeing the woman who's well being I was ostensibly in charge of forced face down into the dirt like she wasn't even human disturbed me."

    "Even Killian was looking a little conflicted. After all, Felicia and him are friends."
    mct "(Makes me wonder why he told her about the club in the first place...)"
    scene w1_2588 with dissolve
    hide screen textbox2 with dissolve
    kat "Oink if you understand me, pig."
    "Felicia hesitated, but only for a moment."
    scene w1_2589 with dissolve
    fel "...oink, oink!"
    scene w1_2588 with dissolve
    "Felicia let out a rough, unladylike snort in confirmation that she understood what her role would be for this month."
    kat "That didn't take long. Don't you have any shame?"
    scene w1_2589 with dissolve
    fel "...oink, oink!"
    scene w1_2590 with dissolve
    kat "No, of course you don't.  You could have all the money in the world and deep down you'd still be a classless whore."
    kat "Clean the taste of whore off my shoe."
    "Kathleen asked the golden-skinned woman for a final degrading act of submission."
    scene w1_2591 with dissolve
    kat "I said clean my shoe, pig!"
    scene w1_2592 with dissolve
    "At first, Felicia gave it a half-hearted lick, tentatively running her small pink tongue across the gold colored hide of the sadistic woman's heel."
    jim "The nasty bitch is really doing it."
    vinc "You hardly had to convince her."
    chuck "'atta girl!"
    scene w1_2591 with dissolve
    kat "Don't dally! Put some more enthusiasm into it! These kind gentlemen are waiting for the night to begin, after all.."
    scene w1_2593 with dissolve
    "Responding to another nudge from the grey-haired woman's foot, Felicia gave the shoe in front of her face a proper tongue bath."
    mct "(Is that what she expected tonight? Was this what she signed up for? Was she enjoying this?)"
    "I had to wonder."
    scene w1_2594 with dissolve
    "What ever she was feeling, she was doing a thorough job of debasing herself before the room."
    "I would be lying if I said the sight of Felicia submissively on her hands and knees was an unattractive one. Before I knew it, the fabric of my suit pants were beginning to feel a little tight."
    "If given a chance..."

    if kat_polite == True:
        mct "(Would I trade places with Mrs. Pulman?)"
    else:
        mct "(Would I trade places with Kathleen?)"

    kat "That's enough. Get up."
    scene w1_2595 with fade
    show screen textbox2 with dissolve
    stop music fadeout 3.0
    kat "We have a clear understanding of the dynamic, yes?"
    scene w1_2596 with dissolve
    fel "......"
    fel "...."
    "Felicia refused to answer the sadistic woman."
    scene w1_2597 with dissolve
    kat "Why aren't you saying anything? I asked you a question."
    scene w1_2598 with dissolve
    fel "Oink, oink?"
    "Pigs don't talk, remember?"
    scene w1_2599 with dissolve
    play music "music/epic-battle-speech.mp3"
    kat "Ha!"
    scene w1_2600 with dissolve

    if kat_polite == True:
        "Amused, Mrs. Pulman surprisingly planted a small kiss on the volunteer whore's forehead."
    else:
        "Amused, Kathleen surprisingly planted a small kiss on the volunteer whore's forehead."

    scene w1_2599 with dissolve
    kat "You're something special alright. This summer is going to be exceptional."
    scene w1_2601 with dissolve
    kat "Between our slut-wife here, this oversized slab of fuck meat, and sweet Rosalind..."
    scene w1_2602 with dissolve
    kat "This might just be our most outstanding summer exhibition yet, gentlemen."
    scene black with fade
    kat "The first game will commence once we get set up. Feel free to socialize with the Carnations."
    stop music fadeout 3.0
    "......"
    "..."
    play music "music/jazz-apricot.mp3"
    scene w1_2603 with cwside
    fel "Yeeesh, that was weird, but I'm not opposed to trying new things."
    scene w1_2604 with dissolve
    ver "You're out of your fucking gourd, you know that?"
    scene w1_2605 with dissolve
    rose "..."
    scene w1_2606 with dissolve
    kil "I expected her to grill you two more."
    scene w1_2607 with dissolve
    mc "Take the small mercies where you can get them I suppose."
    scene w1_2608 with dissolve
    sam "You girls looked mighty fine standing up there. Especially you, {i}Nicki{/i}."
    ver "Thanks..."
    scene w1_2609 with w9
    eric "You are full of surprises, Mrs. Ford."
    scene w1_2610 with dissolve
    fel "The night hasn't even gotten started."
    scene w1_2611 with w9
    tom "You are absolutely beautiful, Rose."
    rose "Oh, uh..."
    "In the brief interlude between the introduction and the night's first event, the girls were swamped by curious patrons."
    scene w1_2612 with w19
    kat "Ian. Help Warren get things set up."
    "Kathleen barked orders from off the stage."
    scene w1_2613 with dissolve
    kat "[mcf]. I need to speak with you."
    mc "Right, okay!"
    scene w1_2614 with fade
    mc "Is there something you need me to do?"
    scene w1_2615 with dissolve
    kat "No, I just wanted to let you know that you'll be center stage for the first game tonight."
    scene w1_2614 with dissolve
    mc "I'm going to be performing?"
    scene w1_2615 with dissolve
    kat "Indeed. During the exhibition season, your job is to support me in making sure we have a show worthy of the name it is under."
    scene w1_2617 with dissolve
    kat "Do a good job tonight and in the future I may just end up letting you have a creative influence over the exhibition."
    kat "I'm not opposed to that, provided you're up to the challenge. In fact, I rather hope you are. A male perspective can be useful, when pandering to other men."
    scene w1_2614 with dissolve
    mc "You've come a long way from the time you told me you had zero faith in me. What's changed?"
    scene w1_2616 with dissolve
    kat "Don't get a big head. I'm still not sold on you."
    scene w1_2618 with dissolve
    kat "Your predecessor was a dull man, only useful as a blunt instrument. I'm hoping you'll have more nuance, so I'm going to be testing you tonight, to give you a chance to prove yourself."
    scene w1_2622 with dissolve
    mct "(It's always tests with her, huh?)"
    hide screen textbox2 with dissolve

    menu:
        "Thank her for the opportunity. [gr]\[Kathleen +1\]":
            $ Kathleen_Affection +=1
            scene w1_2614 with dissolve
            show screen textbox2 with dissolve
            mc "Thanks for giving me a chance."
            scene w1_2617 with dissolve
            kat "I'm a fair woman. I won't hold your association with Ian against you unduly."
            scene w1_2614 with dissolve

        "Tell her you feel unsure at the prospect.":
            scene w1_2620 with dissolve
            show screen textbox2 with dissolve
            mc "I'm not so sure about this..."
            scene w1_2618 with dissolve
            kat "It comes with the job description, Mr. [mcl]."
            scene w1_2614 with dissolve
            mc "Right..."

    mc "How are you going to test me?"
    scene w1_2615 with dissolve
    kat "Well, as I said, you'll be front and center alongside the girls tonight."
    scene w1_2614 with dissolve
    mc "Okay, sure..."
    scene w1_2619 with dissolve
    kat "These games usually require a dick and you've got one. Quite the handsome one too."
    scene w1_2614 with dissolve
    mc "To be honest, I figured the club's patrons would be participating..."
    scene w1_2616 with dissolve
    kat "What? No. They're here to watch. For the most part."
    kat "They'll occasionally get the chance to have fun, but they do have money on the outcome each week. It'd be improper to directly involve them too much."
    mct "(Proper...? What's proper in any of this?)"
    scene w1_2614 with dissolve
    mc "That makes sense, I guess."
    scene w1_2615 with dissolve
    kat "With that being the case, we call on our male employees to fill in as needed. Namely you, Ian, and occasionally even Warren."
    scene w1_2614 with dissolve

    if id_greed == True:
        mc "You are paying me enough I suppose."
    elif id_power == True:
        mct "(If I'm going to be involved, I guess being on this side of things ain't too bad...)"
        mc "Alright."
    elif id_lust == True:
        mct "(Maybe I shouldn't think too hard about this. Just focus on having fun with three attractive women tonight.)"
        mc "Alright."

    scene w1_2617 with dissolve
    kat "Good. I'm glad we spoke."
    scene w1_2621 with dissolve
    kat "Looks like everything is in place."
    scene black with fade
    stop music fadeout 3.0
    "......"
    "..."
    scene w1_2623 with curtains
    play music "music/epic-battle-speech.mp3"
    kat "Tonight's theme is: {b}service{/b}. It's a deceptively simple word, but the nuance of quality VIP service is an art unto itself."
    kat "Good service starts from within. Its core foundation is different from woman to woman, but it is ultimately a craft that requires adaptability, intuition, and the ability to set aside your pride."
    kat "Our first game tonight will be an open-ended examination of these qualities. Each one of the Carnations will be individually tested, asked to provide VIP service to a baseline customer and his desires."
    scene w1_2624 with dissolve
    kat "Mr. [mcl] will provide that baseline for us."
    scene w1_2625 with dissolve
    mc "What do I have to do?"
    scene w1_2626 with dissolve
    kat "You? Not much. You'll privately share with me what your idealized preferences are - what kind of disposition you'd want a girl to adopt, how you'd like to be treated. That sort of thing."
    kat "I only ask that you be honest, as I'll pass that information onto August and Charles, and the three of us will judge how well each girl is able to intuit your preferences and how erotic of a show they put on."
    scene w1_2627 with dissolve
    ver "Are you saying we just got to guess what [mcf] prefers?"
    scene w1_2628 with dissolve
    kat "Not guess, {b}intuit{/b}. Weren't you listening?"
    scene w1_2627 with dissolve
    ver "Sounds like guessing to me."
    scene w1_2629 with dissolve
    kat "It isn't. Your task is to be the boldest, most nasty slut you possibly can be while sussing out Mr. [mcl]'s preferences. Try things, pay attention, and respond to how he reacts. "
    kat "The three of you having a familiarity with him to begin with should help I would think."
    scene w1_2630 with dissolve
    "Veronica didn't look convinced, which was understandable. The subjectivity of the results wouldn't be appealing from her side of things."
    scene w1_2631 with dissolve
    fel "So it's like one big play? Pretend this is a private VIP room, only..."
    fel "{i}Everyone{/i} will be watching."
    scene w1_2632 with dissolve
    kat "Yes, that works. Treat it like a... piece of theater."
    scene w1_2633 with dissolve
    fel "Sounds fun."
    scene w1_2630 with dissolve
    kat "I should mention, this week of the exhibition will be reverse elimination."
    scene w1_2634 with dissolve
    rose "What does that mean?"
    scene w1_2635 with dissolve
    kat "It means, this being a litmus test of sorts, that the winner of this event won't have to participate in the next one."
    "At the news, both Rosalind and Veronica's face lit up."
    mct "(Only having to endure one-third of the night is quite the prize.)"
    kat "Oh, I'd thought that might fire you up."
    scene w1_2636 with dissolve
    fel "So winning means I don't get to play anymore games tonight...?"
    "Felicia looked genuinely conflicted at this revelation."
    scene w1_2637 with dissolve
    kat "Now, girls. Take a seat at the back of the room while I confer with Mr. [mcl]."
    scene w1_2638 with dissolve
    ver "Sure."
    "Following the red-headed woman, the three Carnations left the stage."
    scene w1_2639 with fade
    kat "You should try to look happy. This will end up being a lot of fun for you."
    scene w1_2640 with dissolve
    mc "This is new to me, but I'll live up to your expectations. Don't worry."
    scene w1_2641 with dissolve
    kat "Glad to hear that."
    scene w1_2642 with dissolve
    mc "So what did you want to know? You said you wanted me to list my preferences?"
    scene w1_2641 with dissolve
    kat "Yes. We should keep it relatively simple too. Specific criteria would make it nearly impossible for the girls succeed."
    scene w1_2643 with dissolve
    kat "That and generalities will give the judges working room in their decisions."
    scene w1_2644 with dissolve
    "At the mention of the other judges, I looked over at Dr. Chuck, who gave me an enthusiastic thumbs up."
    scene w1_2645 with dissolve
    kat "So let's just start with..."
    kat "What kind of temperament do you look for in an ideal sexual partner?"
    scene w1_2646 with dissolve
    mct "(What is this, a Myers-Briggs test?)"
    scene w1_2647 with dissolve
    "I took a moment to mull it over."
    mct "(What kind of woman do I prefer in the bedroom?)"
    mct "(Thinking too hard about it won't do me any good. I should go with my gut here.)"
    mc "My gut says..."
    hide screen textbox2 with dissolve


    menu:
        "You like a woman who can take charge and let loose. [gr]\[InControl\]":
            $ w1ExInControl = True
            scene w1_2648 with dissolve
            show screen textbox2 with dissolve
            mc "I like a straight-forward woman. The kind that knows what she wants and takes you by the hand."
            scene w1_2649 with dissolve
            kat "You like a woman who's {b}bold{/b}, then?"
            scene w1_2650 with dissolve
            mc "Yes. Spirit and enthusiasm is important."
            scene w1_2651 with dissolve
            kat "Interesting. I thought you'd prefer a more... {i}submissive{/i} type."


        "You like a demure, obedient woman who can be slutty. [gr]\[Deferential\]":
            $ w1ExDeferential = True
            scene w1_2650 with dissolve
            show screen textbox2 with dissolve
            mc "I like a woman that can switch between classy and dirty. Demure and slutty."
            scene w1_2651 with dissolve
            mct "(Lady in the streets, freak in the sheets.)"
            kat "You want the best of both worlds?"
            scene w1_2650 with dissolve
            mc "Yes. Someone capable of switching between a passive and active role."
            scene w1_2649 with dissolve
            kat "Interesting."

        "You like an attentive woman that knows what buttons to push. [gr]\[Attentive\]":
            $ w1ExAttentive = True
            scene w1_2650 with dissolve
            show screen textbox2 with dissolve
            mc "I'd like a conscientious lover, someone who could read my body like a book and knows when to stop and knows when to go."
            scene w1_2651 with dissolve
            kat "Don't go all flowery on me. What you mean is you want a {b}sensual{/b} kind of woman?"
            scene w1_2649 with dissolve
            kat "Maybe someone to dote on you like a mother?"
            scene w1_2650 with dissolve
            mc "I didn't say that... but it could be nice."
            scene w1_2649 with dissolve
            kat "Interesting, but not totally out of line of what I expected."

    scene w1_2652 with dissolve
    kat "Let's go one deeper."
    if w1ExInControl == True:
        kat "You told me you like a woman who's in control, but what kind of path would you like her to lead you down? How would you like to be treated?"
    if w1ExDeferential == True:
        kat "You told me you like a woman with layers, but what kind of treatment would you prefer tonight?"
    if w1ExAttentive == True:
        kat "You told me you like a woman who's sensual and attentive, but where would that attention lead? What do you want her to make you feel?"

    scene w1_2647 with dissolve
    mct "(That's an even tougher question...)"
    mct "(Everyone wants to be treated well, to have a partner that betters you, but...)"
    mct "(If I could boil it down to one quality, I'd say I want to feel like...)"
    hide screen textbox2 with dissolve

    menu:
        "You want to feel like a king. [gr]\[Worship\]":
            $ w1ExWorship = True
            scene w1_2653 with dissolve
            show screen textbox2 with dissolve
            mc "I want to feel like a king."
            scene w1_2654 with dissolve
            kat "Don't all men?"
            scene w1_2653 with dissolve
            mc "Some more than others, I guess..."
            scene w1_2654 with dissolve
            kat "That's a fine answer, one that I'm sure most of our patrons would say. It's what the business is ultimately about."
            scene w1_2657 with dissolve
            kat "Making the vulgar, base men feel regal."
            scene w1_2653 with dissolve
            mct "(She's one to talk.)"

        "You want to feel cared for. [gr]\[Tender\]":
            $ w1ExTender = True
            scene w1_2653 with dissolve
            show screen textbox2 with dissolve
            mc "Everyone wants to feel cared for, right?"
            scene w1_2654 with dissolve
            kat "No, not everyone. I'll take that as you answer though? You want to feel loved and taken care of?"
            scene w1_2653 with dissolve
            mct "(It does sound like such a basic answer, but deep down, it was true.)"
            mc "Yes."
            scene w1_2655 with dissolve
            kat "So that's the kind of face you want to put on. That one's VERY interesting to know."
            scene w1_2656 with dissolve
            "For whatever reason, my answer seemed to amuse her. Is it because it sounded childish...?"

        "You want to feel sadistic. [gr]\[Nasty\]":
            $ w1ExNasty = True
            show screen textbox2 with dissolve
            "Deep down, there's is a part of me that I keep buried. A part I chose to ignore or otherwise refuse to let define me. And that is..."
            scene w1_2653 with dissolve
            mc "I want to have total, complete control. I want to feel ruthless. Mean. Nasty--"
            scene w1_2657 with dissolve
            kat "That's enough synonyms, dear."
            scene w1_2656 with dissolve
            mc "Sorry."
            "It was true, but I don't know why I chose to admit that to her."
            scene w1_2655 with dissolve
            kat "Sadistic, huh? Aren't we all?"
            kat "So you just come out and admit that? That's admirable in a way."
            scene w1_2658 with dissolve
            kat "Is it because you're beginning to trust me? Hmmm...?"
            scene w1_2659 with dissolve
            "Mrs. Pulman leaned in closer and scrutinized my face."


        "You want to feel like you're being taken for a ride. [gr]\[Tease\]":
            $ w1ExTease = True
            scene w1_2653 with dissolve
            show screen textbox2 with dissolve
            mc "I want to feel like I've been put through the paces."
            scene w1_2657 with dissolve
            kat "That's a rather colorful, but complicated way of putting it."
            scene w1_2653 with dissolve
            mc "Hmm, yeah... I guess what I'm trying to say is..."
            mct "(What {i}am{/i} I trying to say?)"
            mc "After a night with a woman, I want to feel dead. Totally spent."
            mc "I want to feel like I just did something that I'll look back on for the foreseeable future."
            scene w1_2655 with dissolve
            kat "Ah, yes. That perfectly clarifies things."

    scene w1_2660 with dissolve
    kat "So, to recap..."

    if w1ExWorship == True:
        kat "You want your cock worshiped and treated like it's god's gift to women."
        scene w1_2653 with dissolve
        mc "When you put it that way, it sounds ridiculous."
        scene w1_2657 with dissolve
        kat "Don't worry. We are all ridiculous creatures."
        scene w1_2653 with dissolve

    if w1ExTender == True:
        kat "You want a tender experience from a lover."
        scene w1_2655 with dissolve
        kat "That is unusual for these walls, but it is rather cute."
        scene w1_2656 with dissolve
        mc "..."

    if w1ExNasty == True:
        scene w1_2655 with dissolve
        kat "You want to let some of that pent up aggression out."
        scene w1_2656 with dissolve
        mc "The way you phrased it does sounds better than how I put it, but..."

    if w1ExTease == True:
        scene w1_2655 with dissolve
        kat "You want to have your socks knocked off, so to speak."
        scene w1_2656 with dissolve

    mc "That's right."
    scene w1_2661 with dissolve
    kat "Perfect! I think those two pieces of information will be enough."
    kat "I'll let Charles and August know what to look for. You should go get changed."
    scene w1_2662 with dissolve
    mc "Into what?"
    scene w1_2663 with dissolve
    kat "Mmmh... less. You're going to need less clothes."
    kat "Strip down to your underwear."
    scene w1_2662 with dissolve
    mc "If I knew that, I would've worn something sexy."
    scene w1_2663 with dissolve
    kat "Very funny, Mr. [mcl]."
    scene black with fade
    stop music fadeout 3.0
    "......"
    "..."
    scene w1_2664 with fade
    play music "music/i-knew-a-guy.mp3"
    chuck "Ha! You should eat more, lad!"
    "Sure, it felt embarrassing sitting here in my underwear, but the awkwardness was tempered by the knowledge that I'd soon be the sexual guinea pig for three beautiful women."
    "--that was what I told myself, at least."
    sam "You call this a job? Shit, lucky bastard!"
    scene w1_2665 with dissolve
    "Although the commentary from the peanut gallery wasn't helping things."
    scene w1_2666 with dissolve
    kat "Now, the only thing remaining to be determined is who's going first."
    kat "I don't really care. You girls could draw lots if you--"
    scene w1_2667 with dissolve
    "Felicia was quick to hop to her feet, wagging her arm in the air emphatically like she was in an over-eager student."
    fel "I'll go first!"
    scene w1_2668 with dissolve
    kat "You don't get points for gusto, Mrs. Ford."
    scene w1_2669 with dissolve
    fel "That's okay. I'd still like to go first."
    scene w1_2668 with dissolve
    kat "You girls fine with that?"
    scene w1_2670 with dissolve
    ver "It's fine with me."
    rose "Sure..."
    scene w1_2671 with dissolve
    kat "There you have it, gentlemen. Kicking off the first game of our 5th annual summer exhibition, will be Mrs. Felicia Ford."
    scene w1_2672 with dissolve
    kat "Come on up, dear."
    scene w1_2673 with dissolve
    "Felicia was quick to march up the aisle, with not an ounce of hesitation."
    scene w1_2674 with dissolve
    kat "For this test, you'll be given twenty minutes or until you make our boy here pop."
    scene w1_2675 with dissolve
    kat "Remember, your task is to provide exemplary service, in every sense of the word. It's not just about the sexual components, but also your ability to string a man along."
    kat "Not to mention, you should also make it a damn good show for the audience."
    scene w1_2676 with dissolve
    kat "You may begin when you're ready."
    scene w1_2684 with dissolve
    stop music fadeout 3.0
    "......"
    "..."
    scene w1_2677 with dissolve

    if kat_polite == True:
        "Surprisingly, with Mrs. Pulman's permission to begin this absurd stage play, Felicia took a moment of contemplation instead of simply jumping into it."
    else:
        "Surprisingly, with Kathleen's permission to begin this absurd stage play, Felicia took a moment of contemplation instead of simply jumping into it."

    "She shut her eyes tight and cutely bunched her nose up like a chipmunk, before taking a deep breath and centering herself."

label w1ExIntuitionGameFelicia:

    if _in_replay:
        show transitionfelicia02 with cmet
        show screen textbox2 with dissolve
        "Does Felicia refer to the player character as daddy?"
        hide screen textbox2 with dissolve

        menu:
            "Yes, daddy.":
                $ felPN == "Daddy"
                show screen textbox2 with dissolve
            "No.":
                show screen textbox2 with dissolve
                pass

        "What kind of woman did you tell Kathleen you prefer?"
        hide screen textbox2 with dissolve

        menu:
            "You like a woman who can take charge and let loose.":
                $ w1ExInControl = True
                show screen textbox2 with dissolve

            "You like a demure, obedient woman who can be slutty.":
                $ w1ExDeferential = True
                show screen textbox2 with dissolve

            "You like an attentive woman that knows what buttons to push.":
                $ w1ExAttentive = True
                show screen textbox2 with dissolve

        "How did you want to be treated?"
        hide screen textbox2 with dissolve

        menu:
            "You want to feel like a king.":
                $ w1ExWorship = True
                show screen textbox2 with dissolve

            "You want to feel cared for.":
                $ w1ExTender = True
                show screen textbox2 with dissolve

            "You want to feel sadistic.":
                $ w1ExNasty = True
                show screen textbox2 with dissolve

            "You want to feel like you're being taken for a ride.":
                $ w1ExTease = True
                show screen textbox2 with dissolve


        show screen textbox2 with dissolve

    scene w1_2678 with dissolve
    play music "music/helping-hands.mp3"
    fel "Good evening, Sir."
    "Felicia bowed at the waist, offering me a top-side view of her ample cleavage, a motion that threatened to spill the beauties from her costume."
    mc "Uh..."

    if kat_polite == True:
        mct "(Mrs. Pulman said to think of this like theater, but I don't know what to make of that.)"
    else:
        mct "(Kathleen said to think of this like theater, but I don't know what to make of that.)"

    "Next to us was a sea of wrinkled faces, unfalteringly trained on where the two of us stood. It was a fact that was tough to forget."

    scene w1_2679 with dissolve
    if felPN == "Daddy":
        fel "Or would you prefer I call your daddy?"
    else:
        fel "Or would you prefer I call you something else?"

    scene w1_2680 with dissolve
    "Felicia stepped forward, a soft smile on her lips as she posed the question."
    scene w1_2679 with dissolve
    fel "Just keep your eyes on me and you'll soon be forgetting about them, okay?"
    scene w1_2680 with dissolve
    "Sensing my reticence, she gave me some encouragement in a hushed tone aimed only at me."
    "Right, I'm already in the middle of this... I should play along."
    hide screen textbox2 with dissolve

    menu:

        "Tell her she had it right the first time":
            $ felSN = "Sir"
            scene w1_2681 with dissolve
            show screen textbox2 with dissolve
            mc "[felSN] does have a nice ring to it."
            scene w1_2679 with dissolve
            fel "As you wish, [felSN]."

        "You do like it when she calls you daddy." if felPN == "Daddy":
            $ felSN = "daddy"
            scene w1_2681 with dissolve
            show screen textbox2 with dissolve
            mc "I like the way [felSN] sounds."
            scene w1_2679 with dissolve
            fel "Anything for [felSN]."

        "{color=#4169E1}\[Player Input]{/color} You'd prefer it if she called you...":
            show screen textbox2 with dissolve

            python:
                felSN = renpy.input("What do you want Felicia to call you tonight?")
                felSN = felSN.strip()

                if not felSN:
                    felSN = "stud"
                persistent.felSN = felSN

            if felSN == "stud":
                scene w1_2681 with dissolve
                mc"You can just call me [felSN], like you usually do."
                scene w1_2679 with dissolve
                fel "Sure thing, [felSN]."

            else:
                scene w1_2681 with dissolve
                mc "I'd prefer it if you referred to me as [felSN]."
                scene w1_2679 with dissolve
                fel "Anything for a most-valued customer, [felSN]."



    scene w1_2680 with dissolve
    mct "(She's really not conscientious at all of the crowd...)"
    scene w1_2682 with dissolve
    fel "Sit down and make yourself comfortable."
    scene w1_2683 with dissolve
    "Using her chin, she gestured toward the red leather couch that sat at the stage's back edge."
    scene w1_2682 with dissolve
    stop music fadeout 3.0
    fel "I'll pour you a drink."
    scene w1_2683 with dissolve
    mct "(Well, this is {b}her{/b} show. She's the boss.)"
    scene black with fade
    "My job is to do as she asks."
    scene w1_2685 with curtains
    play music "music/echo-sclavi.mp3"
    "After a quick, efficient display of her bartending prowess, Felicia was soon at my side with a mixed drink in hand."
    mc "Did you bartend in college or something?"
    fel "I didn't."
    scene w1_2686 with dissolve
    mc "You looked pretty practiced at it."
    scene w1_2687 with dissolve
    "I tried to make conversation despite the feeling of more than a dozen ears listening in."
    scene w1_2688 with dissolve
    fel "I mixed my share of drinks during my sorority days."
    scene w1_2689 with dissolve
    "The volunteer whore pressed the glass to her soft, glossy lips and took a small sip of the cup's contents."
    scene w1_2690 with dissolve
    mc "I thought that was for me?"
    scene w1_2691 with dissolve
    fel "You feeling {b}thirsty{/b}, [felSN]?"
    "Felicia made the innocuous question sound shamelessly provocative."
    scene w1_2692 with dissolve
    "The question must've been a rhetorical one, as the blonde bunny emptied the glass into her mouth before I even had the chance to answer."
    scene w1_2693 with dissolve
    mc "Eh--?"
    "Before promptly throwing a leg, followed by the rest of her body, over me."
    scene w1_2694 with dissolve
    "The look in her eyes told me everything I needed to know."
    "I parted my lips, in anticipation of what was coming next."
    scene w1_2695 with dissolve
    mc "Mmh..."
    "Felicia locked lips with mine, shoving her tongue down my throat and allowing a citrus-tasting liqueur passage into my mouth."
    fel "*Churp* *Churp*"
    mc "Mmmh...!"
    "Thanks to the intensity of our kiss, not all of the sweet mixture found it's way down my esophagus. Trickles of it spattered the corners of my mouth."
    scene w1_2696 with dissolve
    fel "Ehehe....♥"
    fel "Sorry for the mess..."
    scene w1_2697 with dissolve
    fel "*Lick*"
    "Felicia set to work cleaning up the \"spillage\", dragging the top and bottom of her tongue up and down the side of my face before returning her lips to mine once more."
    scene w1_2698 with dissolve
    "With all the cocktail drained from her mouth, this time it was a pure, unadulterated kiss."
    "Felicia took her time with it too, seemingly relishing the exploration of my mouth in detail."
    "Her tongue wrapped with mine, Felicia pressed our bodies closer together, resting her soft breasts on my chest."
    scene w1_2699 with dissolve
    "I was happy to be taking the passive role, so I just closed my eyes and allowed Felicia showcase her sensuality for the judges."
    scene w1_2700 with dissolve
    mc "Ah...!"
    scene w1_2701 with dissolve
    "Felicia unblinkingly looked into my eyes, down to my mouth, and back to my eyes again."
    mct "(Is she trying to read me...?)"
    scene w1_2702 with dissolve
    fel "Sorry, [felSN]. I might be getting a little ahead of myself."
    scene w1_2703 with dissolve
    "For the benefit of the crowd behind her, her voice kept its typical euphonious pitch."
    "Her face however, was one of stone-cold scrutiny. Looking for ANY minute change in my expression. She was serious about winning this game."

    if w1ExInControl == True or w1ExAttentive == True:
        scene w1_2702 with dissolve
        fel "You don't mind a gal taking some initiative, do you?"
        scene w1_2703 with dissolve
        mct "(If the gold digger thing didn't work out for her, she could always be a police detective...)"
        scene w1_2702 with dissolve
        fel "Sit back and let me take care of you, [felSN]."

        jump w1ExGame1FelControl

    else:
        scene w1_2702 with dissolve
        fel "Mmh...♥ Forgive a girl for taking some initiative."
        scene w1_2703 with dissolve
        mct "(If the gold digger thing didn't work out for her, she could always be a police detective.)"
        scene w1_2702 with dissolve
        fel "Maybe you'd like to get hands on?"
        jump w1ExGame1FelSubmissive


label w1ExGame1FelControl:

    scene w1_2704 with fade
    "Felicia climbed off of me and made her way to the center of the stage, giving the crowd a languishing look before turning on her heels and facing me again."
    scene w1_2705 with dissolve
    "If the expression she gave them was only half as lewd as the one she was shooting me right now, then I had no doubt she was making a favorable impression."
    "Nevertheless, she continued on like it was just me and her. An illusion I couldn't quite allow myself to slip under."
    "Felicia was shinning under the spotlight, but as stunning as she was, past her shoulders was a medley of ugly faces projecting a laser-like focus at the stage."
    mct "(Although, I'm sure most of it is on Felicia's ass right now...)"
    fel "Let me just slip out of this costume first."
    scene w1_2706 with dissolve
    "The blonde beauty took the flat of her palms and guided them down the length of her body."
    scene w1_2707 with dissolve
    "Smoothing out her costume and drawing attention to the goods."
    scene w1_2708 with dissolve
    kat "Straight to the point, Mrs. Ford?"

    if kat_polite == True:
        "Mrs. Pulman called out from the sidelines, interjecting her thoughts into our \"private\" moment."
    else:
        "Mrs. Pulman called out from the sidelines, interjecting her thoughts into  our \"private\" moment."

    scene black with fade
    fel "Straight to the {b}good stuff{/b}, Mrs. P."
    scene w1_2709 with fade
    "Felicia wasted no time in undressing, slipping the red bunny costume off her shoulders and down her long legs."
    scene w1_2710 with dissolve
    "Before butting a heel on the ottoman and..."
    scene w1_2711 with dissolve
    "Giving it a swift push to create a direct path back to me."
    scene w1_2712 with dissolve
    "Confident in her plan of action, Felicia took me by the hand and gave me a conspiratorial nod."
    scene w1_2713 with dissolve
    "One that I acknowledged by standing up. She clearly wants to take the lead here."
    fel "Don't look so tense, [felSN]. I promise I'm going to make you feel good."
    scene w1_2714 with dissolve
    "With reassuring words, Felicia leaned into my chest and began planting small kisses on the nape of my neck."
    scene w1_2715 with dissolve
    fel "*Chup, chup*"
    "Down to my chest."
    scene w1_2716 with dissolve
    "Stomach."
    scene w1_2717 with dissolve
    "Until finally stopping at my crotch."
    fel "Mmmh~♥ Let's get this monster unwrapped."
    scene w1_2718 with dissolve
    "Felicia glanced up one last time, silently asking for confirmation."
    mct "(This is going to be a first...)"
    "Exposing myself to a room full of rich old men that is."
    "Steeling my nerves, I gave Felicia the go ahead in the form of a nod."
    scene w1_2719 with fade
    fel "Hello, Mr. Cock~!"
    "With one quick yank, Felicia had my underwear around and off my ankles, exposing my dick to the open air and the crowd's unflinching gaze."
    scene w1_2720 with dissolve
    kil "Nice cock, bro!"
    "Killian called from across the room, replete with a big fat grin and a thumbs up gesture."
    "The room filled with some light chuckle mingled with some other commentary I couldn't quite make out."
    scene w1_2721 with dissolve
    fel "*Whisper* Don't let them get to you, [mcf]. I'm here and I'll take care of you. I'll make you forget all those old geezers in no time."
    fel "Let's give these gentlemen a proper show."
    scene w1_2722 with dissolve
    "Felicia lead me by the hand to the ottoman and directed me to sit down."
    fel "Have a seat, [felSN]."
    mc "Alright..."
    "My body was feeling an odd mix of stage fright and excitement, head teeming with all the lewd ways Felicia might take this."
    jump w1ExGame1FelContinue

label w1ExGame1FelSubmissive:

    scene w1_2723 with dissolve
    "Felicia gave me a conspiratorial wink."
    scene w1_2703 with dissolve
    mct "(Get hands on, huh...?)"
    "Sensing (or knowing) I'm not the type that likes to sit back, she directed me to take a more active role in our stage play."
    scene w1_2702 with dissolve
    fel "Why don't you help me out of my clothes, [felSN]?"
    scene w1_2724 with dissolve
    mc "I think I can do that."
    "I softly gripped the busty blonde by the waist and did my best to forget everything other than her."
    scene w1_2725 with vpunch
    fel "Oooh! Heheh~♥"
    scene w1_2726 with dissolve
    "I positioned myself in between Felciia's legs, while Felicia looked up at me with excited eyes."
    "The audience REALLY had her feeling this."
    scene w1_2727 with dissolve
    mct "(Beautiful, as always...)"
    scene w1ExGame1FelTitSuck with fade
    "Wordlessly, I angled myself forward and latched my lips on one of her nipples, rolling the soft-pink protuberance around with my tongue."
    fel "A-ah~♥ Shit, that's sudden...!"
    fel "*Whisper* Not that I'm complaining, but you're supposed to be undressing me..."

    scene w1_2733 with dissolve
    if toughness >=20:
        mc "Undress yourself, slut."

    else:
        mc "Undress yourself."

    "I mustered my clearest, most authoritative voice."
    scene w1_2734 with fade
    "Felicia clamored to her feet, to hastily finish what I had started."
    kat "Straight to the point?"

    if kat_polite == True:
        "Mrs. Pulman called out from the sidelines, interjecting her thoughts into our \"private\" moment."
    else:
        "Mrs. Pulman called out from the sidelines, interjecting her thoughts into  our \"private\" moment."

    scene w1_2735 with dissolve
    fel "Straight to the {b}good stuff{/b}, Mrs. P."
    "Meanwhile, I kicked the ottoman out of the way to make room for what I had in mind next."
    scene w1_2736 with fade
    "By the time and I made it across the stage, Felicia had slipped the costume off her shoulders and down past her long, shapely legs. Kicking them out of sight."
    scene w1_2737 with dissolve
    mc "Crawl."
    scene w1_2736 with dissolve
    "I put it curtly, worried my voice would falter due to stage fright."
    scene w1_2738 with dissolve
    "Thankfully, it didin't. Felicia smirked, pleased that I was taking to the role she assigned to me."
    fel "Yes, [felSN]!"
    scene w1_2739 with dissolve
    "Felicia enthusiastically fell to her knees and began to close the gap between us on all fours."
    "She went above and beyond too, making sure to emphatically wag her ass like a dog."
    scene w1_2717 with dissolve
    fel "Mmmh~♥ Let's get this monster unwrapped."
    scene w1_2718 with dissolve
    "Felicia glanced up one last time, silently asking for confirmation."
    mct "(This is going to be a first...)"
    "Exposing myself to a room full of rich old men that is."
    "Steeling my nerves, I gave Felicia the go ahead in the form of a nod."
    scene w1_2719 with fade
    fel "Hello, Mr. Cock~!"
    "With one quick yank, Felicia had my underwear around and off my ankles, exposing my dick to the open air and the crowd's unflinching gaze."
    scene w1_2720 with dissolve
    kil "Nice cock, bro!"
    "Killian called from across the room, replete with a big fat grin and a thumbs up gesture."
    "The room filled with some light chuckle mingled with some other commentary I couldn't quite make out."
    scene w1_2721 with dissolve
    fel "*Whisper* Don't let them get to you, [mcf]. I'm here and I'll take care of you. I'll make you forget all those old geezers in no time."
    scene w1_2722 with dissolve
    "Instead of answering her directly, I sat down and decided to leave her to it. Let her take control again."
    "My body was feeling an odd mix of stage fright and excitement, my mind awash in all the lewd avenues Felicia might take this."
    jump w1ExGame1FelContinue

label w1ExGame1FelContinue:

    scene w1_2740 with dissolve
    fel "You've got such a handsome cock. Let's make this baby {b}grow.{/b}"
    scene w1_2741 with dissolve
    "Honestly, I was surprised the kissing earlier hadn't already sent all the blood rushing to my dick."
    scene w1_2742 with dissolve

    if w1ExInControl == True or w1ExAttentive == True:
        fel "Just lay back and let me take care of you, [felSN]."
    else:
        fel "Just lay back and let me {b}slave{/b} over your cock, [felSN]."

    "Felicia gave my stomach a gentle push, signaling to me to lay back on the ottoman."
    scene w1_2743 with dissolve
    stop music fadeout 3.0
    "Head back, eyes turned toward the ceiling, I decided to focus solely on the forthcoming pleasure."
    "Which didn't take long, as Felicia perched her lips on the underside of my scrotum."
    fel "MMmhhh....♥"
    scene w1_2744 with dissolve
    fel "I should pay my respect to EVERY part of your dick. After all, these marvelous things will be churning out my reward soon enough."
    scene w1_2745 with dissolve
    mc "How can you say that with a straight face?"
    "I wondered aloud."
    scene w1_2746 with dissolve
    "Felicia followed up her outrageous statement with a series of lewd and pornographic sounds as she gently rolled my nuts inside her mouth with the tip of her tongue."
    scene w1ExGame1FelBallSuck with dissolve
    play ambient "sound effects/ballsuck.wav"
    fel "*Chup, Chwup~♥*"
    fel "Mmmmh... Mmmmhh.... *Chup, Chwup.* *Chup, chwup~!*"
    mc "Ah...!"
    "Thanks to Felicia's fervent efforts, every nerve in my nut sack was sending a hit of pleasure to my brain."
    fel "*Chup, Chwup~*"
    mct "(She's {b}really{/b} fucking good at this!)"
    "She was aggressive, but she was never rough. She knew where the line was and she walked it perfectly, keeping me stimulated but never painfully overwrought."
    "It wasn't long before she had the base of my cock twitching in anticipation, every flick of her tongue causing my balls to tighten up like they were about to explode."
    hide screen textbox2 with dissolve

    menu:
        "Tell Felicia she's doing a good job.":
            show screen textbox2 with dissolve
            "This was the first time I'd ever had a woman pay attention to my nuts and by god was it wonderful. I couldn't help but say as much."
            mc "Oh, f-fuck... that's feels so damn good, Felicia. Keep going! Please!"
            scene w1_2751 with dissolve
            fel "Mmhthwank~ouhuuu~!♥"
            "Felicia mumbled something I couldn't make out."
            scene w1ExGame1FelBallSuck with dissolve
            mc "C'mon... ah, you're amazing! You're so damn amazing!"



        "Urge Felicia on with dirty talk":
            show screen textbox2 with dissolve
            "This was the first time I'd ever had a woman pay attention to my nuts and by god was it wonderful."
            mc "F-fuck, you dirty bitch! You're gobbling my nuts like its your last meal!"
            scene w1_2751 with dissolve
            fel "MmmmhEhantahlpeeet~soUOOD~!♥"
            "Felicia mumbled something I couldn't make out."
            mc "H-ha! Don't talk with you mouth full, bitch."
            scene w1ExGame1FelBallSuck with dissolve
            "It was a short, stupid exchange but it filled me with a perverse glee."


        "Keep your trap shut and just focus on the pleasure.":
            show screen textbox2 with dissolve
            "Having a beautiful, rich, big-tittied trophy wife sucking on your nuts isn't an every day thing. Why dilute the experience with words? Why say anything?"
            "I should just enjoy Felicia working her craft."

    fel "Mmmmh... Mmmmhh.... *Chup, Chwup.*"
    "Even if I couldn't see it, I could just feel my scrotum glistening with the wanton ballsucker's saliva. She had undoubtedly polished them to a sheen by now."
    scene w1_2752 with dissolve
    stop ambient
    "Felicia pulled herself off my nuts with an audible {b}*pop*{/b}."
    scene w1_2753 with dissolve
    play music "music/guiton-sketch.mp3"
    fel "There's that big, beautiful dick..."
    fel "Everyone's got there eyes on this thing right now, wishing they were you. Isn't that exciting?"
    scene w1_2754 with dissolve
    mct "(Normally I'd say no, but the way she put it in a hushed, heated, sexed-up tone... I would be inclined to agree.)"
    scene w1_2753 with dissolve
    fel "*Whisper* You're the most virile stud here, [felSN]."
    scene w1_2754 with dissolve
    "This time, she directed her words only to me. A private moment of encouragement."
    "Felicia really did know how to make a man feel on top of the word, I'll give her that."
    scene w1_2753 with dissolve
    fel "Now, let's move on..."
    scene w1_2755 with dissolve
    "Without further ado, Felicia slid her tongue up the entire length of the underside of my cock."
    scene w1_2756 with dissolve
    "Base to..."
    scene w1_2757 with dissolve
    "Tip."
    scene w1_2758 with dissolve
    fel "Quite a bit of work getting from bottom to top, y'know? Mmmh..."
    fel "I bet sucking this thing everyday would be good for a girl's figure."
    scene w1_2760 with dissolve
    fel "*{b}Smoooooch!{/b}*"
    "Felicia began dotting the shaft of my dick with quick, affectionate kisses."
    scene w1_2761 with dissolve
    fel "*Chup, fwhup!*"
    fel "*{b}Smooooch~*♥{/b}"
    scene w1_2758 with dissolve

    if w1ExInControl == True or w1ExAttentive == True:
        fel "May I put it in my mouth, [felSN]?"
        scene w1_2759 with dissolve
        "The question caught me somewhat off guard."
        mc "...eh? Y-yes. Please do!"

    else:
        fel "Now let's see how much of you I can handle, [felSN]."

    scene w1_2762 with dissolve
    "Felicia started out slow, perching the tip of my penis in between her soft, glossy lips."
    scene w1_2763 with dissolve
    "From there, she gave my urethra a tentative probing, sliding the very tip of her dexterous tongue across its slit."
    scene w1ExGameFelJustTheTip with dissolve
    "Next she slid he tongue down to my frenulum, probing the small gap of connective tissue before using it to trace underneath the head of my cock."
    fel "*Fwhup, khwup* *Chup~fwhup~*"
    "The action produced a litany of obscene, lewd noises."
    scene w1_2766 with dissolve
    fel "Ah!"
    scene w1_2768 with dissolve
    fel "Hmm... I love the taste of a sweaty cock. It's a shame you took a shower today or I could've given you a proper cleaning with my mouth..."
    scene w1_2769 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Tell Felicia she's a freak.":
            show screen textbox2 with dissolve
            mc "You're a shameless, dirty bitch. You know that?"
            scene w1_2768 with dissolve
            fel "Thank you for the compliment, [felSN]."
            scene w1_2767 with dissolve
            "Felicia grinned mischievously."
            fel "Tell me something I don't know..."

        "Tell Felicia to get back to it.":
            show screen textbox2 with dissolve
            mc "Stop talking and get my dick back in your mouth."
            scene w1_2768 with dissolve
            fel "Yes, [felSN]..."


        "Wait for Felicia to resume on her own.":
            show screen textbox2 with dissolve
            pass

    scene w1_2770 with dissolve
    scene w1_2771 with dissolve
    scene w1_2772 with dissolve
    scene w1_2773 with dissolve
    "Felicia suddenly took my entire length, folding her tongue around the topside of my cock and sending the glans of my penis barreling down the passage of her throat."
    mc "Ah-!"
    "The sudden collision of my penis head with the volunteer whore's mucous-lined airway sent a pleasurable jolt through my body."
    "Instead of moving, she simply held the position."
    "Instead of trying to dislodge the foreign invader, her throat felt welcoming as Felicia gently hummed."
    "All the while, she unblinkingly peered up at me with her big, sex-hungry blue eyes."
    mct "(Fuck me...)"
    "That look alone made me want to cum, to grab the back of Felicia's head and rut her face like an unthinking animal."
    mct "(Gotta resist... It's her show, I'm just the prop penis here.)"
    frank "Wow, she took that without flinching!"
    kat "Yes, it seems like Mrs. Ford is the perfect cocksucker, isn't she?"
    eric "You don't usually get that from women with money."
    jim "Hehe, guess she had to work for it."
    "The murmuring of the crowd wasn't enough to take me out of the moment."
    "With just the warm comfort of her mouth and the skillful application of her tongue, Felicia had made me forget about those old leering bastards."
    scene w1_2774 with dissolve
    fel "*{b}Plop!{/b}* Ah...."
    "As abruptly as she had swallowed my cock, did she displace it with a pleasant-sounding coo."
    scene w1_2775 with dissolve
    mc "That feels..."
    scene w1_2776 with dissolve
    "Just as I was starting the warm of Felicia's sucking maw, Felicia jumped back into things by showering my aching cock with affection."
    scene w1_2777 with dissolve
    fel "*{b}Smoooooch!{/b}*"
    mc "That feels...!"
    scene w1_2778 with dissolve
    fel "*Chup, fwhup!*"
    fel "*{b}Smooooch~*♥{/b}"
    scene w1_2779 with dissolve
    fel "Ten minutes of sucking on this mighty beast would fuck my jaw up..."
    scene w1_2780 with dissolve
    fel "Heheh, I know! Why don't you..."
    scene black with fade
    "Instead of finishing her sentence, Felicia helped me off the ottoman and switched places with me."
    scene w1_2781 with fade
    fel "Use my mouth like a pussy, [felSN]? Look..."
    scene w1_2782 with dissolve
    fel "Aaaah~!"
    "Felicia fish hooked herself, sticking out her tongue and giving me a lewd look at the inside of her mouth."
    "This was another one of Felicia's talents, seamlessly switching between giving and taking, but always having a hand on the wheel."
    scene w1_2783 with dissolve
    chuck "Don't keep a girl waiting, lad."
    scene w1_2784 with dissolve
    sam "Yeah, give it to the slut!"
    mct "(I'm so damn turned on now...!)"
    scene w1_2782 with dissolve
    "I was so horny, that I was finding the vile encouragement coming from the crowd enticing."
    hide screen textbox2 with dissolve

    menu:
        "Just ram your cock into Felicia's waiting mouth":
            show screen textbox2 with dissolve
            "Not wanting to wait to sleeve myself in the cocksucker's waiting throat, I stepped forward."
            jump w1ExGame1FeliciaTS

        "Tease Felicia a little [gr]\[Toughness +1\]":
            $ toughness += 1
            show screen textbox2 with dissolve
            "Resisting the urge to ram my cock down Felicia's throat, I decided to embrace the moment and tease the waiting cocksucker a little."
            scene w1_2786 with dissolve
            "Stroking my cock, I positioned myself over Felicia's face, letting my swaying balls collide with volunteer whore's cute button nose."
            "There, with my nuts resting on Felicia's chin, I simply took a moment to relish my position over the rich woman."
            scene w1_2785 with dissolve
            fel "What are you waiting for...? Stick it eeeeeEeeeenn....!"
            scene w1_2786 with dissolve
            "Felicia pleaded, cutely."
            play sound "sound effects/slap2.wav"
            scene w1_2787 with hpunch

            if toughness >= 19:
                mc "Where the fuck is your pride?"
            else:
                mc "You're shameless!"

            "To punctuate the statement, I gave slapped a firm, plodding cock-slap to the face."
            "Her soft flesh felt nice on my aching, twitching cock."
            scene w1_2785 with dissolve
            fel "Mmmh... c'mon...!♥ Help me give these gentlemen a show, [felSN]."
            scene w1_2786 with dissolve
            "As tempting as it was, I wasn't quite done enjoying my newly given initiative."
            mc "If you ask nicely."
            scene w1_2788 with dissolve
            "Felicia grinned at my request, keen on where I was taking this."
            scene w1_2785 with dissolve
            fel "Will you fuck my face? Pleeeeeeeese?"
            scene w1_2788 with dissolve
            hide screen textbox2 with dissolve
            jump w1ExGame1FeliciaBeg


    menu w1ExGame1FeliciaBeg:

        "That'll do. You can't wait anymore, anyway.":
            show screen textbox2 with dissolve
            "That's enough of that. Time to sleeve myself in Felicia's tight throat."
            jump w1ExGame1FeliciaTS

        "Tell Felicia that's not good enough.":
            show screen textbox2 with dissolve
            mc "You can do better than that."
            fel "Hmm..."
            "Felicia gave her words some thought, before..."
            scene w1_2785 with dissolve
            fel "[felSN], will you please fuck my tiny little mouth with your monster dick?"
            scene w1_2788 with dissolve
            "The words were dripping with pornographic emphasis. It was such a theatrical request, but Felicia delivered it convincingly."
            kat "Get this show moving, Mr. [mcl]."
            jump w1ExGame1FeliciaTS


label w1ExGame1FeliciaTS:

    scene w1_2789 with dissolve
    "Rolling my hips forward, I slid myself into the blonde beauty's open mouth."
    scene w1_2796 with dissolve
    "She had kept it wide and open, keeping her teeth out of the way of my less-than-precise action."
    mc "Good girl..."
    "Her angle giving me instant access, I slide into the tight passage of her throat like butter, all the way until my balls knocked against the rich slut's nose."
    "Naturally, Felicia didn't reel or gag. Instead, she purred gently like her throat was offering up a gentle massage."
    scene w1_2789 with dissolve
    "Placing a hand around her neck, I reeled back, pulling myself out halfway."
    scene w1_2796 with dissolve
    "Before pushing my hips forward again as a test."
    "Felicia once again didn't show the slightest feeling of discomfort."
    scene w1_2789 with dissolve
    fel "Guaaah...~!"
    scene w1_2796 with hpunch
    "An even more forceful thrust didn't wipe the slutty look off her face."
    mct "(She's sure got some endurance...)"
    "Part of me wanted to test that."
    scene w1_2789 with dissolve
    "Spurred on by having free reign to fuck her throat, I withdrew and extended my hips in repetition."
    scene w1_2796 with dissolve
    "It started out awkward enough."
    "Each gyration varied in stroke."
    scene w1_2789 with dissolve
    scene w1_2792 with dissolve
    "Short."
    scene w1_2789 with dissolve
    scene w1_2796 with dissolve
    "Deep."
    scene w1_2789 with dissolve
    scene w1_2796 with dissolve
    "Fast."
    scene w1_2789 with dissolve
    scene w1_2796 with dissolve
    "Slow."
    "In some ways, I felt like a virgin awkwardly fumbling around. Skittish I might hurt her."
    "Eventually, I became more and more sure that wasn't going to happen."
    scene w1ExGame1FelTS with dissolve
    play ambient "sound effects/fel2.wav"
    fel "*Guug*"
    fel "*gur-gh-gurg!*"
    "Felicia started making the most beautiful noises and eventually I settled into a rhythm."
    "Long, quick furious strokes."
    fel "*Guug*"
    fel "*gur-gh-gurg!*"
    fel "*gur-ghug-gurg!!!*"
    "I enjoy the feeling of her breath quickening, hot air erratically tickling the underside of my cock as her breathing became more and more labored from the tense assault."
    "Felicia tried to breath through her nose, but my cock displaced most of the air before it could enter her pharynx."
    mihir "This new employee is enthusiastic."
    kil "Damn straight he is."
    aug "You only get once chance at making a first impression."
    fel "*Guug*"
    fel "*gur-gh-gurg!*"
    fel "*gur-ghug-gurg!!!*"
    scene w1_2797 with dissolve
    mc "Fuck! I--"
    hide screen textbox2 with dissolve

    menu:
        "Give Felicia's breasts a good whack.":
            play sound "sound effects/slap2.wav"
            scene w1_2798 with dissolve
            mc "*Thwak!*"
            "I felt a sadistic urge and I acted on it. Simple in that."
            play sound "sound effects/slap2.wav"
            scene w1_2799 with dissolve
            mc "*Thwak!* *Thwak!*"
            "The throes of passion eroded my self-control and the volunteer whore's bouncing tits were the perfect target."
            play sound "sound effects/slap2.wav"
            scene w1_2798 with dissolve
            play sound "sound effects/slap2.wav"
            scene w1_2799 with dissolve
            mc "*Thwak!* *Thwak!* *Thwak!*"
            "Each blow sent them pendously knocking against each other."
            fel "*Guug* Gu-ha!"
            "The action surprised Felicia, creating a sputtering noise and causing her airway to tighten as attempted to suck down my air in surprise."

        "Give Felicia's breasts a pull. [gr]\[Toughness +1\]":
            $ toughness += 1
            scene w1_2800 with dissolve
            fel "*Guug* Gu-ha!"
            "I felt a sadistic urge and I acted on it. Simple in that."
            "I tugged roughly at the points of Felicia's bouncing mounds."
            fel "*Guug* *gur-gh-gurg!* {b}Guhg-haaaa!{/b}"
            "The action surprised Felicia, creating a discordant squeal and causing her airway to tighten as attempted to suck down my air in surprise."


        "Just keep hammering her throat.":
            $ toughness -=1
            "A sadistic urge welled up in me, but rather than indulge in tormenting my willing and eager partner, I decided to focus my energy into giving her a dizzying facefucking she'd never forget."

    scene w1ExGame1FelTS2 with dissolve
    show screen textbox2 with dissolve
    "The feeling of sliding in and out of Felicia's throat wasn't too unlike having sex."
    fel "*Guug*"
    fel "*gur-gh-gurg!*"
    fel "*gur-ghug-gurg!!!*"
    "There was little to no resistance, with the pooling saliva and spit providing a generous amount of lubrication."
    fel "*Guug*"
    fel "*gur-gh-gurg!*"
    fel "*gur-ghug-gurg!!!*"
    "When she said to fuck her face like a pussy..."
    mct "(She wasn't kidding.)"
    fel "*Guug*"
    fel "*gur-gh-gurg!*"
    fel "*gur-ghug-gurg!!!*"
    "Even the way I was jackhammering my hips felt like sex. This wasn't a loving, giving act like a blowjob. This was full-on lust addled breeding."
    "The vigorous action had my balls careening violently into Felicia's face adding an extra dimension of stimulation and dominance."
    fel "*Guug*"
    fel "*gur-gh-gurg!*"
    fel "*gur-ghug-gurg!!!*"
    tom "I can't believe that whore's till conscious."
    jim "To be young again... I wish I had that kind of stamina."
    scene w1_2806 with dissolve
    kat "It's like you're trying to break her, [mcf]."
    scene w1_2807 with dissolve

    if kat_polite == True:
        "Before I realized it, Mrs. Pulman had slipped behind me and spoke to me in a relatively conversational tone."
    else:
        "Before I realized it, Kathleen had slipped behind me and spoke to me in a relatively conversational tone."

    hide screen textbox2 with dissolve
    menu:
        "Tell her you're doing your best to put on an entertaining show. [gr]\[Kathleen +2\]":
            $ Kathleen_Trust +=2
            scene w1_2808 with dissolve
            show screen textbox2 with dissolve
            mc "Just want to put on a good show!"
            scene w1_2809 with dissolve
            mc "Is that so?"
            scene w1_2810 with dissolve
            "*{b}Thwap!{/b}*"
            "The boss gave me an encourage swat on the ass, like I was some workhorse."
            kat "I approve."

        "Tell her you can't help it. It feels so good. [gr]\[Kathleen +2\]":
            $ Kathleen_Affection += 1
            $ Kathleen_Trust +=1
            scene w1_2808 with dissolve
            show screen textbox2 with dissolve
            mc "I can't help it. It feels so good...!"
            scene w1_2806 with dissolve
            kat "So cute..."
            scene w1_2810 with dissolve
            "*{b}Thwap!{/b}*"
            "The boss gave me an encourage swat on the ass, like I was some workhorse."
            kat "I approve."

        "Ignore her.":
            show screen textbox2 with dissolve
            mc "N-not really!"
            "I wasn't in the mood to talk, too preoccupied with the pressure that was building in my balls."

    scene w1ExGame1FelTS with dissolve
    fel "*Guug*"
    fel "*gur-gh-gurg!*"
    fel "*gur-ghug-gurg!!!*"
    "The casualness of the exchange felt surreal, considering I was currently rutting another human being's face like it was an object."
    "This had been going on a few minutes now. Half of me was amazed at her endurance, while the other half was concerned with how she was holding up."
    fel "*Guug*"
    fel "*gur-ghug-gurg!!!* Ehuh!"
    "At least I knew she was still conscious thanks to the wet, staccato-like {b}plap{/b} and gutteral moans."
    "Of course, this kind of fucking had me quickly at my ropes end."
    "Each and every thrust pushed me closer and closer to the searing white natural conclusion."
    scene w1_2811 with dissolve
    kat "You're about there, right?"
    scene w1_2812 with dissolve
    mc "Y-yes!"
    "I could feel myself reach the precipice, mere moments away from dumping my sperm straight down Felicia's throat."
    scene w1_2811 with dissolve
    kat "Go ahead. Pump this dumb cunt's stomach full of thick, creamy sperm."
    kat "Don't be afraid to hold back."
    scene w1ExGame1FelTS2 with dissolve

    if kat_polite == True:
        "Mrs. Pulman ushered me on in a svelte, enchanting tone."
    else:
        "Kathleen ushered me on in a svelte, enchanting tone."

    kat "It'll be a long night, but thankfully we have ways of keeping you {b}fighting{/b} fit..."
    "I didn't like how that sounded, but..."
    stop ambient
    play sound "sound effects/spurt.wav"
    scene w1_2813 with flash
    "*Spurt!* *Spurt!*"
    mc "Shit!"
    fel "*gur-ghug-gurg!!!* {b}Mmhhhhaaaaaa!{/b}" with hpunch
    play sound "sound effects/spurt.wav"
    "*Spurt!*" with flash
    "My seed erupted straight down into Felicia's esophagus with a mind-blanking intensity."
    "I was cumming {b}hard{/b}, that it almost could be described as painful."
    play sound "sound effects/spurt.wav"
    fel "*gur-gh-gurg!* Ghuu!Ackhahaha~!" with flash
    "Felicia's throat tightened as she sputtered in surprise, caught off guard by the quantity of spunk I was pouring straight into her stomach."
    scene w1_2814 with dissolve
    stop music fadeout 3.0
    "Still, she didn't lose her composure. Instead opting to form a near-perfect seal with her lips and suck {i}hard{/i} like she was trying to wrangle every last drop of semen from me."
    fel "*Gulp... gulp... gulp*"
    jim "Is he still going?"
    play sound "sound effects/spurt.wav"
    fel "*Gulp... gulp... gulp* Ghna!" with flash
    eric "She didn't miss a beat!"
    "After a few moments, my orgasm subsided, Felicia gently coaxing and carousing the remaining cum from my urethra until I grew soft in her mouth."
    scene w1_2815 with dissolve
    stop ambient
    "Satisfied, I gently removed myself from her straining jaw."
    scene w1_2816 with fade
    play music "music/epic-battle-speech.mp3"
    "Felicia stood up from the ottoman, uneasy on her feet."
    mc "Careful!"
    fel "Oohhheh...[felSN]! That was..."
    fel "D-dizzy... all the blood just went to my head..."
    "Felicia accepted my shoulder in support."
    scene w1_2817 with dissolve
    mc "That was, uh..."
    scene w1_2818 with dissolve
    mct "(The best damn blowjob I'd experienced in my life, if you could even call it that.)"
    scene w1_2819 with dissolve
    fel "I know, hehe~♥"
    scene w1_2818 with dissolve
    "Felicia smiled cutely, in stark contrast to the utterly obscene act we just shared."
    hide screen textbox2 with dissolve

    menu:
        "Give her a kiss on the cheek. [gr]\[Felicia +1\] [red]\[Kathleen -1\]":
            $ Felicia_Affection +=1
            $ Kathleen_Affection -= 1
            scene w1_2820 with dissolve
            show screen textbox2 with dissolve
            mc "*Smooch*"
            scene w1_2818 with dissolve
            "I imagined a kiss looked pretty odd after something like that, but I couldn't help myself."
            scene w1_2817 with dissolve
            mc "That was something."
            scene w1_2819 with dissolve
            fel "I said I know, but thanks."

        "That might give Kathleen the wrong idea.":
            show screen textbox2 with dissolve
            pass

    scene w1_2819 with dissolve
    fel "You really let me have it, you fucking animal."
    scene w1_2818 with dissolve
    "She said it with an odd, warm glow."
    scene w1_2817 with dissolve
    mc "You're an absurd woman, you know that...?"
    scene w1_2821 with dissolve
    kat "*Ahem* That was quite the performance, Mrs. Ford."
    scene w1_2822 with dissolve
    kat "You certainly are quite... orally skilled."
    scene w1_2823 with dissolve
    kat "Take a bow."
    scene w1_2824 with dissolve
    fel "Thank you for watching!"
    play sound "sound effects/applause-small.wav"
    "Felicia enthusiastically made a display of appreciation, prompting the crowd to give her a round of applause."
    "It was utterly surreal."
    scene black with fade
    "I've still got to go through this twice more too - not that I've got much room to complain."
    $ renpy.end_replay()

    if not persistent.felExhibition1Game1:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.felExhibition1Game1 = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)

    stop sound fadeout 3.0
    stop music fadeout 3.0
    "....."
    "..."

    scene w1_2825 with curtains
    play music "music/cello-suite-No-1-G-Major-Prelude.mp3"
    "With almost no down time, the next to volunteer to come up was Rosalind."
    "I was still under a post-orgasm fog, not two minutes had passed since the conclusion of Felicia's leg of the game."
    "Rosalind had entered from the side of the stage and was standing there with a stoic look on her face."
    "I, on the other hand, was still naked. However, this time I didn't have the benefit of my cock stuffed down a beautiful woman's throat, so I was feeling a lot more sheepish about the fact."
    scene w1_2826 with dissolve
    mc "You doing alright? You ready for this?"
    scene w1_2827 with dissolve
    rose "As ready as I can be..."
    if roseFlag == True:
        scene w1_2828 with dissolve
        rose "I'm glad I'm working with you."

    "Rosalind and I exchanged a few words of solidarity, in the brief moments before Kathleen addressed the room."
    scene w1_2829 with dissolve
    kat "Following that interesting performance by our new slut wife, is Mrs. Rosalind Carter."
    scene w1_2830 with dissolve
    kat "I wonder how she hopes to compete. Such a mild personality, in the body of a {b}breeding cow{/b}."
    kat "You're prepared to give these venerable gentlemen a proper show, right?"
    scene w1_2831 with dissolve
    rose "Yes, Mrs. Pulman."
    scene w1_2832 with dissolve
    kat "Good! The same as Mrs. Ford, then: you've got 20 minutes or until you make Mr. [mcl] ejaculate."
    kat "Show us what you've got, dear."
    stop music fadeout 3.0
    scene w1_2833 with dissolve
    rose "Eh...Uh..."
    scene w1_2834 with dissolve
    rose "......"
    rose "..."
    scene w1_2835 with dissolve
    rose "*Ahem-!*"



label w1ExIntuitionGameRosalind:

    if _in_replay:
        show transitionrosalind01 with cmet
        show screen textbox2 with dissolve
        "Does Rosalind refer to the player character as Sir?"
        hide screen textbox2 with dissolve
        menu:
            "Yes, sir!":
                $ prYesSir = True
            "No.":
                pass
        show screen textbox2 with dissolve

    scene w1_2836 with fade
    play music "music/doll-dancing.mp3"
    "Putting on her best game face, Rosalind dropped to her knees in front of me."
    scene w1_2837 with dissolve
    rose "Valued customer..."
    scene w1_2836 with dissolve
    "That previous look of determination faded away, replaced by a needy and submissive demeanor."
    scene w1_2838 with dissolve
    rose "{b}Thank you{/b} for picking me as your partner tonight."

    if w1RoseGonzo == True:
        "Rosalind bowed as deep as she humanly could, touching her forehead to the floor, in a display of deference and humility. Just as I had her do in our interview."
    else:
        "Rosalind bowed as deep as she humanly could, touching her forehead to the floor, in a display of deference and humility."

    rose "......"
    rose "..."
    "She held that awkward position for some moments, until finally..."
    scene w1_2837 with dissolve
    rose "May I get up, [roseSN]?"
    scene w1_2836 with dissolve
    mct "(Ah, that cheeky woman. She's fully committed here, practically chewing the scenery.)"
    scene w1_2839 with dissolve
    "Looking at the crowd, I was met with a dozen expectant faces, waiting to see how I'd respond to the supplicant woman."
    scene w1_2840 with dissolve
    "The boss is watching and waiting too."
    "I'm just as much under the spotlight tonight as the Carnations."
    scene w1_2842 with dissolve
    "Do I tell her to stand back up?"
    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve

    menu w1ExIntuitionGameRoseDogeza:
        "Not yet. Inform Rosalind what name she will answer to tonight." if w1mcRoseSN == False:
            $  w1mcRoseSN = True
            jump w1ExIntuitionGameMCRoseSN

        "Not yet. Inform Rosalind what she will call you tonight." if w1RoseSNMenu == False:
            $ w1RoseSNMenu = True
            jump w1ExIntuitionGameRoseSN

        "Yes, tell her to stand back up.":
            jump w1ExIntuitionGameRosalindContinue


    menu w1ExIntuitionGameMCRoseSN:

        "From where you stand, she looks like a {b}slave{/b} to you.":
            $ mcRoseSN = "slave"
            show screen textbox2 with dissolve

            mc "Tonight you will answer to [mcRoseSN]."
            mc "Whenever I say [mcRoseSN], I'll be talking about you. You got that?"
            scene w1_2841 with dissolve
            rose "Yes, [roseSN]. I understand."
            rose "May I get up now?"
            hide screen textbox2 with dissolve
            jump w1ExIntuitionGameRoseDogeza


        "You will call her what she is: a {b}whore{/b}.":
            $ mcRoseSN = "whore"
            show screen textbox2 with dissolve

            mc "Tonight you will answer to [mcRoseSN]."
            mc "Whenever I say [mcRoseSN], you should know who I'm referring to. You know why that is?"
            scene w1_2841 with dissolve
            rose "Because..."
            scene w1_2842 with dissolve
            mc "Because what?"
            scene w1_2841 with dissolve
            rose "Because I am a [mcRoseSN]."
            scene w1_2842 with dissolve
            mc "We have an understanding then."
            scene w1_2841 with dissolve
            rose "We do. May I get up now?"
            hide screen textbox2 with dissolve
            jump w1ExIntuitionGameRoseDogeza

        "Go with something cute: babe.":
            $ mcRoseSN = "babe"
            show screen textbox2 with dissolve

            mc "I'm going to call you [mcRoseSN] tonight, is that alright with you?"
            scene w1_2841 with dissolve
            rose "You can call me anything you like, [roseSN]."
            rose "May I get up now?"
            hide screen textbox2 with dissolve
            jump w1ExIntuitionGameRoseDogeza

        "Some roleplaying might be nice: call her {b}mom{/b}":
            $ mcRoseSN = "mom"
            show screen textbox2 with dissolve

            if roseSN == "son":
                mc "Likewise, I'll be referring to you as [mcRoseSN]."
                scene w1_2843 with dissolve
                rose "That makes... sense."
                scene w1_2841 with dissolve
                rose "May I get up now?"


            else:
                mc "Tonight I'll be referring to you as [mcRoseSN]. You got that?"
                scene w1_2843 with dissolve
                rose "That's uh, kinda..."
                scene w1_2842 with dissolve
                mc "It's just a little roleplaying."
                scene w1_2841 with dissolve
                rose "Of course. You can call me anything you like, [roseSN]."
                rose "May I get up now?"
                hide screen textbox2 with dissolve
            jump w1ExIntuitionGameRoseDogeza


        "{color=#4169E1}\[Player Input]{/color} You're going to refer to her as...":
            show screen textbox2 with dissolve
            python:
                mcRoseSN = renpy.input("What will you call Rosalind tonight?")
                mcRoseSN = mcRoseSN.strip()

                if not mcRoseSN:
                    mcRoseSN = "Rose"
                persistent.mcRoseSN = mcRoseSN

            mc "Tonight you'll answer to [mcRoseSN]. Got that?"
            scene w1_2841 with dissolve
            rose "Of course, the customer is always right."
            rose "May I get up, [mcRoseSN]?"
            hide screen textbox2 with dissolve
            jump w1ExIntuitionGameRoseDogeza




    menu w1ExIntuitionGameRoseSN:
        "You can't beat a classic: {b}Master{/b}.":
            $ roseSN = "Master"
            show screen textbox2 with dissolve

            mc "Tonight, I want you to call me master. Is that clear, [mcRoseSN]?"
            scene w1_2841 with dissolve
            rose "Yes, [roseSN]. It is clear."
            rose "May I get up now?"
            hide screen textbox2 with dissolve
            jump w1ExIntuitionGameRoseDogeza

        "You want to feel the affection: {b}Dear{/b}.":
            $ roseSN = "dear"
            show screen textbox2 with dissolve

            mc "Tonight, when you refer to me, call me [roseSN]. Understood?"
            scene w1_2841 with dissolve
            rose "You want me to call you [roseSN]? Of course. If that's what you want."
            rose "May I get up, [roseSN]?"
            hide screen textbox2 with dissolve
            jump w1ExIntuitionGameRoseDogeza


        "You want this to feel taboo: {b}Son{/b}.":
            $ roseSN = "son"
            show screen textbox2 with dissolve

            if mcRoseSN == "mom":
                mc "Likewise, I want you to refer to me as [roseSN]. You got that?"
                scene w1_2843 with dissolve
                rose "That makes... sense."
                scene w1_2841 with dissolve
                rose "May I get up, [roseSN]?"


            else:
                mc "I want you to refer to me as [roseSN]. You got that?"
                scene w1_2843 with dissolve
                rose "That's... That's kinda..."
                scene w1_2842 with dissolve
                mc "It's just some roleplaying."
                scene w1_2841 with dissolve
                rose "O-of course. Anything you wish, [roseSN]."
                rose "May I get up now?"
                hide screen textbox2 with dissolve

            jump w1ExIntuitionGameRoseDogeza

        "{color=#4169E1}\[Player Input]{/color} You'd prefer it if she called you...":
            show screen textbox2 with dissolve

            python:
                roseSN = renpy.input("What do you want Rosalind to call you tonight?")
                roseSN = roseSN.strip()

                if not roseSN:
                    roseSN = "Sir"
                persistent.roseSN = roseSN

            mc "Tonight I want you to call me [roseSN]. Are we clear on that?"
            scene w1_2841 with dissolve
            rose "Yes, [roseSN]. We're clear."
            rose "May I get up now?"
            hide screen textbox2 with dissolve

            jump w1ExIntuitionGameRoseDogeza


label w1ExIntuitionGameRosalindContinue:

    scene w1_2842 with dissolve
    show screen textbox2 with dissolve
    show screen qmenu with dissolve
    mc "Yes, get off the floor."
    scene w1_2844 with fade
    stop music fadeout 3.0
    "Rosalind slowly stood back up, but she didn't quite know where to take our \"show\"."
    rose "Uh... do you..."
    scene w1_2845 with dissolve
    "I watched the wheels turn in Rosalind's head, as she considered her plan of attack."
    scene w1_2846 with dissolve
    rose "Right this way, please."
    scene w1_2847 with dissolve
    play music "music/a-kiss-for-amanda.mp3"
    "She patiently held out her hand, waiting for me to take it."
    scene w1_2848 with dissolve
    "Just as with Felicia, this was her moment. I simply had to follow her lead."
    scene w1_2849 with fade
    "From there, she pulled me over to the couch, where I sat waiting for her to pour me a drink."
    mct "(If this keeps up, I'm going to at least be buzzed by the end of the night.)"
    scene w1_2850 with dissolve
    rose "Whiskey, neat."
    mct "(--or just flat out intoxicated.)"
    mc "Thank you."
    scene w1_2851 with fade
    "Rosalind sat down, saddling up next to me and not-so-subtly pressing her large breasts into my side."
    mc "*Glug* *Glug*"
    scene w1_2852 with dissolve
    "Unlike the sweet tasting whiskey I had earlier in the VIP room, this one was more astringent."
    "Drinking it straight wasn't particularly pleasant, but I did my best not to let that show on my face."
    scene w1_2853 with dissolve
    rose "You don't like the taste, right?"
    scene w1_2854 with dissolve
    mc "You can tell?"

    if roseSeduceFlag == True:
        scene w1_2853 with dissolve
        rose "You told me you weren't much of a drinker, remember?"
        "Rose was referring to the night she tried to seduce me."
        scene w1_2854 with dissolve
        mc "Ah, you remember that, huh?"

    else:
        scene w1_2853 with dissolve
        rose "Your poker face is pretty obvious."
        scene w1_2854 with dissolve
        mc "Is that so?"
        scene w1_2853 with dissolve
        rose "Yes, it's not a very good one."

    scene w1_2855 with dissolve
    rose "Maybe I can help you enjoy it more?"
    "I relinquished my grip and let Rosalind pry the glass from my hand."
    scene w1_2856 with dissolve
    rose "I wonder if this would make it taste better?"
    scene w1_2857 with fade
    "Tilting the glass, Rosalind emptied the whiskey onto her chest."
    "The brown liquid spread itself where gravity took it, rolling down the peaks of her breasts and spilling down into their expansive valley."
    scene w1_2859 with wiperight
    rose "Come closer, please."
    scene w1_2858 with dissolve
    "Like Felicia, she decided to get creative with the alcohol."
    mc "...eh--?"
    "Rosalind kept a calming demeanor as she gently guided my head to her whiskey soaked boob-flesh."
    scene w1_2859 with dissolve
    rose "You like my {b}tits{/b} don't you, [roseSN]?"
    "Where Felicia was an explosion, this felt more like a loving embrace."
    rose "Enjoy them."
    "The matronly woman tightened her grip and pulled me into her breasts."
    scene w1_2860 with dissolve
    "I did as she wished, pursing my lips, stretching out my tongue, and lapping at the beads of whiskey that coated her flesh."
    "It didn't really taste any better, but I couldn't argue that this was a more enjoyable way of drinking the bitter liquid."
    rose "Ah..."
    scene w1_2861 with dissolve
    "Once Rosalind saw I had gotten the idea, she lessened her grip, allowing me free range to {i}really{/i} explore the bounty before me."
    "To start out, I let my tongue play across the top of her chest."
    "Puckering, kissing."
    "Licking, lapping."
    scene w1_2862 with dissolve
    "It's not like I was really picking up much whiskey, but that really wasn't the point, was it?"
    scene w1_2863 with dissolve
    "Gradually, I worked my mouth to the tip of her left breast."
    scene w1_2864 with dissolve
    mc "*Fuuuuuuh*!"
    rose "Oh...!"
    "I teasingly blew a stream of hot air over the surface of Rosalind's nipple."
    scene w1_2863 with dissolve
    rose "What are you doing?"
    scene w1_2864 with dissolve
    mc "*Fuuuuuuh*!"
    "Another steady stream brought it to a fine point. Instead of answering her, I brought lips around the tantalizing tip and latched down."
    scene w1_2865 with dissolve
    rose "Ahh-!"
    scene w1_2866 with dissolve
    "From my position, I could feel her breathing intensify. The eb and flow of her breath pushing and pulling her nipple across the tip of my tongue."
    scene w1_2867 with wiperight
    jim "I bet you wish you could get your perverted lips around those milk jugs. Right, Thomas?"
    scene w1_2868 with dissolve
    tom "Those beauties would be better in a milker..."
    scene w1_2869 with dissolve
    jim "You tit fiend!"
    scene w1ExGame1RoseSuck1 with dissolve
    rose "Ah...! You still have a lot of energy."
    rose "Good... I was afraid you might be tired after... OoOooooh~!"
    "Rosalind's nipples proved extremely receptive to being teased."
    mct "(However, one breast shouldn't get all the attention...)"
    scene w1_2875 with dissolve
    mc "Don't think I forgot this one!"
    "I roughly grabbed her unattended breast, digging my fingers deep into soft fat and tissue."
    scene w1_2876 with dissolve
    rose "A-ah! Please, [roseSN]. Enjoy them as much as you want..."
    "Rosalind was playing her part well. It may have been a less proactive approach than Felicia, but it used her best asset to its full advantage."
    "It was easy to get lost in these puppies. As unwieldly as they are, they were just so perfectly squeezable."
    "Plus, focusing so intently on them let my mind create some distance from being watched."
    scene w1_2877 with dissolve
    rose "Eh-oh! You're switching again?"
    "Rosalind had the skin of a doll. Near flawless and pale. It was a pair of breasts that just begged to be..."
    hide screen textbox2 with dissolve


    menu:
        "Worshiped. [gr]\[Rosalind +2\]":
            $ Rosalind_Affection += 1
            $ Rosalind_Libido += 1
            jump w1ExIntuitionGameRosalindWorship

        "Tormented. [gr]\[Rosalind +2\]":
            $ Rosalind_Libido += 2
            jump w1ExIntuitionGameRosalindTorment


label w1ExIntuitionGameRosalindWorship:

    show screen textbox2 with dissolve
    "She had a pair of breasts that just begged to be worshiped."
    scene w1_2878 with dissolve
    "Pressing her two beautiful orbs together, I returned my attention to giving these babies all the love I could muster."
    scene w1_2879 with dissolve
    mc "*Smooch*"
    "It was an overwhelming task, showering so much titflesh with the affection due them, but I was definitely going to try."
    rose "Eh~! Oh! That feels nice!"
    scene w1_2880 with dissolve
    "I kissed and I kissed."
    "Making sure to anoint each teat generously with my saliva, using my tongue to take a survey of the shape and texture of Rosalind's pebble-like areola."
    rose "Oooh! You're like a hungry baby...!"
    rose "H-huh... I'm getting s-so hot..?"
    scene w1_2879 with dissolve
    "I kissed and I kissed and I kissed."
    "Each pass increasingly filling the exhibition hall with obscene, lewd suckling noises."
    mc "*Fwup* *Chup* Mmm..." with vpunch
    rose "Ah...! I haven't...!"
    mc "*Fwup!* *Kwup!* *Chup!*"
    scene w1_2882 with dissolve
    rose "Mmmh... you really love boobs, don't you...?"
    mc "*Fwup* *Chup* Mmmhmmm...!"
    scene w1_2903 with dissolve
    "I methodically circled the circumference of her areola with my tongue, to make sure every nerve in her soft pink teat was alight with pleasure."
    rose "Oh... [mcf]...! Sorry, I mean... [roseSN]!"
    rose " Ah... [roseSN]♥ Ah, I'm feeling...! I'm feeling...!"
    "Knowing I was making her forget her role, even for a moment, made me smile on the inside."
    scene w1_2904 with dissolve
    mct "(Not one centimeter should go unloved!)"
    mc "*{b}Smoooooch{/b}!* *Chup!* *Fwup!* *Khwup!*"
    rose "I'm feeling so weeeeird~!♥"
    "I turned my affection to the underside of Rosalind's left breast, planting a series of quick kisses."
    scene w1_2881 with dissolve
    rose "Mmh!♥ Y-you're licking the other one now...! "
    mct "(I love it when she states the obvious.)"
    rose "W-why am I feeling so itchy down there? Oh, no... oh, no...!"
    scene w1_2882 with dissolve
    "The sudden change made the desperate mother twitch with pleasure."
    rose "Ah..."
    rose "Ah...!"
    rose "Aaaah-!"
    scene w1_2883 with vpunch
    rose "Aaaaaashhhhhhhh~!♥" with flash
    "I opened my mouth wide and created a vacuum like seal, suctioning the wanton mother's puffy nipple {i}hard{/i} and battering it with my tongue in a one-two punch that sent her over the edge."
    "Rosalind cocked her head back and emitted a shrill cry of unmistakable pleasure." with flash
    rose "Ah...♥ Ah..♥ ...eh, ohohoh...♥ [roseSN]...♥"
    mct "(--eh?! Did she just really...)"
    stop music fadeout 3.0
    scene w1_2884 with wipeleft
    sam "Haha, oh man. That's rich!"
    scene w1_2885 with dissolve
    tom "Amazing!"
    scene w1_2886 with dissolve
    jim "Did that cow actually cum from just her tits? How's that supposed to be {b}service{/b} anyway?"
    scene w1_2887 with wiperight
    chuck "Service is anything the customer wants, Jim. Going by the way the lad went after those things..."
    chuck "I say she's doing a pretty damn good job!"
    scene w1_2888 with fade
    "Content that I had worshipped every single nook and cranny of her voluptuous chest, I pulled myself back and took at look at my handy work."
    rose "*Huff* *Huff* Ho... hoh... he..."
    rose "{b}Fuck{b}..."
    rose "That was..."
    jump ExIntuitionGameRosalindHJ


label w1ExIntuitionGameRosalindTorment:

    show screen textbox2 with dissolve
    stop music fadeout 3.0
    "She had a pair of breasts that just begged to be tormented and skin that {b}needed{/b} to be marked."
    scene w1_2889 with dissolve
    rose "Ah--! Wha-?"
    "With no hesitation, I dug my teeth into her right breast."
    "Not enough to draw blood of course, but hard that the desperate mother could feel it."
    scene w1_2890 with dissolve
    play music "music/leaving-home.mp3"
    play sound "sound effects/slap2.wav"
    scene w1_2891 with hpunch
    "*Thwack!*"
    rose "Ghh-!"
    scene w1_2892 with dissolve
    rose "W-why are you..."
    scene w1_2893 with dissolve
    mc "You said I could do whatever I desired, right [mcRoseSN]?"
    scene w1_2894 with dissolve
    "She looked at me heistantly, before answering."
    scene w1_2895 with dissolve
    rose "... o-of course. My breasts belong to you."
    scene w1_2896 with dissolve
    mc "These things are so fucking obscene that they deserve to be punished!"
    scene w1_2897 with dissolve
    "Obviously, what I said didn't make any damn sense, but it sounded good to my lust-addled mind."
    play sound "sound effects/slap2.wav"
    scene w1_2898 with hpunch
    rose "--gah!"
    scene w1_2899 with dissolve
    mc "Thank me, [mcRoseSN]."
    rose "...huh?"
    play sound "sound effects/slap2.wav"
    scene w1_2900 with hpunch
    rose "Eeeeh, shit...!"
    scene w1_2899 with dissolve
    mc "Thank me for abusing your breasts!"
    scene w1_2901 with dissolve
    rose "Thank you!"
    play sound "sound effects/slap2.wav"
    scene w1_2902 with hpunch
    rose "--gh!"
    scene w1_2899 with dissolve
    mc "For what, [mcRoseSN]?"
    play sound "sound effects/slap2.wav"
    scene w1_2898 with hpunch
    rose "Eeeeeh-- Thankyouforabusingmybreasts--!"
    scene w1_2874 with dissolve
    mc "*Smooch*"
    "My sadistic urge satisfied, I planted a kiss at the spot I had repeatedly smacked."
    "A iron fist, velvet glove approach."
    scene w1_2875 with dissolve
    mc "You're a good girl."
    scene w1_2880 with dissolve
    "I brought my mouth back to her soft-pink teat and dug my fingers into the side of her breasts."
    rose "Ah, you're sucking on them now..."
    rose "That feels... nice."
    scene w1_2879 with dissolve
    rose "You're being so..."
    "The sudden change in approach made the desperate mother twitch with pleasure."
    scene w1_2890 with dissolve
    play sound "sound effects/slap2.wav"
    scene w1_2891 with hpunch
    "*Smack!*"
    scene w1_2892 with dissolve
    rose "Eh...! Again?"
    scene w1ExGame1RoseSuck1 with dissolve
    "Without a moment of respite, I went back to the tender approach. Sucking, kissing, licking at the nerve-filled target."
    rose "Ghh- ah-♥"
    rose "Thank you for a-abusing my breasts..."
    mct "(She remembered!)"
    "Rosalind was managing to keep her composure. That was good."
    scene w1_2904 with dissolve
    "I kissed and I kissed."
    "I kissed and I kissed and I kissed."
    "I kissed and I kissed and I kissed, until..."
    scene w1_2905 with vpunch
    rose "S-shit!" with flash
    "I changed gears once more, roughly grabbing her by both teats and squeezing down. To my surprise..."
    scene w1_2906 with dissolve
    rose "Ggeeee-!♥" with flash
    "Rosalind let out an animalisic owl, a strange consolidation of pain and pleasure rolled into one." with flash
    mct "(--eh?! Did she just...)"
    scene w1_2884 with wipeleft
    stop music fadeout 3.0
    sam "Haha, oh man. That's rich!"
    scene w1_2885 with dissolve
    tom "Amazing!"
    scene w1_2886 with dissolve
    jim "Did that cow actually cum from being abused? How's that supposed to be {b}service{/b}..."
    scene w1_2887 with dissolve
    chuck "Service is anything the customer wants. Going by the way the lad attacked those things..."
    chuck "I say she's doing a pretty damn good job!"
    scene w1_2888 with dissolve
    "I was shocked as well. Rosalind had a glassed over expression."
    "Never in my life would I expect to see a woman orgasm from having her breasts abused."
    rose "{b}Fuck{b}... Wh-What..."
    rose "What just happen? Did I really just..."
    "Even Rosalind looked utterly confused. There was a trace of fear in her face too."
    "Part of me wanted to give her a hug, but before she even had time to process what she just learned about herself..."
    jump ExIntuitionGameRosalindHJ


label ExIntuitionGameRosalindHJ:

    scene w1_2907 with dissolve
    kat "Charles is right."
    scene w1_2908 with fade
    kat "That said, even if what little smarts you have get fucked out of your stupid head, the job is to satisfy the customer. {b}Completely{/b}."
    scene w1_2909 with dissolve
    kat "Time. Is. Ticking."
    rose "Uh, r-right!"
    scene w1_2910 with dissolve
    "Getting back on track and pushing her post-orgasm jitters aside, Rosalind refocused on the game at hand."
    scene w1_2911 with cmet
    play music "music/jazz-piano-bar.mp3"
    rose "That was incredible, [roseSN]!"
    scene w1_2912 with dissolve
    "Lurching forward, the curvy woman pulled me into a deep, gentle kiss."
    rose "Mmmh~ *Smooch!*"
    "Rosalind hummed pleasantly as she took the lead, using her soft tongue to infiltrate my mouth and intermingle with my own."
    "She lovingly ran a hand up and down my back in a reassuring fashion. It added a soothing, comforting touch to this obscene situation."
    rose "*Chup* *Chwup!*"
    "I was happy to just squeeze my eyes shut and luxuriate in Rosalind's affection."
    scene w1_2913 with dissolve
    rose "...Mmmhah~♥"
    "After a short time, the kiss was painfully broken."
    scene w1_2914 with dissolve
    rose "That was the first time I've felt that good from just my..."
    scene w1_2915 with dissolve
    "The doe-eyed woman trailed off, either not knowing how to admit the truth about her sensitive body or not wanting to fully put it into words."
    scene w1_2914 with dissolve
    rose "However, it's my turn to show appreciation. Just lie back and let me take care of you, [roseSN]."
    scene black with fade
    "Guiding me to her lap, she had me lay down in a rather vulnerable position."
    scene w1_2916 with dissolve
    "I wasn't quite sure what her plan was here, but nevertheless my dick was standing straight up like a beacon for all the room to see."
    "In spite of cumming not 15 minutes ago, I was {i}hard{/i} and rearing to go once more."
    scene w1_2917 with dissolve
    rose "That's it. Relax for me."
    scene w1_2916 with dissolve
    "She spoke as if her words were a lullaby."
    scene w1_2918 with dissolve
    mc "What's with this position?"
    scene w1_2917 with dissolve
    rose "You seemed enamored with my breasts so..."
    scene w1_2920 with dissolve
    hide screen textbox2 with dissolve
    "Using one hand to guide my head to her breast, she positioned the other around my cock, gripping it on end."
    scene w1_2919 with dissolve
    rose "Enjoy them some more while I show you how much I love you."
    scene w1_2920 with dissolve
    "Rosalind was taking an interesting approach to the game."
    scene w1ExGame1RoseHJ1 with dissolve
    "Slowly, she began to jerk off my overly swollen member."
    "Being laid across her thighs, cradled like an infant, left me nothing to do except for what she intended."
    scene w1ExGame1RoseHJ2 with dissolve
    rose "Good! You've got the idea."
    mc "Mmmhh--!"
    "Her cool hand may have felt nice against my burning prick, but the methodical pace felt like torture."
    "Sometimes even a whole second passed in between her faltering jerks. I don't know if she was doing it on purpose, but if she was, it was devilish."
    rose "Hmm~ Hm-hm-hm~ That's right, [roseSN]..."
    "Rosalind had an almost serene look as she milked me."
    kat "Hmpfh. This is certainly a new approach."
    tom "She's perfect...!"
    mc "Ngg-!"
    scene w1ExGame1RoseHJ1 with dissolve
    "This pace was just too much! I had to..."
    hide screen textbox2 with dissolve

    menu:
        "Ask her to speed up.":
            scene w1_2926 with dissolve
            mc "Ah, too slow! Could you please..."
            scene w1_2919 with dissolve
            rose "Of course, [roseSN]. This is all about you."
            scene w1ExGame1RoseHJ3 with dissolve
            "It really wasn't. Deep down I knew that. This was all just a bizarre game and I was merely a prop dick. However, her words almost had me convinced."
            "A testament to either her natural temperament or her skill as an actress."


        "Tell her to speed up.":
            scene w1_2927 with dissolve
            mc "Speed up, you whore!"
            scene w1_2919 with dissolve
            rose "Of course, [roseSN]. This is all about you."
            scene w1ExGame1RoseHJ3 with dissolve
            "It really wasn't. Deep down I knew that. This was all just a bizarre game and I was merely a prop dick. However, her words almost had me convinced."
            "A testament to either her natural temperament or her skill as an actress."

    "At my ushering, she adopted a more persistent pace. It still wasn't the toe-curling intensity that would bring me to climax, but it was an improvement."
    scene w1_2928 with dissolve
    rose "Hehe, you've got such an expressive penis."
    "She expressed an odd thought as she jacked me off."
    scene w1_2929 with dissolve
    rose "The way it twitches and responds to a little affection is cute."
    rose "Oh.. not to say your penis is {i}little{/i} or {i}cute{/i}..."
    scene w1_2930 with dissolve
    rose "Your dick is actually very... handsome."
    "It was a little surreal given that she was already jerking me off in front of a room of a dozen people, but her face flushed with embarrassment."
    mct "(Ah, whatever...)"
    scene w1ExGame1RoseHJ3 with dissolve
    "Shutting my eyes and sucking on Rosalind's teat, I focused on pure sensation."
    "The feeling, taste, and texture of Rosalind's swollen areola..."
    "The lulling song that she was intermittently humming."
    "The unceasing, carnal noise of flesh-on-flesh contact."
    "Even the comfort of being close, attached at the breast."
    "It was a sensory overload. Being so close to Rosalind, focusing on the small details, made me feel like it was really just the two of us."
    rose "Hmm~ Hm-hm-hm~ That's right, just let it all go..."
    rose "Let all the stress melt from your body. Just focus on your pleasure. Focus on forgetting all your worries. Your fears. Your shortcomings..."
    rose "None of that is real, because you are {b}perfect{/b}."
    rose "It's just you and me, [roseSN]."
    rose "Hmm~ Hm-hm-hm~ Just let it all go..."
    scene w1ExGame1RoseHJ4 with dissolve
    mc "Ah-ooh--!"
    "After landing me on the hook, that's when Rosalind began to reel me in."
    "She intensified her ministrations on my lower body, building more and more into a frenetic pace."
    rose "It's just you and me, [roseSN]."
    "It made for a strange contrast. She had soothed my mind, but the increasingly building ache in my balls threatened to upend the serenity."
    rose "It's just you and me, [roseSN]..."
    "As Rosalind's hand became coated more and more in my pre-cum, the sounds became more lewd and sex like."
    mc "*Plap* *Plap!* *Plap--! Mmmng! Ah! Rose--"
    rose "Ssssh. Sssssh. Don't try to hold on. Just let it happen, baby."
    rose "{b}Explode{/b} for me!"
    stop music
    scene w1_2935 with flash
    play sound "sound effects/spurt.wav"
    mc "Ghhhhh--!"
    mct "(Shit! Fuck! Fuck! Shit!)"
    scene w1_2936 with flash
    play sound "sound effects/spurt.wav"
    "She knew it even before it did. Clamping down tight with her hand just before I burst, she released her grip at just the right time to send a fountain of cum raining down on me, the couch, and Rosalind's evil hand."
    mct "(It's still coming...?)"
    play sound "sound effects/spurt.wav"
    scene white with w20
    mct "(Ah...!)"
    "I was coming so hard, it felt like I overlocked my brain. My mind briefly became a sheer blanket of white."
    scene w1_2937 with fade
    show screen textbox2 with dissolve
    play music "music/epic-battle-speech.mp3"
    mc "What the... what the fuck?"
    "When I regained my senses and opened my eyes..."
    scene w1_2938 with dissolve
    rose "*Slurp*!"
    scene w1_2939 with dissolve
    rose "*Slurp!* *Slurp!* Ah, delicious, [roseSN]."
    mc "Wow..."
    scene w1_2940 with dissolve
    chuck "Who knew anyone could cum that much a {b}second{/b} time. I don't know if that was the lad or Mrs. Carter's doing."
    scene w1_2941 with dissolve
    kat "Probably a little of both. That was certainly... interesting."
    kat "A strong first impression I'd say. I'd ask you to take a bow, but..."
    scene w1_2942 with dissolve
    kat "Let's give our \"customer\" a 5 minute break. He looks like he needs it."
    scene black with fade
    "......"
    $ renpy.end_replay()
    if not persistent.roseExhibition1Game1:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.roseExhibition1Game1 = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)
    "..."

label w1ExIntuitionGameVeronica:

    if _in_replay:
        show transitionveronica02 with cmet
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
    scene w1_2943 with fade
    kat "Last we have Miss Lynch, but she is certainly not {b}least{/b}. Is she?"
    scene w1_2944 with dissolve
    "After a very short intermission, Veronica took the stage."
    "Her expression was hard to read. Arms crossed, she peered out at the crowd with a indiscernible look on her face."
    scene w1_2945 with dissolve
    ver "You've got that right."
    scene w1_2944 with dissolve
    "I had a feeling letting the other two go first was a strategic decision on her part."
    scene w1_2946 with dissolve
    kat "You understand the game's parameters, Miss Lynch?"
    scene w1_2947 with dissolve
    ver "I do. Twenty minutes or until [mcf] ejaculates, whatever comes first."
    scene w1_2948 with dissolve
    kat "Good. Then without further ado, let's wrap up the first game with a bang."
    scene w1_2949 with dissolve
    kat "Make it a worthwhile conclusion."
    scene w1_2950 with dissolve
    ver "Hmmm..."
    scene w1_2951 with dissolve
    mct "(I wonder how she's going to approach this.)"
    mct "(For {i}some{/i} reason, I'm having trouble picturing Veronica being all \"yes, sir\"...)"
    stop music fadeout 3.0
    sam "*Whistle* {b}Fhwooooooooo!{/b}"
    jiji "The girl's got an impressive physique."
    scene w1_2952 with dissolve

    if kat_polite == True:
        mct "(She certainly finessed Mrs. Pulman a few weeks ago...)"
    else:
        mct "(She certainly finessed Kathleen a few weeks ago...)"

    chuck "She's not wasting any time."
    scene w1_2953 with dissolve
    mct "(--huh?)"
    "The murmuring in the room brought my attention back to a somewhat surprising scene."
    play music "music/jack-the-lumberer.mp3"
    scene w1_2954 with wipeleft
    "While I was lost in thought, Veronica had fully shed her costume and proudly put her chiseled physique on display."
    scene w1_2955 with dissolve
    ver "You're looking worn out, {b}[veroSN]{/b}."
    scene w1_2954 with dissolve
    "Veronica had a matter-of-fact customer service look scribed onto her face. It wasn't exactly warm, but it also didn't come across as fake."
    scene w1_2956 with dissolve
    mc "Yeah, you could say that..."
    scene w1_2954 with dissolve
    "Back-to-back orgasms coupled with the stress of being the spotlight did have me feeling drained."
    scene w1_2957 with dissolve
    ver "Lucky you, then! I know a little something about relieving tension."
    "Veronica's voice carried boisterously through the exhibition hall."
    scene w1_2958 with dissolve
    mc "Is that so?"
    scene w1_2959 with dissolve
    ver "Definitely. It just so happens..."
    scene w1_2960 with dissolve
    play sound "sound effects/knuckles-cracking.wav"
    pause 1.0
    play sound "sound effects/knuckles-cracking.wav"
    ver "*{b}Crack, Craaaack!{/b}*"
    scene w1_2961 with dissolve
    ver "I give a killer massage."
    scene w1_2960 with dissolve
    mct "(Is it my imagination or was there an emphasis on the {i}killer{/i} part?)"
    scene w1_2962 with dissolve
    mc "A massage... doesn't sound too bad, actually. Where should I...?"
    scene w1_2963 with dissolve
    ver "Just stay seated. I'll come to you."
    "Veronica positioned herself beside me, wagging her broad hips enticingly along the way."
    scene w1_2964 with dissolve
    mc "You sound confident in your skills."
    scene w1_2965 with dissolve
    ver "You're speaking to the unofficial massage therapist of the 2012 US Women's Olympic shot put team."
    scene w1_2964 with dissolve
    mc "Seriously?"
    scene w1_2966 with dissolve
    ver "It's a strenuous sport. Lots of aching muscles."
    scene w1_2967 with fade
    ver "A good massage is mechanical. A great massage has artistry to it. You want know what I discovered while tending to my teammate's sore {b}bodies{/b}?"
    scene w1_2968 with dissolve
    mc "...well?"
    scene w1_2969 with dissolve
    ver "Full-on uninhibited, naked skin-to-skin contact... that's the secret sauce."
    "Suddenly I felt Veronica press her weight into my back, leaving her heavy chest to rest on my shoulders."
    scene w1_2970 with dissolve
    ver "If both of us are nude, there's nothing to dull the sensation of touch. Plus, it makes things more... exciting."
    "Veronica spoke directly into my eardrum, sending a shiver through my body with her words."
    scene w1_2971 with dissolve
    mc "I did wonder why you {i}immediately{/i} took your clothes off..."
    scene w1_2972 with dissolve
    ver "I think you'd agree I look better without that dumb thing on anyway, but yes. This is all done to maximize your comfort, Mr. {b}Vee{/b}.{b}Eye{/b}. {b}Pee{/b}."
    "To compound the teasing, Veronica pressed her pert cherry-like nipples and drug them up my back."
    ver "May I begin, [veroSN]?"
    stop music fadeout 3.0
    "It felt like Veronica was being excessively glib for what's supposed to be a game about service, but there {b}was{/b} something endearing to her swagger."
    scene w1_2971 with dissolve
    mc "Whenever you'd like."
    scene w1_2973 with dissolve
    "She paused for a moment, before placing two pleasantly warm hands around my neck."
    play music "music/anacaptainslogue.mp3"
    ver "Some oils would make this even better, but we'll make do."
    "Veronica started out with my head, moving one hand slowly up my neck, squeezing and releasing as she went."
    "After running out of neck to travel up, she made her way back down, using her fingers to trace a circular motion down from the base of my skull to my shoulders."
    scene w1_2974 with dissolve
    "From there, the lumbering woman began to knead the top of my shoulders, gently working her finger tips over flesh and muscle."
    "To my surprise, it had an almost immediate effect. The sensation of tension being released."
    mc "It's funny how long it takes you to realize you're actually feeling pretty stiff, huh?"
    scene w1_2975 with dissolve
    ver "People don't listen to their bodies as much as they should."
    "As she worked her way down to my deltoids, the amazon not-so-carelessly allowed the hardening points of her breasts to brush against the skin of my back."
    mc "What's your body telling you right now?"
    ver "That both of us are going to be turned on by the end of this massage."
    "She wasn't wrong. I was quickly beginning to feel the flames of sexual desire well up in me again, so soon after climaxing back to back."
    mc "You're really good at this."
    "The force she was applying to my shoulders increasingly shifted from gentle to firm, as she began using the base of her hands to lift up muscle."
    ver "What did I tell you? I've practiced."
    scene w1_2976 with dissolve
    "To finish off my shoulders, Veronica put her weight into it. Using the strength of her dense muscles to press down hard and really make me feel it."
    mc "OoOooOh..."
    "It hurt a little, but it wasn't unpleasant. She had perfect control of her hands and the understanding of just how much force to use to loosen up overworked muscles."
    ver "I think it's time to move on to other parts of your body."
    scene w1_2977 with fade
    "Suddenly, the tall woman climbed around my side and straddled me. Putting me face to face with Veronica's freckled breasts."
    ver "I would've liked to spend more time working the whole of your back, but we don't exactly have a massage table."
    "Having our bodies pressed together this closely gave me a greater appreciation of Veronica's size. Not just her large frame, but there was also of course the sheer volume of her muscle mass."
    "As her body leaned into mine, with the exception of her breasts, I felt very little give from her naked flesh. It almost felt like I was laying against a wall."
    ver "Give me your hand, please."
    scene w1_2978 with dissolve
    "Taking my hand in hers, she rubbed each of my fingers, one by one. Starting from the base and moving to the tip, before lightly pulling on each finger."
    mc "I've never had a hand massage before. I never would've guessed, but it feels pretty nice."
    "Next she started massaging the pad of my hand, moving her fingers in a circular motion and working her way along its natural contours."
    scene w1_2979 with dissolve
    ver "I'm going to make my way down now."
    scene w1_2980 with fade
    "Lifting herself off of me, Veronica got down on her knees, coming face to face with my cock."
    "The close bodily contact had me semi-hard and I shivered in anticipation as Veronica's scrutinizing gaze unflinchingly fell on my member."
    scene w1_2981 with dissolve
    "Disappointingly, Veronica slid her hands down my legs and grabbed one of my feet and began working it much in the same way she did my hands."
    ver "Never had a foot massage either, I bet."
    mc "No, I haven't."
    "Placing her thumbs on the sole, she worked her way from the ball of my foot all the way down to the heel."
    mc "Ah, yeah... that feels good."
    ver "It's just what you needed, right? What After Rose and blondie emptied your balls."
    ver "You need to recharge a little. Just jumping into things wouldn't be good for either of us."
    scene w1_2982 with dissolve
    "Veronica shared her strategy aloud, for both me and the room to hear."
    ver "You don't mind me taking it slow, do you [veroSN]?"
    mc "That sounds rather agreeable, actually."
    "By this point, I had become relatively adjusted to being on stage. It's not like the crowd was completely out of my mind, but I managed to turn my thoughts into words without tripping over myself."
    scene w1_2983 with dissolve
    "After finishing up with my last foot, Veronica extended her long legs and suddenly stood up, giving me an eye-level view of her breasts pleasantly bouncing as she did."
    scene w1_2984 with dissolve
    ver "I'm going to dance for you now, but first I'm going to fetch you a drink. Keep your ass in that seat."
    scene w1_2985 with dissolve
    "Veronica was barely trying to hide her natural personality. Whether that would help or hurt her in this game, who knows..."
    scene w1_2986 with dissolve
    mc "What like a strip tease? You can dance?"
    scene w1_2987 with dissolve
    ver "Not quite like that, considering I've got nothing to strip off, but something good for the eye just the same."
    ver "You sound surprised."
    scene w1_2988 with dissolve
    stop music fadeout 3.0
    ver "I actually used to teach a pole dancing class at an old gym I used to work at."
    scene w1_2989 with dissolve
    "If I sounded surprised, it was because I was. It was hard to picture a towering woman like Veronica moving around gracefully."
    scene w1_2990 with dissolve
    mc "What's this?"
    scene w1_2991 with dissolve
    ver "Water. You don't need any more alcohol."
    scene w1_2992 with dissolve
    "I appreciated the small kindness."
    scene w1_2993 with dissolve
    play music "music/dancebroom-riddim.mp3"
    sam "*Whistle* Fwhooo!"
    "As she turned around to create some distance for her dance, the crowd who had been silently observing up to this point, broke out with a sharp whistle."
    "Veronica responded with a dismissive wave, swatting at the air as if to say she already knew that."
    scene w1_2994 with dissolve
    ver "Eyes on me, errand boy."
    scene w1_2996 with dissolve
    "Veronica started out simple, shaking her hips and putting an emphasis on her beautifully sculpted lower half - her tree trunk like thighs and the contours of her heart-shaped ass."
    scene w1_2995 with dissolve
    "Slowly, she increased the tempo. Throwing her whole body into the performance, each twist and turn causing her incredibly toned musculature to ripple beautifully."
    scene w1_2996 with dissolve
    "The minutes passed, but she showed no signs of slowing down."
    scene w1_2997 with dissolve
    "Meanwhile, she kept her focus on me. Using her eyes, expressions, and of course her body to hold my attention on her."
    scene w1_2998 with dissolve
    "Until Veronica started to advance toward me. Each step keeping rhythm as her hips swayed pleasantly to an unheard song."
    "My focus was drawn to her midsection, hypnotized by the way her muscular stomach bent and curved along with her stride. All the way until it was right in front of my eyes."
    scene w1_2999 with dissolve
    "Instead of using words, she let hands do the talking. Teasingly sliding them up the curves of her hips, darting across her stomach, and finding perch at her freckled breasts."
    ver "Mmmh...."
    "The redheaded amazon purred with pleasure as she used the tips of her fingers to prod and tweak her puffy, nub-like areolas."
    scene w1_3000 with dissolve
    mc "Is this still part of the dance?"
    scene w1_3001 with dissolve
    "Slinking down to her to her crotch, Veronica began playing with the folds of her cunny before finally speaking."
    scene w1_3002 with dissolve
    ver "You like what you see?"
    scene w1_3003 with dissolve
    scene w1_3004 with dissolve
    scene w1_3003 with dissolve
    "I dutifully nodded yes."
    scene w1_3002 with dissolve
    ver "Then grab my ass, errand boy."
    scene w1_3005 with dissolve
    "Doing as commanded, I quickly reached around Veronica's broad hips and scooped up a handful of taut skin and muscle."
    ver "C'mon! Do it like you mean it!"
    scene w1_3006 with dissolve
    "At the amazon's command, I tightened my grasp. A lot of good it did me. Unlike Rosalind, who's ass was pleasantly plush, Veronica's had very little cushion to her tush."
    "It was the kind of ass that screamed, at least to my growingly perverse mind, \"ride me like a horse\"."
    ver "Good..."
    "Her voice dropped two octaves, before bracing herself against my shoulder and going to town."
    image w1VeroSchlick= Movie(play="w1VeroSchlick.webm")
    image w1VeroSchlick2= Movie(play="w1VeroSchlick2.webm")
    show w1VeroSchlick with dissolve
    "At this distance, I was privy to more detail than I could have ever imagined."
    "The way the lumbering woman's fingers parted her labia, the her thumb arrhythmically brushing against her clitoris, and the increasing blush in the skin around her vulva."
    scene w1_3007 with dissolve
    eric "She's really just going to shamelessly masturbate?"
    scene w1_3008 with dissolve
    kat "It usually takes a lot more prodding on my part to get a girl to do that."
    scene w1_3009 with dissolve
    vinc "Ha, what a slut!"
    scene w1_3010 with dissolve
    sam "Shut up! She's putting on a proper show for you assholes!"
    hide screen textbox2 with dissolve
    show w1VeroSchlick2
    hide w1VeroSchlick
    "Instead showing irritation at all the inane comments, Veronica peered down into my eyes, her own half-lidded from the pleasure of her debasement."
    ver "*Schlick!* *Plap!*"
    "Wet, sticky sounds permeated the air as Veronica became increasingly more stimulated."
    ver "*Schlick!* *Plap!* *Schlick!*"
    "Thick feminine juices coated Veronica's fingers, easily visible and glistening thanks to the sweltering spotlight that hung overhead."
    ver "Ah...♥ This is kinda fucking weird, ain't it? This is all new to me of course...Ehaa-♥"
    "Veronica let out an honest thought in between candied moans."
    mc "Tell me about it..."
    ver "*Schlick!* *Plap!*"
    ver "*Schlick!* *Plap!* *Schlick!*"
    ver "What's going on in your head, [mcf]? You like this shit? You enjoying the show?"
    mc "A--"
    ver "That was rhetorical. Don't answer that. I can tell just by looking at your big, dumb prick of yours."
    show w1VeroSchlick with dissolve
    hide w1VeroSchlick2
    "Not like I could deny it anyway. I was fully erect. Veronica's peepshow had succeeded in recharging my batteries."
    ver "You're a perverted little fuck, you know that?"
    "I could tell from her expression that the sexual tension was mounting. As it did, it seemed Veronica got more aggressive."
    mct "(So this is how she's intent on playing it.)"

    if w1ExTease == True or w1ExInControl == True:
        "I wasn't sure if Veronica had intuited what I wanted or intended that to be a genuine indictment, but either way, she was taking it in a combative direction."
    else:
        "I wasn't sure if that was meant as pillow talk or a genuine indictment, but either way, she was taking it in a combative direction."

    if toughness >=22:
        mc "Takes one to know one, bitch. You're the one jilling yourself off right now."
    elif toughness >= 15:
        mc "Don't act like you don't have a hand in making me like that. You're putting on a damn good show!"
    else:
        mc "Maybe, but you're the one who's making me like that."

    ver "Oh? You want me to take responsibility? Is that what you're saying?"
    show w1VeroSchlick2 with dissolve
    hide w1VeroSchlick
    "Veronica formed her mouth into a wide, toothy, lascivious grin. It felt like that moment of tension in nature documentaries just before the lion jumps out of the grass and seizes the antelope."
    ver "If you're rearing to go, I won't stop you. Go ahead and stroke your dick."
    "Even with my renewed arousal from the muscular woman's lewd show, popping off twice in the span of thirty minutes had left me feeling pretty satisfied."
    mct "(Though, I'd feel bad if I hung her out to dry here in front of the club...)"
    mct "(I know! There's something else that could be fun.)"
    ver "Well, you gonna do it? I know you want to."
    mc "I don't think I will."
    "A tiny hint of concern unveiled itself in her eyes, like I was about to jeopardize her shot at winning the game by being uncooperative."
    "I had to admit a small part of me thought it might be fun to roast the stoic woman over the coals, just to see how she'd react, but that would to cruel considering the situation."
    mc "I have something else in mind."
    scene w1_3011 with dissolve
    show screen textbox2 with dissolve
    "Slinking off the ottoman and onto my knees, I positioned myself at the towering amazon's feet, angling it so my head came face-to-face with her crotch."
    ver "*Schlick!* *Plap!* *Schlick!*"
    "In the mean time, her masturbation hadn't slowed one bit. The only thing that changed, aside from my posture, was a curious look in her eyes."
    "The gears turned in her head, until it finally clicked in place and she picked up on what I was intended."
    scene w1_3013 with dissolve
    ver "Oh... does errand boy want some puss?"
    scene w1_3012 with dissolve
    "I slowly nodded my head, putting on what I hoped was a sly grin."
    scene w1_3014 with dissolve
    ver "Heh, well... the customer is always right, eh?"
    scene w1_3015 with dissolve
    "Veronica's masturbation slowed to a halt and the glassed over look gave way to an eager and predatory one."
    scene w1_3016 with dissolve
    ver "Don't stall then. Get the fuck over here."
    "Veronica invitingly parted her thighs, granting me access to her sweet spot."
    "Beads of femcum, displaced by the amazon's abject self-pleasuring, coated the pubic hair around her vulva."
    scene w1_3017 with dissolve
    "Not dilly-dallying, I set to work, repeatedly tracing the outer folds of her labia with the tip of my tongue."
    ver "That's right...♥ Lick me, [mcf]."
    "Pretty soon, I was coating Veronica's cunny in a thick mixture of saliva and vaginal discharge. From bottom to top, until I..."
    ver "Ah...!"
    "Until reached her clitoral hood and began peeling back the fold of skin with my tongue, to get at the hidden pearl inside."
    hide screen textbox2 with dissolve
    scene w1_3018 with hpunch
    ver "Ah... fuck yeah!"
    mc "Ehoh...?!"
    "The tip of my tongue reaching her sweet spot was like springing a bear trap, causing the amazon's meaty thighs to clamp around my neck with an almost alarming force."
    scene w1_3020 with dissolve
    ver "You're not going anywhere, so don't stop licking...♥"
    "Once the alarm of having a set of large, muscular thighs clamp down around my head was passed, I figured I had no choice but to get back to work, lest I start to run out of air."
    "However, having my mouth sandwiched against Veronica's vulva and my nose smack dab on her clit, left me only one path forward in pleasuring her."
    scene w1_3019 with dissolve
    "I drove my tongue past the protective folds and into her opening."
    ver "That's right. You've got the idea...♥ Do a good job for me, okay?"
    "Veronica's normally husky voice dropped down an octave, as she choked out a command that sounded more like a pleasured plea."
    "It was an exhilarating experience, being tucked between the giant woman's massively powerful thighs. It filled me with my own growingly desperate desire to please her."
    "My head was awash with an odd mix of feelings. Of surprise at how good it felt to give up control, but also with a contradictory desire of wanting to wrest it from the hulking woman."
    "To pleasure her until her legs gave way and she collapsed like a pile of wet rags, a dumb slutty look on her face."
    mc "...!"
    "It was this line of thinking that emboldened my effort, as I used me tongue to reach deeper and deeper, scraping and teasing the slimy walls of her love tunnel."
    scene w1_3021 with dissolve
    ver "Oooh~oh..♥ You are... you are..."
    ver "--not bad at this."
    mct "(Not bad, huh? Time to get creative!)"
    "Using my nose in conjunction with my tongue, I pressed it hard into Veronica's clit used it to rub and caress the sensitive nub."
    ver "Eeeeh...♥" with vpunch
    "It got me the reaction I was looking for, as Veronica squeezed her thighs tighter in overstimulation, pushing me even closer and giving my tongue greater access to her depths."
    scene w1_3022 with dissolve
    ver "Fine... fine!"
    "Veronica wasn't content in letting me do all the work of course, soon I could feel her hips start rocking, her inner walls clamping and sliding up and down my tongue like it was a cock. Working in tandem to provide even greater stimulation."
    ver "You're at least half-good too!"
    jim "She's going to suffocate the kid."
    chuck "Not the worst way to die!"
    "Between my laborious efforts and vice like leglock on the back of my neck, I was slowly losing my breath. Something that should be distressing, but felt more like a call to action."
    ver "Eh..."
    mc "*Slurp* *Slurp* *Slurp...!*"
    ver "Ehehe...!"
    "I bobbed my head in an violent, erratic pace. Not letting the buxom redhead get a chance to get used to one specific pace or pattern."
    "Lapping at her insides with a hunger-like frenzy, her inner walls attempted to constrict and clamp down on my tongue for naught, unable to get a grip on the slick, wiry muscle."
    scene w1_3021 with dissolve
    ver "Ah... ah... Ah-♥ Nggh... ah-♥ Mother fucker! You're getting that thing deep in there! Wh-what are you trying to do, taste my cervix?"
    mc "*Slurp* *Slurp* *Slurp...!*"
    "Veronica's thighs twitched as the assault continued. The thick vascularity in her legs pulsating from heightened arousal."
    ver "Egh...euhh...eugh...!"
    "Even in my cunt-licking stupor, I could pick up Veronica's breath slowing to a deep and irregular pace."
    scene w1_3023 with dissolve
    kat "Wonderful. Your face is twisted up like a Picasso painting, Miss Lynch."
    ver "S-shut up, you old hag!"
    kat "Watch your mouth whore, before I invite the whole room to cum and then shit down your throat."
    ver "Tsk...!"
    "Veronica was (rightly) agitated, but to my surprise, she had enough sense to hold her tongue."
    scene w1_3021 with dissolve
    ver "EeeeeEEeeeeh!"
    "Instead, she gripped the back of my head with both hands, thrusting her hips and by effect practically fucking my face."
    ver "Shit! Fuck! Damn!"
    "A slew of expletives clued me in I was getting close. It was good timing, because my tongue was feeling the strain of the violent, ceaseless wiggling it was doing."
    scene w1_3024 with vpunch
    mc "*Slurp* *Slurp* *Slurp...!*"
    ver "D-don't stop, errand boy! I'm about to cum...! Keep wagging that tongue...!"
    mc "*Slurp* *Slurp* *Slurp...!* " with vpunch
    mc "*{b}Slurp* *Slurp* *Slurp...!{/b}*" with vpunch
    ver "Oh, ah-! It's going to be a big one...!" with vpunch
    mct "(Yes...! She's about there! I'm close!)"
    scene w1_3025 with flash
    ver "OoooOOOooooooOOOOooooOOOOooOh---!♥♥♥ Fuuuuuuuuuuuck!♥♥♥♥"
    mct "(--oh, shit!)"
    scene w1_3028 with dissolve
    mc "Gghhh--!"with flash
    "Even if it weren't for the banshee like scream or copious squirt spattering my face, I would've known she reached her climax thanks to one thing..."
    stop music fadeout 3.0
    "Veronica's thighs clamped down {b}hard{/b} on my neck as she orgasmed, sending a shock of panic through my system thanks to the nauseating *crunch* it produced."
    play sound "sound effects/thud-floor.mp3"
    scene w1_3026 with vpunch
    ver "*{b}THUD!{/b}*"
    "Just as a real mortal fear began to dawn on me, it just as quickly vanished as Veronica loss control of her legs and began to tumble to the floor."
    scene w1_3027 with dissolve
    "Her large frame made quite the noise as it crashed to the stage floor."
    ver "Gh....!♥ A-ah- ehehe... wh-what derh...♥"
    "Not to mention the incoherent babbling the foul-mouth woman was doing."
    mct "(I know I fantasized about this, but I didn't actually think she'd collapse...)"
    "The life had gone out Veronica's limbs and she was folded over like a discarded shirt."
    ver "Eheh...eheh...!"
    "Her breathing came out as a rattle and her eyes were alarmingly unfocused."
    scene w1_3029 with dissolve
    show screen textbox2 with dissolve
    kat "Hmppfh... that was excellent, [mcl]. What a sloppy bitch."
    kat "You still have 3 minutes, by the way. The game isn't over."
    scene w1_3030 with dissolve
    mct "(Right. I haven't ejaculated and time hasn't run out...)"
    "Seeing her reduced to THAT, thanks to my own efforts, filled me with a perverted sense of pride and and some urges of my own."
    "There's still time, if I want to have some fun..."
    hide screen textbox2 with dissolve
    stop music fadeout 3.0

    menu w1ExIntuitionVeroEnding:

        "{color=#FF1493}\[Asshole]{/color} Relieve your bladder on Veronica's crumpled body. [gr]\[Kathleen +2\] \[Warren +2\] \[Sam +1\] [red]\[Veronica -4\] \[Rosalind -1\] \[Hana -2\]" if toughness >= 21:
            $ Kathleen_Affection += 2
            $ Warren_Friendship += 2
            $ Sam_Friendship +=1
            $ Veronica_Affection -= 4
            $ Rosalind_Affection -= 1
            $ Hana_Affection -= 2
            $ w1ExVeroPissedOn = True

            scene w1_3031 with dissolve
            play music "music/leaving-home.mp3"
            show screen textbox2 with dissolve
            "It suddenly occurred to me, I hadn't used the rest room all night and the girls have been pumping me full of drinks..."
            "Maybe it's this place having an effect on me, but pissing on the haughty woman seemed enticing all of a sudden."
            "It certainly fit the scene. She was keeled over like discarded trash, coated in sweat and disheveled."
            mct "(Ah, what the hell. When in Rome...)"
            mct "(These old fucks should get a kick out of this.)"
            scene w1_3032 with fade
            "Using my foot, I nudged the toppled amazon to see if she was alright."
            ver "H-huh...?"
            "She still hadn't quite come to her senses yet. Which for my brazen purposes..."
            mct "(Good!)"
            scene w1_3033 with dissolve
            "With my painfully erect shaft in hand, I angled it at the bedraggled woman's crumpled form."
            scene w1_3034 with dissolve
            play ambient "sound effects/urine-ground.wav"
            mc "Take it, bitch!"
            "An unsteady stream of urine flowed from my urethra, tricking down onto the prone woman's chest."
            scene w1_3035 with dissolve
            ver "Eh...?"
            "The sounds Veronica made told me she was just about to come to her senses and realize what was going on."
            kat "Bahahahaha! Ah, perfect! What a perfect ending!"
            "Watching my piss spatter across the headstrong woman's chest was a perverse thrill unlike any other."
            scene w1_3036 with dissolve
            ver "Geeuh?!!! What dhugh-- fuck!"
            "Here was a woman who treated her body like a temple and now I was using that same body as a toilet."
            mc "Don't be mad. You got me all wet just now, I'm just returning the favor."
            ver "M-mother fucker!"
            scene w1_3037 with dissolve
            stop ambient fadeout 3.0
            "The crowd behind me let out a series of laughter, seemingly amused with this ending."
            scene black with fade
            "My stream slowing down to a trickle, I gave it a last couple of shakes before deciding I was finished."
            scene w1_3038 with w20
            "Veronica had no words. From her position, all she could levy at me was a look of anger and humiliation."
            "A look that made my cock ache even more."
            "Part of me felt bad for being so impulsive, but for the most part... I felt free."


        "{color=#FF1493}\[Kind/Mischievous]{/color} Make sure Veronica is okay. [gr]\[Veronica +2\] \[Rosalind +1\] \[Hana +1\] [red]\[Kathleen -1\]" if toughness <= 19:
            $ Veronica_Affection += 2
            $ Rosalind_Affection += 1
            $ Hana_Affection += 1
            $ Kathleen_Affection -= 1

            scene w1_3039 with dissolve
            play music "music/night-on-the-docks-sax.mp3"
            show screen textbox2 with dissolve
            "No. I shouldn't take advantage of my position. I want to be their friend, don't I?"
            scene w1_3040 with fade
            mc "Hey..."
            mc "That looked pretty intense. Are you okay?"
            scene w1_3041 with dissolve
            ver "Euh-- eh, w-what?"
            ver "Shit, I'm on the floor?"
            mc "Yeah. You about popped my head like a melon too."
            scene w1_3042 with dissolve
            ver "S-sorry about that, I didn't expect it to hit me that hard..."
            mc "You're under a lot of stress, I get it. It's a like a pressure cooker."
            scene w1_3043 with dissolve
            ver "I don't think that's how the human body works, doc..."
            mc "Alright, then I guess the only other explanation is your legs turned to jelly all thanks to my sexual prowess."
            scene w1_3044 with dissolve
            ver "Pfft-ha, oho. Don't make me laugh, [mcf]. I'm starting to get a headache."
            "Standing back up, I offered the toppled amazon my hand."
            mc "Let me help you get to your feet."
            scene black with fade
            ver "...yeah, okay."
            scene w1_3045 with fade
            ver "Thanks... I guess."
            scene w1_3046 with dissolve
            hide screen textbox2 with dissolve

            default dynamicChoice4 = ""
            if Veronica_Affection >= 10:
                $ dynamicChoice4 = "[gr]\[Veronica +1\]"
            else:
                $ dynamicChoice4 = "[red]\[Veronica -1\]"

            menu:
                "Acknowledge her by slapping her ass. [dynamicChoice4]":
                    scene w1_3047 with dissolve
                    scene w1_3048 with instantdissolve
                    play sound "sound effects/slap2.wav"
                    scene w1_3049 with instantdissolve
                    show screen textbox2 with dissolve
                    "*{b}Smack{/b}!*"
                    scene w1_3050 with dissolve
                    mc "You're welcome."
                    if Veronica_Affection >= 10:
                        $ Veronica_Horniness += 1
                        scene w1_3051 with dissolve
                        ver "Cocky little cuss..."
                        "Despite her words, Veronica gave me a sly smile."

                    else:
                        $ Veronica_Affection -= 1
                        scene w1_3052 with dissolve
                        ver "Egh. Don't get cocky, errand boy."

                "Tell her no problem.":
                    scene w1_3053 with dissolve
                    show screen textbox2 with dissolve
                    mc "Yeah, no problem."


        "Ejaculate on the prone woman's face. [gr]\[Veronica +1\]":
            $ Veronica_Horniness += 1
            $ w1ExGame1Ejaculation = True
            play music "music/sneaky-snitch.mp3"
            show screen textbox2 with dissolve
            mct "(Well, I'm all worked up.... might as well take care of that, right?)"
            scene w1_3054 with dissolve
            "Taking my shaft in hand, I began to quickly stroke my aching cock."
            play ambient "sound effects/fap.wav"
            "I kept the thought of the dirty old men behind me out of mind and instead focused on Veronica's naked, disheveled body."
            "Seeing a perfectly honed, hard-earned body toppled from sexual exhaustion was a genuine thrill."
            scene w1_3055 with fade
            if toughness >= 20:
                mc "Ah...! You bitch...! You beautiful, dirty bitch!"
            else:
                mc "Ah...! You're so fucking beautiful...!"
            ver "Eeehmg... Wha...?"

            "It didn't take long for the urge to ejaculate to build in me."

            if toughness >= 20:
                mc "I'm about to blow my load. Get ready, whore!"
            else:
                mc "I'm about to cum. Get Ready!"
            "Positioning myself by the amazon's head, I aimed my cock and let loose."
            stop ambient
            play sound "sound effects/spurt.wav"
            scene w1_3056 with flash
            play sound "sound effects/spurt.wav"
            mc "Take it! All over your face!" with flash
            ver "Geh...?!"
            scene w1_3057 with dissolve
            ver "T-this smell... it's..."
            mc "Damn. That was... ah, that was intense."
            ver "Did you just...?"
            "I let out a contented sigh, before wiping the remaining cum on Veronica's chest."
            "I felt utterly exhausted from this ordeal."

        "Just let the time run out. [gr]\[Veronica +1\]":
            $ Veronica_Affection += 1
            scene w1_3074 with dissolve
            mc "Already exhausted from this ordeal, I pushed aside my sexual urge and decided to take a seat on the couch."
            scene w1_3058 with dissolve
            "Instead, I decided to relax and take in Veronica's naked form as she regained her composure."
            "Seeing a perfectly honed, hard-earned body toppled from sexual exhaustion was a genuine thrill."
            scene w1_3059 with dissolve
            "By the time Veronica got the strength back in her legs and got to her feet, time was close to being up."
            ver "I didn't expect... that was... wow..."

        "{color=#696969}\[Asshole] Relieve your bladder on Veronica's crumpled body." if toughness <= 20:
            jump w1ExIntuitionVeroEnding

        "{color=#696969}\[Kind/Mischievous] Make sure Veronica is okay." if toughness >= 20:
            jump w1ExIntuitionVeroEnding


    scene black with fade
    stop music fadeout 3.0
    "......"
    $ renpy.end_replay()
    if not persistent.veroExhibition1Game1:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.veroExhibition1Game1 = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)
    "..."

    scene w1_3060 with circlewipe
    play music "music/cold-sober.mp3"
    "After game one had wrapped up, I was thankfully free to skitter out from the spotlight while the judges conferred."
    "Picking a winner based off of some vague description I gave seemed farcical, but I suppose that's ultimately what the whole month was."
    "Meanwhile, the Carnations stood center stage, talking amongst themselves."
    scene w1_3061 with dissolve
    "The crowd in front them engaged in some light conversation and debauchery."
    scene w1_3062 with dissolve
    kil "That looked like fun. Hell of the way to start the night, eh?"

    if w1ExVeroPissedOn == True:
        kil "I can't believe you actually pissed on that tall bitch."
        kil "You're a lot freakier than you let on."

    scene w1_3063 with dissolve
    mc "It was like an oven up there."
    scene w1_3062 with dissolve
    kil "Yeah, that was one of the first things I noticed too."
    kil "Kat says the heat makes people more agreeable, but I have a theory she just wants to make everyone who steps up there miserable."
    scene w1_3063 with dissolve
    mc "Both of those can be true."
    scene w1_3064 with dissolve
    kil "Still, other than that, you had a good time right?"

    if toughness >= 20:
        scene w1_3065 with dissolve
        mc "It was... exhilarating, actually."
    else:
        scene w1_3063 with dissolve
        mc "I enjoyed... some aspects of it."

    scene w1_3062 with dissolve
    kil "Yeah, of course you did. Where else in your life are you going back-to-back with three women?"
    scene w1_3066 with wipeleft
    hana "That would be pretty sweet if the women were actually into you, dumbass."
    scene w1_3067 with dissolve
    hana "Three women doing it only because they're desperately trying to win a prize isn't anything to be proud of."
    scene w1_3068 with dissolve
    kil "Hana! I thought you despised coming down here."
    kil "You spent all of last summer tethered to the bar. Don't tell me you're getting curious about the fun?"
    scene w1_3069 with dissolve
    hana "I got bored, so I thought I'd poke my head in. See how [mcf] was doing."
    scene w1_3070 with dissolve
    kil "Oh? Guess you two hit it off when I wasn't looking."

    if hanaFlag == True:
        scene w1_3071 with dissolve
        yh "It ain't like that."
    else:
        scene w1_3072 with dissolve
        hana "It ain't like that."

    scene w1_3073 with dissolve
    kil "That's too bad. [mcf] could probably help you stop being a bitch."
    scene w1_3075 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Tell Killian to stop being a dick. [gr]\[Hana +1\] [red]\[Killian -1\]":
            $ Hana_Affection += 1
            $ Killian_Bromance -= 1
            scene w1_3076 with dissolve
            show screen textbox2 with dissolve
            mc "Stop being a fuckin asshole, Ian."
            scene w1_3077 with dissolve
            kil "Me? An asshole...?"
            kil "Yeah, that shoe fits. Still you're being awfully fucking sensitive for some reason. It \"ain't like that\", huh?"
            scene w1_3078 with dissolve
            hana "No, you just talk so much shit that we can smell it on your breath."
            scene w1_3079 with dissolve
            kil "Yeesh. Fine, sorry. Here I thought this was just what the two of us considered flirting."
            scene w1_3080 with dissolve
            hana "*sigh* Don't make me gag."

        "Don't get in between the two.":
            scene w1_3080 with dissolve
            show screen textbox2 with dissolve
            hana "Your ass must be jealous of how much shit comes out of your mouth."
            scene w1_3081 with dissolve
            kil "It's better than being in an angry mood all the time."
            scene w1_3082 with dissolve
            hana "Must be pretty easy to be happy when you have a trust fund. You and your psychopathic uncle can get--"
            scene w1_3081 with dissolve
            kil "You think I don't have any problems?"
            scene w1_3082 with dissolve
            hana "I'm sure you have {b}PLENTY{/b}. Like... \"Should I get her drunk or just break out the Rohypnol tonight?\" Decisions, decisions."
            scene w1_3081 with dissolve
            kil "Fuck you! I'm not a rapist!"
            scene w1_3082 with dissolve
            hana "Yeah, maybe. It's probably just the money that allows ANYONE to tolerate you enough to pretend to be your friend."

    stop music fadeout 3.0
    kat "We've arrived at a decision, gentlemen."
    scene w1_3083 with dissolve

    if kat_polite == True:
        "Thankfully, Mrs. Pulman's announcement interrupted Hana and Ian's little spat."
    else:
        "Thankfully, Kathleen's announcement interrupted Hana and Ian's little spat."

    scene w1_3084 with dissolve
    play music "music/epic-battle-speech.mp3"
    kat "Based off the criteria that Mr. [mcl] set in advance... the winner of our first game of the night, and the Carnation who will have the benefit of bypassing the second game is..."

    if w1ExDeferential == True and w1ExWorship == True:
        $ w1ExIntuitionGameWinnerFel = True
        scene w1_3087 with dissolve
        kat "Mrs. Felicia Ford, our would be sister-in-arms! She certainly knows how to worship a cock, doesn't she?"

    if w1ExDeferential == True and w1ExNasty == True:
        $ w1ExIntuitionGameWinnerFel = True
        scene w1_3087 with dissolve
        kat "Mrs. Felicia Ford, our would be sister-in-arms! Who put on the most lewd and nasty showing of the night."

    if w1ExDeferential == True and w1ExTender == True:
        $ w1ExIntuitionGameWinnerRose = True
        scene w1_3085 with dissolve
        kat "Mrs. Rosalind Carter, who put on quite the tender and loving show for this stage!"

    if w1ExDeferential == True and w1ExTease == True:
        $ w1ExIntuitionGameWinnerFel = True
        scene w1_3087 with dissolve
        kat "Mrs. Felicia Ford, our would be sister-in-arms! She certainly knows how to treat a cock, doesn't she?"

    if w1ExInControl == True and w1ExWorship == True:
        $ w1ExIntuitionGameWinnerFel = True
        scene w1_3087 with dissolve
        kat "Mrs. Felicia Ford, our would be sister-in-arms!  Who knew how to both guide a man around {b}and{/b} worship a cock."

    if w1ExInControl == True and w1ExNasty == True:
        $ w1ExIntuitionGameWinnerFel = True
        scene w1_3087 with dissolve
        kat "Mrs. Felicia Ford, our would be sister-in-arms! Who put on the most lewd and nasty showing of the night."

    if w1ExInControl == True  and w1ExTender == True:
        $ w1ExIntuitionGameWinnerVero = True
        scene w1_3086 with dissolve
        kat "Miss Veronica Lynch, who thought outside the box and forcefully took care of the client's nonsexual needs."

    if w1ExInControl == True and w1ExTease == True:
        $ w1ExIntuitionGameWinnerVero = True
        scene w1_3086 with dissolve
        kat "Miss Veronica Lynch, who thought outside the box and forcefully took care of the client's nonsexual needs."

    if w1ExAttentive == True and w1ExWorship == True:
        $ w1ExIntuitionGameWinnerRose = True
        scene w1_3085 with dissolve
        kat "Mrs. Rosalind Carter, who put on quite the tender and loving show for this stage!"

    if w1ExAttentive == True and w1ExNasty == True:
        $ w1ExIntuitionGameWinnerVero = True
        scene w1_3086 with dissolve
        kat "Miss Veronica Lynch, who thought outside the box and forcefully took care of the client's nonsexual needs."

    if w1ExAttentive == True and w1ExTender == True:
        $ w1ExIntuitionGameWinnerRose = True
        scene w1_3085 with dissolve
        kat "Mrs. Rosalind Carter, who put on quite the tender and loving show for this stage!"

    if w1ExAttentive == True and w1ExTease == True:
        $ w1ExIntuitionGameWinnerVero = True
        scene w1_3086 with dissolve
        kat "Miss Veronica Lynch, who thought outside the box and forcefully took care of the client's nonsexual needs."


    if w1ExIntuitionGameWinnerRose == True:
        scene w1_3088 with dissolve
        $ history_rosalind = "To her surprise, with her incongruously loving performance, Rosalind took the first game of the first exhibition. Leaving Veronica and Felicia to move onto the second game."
        $ unread_rosalind = True
        play sound "sound effects/notification.wav"
        show bioupdate with dissolve
        rose "...me?"
        scene w1_3089 with dissolve
        play sound "sound effects/applause-small.wav"
        "A look of surprise fell over the hard luck mother as a round of applause erupted from the crowd."
        tom "There, there!"
        frank "I told you she'd come out on top."

        if w1RoseGonzo == True:
            jim "Looks like my hunch was right!"

        scene w1_3088 with dissolve
        rose "Uh..."
        scene w1_3089 with dissolve
        kat "Don't look so dumbfounded, dear. You managed to deliver what Mr. [mcl] asked for, even if it was just a fluke."
        scene w1_3088 with dissolve
        rose "That means... I'm done for the night?"
        scene w1_3090 with dissolve
        kat "That it does. It's bitter sweet for your fans, of course, but you've earned that privilege. Lucky you."
        kat "The next two games are going to be {b}drastically{/b} more punishing."
        scene w1_3091 with dissolve
        ver "Damn it!"
        scene w1_3092 with dissolve
        kat "Now, now. Don't be a sore loser, Miss Lynch. It makes you look uglier than you already do."
        scene w1_3093 with dissolve
        fel "Hehe, congrats! I didn't expect that!"
        "Her opponents had fittingly polar opposite reactions to the news."
        scene w1_3094 with dissolve
        mc "Guess Felicia's happy. Her fun gets to continue."
        scene w1_3095 with dissolve
        hana "Is she the Carnation that {i}wanted{/i} to join? What a weirdo."
        scene w1_3096 with dissolve
        kil "Good. I was hoping to see that redhead in action some more."
        scene w1_3097 with dissolve
        hana "Is that your type? The kind of woman who could beat you up?"
        scene w1_3098 with dissolve
        mc "Ha, you should see his girlfriend. She's pretty much the opposite of Veronica. All girly and sweet."
        scene w1_3099 with dissolve
        kil "Don't try and put a label on me. I love all kinds of women."
        scene w1_3100 with dissolve
        mc"You {i}lust{/i} after all kinds of women you mean."
        scene w1_3101 with dissolve
        kil "What's the difference?"
        hana "Wh--"



    if w1ExIntuitionGameWinnerFel == True:

        scene w1_3102 with dissolve
        $ history_felicia = "Shining like a star with her lewd performance, Felicia took the first game of the first exhibition. Leaving Rosalind and Veronica to move onto the second game."
        $ unread_felicia = True
        play sound "sound effects/notification.wav"
        show bioupdate with dissolve
        fel "Ha!"
        play sound "sound effects/applause-small.wav"
        "Felicia triumphantly cheered in a fittingly exaggerated fashion as a round of applause erupted from the crowd."
        eric "Ha! Excellent!"
        mihir "An impressive showing."

        if w1FelGonzo == True:
            jim "Looks like my hunch was right!"

        scene w1_3091 with dissolve
        ver "Damn it!"
        scene w1_3092 with dissolve
        kat "Now, now. Don't be a sore loser, Miss Lynch. It makes you look uglier than you already do."
        scene w1_3104 with dissolve
        rose "..."
        scene w1_3105 with dissolve
        kat "--and you don't look so downtrodden. This is just the first of many chances you'll have to win."
        scene w1_3106 with dissolve
        fel "I guess that means I'm sitting the rest of the night out?"
        scene w1_3090 with dissolve
        kat "That it does. You've earned that privilege. Lucky you."
        kat "The next two games are going to be {b}drastically{/b} more punishing."
        scene w1_3094 with dissolve
        mc "Too bad for Felicia I guess. It means tonight's fun is over for her."
        scene w1_3095 with dissolve
        hana "Is she the Carnation that {i}wanted{/i} to join? What a weirdo."
        scene w1_3096 with dissolve
        kil "Sucks for her, but I was hoping to see that redhead in action some more."
        scene w1_3097 with dissolve
        hana "Is that your type? The kind of woman who could beat you up?"
        scene w1_3098 with dissolve
        mc "Ha, you should see his girlfriend. She's pretty much the opposite of Veronica. All girly and sweet."
        scene w1_3099 with dissolve
        kil "Don't try and put a label on me. I love all kinds of women."
        scene w1_3100 with dissolve
        mc"You {i}lust{/i} after all kinds of women you mean."
        scene w1_3101 with dissolve
        kil "What's the difference?"
        hana "Wh--"


    if w1ExIntuitionGameWinnerVero == True:

        scene w1_3107 with dissolve
        play sound "sound effects/applause-small.wav"
        "Instead of looking pleased, Veronica simply shrugged. As if it was to be expected."
        $ history_veronica = "Veronica's equal display of tender care and domineering spirit secured her the first game of the frist exhibition, leaving Rosalind and Felicia to move onto the next one."
        $ unread_veronica = True
        play sound "sound effects/notification.wav"
        show bioupdate with dissolve
        sam "There wasn't ever any fucking doubt!"
        jiji "She's a remarkable specimen."

        if w1VeroGonzo == True:
            jim "Looks like my hunch was right!"

        scene w1_3108 with dissolve
        fel "Congratulations, Red. You really know how to take charge."
        fel "You look cute when you cum, by the way."
        scene w1_3109 with dissolve
        ver "Shut up, blondie."
        scene w1_3103 with dissolve
        kat "Now, now. Learn how to take a compliment, Miss Lynch."
        scene w1_3104 with dissolve
        rose "..."
        scene w1_3105 with dissolve
        kat "--and you don't look so downtrodden. This is just the first of many chances you'll have to win."
        scene w1_3110 with dissolve
        ver "I'm done for the night?"
        scene w1_3090 with dissolve
        kat "Indeed. You still need to be here, but you've earned the privilege of watching the next two games. Lucky you."
        kat "The next two games are going to be {b}drastically{/b} more punishing."
        scene w1_3094 with dissolve
        mc "Guess Felicia's happy. Her fun gets to continue."
        scene w1_3095 with dissolve
        hana "She's the one that {i}wanted{/i} to join? What a weirdo."
        scene w1_3111 with dissolve
        kil "Damn. I was hoping to see the redhead in action some more tonight."
        scene w1_3097 with dissolve
        hana "Is that your type? The kind of woman who could beat you up?"
        scene w1_3098 with dissolve
        mc "Ha, you should see his girlfriend. She's pretty much the opposite of Veronica. All girly and sweet."
        scene w1_3099 with dissolve
        kil "Don't try and put a label on me. I love all kinds of women."
        scene w1_3100 with dissolve
        mc"You {i}lust{/i} after all kinds of women you mean."
        scene w1_3101 with dissolve
        kil "What's the difference?"
        hana "Wh--"

    stop music fadeout 3.0
    scene w1_3112 with dissolve
    kat "With that, we'll move onto the second game of the night. Ian, a hand?"
    scene w1_3113 with wipeleft
    kil "Hold that thought and then promptly toss it in the trash, Hana."
    scene black with fade
    "..."
    scene w1_3114 with dissolve
    play music "music/covert-affair.mp3"
    mc "You two get along like oil and water."
    scene w1_3115 with dissolve
    hana "No shit."
    scene w1_3116 with dissolve
    mc "It's entertaining."
    scene w1_3115 with dissolve
    hana "No, it isn't. I hate spoiled rich boys."
    scene w1_3117 with dissolve
    mc "Eh, it kinda is."
    scene w1_3115 with dissolve
    hana "No, it isn't."
    scene w1_3114 with dissolve
    mc "So you wanted to check up on me?"

    if hanaFlag == True:
        scene w1_3118 with dissolve
        hana "Yeah, it's your first night. Bet you've never screwed in front of a crowd before."
        scene w1_3119 with dissolve
        mc "...did you see all that?"
        scene w1_3120 with dissolve
        hana "No, I just caught the end with that buff chick."
        if w1ExVeroPissedOn == True:
            hana "Can't believe you just peed on her like that."
        scene w1_3121 with dissolve
        mc "Eh... that's..."
        scene w1_3122 with dissolve
        hana "Oh, don't be embarrassed, dork. I was impressed."
        scene w1_3123 with dissolve
        mc "Impressed about what?"
        scene w1_3124 with dissolve
        hana "Your giving, charitable demeanor."
        scene w1_3125 with dissolve
        mc "Ha! Screw you!"


    else:
        scene w1_3118 with dissolve
        hana "Yeah, see how much a dork like you was in over his head. First time screwing in front of a crowd?"
        scene w1_3119 with dissolve
        mc "...did you see all that?"
        scene w1_3120 with dissolve
        hana "No, I just caught the end with that buff chick."
        if w1ExVeroPissedOn == True:
            hana "Can't believe you just peed on her like that."
        scene w1_3121 with dissolve
        mc "Eh... that's..."
        scene w1_3122 with dissolve
        hana "Embarrassing? Fuck yeah it was."

    scene w1_3126 with fade
    hana "Ah, but seriously though... don't feel too self-conscious about just lil' ol' me. Not like a dozen other people beside me didn't see your nuts to begin with."
    scene w1_3127 with dissolve
    mc "When you put it that way, it sounds mortifying."
    scene w1_3126 with dissolve
    hana "Not to sound like a broken record, but that's an apt description for this horror show."
    scene w1_3128 with dissolve
    hana "Look over there."
    scene w1_3129 with dissolve
    hana "That guy's Joe Shelby."
    mc "Like the car guy? From that movie?"
    hana "...huh? No. That's Carrol Shelby. {b}Joe{/b} is a state congressman and a moralistic, holier-than-thou shithead."
    scene w1_3130 with dissolve
    hana "Last year, Mr. Family values choked Harper until she passed out."
    scene w1_3131 with dissolve
    mc "What the fuck?"
    scene w1_3130 with dissolve
    hana "She refused to work for like a week. Keep an eye on that asshole, alright?"
    scene w1_3127 with dissolve
    mc "I'll try."
    scene w1_3126 with dissolve
    hana "Don't try. Do, please. Us peons should look out for each other."

    if hanaFlag == True:
        scene w1_3132 with dissolve
        hana "By the way, it's nice having someone my own age around."
        scene w1_3133 with dissolve
        "Hana placed a hand on my thigh and gave me an unfiltered smile that caught me off guard."
        scene w1_3135 with dissolve
        "I thought back to the other night, when I discovered our similar backgrounds."
        mc "This place must get pretty lonely."
        scene w1_3133 with dissolve
        scene w1_3134 with dissolve
        scene w1_3133 with dissolve
        "Rather than responding, she just nodded slightly."

    scene w1_3136 with dissolve
    hana "Looks like things are about to heat back up again."
    scene w1_3164 with dissolve
    hana "I should get back to the bar. This is about the time of night everyone starts to really knock 'em back."

    if hanaFlag == True:
        scene w1_3137 with dissolve
        hana "Nice chatting with you. Keep your head up, [mcf]."
        hana "See you later."
    else:
        scene w1_3138 with dissolve
        hana "Good talking with ya, new guy. See you around."


    mc "Later."
    scene w1_3139 with dissolve
    mct "(I wonder what that old woman will throw at them next...)?"
    stop music fadeout 3.0
    "......"
    scene black with fade
    "..."

    if w1ExIntuitionGameWinnerRose == True:
        jump w1ExFollowThroughVeroFelStart

    if w1ExIntuitionGameWinnerFel == True:
        jump w1ExFollowThroughVeroRoseStart

    if w1ExIntuitionGameWinnerVero == True:
        jump w1ExFollowThroughRoseFelStart



label w1ExFollowThroughVeroFelStart:

    scene w1_3140 with curtains
    kat "Gentlemen, we are to begin! Allow me to explain the next game."
    "About twenty or so minutes after Hana had scurried back to the bar, game two was kicking off. Veronica and Felicia had already taken their \"starting\" positions, ass to ass and down on their hands and knees at the center of the stage."
    scene w1_3141 with dissolve
    play music "music/myst-on-the-moor.mp3"

    if kat_polite == True:
        "A double-sided dildo rested between them, lewdly connecting the two women together at their honeypots. They were tasked with the uncomfortable prospect of awkwardly holding that position while Mrs. Pulman explained what was coming next."
    else:
        "A double-sided dildo rested between them, lewdly connecting the two women together at their honeypots. They were tasked with the uncomfortable prospect of awkwardly holding that position while Kathleen explained what was coming next."

    scene w1_3142 with dissolve
    kat "Our first game was about the first tenant of customer service. Exploring the needs of the customer."
    kat "Our second game will hone in on what I think of as the next: {b}actualization{/}. The art of the follow through."
    kat "In simplest terms, being able to keep focus on your task despite any roadblocks that might arise."
    scene w1_3143 with dissolve

    if kat_polite ==True:
        "Par for the course, Mrs. Pulman aggrandized what is otherwise just an excuse to perversely watch women squirm in discomfort."
    else:
        "Par for the course, Kathleen aggrandized what is otherwise just an excuse to perversely watch women squirm in discomfort."

    scene w1_3144 with dissolve
    kat "...and what will be the task? It's simple. You'll just need to shake your hips like the whores you are."
    kat "You two will fuck each other for all your worth. If you start slacking, the collars around your neck will generously provide you a pick me up"
    scene w1_3145 with dissolve
    ver "What do you mean by pick-me-up?"
    scene w1_3146 with dissolve
    kat "Simply put, it'll administer a brief shock that will jolt you back to your senses and get you moving again. If you don't get back to the task within 10 seconds, you'll be disqualified."
    scene w1_3147 with dissolve
    ver "What the fuck?"
    scene w1_3148 with dissolve
    fel "Eh...? A shock...?"
    scene w1_3149 with dissolve
    kat "Don't be alarmed. It's nothing dangerous for a healthy adult woman. It's more akin to a dog's training collar, but for stupid sluts like you."
    scene w1_3150 with dissolve
    fel "..."
    "Even Felicia was looking a little unsure about this one."
    scene w1_3151 with dissolve
    kat "If you find the prospect unappealing, one of you can always resign and move onto the last game by your lonesome."
    scene w1_3152 with dissolve
    fel "Hehe, no... I'm game."
    ver "Let's do this."
    scene w1_3153 with dissolve
    kat "Good. I thought so. That's not all there is to this game though. You'll also be asked some questions."
    scene w1_3154 with dissolve
    kat "Simple, basic things that any woman your age should be able to answer. A wrong or delayed answer will make things more difficult for you."
    scene w1_3155 with dissolve
    kat "Do you two understand the parameters of this game?"
    scene w1_3156 with dissolve
    fel "Yes, ma'am."
    ver "Aye..."
    scene w1_3157 with dissolve
    kat "Mr. [mcl]! Mr. Beaufort! You'll be charged with administering the shocks. You've familiarized yourself with the remote control I've given you?"
    scene w1_3158 with dissolve
    kil "Yup!"
    mc "I think so."
    scene w1_3157 with dissolve
    kat "It's very simple. There's three settings. Each corresponds to a low, medium, and high powered shock. I'll leave it to your discretion what you feel is appropriate."
    mct "(Is this part of the test she mentioned...?)"
    kat "Mr. [mcl]'s remote is synced with Miss Lynch's collar. Mr. Beaufort's is synced to Mrs. Ford's."

label w1ExFollowThroughVeroFel:

    if _in_replay:
        show screen textbox2 with dissolve

    scene w1_3159 with dissolve
    kat "Now, enough talking. Let's get to why all you gentlemen are really here. On the count of three, I want you to start fucking each other like your future depends on it."
    stop music fadeout 3.0
    scene w1_3160 with dissolve
    kat "Three..."
    scene w1_3161 with dissolve
    kat "Two..."
    scene w1_3162 with dissolve
    kat "One..."
    scene w1_3163 with vpunch
    kat "Begin, whores!"
    image verofeldil1= Movie(play="verofeldil1.webm")
    image verofeldil2= Movie(play="verofeldil2.webm")
    image verofeldil3= Movie(play="verofeldil3.webm")
    image verofeldil4= Movie(play="verofeldil4.webm")
    image verofeldil5= Movie(play="verofeldil5.webm")
    image verofeldil6= Movie(play="verofeldil6.webm")
    image verofeldil7= Movie(play="verofeldil7.webm")
    show verofeldil1 with dissolve
    play music "music/guiton-sketch.mp3"
    "Cutting through the air with an enthusiastic chop, she signaled for the two Carnations to begin the trial."
    "Neither woman hesitated to jump ass first into the task in front of them, the two of them drawing their bodies back until their haunches collided with a satisfying smack."
    "Both women then scrambled to push forward, sliding themselves off and revealing more and more of the golden toy that connected them."
    "It was like an awkward dance. On paper it might sound simple, but the reality was each woman was struggling to find the appropriate tempo that would make it easier for the both of them."
    "Veronica lurched forward at such a depth that the dildo almost slipped out from in between them, but Felicia was quick to pull back and keep it locked between them."
    kat "That's right, girls. Keep those hips moving and those asses shaking. It's one of the few things you're good for."
    "Eventually the two settled found a workable rhythm, moving in tandem like some perverted seesaw."
    "As one would expect, both Carnations bore an uncomfortable look on their face. Each concentrated on keeping their hips unceasingly moving and the sex-toy lodged in their quims."
    scene verofeldil3 with dissolve
    hide verofeldil1
    hide screen textbox2 with dissolve
    fel "How you doing back there, Red? You've got a rock-hard tush, you know that?"
    ver "D-don't distract me."
    fel "Isn't that the objective of this? For us to pat our head and rub our belly at the same time?"
    scene verofeldil4 with dissolve
    hide verofeldil3
    "Veronica merely grimaced, not dignifying the flippant woman with a response."
    "Instead, she squared her shoulders and bucked her hips, vigorously sleeving and unsheathing herself from the toy with a stronger intensity than before."
    "*Plap* *Smack* *Slap!*"
    "*Plap* *Smack* *Slap* *Smack!* *Plap!* *Slap!*"
    fel "Oooooh...!"
    "It was like she was declaring: \"I'm going to wear you down\". However..."
    ver "Ngg...!"
    "It was a double sided sword, almost quite literally. She wasn't immune to the pleasurable change of pace herself."
    scene w1_3165 with dissolve
    show screen textbox2 with dissolve
    kat "Such beautiful, bouncing asses... don't you agree, gentleman?"
    scene w1_3166 with dissolve
    "The crowd reacted with a mix of noise that could be taken as agreement."
    kat "However, let's make things more interesting."
    scene w1_3167 with dissolve
    kat "Hmmm-mmmh~hmmm~ Let's see...    "
    kat "You girls know your multiplication tables...?"

    if kat_polite:
        "Having gone over to one of the nearby tables, Mrs. Pulman carefully considered her options while posing an odd question."
    else:
        "Having gone over to one of the nearby tables, Kathleen carefully considered her options while posing an odd question."

    scene w1_3168 with dissolve
    "Both women must've took the question as rhetorical, as neither answered her."
    scene w1_3169 with dissolve
    kat "Let's get things rolling. We'll start with..."
    scene w1_3170 with dissolve
    kat "Miss Lynch."
    hide screen textbox2 with dissolve
    scene verofeldil2 with dissolve
    hide verofeldil4
    ver "Eeeeh...? W-what are you talking about?"
    kat "Answer quickly. What is nine times twelve?"
    ver "W-what--?"
    kat "Five, four, three, two..."
    ver "Uh... 108!"
    scene w1_3154 with dissolve
    show screen textbox2 with dissolve
    kat "Correct. Mrs. Ford: fourteen times six?"
    fel "Wait... eh... 72... 78... eighty- eighty four!"
    scene w1_3155 with dissolve
    kat "Correct. Veronica! Thirteen times nine?"
    ver "One--one hundred seventeen!"
    scene verofeldil1 with dissolve
    hide verofeldil2

    if kat_polite == True:
        "All the while the two pumped their hips, the Carnations went back and forth answering Mrs. Pulman's questions."
    else:
        "All the while the two pumped their hips, the Carnations went back and forth answering Kathleen's questions."

    fel "75!"
    ver "119!"
    fel "169!"
    ver "196!"
    fel "Eh, eh... duh duh... duh... two... 224...?"
    scene w1_3171 with dissolve
    hide screen textbox2 with dissolve
    kat "Oops, sorry! The answer was 238! Mrs. Ford takes the first hit."
    fel "What are you ta--"
    scene w1_3172 with dissolve
    fel "Ooooh! What the fuck?"

    if kat_polite == True:
        "Finding a window of opportunity while the pair was separating, Mrs. Pulman shoved a prickly golf ball sized sphere into Felicia's puckering asshole."
    else:
        "Finding a window of opportunity while the pair was separating, Mrs. Kathleen shoved a prickly golf ball sized sphere into Felicia's puckering asshole."
    scene w1_3173 with vpunch
    fel "G-gguh..!?"
    scene w1_3174 with dissolve
    "The reaction was immediate. As the pair's backsides smacked together once more, a look of dazed shock flooded the blonde woman's face."
    fel "Eh...?"
    scene w1_3173 with vpunch
    fel "Gg--ah~!!!"
    "Every time Felicia's ass was sent shaking from colliding with Veronica's stone stolid backside, she reeled from the pink toy sliding around her colon."
    scene w1_3174 with dissolve
    fel "Ahh... fuck! W-warn a girl-before you...!"
    ver "W-what did you just do? Why is blondie squealing?"
    kat "You mean besides her being a pig whore?"
    scene w1_3175 with dissolve
    play sound "sound effects/slap2.wav"
    scene w1_3176 with vpunch
    "*{b}Smack!!!{/b}*"
    fel "OOooooooOOoooOOOh!"
    kat "Miss Lynch. Sixteen times eighteen?"
    scene verofeldil2 with dissolve
    hide verofeldil1
    ver "Eh...?"
    kat "Five, four, three..."
    ver "Who the fuck knows their multiplication tables that high?!"
    kat "One... times up!"
    ver "Shit! What are you going to do?"
    "Understandably, having no idea what Felicia just had happened to her, Veronica's normally indomitable expression cracked, showing signs of fear and concern."
    scene w1_3177 with dissolve
    kat "Remember? A wrong or delayed answer will make things more difficult for you."
    scene w1_3178 with dissolve
    ver "Gh...? W-what did you just put in mee-"
    scene w1_3179 with vpunch
    ver "aAaaaAAAsssssssss!"
    scene w1_3180 with dissolve
    "Veronica reacted as Felicia had, with total and complete shock at the strange sensation."
    fel "Eh, Whhhhy does this feel sort of good?"
    scene w1_3179 with vpunch
    ver "Fuck no it doesn't!"
    kat "Miss Ford. Nineteen times sixty three..."
    scene w1_3181 with dissolve
    show screen textbox2 with dissolve
    fel "Is that a joke?!"
    scene w1_3182 with dissolve

    if kat_polite == True:
        "The girls did their best to answer Mrs. Pulman's questions, but one by one the balls began to disappear in equal measure."
    else:
        "The girls did their best to answer Kathleen's questions, but one by one the balls began to disappear in equal measure."

    scene w1_3183 with dissolve
    "Two for Veronica..."
    scene w1_3184 with dissolve
    "Three for Felicia... three for Veronica."
    scene w1_3185 with dissolve
    "By the time they'd all disappeared, the spike-lined balls had been equally split between the Carnations and were now freely rattling around the girl's buttholes."
    play sound "sound effects/slap2.wav"
    pause 0.5
    play sound "sound effects/slap2.wav"
    pause 0.5
    play sound "sound effects/slap2.wav"
    "*{b}Smack{/b}* *{b}Smack{/b}!* *{b}Smack{/b}-!!*"
    scene w1_3186 with dissolve
    ver "Mmmmmnnaaaa!"
    fel "Geh-! S-stop hitting me! It feels weeeeeeeeird!"
    "At this point, both women were howling in confuddled mix of pain and pleasure."

    if kat_polite == True:
        "Each swat of the paddle in Mrs. Pulman's grip sent each of their wide asses quaking, knocking the ribbed pink toys against each other and scraping the lining of their bowels."
    else:
        "Each swat of the paddle in Kathleen's grip sent each of their wide asses quaking, knocking the ribbed pink toys against each other and scraping the lining of their bowels."

    "The pervert in me had to hand it to her. It was a simple approach, but the results were etched into the pair's enraptured faces."
    fel "Onnn- oh, gghuu!"
    scene w1_3190 with dissolve
    kat "Remember the aim of the game: soldier through the sensation. Keep fucking each other until you drop."
    scene w1_3188 with dissolve
    ver "Yeh-y-you don't need to remind me of that!"
    scene w1_3187 with dissolve
    kat "That was directed at the other slut. She's clearly enjoying herself."
    scene w1_3188 with dissolve
    "She was right. Felicia was going cross-eyed."
    scene w1_3190 with dissolve
    kat "Not your first time being double stuffed?"
    scene w1_3189 with dissolve
    fel "Eeeh, ye-no, n-no it is! I mean, only with toys...!"
    scene w1_3190 with dissolve
    kat "Really? I figured a woman like you would be more experienced in that area."
    scene w1_3191 with quickdissolve
    scene w1_3192 with quickdissolve
    play sound "sound effects/slap2.wav"
    scene w1_3193 with vpunch
    "*{b}Slap!{/b}*"
    fel "Ooowowooooo~ehg, they're moving around in my buuuutt!"
    scene w1_3192 with dissolve
    scene w1_3191 with dissolve
    fel "G-guh...! My asshole is on fire... Itz... tt-to..."
    kat "I should remember that you have an extra-sensitive anus. That will come in handy later."
    scene w1_3191 with quickdissolve
    scene w1_3192 with quickdissolve
    play sound "sound effects/slap2.wav"
    scene w1_3193 with vpunch
    "*{b}Slap!{/b}*"
    fel "Geh-hggg! Shwhnit...!"
    "Every blow wrenched a yelp of pleasure from the volunteer whore's vocal cords."
    scene w1_3192 with dissolve
    scene w1_3191 with dissolve
    fel "F-fu- n-no fair!"
    scene w1_3191 with quickdissolve
    scene w1_3192 with quickdissolve
    play sound "sound effects/slap2.wav"
    scene w1_3193 with vpunch
    "*{b}Smack!{/b}*"
    fel "EeeaaaAAaaaaHgh! Ohhwwho...!"
    "Every blow made Felicia look more and more hopless, more wretched, and more on edge."
    scene w1_3192 with dissolve
    scene w1_3191 with dissolve
    kat "There it is! I was waiting to see your face twisted up like a perverted bitch! You're taking this place much too lightly."
    fel "Gg-gh... itz- t-too m-much...!"
    kat "I'm going to teach you many wonderful things thing this month, dear! Now cum!"
    scene w1_3191 with quickdissolve
    scene w1_3192 with quickdissolve
    play sound "sound effects/slap2.wav"
    scene w1_3193 with vpunch
    "*{b}Slap!{/b}*"
    scene w1_3194 with dissolve
    fel "Eeeeeeeeeeeooooowwwwh!"
    "With a violent cry, Felicia arched her back and tightly shut her eyes in abject ecstasy."
    fel "OooOooooOooh~oooh...ehehe...♥"
    scene w1_3190 with dissolve
    kat "Did you cum from your pussy or your ass? Both maybe?"
    kat "Ha! You might just be this summer's anal queen."
    scene w1_3189 with dissolve
    "Felicia stumbled forward slightly and her orgasm dulled her previous energy, but she amazingly kept to task, never not working in tandem with Veronica's bucking hips."
    scene w1_3187 with dissolve
    kat "What about you, Miss Lynch? How are you holding up?"
    scene w1_3195 with dissolve
    ver "F-feh! I could do this all night!"
    kat "Is that so? Then let's get back on track then."
    scene w1_3196 with dissolve
    mc "They're unbelievable..."
    scene w1_3197 with dissolve
    kil "Shit, this is good..."
    scene w1_3198 with dissolve
    kat "This time you have 30 seconds to answer."
    ver "We're not done with that?"
    kat "No. Not until one of you yields."
    scene w1_3199 with dissolve
    kat "I have a riddle for you, are you listening?"
    hide screen textbox2 with dissolve
    scene verofeldil2 with dissolve
    hide verofeldil1
    ver "Ggeeeh, t-this is... yes! I'm listening!"
    kat "Good! Here it is: \"Without it, I'm dead. If I'm not, then I'm behind. What am I?\"."
    ver "Uuuuh, ah, fuck! I was never good at these! Uh... Without it I'm..."
    ver "...then I'm behind...? Uh..."
    kat "Ten seconds."
    ver "MMh... Uh..."
    kat "Five seconds. Four, three, two..."
    ver "Oxygen?!"
    kat "Sorry, that is an incorrect answer. The one I'm looking for is \"ahead\"."
    ver "Dah-damn it!"
    scene verofeldil3 with dissolve
    hide verofeldil2
    kat "Your turn, Mrs. Ford. What has a head and a tail, but no body?"
    fel "Head... tail.... oh!"
    fel "A coin?"
    kat "Correct. Very good! That was surprisingly quick."
    kat "Now..."
    scene w1_3200 with hpunch
    play sound "sound effects/vib-start.wav"
    "*Bzzzzt!*"
    "Just like with the balls, the cruel woman slipped the newly fetched toy - an anal vibrator - smoothly into the amazon's tightening pucker and turned it on."
    scene verofeldil5 with dissolve
    hide verofeldil3
    ver "Mmmmn~eeh, ah... fhug...!!!"
    ver "Gho-o-hohh-! Ehhh...! Oooowwh..!"
    "The vibrating rod being shoved mercilessly into her crowded tail hole produced a garbled slew of intelligibly whorish moans."
    ver "Fhooowwwuuuck!"
    kat "Haha, how do you like that?"
    ver "Tk-! The vib---gh, the vibrations-!"
    kat "I know, right? In such a tight space, it's making the studded eggs vibrate along with it. You can feel those vibrations all the way into your stomach and into your chest."
    ver "Ghh...! Y-ngh-mmg-oh, yh-yes!"
    kat "I'm very glad you were the one who got my riddle wrong. Unlike Felicia, you need that extra push to make you admit a basic truth."
    kat "What truth is that, you're unable to ask right now... but I'll tell you anyway. The truth is, there is a part of you that enjoys this."
    ver "Ehegh, n-no!"
    kat "Don't lie. I know all about you, Miss Lynch. You career as a sportswoman, your work as a fitness model. The fitness competitions... you like being looked at. You like the limelight."
    kat "Just like Mrs. Ford enjoys it. Really, you're two peas from the same whorish pod."

    if kat_polite == True:
        "Mrs. Pulman must've been delighted to have Veronica under her control, with no choice but to listen to her bullshit observations."
    else:
        "Kathleen must've been delighted to have Veronica under her control, with no choice but to listen to her bullshit observations."

    ver "Egug...! F-fhuck...! Ehuu...!!"
    ver "Datsnohttrueeeee....!"
    "Even with the additional discomfort, Veronica continued to match Felicia's pace, moving her hips at a furious pace and drilling herself on the golden dildo."
    "The sight made me think Mrs. Pulman might've not been too off base when it came to Veronica. From where I sat, it looked like the woman at least had something of an exhibitionist streak."
    "She was at least feeling it. It wasn't just the goal of winning the competition that was driving her hips, it was also needy, craven desire."
    scene verofeldil6 with dissolve
    hide verofeldil5
    fel "Gh... oh~♥ It doesnt'stooohp!!"
    "Her opponent was looking much of the same. Felicia's beautiful face had contorted in a mess of pleasure, drool pooling at the corners of her mouth and dripping down her chin."
    "Her last orgasm hadn't dulled her sensitivity in the least."
    scene verofeldil7 with dissolve
    hide verofeldil6
    show screen textbox2 with dissolve
    "Incredibly the scene carried on for minutes more. Felicia was rocked by numerous mini-orgasms in the mean time, but she still managed to hang on."
    "It was an marvelous sight. The two women sweating profusely, squirming in ecstasy, loose strands of hair matting the napes of the neck."
    "The room was completely silent."
    "Even our cruel ringleader shut the fuck up for once, instead letting the show be carried by the dirty sounds of copulation and ragged breathing."
    "In this moment, I felt utterly divorced from my regular life. [mcf] was just a name at the back of my head and his worries seemed so trite."
    fel "Oh... no...!"
    ver "Eh... eh..!"
    scene w1_3201 with flash
    ver "Ooofffhhooooo-! Ghhhg... fhuu... ghw..."
    "I watched the large woman's expression go cross-eyed, her throat letting out a deep, guttural howl as she reached her peaked."
    kat "Oh? Already?"
    ver "Geggggeh--!"
    scene w1_3202 with flash
    fel "Geeeh, fu-again?! My AasaassssSSssss.... es... numb...!"
    kat "You too? My, my. You {i}really{/i} do have a sensitive asshole, don't you?"
    kat "Once you pop, you just can't stop."
    scene w1_3203 with vpunch
    stop music
    play sound "sound effects/thud-floor.mp3"
    "*{b}Thud!{/b}*"
    "In an instant, the flurry of sex just ceased."
    "Both Carnations gave out, flopping down on the cushioned surface. They weren't unconscious, but their legs had turned to jelly and their minds to mush."
    kat "It looks like both these fuck pigs are out. I wonder, will we be lucky enough to have a game of sudden death? Hmpfhf... no, no..."
    "The ten seconds passed."
    kat "How about this? The first whore to get on her feet and take a bow wins."
    scene w1_3204 with dissolve
    kat "Lend the girls a hand, boys."
    scene w1_3205 with dissolve
    mc "Oh...?"
    scene w1_3206 with vpunch
    play music "music/doll-dancing.mp3"
    play sound "sound effects/shock2.wav"
    "*Bzzt!"
    "Felicia suddenly tensed up, her toned legs straightening out from a sudden zap from her collar."
    kil "C'mon! Get up, Felish!"
    "Ian called out words of encouragement to get the golden beauty to her feet."
    scene w1_3207 with vpunch
    play sound "sound effects/shock2.wav"
    "*Bzzt!"
    kil "You gotta stand up if you wanna win!"
    fel "Ah, eh... what? Oh, right... Mrs. P said..."
    play sound "sound effects/shock3.wav"
    "*Bzzt!" with vpunch
    fel "Gh--! Oh!"
    scene w1_3208 with dissolve
    "Felicia made the first move in the battle to stand up, while Veronica still hadn't regained her senses."
    scene w1_3209 with dissolve
    mct "(Oh, shit... right!)"
    "In my hand was the remote control to the shock collar around Veronica's neck and I was tasked with the dubious responsibility of providing \"encouragement\" to the slumbering amazon."
    "I peered at the menu, unsure about what to do."
    hide screen textbox2 with dissolve


    menu:
        "Hit the low setting button. [gr]\[ShockPoints +1\]":
            $ w1ExShockPoints +=1
            scene w1_3210 with dissolve
            show screen textbox2 with dissolve
            play sound "sound effects/short-beep.wav"
            "Not wanting to hurt Veronica, my thumb reflexively moved to the top option."
            scene w1_3213 with vpunch
            play sound "sound effects/shock1.wav"
            "*Bzzt!"
            ver "Eh...?"
            "Almost instantly, Veronica's collar gave a slight buzz, but the collapsed woman did not even stir."
            mc "Veronica! You need to stand up!"
            play sound "sound effects/shock1.wav"
            "*Bzzt!" with vpunch
            mc "You'll lose if you don't!"
            play sound "sound effects/shock1.wav"
            "*Bzzt!" with vpunch
            if toughness > 20:
                mc "Stand the fuck up, girl!"
            else:
                mc "Can't you hear me?"
            "I called out, hoping to get through to her, but to no avail."
            scene w1_3214 with dissolve
            "Felicia, meanwhile was in the process of standing up. If I didn't do something, Veronica was about to lose game #2 and move onto the final one."
            "Then again, what does it matter to me who wins...?"
            scene w1_3209 with dissolve
            hide screen textbox2 with dissolve
            jump w1ExFollowThroughVeroShock

        "Hit the medium setting button. [gr]\[ShockPoints +2\]":
            $ w1ExShockPoints +=2
            scene w1_3211 with dissolve
            show screen textbox2 with dissolve
            play sound "sound effects/short-beep.wav"
            "Wanting her to get up, but too scared to press the high setting, my thumb reflexively moved to the middle option."
            scene w1_3213 with vpunch
            play sound "sound effects/shock2.wav"
            "*Bzzt!"
            scene w1_3215 with dissolve
            ver "Eh..ooOoh? What the-?"
            "Almost instantly, Veronica's collar gave a moderate buzz, returning the amazon to some semblance of alertness."
            play sound "sound effects/shock2.wav"
            "*Bzzt!" with vpunch
            mc "Veronica! You need to stand up! You'll lose if you don't!"
            ver "W-what...?"
            if toughness > 20:
                mc "Stand the fuck up, girl!"
            else:
                mc "Stand up!"
            scene w1_3216 with dissolve
            "Felicia, meanwhile was in the process of standing up. If I didn't do something, Veronica was about to lose game #2 and move onto the final one."
            "Then again, what does it matter to me who wins...?"
            scene w1_3209 with dissolve
            hide screen textbox2 with dissolve
            jump w1ExFollowThroughVeroShock

        "Hit the high setting button. [gr]\[ShockPoints +3\]":
            $ w1ExShockPoints +=3
            scene w1_3212 with dissolve
            show screen textbox2 with dissolve
            play sound "sound effects/short-beep.wav"
            "Wanting her to get up, or just curious about what it'd do, my thumb reflexively moved to the bottom option."
            scene w1_3213 with vpunch
            play sound "sound effects/shock3.wav"
            "*Bzzt!"
            scene w1_3217 with dissolve
            ver "Eh..ooOooooh? Shit! What the-?"
            "Almost instantly, Veronica's collar gave a distinct buzz, causing her to spring straight up from her stupor."
            mc "Veronica! You need to stand up!"
            ver "W-what...? Eh...?"
            mc "Veronica! You need to stand up! You'll lose if you don't!"
            scene w1_3218 with dissolve
            "Felicia, meanwhile was in the process of standing up. If I didn't do something, Veronica was about to lose game #2 and move onto the final one."
            "Then again, what does it matter to me who wins...?"
            scene w1_3209 with dissolve
            hide screen textbox2 with dissolve
            jump w1ExFollowThroughVeroShock


    menu w1ExFollowThroughVeroShock:
        mod "For Felicia Win: ShockPoints == 2, 3 or 6\nFor Veronica Win: ShockPoints ==  4 or 5"
        "Hit the low setting button. [gr]\[ShockPoints +1\]":

            if w1ExShockPoints == 1:
                $ w1ExGame2WinnerFel = True
                $ w1ExGame2LoserVero = True
                scene w1_3210 with dissolve
                play sound "sound effects/short-beep.wav"
                show screen textbox2 with dissolve
                "Still hesitant about harming her, I gave the first option a second press."
                play sound "sound effects/shock1.wav"
                scene w1_3219 with vpunch
                "*Bzzt!"
                mc "Felicia's about to win if you don't stand up!"
                "Again, the redhead barely registered the shock. By the time I considered maybe trying the medium option..."
                scene w1_3223 with fade
                "Felicia had managed to climb to her feet."
                fel "Eh...! I win...?"
                scene black with fade
                if not persistent.w1ExGame2VeroFelGallery:
                    play sound "sound effects/notification.wav"
                    show memoryunlock with dissolve
                    $ renpy.pause(3, hard=True)
                    $ persistent.w1ExGame2VeroFelGallery = True
                    hide memoryunlock with dissolve
                    $ renpy.pause(0.5, hard=True)
                "Felicia had taken game number 2."
                $ renpy.end_replay()
                jump w1ExGame2Aftermath

            if w1ExShockPoints == 2:
                $ w1ExGame2WinnerFel = True
                $ w1ExGame2LoserVero = True
                scene w1_3210 with dissolve
                show screen textbox2 with dissolve
                play sound "sound effects/short-beep.wav"
                "Thinking I had gotten her attention with the last one, I gave the first option a press."
                scene w1_3220 with vpunch
                play sound "sound effects/shock1.wav"
                "*Bzzt!"
                mc "Felicia's about to win if you don't stand up!"
                ver "I need to...?"
                "The redhead barely registered the shock. By the time I considered maybe trying another option..."
                scene w1_3223 with fade
                "Felicia had managed to climb to her feet."
                fel "Eh...! I win...?"
                scene black with fade
                if not persistent.w1ExGame2VeroFelGallery:
                    play sound "sound effects/notification.wav"
                    show memoryunlock with dissolve
                    $ renpy.pause(3, hard=True)
                    $ persistent.w1ExGame2VeroFelGallery = True
                    hide memoryunlock with dissolve
                    $ renpy.pause(0.5, hard=True)
                "Felicia had taken game number 2."
                $ renpy.end_replay()
                jump w1ExGame2Aftermath

            if w1ExShockPoints == 3:
                $ w1ExGame2WinnerVero = True
                $ w1ExGame2LoserFel = True
                scene w1_3210 with dissolve
                play sound "sound effects/short-beep.wav"
                show screen textbox2 with dissolve
                "Seeing how fast she sprung up previously, I was hesitant to giving her another shock at the same power, so I opted to take it all the way down to low."
                scene w1_3220 with dissolve
                play sound "sound effects/shock1.wav"
                "*Bzzt!" with vpunch
                ver "Ugh..."
                mc "Felicia's about to win if you don't stand up!"
                scene w1_3221 with dissolve
                ver "Oh, shit!"
                "Thankfully, the first shock seemed to have brought her back to full cognition and she immediately understood."
                "With a startling burst of energy..."
                "Veronica took to her feet in lighting fast time."
                scene w1_3224 with fade
                "Veronica took to her feet in lighting fast time, beating Felicia to the punch and securing game number 2."
                scene black with fade
                if not persistent.w1ExGame2VeroFelGallery:
                    play sound "sound effects/notification.wav"
                    show memoryunlock with dissolve
                    $ renpy.pause(3, hard=True)
                    $ persistent.w1ExGame2VeroFelGallery = True
                    hide memoryunlock with dissolve
                    $ renpy.pause(0.5, hard=True)
                ver "So... I win?"
                $ renpy.end_replay()
                jump w1ExGame2Aftermath


        "Hit the medium setting button. [gr]\[ShockPoints +2\]":
            if w1ExShockPoints == 1:
                $ w1ExGame2WinnerFel = True
                $ w1ExGame2LoserVero = True
                scene w1_3211 with dissolve
                show screen textbox2 with dissolve
                play sound "sound effects/short-beep.wav"
                "Still not wanting to hurt her, but feeling a sense of urgency, I decided to move up to the next level of power."
                scene w1_3220 with vpunch
                play sound "sound effects/shock2.wav"
                "*Bzzt!"
                ver "Eh..ooOoh? What the-?"
                "Almost instantly, Veronica's collar gave a moderate buzz, returning the amazon to some semblance of alertness."
                mc "Felicia's about to win if you don't stand up!"
                ver "Wait, she is?!"
                "However, it proved too little too late as it wasn't enough to clear the haze of confusion she was under. By the time she realized what was going on..."
                scene w1_3223 with dissolve
                "Felicia had managed to climb to her feet."
                fel "Eh...! I win...?"
                scene black with fade
                if not persistent.w1ExGame2VeroFelGallery:
                    play sound "sound effects/notification.wav"
                    show memoryunlock with dissolve
                    $ renpy.pause(3, hard=True)
                    $ persistent.w1ExGame2VeroFelGallery = True
                    hide memoryunlock with dissolve
                    $ renpy.pause(0.5, hard=True)
                "Felicia had taken game number 2."
                $ renpy.end_replay()
                jump w1ExGame2Aftermath


            if w1ExShockPoints == 2:
                $ w1ExGame2WinnerVero = True
                $ w1ExGame2LoserFel = True
                scene w1_3211 with dissolve
                show screen textbox2 with dissolve
                play sound "sound effects/short-beep.wav"
                "The medium option seemed effective, so I opted to give it another press."
                scene w1_3221 with vpunch
                play sound "sound effects/shock2.wav"
                "*Bzzt!"
                mc "Felicia's about to win if you don't stand up!"
                ver "Oh shit!"
                scene w1_3224 with fade
                "Immediately registering what was going on, Veronica sprung up with a surprising vigor."
                "Beating Felicia to the punch and securing game number 2."
                scene black with fade
                if not persistent.w1ExGame2VeroFelGallery:
                    play sound "sound effects/notification.wav"
                    show memoryunlock with dissolve
                    $ renpy.pause(3, hard=True)
                    $ persistent.w1ExGame2VeroFelGallery = True
                    hide memoryunlock with dissolve
                    $ renpy.pause(0.5, hard=True)
                ver "So... I win?"
                $ renpy.end_replay()
                jump w1ExGame2Aftermath


            if w1ExShockPoints == 3:
                $ w1ExGame2WinnerVero = True
                $ w1ExGame2LoserFel = True
                scene w1_3211 with dissolve
                play sound "sound effects/short-beep.wav"
                show screen textbox2 with dissolve
                "Seeing how fast she sprung up previously, I was hesitant to giving her another shock at the same power, so I opted to take it all the way down a level."
                scene w1_3221 with vpunch
                play sound "sound effects/shock2.wav"
                "*Bzzt!"
                mc "Felicia's about to win if you don't stand up!"
                ver "Gggh...! Wha- Oh, oh shit! I need to...!"
                scene w1_3224 with fade
                "Immediately registering what was going on, Veronica sprung up with a surprising vigor."
                "Beating Felicia to the punch and securing game number 2."
                scene black with fade
                if not persistent.w1ExGame2VeroFelGallery:
                    play sound "sound effects/notification.wav"
                    show memoryunlock with dissolve
                    $ renpy.pause(3, hard=True)
                    $ persistent.w1ExGame2VeroFelGallery = True
                    hide memoryunlock with dissolve
                    $ renpy.pause(0.5, hard=True)
                ver "So... I win?"
                $ renpy.end_replay()
                jump w1ExGame2Aftermath

        "Hit the high setting button. [gr]\[ShockPoints +3\]":

            if w1ExShockPoints == 1:
                $ w1ExGame2WinnerVero = True
                $ w1ExGame2LoserFel = True
                scene w1_3212 with dissolve
                play sound "sound effects/short-beep.wav"
                show screen textbox2 with dissolve
                "Seeing how fast she sprung up previously, I was hesitant to giving her another shock at the same power, so I opted to take it all the way down to low."
                scene w1_3220 with dissolve
                ver "Ugh..."
                play sound "sound effects/shock3.wav"
                scene w1_3221 with vpunch
                "*Bzzt!"
                ver "Gah! W-what...?"
                mc "Felicia's about to win if you don't stand up!"
                ver "Huh... What is... oh, shit!"
                "The reality quickly dawned on Veronica and with a startling burst of energy..."
                scene w1_3224 with fade
                "Veronica took to her feet in lighting fast time, Beating Felicia to the punch and securing game number 2."
                scene black with fade
                if not persistent.w1ExGame2VeroFelGallery:
                    play sound "sound effects/notification.wav"
                    show memoryunlock with dissolve
                    $ renpy.pause(3, hard=True)
                    $ persistent.w1ExGame2VeroFelGallery = True
                    hide memoryunlock with dissolve
                    $ renpy.pause(0.5, hard=True)
                ver "So... I win?"
                $ renpy.end_replay()
                jump w1ExGame2Aftermath


            if w1ExShockPoints == 2:
                $ w1ExGame2WinnerVero = True
                $ w1ExGame2LoserFel = True
                scene w1_3212 with dissolve
                play sound "sound effects/short-beep.wav"
                show screen textbox2 with dissolve
                "The high powered option had caused her to sit straight up, but I was hesitant to dole out another shock at the same power, so I opted to take it down to medium"
                scene w1_3221 with vpunch
                play sound "sound effects/shock3.wav"
                "*Bzzt!"
                mc "Felicia's about to win if you don't stand up!"
                ver "Gggh...! Wha- Oh, oh shit!"
                "Immediately registering what was going on, Veronica sprung up with a surprising vigor."
                scene w1_3224 with fade
                "Beating Felicia to the punch and securing game number 2."
                scene black with fade
                if not persistent.w1ExGame2VeroFelGallery:
                    play sound "sound effects/notification.wav"
                    show memoryunlock with dissolve
                    $ renpy.pause(3, hard=True)
                    $ persistent.w1ExGame2VeroFelGallery = True
                    hide memoryunlock with dissolve
                    $ renpy.pause(0.5, hard=True)
                ver "So... I win?"
                $ renpy.end_replay()
                jump w1ExGame2Aftermath

            if w1ExShockPoints == 3:
                $ w1ExGame2WinnerFel = True
                $ w1ExGame2LoserVero = True
                scene w1_3212 with dissolve
                show screen textbox2 with dissolve
                play sound "sound effects/short-beep.wav"
                "Seeing how fast she sprung up previously, I was sure another shock at that level would do it."
                scene w1_3222 with vpunch
                play sound "sound effects/shock3.wav"
                "*Bzzt!"
                ver "Geee-h, f-fuck! Son of a bitch...!"
                mc "Felicia's about to win if you don't stand up!"
                ver "Ah, that hurts-!"
                "Instead of alerting her to what was going on, the pain from the back to back shocks distracted her. So much so that..."
                scene w1_3223 with dissolve
                "Felicia had managed to climb to her feet."
                fel "Eh...! I win...?"
                scene black with fade
                if not persistent.w1ExGame2VeroFelGallery:
                    play sound "sound effects/notification.wav"
                    show memoryunlock with dissolve
                    $ renpy.pause(3, hard=True)
                    $ persistent.w1ExGame2VeroFelGallery = True
                    hide memoryunlock with dissolve
                    $ renpy.pause(0.5, hard=True)
                "Felicia had taken game number 2."
                $ renpy.end_replay()
                jump w1ExGame2Aftermath




label w1ExFollowThroughVeroRoseStart:

    scene w1_3225 with curtains
    kat "Gentlemen, we are to begin! Allow me to explain the next game."
    "About twenty or so minutes after Hana had scurried back to the bar, game two was kicking off. Veronica and Rosalind had already taken their \"starting\" positions, ass to ass and down on their hands and knees at the center of the stage."
    scene w1_3226 with dissolve
    play music "music/myst-on-the-moor.mp3"

    if kat_polite == True:
        "A double-sided dildo rested between them, lewdly connecting the two women together at their honeypots. They were tasked with the uncomfortable prospect of awkwardly holding that position while Mrs. Pulman explained what was coming next."
    else:
        "A double-sided dildo rested between them, lewdly connecting the two women together at their honeypots. They were tasked with the uncomfortable prospect of awkwardly holding that position while Kathleen explained what was coming next."

    scene w1_3142 with dissolve
    kat "Our first game was about the first tenant of customer service. Exploring the needs of the customer."
    kat "Our second game will hone in on what I think of as the next: {b}actualization{/}. The art of the follow through."
    kat "In simplest terms, being able to keep focus on your task despite any roadblocks that might arise."
    scene w1_3143 with dissolve

    if kat_polite ==True:
        "Par for the course, Mrs. Pulman aggrandized what is otherwise just an excuse to perversely watch women squirm in discomfort."
    else:
        "Par for the course, Kathleen aggrandized what is otherwise just an excuse to perversely watch women squirm in discomfort."

    scene w1_3144 with dissolve
    kat "...and what will be the task? It's simple. You'll just need to shake your hips like the whores you are."
    kat "You two will fuck each other for all your worth. If you start slacking, the collars around your neck will generously provide you a pick me up"
    scene w1_3145 with dissolve
    ver "What do you mean by pick-me-up?"
    scene w1_3146 with dissolve
    kat "Simply put, it'll administer a brief shock that will jolt you back to your senses and get you moving again. If you don't get back to the task within 10 seconds, you'll be disqualified."
    scene w1_3147 with dissolve
    ver "What the fuck?"
    scene w1_3227 with dissolve
    rose "You're going to shock us? That's... scary..."
    scene w1_3228 with dissolve
    kat "Don't get bent out of shape. It's nothing dangerous for a healthy adult woman. It's more akin to a dog's training collar, but adjusted for a dumb cow like you."
    scene w1_3229 with dissolve
    rose "..."
    "Rosalind looks uncomfortable for a brief moment, but she quickly steeled herself."
    scene w1_3230 with dissolve
    hide screen textbox2 with dissolve
    kat "If either of you find the prospect unappealing, one of you can always resign and move onto the last game by your lonesome."
    scene w1_3231 with dissolve
    ver "No! Let's do this."
    rose "I'll do whatever it takes."
    scene w1_3232 with dissolve
    kat "Good. I thought so. That's not all there is to this game though. You'll also be asked some questions."
    scene w1_3154 with dissolve
    show screen textbox2 with dissolve
    kat "Simple, basic things that any woman your age should be able to answer. A wrong or delayed answer will make things more difficult for you."
    scene w1_3155 with dissolve
    kat "Do you two understand the parameters of this game?"
    scene w1_3156 with dissolve
    rose "Yes, Mrs. Pulman."
    ver "Aye..."
    scene w1_3233 with dissolve
    kat "Mr. [mcl]! Mr. Beaufort! You'll be charged with administering the shocks. You've familiarized yourself with the remote control I've given you?"
    scene w1_3234 with dissolve
    kil "Yup!"
    mc "I think so."
    scene w1_3233 with dissolve
    kat "It's very simple. There's three settings. Each corresponds to a low, medium, and high powered shock. I'll leave it to your discretion what you feel is appropriate."
    mct "(Is this part of the test she mentioned...?)"
    kat "Mr. [mcl]'s remote is synced with Mrs. Carter's collar. Mr. Beaufort's is synced to Miss Lynch's."


label w1ExFollowThroughVeroRose:

    if _in_replay:
        show screen textbox2 with dissolve

    scene w1_3159 with dissolve
    kat "Now, enough talking. Let's get to why all you gentlemen are really here. On the count of three, I want you to start fucking each other like your future depends on it."
    stop music fadeout 3.0
    scene w1_3160 with dissolve
    kat "Three..."
    scene w1_3161 with dissolve
    kat "Two..."
    scene w1_3162 with dissolve
    kat "One..."
    scene w1_3163 with dissolve
    image roseverodil1= Movie(play="roseverodil1.webm")
    image roseverodil2= Movie(play="roseverodil2.webm")
    image roseverodil3= Movie(play="roseverodil3.webm")
    image roseverodil4= Movie(play="roseverodil4.webm")
    image roseverodil5= Movie(play="roseverodil5.webm")
    kat "Begin, whores!"
    play music "music/guiton-sketch.mp3"
    show roseverodil1 with dissolve
    "Cutting through the air with an enthusiastic chop, she signaled for the two Carnations to begin the trial."
    "Veronica hurled herself ass first, drawing her body back until her rear collided with Rosalind's with a rippling impact."
    "Rosalind on the other hand took a more tentative approach, blindly using her hips to slowly feel out the mechanics of the act."
    "In response, Veronica slowed her pace to match her opponents, in a conscientious effort to keep the toy safely between them."
    "Both women pushed back and forward, sliding themselves off and revealing more and more of the golden toy that connected them before sleeving it once more within their quims."
    "It was like an awkward dance. On paper it might sound simple, but the reality was each woman was struggling to find the appropriate tempo that would make it easier for the both of them."
    kat "Very good, girls."
    "Veronica lurched forward at such a depth that the dildo almost slipped out from in between them, but quickly overcorrected and brought her ass crashing back into Rosalind's, resulting in a pleasant looking ripple on the whore mother's behind."
    scene roseverodil4 with dissolve
    hide roseverodil1
    kat "Keep those hips moving and those asses shaking. It's one of the few things you're good for."
    "Eventually the two settled found a workable rhythm, moving in tandem like some perverted seesaw."
    "As one would expect, both Carnations bore an uncomfortable look on their face. Each concentrated on keeping their hips unceasingly moving and the sex-toy lodged in their cunts."
    hide screen textbox2 with dissolve
    scene roseverodil2 with dissolve
    hide roseverodil4
    ver "Just give up, Rose! The sooner you do, the sooner this night can be over and you can get back to your kid!"
    scene roseverodil3 with dissolve
    hide roseverodil2
    rose "Don't...! Why don't you just focus on what you're doing instead of worrying about me?"
    scene roseverodil1 with dissolve
    hide roseverodil3
    show screen textbox2 with dissolve
    ver "What do you think I'm doing here?"
    "Veronica squared her shoulders and began to buck her hips more forcefully."
    rose "Geh...!"
    "*Plap* *Smack* *Slap!*"
    rose "Ah~ oh, no...!"
    "The sudden change in pace startled Rosalind, causing her face to scrunch up in a mix of pleasure and tension."
    scene roseverodil4 with dissolve
    hide roseverodil1
    "It was like Veronica was declaring to her: \"I'm going to wear you down\". However..."
    ver "Ngg...!"
    "It was a double sided sword, almost quite literally. She wasn't immune to rough change of pace herself."
    kat "You best keep up, Rose. You want to win this don't you?"
    rose "Yes!"
    kat "I know you do! Give these gentlemen a fine show then! Make that fat ass of your bounce!"
    scene w1_3166 with dissolve
    kat "However, let's make things more interesting."
    scene w1_3167 with dissolve
    kat "Hmmm-mmmh~hmmm~ Let's see...    "
    kat "You girls know your multiplication tables...?"
    scene w1_3168 with dissolve

    if kat_polite:
        "Having gone over to one of the nearby tables, Mrs. Pulman carefully considered her options while posing an odd question."
    else:
        "Having gone over to one of the nearby tables, Kathleen carefully considered her options while posing an odd question."

    "Neither women deigned to answer her question."
    scene w1_3169 with dissolve
    kat "Let's get things rolling. We'll start with..."
    scene w1_3170 with dissolve
    kat "Miss Lynch."
    hide screen textbox2 with dissolve
    scene roseverodil2 with dissolve
    hide roseverodil4
    ver "Eeeeh...? W-what are you talking about?"
    kat "Answer quickly. What is eleven times twelve?"
    ver "W-what--?"
    kat "Five, four, three, two..."
    ver "Uh... 132!"
    scene roseverodil3 with dissolve
    hide roseverodil2
    kat "Correct. Mrs. Carter: fourteen times eight?"
    rose "Wait... eh... 96... 104.. 112!"
    kat "Correct!"
    rose "Why are you--"
    scene roseverodil4 with dissolve
    hide roseverodil3
    show screen textbox2 with dissolve
    kat "Veronica! Thirteen times nine?"
    ver "One--one hundred seventeen!"

    if kat_polite == True:
        "All the while the two pumped their hips, the Carnations went back and forth answering Mrs. Pulman's questions."
    else:
        "All the while the two pumped their hips, the Carnations went back and forth answering Kathleen's questions."

    rose "120!"
    ver "168!"
    rose "182!"
    scene w1_3235 with dissolve
    hide screen textbox2 with dissolve
    kat "Oops, sorry! The answer was 196! Mrs. Carter takes the first hit."
    rose "The first hit...?"
    "Rosalind looked anxious at the ominous words."
    scene w1_3236 with dissolve
    rose "Gh! Wh-wha-"
    scene w1_3237 with vpunch
    rose "Eeee-wh-what!"

    if kat_polite == True:
        "Finding a window of opportunity while the pair was separating, Mrs. Pulman shoved a prickly golf ball sized sphere into Rosalind's tight tailhole."
    else:
        "Finding a window of opportunity while the pair was separating, Mrs. Kathleen shoved a prickly golf ball sized sphere into Rosalind's tight tailhole."

    scene w1_3238 with vpunch
    rose "Eh... gah!"
    scene w1_3237 with dissolve
    "The reaction was immediate. As the pair's backsides smacked together, a look of sudden discomfort flooding the whore mother's face."
    scene w1_3238 with dissolve
    rose "Did you just...ng- ah!"
    scene w1_3237 with vpunch
    rose "Mmmmhm!"
    scene w1_3238 with dissolve
    "Every time Rosalind's plump ass collided with Veronica's stony backside, she reeled from the pink toy sliding around her colon and let out a delectable, shrill cry."
    ver "W-why is she sounding like that?!"
    scene w1_3237 with vpunch
    rose "My.. butt! My buUuuUuuTT!! I've never had-"
    scene w1_3239 with dissolve
    play sound "sound effects/slap2.wav"
    scene w1_3240 with vpunch
    "*{b}Smack!!!{/b}*"
    rose "Tcckkk--! Fgggh--!"
    scene w1_3154 with dissolve
    show screen textbox2 with dissolve
    kat "Had anything shoved in your shithole?"
    kat "Wonderful. We have our very own anal newbie in our midst tonight, gentlemen."
    kat "You're going to learn quick. I promise you'll be crying out like a seasoned buttslut by the end of this."
    scene w1_3156 with dissolve
    rose "Ehehe...!"
    scene w1_3155 with dissolve
    kat "Miss Lynch, back to you. Seventimes time nineteen, please."
    ver "What the fuck?!"
    kat "Five, four, three..."
    ver "No one c-can -ah!- answer that in..."
    scene w1_3241 with dissolve
    hide screen textbox2 with dissolve
    kat "Times up!"
    scene w1_3242 with dissolve
    ver "Gh...? W-what did you just put in my--"
    scene w1_3244 with vpunch
    ver "AaaaAAAssssssssshole!"
    scene w1_3243 with dissolve
    "Veronica reacted as Rosalind had, with total and complete shock at the strange sensation."
    scene w1_3244 with vpunch
    ver "Gha!"
    scene w1_3243 with dissolve
    kat "Just a little toy to make things more interesting."
    scene w1_3244 with vpunch
    ver "Little? Gh! Egh! Fuck!"
    rose "OoooOOoooooh!"
    "The pair practically harmonized, squealing in unison and creating a wonderful sound."
    scene w1_3181 with dissolve
    show screen textbox2 with dissolve
    kat "Mrs. Carter. Nineteen times fifteen..."
    rose "Oh, no..."
    scene w1_3182 with dissolve

    if kat_polite == True:
        "The pair answered Mrs. Pulman's questions back and forth, with equal opportunity, but invariably Rosalind came up on the short side of things."
    else:
        "The pair answered Kathleen's questions back and forth, with equal opportunity, but invariably Rosalind came up on the short side of things."

    scene w1_3183 with dissolve
    "One by one..."
    scene w1_3184 with dissolve
    "The remaining four balls on the table disappeared..."
    scene w1_3185 with dissolve
    "By the time they'd all disappeared, four out of the six spike-lined balls had found their way into Rosalind's butthole."
    play sound "sound effects/slap2.wav"
    pause 0.5
    play sound "sound effects/slap2.wav"
    pause 0.5
    play sound "sound effects/slap2.wav"
    "*{b}Smack{/b}* *{b}Smack{/b}!* *{b}Smack{/b}-!!*"
    scene w1_3245 with dissolve
    rose "Onnn- oh, gghuu!"

    if kat_polite == True:
        "At this point, Rosalind was suffering the brunt of the punishment. Having run out of the sex-toys, Mrs. Pulman began delivering harsh spanks for incorrect answers."
    else:
        "At this point, Rosalind was suffering the brunt of the punishment. Having run out of the sex-toys, Kathleen began delivering harsh spanks for incorrect answers."

    "Each swat of the paddle sent Rosalind's wide ass quaking, knocking the ribbed pink toys against each other and scraping the lining of the desperate mother's bowels."
    "The pervert in me had to hand it to her. It was a simple approach, but the results were etched into Rosalind's increasingly twisted face."
    scene w1_3246 with quickdissolve
    scene w1_3247 with quickdissolve
    play sound "sound effects/slap2.wav"
    scene w1_3248 with vpunch
    "*{b}Slap!{/b}*"
    scene w1_3247 with dissolve
    scene w1_3246 with dissolve
    rose "Ohh... oh! Mercy! Mercy!"
    kat "You want mercy, you stupid slut?!"
    rose "Yes!"
    scene w1_3246 with quickdissolve
    scene w1_3247 with quickdissolve
    play sound "sound effects/slap2.wav"
    scene w1_3248 with vpunch
    "*{b}Slap!{/b}*"
    scene w1_3247 with dissolve
    scene w1_3246 with dissolve
    kat "You're letting Miss Lynch run away with this! You can't even answer a simple question?"
    scene w1_3246 with quickdissolve
    scene w1_3247 with quickdissolve
    play sound "sound effects/slap2.wav"
    scene w1_3248 with vpunch
    "*{b}Slap!{/b}*"
    scene w1_3247 with dissolve
    scene w1_3246 with dissolve
    rose "Ng! Eh... gghuu..! It feels goood? Why does it feel...?"
    scene w1_3246 with quickdissolve
    scene w1_3247 with quickdissolve
    play sound "sound effects/slap2.wav"
    scene w1_3248 with vpunch
    "*{b}Slap!{/b}*"
    scene w1_3247 with dissolve
    scene w1_3246 with dissolve
    rose "Ng! Merc-eeeeeeeh...!!! I'm going to...!"
    scene w1_3246 with quickdissolve
    scene w1_3247 with quickdissolve
    play sound "sound effects/slap2.wav"
    scene w1_3248 with vpunch
    "*{b}Slap!{/b}*"
    "One final slap sent Rosalind over the edge, causing her to arch her back and call out with a violent, pleasured cry."
    scene w1_3249 with dissolve
    rose "Ffghhhhheeeee!...ehehe... hehe...!"
    scene w1_3190 with dissolve
    kat "Ha! That was fast! You came from having your fat ass battered. You're a fucking natural!"
    scene w1_3189 with dissolve

    if kat_polite == True:
        "Mrs. Pulman cackled in delight, pleased at the miserable display in front of her."
    else:
        "Kathleen cackled in delight, pleased at the miserable display in front of her."

    rose "Eheh... heh... eheh... woah..."
    scene w1_3195 with dissolve
    ver "H-hey... ngh! Don't you think you're being a little too hard on her? Ah...!"
    "While Rosalind had been taking the worst of it, Veronica still showed signs of sexual arousal. Sweet, quiet moans escaped her lips as she expressed open concern for her opponent."
    scene w1_3187 with dissolve
    kat "You should worry about yourself, Miss Lynch."
    scene w1_3188 with dissolve
    "Despite having just orgasmed, Rosalind kept to task. Never ceasing working in tandem with Veronica's bucking hips."
    scene w1_3187 with dissolve
    kat "Mrs. Carter isn't out of this by a long shot."
    scene w1_3189 with dissolve
    rose "I-I'm... eh... I'm going to w-win...!"
    scene w1_3187 with dissolve
    kat "What about you?"
    scene w1_3188 with dissolve
    ver "F-feh! I could do this all night!"
    scene w1_3187 with dissolve
    kat "Big words when you don't know what's next."
    scene w1_3251 with dissolve
    mc "They're unbelievable..."
    scene w1_3250 with dissolve
    kil "Shit, this is good..."
    scene w1_3198 with dissolve
    kat "This time you have 30 seconds to answer."
    ver "We're not done with this nonsense?"
    kat "No. Not until one of you yields."
    scene w1_3199 with dissolve
    kat "I have a riddle for you, are you listening?"
    hide screen textbox2 with dissolve
    scene roseverodil2 with dissolve
    hide roseverodil4
    ver "Ggeeeh, t-this is... yes! I'm listening!"
    kat "Good! Here it is: \"Without it, I'm dead. If I'm not, then I'm behind. What am I?\"."
    ver "Uuuuh, ah, fuck! I was never good at these! Uh... Without it I'm..."
    ver "...then I'm behind...? Uh..."
    kat "Ten seconds."
    ver "MMh... Uh..."
    kat "Five seconds. Four, three, two..."
    ver "Oxygen?!"
    kat "Sorry, that is an incorrect answer. The one I'm looking for is \"ahead\"."
    ver "Dah-damn it!"
    kat "Now..."
    play sound "sound effects/vib-start.wav"
    scene w1_3252 with hpunch
    "*Bzzzzt!*"
    "Like with the balls, the cruel woman slipped the newly fetched toy - an anal vibrator - smoothly into the amazon's tightening pucker and turned it on."
    ver "Mmmmn~eeh, ah... fhug...!!!"
    "The vibrating rod being shoved mercilessly into her crowded tail hole produced a garbled slew of intelligibly whorish moans."
    scene roseverodil5 with dissolve
    hide roseverodil2
    show screen textbox2 with dissolve
    kat "Haha, how do you like that?"
    ver "Tk-! The vib---gh, the vibrations-!"
    kat "I know, right? In such a tight space, it's making the studded eggs vibrate along with it. You can feel those vibrations all the way into your stomach and into your chest."
    ver "Ghh...! Y-ngh-mmg-oh, yh-yes!"
    kat "I'm very glad you were the one who got my riddle wrong. You need that extra push to make you admit a basic truth."
    kat "What truth is that, you're unable to ask right now... but I'll tell you anyway. The truth is, there is a part of you that enjoys this."
    ver "Ehegh, n-no!"
    kat "Don't lie. I know all about you, Miss Lynch. You career as a sportswoman, your work as a fitness model. The fitness competitions... you like being looked at. You like the limelight."

    if kat_polite == True:
        "Mrs. Pulman must've been delighted to have Veronica under her control, with no choice but to listen to her bullshit observations."
    else:
        "Kathleen must've been delighted to have Veronica under her control, with no choice but to listen to her bullshit observations."

    "Even with the additional discomfort, Veronica continued to match Rosalind thrust for thrust, moving her hips at a furious pace and drilling herself on the golden dildo."
    ver "Gh-! Ah-! Eyeee....!"
    "The sight made me think Mrs. Pulman might've not been off base when it came from Veronica. From where I sat, it looked like the woman at least had something of an exhibitionist streak."
    ver "Zheee-buzz-buzzing!"
    "She was at least feeling it. It wasn't just the goal of winning the competition that was driving her hips, it was also needy, craven desire."
    "Rosalind was naturally looking in even worse shape, having double the amount of toys inside her and being in a post-orgasm haze."
    hide screen textbox2 with dissolve
    scene roseverodil2 with dissolve
    hide roseverodil5
    ver "Eh.. w-what about Rose? Doesn't she get -ng!- a riddle?"
    kat "Sorry! I only know the one!"
    scene roseverodil5 with dissolve
    hide roseverodil2
    show screen textbox2 with dissolve
    "Incredibly the scene carried on for minutes more, Rosalind hanging on by a thread. She pistoned her hips with wild abandoned, keeping her giant ass in a perpetual flurry."
    "Veronica kept howling, but did the same. It was an marvellous sight. The two women sweating profusely, squirming in ecstasy, loose strands of hair matting the napes of the neck."
    "The room was completely quite."
    "Even our cruel ringleader shut the fuck up for once, instead letting the near silent room be filled with the dirty sounds of copulation and ragged breathing."
    "In this moment, I was utterly divorced from my regular life. [mcf] was just a name at the back of my head and his worries seemed so trite."
    ver "Eh... eh..!"
    scene w1_3253 with vpunch
    ver "Ooofffhhooooo-! Ghhhg... fhuu... ghw...!!!!!!!"
    "I watched the large woman's expression go cross-eyed, her throat letting out a deep, guttural howl as she reached her peaked."
    ver "Geggggeh--!" with vpunch
    kat "Oh? Already? That did it?"
    scene w1_3254 with vpunch
    rose "Geeeh, oh bo....?! My buuuuuuuutt!"
    kat "Oh, you too?"
    rose "Fheeee! Ooooh! Egggguuuggg!" with vpunch
    kat "Once you pop, you just can't stop I guess."
    stop music
    play sound "sound effects/thud-floor.mp3"
    scene w1_3255 with vpunch
    "*{b}Thud!{/b}*"
    "In an instant, the flurry of sex just ceased."
    "Both Carnations gave out, flopping down on the cushioned surface. They weren't unconscious, but their legs had turned to jelly and their minds to mush."
    kat "It looks like both these fuck pigs are out. I wonder, will we be lucky enough to have a game of sudden death? Hmpfhf... no, no..."
    "The ten seconds passed."
    kat "How about this? The first whore to get on her feet and take a bow wins."
    scene w1_3256 with dissolve
    kat "Lend the girls a hand, boys."
    scene w1_3257 with dissolve
    mc "Oh...?"
    play music "music/doll-dancing.mp3"
    play sound "sound effects/shock2.wav"
    scene w1_3258 with vpunch
    "*Bzzt!"
    scene w1_3259 with dissolve
    "Veronica suddenly tensed up, her long legs straightening out from a sudden zap from her collar."
    kil "C'mon! Get up! Get the fuck up!"
    "Ian called out words of encouragement to get the slumbering giant to her feet."
    play sound "sound effects/shock2.wav"
    "*Bzzt!" with vpunch
    scene w1_3260 with dissolve
    kil "You gotta stand up!"
    ver "Mmmh... what?"
    play sound "sound effects/shock3.wav"
    "*Bzzt!" with vpunch
    ver "Fhhuck!"
    kil "Get the fuck on your feet if you want to win!"
    ver "Mmmh..."
    "Veronica was still in a daze, but her body unconsciously began making the first move in the battle to stand up. Meanwhile, Rosalind hadn't regaind her senses."
    scene w1_3261 with dissolve
    mct "(Oh, shit... right!)"
    "I held in my hand a remote control to the shock collar around her neck, tasked with the dubious responsibility of providing encouragement to the slumbering amazon."
    "I looked down at the phone in my hand, unsure about what to do."
    hide screen textbox2 with dissolve

    menu:
        "Hit the low setting button. [gr]\[ShockPoints +1\]":
            $ w1ExShockPoints +=1
            play sound "sound effects/short-beep.wav"
            scene w1_3262 with dissolve
            show screen textbox2 with dissolve
            "Not wanting to hurt the half-conscious mother, my thumb reflexively moved to the top option."
            play sound "sound effects/shock1.wav"
            scene w1_3265 with vpunch
            "*Bzzt!"
            scene w1_3266 with dissolve
            rose "Ghe-?"
            "Almost instantly, Rosalind's collar gave a slight buzz, causing the woman to flinch slightly."
            scene w1_3265 with dissolve
            mc "Rose! You need to stand up!"
            play sound "sound effects/shock1.wav"
            "*Bzzt!" with vpunch
            mc "You'll lose if you don't!"
            play sound "sound effects/shock1.wav"
            scene w1_3266 with vpunch
            "*Bzzt!"
            mc "The first to stand up wins!"
            rose "W-what...?"
            "I called out, hoping to get through to her, but she held a confused look on her face."
            "Veronica, meanwhile was fumbling to get up. If I didn't do something, Rosalind was about to lose game #2 and move onto the final one."
            "Then again, what does it matter to me who wins...?"
            hide screen textbox2 with dissolve
            scene w1_3261 with dissolve
            jump w1ExFollowThroughRoseShock

        "Hit the medium setting button. [gr]\[ShockPoints +2\]":
            $ w1ExShockPoints +=2
            play sound "sound effects/short-beep.wav"
            scene w1_3263 with vpunch
            show screen textbox2 with dissolve
            "Wanting her to get up, but too scared to press the high setting, my thumb reflexively moved to the middle option."
            play sound "sound effects/shock2.wav"
            scene w1_3265 with vpunch
            "*Bzzt!"
            rose "Ghe-? Ow!"
            "Almost instantly, Rosalind's collar gave a moderate buzz, causing the matronly woman to flinch in pain."
            play sound "sound effects/shock2.wav"
            scene w1_3267 with vpunch
            "*Bzzt!"
            mc "Rose! You need to stand up! You'll lose if you don't!"
            rose "W-what...?"
            mc "The first to stand up wins!"
            "Rosalind's face told me she was beginning to understand."
            "Veronica, meanwhile was fumbling to get up. If I didn't do something, Rosalind was about to lose game #2 and move onto the final one."
            "Then again, what does it matter to me who wins...?"
            hide screen textbox2 with dissolve
            scene w1_3261 with dissolve
            jump w1ExFollowThroughRoseShock

        "Hit the high setting button. [gr]\[ShockPoints +3\]":
            $ w1ExShockPoints +=3
            play sound "sound effects/short-beep.wav"
            scene w1_3264 with dissolve
            show screen textbox2 with dissolve
            "Wanting her to get up, or just curious about what it'd do, my thumb reflexively moved to the bottom option."
            play sound "sound effects/shock3.wav"
            scene w1_3265 with vpunch
            "*Bzzt!"
            scene w1_3267 with dissolve
            rose "Ghe- ..ooOooooh? Aaah! The hell-?"
            "Almost instantly, Rosalind's collar gave a distinct buzz, causing her to spring straight up from her stupor and cry out in pain."
            mc "Rose! You need to stand up!"
            scene w1_3269 with dissolve
            rose "W-what...? Eh...?"
            mc "The first to stand up wins! You'll lose if you don't!"
            rose "Crap! That stings... wait, what...?"
            "Although distracted by the shock, Rosalind's face told me she was beginning to understand. "
            "Veronica, meanwhile was fumbling to get up. If I didn't do something, Rosalind was about to lose game #2 and move onto the final one."
            "Then again, what does it matter to me who wins...?"
            hide screen textbox2 with dissolve
            scene w1_3261 with dissolve
            jump w1ExFollowThroughRoseShock

    menu w1ExFollowThroughRoseShock:
        mod "For Veronica Win: ShockPoints == 2, 5 or 6\nFor Roselind Win: ShockPoints == 3 or 4"
        "Hit the low setting button. [gr]\[ShockPoints +1\]":

            if w1ExShockPoints == 1:
                $ w1ExGame2WinnerVero = True
                $ w1ExGame2LoserRose = True
                play sound "sound effects/short-beep.wav"
                scene w1_3262 with dissolve
                show screen textbox2 with dissolve
                "Still hesitant about harming her, I gave the first option a second press."
                play sound "sound effects/shock1.wav"
                scene w1_3265 with vpunch
                "*Bzzt!"
                scene w1_3266 with dissolve
                mc "Veronica is going to win if you don't stand up right now!"
                scene w1_3267 with dissolve
                rose "Eh, she... she is? Oh, shoot!"
                "By the time she had fully grasped the situation, it was too little, too late."
                "Veronica had managed to prop herself up and stand on her own two feet."
                scene w1_3272 with fade
                ver "*huff* *huff* I... win?"
                scene black with fade
                if not persistent.w1ExGame2VeroRoseGallery:
                    play sound "sound effects/notification.wav"
                    show memoryunlock with dissolve
                    $ renpy.pause(3, hard=True)
                    $ persistent.w1ExGame2VeroRoseGallery = True
                    hide memoryunlock with dissolve
                    $ renpy.pause(0.5, hard=True)
                "Veronica had taken game number 2."
                $ renpy.end_replay()
                jump w1ExGame2Aftermath

            if w1ExShockPoints == 2:
                $ w1ExGame2WinnerRose = True
                $ w1ExGame2LoserVero = True
                play sound "sound effects/short-beep.wav"
                scene w1_3262 with dissolve
                show screen textbox2 with dissolve
                "Thinking I had gotten her attention with the last one, I gave the first option a press."
                play sound "sound effects/shock1.wav"
                scene w1_3269 with vpunch
                "*Bzzt!"
                mc "Veronica is going to win if you don't stand up right now!"
                scene w1_3270 with dissolve
                rose "Oh, shoot!"
                "Rosalind, in a state of panic, urgently leaped to her feet."
                scene w1_3271 with dissolve
                rose "*huff* *huff* Oooh, head rush..."
                rose "Uh, d-do I win?"
                scene black with fade
                if not persistent.w1ExGame2VeroRoseGallery:
                    play sound "sound effects/notification.wav"
                    show memoryunlock with dissolve
                    $ renpy.pause(3, hard=True)
                    $ persistent.w1ExGame2VeroRoseGallery = True
                    hide memoryunlock with dissolve
                    $ renpy.pause(0.5, hard=True)
                "Rosalind had secured game number 2."
                $ renpy.end_replay()
                jump w1ExGame2Aftermath

            if w1ExShockPoints == 3:
                $ w1ExGame2WinnerRose = True
                $ w1ExGame2LoserVero = True
                play sound "sound effects/short-beep.wav"
                scene w1_3262 with dissolve
                show screen textbox2 with dissolve
                "Seeing how fast she sprung up previously, I was hesitant to giving her another shock at the same power, so I opted to take it all the way down to low."
                play sound "sound effects/shock1.wav"
                scene w1_3269 with vpunch
                "*Bzzt!"
                scene w1_3268 with dissolve
                rose "Zzzzh, shoot! Ow, ow, ah! "
                scene w1_3269 with dissolve
                mc "Veronica is going to win if you don't stand up right now!"
                scene w1_3270 with dissolve
                rose "Oh, I need to...!"
                rose "Oh, shoot!"
                "Despite the pained look, it seemd Rosalind fully understood. In a state of panic, urgently leaped to her feet."
                scene w1_3271 with dissolve
                rose "*huff* *huff* Oooh, head rush..."
                rose "Uh, d-do I win?"
                scene black with fade
                if not persistent.w1ExGame2VeroRoseGallery:
                    play sound "sound effects/notification.wav"
                    show memoryunlock with dissolve
                    $ renpy.pause(3, hard=True)
                    $ persistent.w1ExGame2VeroRoseGallery = True
                    hide memoryunlock with dissolve
                    $ renpy.pause(0.5, hard=True)
                "Rosalind had secured game number 2."
                $ renpy.end_replay()
                jump w1ExGame2Aftermath


        "Hit the medium setting button. [gr]\[ShockPoints +2\]":
            if w1ExShockPoints == 1:
                $ w1ExGame2WinnerRose = True
                $ w1ExGame2LoserVero = True
                play sound "sound effects/short-beep.wav"
                scene w1_3263 with dissolve
                show screen textbox2 with dissolve
                "Not sure if another low setting shock would do it, I opted to move up a level."
                play sound "sound effects/shock2.wav"
                scene w1_3265 with vpunch
                "*Bzzt!"
                scene w1_3267 with dissolve
                rose "Eh..ow! Shoot!"
                "Almost instantly, Rosalind's collar gave a moderate buzz, returning the light to her eyes."
                scene w1_3269 with dissolve
                mc "Veronica is going to win if you don't stand up right now!"
                scene w1_3270 with dissolve
                rose "Eh, she... she is? Oh, shoot!"
                "Rosalind, in a state of panic, urgently leaped to her feet."
                scene w1_3271 with dissolve
                rose "*huff* *huff* Oooh, head rush..."
                rose "Uh, d-do I win?"
                scene black with fade
                if not persistent.w1ExGame2VeroRoseGallery:
                    play sound "sound effects/notification.wav"
                    show memoryunlock with dissolve
                    $ renpy.pause(3, hard=True)
                    $ persistent.w1ExGame2VeroRoseGallery = True
                    hide memoryunlock with dissolve
                    $ renpy.pause(0.5, hard=True)
                "Rosalind had secured game number 2."
                $ renpy.end_replay()
                jump w1ExGame2Aftermath


            if w1ExShockPoints == 2:
                $ w1ExGame2WinnerRose = True
                $ w1ExGame2LoserVero = True
                show screen textbox2 with dissolve
                play sound "sound effects/short-beep.wav"
                scene w1_3263 with dissolve
                "The medium option seemed effective, so I opted to give it another press."
                play sound "sound effects/shock2.wav"
                scene w1_3269 with vpunch
                "*Bzzt!"
                scene w1_3270 with dissolve
                rose "Eh..ow! Shoot!"
                "Almost instantly, Rosalind's collar gave a moderate buzz, the light fully returning to her eyes."
                mc "Veronica is going to win if you don't stand up right now!"
                rose "Oh shoot!"
                "Rosalind, in a state of panic, urgently leaped to her feet."
                scene w1_3271 with dissolve
                rose "*huff* *huff* Oooh, head rush..."
                rose "Uh, d-do I win?"
                scene black with fade
                if not persistent.w1ExGame2VeroRoseGallery:
                    play sound "sound effects/notification.wav"
                    show memoryunlock with dissolve
                    $ renpy.pause(3, hard=True)
                    $ persistent.w1ExGame2VeroRoseGallery = True
                    hide memoryunlock with dissolve
                    $ renpy.pause(0.5, hard=True)
                "Rosalind had secured game number 2."
                $ renpy.end_replay()
                jump w1ExGame2Aftermath


            if w1ExShockPoints == 3:
                $ w1ExGame2WinnerVero = True
                $ w1ExGame2LoserRose = True
                play sound "sound effects/short-beep.wav"
                scene w1_3263 with dissolve
                show screen textbox2 with dissolve
                "Seeing how distracted she seemed with the high option, I decided to take it down a level."
                play sound "sound effects/shock2.wav"
                scene w1_3269 with vpunch
                "*Bzzt!"
                scene w1_3268 with dissolve
                mc "Veronica is going to win if you don't stand up right now!"
                rose "Aw...! Ow...! Wait, w-what?"
                "Distracted by the pain, by the time she realized what was going on, it was too little, too late."
                scene w1_3272 with dissolve
                "Veronica had managed to prop herself up and stand on her own two feet."
                scene black with fade
                if not persistent.w1ExGame2VeroRoseGallery:
                    play sound "sound effects/notification.wav"
                    show memoryunlock with dissolve
                    $ renpy.pause(3, hard=True)
                    $ persistent.w1ExGame2VeroRoseGallery = True
                    hide memoryunlock with dissolve
                    $ renpy.pause(0.5, hard=True)
                ver "*huff* *huff* I... win?"
                $ renpy.end_replay()
                jump w1ExGame2Aftermath

        "Hit the high setting button. [gr]\[ShockPoints +3\]":

            if w1ExShockPoints == 1:
                $ w1ExGame2WinnerRose = True
                $ w1ExGame2LoserVero = True
                play sound "sound effects/short-beep.wav"
                scene w1_3264 with dissolve
                show screen textbox2 with dissolve
                "Worried that the low option didn't have an effect, I decided to try the opposite end, taking it all the way to high."
                scene w1_3265 with dissolve
                rose "Uh..."
                play sound "sound effects/shock3.wav"
                scene w1_3267 with vpunch
                "*Bzzt!"
                rose "Zzzzh, shoot! Ow, ow, ah! "
                scene w1_3269 with dissolve
                mc "Veronica is going to win if you don't stand up right now!"
                mc "Felicia's about to win if you don't stand up!"
                scene w1_3270 with dissolve
                rose "Oh, I need to...!"
                rose "Oh, shoot!"
                "Despite the pained look, it seemed Rosalind fully understood. In a state of panic, urgently leaped to her feet."
                scene w1_3271 with dissolve
                rose "*huff* *huff* Oooh, head rush..."
                rose "Uh, d-do I win?"
                scene black with fade
                if not persistent.w1ExGame2VeroRoseGallery:
                    play sound "sound effects/notification.wav"
                    show memoryunlock with dissolve
                    $ renpy.pause(3, hard=True)
                    $ persistent.w1ExGame2VeroRoseGallery = True
                    hide memoryunlock with dissolve
                    $ renpy.pause(0.5, hard=True)
                "Rosalind had secured game number 2."
                $ renpy.end_replay()
                jump w1ExGame2Aftermath


            if w1ExShockPoints == 2:
                $ w1ExGame2WinnerVero = True
                $ w1ExGame2LoserRose = True
                play sound "sound effects/short-beep.wav"
                scene w1_3264 with dissolve
                show screen textbox2 with dissolve
                "Seeing how effective the second option was, I decided that the third option should definitely do it."
                play sound "sound effects/shock2.wav"
                scene w1_3269 with vpunch
                "*Bzzt!"
                scene w1_3268 with dissolve
                mc "Veronica is going to win if you don't stand up right now!"
                rose "Aw...! Ow...! Ow, ow, ah! Wait, w-what?"
                "Distracted by the pain, by the time she realized what was going on, it was too little, too late."
                scene w1_3272 with dissolve
                "Veronica had managed to prop herself up and stand on her own two feet."
                scene black with fade
                if not persistent.w1ExGame2VeroRoseGallery:
                    play sound "sound effects/notification.wav"
                    show memoryunlock with dissolve
                    $ renpy.pause(3, hard=True)
                    $ persistent.w1ExGame2VeroRoseGallery = True
                    hide memoryunlock with dissolve
                    $ renpy.pause(0.5, hard=True)
                ver "*huff* *huff* I... win?"
                $ renpy.end_replay()
                jump w1ExGame2Aftermath

            if w1ExShockPoints == 3:
                $ w1ExGame2WinnerVero = True
                $ w1ExGame2LoserRose = True
                play sound "sound effects/short-beep.wav"
                scene w1_3264 with dissolve
                show screen textbox2 with dissolve
                "Seeing how fast she sprung up previously, I was sure another shock at that level would do it."
                play sound "sound effects/shock3.wav"
                scene w1_3269 with vpunch
                "*Bzzt!"
                scene w1_3268 with dissolve
                rose "Geee-h! Ow, ow, ow, OW!"
                mc "Veronica is going to win if you don't stand up right now!"
                rose "That frickin' stings!"
                "Instead of alerting her to what was going on, all she could focus on was the pain from the back-to-back shocks. So much so that..."
                scene w1_3272 with dissolve
                "Veronica had managed to prop herself up and stand on her own two feet."
                scene black with fade
                if not persistent.w1ExGame2VeroRoseGallery:
                    play sound "sound effects/notification.wav"
                    show memoryunlock with dissolve
                    $ renpy.pause(3, hard=True)
                    $ persistent.w1ExGame2VeroRoseGallery = True
                    hide memoryunlock with dissolve
                    $ renpy.pause(0.5, hard=True)
                ver "*huff* *huff* I... win?"
                $ renpy.end_replay()
                jump w1ExGame2Aftermath


label w1ExFollowThroughRoseFelStart:
    if _in_replay:
        show screen textbox2 with dissolve

    scene w1_3273 with curtains
    kat "Gentlemen, we are to begin! Allow me to explain the next game."
    "About twenty or so minutes after Hana had scurried back to the bar, game two was kicking off. Rosalind and Felicia had already taken their \"starting\" positions, ass to ass and down on their hands and knees at the center of the stage."
    scene w1_3274 with dissolve
    play music "music/myst-on-the-moor.mp3"

    if kat_polite == True:
        "A double-sided dildo rested between them, lewdly connecting the two women together at their honeypots. They were tasked with the uncomfortable prospect of awkwardly holding that position while Mrs. Pulman explained what was coming next."
    else:
        "A double-sided dildo rested between them, lewdly connecting the two women together at their honeypots. They were tasked with the uncomfortable prospect of awkwardly holding that position while Kathleen explained what was coming next."

    scene w1_3142 with dissolve
    kat "Our first game was about the first tenant of customer service. Exploring the needs of the customer."
    kat "Our second game will hone in on what I think of as the next: {b}actualization{/}. The art of the follow through."
    kat "In simplest terms, being able to keep focus on your task despite any roadblocks that might arise."
    scene w1_3143 with dissolve

    if kat_polite ==True:
        "Par for the course, Mrs. Pulman aggrandized what is otherwise just an excuse to perversely watch women squirm in discomfort."
    else:
        "Par for the course, Kathleen aggrandized what is otherwise just an excuse to perversely watch women squirm in discomfort."

    scene w1_3144 with dissolve
    kat "...and what will be the task? It's simple. You'll just need to shake your hips like the whores you are."
    kat "You two will fuck each other for all your worth. If you start slacking, the collars around your neck will provide a pick-me-up."
    scene w1_3227 with dissolve
    rose "Umm... what are you talking about? What kind of \"pick-me-up\"?"
    scene w1_3228 with dissolve
    kat "Simply put, it'll administer a brief shock that will jolt you back to your senses and get you moving again. If you don't get back to the task within 10 seconds, you'll be disqualified."
    scene w1_3275 with dissolve
    fel "Like an electrical shock...?"
    scene w1_3227 with dissolve
    rose "You're going to shock us? That's... scary..."
    scene w1_3228 with dissolve
    kat "Don't get bent out of shape. It's nothing dangerous for a healthy adult woman. It's more akin to a dog's training collar, but adjusted for a dumb cow like you."
    scene w1_3229 with dissolve
    rose "..."
    "Rosalind looks uncomfortable for a brief moment, but she quickly steeled herself."
    hide screen textbox2 with dissolve
    scene w1_3276 with dissolve
    kat "If either of you find the prospect unappealing, one of you can always resign and move onto the last game by your lonesome."
    scene w1_3277 with dissolve
    fel "No, I'm game. Let's do it!"
    rose "...I'll do whatever you ask."
    scene w1_3278 with dissolve
    kat "Good. I thought so. That's not all there is to this game though. You'll also be asked some questions."
    scene w1_3154 with dissolve
    show screen textbox2 with dissolve
    kat "Simple, basic things that any woman your age should be able to answer. A wrong or delayed answer will make things more difficult for you."
    scene w1_3155 with dissolve
    kat "Do you two understand the parameters of this game?"
    scene w1_3156 with dissolve
    rose "Yes, Mrs. Pulman."
    fel "Yes, ma'am!"
    scene w1_3157 with dissolve
    kat "Mr. [mcl]! Mr. Beaufort! You'll be charged with administering the shocks. You've familiarized yourself with the remote control I've given you?"
    scene w1_3158 with dissolve
    kil "Yup!"
    mc "I think so."
    scene w1_3157 with dissolve
    kat "It's very simple. There's three settings. Each corresponds to a low, medium, and high powered shock. I'll leave it to your discretion what you feel is appropriate."
    mct "(Is this part of the test she mentioned...?)"
    kat "Mr. [mcl]'s remote is synced with Mrs. Ford's collar. Mr. Beaufort's is synced to Mrs Carter's."

label w1ExFollowThroughRoseFel:

    scene w1_3159 with dissolve
    kat "Now, enough talking. Let's get to why all you gentlemen are really here. On the count of three, I want you to start fucking each other like your future depends on it."
    stop music fadeout 3.0
    scene w1_3160 with dissolve
    kat "Three..."
    scene w1_3161 with dissolve
    kat "Two..."
    scene w1_3162 with dissolve
    kat "One..."
    scene w1_3163 with dissolve
    image rosefeldil1= Movie(play="rosefeldil1.webm")
    image rosefeldil2= Movie(play="rosefeldil2.webm")
    image rosefeldil3= Movie(play="rosefeldil3.webm")
    image rosefeldil4= Movie(play="rosefeldil4.webm")
    image rosefeldil5= Movie(play="rosefeldil5.webm")
    image rosefeldil6= Movie(play="rosefeldil6.webm")
    image rosefeldil7= Movie(play="rosefeldil7.webm")
    kat "Begin, whores!"
    play music "music/guiton-sketch.mp3"
    show rosefeldil1 with dissolve
    "Cutting through the air with an enthusiastic chop, she signaled for the two Carnations to begin the trial."
    "Felicia didn't hesitate. She hurled herself ass first, drawing her body back until her rear collided with Rosalind's with a rippling impact."
    "Rosalind on the other hand took a more tentative approach, blindly using her hips to slowly feel out the mechanics of the act."
    "Felicia seemed unconcerned with matching her opponent's pace, haphazardly bucking her hips and threatening to dislodge the golden toy that connected them."
    "Through sheer luck, the toy managed to stay sheathed in their quims. Both women pushed back and forward, sliding themselves off and revealing more and more of the dildo before disappearing once more into the women's depths."
    "It was like an awkward dance. On paper it might sound simple, but the reality was each Rosalind was struggling to find the appropriate rhythm that would make it easier for the both of them."
    kat "Very good, girls."
    "Felicia lurched forward at such a depth that the dildo almost slipped out from in between them, but a panicking Rosalind quickly overcorrected and brought her ass crashing back into the golden beauty's, causing the whore mother's gelatinous behind to quake."
    kat "Keep those hips moving and those asses shaking. It's one of the few things you're good for."
    scene rosefeldil4 with dissolve
    hide rosefeldil1
    "Eventually the two settled found a workable rhythm, moving in tandem like some perverted seesaw."
    "Each concentrated on keeping their hips unceasingly moving and the sex-toy lodged in their cunts."
    "No thanks to Felicia, eventually the two settled into a workable rhythm, moving in tandem like some perverted seesaw."
    "Rosalind bore an uncomfortable look on her face, concentrating on keeping her hips unceasingly moving and the sex-toy lodged in their cunts."
    "Felicia, on the other hand, was enjoying it. Eyes tightly shut and lips brimming with a smile."
    scene rosefeldil1 with dissolve
    fel "You've got such a plump ass, Rosie! It bet we look delicious right now!"
    "Seemingly unconcerned with the potential outcome of the game itself, Felicia offhandly gave Rosalind a bizarre compliment."
    kat "It's obscene is what it is. "
    rose "W-why don't you just -ah!- focus on what you're doing instead of worrying about my behind?"
    fel "Ah, c'mon! How can you hope to win if you don't find just a little enjoyment in this?"
    rose "Enjoyment?! Don't be..."
    scene rosefeldil4 with dissolve
    "Taking offense to the capricious woman's candor, Rosalind squared her shoulders and forecfully bucked her hips. Sleaving and unsheathing herself from the toy with a stronger intensity than before."
    "For whatever reason, Felicia seemed to have gotten under her skin - which was no wonder, when you consider their drastically different circumstances."
    "To Rosalind, this was no romp or game."
    "*Plap* *Smack* *Slap!*"
    fel "Oh..! Ah...!"
    "*Plap* *Smack* *Slap* *Smack!* *Plap!* *Slap!*"

    fel "You sure know how to fuck, Rose!"
    kat "What a surprise. I didn't expect Mrs. Carter to take the initiative."
    rose "I'm going to win this!"
    scene w1_3165 with dissolve
    kat "You are? Well then, give these gentlemen a fine show! Make that fat ass of yours bounce!"
    scene w1_3166 with dissolve
    kat "However, let's make things more interesting."
    scene w1_3167 with dissolve
    kat "Hmmm-mmmh~hmmm~ Let's see...    "
    kat "You girls know your multiplication tables...?"

    if kat_polite:
        "Having gone over to one of the nearby tables, Mrs. Pulman carefully considered her options while posing an odd question."
    else:
        "Having gone over to one of the nearby tables, Kathleen carefully considered her options while posing an odd question."

    scene w1_3168 with dissolve
    "Neither women deigned to answer her question, instead focusing on keeping their hips bouncing at a furious pace."
    scene w1_3169 with dissolve
    kat "Let's get things rolling. We'll start with..."
    scene w1_3170 with dissolve
    kat "Mrs. Ford"
    hide screen textbox2 with dissolve
    scene rosefeldil2 with dissolve
    fel "Start with what?"
    kat "Answer quickly. What is thirteen times twelve?"
    fel "Wait, you seriously want me to do math?"
    kat "Five, four, three, two..."
    fel "Uh... 156!"
    kat "Correct. Mrs. Carter: fourteen times eight?"
    scene rosefeldil3 with dissolve
    rose "Wait... eh... 96... 104.. 112!"
    kat "Correct!"
    rose "Why are you--"
    scene rosefeldil4 with dissolve
    show screen textbox2 with dissolve
    kat "Felicia! Thirteen times seven?"
    fel "Nine-ninty one?"

    if kat_polite == True:
        "All the while the two pumped their hips, the Carnations went back and forth answering Mrs. Pulman's questions."
    else:
        "All the while the two pumped their hips, the Carnations went back and forth answering Kathleen's questions."

    rose "168!"
    fel "112!"
    rose "182!"
    hide screen textbox2 with dissolve
    scene w1_3279 with dissolve
    kat "Oops, sorry! The answer was 196! Mrs. Carter takes the first hit."
    rose "The first hit...?"
    "Rosalind looked anxious at the ominous words."
    scene w1_3280 with dissolve
    rose "Gh! Wh-wha-"
    scene w1_3281 with vpunch
    rose "Eeee-wh-what!"

    if kat_polite == True:
        "Finding a window of opportunity while the pair was separating, Mrs. Pulman shoved a prickly golf ball sized sphere into Rosalind's tight tailhole."
    else:
        "Finding a window of opportunity while the pair was separating, Mrs. Kathleen shoved a prickly golf ball sized sphere into Rosalind's tight tailhole."

    scene w1_3282 with dissolve
    rose "Ehf... gah!"
    "The reaction was immediate. As the pair's backsides smacked together, a look of sudden discomfort flooded the whore mother's face."
    rose "Did you just-!"
    scene w1_3281 with vpunch
    rose "Mmmmhm-aah!"
    "Every time Rosalind's plump ass collided with Felicia's firm backside, she reeled from the pink toy sliding around her colon and let out a delectable, shrill cry."
    scene w1_3282 with dissolve
    fel "What just happened? Why is she making those noises?"
    kat "Do you mean why is she squealing like a dumb whore?"
    scene w1_3281 with vpunch
    rose "My.. butt! My buUuUutt! I've never...!"
    scene w1_3283 with dissolve
    play sound "sound effects/slap2.wav"
    scene w1_3284 with vpunch
    "*{b}Smack!!!{/b}*"
    rose "Tcckkk---! Fghggh---!"
    scene w1_3283 with dissolve
    kat "Don't tell me you've never had anything shoved in your shithole?"
    play sound "sound effects/slap2.wav"
    scene w1_3284 with vpunch
    "*{b}Smack!!!{/b}*"
    rose "Ayahhh-gheh!"
    scene w1_3154 with dissolve
    show screen textbox2 with dissolve
    kat "Wonderful. We have our very own anal newbie in our midst tonight, gentlemen."
    kat "You're going to learn quick. I promise you'll be crying out like a seasoned buttslut by the end of this."
    scene w1_3156 with dissolve
    rose "Ehehe...!"
    scene w1_3155 with dissolve
    kat "Mrs. Ford, back to you..."
    hide screen textbox2 with dissolve
    scene rosefeldil2 with dissolve
    fel "M-more math? What are you going to do to me if I get the answer wrong?"
    kat "What is sixteen times fourteen"
    "For the first time, the unknown punishment had Felicia at least looking moderately concerned."
    kat "Five, four, three..."
    fel "Wait, that's not fair. No one can answer that in..."
    scene w1_3285 with dissolve
    kat "One... times up!"
    fel "Ah, shit..."
    scene w1_3286 with dissolve
    fel "Ffuh...?! W-what--"
    scene w1_3287 with vpunch
    fel "Geh! Ffhu...!"
    "Felicia reacted as Rosalind had, with total and complete shock at the strange sensation."
    scene w1_3288 with dissolve
    fel "Ahh... fuck! W-warn a girl-before you...!"
    scene w1_3287 with dissolve
    fel "What did you just stick up my butt? It feels...!"
    kat "It's just a little toy to make things more interesting."
    scene w1_3288 with vpunch
    fel "Guh! Eehehe...!"
    rose "OoooOOoooooh!"
    "The pair practically harmonized, squealing in unison and creating a wonderful sound."
    scene w1_3181 with dissolve
    show screen textbox2 with dissolve
    kat "Mrs. Cater. Nineteen times sixty three..."
    rose "Oh, no..."
    scene w1_3182 with dissolve

    if kat_polite == True:
        "The girls did their best to answer Mrs. Pulman's questions, but one by one the balls began to disappear in equal measure."
    else:
        "The girls did their best to answer Kathleen's questions, but one by one the balls began to disappear in equal measure."

    scene w1_3183 with dissolve
    "Two for Rosalind..."
    scene w1_3184 with dissolve
    "Three for Felicia... three for Rosalind."
    scene w1_3185 with dissolve
    "By the time they'd all disappeared, the spike-lined balls had been equally split between the Carnations and were now freely rattling around the girl's buttholes. Exactly how I imagined our cruel ringleader had devised it."
    play sound "sound effects/slap2.wav"
    pause 0.5
    play sound "sound effects/slap2.wav"
    pause 0.5
    play sound "sound effects/slap2.wav"
    "*{b}Smack{/b}* *{b}Smack{/b}!* *{b}Smack{/b}-!!*"
    rose "Onnn- oh, gghuu!"
    fel "Geh-! S-stop hitting me! It feels weeeeeeeeird!"
    scene w1_3297 with dissolve
    "At this point, both women were howling in a confuddled mix of pain and pleasure."

    if kat_polite == True:
        "Each swat of the paddle in Mrs. Pulman's grip sent each of their wide asses quaking, knocking the ribbed pink toys against each other and scraping the lining of their bowels."
    else:
        "Each swat of the paddle in Kathleen's grip sent each of their wide asses quaking, knocking the ribbed pink toys against each other and scraping the lining of their bowels."

    "The pervert in me had to hand it to her. It was a simple approach, but the results were etched into the pair's enraptured faces."
    kat "Remember the aim of the game: soldier through the sensation. Keep fucking each other until you drop."
    scene w1_3289 with quickdissolve
    scene w1_3290 with quickdissolve
    play sound "sound effects/slap2.wav"
    scene w1_3291 with vpunch
    "*{b}Slap!{/b}*"
    rose "Geh-oh-gh-oh!"
    scene w1_3293 with quickdissolve
    scene w1_3294 with quickdissolve
    play sound "sound effects/slap2.wav"
    scene w1_3295 with vpunch
    "*{b}Slap!{/b}*"
    scene w1_3187 with dissolve
    kat "Not your first time being double stuffed, is it Felicia?"
    scene w1_3188 with dissolve
    fel "Eeeh, ye-no, n-no it is! I mean, only with toys...!"
    scene w1_3187 with dissolve
    kat "Really? I figured a woman like you would be more experienced in that area."
    scene w1_3293 with quickdissolve
    scene w1_3294 with quickdissolve
    play sound "sound effects/slap2.wav"
    scene w1_3295 with vpunch
    "*{b}Slap!{/b}*"
    fel "Ooowowooooo~ehg, they're moving around in my buuuutt!"
    scene w1_3289 with quickdissolve
    scene w1_3290 with quickdissolve
    play sound "sound effects/slap2.wav"
    scene w1_3291 with vpunch
    "*{b}Slap!{/b}*"
    rose "Ohh... oh! Mercy! Mercy!"
    scene w1_3190 with dissolve
    kat "You want mercy, you stupid slut?!"
    scene w1_3189 with dissolve
    rose "Yes!"

    if kat_polite == True:
        "Mrs. Pulman split her efforts between the two carnations, given each ass an energetic wallop."
    else:
        "Kathleen split her efforts between the two carnations, given each ass an energetic wallop."

    scene w1_3293 with quickdissolve
    scene w1_3294 with quickdissolve
    play sound "sound effects/slap2.wav"
    scene w1_3295 with vpunch
    "*{b}Slap!{/b}*"
    fel "Ooowowooooo~ehg, s-shit!"
    scene w1_3289 with quickdissolve
    scene w1_3290 with quickdissolve
    play sound "sound effects/slap2.wav"
    scene w1_3291 with vpunch
    "*{b}Slap!{/b}*"
    rose "M-Mercy!"
    hide screen textbox2 with dissolve
    scene rosefeldil6 with dissolve
    "Felicia didn't have the benefit of a fat ass to dull the impact of the blows. She was feeling the treatment more acutely and it showed."
    "She was going cross-eyed, from the toy drilling her cunt and the sensation of toys rattling around her anus."
    kat "I should remember that you have an extra-sensitive anus. That could come in handy later."
    scene w1_3293 with quickdissolve
    scene w1_3294 with quickdissolve
    play sound "sound effects/slap2.wav"
    scene w1_3295 with vpunch
    show screen textbox2 with dissolve
    "*{b}Slap!{/b}*"
    scene w1_3294 with dissolve
    scene w1_3293 with dissolve
    fel "EeeeeEh, f-fu-"
    scene w1_3293 with quickdissolve
    scene w1_3294 with quickdissolve
    play sound "sound effects/slap2.wav"
    scene w1_3295 with vpunch
    "*{b}Smack!{/b}*"
    scene w1_3187 with dissolve
    kat "There it is! I was waiting to see your face twisted up like a perverted bitch! You're taking this place much too lightly."
    kat "I'm going to teach you many wonderful things, dear! Now cum!"
    scene w1_3293 with quickdissolve
    scene w1_3294 with quickdissolve
    play sound "sound effects/slap2.wav"
    scene w1_3295 with vpunch
    "*{b}Slap!{/b}*"
    fel "EeEeeeeeeeeeeeeeh!" with vpunch
    "With a violent cry, Felicia arched her back and tightly shut her eyes in abject pleasure."
    scene w1_3296 with flash
    fel "OooOooooOooh~oooh...ehehe...♥" with vpunch
    kat "Ha! Did you cum from your pussy or your ass?"
    "Felicia stumbled forward slightly and her orgasm dulled her previous energy, but she kept to task. Never stopping working in tandem with Veronica's bucking hips."
    hide screen textbox2 with dissolve
    scene rosefeldil7 with dissolve
    "At the other end of things, Rosalind was looking haggard herself. Hips hips followed a more erractic rhythm and it looked like she wasn't too far behind Felicia."
    rose "Eh-heh... t-this feels good?"
    kat "It does indeed, you masochistic cow!"
    scene w1_3289 with quickdissolve
    scene w1_3290 with quickdissolve
    play sound "sound effects/slap2.wav"
    scene w1_3291 with vpunch
    show screen textbox2 with dissolve
    "*{b}Slap!{/b}*"
    rose "Geheh!!!"
    scene w1_3290 with dissolve
    scene w1_3289 with dissolve
    kat "You fat ass slut!"
    scene w1_3290 with quickdissolve
    play sound "sound effects/slap2.wav"
    scene w1_3291 with vpunch
    rose "Ng! Merc-eeeeeeeh...!!! I'm going to...!"
    scene w1_3290 with dissolve
    scene w1_3289 with dissolve
    kat "Cum for me!"
    scene w1_3290 with quickdissolve
    play sound "sound effects/slap2.wav"
    scene w1_3291 with vpunch
    "*{b}Slap!{/b}*"
    "One final slap sent Rosalind over the edge, causing her to arch her back and call out with a violent, pleasured cry."
    scene w1_3292 with flash
    rose "Ffghhhhheeeee!...ehehe... hehe...!"
    kat "Ha! That was fast! You came from having your fat ass battered. You're a fucking natural!"

    if kat_polite == True:
        "Mrs. Pulman cackled in delight, pleased at the miserable display in front of her."
    else:
        "Kathleen cackled in delight, pleased at the miserable display in front of her."

    rose "Eheh... heh... eheh... woah..."

    "She had managed to quickly bring both women to orgasm. It was honestly impressive in a fucked up way."
    kat "Don't think this is over though. Don't stop moving, there's more to come!"
    scene w1_3196 with dissolve
    mc "They're unbelievable..."
    scene w1_3197 with dissolve
    kil "Shit, this is good..."
    scene w1_3198 with dissolve
    kat "This time you have 30 seconds to answer."
    fel "We're not done with the questions?"
    kat "No. Not until one of you yields. Mrs. Carter..."
    scene w1_3199 with dissolve
    kat "I have a riddle for you, are you listening?"
    hide screen textbox2 with dissolve
    scene rosefeldil3 with dissolve
    rose "Geeh, yes! What is it?"
    kat "Good! Here it is: \"Without it, I'm dead. If I'm not, then I'm behind. What am I?\"."
    rose "Uh... oh, s-shoot...!"
    "In between her impassioned criesm a sliver of panic snuck onto Rosalond's face."
    rose "Uh, crap... I don't know."
    "Instead of waiting out the time, Rosalind just admitted the inevitable."
    rose "Just get whatever you're going to do over with, okay?"
    kat "You give up?"
    rose "Yes."
    kat "{b}Fantastic{/b}."
    kat "The answer I was looking for was \"ahead\"."
    scene rosefeldil2 with dissolve
    kat "Your turn, Mrs. Ford. What has a head and a tail, but no body?"
    fel "Head... tail.... oh!"
    fel "A coin?"
    kat "Correct. Very good! That was surprisingly quick."
    kat "Now..."
    play sound "sound effects/vib-start.wav"
    scene w1_3310 with hpunch
    "*Bzzzzt!*"
    "Like with the balls, the cruel woman slipped the newly fetched toy - an anal vibrator - smoothly into the mother's winking pucker and turned it on."
    rose "Mmmmn~eeh, zzzzzz-zah... fhug...zzz!!!"
    "The vibrating rod being shoved mercilessly into her crowded tail hole produced a garbled slew of intelligibly whorish moans."
    kat "Haha, how do you like that?"
    scene rosefeldil7 with dissolve
    rose "The v-v-v-v-ibrationzzz...! Gh!"
    kat "I know, right? In such a tight space, it's making the studded eggs vibrate along with it. You can feel those vibrations all the way into your stomach and into your chest."
    rose "Y-ngh, mmg-zzzaaa!"
    kat "I'm very glad you got my riddle wrong."
    kat "For a woman who's an anal virgin, this kind of stimulation could just drive you mad."
    rose "Zzhaaa- eh, ohohOhOHOH!"
    kat "What sweet, sweet music."
    kat "I wonder what your wayward husband would think to hear you howling like an animal? He'd probably be glad he up and disappeared."
    rose "N-no!"
    scene rosefeldil5 with dissolve
    show screen textbox2 with dissolve
    kat "Don't deny it. I mean look at how you're shaking your hips? Haven't you noticed you've been doing it harder ever since I inserted that vibrator?"
    kat "Deep down you're a slut. It's just lucky you found your way here, so you can finally be yourself."
    rose "A-ah! That's not true!"
    kat "It is. You can't deny it. At some level, you're enjoying yourself. It's freeing, isn't it?"
    kat "Under the spot light, you can forget who you are and your miserable life."
    rose "{b}S-shut up! I love my life!{/b}"
    "Rosalind cried out and shouted at the cruel old woman, sucking our noise out of the hall."
    rose "Oh..."

    if kat_polite == True:
        "Rosalind looked fearful over her outburst, but Mrs. Pulman merely smiled."
    else:
        "Rosalind looked fearful over her outburst, but Kathleen merely smiled."
    hide screen textbox2 with dissolve
    scene rosefeldil7 with dissolve
    kat "So, you wouldn't trade it for all the pleasure in the world?"
    rose "No."
    kat "Ha! I guess we'll see."

    if kat_polite == True:
        "Even with the additional discomfort and Mrs. Pulman teasing her, Rosalind continued to match Felicia's pace, moving her hips at a furious pace and drilling herself on the golden dildo."
    else:
        "Even with the additional discomfort and Kathleen teasing her, Rosalind continued to match Felicia's pace, moving her hips at a furious pace and drilling herself on the golden dildo."
    scene rosefeldil5 with dissolve
    show screen textbox2 with dissolve
    "The sight made me think Mrs. Pulman wasn't entirely off base about Rosalind enjoying it on some level. From where I sat, it looked like the woman at least had something of an exhibitionist streak."
    "She was in the midst of pure sexual arousal. It wasn't just the goal of winning the competition that was driving her hips, it was also needy, craven desire."
    hide screen textbox2 with dissolve
    scene rosefeldil6 with dissolve
    "Her opponent was looking much of the same. Felicia's was looking like a mess."
    scene rosefeldil5 with dissolve
    show screen textbox2 with dissolve
    "Incredibly the scene carried on for minutes more, Felicia being rocked by numerous mini-orgasms, but still managing to hang on."
    "It was a marvellous sight. The two women sweating profusely, squirming in ecstasy, loose strands of hair matting the napes of the neck."
    "The room was completely quite."
    "Even our cruel ringleader shut the fuck up for once, instead letting the near silent room be filled with the dirty sounds of copulation and ragged breathing."
    "In this moment, I was utterly divorced from my regular life. [mcf] was just a name at the back of my head and his worries seemed so trite."
    rose "Eh... eh..!"
    scene w1_3298 with vpunch
    rose "Ooofffhhooooo-! Oh, gh- I'm-- Ghhhg... fhuu... ghw..."
    "I watched Rosalind's expression go cross, her vocal cords letting out a shrill, banshee like screech that announced her impeding orgasm."
    fel "Geggggeh--!" with vpunch
    kat "I can't believe--"
    scene w1_3299 with vpunch
    fel "Geeeh, fu-again?! My AasaassssSSssss.... es... numb...!"
    fel "Fggg-ooOooooooooo!" with vpunch
    "Following Rosalind's example, Felicia soon came again herself, letting out an incoherent mess of babbling and swearing as she did."
    kat "You too? My, my. You {i}really{/i} do have a sensitive asshole, don't you?"
    kat "Once you pop, you just can't stop."
    play sound "sound effects/thud-floor.mp3"
    scene w1_3300 with vpunch
    "*{b}Thud!{/b}*"
    "In an instant, the flurry of sex just ceased."
    "Both Carnations gave out, flopping down on the cushioned surface. They weren't unconscious, but their legs had turned to jelly and their minds to mush."
    kat "It looks like both these fuck pigs are out. I wonder, will we be lucky enough to have a game of sudden death? Hmpfhf... no, no..."
    "The ten seconds passed."
    kat "How about this? The first whore to get on her feet and take a bow wins."
    scene w1_3204 with dissolve
    kat "Lend the girls a hand, boys."
    scene w1_3205 with dissolve
    mc "Oh...?"
    play music "music/doll-dancing.mp3"
    play sound "sound effects/shock2.wav"
    scene w1_3265 with vpunch
    "*Bzzt!"
    scene w1_3266 with dissolve
    "Rosalind suddenly tensed up, her pale legs straightening out from a sudden zap from her collar."
    kil "C'mon! Get up, Rose!"
    "In contrast to the jolt he just gave her, Ian called out words of encouragement to get the slumped over mother to her feet."
    play sound "sound effects/shock2.wav"
    scene w1_3267 with vpunch
    "*Bzzt!"
    kil "You gotta stand up if you wanna win!"
    scene w1_3269 with dissolve
    rose "Ah, oh... what? I need to...?"
    play sound "sound effects/shock2.wav"
    scene w1_3268 with vpunch
    "*Bzzt!"
    rose "Gh--! Crap, that stings!"
    "Rosalind made the first move in the battle to stand up, while Felicia still hadn't regained her senses."
    scene w1_3209 with dissolve
    mct "(Oh, shit... right!)"
    "I held in my hand a remote control to the shock collar around her neck, tasked with the dubious responsibility of providing encouragement to the down and out beauty."
    "I looked down at the phone in my hand, unsure about what to do."
    hide screen textbox2 with dissolve

    menu:
        "Hit the low setting button. [gr]\[ShockPoints +1\]":
            $ w1ExShockPoints +=1

            play sound "sound effects/short-beep.wav"
            scene w1_3210 with dissolve
            show screen textbox2 with dissolve
            "Not wanting to hurt Felicia, my thumb reflexively moved to the top option."
            play sound "sound effects/shock1.wav"
            scene w1_3301 with vpunch
            "*Bzzt!"
            scene w1_3302 with dissolve
            fel "Eh...?"
            "Almost instantly, Felicia's collar gave a slight buzz, causing the collapsed woman to stir slightly."
            mc "Felicia! You need to stand up!"
            play sound "sound effects/shock1.wav"
            "*Bzzt!" with vpunch
            mc "You'll lose if you don't!"
            play sound "sound effects/shock1.wav"
            "*Bzzt!" with vpunch

            if toughness > 20:
                mc "Stand the fuck up, girl!"
            else:
                mc "Can't you hear me?"

            "I called out, hoping to get through to her, but to no avail."
            "Rosalind, meanwhile was in the process of standing up. If I didn't do something, Felicia was about to lose game #2 and move onto the final one."
            "Then again, what does it matter to me who wins...?"
            hide screen textbox2 with dissolve
            scene w1_3209 with dissolve
            jump w1ExFollowThroughFelShock

        "Hit the medium setting button. [gr]\[ShockPoints +2\]":
            $ w1ExShockPoints +=2

            play sound "sound effects/short-beep.wav"
            scene w1_3211 with dissolve
            show screen textbox2 with dissolve
            "Wanting her to get up, but too scared to press the high setting, my thumb reflexively moved to the middle option."
            play sound "sound effects/shock2.wav"
            scene w1_3301 with vpunch
            "*Bzzt!"
            scene w1_3302 with dissolve
            fel "Eh... shit! What the-?"
            "Almost instantly, Rosalind's collar gave a moderate buzz, causing the woman to stir."
            play sound "sound effects/shock2.wav"
            scene w1_3304 with vpunch
            "*Bzzt!"
            scene w1_3306 with dissolve
            mc "Felicia! You need to stand up! You'll lose if you don't!"
            fel "Huh, what are you talking about?"

            if toughness > 20:
                mc "Stand the fuck up, girl!"
            else:
                mc "Stand up!"

            "Rosalind, meanwhile was in the process of standing up. If I didn't do something, Felicia was about to lose game #2 and move onto the final one."
            "Then again, what does it matter to me who wins...?"
            hide screen textbox2 with dissolve
            scene w1_3209 with dissolve
            jump w1ExFollowThroughFelShock

        "Hit the high setting button. [gr]\[ShockPoints +3\]":
            $ w1ExShockPoints +=3

            play sound "sound effects/short-beep.wav"
            scene w1_3212 with dissolve
            show screen textbox2 with dissolve
            "Wanting her to get up, or just curious about what it'd do, my thumb reflexively moved to the bottom option."
            play sound "sound effects/shock3.wav"
            scene w1_3301 with vpunch
            "*Bzzt!"
            scene w1_3304 with dissolve
            fel "Eh..ooOooooh? Fuck! What the sh-?"

            "Almost instantly, Felicia's collar gave a distinct buzz, causing her to spring straight up from her stupor."
            scene w1_3306 with dissolve
            mc "Felicia! You need to stand up!"
            fel "Grh, that hurts!"
            mc "You'll lose if you don't!"
            "Rosalind, meanwhile was in the process of standing up. If I didn't do something, Felicia was about to lose game #2 and move onto the final one."
            "Then again, what does it matter to me who wins...?"
            hide screen textbox2 with dissolve
            scene w1_3209 with dissolve
            jump w1ExFollowThroughFelShock

    menu w1ExFollowThroughFelShock:
        mod "For Rosalind Win: ShockPoints == 2, 5 or 6\nFor Felicia Win: ShockPoints == 3 or 4"
        "Hit the low setting button. [gr]\[ShockPoints +1\]":

            if w1ExShockPoints == 1:
                $ w1ExGame2WinnerRose = True
                $ w1ExGame2LoserFel = True
                play sound "sound effects/short-beep.wav"
                scene w1_3210 with dissolve
                show screen textbox2 with dissolve
                "Still hesitant about harming her, I gave the first option a second press."
                play sound "sound effects/shock1.wav"
                scene w1_3302 with vpunch
                "*Bzzt!"
                mc "Rosalind is going to win if you don't stand up right now!"
                scene w1_3306 with dissolve
                fel "Eh... huh...?"
                "By the time she had fully grasped the situation, it was too little, too late."
                scene w1_3308 with dissolve
                "Rosalind had managed to prop herself up and stand on her own two feet."
                rose "I'm up! Does that mean...?"
                scene black with fade
                if not persistent.w1ExGame2RoseFelGallery:
                    play sound "sound effects/notification.wav"
                    show memoryunlock with dissolve
                    $ renpy.pause(3, hard=True)
                    $ persistent.w1ExGame2RoseFelGallery = True
                    hide memoryunlock with dissolve
                    $ renpy.pause(0.5, hard=True)
                "Rosalind had taken game number 2."
                $ renpy.end_replay()
                jump w1ExGame2Aftermath

            if w1ExShockPoints == 2:
                $ w1ExGame2WinnerFel = True
                $ w1ExGame2LoserRose = True
                play sound "sound effects/short-beep.wav"
                scene w1_3210 with dissolve
                show screen textbox2 with dissolve
                "Thinking I had gotten her attention with the last one, I gave the first option a press."
                play sound "sound effects/shock1.wav"
                scene w1_3307 with vpunch
                "*Bzzt!"
                mc "Rosalind is going to win if you don't stand up right now!"
                fel "Ah, right!"
                scene w1_3309 with dissolve
                "Felicia, fully understanding what was going on, suddenly leapt up on her long, toned legs."
                fel "I win!"
                scene black with fade
                if not persistent.w1ExGame2RoseFelGallery:
                    play sound "sound effects/notification.wav"
                    show memoryunlock with dissolve
                    $ renpy.pause(3, hard=True)
                    $ persistent.w1ExGame2RoseFelGallery = True
                    hide memoryunlock with dissolve
                    $ renpy.pause(0.5, hard=True)
                "Felicia had secured game number 2."
                $ renpy.end_replay()
                jump w1ExGame2Aftermath

            if w1ExShockPoints == 3:
                $ w1ExGame2WinnerFel = True
                $ w1ExGame2LoserRose = True
                play sound "sound effects/short-beep.wav"
                scene w1_3210 with dissolve
                show screen textbox2 with dissolve
                "Seeing how fast she sprung up previously, I was hesitant to giving her another shock at the same power, so I opted to take it all the way down to low."
                play sound "sound effects/shock1.wav"
                scene w1_3304 with vpunch
                "*Bzzt!"
                scene w1_3303 with dissolve
                fel "Eh, what?"
                mc "Rosalind is going to win if you don't stand up right now!"
                rose "Oh, I need to...!"
                scene w1_3309 with dissolve
                "Despite the pained look, it seemed Felicia fully understood. With a burse of energy, she leapt up on her long, toned legs."
                fel "I win! ...right?"
                scene black with fade
                if not persistent.w1ExGame2RoseFelGallery:
                    play sound "sound effects/notification.wav"
                    show memoryunlock with dissolve
                    $ renpy.pause(3, hard=True)
                    $ persistent.w1ExGame2RoseFelGallery = True
                    hide memoryunlock with dissolve
                    $ renpy.pause(0.5, hard=True)
                "Felicia had secured game number 2."
                $ renpy.end_replay()
                jump w1ExGame2Aftermath


        "Hit the medium setting button. [gr]\[ShockPoints +2\]":
            if w1ExShockPoints == 1:
                $ w1ExGame2WinnerFel = True
                $ w1ExGame2LoserRose = True
                play sound "sound effects/short-beep.wav"
                scene w1_3211 with dissolve
                show screen textbox2 with dissolve
                "Not sure if another low setting shock would do it, I opted to move up a level."
                play sound "sound effects/shock2.wav"
                scene w1_3302 with vpunch
                "*Bzzt!"
                scene w1_3303 with dissolve
                fel "Eh, oh- what?"
                "Almost instantly, Felicia's collar gave a moderate buzz, returning the light to her eyes."
                mc "Rosalind is going to win if you don't stand up right now!"
                fel "Oh, I need to...!"
                scene w1_3309 with dissolve
                "Despite the pained look, it seemed Felicia fully understood. With a burse of energy, she leapt up on her long, toned legs."
                fel "I win! ...right?"
                scene black with fade
                if not persistent.w1ExGame2RoseFelGallery:
                    play sound "sound effects/notification.wav"
                    show memoryunlock with dissolve
                    $ renpy.pause(3, hard=True)
                    $ persistent.w1ExGame2RoseFelGallery = True
                    hide memoryunlock with dissolve
                    $ renpy.pause(0.5, hard=True)
                "Felicia had secured game number 2."
                $ renpy.end_replay()
                jump w1ExGame2Aftermath


            if w1ExShockPoints == 2:
                $ w1ExGame2WinnerFel = True
                $ w1ExGame2LoserRose = True
                play sound "sound effects/short-beep.wav"
                scene w1_3211 with dissolve
                show screen textbox2 with dissolve
                "The medium option seemed effective, so I opted to give it another press."
                play sound "sound effects/shock2.wav"
                scene w1_3304 with vpunch
                "*Bzzt!"
                scene w1_3305 with dissolve
                fel "Eg-! That hurts!"
                "Almost instantly, Rosalind's collar gave a moderate buzz, causing her to wince."
                scene w1_3307 with dissolve
                mc "Rosalind is going to win if you don't stand up right now!"
                fel "Oh, I need to...!"
                scene w1_3309 with dissolve
                "Despite the pained look, it seemed Felicia fully understood. With a burse of energy, she leapt up on her long, toned legs."
                fel "I win! ...right?"
                scene black with fade
                if not persistent.w1ExGame2RoseFelGallery:
                    play sound "sound effects/notification.wav"
                    show memoryunlock with dissolve
                    $ renpy.pause(3, hard=True)
                    $ persistent.w1ExGame2RoseFelGallery = True
                    hide memoryunlock with dissolve
                    $ renpy.pause(0.5, hard=True)
                "Felicia had secured game number 2."
                $ renpy.end_replay()
                jump w1ExGame2Aftermath


            if w1ExShockPoints == 3:
                $ w1ExGame2WinnerRose = True
                $ w1ExGame2LoserFel = True
                play sound "sound effects/short-beep.wav"
                scene w1_3211 with dissolve
                show screen textbox2 with dissolve
                "Seeing how distracted she seemed with the high option, I decided to take it down a level."
                play sound "sound effects/shock2.wav"
                scene w1_3305 with vpunch
                "*Bzzt!"
                mc "Rosalind is going to win if you don't stand up right now!"
                fel "Gh! Fhuuu!"
                "Unfortunately, the shock proved to be too painful. Instead of realizing what was going on, she was distracted by the pain."
                scene w1_3308 with dissolve
                "While still groaning, Rosalind had managed to prop herself up and stand on her own two feet."
                rose "I'm up! Does that mean...?"
                scene black with fade
                if not persistent.w1ExGame2RoseFelGallery:
                    play sound "sound effects/notification.wav"
                    show memoryunlock with dissolve
                    $ renpy.pause(3, hard=True)
                    $ persistent.w1ExGame2RoseFelGallery = True
                    hide memoryunlock with dissolve
                    $ renpy.pause(0.5, hard=True)
                "Rosalind had taken game number 2."
                $ renpy.end_replay()
                jump w1ExGame2Aftermath

        "Hit the high setting button. [gr]\[ShockPoints +3\]":
            if w1ExShockPoints == 1:
                $ w1ExGame2WinnerFel = True
                $ w1ExGame2LoserRose = True
                play sound "sound effects/short-beep.wav"
                scene w1_3212 with dissolve
                show screen textbox2 with dissolve
                "Worried that the low option didn't have an effect, I decided to try the opposite end, taking it all the way to high."
                play sound "sound effects/shock3.wav"
                scene w1_3304 with vpunch
                "*Bzzt!"
                scene w1_3305 with dissolve
                fel "Zzzzh, damn! Ow, ow, ow! That-"
                scene w1_3307 with dissolve
                mc "Rosalind is going to win if you don't stand up right now!"
                fel "Oh, I need to...!"
                scene w1_3309 with dissolve
                "Despite the pained look, it seemed Felicia fully understood. With a burse of energy, she leapt up on her long, toned legs."
                fel "I win! ...right?"
                scene black with fade
                if not persistent.w1ExGame2RoseFelGallery:
                    play sound "sound effects/notification.wav"
                    show memoryunlock with dissolve
                    $ renpy.pause(3, hard=True)
                    $ persistent.w1ExGame2RoseFelGallery = True
                    hide memoryunlock with dissolve
                    $ renpy.pause(0.5, hard=True)
                "Felicia had secured game number 2."
                $ renpy.end_replay()
                jump w1ExGame2Aftermath

            if w1ExShockPoints == 2:
                $ w1ExGame2WinnerRose = True
                $ w1ExGame2LoserFel = True
                play sound "sound effects/short-beep.wav"
                scene w1_3212 with dissolve
                show screen textbox2 with dissolve
                "Seeing how effective the second option was, I decided that the third option should definitely do it."
                play sound "sound effects/shock2.wav"
                scene w1_3305 with vpunch
                "*Bzzt!"
                mc "Rosalind is going to win if you don't stand up right now!"
                fel "Gh! Fhuuu!"
                "Unfortunately, the shock proved to be too painful. Instead of realizing what was going on, she was distracted by the pain."
                scene w1_3308 with dissolve
                "While still groaning, Rosalind had managed to prop herself up and stand on her own two feet."
                rose "I'm up! Does that mean...?"
                scene black with fade
                if not persistent.w1ExGame2RoseFelGallery:
                    play sound "sound effects/notification.wav"
                    show memoryunlock with dissolve
                    $ renpy.pause(3, hard=True)
                    $ persistent.w1ExGame2RoseFelGallery = True
                    hide memoryunlock with dissolve
                    $ renpy.pause(0.5, hard=True)
                "Rosalind had taken game number 2."
                $ renpy.end_replay()
                jump w1ExGame2Aftermath

            if w1ExShockPoints == 3:
                $ w1ExGame2WinnerRose = True
                $ w1ExGame2LoserFel = True
                play sound "sound effects/short-beep.wav"
                scene w1_3212 with dissolve
                show screen textbox2 with dissolve
                "Seeing how fast she sprung up previously, I was sure another shock at that level would do it."
                play sound "sound effects/shock3.wav"
                scene w1_3305 with vpunch
                "*Bzzt!"
                mc "Rosalind is going to win if you don't stand up right now!"
                fel "Gh! Fhuuu!"
                "Unfortunately, the shock proved to be too painful. Instead of realizing what was going on, she was distracted by the pain."
                scene w1_3308 with dissolve
                "While still groaning, Rosalind had managed to prop herself up and stand on her own two feet."
                rose "I'm up! Does that mean...?"
                scene black with fade
                if not persistent.w1ExGame2RoseFelGallery:
                    play sound "sound effects/notification.wav"
                    show memoryunlock with dissolve
                    $ renpy.pause(3, hard=True)
                    $ persistent.w1ExGame2RoseFelGallery = True
                    hide memoryunlock with dissolve
                    $ renpy.pause(0.5, hard=True)
                "Rosalind had taken game number 2."
                $ renpy.end_replay()
                jump w1ExGame2Aftermath


label w1ExGame2Aftermath:

    stop music fadeout 3.0
    "......"
    "..."
    play music "music/cold-sober.mp3"
    scene w1_3311 with circlewipe

    if kat_polite == True:
        "Following Mrs. Pulman's concluding remarks, which was about as derogatory and self-important as you might expect, there was a brief interlude before the final game."
    else:
        "Following Kathleen's concluding remarks, which was about as derogatory and self-important as you might expect, there was a brief interlude before the final game."

    if w1ExGame2LoserFel == True:
        $ history_felicia = "Felicia narrowly lost the first week's second game, placing her on the chopping block for the final punishment game."
        $ unread_felicia = True
        play sound "sound effects/notification.wav"
        show bioupdate with dissolve
    if w1ExGame2LoserRose == True:
        $ history_rosalind = "Rosalind narrowly lost the first week's second game, placing her on the chopping block for the final punishment game."
        $ unread_rosalind = True
        play sound "sound effects/notification.wav"
        show bioupdate with dissolve

    if w1ExGame2LoserVero == True:
        $ history_veronica = "Veronica narrowly lost the first week's second game, placing her on the chopping block for the final punishment game."
        $ unread_veronica = True
        play sound "sound effects/notification.wav"
        show bioupdate with dissolve

    "A chance for the girls to decompress and clean up, but on the whole the mood in the room was conspicuously somber."
    "On stage, everyone performed admirably, wholly focused on the task at hand and the prize at the end of the month, so much so that it was easy to forget that they weren't professional whores."
    "The anxiety and humiliation they endured must've hit them like a pile of bricks as soon as they had settled into the relative privacy of their dressing room, as that's when everything deflated."
    mct "(Well, at least as far as Veronica and Rosalind are concerned...)"
    "Felicia was still keeping it cool."

    if w1ExGame2LoserFel == True or w1ExGame2WinnerFel == True:
        "Even after the arduous pace of the second game."
    else:
        "She had avoided the arduous second game."

    scene w1_3312 with dissolve
    mc "You girls... alright?"
    "I opted to say {i}something{/i} to break the tense silence, even if it was a trite question."
    scene w1_3313 with dissolve

    if w1ExGame2LoserRose == True or w1ExGame2WinnerRose == True:
        rose "No, that was... rough."
    else:
        rose "I know I shouldn't complain, since I won the first game, but... that was scary."

    scene w1_3314 with dissolve
    ver "What the hell do you think??"

    if w1ExGame2LoserVero == True or w1ExGame2WinnerVero == True:
        ver "You didn't just have a bunch of spiky toy balls shoved up your ass."

    else:
        ver "Unlike you, I'm not a pervert. I didn't get my kicks off performing up there."
        scene w1_3316 with dissolve
        mct "(Actually, she did...)"

    if w1ExVeroPissedOn == True:
        scene w1_3315 with dissolve
        ver "Not to mention, you fucking peed on me, asshole!"

    scene w1_3317 with dissolve
    mc "What about you, Felicia?"
    scene w1_3318 with dissolve
    fel "It was interesting."
    scene w1_3319 with dissolve
    rose "Tsk!"
    "Rosalind clicked her tongue in frustration."
    scene w1_3320 with dissolve
    rose "Interesting...? I can't believe you! Are you really here because you want to be a member of this awful place?"
    scene w1_3321 with dissolve
    fel "There's..."
    scene w1_3322 with dissolve
    "Felicia paused and weighed her answer, before finally speaking again."
    scene w1_3323 with dissolve
    fel "There's more to it than that. I have my reasons for what I asked for, just like you."
    scene w1_3324 with dissolve
    rose "That's crap! You're nothing--"
    scene w1_3325 with dissolve
    ver "Hey, calm down."

    if w1ExGame2LoserRose == True:
        ver "You still have the final game to think about. Don't get distracted, you just got to focus on what you've got to do."
    else:
        ver "There's no point in getting bent out of shape. You just got to focus on what you've got to get done this month."

    scene w1_3326 with dissolve
    rose "Ah... ha...."
    scene w1_3327 with dissolve
    rose "..."
    scene w1_3328 with dissolve
    rose "You're right, thank you."
    scene w1_3329 with dissolve
    ver "I wonder what the last game will involve...."

    if w1ExGame2LoserVero == True:
        scene w1_3330 with dissolve
        rose "You're nervous."
        scene w1_3329 with dissolve
        ver "Of course I am."
        mct "(That's right... Veronica is facing the final challenge of the night alone."
        scene w1_3331 with dissolve
        rose "Can you tell me what's coming up next, [mcf]?"
        scene w1_3332 with dissolve
        mc "No, I'm in the dark as much as you."
        "For a moment, Veronica looked at me questioningly, but ultimately seemed to accept my answer."
        scene w1_3333 with dissolve
        ver "I guess I'll be finding out soon enough. Might be better not to know what's coming..."
        scene w1_3334 with dissolve
        fel "Yeah, why spoil the surprise?"
        scene w1_3335 with dissolve
        ver "Save me the glib attitude. It's annoying when you're here willingly."


    if w1ExGame2LoserRose == True:
        ver "Don't let that old woman beat you, Rose."
        scene w1_3330 with dissolve
        rose "I won't. I've got to win."
        mct "(That's right... Rosalind is facing the final challenge of the night alone."
        scene w1_3331 with dissolve
        rose "Do you have any idea what it'll be, [mcf]?"
        scene w1_3332 with dissolve
        mc "No, I'm in the dark as much as you."
        "Rosalind seemed to accept my answer unquestioningly, giving an anxious smile about what's coming next."
        scene w1_3336 with dissolve
        rose "I guess I'll find out soon then."
        scene w1_3334 with dissolve
        fel "Yeah, why spoil the surprise?"
        scene w1_3335 with dissolve
        ver "Can you save the glib attitude, please? It's annoying when you're here willingly."

    if w1ExGame2LoserFel == True:
        scene w1_3337 with dissolve
        ver "Have fun up there, blondie. Better you than us, right?"
        scene w1_3338 with dissolve
        "Felicia didn't answer her, but for a split second, her expression made her look terribly alone."
        scene w1_3331 with dissolve
        rose "Do you have any idea what it'll be, [mcf]?"
        scene w1_3332 with dissolve
        mc "No, I'm in the dark as much as you."
        scene w1_3339 with dissolve
        fel "Hmmm... I guess it's probably for the best if you don't spoil it."
        scene w1_3340 with dissolve
        ver "You're not nervous, are you blondie?"
        scene w1_3341 with dissolve
        fel "Everyone gets a little stage fright."
        scene w1_3340 with dissolve
        ver "Yeah, but you're here willingly."


    scene w1_3342 with dissolve
    fel "So are you two. Don't forget that! No one has a gun to your head, do they?"
    scene w1_3343 with dissolve
    ver "You know what I mean. You don't need money."
    scene w1_3342 with dissolve
    fel "Not everything can be solved with money, {b}red{/b}. Not everything can even be solved..."
    scene w1_3343 with dissolve
    stop music fadeout 3.0
    ver "Mine can. That's why I'm here."
    scene w1_3344 with dissolve
    kat "My, girls! There's a man present and you're not decent!"

    if kat_polite == True:
        "Mrs. Pulman entered from behind us, opening with a flat attempt at humor."
    else:
        "Kathleen entered from behind us, opening with a flat attempt at humor."

    scene w1_3345 with dissolve
    mc "What's decent about any of this?"
    scene w1_3346 with dissolve
    kat "Not much, is there?"
    scene w1_3347 with dissolve
    rose "Is there something you need, Mrs. Pulman?"
    scene w1_3348 with dissolve

    if w1ExGame2LoserVero == True:
        kat "I'm here to help Miss Lynch with her wardrobe."
        scene w1_3350 with dissolve
        ver "..."
        jump w1ExEarningsGameVeronicaStart

    if w1ExGame2LoserRose == True:
        kat "I'm here to help you with your wardrobe."
        scene w1_3351 with dissolve
        rose "..."
        jump w1ExEarningsGameRosalindStart

    if w1ExGame2LoserFel == True:
        kat "I'm here to help Mrs. Ford with her wardrobe."
        scene w1_3349 with dissolve
        fel "..."
        jump w1ExEarningsGameFeliciaStart


label w1ExEarningsGameRosalindStart:

    play music "music/leaving-home.mp3"
    scene w1_3352 with w19
    mct "(Yeesh, that looks uncomfortable...)"
    scene w1_3353 with dissolve
    "The next game saw Rosalind hog tied, perched at the edge of a table in a way that emphasized the size and shape of her bust."

    if kat_polite == True:
        "Uncomfortably waiting for Mrs. Pulman to explain what was about to happen to her."
    else:
        "Uncomfortably waiting for Kathleen to explain what was about to happen to her."

    "For once, she was taking her sweet time to begin talking."
    scene w1_3354 with dissolve
    mc "It's got to suck to be the only one about to be raked over the fire."
    scene w1_3355 with dissolve
    ver "No, kidding. She's got to be terrified. I'd be."
    scene w1_3356 with dissolve
    kil "Seems out of character for you to just admit that."
    scene w1_3357 with dissolve
    ver "You know jack shit about my \"character\", boy."
    scene w1_3358 with dissolve
    fel "She's going to nail this."
    scene w1_3355 with dissolve
    ver "Huh? What are you talking about?"
    scene w1_3352 with dissolve
    fel "Look at her face."
    ver "You're right. She's ready for what's coming."
    "They were right. Despite looking like she's about to be served up as dinner, there was a indomitable clarity to her body language."
    scene w1_3359 with dissolve
    kat "Looks like everyone has returned to their seats. Are you ready to begin?"
    scene w1_3360 with dissolve
    isak "Yes, ma'am!"
    tom "I've been looking forward to this."

    if kat_polite == True:
        "The room unanimously voiced their approval at Mrs. Pulman moving on."
    else:
        "The room unanimously voiced their approval at Kathleen moving on."

    scene w1_3361 with dissolve
    kat "Excellent. Our final game is a punitive one, to penalize Mrs. Carter for falling short of the club's standards."
    scene w1_3362 with dissolve
    kat "That doesn't mean she won't be afforded the opportunity to gain ground in the standings tonight. After all, it wouldn't be any fun if there wasn't anything at stake."
    scene w1_3361 with dissolve
    kat "However, her success will be linked with the interest she has garnered tonight."
    scene w1_3363 with dissolve
    chuck "What are you getting at, Kat?"
    scene w1_3361 with dissolve
    kat "Tonight we're going to do something special. I'm going to hinge this slut's success with the wallet's of our esteemed patrons."

    if w1RoseGonzo == True and w1GonzoReward == True:
        kat "She was the favorite going into tonight after all."

    scene w1_3362 with dissolve
    kat "A whore that can't be proactive in their service can always earn her keep as a cum rag."
    scene w1_3364 with dissolve
    "At the mention of the rank and noxious phrase, Rosalind's pale complexion blanched even more."
    kat "For the price of $200 a pop, you can sexually release yourself on and sully this fat cow's face and tits as much as your heart desires."
    scene w1_3365 with dissolve
    jim "$200 just for that?"
    scene w1_3366 with dissolve
    frank "Not all of us are on a cop's salary, Jim."
    scene w1_3361 with dissolve
    kat "If she manages to earn $4000, I'll consider this a win for her."
    scene w1_3367 with dissolve
    kil "Heh, things are about to get messy..."
    scene w1_3368 with dissolve
    fel "No kidding."
    scene w1_3369 with dissolve
    ver "This is stupid. I'd feel sorry for poor Rose if she didn't have it so easy."
    scene w1_3370 with dissolve
    mc "What the hell are you talking about?"
    scene w1_3369 with dissolve
    ver "She's just got to sit there, while Felicia and I had to work for our wins."
    scene w1_3370 with dissolve
    mc "Don't be so callous. She's getting the worst of the night."
    scene w1_3371 with dissolve
    ver "..."
    scene w1_3372 with dissolve
    mct "(Come to think of it, do I even need to see this? My absence will most likely be noticed, but I could duck out of here and visit Hana. Avoid seeing this nasty business.)"
    "Then again, if I wanted to, I could enjoy the show and maybe even join in..."
    hide screen textbox2 with dissolve

    menu:
        "Stick around and watch Rosalind get covered in cum. [gr]\[Toughness +2\]\[Kathleen +1\]":
            $ toughness += 2
            $ Kathleen_Trust += 1
            stop music fadeout 3.0
            show screen textbox2 with dissolve
            mct "(Well, it is my job to be here and it does pay well...)"
            scene w1_3373 with dissolve
            kat "If you're interested, please make yourself comfortable gentlemen and form a line."
            jump w1ExEarningsGameRosalind

        "Slip out of the room and find Hana. [gr]\[Hana +3\]":
            $ w1ExGame3Avoid = True
            $ Hana_Affection += 3

            show screen textbox2 with dissolve
            mct "(No, I definitely don't want to see this.)"
            jump w1ExHanaHangout


label w1ExEarningsGameFeliciaStart:


    play music "music/leaving-home.mp3"
    scene w1_3374 with w19
    mct "(Yeesh, that looks uncomfortable...)"

    scene w1_3376 with dissolve
    "The next game saw Felicia resting on her neck, ass hiked straight up into the air and legs drawn back over her shoulder."

    if kat_polite == True:
        "Excruciatingly waiting for Mrs. Pulman to explain what was about to happen to her."
    else:
        "Excruciatingly waiting for Kathleen to explain what was about to happen to her."

    "For once, she was taking her sweet time to begin talking."
    scene w1_3377 with dissolve
    mc "It's got to feel lonely up there knowing you're the only one about to be raked over the fire."
    scene w1_3378 with dissolve
    ver "No, kidding, but she asked for it."
    scene w1_3379 with dissolve
    kil "Nah, Felicia ain't the kind of woman that would sweat this."
    scene w1_3380 with dissolve
    ver "You of all people should know the phrase \"false bravado\", boy."
    scene w1_3381 with dissolve
    rose "I don't know about that... she looks pretty ready."
    scene w1_3378 with dissolve
    ver "Huh? What are you talking about?"
    scene w1_3374 with dissolve
    rose "Look at her expression. She looks... excited."
    ver "You're right, that's some game face."
    "Despite looking like she's about to be served up as dinner, Felicia looked relatively undaunted."
    scene w1_3375 with dissolve
    kat "Looks like everyone has returned to their seats. Are you ready to begin?"
    scene w1_3382 with dissolve

    if kat_polite == True:
        "The room unanimously voiced their approval at Mrs. Pulman moving on."
    else:
        "The room unanimously voiced their approval at Kathleen moving on."

    scene w1_3361 with dissolve
    kat "Excellent. Our final game is a punitive one, to penalize Mrs. Ford for falling short of the club's standards."
    scene w1_3362 with dissolve
    kat "That doesn't mean she won't be afforded the opportunity to gain ground in the standings tonight. After all, it wouldn't be any fun if there wasn't anything at stake."
    scene w1_3361 with dissolve
    kat "However, her success will be linked with the interest she has garnered tonight."
    scene w1_3363 with dissolve
    chuck "What are you getting at, Kat?"
    scene w1_3361 with dissolve
    kat "Tonight we're going to do something special. I'm going to hinge this slut's success with the wallet's of our esteemed patrons."

    if w1FelGonzo == True and w1GonzoReward == True:
        kat "She was the favorite going into tonight after all."

    scene w1_3362 with dissolve
    kat "A whore that can't be proactive in their service can always earn her keep as a cum rag."
    scene w1_3375 with dissolve
    "At the mention of the noxious phrase, Felicia raised a curious eyebrow."
    kat "That's right, for the price of $200 a pop, you can sexually release yourself onto this pig's lewd body as much as your heart desires."
    scene w1_3365 with dissolve
    jim "$200 just for that?"
    scene w1_3366 with dissolve
    frank "Not all of us are on a cop's salary, Jim."
    scene w1_3361 with dissolve
    kat "If she manages to earn $4000, I'll consider this a win for her."
    scene w1_3383 with dissolve
    kil "Things are about to get messy..."
    rose "Oh, my..."
    scene w1_3369 with dissolve
    ver "This is stupid. Why does she get it so easy?"
    scene w1_3370 with dissolve
    mc "What the hell are you talking about?"
    scene w1_3369 with dissolve
    ver "She's just got to sit there, while Rosie and I had to work for our wins."
    scene w1_3370 with dissolve
    mc "Don't be so callous. She's getting the worst of the night."
    scene w1_3371 with dissolve
    ver "..."
    scene w1_3372 with dissolve
    mct "(Come to think of it, do I even need to see this? My absence will most likely be noticed, but I could duck out of here and visit Hana. Avoid seeing this nasty business.)"
    "Then again, if I wanted to, I could enjoy the show and maybe even join in..."
    hide screen textbox2 with dissolve

    menu:
        "Stick around and watch Felicia get covered in cum. [gr]\[Toughness +2\] \[Kathleen +1\]":
            $ toughness += 2
            $ Kathleen_Trust += 1
            show screen textbox2 with dissolve
            stop music fadeout 3.0
            show screen textbox2 with dissolve
            mct "(Well, it is my job to be here and it does pay well...)"
            scene w1_3384 with dissolve
            kat "If you're interested, please make yourself comfortable gentlemen and form a line."
            jump w1ExEarningsGameFelicia

        "Slip out of the room and find Hana. [gr]\[Hana +3\]":
            $ w1ExGame3Avoid = True
            $ Hana_Affection += 3
            show screen textbox2 with dissolve
            mct "(No, I definitely don't want to see this.)"
            jump w1ExHanaHangout


label w1ExEarningsGameVeronicaStart:

    play music "music/leaving-home.mp3"
    scene w1_3385 with w19
    mct "(Yeesh, that looks uncomfortable...)"
    scene w1_3387 with dissolve
    "The next game saw Veronica's body stretched out over a table, limbs tied to the table's legs like she was a sacrificial offering."

    if kat_polite == True:
        "Gloomily waiting for Mrs. Pulman to explain what was about to happen to her."
    else:
        "Gloomily waiting for Kathleen to explain what was about to happen to her."

    "For once, she was taking her sweet time to begin talking."
    scene w1_3388 with dissolve
    mc "It's got to feel lonely up there knowing you're the only one being raked over the fire."
    scene w1_3389 with dissolve
    rose "I bet she's terrified. Poor Veronica."
    scene w1_3390 with dissolve
    kil "I bet she isn't used to being tied up."
    scene w1_3391 with dissolve
    fel "You don't know what she gets up to in her personal life."
    scene w1_3389 with dissolve
    rose "She looks pretty ready..."
    scene w1_3392 with dissolve
    fel "Doesn't she?"
    scene w1_3385 with dissolve
    rose "Yeah. It's hard to tell from over here, but she looks scary."
    "They were right. Despite looking like she's about to be served up as dinner, she had her game face on."
    scene w1_3386 with dissolve
    kat "Looks like everyone has returned to their seats. Are you ready to begin?"
    scene w1_3393 with dissolve
    isak "Yes, ma'am!"
    sam "Hell, yeah!"
    chuck "I'm sad to see the night wind down!"

    if kat_polite == True:
        "The room unanimously voiced their approval at Mrs. Pulman moving on."
    else:
        "The room unanimously voiced their approval at Kathleen moving on."

    scene w1_3361 with dissolve
    kat "Excellent. Our final game is a punitive one, to penalize Miss Lynch for falling short of the club's standards."
    scene w1_3362 with dissolve
    kat "That doesn't mean she won't be afforded the opportunity to gain ground in the standings tonight. After all, it wouldn't be any fun if there wasn't anything at stake."
    scene w1_3361 with dissolve
    kat "However, her success will be linked with the interest she has garnered tonight."
    scene w1_3363 with dissolve
    chuck "What are you getting at, Kat?"
    scene w1_3361 with dissolve
    kat "Tonight we're going to do something special. I'm going to hinge this slut's success with the wallet's of our esteemed patrons."

    if w1VeroGonzo == True and w1GonzoReward == True:
        kat "She was the favorite going into tonight after all."

    scene w1_3362 with dissolve
    kat "A whore that can't be proactive in their service can always earn her keep as a cum rag."
    scene w1_3386 with dissolve
    "At the mention of the noxious phrase, Veronica let out an exasperated sigh."
    kat "For the price of $200 a pop, you can sexually release yourself onto this overdeveloped bitch's lewd body as much as your heart desires."
    scene w1_3365 with dissolve
    jim "$200 just for that?"
    scene w1_3366 with dissolve
    frank "Not all of us are on a cop's salary, Jim."
    scene w1_3361 with dissolve
    kat "If she manages to earn $4000, I'll consider this a win for her."
    scene w1_3395 with dissolve
    kil "Heh, things are about to get messy..."
    rose "Oh, my..."
    scene w1_3396 with dissolve
    fel "She's already starting to sweat."
    scene w1_3397 with dissolve
    mc "Who wouldn't be?"
    scene w1_3398 with dissolve
    fel "This should be interesting."
    scene w1_3399 with dissolve
    mct "(Come to think of it, do I even need to see this? My absence will most likely be noticed, but I could duck out of here and visit Hana. Avoid seeing this nasty business.)"
    "Then again, if I wanted to, I could enjoy the show and maybe even join in..."
    hide screen textbox2 with dissolve

    menu:
        "Stick around and watch Veronica get covered in cum. [gr]\[Toughness +2\] \[Kathleen +1\]":
            $ toughness += 2
            $ Kathleen_Trust += 1
            show screen textbox2 with dissolve
            stop music fadeout 3.0
            show screen textbox2 with dissolve
            mct "(Well, it is my job to be here and it does pay well...)"
            scene w1_3394 with dissolve
            kat "If you're interested, please make yourself comfortable gentlemen and form a line."
            jump w1ExEarningsGameVeronica

        "Slip out of the room and find Hana. [gr]\[Hana +3\]":
            $ w1ExGame3Avoid = True
            $ Hana_Affection += 3
            show screen textbox2 with dissolve
            mct "(No, I definitely don't want to see this.)"
            jump w1ExHanaHangout



label w1ExEarningsGameRosalind:

    if _in_replay:
        show screen textbox2 with dissolve

    scene black with fade
    "......"
    hide screen textbox2 with dissolve
    show screen camcorder with dissolve
    "..."
    play music "music/beginning-of-conflict.mp3"
    scene w1_3400 with pixellate
    rose "Eh... w-what was that? W-why am I suddenly..."
    kat "Turned on? Hot?"
    rose "Y-yes! My head feels like it's about to boil!"
    scene w1_3401 with dissolve
    kat "Don't think too much about it. It's just something to make things more interesting, for both us and for you."
    rose "W-was it a drug....? Aha... ha...!"

    if w1GonzoReward:
        "I watched from the sidelines, as that all-too-familiar aphrodisiac began sinking it's devious claws into the bound mother."
    else:
        "I watched as what I presumed to be some sort of sex drug began sinking it's claws into the bound mother."

    kat "It's just a handy syrup that will make you feel good. Don't worry your pretty little head about it."
    scene w1_3402 with dissolve
    "Rosalind began to finick in place, trying to fruitlessly scratch an itch she was unable to reach."
    "The table she rested on proved sturdy, barely budging as the hog tied woman uncomfortably fidgeted on its face."

    if kat_polite == True:
        "Apart from how wonderful it made Rose's breasts look, it occurred to me that Mrs. Pulman had a more cruel reason in mind when she chose that position."
    else:
        "Apart from how wonderful it made Rose's breasts look, it occurred to me that Kathleen had a more cruel reason in mind when she chose that position."

    "Hands and legs bound, Rosalind had no avenue for satisfaction. The drug in her system would make her insanely aroused, but she wouldn't find sexual release."
    hide screen camcorder
    scene w1_3403 with fade
    show screen textbox2 with dissolve
    "I had been tasked with recording the event, something that no one had a problem with. In actuality, they seemed excited at the opportunity to have a copy of the debauchery for home consumption."
    "It seemed awfully gauche to me, that these men with all their money and access, would jack off at home like a common pervert."

    hide screen textbox2 with dissolve
    scene w1ExGame3Rose with pixellate
    show screen camcorder
    if history_voyeur == True:
        "At the same time, I understood. Peaking through the view finder at the obscene sight had brought out the voyeur in me in full force."
    else:
        "I wondered if I'd ever fully grasp the psychology of these men or if I'd even wanted to understand."

    tom "I'm so glad I got to be first to soil those beautiful breasts of yours..."
    "The boob-obsessed lawyer eked out some words while stroking his dick in front of the tied up mother's face."
    scene w1_3407 with dissolve
    "Rosalind tried to avert her gaze, but it would unavoidably find its way back to the cock square in front of her."
    kat "Come now, Mrs. Carter. Don't look so mortified. You should thank Mr. Blake for being your first customer."
    scene w1_3408 with dissolve
    rose "Uh..."
    "Rosalind looked totally scatterbrained. I don't know if it was solely due to the aphrodisiac coursing through her veins, but..."
    "At this moment, I was sure she was being struck by her lack of power."
    scene w1_3407 with dissolve
    rose "Um... t-thank you, Mr. Blake."
    scene w1ExGame3Rose with dissolve
    "Rosalind's flushed skin turned a shade brighter with the embarrassing words."
    tom "*huff* *huff* Ah... ah...!"
    kat "What are you thanking him for, dear?"
    rose "Um... for being my first customer?"
    kat "No. You should thank him for stroking his cock to your fat cow tits."
    rose "Mmmmh, t-thank you for stroking your cock to my f-fat cow tits!"
    "So flustered, Rosalind practically shouted the obscene statement."
    scene w1_3407 with dissolve
    tom "Ha! No need to thank me, gorgeous. You're a damn goddess!"
    rose "Um... thanks?"
    play sound "sound effects/spurt.wav"
    scene w1_3409 with dissolve
    tom "Aaaaaaah!"
    "Aiming his cock at Rosalind's breasts, he let out a cry just before he painted the whore mother's bountiful jugs white."
    scene w1_3410 with dissolve
    rose "B-bleh...!"
    "As soon as the excited man's seed touched her skin, Rosalind's face flashed in a violent revulsion."
    rose "E-huh...? Eheh..."
    rose "M-my skin is so hot, that it feels...!"
    rose "P-pleasant...?"
    "Her natural disgust was at odds with the physiological effects of the aphrodisiac."
    scene w1_3411 with fade
    "Just as soon as the lawyer had shuffled off stage, he was replaced by another man eager for his turn."
    "Likewise more men had begun to pool around the hog tied mother like sharks drawn to blood in the water."
    rose "Ummmmh... t-thank you for your interest, sirs."
    "She squirmed in place, her thighs rubbing together in a fruitless effort to belay the uncurbed arousal between her legs."
    "Unable to move. Rosalind naturally had no other course but to endure."
    scene black with fade
    "......"
    "..."
    scene w1_3412 with fade
    rose "Oh my... there's so many of you."
    jim "I'm next, before this whore becomes too disgusting!"
    frank "Ahaha, you seemed so price shy earlier!"
    jim "Can it, a man can change his mind."
    scene w1_3413 with fade
    "Over the next however long, various patrons used Rosalind as a perverted canvas, spilling their ejaculate wherever they desired on the bound woman's body."
    "Patron by patron, Rosalind's flawless clear skin was dyed in white."
    scene w1_3414 with dissolve
    rose "Gheh... the smeeeell..."
    "I watched as the calm, motherly image I held of Rose was reduced to something obscene and base."
    vinc "Can't we do more than just jerk off? I'll pay $5,000 right now to fuck her!"
    kat "I'm afraid that's outside the parameters of the game, Mr. Bianchi."
    scene w1_3415 with dissolve
    "Bill after hundred dollar bill pilled up around Rosalind's soiled body."
    "It made for quite the sight, driving home Rosalind's role as a prostitute to both her and onlooker alike."
    rose "T-thank you..."
    "Every time a man unloaded onto her chest or face, Rosalind pushed down her disgust and thanked her beneficiary in an artifical tone."
    tom "Ah... ah...! "
    "Some of the men had even lined up to go again."
    scene w1_3416 with dissolve
    rose "Ah... i-it's you?"
    "Killian had stepped up to the plate, tossing down a wad of cash and furiously stroking his cock."
    hide screen camcorder with dissolve
    scene w1_3417 with dissolve
    show screen textbox2 with dissolve
    kil "Sorry, but [mcf] got to have all the fun earlier. Not to mention how fucking hot this is."
    kil "You're a nasty bitch, you know that?"
    rose "No, it's only because I have to do this..."
    kil "Doesn't change the fact you're covered in cum right now."
    scene w1_3418 with dissolve
    chuck "I bet you didn't think to bring any cash with you tonight, lad."
    scene w1_3419 with dissolve
    mc "Ah, well... it's too rich for me anyway."
    scene w1_3420 with dissolve
    "Holding out his hand, Dr. Chuck offered me a neat stack of bills."
    chuck "Go enjoy yourself. I'll take over filming! Consider it a gift from your Uncle Chuck!"
    hide screen textbox2 with dissolve
    scene w1_3415 with fade
    show screen camcorder with dissolve
    "Stealing one last glance over at Rosalind and the gathered men, something about the scenario tempted me."
    hide screen camcorder with dissolve
    scene w1_3421 with dissolve
    show screen textbox2 with dissolve
    mct "(...{i}do I{/i} want to take part in this?)"
    stop music fadeout 3.0
    hide screen textbox2 with dissolve

    menu:
        "Join in on the fun. [gr]\[Killian +2\] \[Rosalind +1\]":
            $ Killian_Bromance += 2
            $ Rosalind_Libido += 1

            show screen textbox2 with dissolve
            mct "(Deep down... yeah, I do.)"
            "Plus, I suppose in a twisted way, this technically helps Rosalind out."
            scene w1_3422 with dissolve

            if chuck_polite == True:
                mc "Thank you for your generosity, sir."
            if chuck_uncle == True:
                mc "Thanks for your generosity, Uncle Chuck."
            else:
                mc "Thank you for your generosity, Dr. Chuck."

            chuck "Don't mention it, lad. Besides, I wouldn't mind some time behind the camera, heh..."
            "Dr. Chuck flashed me a knowing smile in perverted solidarity."
            scene black with fade
            "Taking the cash and adding it to the other bills surrounding Rosalind's grimy body, I discarded my clothes and found a place next to my friend."
            scene w1_3425 with dissolve
            play music "music/doll-dancing.mp3"
            kil "Ohoho, you still got some in the tank?"
            scene w1_3426 with dissolve
            mc "Don't make this weird..."
            scene w1_3425 with dissolve
            kil "Too late for that! Might as well lean into it. Enjoy having a mutual wank with your best bud onto some slut!"
            scene w1_3427 with dissolve
            rose "You too, [mcf]...?"
            scene w1_3428 with dissolve
            mc "You got to make money to win, right?"
            scene w1_3427 with dissolve
            rose "I do..."
            scene w1_3429 with dissolve
            kil "Then you should be grateful that [mcf] joined in!"
            scene w1_3427 with dissolve
            rose "...y-yeah, you're right! Please enjoy..."
            scene w1_3429 with dissolve
            kil "That's the spirit!"
            scene w1ExGame3Rose2 with dissolve
            "Shutting everything out, I decided to focus on the sight in front of me. The sight of Rosalind, drowning in baby batter, money strewn about her like an expensive whore."
            "How she tightly held one eye shut, to avoid the jizz clinging to her brow from getting into her eye."
            "How the semen dripped, rolling down her large breasts and pooled at the tips of her nipples."
            "It was {i}utterly{/i} disgusting, yet... I furiously stroked my cock with wild abandon, like I hadn't jerked it in a week."
            scene w1_3433 with dissolve
            rose "Do you... do you like me like this, Mr. [mcl]?"
            scene w1ExGame3Rose2 with dissolve
            "Yes - part of me relished her humiliation."
            "Rosalind's one open eye was glued to the sight of me jackhammering my cock."
            kil "I think she's happy you joined in!"
            vinc "She likes the boy, eh? Bahaha!"
            "It was difficult to read Rose's expression with my lust addled mind."
            mct "(No, she's just latching onto the most familiar face to take her mind of the humilation.)"
            "Rosalind was surprisingly adaptive to this environment."
            scene w1_3433 with dissolve
            rose "Ah... eh... do you... do you like me like this?"
            "She asked me again, with aphrodisiac-laced words."
            mc "I do."
            rose "I thought so... please stroke your cock until you finish all over me, [mcf]."
            scene w1_3434 with dissolve
            kil "Hey! What am I, chopped liver? Ask me too!"
            rose "You too, Mr. Beaufort. Use me like a rag."
            scene w1ExGame3Rose2 with dissolve
            kil "Ah, that felt a lot colder, but who cares...! Have what you asked for, bitch!"
            play sound "sound effects/spurt.wav"
            scene w1_3435 with dissolve
            "With a short, barbarous grunt Ian let loose a torrent of jizz onto Rosalind's face."
            kil "G-ah, gnnh!"
            rose "Geh!"
            scene w1_3436 with dissolve
            "Nailing her right in her one open eye. He did that on purpose!"
            mc "Oh, here it comes...! "
            "Seeing the beautiful mother's ruined, suddenly grimacing expression was enough to push me over the edge as well."
            play sound "sound effects/spurt.wav"
            scene w1_3437 with dissolve
            mc "Gh--!"
            "One last spurt had Rosalind looking like a glazed donut."
            scene w1_3438 with dissolve
            rose "Geh... it's in my nose... ew...."
            mc "Ah, s-sorry..."



        "Just keep filming.":

            scene w1_3423 with dissolve
            show screen textbox2 with dissolve
            if chuck_polite == True:
                mc "No, but thanks for the kind offer, sir."
            if chuck_uncle == True:
                mc "No, but thanks for the kind offer, Uncle Chuck."
            else:
                mc "No, but thanks for the kind offer, Dr. Chuck."

            scene w1_3418 with dissolve
            chuck "Really, lad?"
            scene w1_3419 with dissolve
            mc "I guess kinda like it behind the camera."
            scene w1_3424 with dissolve
            "Dr. Chuck flashed me a knowing smile in perverted solidarity."
            chuck "Heh, that I understand!"
            hide screen textbox2 with dissolve
            scene black with fade
            show screen camcorder with dissolve
            "Patting me on the back, Dr. Chuck veered off and I turned my attention back to the stage."
            scene w1ExGame3Rose3 with dissolve
            play music "music/on-the-ground.mp3"
            kil "There's something about you Rose... ah...!"
            "Killian was stroking his cock furiously, seemingly not a care in the world."
            kil "Ah! I know what it is... it's those huge milk jugs of yours!"
            "My best friend reveled in his crass attitude."
            rose "So everyone has said..."
            vinc "Well, we're not her for your personality! Bahaha!"
            rose "Mhh..."
            "Beneath the layers of baby batter, Rosalind's expression was difficult to read."
            rose "Please, enjoy them then..."
            kil "Oh, I will!"
            "Tuning Ian's inane comments out, I decided to focus on Rosalind. Drowning in baby batter, money strewn about her like an expensive whore."
            "How she tightly held one eye shut, to avoid the jizz clinging to her brow from getting into her eye."
            "How the semen dripped, rolling down her large breasts and pooled at the tips of her nipples."
            "It was {i}utterly{/i} disgusting, yet... there was something compelling about it."
            rose "P-please, use me like a rag..."
            "She did her best to say the things these perverts wanted to hear."
            kil "Have what you asked for, bitch!"
            play sound "sound effects/spurt.wav"
            scene w1_3442 with dissolve
            "With a short, barbarous grunt Ian let loose a torrent of jizz onto Rosalind's face."
            kil "G-ah, gnnh!"
            rose "Geh!"
            scene w1_3443 with dissolve
            "Nailing her right in her one open eye. He did that on purpose!"
            kil "Ah, that was fun. I think I could go again..."
            hide screen camcorder
            show screen textbox2 with dissolve


    scene black with fade
    stop music fadeout 3.0
    "The scene continued on for twenty more minutes, by the end of it..."
    scene w1_3444 with dissolve
    $ history_rosalind = "Rosalind took part in this week's final game, managing to make enough money to go into the next week on equal footing with the other two Carnations."
    $ unread_rosalind = True
    play sound "sound effects/notification.wav"
    show bioupdate with dissolve
    rose "*Cough, cough!* Y-yhuck! Gh! *Cough, cough!*"
    kat "You look absolutely rancid, my dear."
    rose "Ghu..."
    frank "Holy shit, that glob is like a foot long!"
    mihir "Disgusting."
    chuck "You did amazing! Good job, Rose!"
    scene black with fade
    if not persistent.w1ExGame3RoseGallery:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w1ExGame3RoseGallery = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)
    "Rosalind made her quota, plus a half."
    "......"
    "..."
    $ renpy.end_replay()
    jump w1ExKatEnding


label w1ExEarningsGameFelicia:

    if _in_replay:
        show screen textbox2 with dissolve

    scene black with fade
    "......"
    "..."
    scene w1_3445 with curtains
    fel "Eh... What did you just give me? Why am I so incredibly... {b}horny{/b} right now?"
    kat "Don't think too much about it, dear. It's just something to make things more interesting, for both us and for you."
    scene w1_3446 with dissolve
    fel "Whatever it is, it feels... {b}good{/b}."

    if w1GonzoReward:
        "I watched from the sidelines, as that all-too-familiar aphrodisiac began sinking it's devious claws into the upside down, volunteer whore."
    else:
        "I watched as what I presumed to be some sort of sex drug began sinking it's claws into the upside down, volunteer whore."

    scene w1_3447 with dissolve
    kat "I'm glad you seem to have an open mind, because we haven't even fully set the stage yet."
    scene w1_3448 with dissolve
    fel "Oh...? There's more...?"
    scene w1_3450 with dissolve
    kat "Since you can't help yourself because of the shackles, I've decided to generously lend you a hand."
    kat "How do you like the sound of that?"
    scene w1_3449 with dissolve
    fel "I say, hurry up!"
    scene w1_3450 with dissolve
    kat "Heh, heh, heh... so fucking glib."
    scene black with fade
    play sound "sound effects/vib-start.wav"
    fel "Ehoooo...?"
    hide screen textbox2 with dissolve
    show screen camcorder with dissolve
    scene w1_3451 with pixellate
    play music "music/beginning-of-conflict.mp3"
    fel "Oooooooohohohoho...! Gh-! It's on m-max...!"
    "Felicia violently wiggled her hips, causing her shackles to make a distinct clacking sound."
    hide screen camcorder with dissolve
    scene w1_3403 with dissolve
    show screen textbox2 with dissolve
    "I had been tasked with recording the event, something that no one had a problem with. In actuality, they seemed excited at the opportunity to have a copy of the debauchery for home consumption."
    "It seemed awfully gauche to me, that these men with all their money and access, would jack off at home like a common pervert."
    hide screen textbox2 with dissolve
    scene w1ExGame3Fel with dissolve
    show screen camcorder
    eric "I just had to be the first up here."
    "Felicia's biggest fan had beaten the other men to the stage and was now furiously stroking his cock to the shackled beauty."
    fel "Heh, thanks mister... you sure are excited..."
    eric "That's because you're an interesting woman, Mrs. Ford. This place has never had a social climber like you before. Not to mention..."
    eric "The wife of Elias Ford, h-o-l-y s-h-i-t! What wonderful luck."
    "The cackling CEO didn't let up for one moment, full fisting his cock at a dizzying speed while spelling out his excitement."
    hide screen camcorder with dissolve
    scene w1_3455 with dissolve
    show screen textbox2 with dissolve
    fel "Ah-! Why does that-eh, geeee..."
    fel "W-why does interest you, Mr. Waylon?"
    "Despite the aphrodisiac coursing through her veins, Felicia mustered an appopriately curious tone when questioning the man's reasoning."
    scene w1_3456 with dissolve
    eric "It's because I've met your husband. He's a holier-than-thou prick of the highest magnitude! Needless to say, seeing his wife whore herself out, that's a thrill!"
    hide screen textbox2 with dissolve
    scene w1ExGame3Fel with dissolve
    show screen camcorder
    fel "You're a real piece of work, mister. You've got a woman like me tied up in front of you and all you can think about is a middle-aged man?"
    eric "Don't get too full of yourself..."
    fel "Oeeh, oh... is that what I'm doing?"
    eric "Bitches like you are a dime and dozen. Your status is the only thing that makes you interesting."
    hide screen camcorder with dissolve
    scene w1_3457 with dissolve
    show screen textbox2 with dissolve
    fel "{i}I'm{/i} a dime a dozen? Just keep stroking your cock and we'll both pretend you're not just another Gordon Gekko wannabe."
    scene w1_3458 with dissolve
    eric "..."
    scene w1_3459 with dissolve
    chuck "Bahaha! She's got your number Waylon!"
    scene w1_3456 with dissolve
    eric "I know. Isn't she great?"
    eric "I apologize, Mrs. Ford. You've got a little more personality than your typical gold digging bimbo."
    scene w1_3460 with dissolve
    eric "Now take my cum, whore!"
    hide screen textbox2 with dissolve
    play sound "sound effects/spurt.wav"
    scene w1_3461 with dissolve
    show screen camcorder
    "Aiming his dick at center mass, the talkative businessman's cockhead exploded, shooting a thick stream of white all over her face, chest, and stomach."
    fel "Eeeh...! Gh...! Woah-!"
    scene w1_3462 with dissolve
    fel "That feels... good on my skin? What the hell...?"
    eric "I think I might just line up again."
    kat "You hear that? Your first repeat customer. How wonderful."
    scene w1_3463 with fade
    "True to what he said, Eric hobbled to the back of the group of gathering men and allowed another one to take his place."

    if w1ExTenorRepeat == True:
        "Vincenzo Bianchi - the apparently world famous tenor I had seen in the hall."
    else:
        "A fat, disgusting man with an even creepier smile."


    fel "Thank you for your interest as well, mister."
    "Felicia showed her appreciation in a clear, measured tone."
    fel "Please, enjoy your time as well."
    scene black with fade
    "......"
    "..."
    scene w1_3464 with fade
    fel "Jeez, there's so many of you!"
    frank "I usually prefer women with more meat on them, but you're actually not so bad looking up close."
    jim "I'm next, before this whore becomes too disgusting!"
    frank "Really? You seemed so price shy earlier."
    jim "Eric made a good point. It's not everyday you get cum on the face of the wife of a rich, influential man."
    scene w1_3465 with fade
    play sound "sound effects/spurt.wav"
    "Over the next however long, various patrons used Felicia as a perverted canvas, spilling their ejaculate wherever they desired on the shackled woman's body."
    "Patron by patron, Felicia's golden, spotless skin was marred and dyed in white."
    scene w1_3466 with fade
    play sound "sound effects/spurt.wav"
    "I watched as the confident, cocksure woman devolved into a mindless puddle of hedonism."
    eric "This is what I was waiting to see!"
    "Bill after hundred dollar bill pilled up around Felicia's soiled body."
    sam "She's beginning to smell like a sewer. Eugh!"
    "It made for quite the sight, driving home to all onlookers the golden beauty's fall from rich housewife to common whore."
    scene w1_3467 with fade
    play sound "sound effects/vib-start.wav"
    fel "Fwoo-h! Oooh! Gheee...!"
    "Every time a man unloaded onto her chest or face, more and more of Felicia disappeared."
    eric "Ah, I'm back! Ready for another load? "
    "It had even gotten back to Felicia's number one fan."
    scene w1_3468 with fade
    fel "Gh.... ohoh, w-wait... Ian?"
    scene w1_3477 with dissolve
    "Killian had stepped up to the plate, tossing down a wad of cash and furiously stroking his cock."
    fel "Couldn't help--"
    hide screen camcorder with dissolve
    scene w1_3469 with dissolve
    show screen textbox2 with dissolve
    kil "Shut up."
    scene w1_3470 with dissolve
    "Ian practically growled at Felicia."
    fel "What?"
    scene w1_3469 with dissolve
    kil "I said shut the fuck up, bitch!"
    hide screen textbox2 with dissolve
    show screen camcorder
    scene w1ExGame3Fel2 with dissolve
    "Felicia looked visibly confused at Killian sudden shift in attitude."
    mct "(As was I, quite frankly...)"
    kil "Y'know, I always kind of wanted to say that to you..."
    kil "Outside these walls, you're a friend. In here, you're just a nasty slut who should shut her damn yap when a customer tells her to."
    fel "Wh-- Mmmh...!"
    "Felicia had to stop herself from responding."
    kil "Heh, good girl! You really do understand how to play the game."
    play sound "sound effects/vib-start.wav"
    fel "*Bzzt!* Ge-eh...!"
    kil "I almost wish I could snap a picture and let Mina take a peep at this. She thinks you're so cool, you know that?"
    kil "This would totally shatter that illusion."
    "For whatever reason, Killian was without a doubt reveling in the chance to talk down to Felicia."
    hide screen camcorder
    scene w1_3474 with dissolve
    show screen textbox2 with dissolve
    fel "Eh... oooooh! S-she'd have an aneurysm, wouldn't she?"
    scene w1_3469 with dissolve
    kil "That thought turns you on?"
    scene w1_3470 with dissolve
    fel "*Bzzt* Ehehhe....! Y-yes...!"
    scene w1_3475 with dissolve
    kil "Ha! You fucking slut!"
    fel "Oh... oh... no...!"
    fel "OoooooOOoooooh-!" with vpunch
    play sound "sound effects/vib-start.wav"
    fel "*{b}Bzzzzzzzzzzt!{/b} Egheeeee!*" with vpunch
    "A shrill cry briefly over-powered the dull persistent buzz of the toy jammed in her cunt. A prelude to..."
    scene w1_3476 with w19
    play sound "sound effects/vib-start.wav"
    "Felicia creaming herself, squirting a clear stream of liquid out of her overstuffed hole until it reached it's apex and rained back down on her face." with vpunch
    "Adding her own flavor into the mess."
    scene w1_3418 with dissolve
    chuck "I bet you didn't think to bring any cash with you tonight, lad."
    scene w1_3419 with dissolve
    mc "Ah, well... it's too rich for me anyway."
    scene w1_3421 with dissolve
    "Holding out his hand, Dr. Chuck offered me a neat stack of bills."
    scene w1_3420 with dissolve
    chuck "Go enjoy yourself. I'll take over filming! Consider it a gift from your Uncle Chuck!"
    scene w1_3477 with dissolve
    "Stealing one last glance over at Felicia and the gathered men, something about the scenario tempted me."
    scene w1_3421 with dissolve
    mct "(...{i}do I{/i} want to take part in this?)"
    stop music fadeout 3.0
    hide screen textbox2 with dissolve

    menu:
        "Join in on the fun. [gr]\[Killian +2\]":
            $ Killian_Bromance += 2

            show screen textbox2 with dissolve
            mct "(Deep down... yeah, I do.)"
            "Plus, I suppose in a twisted way, this technically helps Felicia out."
            scene w1_3422 with dissolve

            if chuck_polite == True:
                mc "Thank you for your generosity, sir."
            if chuck_uncle == True:
                mc "Thanks for your generosity, Uncle Chuck."
            else:
                mc "Thank you for your generosity, Dr. Chuck."

            chuck "Don't mention it, lad. Besides, I wouldn't mind some time behind the camera, heh..."
            "Dr. Chuck flashed me a knowing smile in perverted solidarity."
            scene black with fade
            "Taking the cash and adding it to the other bills surrounding Felicia's grimy body, I discarded my clothes and found a place next to my friend."
            play music "music/doll-dancing.mp3"
            scene w1_3478 with dissolve
            kil "Heh, look who's joining us! It's our mutual friend [mcf]!"
            kil "He's come to jerk off on you while you're folded over like a pretzel!"
            scene w1_3479 with dissolve
            mc "Don't make this weird..."
            scene w1_3478 with dissolve
            kil "Too late for that! Might as well lean into it. Enjoy having a mutual wank with your best bud onto some slut!"
            scene w1_3480 with dissolve
            fel "Y-yeah, we're past that by the point, right? Just enjoy yourself, [felSN]."
            scene w1_3481 with dissolve
            mct "(Well... if you insist.)"
            scene w1ExGame3Fel3 with dissolve
            "Shutting everything out, I decided to focus on the sight in front of me. The sight of Felicia, drowning in baby batter, money strewn about her like an expensive whore."
            "The way she was spattered with cum, jizz leaking down her torso and pooling in between her gorgeous breasts."
            "How that dripped even further, spilling down her neckline and onto her chin..."
            "It was {i}utterly{/i} disgusting, yet... I furiously stroked my cock with wild abandon, like I hadn't jerked it in a week."
            fel "Geh.... eh...."
            "Felicia wasn't quite focusing on anything in particular. Every so often her eyeline would veer over to my cock, but it was never held long before her eyes lost focus again."
            kil "You getting close, bro?"
            mc "H-huh?"
            "Killian's question pulled me back to reality."
            kil "I asked if you're about to bust a nut."
            mc "Uh, yeah. I'm about there I guess..."
            kil "Why don't we hose down this slut at the same time?"
            mc "Heh, okay."
            kil "Great! Hey, Felish... you should ask for it. Ask for our cum."
            scene w1_3486 with dissolve
            fel "Like you wouldn't finish anyway if I didn't."
            scene w1_3487 with dissolve
            kil "I said beg for it, bitch."
            play sound "sound effects/vib-start.wav"
            scene w1_3488 with dissolve
            fel "*Bzzzt* Mmmh, fine...!"
            fel "[mcf], Ian... hurry up and give me a large, thick dose of your jizz! Please!"
            scene w1ExGame3Fel3 with dissolve
            kil "Ha! Good enough, you ready [mcf]?"
            "Giving Ian a nod, I focused my gaze on Felicia and allowed my hand to finally bring myself over the edge."
            play sound "sound effects/spurt.wav"
            scene w1_3485 with flash
            mc "Gh-!"
            play sound "sound effects/spurt.wav"
            kil "Ah, ngh- fuck yeah!" with flash
            "Simultaneously, we both unleased a torrent of cum on the shackled beauty."
            scene w1_3489 with dissolve
            fel "Eh, oh...! Fhuck... dhat's ahlots..."
            fel "E-emmprhessive..."
            "Our combined effort had Felicia looking like a glazed donut."
            scene black with fade
            kil "Ah, nice one, bro..."
            mc "Yeah, you too..."
            mct "(Shit, that was weird...)"


        "Just keep filming.":
            scene w1_3423 with dissolve
            show screen textbox2 with dissolve
            if chuck_polite == True:
                mc "No, but thanks for the kind offer, sir."
            if chuck_uncle == True:
                mc "No, but thanks for the kind offer, Uncle Chuck."
            else:
                mc "No, but thanks for the kind offer, Dr. Chuck."

            scene w1_3418 with dissolve
            chuck "Really, lad?"
            scene w1_3419 with dissolve
            mc "I guess kinda like it behind the camera."
            scene w1_3424 with dissolve
            "Dr. Chuck flashed me a knowing smile in perverted solidarity."
            chuck "Heh, that I understand!"
            hide screen textbox2 with dissolve
            scene black with fade
            show screen camcorder with dissolve
            "Patting me on the back, Dr. Chuck veered off and I turned my attention back to the stage."
            scene w1ExGame3Fel4 with dissolve
            play music "music/on-the-ground.mp3"
            kil "Mmmh..."
            "Killian was stroking his cock furiously, seemingly not a care in the world."
            kil "You're so damn hot. I kinda wish I knew you when you were 21!"
            kil "Not that you don't still got it..."
            scene w1_3486 with dissolve
            fel "Just shut up and jerk your cock your cocky bastard."
            scene w1_3487 with dissolve
            kil "Oh, you want it?"
            scene w1_3486 with dissolve
            fel "Well, I got to make money and you're taking an awful long time."
            scene w1ExGame3Fel4 with dissolve
            "Tuning Ian's inane comments out, I decided to focus on the sight in front of me. The sight of Felicia, drowning in baby batter, money strewn about her like an expensive whore."
            "The way she was spattered with cum, jizz leaking down her torso and pooling in between her gorgeous breasts."
            "How that dripped even further, spilling down her neckline and onto her chin..."
            kil "Ah! Take it, you gold digging bitch!"
            play sound "sound effects/spurt.wav"
            scene w1_3493 with dissolve
            kil "Ah, ngh- fuck yeah!"
            "With a short, barbarous grunt Ian let loose a torrent of jizz onto Felicia's face."
            kil "G-ah, gnnh!"
            fel "Guh..?!"
            scene w1_3494 with dissolve
            "By luck or extraordinary aim, Ian had shot his load straight into Felicia's gaping mouth and down the back of her throat."
            fel "Guh--huh...!"
            kil "Ah, that was fun. I think I could go again..."
            hide screen camcorder
            show screen textbox2 with dissolve

    scene black with fade
    stop music fadeout 3.0
    "The scene continued on for twenty more minutes, by the end of it..."
    scene w1_3495 with dissolve
    $ history_felicia = "Felicia took part in this week's final game, managing to make enough money to go into the next week on equal footing with the other two Carnations."
    $ unread_felicia = True
    play sound "sound effects/notification.wav"
    show bioupdate with dissolve
    fel "Eguh... eoh...."
    kat "You look absolutely disgusting, pig."
    fel "Eheh... oh..."
    frank "The bitch really reeks!"
    mihir "It's fucking putrid is what it is."
    chuck "You did amazing! Good job, Felicia!"
    scene black with fade

    if not persistent.w1ExGame3FelGallery:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w1ExGame3FelGallery = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)

    "Felicia had made her buck."
    "......"
    "..."
    $ renpy.end_replay()
    jump w1ExKatEnding


label w1ExEarningsGameVeronica:

    if _in_replay:
        show screen textbox2 with dissolve

    scene black with fade
    "......"
    hide screen textbox2 with dissolve
    show screen camcorder with dissolve
    "..."
    play music "music/beginning-of-conflict.mp3"
    scene w1_3496 with fade
    ver "Ng...! What the hell did you just inject me with?! I feel...!"
    scene w1_3497 with dissolve
    kat "Turned on?"
    scene w1_3499 with dissolve
    ver "Yes!"
    hide screen camcorder
    scene w1_3447 with dissolve
    show screen textbox2 with dissolve
    kat "Relax, Miss Lynch. It's just something to make things more interesting, for both us and for you."
    kat "You should be somewhat familiar with it. You had a taste just a few weeks ago."
    scene w1_3448 with dissolve
    ver "That sex drug...?"
    hide screen textbox2 with dissolve
    show screen camcorder
    scene w1_3497 with dissolve
    kat "Precisely."
    scene w1_3497 with dissolve

    if w1GonzoReward:
        "I watched from the sidelines, as that all-too-familiar aphrodisiac began sinking it's devious claws into the stretched out amazon."
    else:
        "I watched as the aphrodisiac began sinking it's claws into the stretched out amazon."

    scene w1_3500 with dissolve
    ver "Eh... damn this! My head is feeling all foggy..."
    scene w1_3498 with dissolve
    kat "It's going to be a wild time if you're already feeling it that strongly. It's barely had time to kick in."
    scene w1_3499 with dissolve
    ver "It's gonna get more intense?"
    hide screen camcorder
    scene w1_3450 with dissolve
    show screen textbox2 with dissolve
    kat "Oh, you're in for a {i}real{/i} treat."
    scene w1_3449 with dissolve
    ver "I don't... like the sound of that."
    scene black with fade
    hide screen textbox2 with dissolve
    show screen camcorder with dissolve
    ver "H-hey, I can't see...!"
    play sound "sound effects/vib-start.wav"
    ver "Ghe-!"
    scene w1_3501 with fade
    ver "Oooooooooh! That's...! Gh-"
    "Mrs. Pulman had blindfolded the bound woman, attaching a set of clothes pins and placing a large vibrator in her pussy."
    ver "Egh, intense!"
    "Veronica's hips violently jerked, but she she was stretched so taut over the table that it barely moved in response."
    "Tied down as she was, she had little choice but to accept the devious fate that loomed over her."
    hide screen camcorder
    scene w1_3403 with dissolve
    show screen textbox2 with dissolve
    "I had been tasked with recording the event, something that no one had a problem with. In actuality, they seemed excited at the opportunity to have a copy of the debauchery for home consumption."
    "It seemed awfully gauche to me, that these men with all their money and access, would jack off at home like a common pervert."
    show screen camcorder
    scene w1ExGame3Vero with dissolve
    sam "Finally..."
    ver "S-sam? Is that you?"
    sam "Hehe, you betcha. No danger of you busting my nose again when you're strapped down like this."
    ver "You're such a fucking creep...!."
    scene w1_3505 with dissolve
    sam "Hey, don't be a bitch. I'm the one who got you in the door to this place."
    scene w1_3506 with dissolve
    ver "So you can jerk off on my face?"
    scene w1_3505 with dissolve
    sam "Ha! That's just a bonus for me. Truth is, I'm only trying to help your gym to survive."
    play sound "sound effects/vib-start.wav"
    scene w1_3507 with vpunch
    ver"*Bzzt* Y-yeah, right."
    scene w1_3508 with dissolve
    sam "You should drop the attitude and be more thankful that you've been afforded this opportunity."
    sam "Not everyone is given the chance to fix their mistakes."
    scene w1_3509 with dissolve
    ver "Ghmmh..."
    scene w1ExGame3Vero with dissolve
    "Samson taunted the stretched out woman. Something that seemed incredibly viscous to me, considering I'd just learned hours ago about his hand in Veronica's misfortune."
    sam "You look good on your back, Nicki. You're practically a natural."
    sam "The hard work required to sculpt that perfect body of yours... I bet you couldn't have imagined all that effort and sweat going toward being eye candy for your betters. Hehehe..."
    ver "Better? Get real! You're a washed up old actor riding the coat tails of a few mediocre hits."
    sam "Oh? Hohoho..."
    sam "I'm not the one laid out on a table, tied down, tits sticking out with a man beating his cock in my face right now!"
    scene w1_3510 with dissolve
    jiji "Don't let Mr. Garcia's crude attitude get to you. You're a remarkable looking woman. You must be quite disciplined."
    scene w1_3511 with dissolve
    ver "Eh-? Ahh...! W-who's that?"
    scene w1_3510 with dissolve
    jiji "My name is Kristoff Jostad Jameson. You can call me JJ if you wish."
    scene w1_3507 with dissolve
    ver "You're the man with the silly mustache?"
    scene w1_3508 with dissolve
    jiji "I thought it was distinguished."
    scene w1_3507 with dissolve
    ver "Not really. It's the 21st century."
    scene w1_3508 with dissolve
    jiji "A little word of advice..."
    play sound "sound effects/spurt.wav"
    scene w1_3512 with dissolve
    jiji "Gh!"
    scene w1_3513 with dissolve
    jiji "Even if you don't really mean it, do a better job at accepting an olive branch when it's handed to you."
    scene w1_3514 with dissolve
    "With those parting words, the tall man marched off the stage, leaving Samson at the amazon's head."
    scene w1_3515 with dissolve
    sam "Damn! I was hoping I'd be the first. Oh, well!"
    scene w1_3516 with dissolve
    sam "Take it!"
    play sound "sound effects/spurt.wav"
    scene w1_3517 with dissolve
    sam "Aaaarrgh!"
    "Aiming his dick straight at Veronica's face, the large man's cockhead exploded, sending thick ropes of jizz splashing down on his target."
    scene w1_3518 with dissolve
    ver "Eh?!"
    sam "Ah... that was nice. Can't wait to do this again, heheh..."
    sam "Looks like you've got the club's interest, Nicki. The men are lining up!"
    scene black with fade
    "......"
    "..."
    scene w1_3551 with dissolve
    ver "Eugh...! The smell!"
    mihir "*Fwooo* She's a big bitch."
    jim "I'm next, before this whore becomes too disgusting!"
    frank "Ahaha, you seemed so price shy earlier!"
    jim "Can it, a man can change his mind."
    scene w1_3552 with fade
    "Over the next however long, various patrons used Veronica as a perverted canvas, spilling their ejaculate wherever they desired on the bound amazon's body."
    "One load after another, Veronica's well defined musculature was being obscured by a slick, slimy coat of jizz."
    play sound "sound effects/vib-start.wav"
    ver "*Bzzt* Ugh... it's still not over...?"
    "Being blindfolded, Veronica had no way of telling how many men was pooling around her."
    "She had no inkling that some were even lining up for seconds."
    "Slowly the stress and humiliation had dulled Veronica's fiery attitude and she looked lesser."
    scene w1_3553 with fade
    play sound "sound effects/spurt.wav"
    ver "Eh... oh...! Shwwhit!"
    "Despite her disdain, her lower half painted a different story."
    "Her abdomen and buttocks ebbed and flowed alongside the vibrator crammed in her cunny."
    ver "Gh- what -ah!- what's taking so long here?"
    scene w1_3554 with fade
    play sound "sound effects/spurt.wav"
    "Bill after hundred dollar bill pilled up around Veronica's soiled body."
    "It made for quite the sight, solidifying Veronica's place on the pecking order as a whore like any other."
    play sound "sound effects/vib-start.wav"
    ver "*Bzzt* Ghee...! Ah! Fhuccccck...!" with vpunch
    ver "I'm just getting hornier and hornier!"
    kat "Oh? Not satisfied with just the toy? Too bad."
    kat "That's all you'll get, so you better make do."
    "The scene continued, with more and more of Veronica disappearing under a veneer of cum."
    sam "Hey there, Nicki. Ready for seconds?"
    scene black with fade
    "..."
    scene w1ExGame3Vero2 with dissolve
    "Even my best friend stepped up to the plate."
    kil "Hey there, beautiful. Come here often?"
    "Killian chuckled at his own stupid joke."
    ver "That voice... that you, ginger boy?"
    kil "Yep, it's me. Sorry, I couldn't help myself. [mcf] got to have all the fun earlier."
    kil "It got me all worked up. You don't mind, do you {b}hun{/b}?"
    "He was enjoying condescending down to Veronica, that was for sure."
    scene w1_3522 with dissolve
    ver "Gh! What the fuck do I care? You or those old farts, doesn't matter to me. Just give me your money."
    scene w1_3523 with dissolve
    kil "You're sounding like a proper whore all of a sudden."
    play sound "sound effects/vib-start.wav"
    scene w1_3522 with vpunch
    ver "*Bzzzt* Whateeeever i-t takes to win!"
    hide screen camcorder
    scene w1_3418 with dissolve
    show screen textbox2 with dissolve
    chuck "I bet you didn't think to bring any cash with you tonight, lad."
    scene w1_3419 with dissolve
    mc "Ah, well... it's too rich for me anyway."
    scene w1_3421 with dissolve
    "Holding out his hand, Dr. Chuck offered me a neat stack of bills."
    scene w1_3420 with dissolve
    chuck "Go enjoy yourself. I'll take over filming! Consider it a gift from your Uncle Chuck!"
    scene w1_3477 with dissolve
    "Stealing one last glance over at Veronica and the gathered men, something about the scenario tempted me."
    scene w1_3421 with dissolve
    mct "(...{i}do I{/i} want to take part in this?)"
    stop music fadeout 3.0
    hide screen textbox2 with dissolve

    menu:
        "Join in on the fun. [gr]\[Killian +2\] [red]\[Veronica -1\]":
            $ Killian_Bromance += 2
            $ Veronica_Affection -= 1

            show screen textbox2 with dissolve
            mct "(Deep down... yeah, I do.)"
            "Plus, I suppose in a twisted way, this technically helps Veronica out."
            scene w1_3422 with dissolve

            if chuck_polite == True:
                mc "Thank you for your generosity, sir."
            if chuck_uncle == True:
                mc "Thanks for your generosity, Uncle Chuck."
            else:
                mc "Thank you for your generosity, Dr. Chuck."

            chuck "Don't mention it, lad. Besides, I wouldn't mind some time behind the camera, heh..."
            "Dr. Chuck flashed me a knowing smile in perverted solidarity."
            scene black with fade
            "Taking the cash and adding it to the other bills surrounding Veronica's grimy body, I discarded my clothes and found a place next to my friend."
            scene w1_3524 with fade
            play music "music/doll-dancing.mp3"
            kil "Couldn't help but join in, eh?"
            scene w1_3525 with dissolve
            mc "When in Rome..."
            scene w1_3524 with dissolve
            kil "Be a fucking degenerate?"
            play sound "sound effects/vib-start.wav"
            scene w1_3526 with dissolve
            ver "*Bzzt!* H-huh? Errand boy?"
            scene w1_3527 with dissolve
            mc "Hi, Veronica. Hope you're not too surprised to see me."
            scene w1_3526 with dissolve
            ver "The more, t-the... gn-the merrier."
            scene w1_3524 with dissolve
            kil "Hear that, bro? She's happy you joined in."
            scene w1ExGame3Vero3 with dissolve
            "Shutting out Ian's inane comments, I decided to focus on the sight in front of me. The sight of Veronica, with rippling muscles anointed in jizz and money strewn about her like an expensive whore."
            "The way the spunk pooled in the curvature of her stomach, her chest rising and falling along with her breath..."
            "The way the spunk clung to her puffy clothes-pin attached nipples, the appalling amount of ejaculate making her reddened teats look like frosted cherries."
            "It was {i}utterly{/i} disgusting, yet... I furiously stroked my cock with wild abandon, like I hadn't jerked it in a week."
            scene w1_3531 with dissolve
            ver "Ngh..! Eeeeeugh, h-how close am I to the four grand, errand boy?"
            "Veronica's question pulled me back to my senses."
            scene w1_3532 with dissolve
            mc "Uh, well..."
            scene w1_3533 with dissolve
            "I took a look at all the discarded bills, the ones that laid next to her and the ones that clung to her soiled skin, trying to mentally calculate the total in the vain."
            scene w1_3532 with dissolve
            mc "It's kind of hard to tell, but you probably have a ways to go if I had to guess."
            scene w1_3531 with dissolve
            ver "Mmmh...! Damn! Y-you two should hurry up then!"
            scene w1ExGame3Vero3 with dissolve
            kil "Don't rush me. You'll get your helping of my cum when I'm -ngh, r-ready."
            kil "However, it just show happens I'm about to be ready. What about you, [mcf]?"
            mc "Sorry, what are you asking me?"
            kil "I'm asking if you're about to pop your top."
            mc "Uh, yeah. I'm about there I guess..."
            kil "Then after you, my good man."
            scene w1_3535 with dissolve
            kil "Open up, slut. My buddy's about to make a deposit!"
            ver "G-geh?! Sptt...!"
            "Ian pinched the bound woman's nose tightly shut, to prompt the amazon to open her mouth."
            scene w1_3534 with dissolve
            ver "What do you think you're doing, boy?"
            scene w1_3535 with dissolve
            kil "Uh uh uh... open a little wider."
            ver "Gh....!"
            scene w1_3536 with dissolve
            "Veronica complied, but not before letting out an exasperated growl."
            kil "Well, what are you waiting for? Cum down her throat!"
            scene w1_3537 with dissolve
            "With Ian's assistence in keeping her mouth a target, I aimed my cock at the general direction of Veronica's lips."
            mc "Gh-! Here it comes, Veronica...!"
            play sound "sound effects/vib-start.wav"
            scene w1_3538 with vpunch
            ver "*Bzzt* D-do it!"
            scene w1_3537 with dissolve
            kil "Go ahead. Let her have it!"
            play sound "sound effects/spurt.wav"
            scene w1_3539 with flash
            mc "Oh, ng! Oooh!"
            "Encouraged, my testes tightened and my glans expanded to let out a deluge of semen that found its way into Veronica's mouth like a heat-seeking cumshot."
            scene w1_3540 with dissolve
            ver "Guh! *cough* Ehng... fhu-- ack!"
            "The spunk near instantly hit the back of Veronica's throat, clinging to it like cellophane and causing the redheaded beauty to choke and gag."
            scene w1_3541 with dissolve
            ver "*Cough, cough!* Yak-! *Cough, cough!* Eguh..!"
            kil "Heh, nice one. Nothing but net!"
            kil "Me? I'm going to go for a rimshot."
            mc "Don't you think you're taking the sports metaphors a little too..."
            kil "Arg, here it comes!"
            play sound "sound effects/spurt.wav"
            scene w1_3542 with dissolve
            kil "Oognh!"
            "Letting out a cry that sounded like an injured dog, Killian angled his cock and let out his orgasm all over the blindfolded womans' face."
            scene w1_3543 with dissolve
            "Veronica was looking like a glazed donut."
            ver "Gh!"
            kil "Ah...! Oh, man. That was fun."
            scene black with fade
            kil "We should do this kind of thing more often, [mcf]."
            mc "Don't be weird."
            kil "Like it isn't already?"
            "......"
            "..."

        "Just keep filming.":
            scene w1_3423 with dissolve
            show screen textbox2 with dissolve
            if chuck_polite == True:
                mc "No, but thanks for the kind offer, sir."
            if chuck_uncle == True:
                mc "No, but thanks for the kind offer, Uncle Chuck."
            else:
                mc "No, but thanks for the kind offer, Dr. Chuck."

            scene w1_3418 with dissolve
            chuck "Really, lad?"
            scene w1_3419 with dissolve
            mc "I guess kinda like it behind the camera."
            scene w1_3424 with dissolve
            "Dr. Chuck flashed me a knowing smile in perverted solidarity."
            chuck "Heh, that I understand!"
            scene black with fade
            "Patting me on the back, Dr. Chuck veered off and I turned my attention back to the stage."
            scene w1ExGame3Vero2 with dissolve
            play music "music/on-the-ground.mp3"
            kil "You know there's something about you, Veronica."
            play sound "sound effects/vib-start.wav"
            ver "*Bzzt!* W-what's that?"
            kil "Beats me. I never thought I'd be into a woman like you, but I find you attractive."
            kil "I guess I like seeing a strong woman put on her back. No offense, I know that sounds awful, but these kind of things are outside value judgements."
            kil "It's just pure animal feeling."
            ver "Gh! Ghe, what the hell are you talking about, you fucking weirdo?"
            kil "Eh, just thinking out loud I guess."
            "Shutting out Ian's inane comments, I decided to focus on the sight in front of me. The sight of Veronica, with rippling muscles anointed in jizz and money strewn about her like an expensive whore."
            "The way the spunk pooled in the curvature of her stomach, her chest rising and falling along with her breath..."
            "The way it clung to her puffy clothes-pin attached nipples, the appalling amount of ejaculate making her reddened teats look like frosted cherries."
            scene w1_3522 with dissolve
            ver "Ngh..! Eeeeeugh, h-how close am I to the four grand?"
            scene w1_3545 with dissolve
            "Veronica's question pulled me back to my senses."
            kil "You've got a ways to go."
            scene w1_3544 with dissolve
            ver "Mmmh...! Damn! Y-you should hurry up then!"
            scene w1_3523 with dissolve
            kil "Don't rush me, bitch. I'll cum when I'm ready. You just sit there and wait, okay?"
            scene w1_3522 with dissolve
            ver "Grh..."
            scene w1_3546 with dissolve
            kil "It just so happens I'm ready. Open up wide, okay? I'm gonna make a direct deposit."
            "Killian moved up to Veronica's head and aimed his dick, but Veronica didn't comply."
            kil "I said open up and say \"aaaaah\"."
            ver "Mmmg..."
            scene w1_3547 with dissolve
            kil "'atta girl! Here it comes! Take it!"
            play sound "sound effects/spurt.wav"
            scene w1_3548 with dissolve
            kil "Oognh!"
            "Letting out a cry that sounded like an injured dog, missed his mark of the inside of Veronica's mouth and instead plastered her face with his seed."
            scene w1_3549 with dissolve
            ver "Ugh..."
            kil "Ah, that was fun. I think I could go again..."

    scene black with fade
    stop music fadeout 3.0
    if not persistent.w1ExGame3VeroGallery:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w1ExGame3VeroGallery = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)
    "The scene continued on for twenty more minutes, by the end of it..."
    scene w1_3550 with dissolve
    ver "Eguh, disgusting..."
    kat "You're not wrong about that, dear."
    ver "I- iss it finished? Did I make enough?"
    kat "Looks like it."
    sam "Oh, man. That was awesome."
    chuck "You did amazing! Good job, Veronica!"
    scene black with fade
    $ history_veronica = "Felicia took part in this week's final game, managing to make enough money to go into the next week on equal footing with the other two Carnations."
    $ unread_veronica = True
    play sound "sound effects/notification.wav"
    show bioupdate with dissolve
    "Veronica had made her quota and then some. She proved surprisingly popular."
    "......"
    "..."
    $ renpy.end_replay()
    jump w1ExKatEnding






label w1ExHanaHangout:

    stop music fadeout 3.0
    scene w1_3555 with fade
    mc "Hey, if Mrs. Pulman asks, I ducked out of here to check on Hana."
    scene w1_3556 with dissolve
    kil "You sure you want to be barking up that tree? Her being the boss' daughter, I mean..."
    scene w1_3559 with dissolve
    mc "What? No. It's not like that. I've just seen enough exhibitionist sex to last me a lifetime."
    scene w1_3557 with dissolve
    kil "Well, if you want to miss all the fun, be my guest. I'll let Mrs. Pulman know where to find you."
    scene w1_3558 with dissolve
    mc "You have any idea where she'd be?"
    scene w1_3557 with dissolve
    kil "Try the VIP lounge's bar. That's where the drinks come from when we're down here."
    scene w1_3558 with dissolve
    mc "Thanks, Ian."
    scene w1_3560 with dissolve
    kil "No problem, man."
    scene black with fade
    "Doing my best to look inconspicuous, I moved along the edge of the room until I reached the exit and headed towards the basement's bar."
    "......"
    "..."
    scene w1_3561 with cmet
    play music "music/jazz-piano-bar.mp3"
    "Once there, I spotted not only Hana, but also Lucy."
    "I could tell by the look on her face and the way she slumped her shoulders that she was troubled."
    hana "Oh, [mcf]!"
    "My entrance interrupted the pair's conversation, with Hana giving me a wave over."
    hana "Come join us."
    scene w1_3562 with wiperight
    mc "What are you two up to?"
    scene w1_3563 with dissolve
    hana "I was just listening to Lucy's problems."
    scene w1_3564 with dissolve
    mc "You sound like a real bartender, you know that."
    scene w1_3565 with dissolve
    hana "What brings you here? The house girls usually bring the drinks."
    scene w1_3564 with dissolve
    mc "Nah, I left the show early. I'd seen enough."
    scene w1_3566 with dissolve
    hana "Good choice. You want something to wet your whistle?"
    scene w1_3567 with dissolve
    mc "No thanks. How are you Lucy?"
    scene w1_3568 with dissolve
    "I asked, although..."
    "I could guess the true answer wasn't positive."
    scene w1_3569 with dissolve
    lucy "I'm... fine."
    scene w1_3570 with dissolve
    mc "I guess I would have trouble imagining, huh?"
    scene w1_3571 with dissolve
    hana "She was just telling me the reason she's here. You're familiar, right?"
    scene w1_3569 with dissolve
    lucy "I want to get my son into St. Ives."
    scene w1_3572 with dissolve
    hana "Jeez, is that really worth whoring yourself out? What's so damn great about that school?"
    scene w1_3573 with dissolve
    mc "It means you get into your choice college for one. It sets you up for life."
    scene w1_3574 with dissolve
    lucy "Ah... what he said, basically."
    scene w1_3575 with dissolve
    hana "So? Having everything handed to you just turns a brat into a shitty adult."
    scene w1_3576 with dissolve
    mc "I didn't peg you as a pull yourself up by your bootstraps kind of girl."
    scene w1_3577 with dissolve
    hana "I know the value of hard work, but I guess I also know that only gets you so far..."
    scene w1_3572 with dissolve
    hana "You must really care about your kid's future to be subjecting yourself to this."
    scene w1_3578 with dissolve
    lucy "That's the thing... I don't know anymore. Mrs. Pulman called it vanity and I don't know if I can one hundred percent deny that."
    scene w1_3579 with dissolve
    hana "Don't let her fuck with your head. She likes to make whales believe they're minnows. She's a real nasty bitch."
    scene w1_3580 with dissolve
    lucy "..."
    scene w1_3581 with dissolve
    mc "Yeah, listen to Hana. My own mother endured something similar and it's not like she did it because I'd go hungry otherwise."
    scene w1_3582 with dissolve
    hana "What do you mean?"
    scene w1_3583 with dissolve

    if hanaFlag == True:
        mc "Well, I told you my mom did porn after my father's death."
        scene w1_3584 with dissolve
        hana "Yeah, we got that in common. Sort of."
    else:
        mc "My mother worked as a porn star for awhile, following my father's death."
        scene w1_3585 with dissolve
        hana "Shit? For real?"

    scene w1_3581 with dissolve
    mc "As best as I can guess, she did it so things wouldn't change too much for me. So my life wouldn't be upended more than it already was."
    mc "You know, so we wouldn't have to move. So I didn't have to change schools..."
    mc "I guess she thought it was important for a kid to have a sense of normalcy in their life after something like that. I dunno. Even now, I don't quite get it."
    mc "Point being, I don't think you're necessarily being frivolous."
    scene w1_3586 with dissolve
    lucy "...thanks, [mcf]. I know you're just saying that, but I appreciate the sentiment."
    scene w1_3587 with dissolve
    lucy "I need to go get washed up. Apparently I need to be available for after the exhibition."
    hana "Sure, see you around."
    mc "Bye."
    scene w1_3588 with dissolve
    "Lucy left, leaving just Hana and myself."
    scene w1_3589 with dissolve
    hana "*sigh* For the record, I think using sex to unfairly get your kid into a school is pretty scummy, but I didn't want to kick her while she's down."
    scene w1_3590 with dissolve
    mc "The world is scummy. It's not my place to judge."
    scene w1_3591 with dissolve
    hana "Can you guess how I found her earlier?"
    scene w1_3592 with dissolve
    mc "Tied up, stuffed with toys, left all alone?"
    scene w1_3591 with dissolve
    hana "Yeeeeeah..."
    scene w1_3593 with dissolve
    "There was a brief, but hefty moment of silence to our talk."
    scene w1_3595 with dissolve
    hana "Welp, so you came to see little ol' me?"
    scene w1_3594 with dissolve
    mc "Just repaying your visit from earlier."
    scene w1_3595 with dissolve
    hana "Heh, nice. Since you're here, you want to hit up the steam room? Always good to have a buddy in case you pass out."
    scene w1_3594 with dissolve
    mc "Shouldn't you be at the bar?"
    scene w1_3595 with dissolve
    hana "Shouldn't you be at the exhibition?"
    stop music fadeout 3.0
    scene black with fade
    mc "Good point."
    "......"
    "..."
    scene w1_3619 with w12
    play ambient "sound effects/sauna.mp3"
    mct "(Aaaaaah...)"
    mct "(After the first leg of the night, {b}damn, I'm tired{/b}.)"
    "I was glad I went along with Hana's suggestion. It kinda felt like I was playing hooky."
    mct "(Plus... half dressed in a sauna with a beauty like Hana... yeah, this was certainly a better way of ending the night than sticking around for a circle jerk.)"
    scene w1_3596 with dissolve
    hana "This place does have its perks."
    hana "Why the hell does feeling like you're being smothered with heat feel sooooooo good?"
    scene w1_3597 with dissolve
    mc "Do you actually want an answer to that?"
    scene w1_3598 with dissolve
    hana "You have one for me?"
    scene w1_3597 with dissolve
    mc "The heat causes your blood vessels to expand, increasing blood flow, improving circulation, loosening tight muscles and clearing out built-up lactic acid."
    scene w1_3599 with dissolve
    hana "Ha, you fucking nerd."
    scene w1_3600 with dissolve
    "For a minute going on forever, Hana and I shared a comfortable silence. One of those rare moments where nothing in your head wants to get out."
    scene w1_3601 with dissolve
    hana "Hmm...~ Hmmmhmmmh...~"
    "......"
    "..."
    scene w1_3602 with dissolve
    stop ambient fadeout 3.0
    play music "music/jazz-apricot.mp3"
    hana "You ever been in love [mcf]?"
    scene w1_3603 with dissolve
    mc "The hell? Where's that coming from?"
    scene w1_3604 with dissolve
    hana "Things were getting a little too comfortable, so I thought I'd ask you an embarrassing personal question."
    hana "You don't have to answer, but I'm a tit-for-tat girl."
    scene w1_3603 with dissolve
    mc "You mean, I get to ask you something if I answer your question?"
    scene w1_3602 with dissolve
    hana "Correctomundo."
    scene w1_3606 with dissolve
    mc "Okay, fine. Have I ever been in love, eh?"
    scene w1_3609 with dissolve
    mc "It depends on how lax you definition of love is, I guess."
    scene w1_3608 with dissolve
    hana "We don't have to get philosophical about it. Why don't you tell me about your first crush?"
    hana "You're not from mars. You had one of those right?"
    scene w1_3606 with dissolve
    mc "Of course I did."
    scene w1_3607 with dissolve
    hana "So?"
    scene w1_3609 with dissolve
    mc "Well, you're going to think it's dorky."
    scene w1_3607 with dissolve
    hana "I like dorky. Tell me."
    scene w1_3606 with dissolve
    mc "Okay... well, my first crush was an older woman."
    scene w1_3607 with dissolve
    hana "What, like a schoolboy crush on your homeroom teacher?"
    scene w1_3611 with dissolve
    mc "It was the mother of a friend. For whatever reason, I've always had a thing for older women. It might've started her."
    scene w1_3613 with dissolve
    hana "It wasn't Ian's mom, was it?"
    scene w1_3614 with dissolve
    mc "Uh..."
    scene w1_3612 with dissolve
    hana "Ha, really? You had a crush on that asshole's mom? Did he know about it?"
    scene w1_3611 with dissolve
    mc "I don't think so, but maybe? This was a long, loooong time ago."
    scene w1_3607 with dissolve
    hana "What did you like about her?"
    scene w1_3609 with dissolve
    mc "As a kid? I don't know. Just one of those things. I thought she was pretty I guess."
    scene w1_3607 with dissolve
    hana "That's kinda basic, but it's sweet."
    hana "What about something more substantial?"
    scene w1_3606 with dissolve
    mc "That's a separate question. Don't I get to ask you something?"
    scene w1_3608 with dissolve
    hana "C'mon, just answer it! I'll let you ask me something real good after."
    scene w1_3617 with dissolve
    mc "Okay. Something more substantial, you said? Hmm..."
    scene w1_3627 with dissolve
    mc "There was my \"great\" high school love."
    scene w1_3628 with dissolve
    hana "That sounds more up my alley. Tell me more."
    scene w1_3627 with dissolve
    mc "It's more pathetic than anything. We'd been friends since grade school."
    scene w1_3628 with dissolve
    hana "What was she like?"
    scene w1_3609 with dissolve
    mc "She was a tomboy. The kind of girl that wasn't afraid of getting dirty during recess."
    mc "She was basically \"one of the boys\", until one day, she magically wasn't. She grew up and suddenly I was noticing new things about her."
    scene w1_3610 with dissolve
    hana "Puberty's a bitch."
    scene w1_3606 with dissolve
    mc "Anyway, that's when I started catching feelings for her. For the longest time, it was one sided."
    mc "It was unrequited all the way up to my junior year."
    scene w1_3613 with dissolve
    hana "Seriously? You never asked her out or anything before that? After seeing you with your cock out in front of a room full of old perverts, I wouldn't think you'd be so timid."
    scene w1_3614 with dissolve
    mc "It's not like I was a shy kid, but I did have a tendency to get stuck in my head and second guess things. So I just kept my feelings under wraps and mostly out of mind."
    scene w1_3620 with dissolve
    hana "What came after that longest time?"
    scene w1_3627 with dissolve
    mc "{b}She asked me out{/b}. We went to Junior-Senior prom. Dated a little while after that too, but things fizzled out pretty quick."
    mc "All that bluster and yearning and I realized I didn't even know her that well in the first place. Turns out I didn't like her that much."
    scene w1_3609 with dissolve
    mc "On the plus side, I learned about managing your expectations versus reality. After that came Marlow, but..."
    mc "That's a story for another time. I've spoken enough about my love life. It's your turn now."
    scene w1_3629 with dissolve
    hana "Hmmm? Huh? My turn for what?"
    scene w1_3616 with dissolve
    mc "Don't give me that look. Tit-for-tat, right?"
    scene w1_3623 with dissolve
    hana "Instead of asking me a question, wouldn't you rather see my tits?"
    scene w1_3624 with dissolve
    mc "Very funny."
    scene w1_3623 with dissolve
    hana "I'm serious. You want a look? I don't like talking about myself, but I did promise I'd give something in return."
    scene w1_3624 with dissolve
    mc "No, I want to ask you a question."
    scene w1_3626 with dissolve
    hana "Huh? What? {b}Really{/b}?"
    hana "I don't know if I should feel insulted or not."
    scene w1_3625 with dissolve
    mc "No offense, but there's a dozen topless women walking around downstairs."
    scene w1_3623 with dissolve
    hana "Yeah, but you haven't seen mine."
    scene w1_3625 with dissolve
    mc "Nice try, but you're not wiggling out of this."
    scene w1_3615 with dissolve
    hana "Fine. Your choice. Ask me anything, [mcf]."
    scene w1_3617 with dissolve
    mc "Okay. I got to make this a good one, give me a second to think..."
    scene w1_3618 with dissolve
    mc "Hmm..."
    scene w1_3613 with dissolve
    hana "Eeeeh? Stop looking at me like you're about to dissect me."
    scene w1_3614 with dissolve
    mc "Okay, got it!"
    scene w1_3615 with dissolve
    hana "Oh, boy... let me have it."
    scene w1_3611 with dissolve
    mc "What's your fondest memory?"
    scene w1_3613 with dissolve
    hana "Is that a joke? That's what you want to ask me? You don't want to ask something embarrassing?"
    scene w1_3614 with dissolve
    mc "No. I want to hear you talk about something that makes you happy."
    scene w1_3616 with dissolve
    hana "Mmmmh...?"
    scene w1_3598 with dissolve
    hana "You really are a dork."
    scene w1_3599 with dissolve
    hana "Okay, fair's fair: my fondest memory..."
    scene w1_3600 with dissolve
    "Hana paused a moment to collect her thoughts. She seemed to give it some genuine thought, before arriving at a satisfactory answer."
    scene w1_3602 with dissolve
    hana "Got it."

    if hanaFlag == True:
        hana "This is well before my mother got sick. Back then, it was just me, her, and my grandfather."
    else:
        hana "This is from when I was a kid. Back then it was just me, my mother, and my grandfather."

    scene w1_3604 with dissolve
    hana "All three of us lived together. My mom always told people she was looking after grandpop, but it was more like he was looking after her. She never quite had her shit together, y'know?"
    hana "I loved my grandpop. He always had a PBJ fixed when I got home from school. Glass of milk, crusts cut off... he called it \"the works\"."
    scene w1_3603 with dissolve
    mc "That sounds really nice. Is that your answer?"
    scene w1_3602 with dissolve
    hana "Oh, no. Just giving you a little context first."
    scene w1_3630 with dissolve
    hana "Anyway, my grandpop loved music. He always talked about how music had the power to transport you back in time. That a song could be tied to specific moments in your life and just by hearing it, you could transport yourself back in time."
    hana "Recall all kinds of memories... major life events, love and heart break, and even take you back to the first time you saw your favorite movie."
    scene w1_3601 with dissolve
    mc "I like the way your grandfather viewed music. Is that where your love of music comes from?"
    scene w1_3630 with dissolve
    hana "It's where it started, yeah. My grandpop introduced me to all kinds of awesome bands as a kid. All kinds of styles and genres, but the one that made the biggest mark on me was punk."
    hana "When I was 10, he took me to see my first live concert. The venue only held a few hundred people, but to a kid, that was the most people I'd even seen in one place at the time."
    scene w1_3602 with dissolve
    hana "It felt like all the people in the world were there to listen to the band play. That was crazy to me."
    scene w1_3603 with dissolve
    mc "It is kinda crazy when you think about it. The way so many people's lives can be touched by the same thing."
    scene w1_3631 with dissolve
    hana "Exactly. It was because of that I fell in love with rock music. I wasn't an outgoing child. I always went straight home after school, but that concert inspired me in more ways than one."
    scene w1_3632 with dissolve
    hana "The place smelled horrible and the music was blown out, but the band had so much energy. They played loud and fast and everyone was losing their minds. Cheering uncontrolably."
    hana "Not only that, the drummer was a chick too. That was so cool to me! All the drummers I'd seen up to that point, in the music my granpop introduced to me, were ugly dudes."
    scene w1_3598 with dissolve
    hana "That was the perfect night. That's when music became more than just an excuse to hang out with my grandpop, it became something that connected us."
    scene w1_3633 with dissolve
    hana "Anytime I hear the first song they played that night, I feel like I'm reliving that night. I feel like a kid again."
    hana "I remember how tightly he gripped my hand, so we wouldn't get separated. I remember how large they seemed compared to mine. I remember sitting on his broad shoulders to get a better view of the band..."
    scene w1_3611 with dissolve
    mc "The power to transport you back in time. Just like he talked about."
    scene w1_3620 with dissolve
    hana "Yeah, just like he said."
    scene w1_3635 with dissolve
    hana "He's, uh... dead now."
    scene w1_3636 with dissolve
    mc "I'm sorry..."
    scene w1_3633 with dissolve
    hana "No. It feels really nice to reminiscence."
    scene w1_3611 with dissolve
    mc "What band did you see play that night?"
    scene w1_3615 with dissolve
    hana "You'd probably know them, actually. They blew up in the years after I saw them."
    hana "Still, I'd rather not say. I like the fact that whenever they come on the radio, I'm the only person in the world who can connect them with that story."
    scene w1_3611 with dissolve
    mc "Who's the dork now? That's so sentimental and corny."
    scene w1_3613 with dissolve
    hana "So what?"
    scene w1_3614 with dissolve
    mc "So... I think that's really great. I love that. Thanks for sharing."
    scene w1_3633 with dissolve
    hana "No problem. Fair's fair, after all."
    scene w1_3634 with dissolve
    "Hana smiled at me earnestly, in a way you rarely glimpse in your everyday life. Even from the people you're close to."
    scene w1_3637 with dissolve
    hana "Let's get out of here. I feel like I'm about to boil."
    mc "Heh, yeah. Me too."
    scene black with fade
    stop music fadeout 3.0
    $ history_hana = "I ducked out during the third game of the night and hung out with Hana, where she told me about her grandfather and the direct hand he had in her falling in love with music."
    $ unread_hana = True
    play sound "sound effects/notification.wav"
    show bioupdate with dissolve
    "......"
    "..."

    if hanaFlag == True:
        hana "Oh, [mcf]?"
        scene w1_3638 with dissolve
        play ambient "sound effects/sauna.mp3"
        "Hana looked me dead in the eyes, the corners of her mouth curling deviously into a mirthy grin."
        mc "What is it?"
        play sound "sound effects/sting-mystical.mp3"
        scene w1_3639 with dissolve
        pause 0.1
        scene w1_3640 with dissolve
        scene w1_3641 with dissolve
        mc "Gh--!"
        "In one unbroken motion, Hana hooked her fingertips into the underside of her bikini top and yanked it down in one quick motion, exposing her pale shapely breasts."
        mc "What are you...?"
        scene w1_3642 with dissolve
        hana "A dozen other topless women downstairs, eh?"
        hana "Still think they're just a dime-a-dozen?"
        scene w1_3641 with dissolve
        mc "Aaaah, I didn't mean it that way..."
        scene w1_3643 with dissolve
        hana "You want to see these babies next time, maybe be more considerate with your words, jerk."
        scene w1_3644 with dissolve
        mc "Wait, come back-!"
        "Hana left the sauna as quickly as she knocked me flat on my proverbial ass."
        mc "Eh- oh...."
        mct "(Wait, next time...?)"
        scene black with fade
        stop ambient fadeout 3.0
        "......"
        "..."

    jump w1ExKatEnding


label w1ExKatEnding:

    scene w1_3645 with circlewipe

    if w1ExGame3Avoid:
        "After whiling away the final leg of the exhibition with Hana and the club's patrons now enjoying the building's comforts, I found myself in Kathleen's office."
    else:
        "With tonight's exhibition wrapping up and the patrons enjoying the club's amenities, booze, and women, I was found myself in Kathleen's office."

    scene w1_3646 with dissolve
    play music "music/Moonlight-Sonata.mp3"
    "Alone, just the two of us."
    kat "Good job tonight, [mcf]."
    kat "Performing under the spotlight as you did takes a non-trivial amount of mental fortitude."
    scene w1_3647 with dissolve
    mc "Not to mention, a few screws loose in the head and a troubling lack of shame."
    scene w1_3648 with dissolve
    kat "So candid. That's good."

    if w1ExGame3Avoid:
        scene w1_3649 with dissolve
        kat "However, I {b}was{/b} sad to see you absent during the final game."

        if hanaFlag == True:
            kat "I know I told you to be a friend to Miss Rhodes, but don't let it interfere with your duties."
        else:
            kat "It's good you're getting along with Miss Rhodes, but don't let it interfere with your duties."

        scene w1_3651 with dissolve
        mc "Sorry, I should've asked you first to see if I was needed."
        scene w1_3650 with dissolve
        kat "That's alright."

    else:
        scene w1_3650 with dissolve
        kat "It bodes well for our future relationship."

    kat "All things considered, you performed to my standards tonight and made a positive impression on our members."
    scene w1_3651 with dissolve
    mc "After the initial hurdle of stepping on stage, it felt like a dream."
    scene w1_3652 with dissolve
    kat "It's a peculiar feeling, isn't it? Everything begins to look soft under the harsh spotlight. It's strange."
    scene w1_3653 with wipeleft
    mc "I felt like I couldn't even process my own thoughts at some points. That part of it wasn't totally unpleasant."
    scene w1_3654 with dissolve
    kat "You have a more refined sensibility than expected."
    scene w1_3655 with dissolve
    kat "Truthfully, I don't know if that's a bad thing or not, but it's a nice change of pace from the cruder element between these walls."
    scene w1_3653 with dissolve
    mc "Are you worried I can't do the job? You just said I lived up to your expectations."
    scene w1_3655 with dissolve
    kat "No, but your tendency to self-reflect can either help or hinder you in our work."

    if Kathleen_Trust >= 5:
        scene w1_3656 with dissolve
        kat "After tonight, I can say I'm at least rooting for you."
    kat "..."
    scene w1_3657 with dissolve
    if kat_polite == True:
        "Mrs. Pulman's uncharacteristically gentle expression dissolved before my eyes, replaced with a gloomy looking frown."
    else:
        "Kathleen's uncharacteristically gentle expression dissolved before my eyes, replaced by a gloomy looking frown."

    scene w1_3658 with dissolve
    mc "Is something the matter?"
    scene w1_3659 with dissolve
    kat "No, it's nothing."
    scene w1_3651 with dissolve
    mc "Wouldn't you rather enjoy yourself with the other guests? We could've discussed this downstairs."
    scene w1_3649 with dissolve
    kat "What? Like I'm one of \"the boys\"?"
    kat "No... after an exhibition, I prefer solitude. This place may be a world of my own creation, but I find parts of it aggravating and tiring."
    "Kathleen's words sounded very lonely to me."
    scene w1_3650 with dissolve
    kat "However, you should go enjoy your night as you wish. I don't need you for anything else tonight."
    scene w1_3651 with dissolve
    mc "Well then, I think I'll head home."
    scene w1_3650 with dissolve
    kat "You're not going to stay and enjoy the party?"
    scene w1_3651 with dissolve
    mc "No, I've had enough tonight."
    scene w1_3650 with dissolve
    kat "I understand."
    scene w1_3660 with dissolve
    kat "Take one of the USB sticks on the desk as a memento of your first exhibition of the club. It's footage of tonight's exhibition."
    mc "Eh...? Yeah, okay."
    mc "Thanks."
    "I didn't {i}really{/i} want it, but I decided turning it down would be more trouble than simply accepting it."
    scene black with fade
    "Besides, I had another video I wanted to watch before I ended this absurd, abnormal night."
    stop music fadeout 3.0
    $ history_kathleen = "Mrs. Pulman expressed her pleasure at my performance during the exhibition. I think she's beginning to trust me."
    $ unread_kathleen = True
    play sound "sound effects/notification.wav"
    show bioupdate with dissolve
    "........."
    "......"
    "..."
    scene w1_3661 with pixellate
    play music "music/night-on-the-docks-sax.mp3"
    man "Do you have anything to say to the viewers at home?"
    scene w1_3662 with dissolve
    vic "T-thanks for watching..."
    scene w1_3663 with pixellate
    mc "..."
    "As soon as I got home, I put on one of my mother's old adult videos."
    "Even if I found the contents repulsive,  it was something I did from time to time. To me, it served as a tangible reminder of what she endured to give me a good home."
    "It was bitterly sad to me that my mother thought she carried her past alone."
    scene w1_3667 with dissolve
    mct "(One day, I'll be honest with mom.)"
    "A few years ago, I made a promise to myself. I would tell her I knew about her life as a porn star and thank her from the bottom of my heart."
    mct "(On that day, I'd never watch these fucking things again.)"
    scene w1_3663 with dissolve
    "Tonight though, I wanted to watch one for a different reason. To make sure I remembered that Rosalind, Veronica, and Felicia were human beings just like my mother."
    "In the midst of hedonism, it's easy to lose your sense of empathy. I wanted to preempt that from happening."
    "I do this, but at the same time..."
    mct "(It was fun, wasn't it?)"
    play sound "sound effects/ringing-inbound.wav"
    scene w1_3664 with dissolve
    "*Ring, ring. Ring, ring*"
    mct "(It's mom...)"
    stop sound
    scene w1_3665 with dissolve
    play sound "sound effects/phonemenu.wav"
    mc "Hello?"
    scene w1_3669 with dissolve
    vic "Hey! I didn't wake you up, did I?"
    scene w1_3668 with dissolve
    mc "No, I was still up. I was just watching a movie."
    scene w1_3669 with dissolve
    vic "Oh? What movie?"
    scene w1_3665 with dissolve
    scene w1_3666 with dissolve
    mc "The Life of Oharu."
    vic "Why in the world are you watching that dreary thing? You should watch something more cheerful."
    scene w1_3668 with dissolve
    mc "You're probably right. Something more your speed, like {i}Black Belly of the Tarantula{/i} or {i}Blood and Lace{/i}?"
    scene w1_3670 with dissolve
    vic "Hehehe, that's just fantasy entertainment. Anyway, I'm calling you so late for a very special reason..."
    scene w1_3668 with dissolve
    mc "Oh, I guess it is after midnight, isn't it?"
    scene w1_3671 with dissolve
    vic "Bingo! Happy birthday, my baby boy! I'm so blessed to have you as my son!"
    mc "Thanks, mom."
    scene black with fade
    vic "What do you want to do tomorrow?"
    stop music fadeout 3.0
    "......"
    "..."
    play sound "sound effects/sting-mumbaieffect.wav"
    hide screen qmenu with dissolve
    call screen thanksforplaying with curtains












##
