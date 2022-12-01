import re
text = "This is line 1. Date is 2017/06/01. And there is another date : 2014-17-01. The third and final date is 2015/08/30."
pat  = re.compile(r"(\d{4})[-/](\d{2})[-/](\d{2})")
print(pat)
print(type(pat))
result = pat.findall(text)
print(result)
