#!/usr/bin/env python

""" Script to extract colors from iterm profile

    usage example:
    ./iterm2xterm.py monokai-iterm/monokai.itermcolors
"""


import sys
import re
import plistlib
import pprint

profile = plistlib.readPlist(sys.argv[1])


def color2rgb(d):
    r = "%02X" % int(float(d["Red Component"]) * 255)
    g = "%02X" % int(float(d["Green Component"]) * 255)
    b = "%02X" % int(float(d["Blue Component"]) * 255)

    rgb = "#%s%s%s" % (r, g, b)
    return rgb

gnome_profile = {
    "palette": range(16)
}

for k in profile:
    m = re.search("Ansi (\d{1,2}) Color", k)
    if m:
        pos = int(m.group(1))
        rgb = color2rgb(profile[k])
        assert(len(rgb) == 7)

        gnome_profile["palette"][pos] = "color%s=%s" % (pos, rgb)

    m = re.search("Background Color", k)
    if m:
        gnome_profile["background_color"] = color2rgb(profile[k])

    m = re.search("Foreground Color", k)
    if m:
        gnome_profile["foreground_color"] = color2rgb(profile[k])

    m = re.search("Bold Color", k)
    if m:
        gnome_profile["bold_color"] = color2rgb(profile[k])


p = pprint.PrettyPrinter(indent=4)
p.pprint(gnome_profile)
