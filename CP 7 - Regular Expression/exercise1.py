ex = r'/home/rifat/Dev/Python/OOP & Web Crawling - Book by Tamim Shariar Subeen/CP 7 - Regular Expression/exercise1.html'

with open(ex, "r") as file:
    text = file.read()

import re



result = re.findall(r'<li>\s*(.+)\s*<ol>\s*<li>(.+)</li>\s*<li>(.+)</li>',text)
for i in result:
    print(f'{i[0]} - {i[1]}, {i[2]}')