from lxml import etree
from io import StringIO, BytesIO
import re
import numpy
import sys

def iterlines(foo):
    prevnl = -1
    while True:
      nextnl = foo.find('\n', prevnl + 1)
      if nextnl < 0: break
      yield foo[prevnl + 1:nextnl]
      prevnl = nextnl

lines = []
for event, element in etree.iterparse(sys.argv[1], events=("start", "end")):
    if event == "end" and element.tag.startswith("seg"):
        if element.text:
            for line in iterlines(element.text):
                lines.append(line)

with open(sys.argv[2], 'w') as f:
    for line in lines:
        string = line + "\n"
        f.write(string.encode('utf8'))
