# RadIOqt

Shoutcast/Icecast player

## What is this?

Plays back shoutcast and icecast streams using VLC's Python bindings.

# Requirements
See requirements.txt for a full list of dependencies.

# Running the .py

Ensure both of the above dependencies are installed and run ```radio.py``` just how you would any other Python file.

Running the install script will copy any of the image assets and configuration files to their appropriate location. If you have a precompiled binary, it will copy it from dist/radio to /usr/local/bin/radioqt

# Building the Binary

```pip3 install pyinstaller```

Then build inside of the project folder

```pyinstaller radio.py --clean --onefile```

and the resulting binary will be located in **dist/radio**

# Bugs / Feature Requests

Open up an issue on the Github page and I'll take a look at it. PR's welcome :)
