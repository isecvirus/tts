
"""
@Author = virus
@version = 1.0.0
@Name = % Still thinking about it, but for now "tts" will work %

I might implement this whole code to make it..
..safe for identity keepers.

BTW shoutout to 'em and keep the privacy working.
"""

import pyttsx3
from prompt_toolkit import prompt, HTML, print_formatted_text
from prompt_toolkit.shortcuts import radiolist_dialog


def prompt_continuation(width, line_number, wrap_count):
    text = ("%s | " % str(line_number + 1).rjust(3, " ")).rjust(width)
    return HTML("<strong>%s</strong>") % text

def get_gender():
    male = pyttsx3.init().getProperty("voices")[0].id
    female = pyttsx3.init().getProperty("voices")[1].id

    return radiolist_dialog(
        values=[
            (male, HTML('<style fg="cyan">Male</style>')),
            (female, HTML('<style fg="pink">Female</style>')),
        ],
        title="Choose voice gender",
        text="*[ After this you'll be prompted to input your text ]*",
    ).run()

if gender := get_gender():
    print_formatted_text("  * | Press [ESC + Enter] to confirm filename.")
    text = prompt("  1 | ", multiline=True, mouse_support=True, enable_suspend=True, enable_history_search=True,
                  search_ignore_case=True, prompt_continuation=prompt_continuation)

    if text:
        while True:
            output = prompt("\nfilename: ", placeholder=HTML("<p fg='#222222'>output.mp3</p>"))

            if output:
                engine = pyttsx3.init()
                engine.setProperty("voice", gender)

                engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)
                engine.setProperty('rate', 150)  # Speech rate (words per minute)
                engine.setProperty('voice', 'en-us')  # Voice type

                engine.save_to_file(text, output)

                engine.runAndWait()
            break