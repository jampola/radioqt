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
