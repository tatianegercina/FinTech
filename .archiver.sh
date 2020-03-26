#!/bin/bash

# This script creates a light version of the content
# suitable for low bandwidth connections.
# It compresses all images and zips each unit folder.
# The files go into a build subdirectory.

echo "Compress and Zip Lesson Plans..."
if [ -d "build" ]
then
    rm -rf build/*
else
    mkdir -p build/01-Lesson-Plans
fi

# Lesson Plans
find 01-Lesson-Plans -type d -mindepth 1 -maxdepth 1 -exec cp -r {} build/01-Lesson-Plans/ \;

pushd build/01-Lesson-Plans

echo "Compress Lesson Images..."
for f in $(find -E . -iregex ".*\.(jpg|png|jpeg)" -mindepth 1); do mv $f $f.raw && imagemin $f.raw > $f && rm $f.raw; done
echo "Zip Lesson Folders..."
find . -type d -maxdepth 1 -mindepth 1 -exec zip -rm {}.zip {} \;

popd

echo "Compress and Zip Homework..."
# Homework
mkdir build/02-Homework
find 02-Homework -type d -mindepth 1 -maxdepth 1 -exec cp -r {} build/02-Homework/ \;

pushd build/02-Homework

echo "Compress Homework Images..."
for f in $(find -E . -iregex ".*\.(jpg|png|jpeg)" -mindepth 1); do mv $f $f.raw && imagemin $f.raw > $f && rm $f.raw; done
echo "Zip Homework Folders..."
find . -type d -maxdepth 1 -mindepth 1 -exec zip -rm {}.zip {} \;

popd

echo "Compress and Zip Projects..."
# Projects
mkdir build/03-Projects
find 03-Projects -type d -mindepth 1 -maxdepth 1 -exec cp -r {} build/03-Projects/ \;

pushd build/03-Projects

echo "Compress Project Images..."
for f in $(find -E . -iregex ".*\.(jpg|png|jpeg)" -mindepth 1); do mv $f $f.raw && imagemin $f.raw > $f && rm $f.raw; done
echo "Zip Project folders..."
find . -type d -maxdepth 1 -mindepth 1 -exec zip -rm {}.zip {} \;

popd

echo "Done! High five! ヘ( ^o^)ノ＼(^_^ )"
