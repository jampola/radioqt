# RadIOqt 0.1

Shoutcast/Icecast player

## What is this?

Plays back shoutcast and icecast streams using VLC's Python bindings.

# Requirements
See requirements.txt for a full list of dependencies.

# Running the .py

Ensure both of the above dependencies are installed and run ```radio.py``` just how you would any other Python file.

# Building the Binary

```pip3 install pyinstaller```

Then build inside of the project folder

```pyinstaller radio.py --clean --onefile```

and the resulting binary will be located in **dist/radio**

# Bugs / Feature Requests

Open up an issue on the Github page and I'll take a look at it. PR's welcome :)
