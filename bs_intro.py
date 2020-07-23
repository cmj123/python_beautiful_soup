# Import the required libraries
from bs4 import BeautifulSoup
import re

input = '''<html>
<head><title>Page title</title></head>
<p id="firstpara" align="center"> This is a paragraph <b>one</b>
<p id="secondpara" align="blah"> This is paragraph <b>two</b>
</html>'''

soup = BeautifulSoup(input, "lxml")
titleTag = soup.html.head.title
print(titleTag)
print(titleTag.string)
print(len(soup('p')))
print(soup('p', {'id':'secondpara'}))
print(soup('p', {'id':'secondpara'})[0]['id'])
print(soup('p')[1].b.string)
titleTag['id'] = 'theTitle'
titleTag.string = "New Title"
print("--title & contents")
print(soup.html.head.title)
print(soup.html.head.title.contents)


print("----- part 2 -----")
html_doc = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="title">
            <b>The Dormouse's story</b>
        </p>
        <p class="story">
            Once uopon a time there were three little sisters; and
            their names were
            <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
            <a href="http://example.com/lancie" class="sister" id="link2">Lancie</a> and
            <a href="http://example.com/lancie" class="tillie" id="link3">Tillie</a>;
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.head)
print(soup.title.string)
print(soup.body.b)
print(soup.a)
print(len(soup.find_all('a')))
