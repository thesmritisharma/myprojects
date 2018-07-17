from tkinter import *
import urllib.request, urllib.parse, urllib.error
import lxml.html
import requests
import timeit
import html5lib
from bs4 import BeautifulSoup
import re
import webbrowser

root = Tk()
root.geometry("1200x600")
# root.state('zoomed')
root.title("Search Engine")


def ShowResult(database):
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)

    listbox = Listbox(root, width=100, height=20, font=("", 15))
    listbox.place(x=10, y=50)

    for item in database:
        listbox.insert(END, item)

    # bind listbox to scrollbar
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)
    ShowResult.f = 0

    def openweb(event):
        url = listbox.get(ACTIVE)
        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(url)

    def do(event):
        if ShowResult.f == 1:
            do.lineshow.destroy()
        value = str((listbox.get(ACTIVE)))
        do.lineshow = Label(root, text=value, fg="blue", font=("", 15, "bold"))
        do.lineshow.place(x=10, y=550)
        ShowResult.f = 1

    callback = lambda event: do(event)
    callback2 = lambda event: openweb(event)

    listbox.bind("<Button-1>", callback)
    listbox.bind("<Double-Button-1>", callback2)


def createlist():
    search = X.get()
    results = 10
    database = []
    start = timeit.default_timer()
    page = requests.get("https://www.google.com/search?q={}&num={}".format(search, results))
    soup = BeautifulSoup(page.content, "html5lib")
    links = soup.findAll("a")
    for link in links:
        link_href = link.get('href')
        if "url?q=" in link_href and not "webcache" in link_href:
            mysearch = link.get('href').split("?q=")[1].split("&sa=U")[0]
            database.append(mysearch)
    ShowResult(database)


label = Label(root, text="Welcome to Search Engine")
X = Entry(root, width=40)
X.pack()
show = Button(root, text="Submit", command=createlist)
show.pack()
root.mainloop()