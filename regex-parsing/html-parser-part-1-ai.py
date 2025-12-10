from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for attr, value in attrs:
            print("->", attr, ">", value)

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for attr, value in attrs:
            print("->", attr, ">", value)

if __name__ == "__main__":
    n = int(input().strip())
    html = ""
    for _ in range(n):
        html += input() + "\n"

    parser = MyHTMLParser()
    parser.feed(html)
    parser.close()
