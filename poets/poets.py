import re
from http import client
from random import randint

from poets.parser import PoetParser

ORG_WIKI_LIST_OF_POETS = 'en.wikipedia.org'
pattern = re.compile("^[A-Z]{1}[a-zA-Z-]* [A-Z]{1}[a-zA-Z-]*$")


def poets() -> str:
    res = client.HTTPSConnection(ORG_WIKI_LIST_OF_POETS)
    res.request("GET", "/wiki/List_of_poets")
    html = res.getresponse().read()
    parser = PoetParser()
    parser.feed(str(html))
    poets_list = parser.poets
    poet = poets_list[randint(0, len(poets_list) - 1)]
    while not pattern.match(poet):
        poet = poets_list[randint(0, len(poets_list) - 1)]
    return poet
