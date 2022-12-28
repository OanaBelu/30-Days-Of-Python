# BeautifulSoup

"""Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser
to provide idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours
or days of work."""


# By default, Beautiful Soup parses documents as HTML. To parse a document as XML, pass in “xml” as the second argument
# to the BeautifulSoup constructor: soup = BeautifulSoup(markup, "xml")
# You’ll need to have lxml installed.


from bs4 import BeautifulSoup

html_doc = """
<html>

<head>
    <title>The Dormouse's story</title>
</head>

<body>
    <p class="title"><b>The Dormouse's story</b></p>

    <p class="story">
        Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.
    </p>

</body>

</html>
"""
soup = BeautifulSoup(html_doc, "html.parser")
print(soup.title)  # <title>The Dormouse's story</title>
print(soup.title.name)  # title
print(soup.title.string)  # The Dormouse's story
print(soup.title.parent.name)  # head
print(soup.p)  # <p class="title"><b>The Dormouse's story</b></p>
print(soup.p['class'])  # ['title']
print(soup.a)  # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
print(soup.find_all('a'))
"""[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, 
<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
 <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]"""
print(soup.find(id="link3"))  # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

for link in soup.find_all('a'):
    print(link.get('href'))
"""http://example.com/elsie
http://example.com/lacie
http://example.com/tillie
"""

print(soup.get_text())
"""
The Dormouse's story


The Dormouse's story

        Once upon a time there were three little sisters; and their names were
        Elsie,
        Lacie and
        Tillie;
        and they lived at the bottom of a well."""

print(soup.original_encoding)
# print(soup.body.p)
# print(soup.head)
# head_tag = soup.head
# title_tag = head_tag.contents[0]
# print(title_tag)
#
# sisters = soup.select(".sister")
#
# for sister in sisters:
#     print(sister.string)
#
# print(soup.prettify())


# from bs4 import CData
#
# cdata = CData("A CDATA block")
# comment.replace_with(cdata)
#
# print(soup.b.prettify())

from bs4 import UnicodeDammit
dammit = UnicodeDammit("Sacr\xc3\xa9 bleu!")
print(dammit.unicode_markup)
# SacrÃ© bleu!
print(dammit.original_encoding)

dammit = UnicodeDammit("Sacr\xe9 bleu!", ["latin-1", "iso-8859-1"])
print(dammit.unicode_markup)
# Sacré bleu!
dammit.original_encoding
# 'latin-1'

from bs4 import SoupStrainer

only_a_tags = SoupStrainer("a")

only_tags_with_id_link2 = SoupStrainer(id="link2")

def is_short_string(string):
    return string is not None and len(string) < 10

only_short_strings = SoupStrainer(string=is_short_string)
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.find_all(only_short_strings))
# ['\n', '\n', '\n', '\n', '\n', '\n', '\n', 'Elsie', 'Lacie', 'Tillie', '\n', '\n', '\n']



# When a parser tells Beautiful Soup about a tag or a string, Beautiful Soup will instantiate a Tag or NavigableString
# object to contain that information. Instead of that default behavior, you can tell Beautiful Soup to instantiate
# subclasses of Tag or NavigableString, subclasses you define with custom behavior:

from bs4 import Tag, NavigableString
class MyTag(Tag):
    pass


class MyString(NavigableString):
    pass


markup = "<div>some text</div>"
soup = BeautifulSoup(markup, 'html.parser')
print(isinstance(soup.div, MyTag))
# False
print(isinstance(soup.div.string, MyString))
# False

my_classes = { Tag: MyTag, NavigableString: MyString }
soup = BeautifulSoup(markup, 'html.parser', element_classes=my_classes)
print(isinstance(soup.div, MyTag))
# True
print(isinstance(soup.div.string, MyString))
# True
