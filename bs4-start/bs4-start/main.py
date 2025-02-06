from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yce_web_page = response.text
print(yce_web_page)


soup = BeautifulSoup(yce_web_page,"html.parser")
article_texts = []
article_links = []
articles = soup.find_all(name="span",class_="titleline")

for article_tags in articles:
    text = article_tags.getText()
    article_texts.append(text)
    link = article_tags.select_one(selector="a").get("href")
    article_links.append(link)
article_upvote = [int(score.getText().split()[0]) for score in soup.select(selector=".score")]

print(article_texts)
print(article_links)
print(article_upvote)

# largestpoint = article_upvote[0]
# for i in article_upvote:
#     if i > largestpoint:
#         largestpoint = i
           #Or

largestpoint = max(article_upvote)
print(largestpoint)

index_of_highestpoint = article_upvote.index(largestpoint)
highestpoint_article_text = article_texts[index_of_highestpoint] 
highestpoint_article_link = article_links[index_of_highestpoint]
print(highestpoint_article_text)
print(highestpoint_article_link)















































# # import lxml        #This for when the "html.parser is not working" 

# with open("./website.html") as file:
#     contents = file.read()
    
# # print(contents)
# # contents is which we required to create our soup.
# soup = BeautifulSoup(contents,"html.parser")  # This "html.parser" help the beautiful soup understand this contents and the soup is the object that
#                                               # help us to tap in to the website.html verious part of the website using python
# # print(soup.title.name)     # gives the name of the title tag 
# # print(soup.title.string)   # The gives the string in the title tag
# # print(soup.prettify())     # This indent the html code in format
# # print(soup.a)
# # print(soup.p)
# # print(soup.prettify()) # This gives the html code prober format
# # print(soup.a) #This gives the first anker tag and by using p or li will give the first p and li

# all_anchor_tag = soup.find_all(name="a") # gives all  the tags as you give argument as the name of the tag to the name parameter
# # print(all_anchor_tag)

# # for tags in all_anchor_tag:
#     # print(tags.getText())
      # print(tags.get("href"))

# heading = soup.find(name="h1",id = "name")
# print(heading)

# section_heading = soup.find(name="h3",class_ = "heading")
# print(section_heading)

# comany_url = soup.select_one(selector="p a")
# print(comany_url)

# name = soup.select_one(selector="#name")
# print(name)

# heading = soup.select(selector= ".heading")
# print(heading)