# Scraper 1.0.0
# 13 May 2016
# Simple URL scraper (snipped based on html <body> tag and saved to file)

### IMPROVEMENT: USER-INPUT URL

import urllib
fout = open('textfilename.txt', 'w')
fhand1 = urllib.urlopen('http://deborahroberts.info/test-text/')
text1 = fhand1.read()
pos = text1.find('<body')
pos1 = text1.find('</body>')
snipped = text1[pos:pos1+7]
print snipped

fout.write(snipped)
fout.close()
