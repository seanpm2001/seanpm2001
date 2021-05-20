# Start of script

"""
Info
This is an experimental script used to test recently learned Python knowledge from last night.
Data is taken and modified from https://en.wikiversity.org/wiki/Python_Programming/ with my own additions to demo sections
"""

# Regex

import re # import regex

# Example 1

string = "<p>HTML text.</p>"
match = re.match("<p>.*</p>", string)
if match:
    print("start:", match.start(0))
    print("end:", match.end(0))
    print("group:", match.group(0))

# Example 2

string = "<h1>Heading</h1><p>HTML text.</p>"
match = re.search("<p>.*</p>", string)
if match:
    print("start:", match.start(0))
    print("end:", match.end(0))
    print("group:", match.group(0))

# Example 3

string = "<h1>Heading</h1><p>HTML text.</p>"

match = re.search("<.*>", string)
if match:
    print("Greedy")
    print("start:", match.start(0))
    print("end:", match.end(0))
    print("group:", match.group(0))

match = re.search("<.*?>", string)
if match:
    print("\nNon-greedy")
    print("start:", match.start(0))
    print("end:", match.end(0))
    print("group:", match.group(0))

# Example 4    

string = "<h1>Heading</h1><p>HTML text.</p>"
matches = re.findall("<.*?>", string)
print("matches:", matches)

# Example 5

string = "<h1>Heading</h1><p>HTML text.</p>"
string = re.sub("<.*?>", "", string)
print("string:", string)

# Example 6

string = "cat: Frisky, dog: Spot, fish: Bubbles"
keys = re.split(": ?\w*,? ?", string)
values = re.split(",? ?\w*: ?", string)
print("string:", string)
print("keys:", keys)
print("values:", values)

# Example 7

string = "<p>Lines of<br>HTML text</p>"
regex = re.compile("<br>", re.IGNORECASE)
match = regex.search(string)
if match:
    print("start:", match.start(0))
    print("end:", match.end(0))
    print("group:", match.group(0))

# Example 8

string = "<p>HTML text.</p>"
match = re.match("<p>(.*)</p>", string)
if match:
    print("start:", match.start(1))
    print("end:", match.end(1))
    print("group:", match.group(1))

string = "'cat': 'Frisky', 'dog': 'Spot', 'fish': 'Bubbles'"

match = re.search("'cat': '(.*?)', 'dog': '(.*?)', 'fish': '(.*?)'", string)
if match:
    print("groups:", match.group(1), match.group(2), match.group(3))
    
lst = re.findall(r"'(.*?)': '(.*?)',?\s*", string)
for key, value in lst:
  print("%s: %s" % (key, value))

# Demo

string9 = "<H1 lang="en">Hello world</H1>"
match = re.match("en") # Incomplete, don't know what to do, confused about strings within strings

# Demo 2

string10 = "'dog': 'Guinea', 'cat': 'cocoa', 'fish': 'many'"
if match:
    print("groups:", match.group(1), match.group(2), match.group(3))
# How to assign IDs to strings separately

# Modules

import functions # import functions, also known as modules
import classes # I didn't know this needed to be imported manually

class classOne(object)
  return method1()
  break
  def method1(self)
    print ("You can have more than 1 class in a program. Classes are a key part in OOP (Object Oriented Programming")
    break
 class objectTwo(object)
    return method2()
    break
 def method2(self)
    print ("Classes are objects?")
  
# End of script
