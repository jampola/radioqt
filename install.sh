#!/bin/bash

ICONSDESTDIR="/usr/share/radioqt/icons"
BINDIR="/usr/local/bin/"

# create BINDIR and ICONSDESTDIR and PIXMAPSDESTDIR if they don't exist
if [ ! -d "$BINDIR" ]; then
    mkdir -p "$BINDIR"
fi

if [ ! -d "$ICONSDESTDIR" ]; then
    mkdir -p "$ICONSDESTDIR"
fi

# copy files to BINDIR and ICONSDESTDIR and PIXMAPSDESTDIR
cp -f dist/debian/radio "$BINDIR/radioqt"
cp -f lib/img/* "$ICONSDESTDIR"
