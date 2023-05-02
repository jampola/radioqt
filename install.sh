#!/bin/bash

ICONSDESTDIR="/usr/local/bin/radioqt/icons"
PIXMAPSDESTDIR="/usr/local/bin/radioqt/pixmaps"
BINDIR="/usr/local/bin/radioqt"

# create BINDIR and ICONSDESTDIR and PIXMAPSDESTDIR if they don't exist
if [ ! -d "$BINDIR" ]; then
    mkdir -p "$BINDIR"
fi

if [ ! -d "$ICONSDESTDIR" ]; then
    mkdir -p "$ICONSDESTDIR"
fi

if [ ! -d "$PIXMAPSDESTDIR" ]; then
    mkdir -p "$PIXMAPSDESTDIR"
fi

# copy files to BINDIR and ICONSDESTDIR and PIXMAPSDESTDIR
cp -f radioqt.sh "$BINDIR/radioqt"
cp -f icons/* "$ICONSDESTDIR"
cp -f pixmaps/* "$PIXMAPSDESTDIR"

# create desktop file
DESKTOPFILE="/usr/share/applications/radioqt.desktop"
echo "[Desktop Entry]" > "$DESKTOPFILE"
echo "Version=1.0" >> "$DESKTOPFILE"
echo "Type=Application" >> "$DESKTOPFILE"
echo "Name=RadioQt" >> "$DESKTOPFILE"
echo "Comment=Internet radio player" >> "$DESKTOPFILE"
echo "Exec=/usr/local/bin/radioqt/radioqt" >> "$DESKTOPFILE"
echo "Icon=/usr/local/bin/radioqt/pixmaps/radioqt.png" >> "$DESKTOPFILE"
echo "Terminal=false" >> "$DESKTOPFILE"
echo "Categories=AudioVideo;Player;Audio;" >> "$DESKTOPFILE"
echo "MimeType=audio/x-mpegurl;audio/x-scpls;audio/x-mp3-playlist;" >> "$DESKTOPFILE"
echo "Keywords=radio;qt;internet;player;" >> "$DESKTOPFILE"

