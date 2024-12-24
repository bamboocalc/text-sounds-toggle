# text-sounds-toggle
Toggle between voice acting and text sounds in your Ren'Py game

Steps:
1. Add the "click_to_continue" function inside an init python block
2. Add a new variable "persistent.voice_acting" to your script.rpy file and set the default value to True
3. For every character who you want this new function to apply to, append "callback=click_to_continue" to their character object.
4. Consider watching the video tutorial for a visual demonstration: https://youtu.be/gGRv8aTfr3g
