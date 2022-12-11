test = "Email your feedbackk here : book@subeen.com py.book@subeen.com book_py@subeen.com book@subeen thank you"
email = "book at subeen.com, book At subeen.com, book (at) subben [dot] com"
import re
pa = re.compile(r'(\w*)\s+[\(\[]*\s*at*\s*[\)\]]*\s+(\w*)(?:\s+[\(\[]*\s*dot*\s*[\)\]]*\s+|\.)(\w*)',flags=re.IGNORECASE)
em = pa.sub(r'\1@\2.\3',email)

print(em)


