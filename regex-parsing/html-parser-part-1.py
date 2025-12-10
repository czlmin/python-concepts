# https://www.hackerrank.com/challenges/html-parser-part-1/problem?isFullScreen=true

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for name, value in attrs:
            print("->", name, ">", value)

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for name, value in attrs:
            print("->", name, ">", value)

N = int(input())
html_string = ""
for _ in range(N):
    html_string += input() + "\n"
parser = MyHTMLParser()
parser.feed(html_string)
parser.close()
