#!/usr/bin/env python3
import re

re_str = 'One sentence. Another sentence? And last sentence!'

# * Split
# split exclude split values
print(re.split(r'[.?!]', re_str))

# split includes split values
print(re.split(r'([.?!])', re_str))