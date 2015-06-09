#!/usr/bin/env python3

from lxml import etree
import os, sys

INKSCAPE = "/usr/bin/inkscape"
TEMPLATE = "avatar.svg"
OUT = "avatar.png"
ABSPREFIX = os.getcwd()
TMP = "out.svg"

def render(image):
  templatexml = etree.parse(TEMPLATE)
  r = templatexml.getroot()
  print(r.xpath('svg')) #HELP
  #templatexml.root.elements["//pattern[@inkscape:label='avatarpattern']/image"].attributes['xlink:href'] = image
  #templatexml.root.elements["//pattern[@inkscape:label='avatarpattern']/image"].attributes['sodipodi:absref'] = 
  #  "file://#{ABSPREFIX}/#{image}"
  #puts templatexml.root.elements["//pattern[@inkscape:label='avatarpattern']/image"].attributes['sodipodi:absref']
  templatexml.write(TMP, encoding="utf-8")
  command = "%s -e %s %s" % (INKSCAPE, OUT, TMP)
  print(command)
  os.system(command)

if len(sys.argv)>1:
  render(sys.argv[1])
else:
  print("`./render-avatar.rb photo.jpg`\n\nPass a square photo filename as a parameter.")

