# -*- coding: utf-8 -*-
import sys
import re

def isHangul(text):
    #Check the Python Version
    pyVer3 =  sys.version_info >= (3, 0)

    if pyVer3 : # for Ver 3 or later
        encText = text
    else: # for Ver 2.x
        if type(text) is not unicode:
            encText = text.decode('utf-8')
        else:
            encText = text

    hanCount = len(re.findall(u'[\u3130-\u318F\uAC00-\uD7A3]+', encText))
    return hanCount > 0

# for Test
if __name__ == '__main__':
    han = '한글'
    han2 = u'한글'
    input = 'English1234'  #utf-8
    input2 = u'English1234' #unicode
    #(major_ver, minor_ver) = (sys.version_info).split(',')
    print(han + " is " + str(isHangul(han)))
    print(han2 + " is " + str(isHangul(han2)))
    print(input + " is " + str(isHangul(input)))
    print(input2 + " is " + str(isHangul(input2)))
