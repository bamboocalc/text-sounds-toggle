
# This is an example of a character object
define player = Character("Myself", color="#f80067", callback=click_to_continue)

#Make sure to set the default value to True if your game has voice acting already
default persistent.voice_acting = True

init python:    
    def click_to_continue(event, interact=False, **kwargs):
        if not persistent.voice_acting:
            if event == "show":
                # Get the length of the current dialogue block
                what = renpy.store._last_say_what
                if what:
                    beeps = len(what) # The number of text sounds queued is dependant on the length of the dialog block
                else:
                    beeps = 5  # If the dialog block is empty, play the keyboard sound only 5 times
                for _ in range(beeps):
                    randosound = renpy.random.randint(1, 7)
                    renpy.sound.queue(f"audio/type/tap-0{randosound}.wav", channel="sound", loop=False) # Replace "audio/type/tap-0" with the path and file name of the audio file you wish to use for your text sounds
            elif event == "end" or event == "slow_done":
                renpy.sound.stop(channel="sound")
        else:
            if event == "begin":
                renpy.sound.play("audio/type/ctc.wav", channel="sound", loop=False)


screen preferences():
    tag menu

    use game_menu(_("Prefs"), scroll="viewport"):

        vbox: # Find your screens.rpy file and place this vbox somewhere inside it. (The exact location within the Preferences Screen is based on your project's needs!)
            style_prefix "radio"
            label _("Voice Acting")
            textbutton _("{Enabled") action [SetVariable("persistent.voice_acting",True), SetMute(['voice'], False)]
            textbutton _("Disabled") action [SetVariable("persistent.voice_acting",False), SetMute(['voice'], True)]