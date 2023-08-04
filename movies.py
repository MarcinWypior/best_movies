from bs4 import BeautifulSoup
import requests

response = requests.get(
    url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.select(class_= ".title",selector="h3")

def remove_first_word(input_string):
    words = input_string.split()
    # Join all the words except the first one
    result = ' '.join(words[1:])
    return result

for title in titles:
    print(title.text)

titles_with_ranking = [remove_first_word(title.text) for title in titles[::-1]]

for title in titles_with_ranking:
    print(title)

