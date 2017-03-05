#!/usr/bin/python

import subprocess
import pandocfilters

def claim_filter(key, value, format, meta):
  if key == 'Link':
    (identifier, classes, attributes_list), content, target = value
    attributes = dict(attributes_list)
    if 'claim' in attributes:
      claim_test_command = attributes['claim']
      if subprocess.call(claim_test_command, shell=True) == 0:
        return pandocfilters.Span((identifier, classes, attributes_list), content)
      else:
        return pandocfilters.Strong([pandocfilters.Strikeout(content)])

pandocfilters.toJSONFilter(claim_filter)
