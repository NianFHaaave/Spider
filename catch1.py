import urllib.request

if __name__ == "__main__":
    res = request.urlopen()
    html = res.read()
    html = html.decode("utf-8")
    print(html)
