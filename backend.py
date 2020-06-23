from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re

url = input("website to test: ")
keyword = input("keyword to search: ")
keyword = keyword.casefold()

try:
    req = Request(url, headers={"User-Agent":"Mozilla/6.0"})
    html = urlopen(req)
except HTTPError as e:
    print(e)

html = urlopen(url)
data = BeautifulSoup(html, "html.parser")

def seo_title(keyword, data):
    if data.title:
        if keyword in data.title.text.casefold():
            status = "Found"
        else:
            status = "Keyword Not Found"
    else:
        status = "No title found"
    return status

def seo_stop_words(data):
    words = 0
    list_words = []
    if data.title:
        with open("stop_words_list.txt", "r") as f:
            for line in f:
                if re.search(r"\b" + line.rstrip("\n") + r"\b", data.title.text.casefold()):
                    words += 1
                    list_words.append(line.rstrip("\n"))
        if words > 0:
            stop_words = "Found {} stop words. - {}".format(words, list_words)
        else:
            stop_words = "No stop words found"
    else:
        stop_words = "No title found"
    return stop_words

def seo_title_length(data):
    if data.title:
        if len(data.title.text) < 60:
            length = "Length under maximum characters. Length = {}".format(len(data.title.text))
        else:
            length = "Length over maximum characters. Length = {}".format(len(data.title.text))
    else:
        length = "No title found"
    return length

def seo_url(url):
    if url:
        if keyword in url:
            slug = "Keyword found in URL."
        else:
            slug = "Keyword not found in URL, suggest add keyword to slug"
    else:
        slug = "No url was returned"
    return slug

def seo_url_length(url):
    if url:
        if len(url) < 100:
            url_length = "URL have {} characters, recommended 100.".format(len(url))
        else:
            url_length = "URL over maximum 100 recomended = {}".format(len(url))
    else:
        url_length = "URL not found"
    return url_length

def seo_h1(keyword, data):
    total_h1 = 0
    total_keyword_h1 = 0
    if data.h1:
        all_tags = data.find_all("h1")
        for tag in all_tags:
            total_h1 += 1
            tag = str(tag.string)
            if keyword in tag.casefold():
                total_keyword_h1 += 1
                h1_tag = "Found keyword in H1 Tag. {} Tags".format(total_h1)
            else:
                h1_tag = "Keyword not found in H1 Tag."
    else:
        h1_tag = "No H1 Tags Found"
    return h1_tag

def seo_h2(keyword, data):
    total_h2 = 0
    total_keyword_h2 = 0
    if data.h2:
        all_tags = data.find_all("h2")
        for tag in all_tags:
            total_h2 += 1
            tag = str(tag.string)
            if keyword in tag.casefold():
                total_keyword_h2 += 1
                h2_tag = "Found keyword in H2 Tag. {} Tags".format(total_h2)
            else:
                h2_tag = "Keyword not found in H2 Tag."
    else:
        h2_tag = "No H2 Tags Found"
    return h2_tag

print(seo_title(keyword, data))
print(seo_stop_words(data))
print(seo_title_length(data))
print(seo_url(url))
print(seo_url_length(url))
print(seo_h1(keyword, data))
print(seo_h2(keyword, data))



