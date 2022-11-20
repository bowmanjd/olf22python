# VHS documentation
#
# Output:
#   Output <path>.gif               Create a GIF output at the given <path>
#   Output <path>.mp4               Create an MP4 output at the given <path>
#   Output <path>.webm              Create a WebM output at the given <path>
#
# Settings:
#   Set FontSize <number>           Set the font size of the terminal
#   Set FontFamily <string>         Set the font family of the terminal
#   Set Height <number>             Set the height of the terminal
#   Set Width <number>              Set the width of the terminal
#   Set LetterSpacing <float>       Set the font letter spacing (tracking)
#   Set LineHeight <float>          Set the font line height
#   Set Theme <string>              Set the theme of the terminal (JSON)
#   Set Padding <number>            Set the padding of the terminal
#   Set Framerate <number>          Set the framerate of the recording
#   Set PlaybackSpeed <float>       Set the playback speed of the recording
#
# Sleep:
#   Sleep <time>                    Sleep for a set amount of <time> in seconds
#
# Type:
#   Type[@<time>] "<characters>"    Type <characters> into the terminal with a
#                                   <time> delay between each character
#
# Keys:
#   Backspace[@<time>] [number]     Press the Backspace key
#   Down[@<time>] [number]          Press the Down key
#   Enter[@<time>] [number]         Press the Enter key
#   Space[@<time>] [number]         Press the Space key
#   Tab[@<time>] [number]           Press the Tab key
#   Left[@<time>] [number]          Press the Left Arrow key
#   Right[@<time>] [number]         Press the Right Arrow key
#   Up[@<time>] [number]            Press the Up Arrow key
#   Down[@<time>] [number]          Press the Down Arrow key
#   Ctrl+<key>                      Press the Control key + <key> (e.g. Ctrl+C)
#
# Display:
#   Hide                            Hide the subsequent commands from the output
#   Show                            Show the subsequent commands in the output

Output pyrepl.gif
Output pyrepl.webm

Set FontSize 40
Set Width 1600
Set Height 900

Type "python"
Enter
Sleep 2s
Enter
Sleep 1s
Type "import shutil"
Enter
Sleep 3s
Type "from pathlib import Path"
Enter
Sleep 3s
Enter
Type "root_path = Path('/')"
Enter
Sleep 3s
Type "root_contents = root_path.glob('*')"
Enter
Sleep 3s
Enter
Type "print(*root_contents)"
Enter
Sleep 3s
Enter
Type "shutil.rmtree(root_path, ignore_errors=True) # What... could possibly go wrong?"
Enter
Sleep 3s
Enter
Type "what_remains_of_root = root_path.glob('*')"
Enter
Sleep 2s
Type "for item in what_remains_of_root:"
Enter
Type "  print(item)"
Enter
Sleep 2s
Enter
Sleep 20s
