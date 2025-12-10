# https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem?isFullScreen=true

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for name, value in attrs:
            print("->", name, ">", value)

    def handle_startendtag(self, tag, attrs):
        print(tag)
        for name, value in attrs:
            print("->", name, ">", value)

N = int(input())
html_string = ""
for _ in range(N):
    html_string += input() + "\n"
parser = MyHTMLParser()
parser.feed(html_string)
parser.close()
