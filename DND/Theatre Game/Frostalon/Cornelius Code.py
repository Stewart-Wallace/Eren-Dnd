# -*- coding: utf-8 -*-
"""
Created on Mon May 31 20:27:23 2021

@author: Stug
"""

codex = {
        'a': '|:',
        'b': "|'",
        'c': '|.',
        'd': '|-',
        'e': '-|',
        'f': '=-',
        'g': "'|",
        'h': '||',
        'i': '..',
        'j': "'-",
        'k': '-.',
        'l': '.|',
        'm': 'l|',
        'n': '--',
        'o': '.l',
        'p': '-l',
        'q': '|l',
        'r': "''",
        's': ':|',
        't': "'|",
        'u': 'l-',
        'v': "l'",
        'w': "-'",
        'x': ".'",
        'y': '-=',
        'z': '=l',
        ' ': 'll',
        '.': '==',
        ',': '-_',
        }

string = 'the tabaxi child named teelos has been seen at the site once again. the child needs to be sorted with, he made his way into the main chamber and almost damaged the main limestone column. if the child is spotted near here again they will set apon by tarnall and his goons and will not make it back to the town.'
new_string = ''
for pp in string:
    new_string = new_string + codex[pp]
    
text_file = open("Output.txt", "w")

text_file.write(new_string)

text_file.close()