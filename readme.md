# journeymap-sticher

Takes a bunch of files with coordinates delimited by commas, and creates one big image.

ex, a bunch of files such as -4,3.png and -4,4.png

They don't need to be attached to one another, the program will make the smallest image possible that contains all of the tiles.

Not a perfect solution, but workable. I think that some problems may occur if your coordinates are all negative, or don't cross the origin (probably both).

Requires the `pillow` library to be installed via pip:

```pip install pillow```

It creates a single .png file called output.png

I use this program to convert my journeymap maps into a proper big map I can print out (since some maps are just HUGE)
