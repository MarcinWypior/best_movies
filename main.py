from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, 'html.parser')

article_titles = []
article_links = []
for article_tag in soup.find_all(name="span", class_="titleline"):
    article_titles.append(article_tag.getText())
    article_links.append(article_tag.find("a")["href"])

article_upvotes = []
for article in soup.find_all(name="td", class_="subtext"):
    if article.span.find(class_="score") is None:
        article_upvotes.append(0)
    else:
        article_upvotes.append(int(article.span.find(class_="score").contents[0].split()[0]))

max_points_index = article_upvotes.index(max(article_upvotes))
print(
    f"{article_titles[max_points_index]}, "
    f"{article_upvotes[max_points_index]} points, "
    f"available at: {article_links[max_points_index]}."
)


# ranking_list = []
# for i in range(len(list_of_titles)):
#     print(list_of_titles[i].getText(),'---',list_of_scores[i].getText(),"\n")
#     ranking_list.append((list_of_titles[i],list_of_scores[i]))





# with open("website.html", encoding="utf-8") as webpage:
#     content = webpage.read()
#
# soup = BeautifulSoup(content,'html.parser')
#
#

# form_tag = soup.find("input")
# max_length = form_tag.get("maxlength")
# print(max_length)

# max_length = form_tag.maxlength
# max_length = form_tag.attr("maxlength")
# max_length = form_tag.attrs("maxlength")
# max_length = form_tag.get("maxlength")
# all_anchor_tags = soup.find_all(name="a")
#
# for tag in all_anchor_tags:
#     print(tag.get("href"))

# heading = soup.find(name="h1", id= "name")
# print("\n ",heading)
#
# company_url = soup.select_one(selector="p a")
# print("\n company url: ",company_url)
#
# name = soup.select_one(selector="#name")
# print("\n name: ",name.text)
