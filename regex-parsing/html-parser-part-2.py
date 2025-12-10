# 

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        data = data.split("\n")
        if len(data) > 1:
            print(">>> Multi-line Comment")
            for d in data:
                print(d)
        elif len(data) == 1:
            print(">>> Single-line Comment")
            print(data[0])

    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)


html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()