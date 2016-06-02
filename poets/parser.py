from html import parser


class PoetParser(parser.HTMLParser):
    def error(self, message):
        pass

    poets = []

    def handle_starttag(self, tag, attrs):

        if tag == 'a':
            attr_map = dict(attrs)
            if 'title' in attr_map:
                title = attr_map['title']
                self.poets.append(title)
