# read - https://pypi.org/project/PEPit/   --these
# are PEPit guidelines je harry ne suggest kele to read


#used Re.txt refernece in this tutorial
import re

mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiinaiiiiiiiiiiii'''

# primarily used re functions are - findall, search, split, sub, finditer

# pattern = re.compile(r'fass')  #giving raw string as input
# pattern = re.compile(r'.adm')  #giving raw string as input
# pattern = re.compile(r'^Tata')  #giving raw string as input
# pattern = re.compile(r'ii$')  #giving raw string as input
# pattern = re.compile(r'ai*')  #giving raw string as input
# pattern = re.compile(r'ai{2}')  #giving raw string as input
# pattern = re.compile(r'(ai){2}')  #giving raw string as input
# pattern = re.compile(r'(ai){1}|t')  #giving raw string as input


#task = given a string with a lot of
# indian phone numbers starting from+91 using \b

# Special Sequences
# pattern = re.compile(r'\ATata')  #giving raw string as input
# pattern = re.compile(r'\bFax')  #giving raw string as input
# pattern = re.compile(r'Fax\b')  #giving raw string as input
# pattern = re.compile(r'\d5-\d{4}')  #giving raw string as input
pattern = re.compile(r"\b[+4]+ \([\d]+\)\s[\d]+ [0-9]+")  #+44 (20) 7235 8281
#note- in regex, the pattern we want to search, we can pass literal value for eg [\d] -> [0-9]
# or can use meta chars n special sequences ur choice

matches = pattern.finditer(mystr)
for match in matches:
    print(match)
    # print(mystr[448:452])  #span print kela match obj madhla