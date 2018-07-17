import urllib.request, urllib.parse, urllib.error
import lxml.html

flag = 0
print("Enter Website")
x = input()
if "http://" not in x:
    website = "http://" + x
elif "https://" in x:
    website = "http://" + x
else:
    website = x
try:
    connection = urllib.request.urlopen(website)
    dom = lxml.html.fromstring(connection.read())
    avi = 1
except:
    print("There are no such website")
    avi = 0
linklist = []
if (avi == 1):
    for link in dom.xpath('//a/@href'):
        if link != "#":
            print(link)
            link = link.lower()
            linklist.append(link)
            linklist.sort()

    search = input("Search:").lower()
    searchlink = ''
    for i in linklist:
        if search in i:
            flag = 1
            if "http://" not in i:
                if i.startswith("/"):
                    if searchlink != i:
                        searchlink = "http://" + x + i
                        print(searchlink)
                        temp = searchlink
                else:
                    if searchlink != i:
                        searchlink = "http://" + x + "/" + i
                        print(searchlink)
                        temp = searchlink
            else:
                if searchlink != i:
                    searchlink = i
                    print(searchlink)
                    temp = searchlink
    if flag == 0:
        print("Search not found...")
