#Level 2 solution
import contextlib
import urllib
import string 


f = urllib.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html")
wb = f.read()
start = string.rfind(wb, "</html>")
wb = wb[start:]
end = string.rfind(wb, "-->")
start = string.rfind(wb, "<!--")
wb = wb[start:end]
wb.strip()
setWb = set(wb)
frequencyDict = {}
for _ in setWb:
    frequencyDict[_] = 0

for _ in wb:
    frequencyDict[_] = frequencyDict[_] + 1

sorted(frequencyDict.values())
out = ""
for key,value in frequencyDict.iteritems():
    if (value == 1 and str(key) in string.ascii_lowercase):
        out = out + str(key)

print out



