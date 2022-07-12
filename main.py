from bs4 import BeautifulSoup
import requests
from termcolor import colored

main_source = requests.get("https://www.tagesschau.de/").text
main_soup = BeautifulSoup(main_source, "lxml")
main_articles = main_soup.find_all("div", class_ = "teaser teaser--small")

source1 = requests.get('https://www.tagesschau.de/inland//').text
soup1 = BeautifulSoup(source1, 'lxml')
articles1 = soup1.find_all("div", class_ = "teaser teaser--small")

source2 = requests.get("https://www.tagesschau.de/ausland/").text
soup2 = BeautifulSoup(source2, 'lxml')
articles2 = soup2.find_all("div", class_ = "teaser teaser--small")

source3 = requests.get("https://www.tagesschau.de/wirtschaft/").text
soup3 = BeautifulSoup(source3, 'lxml')
articles3 = soup3.find_all("div", class_ = "teaser teaser--small")	

source4 = requests.get("https://www.tagesschau.de/wetter/").text
soup4 = BeautifulSoup(source4, 'lxml')
articles4 = soup4.find("div", class_ = "columns twelve m-eight")

main_article_heading = []
main_article_text = []
article_inland_heading = []
article_inland_text = []
article_ausland_heading = []
article_ausland_text = []
article_wirtschaft_heading = []
article_wirtschaft_text = []
article_wetter_heading = []
article_wetter_text = []

for article in main_articles:
    main_article_heading.append(article.find("span", class_ = "teaser__topline").text.strip())
    main_article_text.append(article.find("p", class_ = "teaser__shorttext").text.strip())

for article in articles1:
    article_inland_heading.append(article.find("span", class_ = "teaser__topline").text.strip())
    article_inland_text.append(article.find("p", class_ = "teaser__shorttext").text.strip())
    
for article in articles2:
    article_ausland_heading.append(article.find("span", class_ = "teaser__topline").text.strip())
    article_ausland_text.append(article.find("p", class_ = "teaser__shorttext").text.strip())    

for article in articles3:
    article_wirtschaft_heading.append(article.find("span", class_ = "teaser__topline").text.strip())
    article_wirtschaft_text.append(article.find("p", class_ = "teaser__shorttext").text.strip())

article_wetter_heading.append(articles4.find("span", class_="hyphenate").text.strip())
article_wetter_text.append(articles4.find("p", class_="teaser__shorttext").text.strip())

def article_to_see():
    print("\n")
    print(colored("Tagesschau Nachrichten", "blue"))
    choose = input("Möchtest du die Hauptnachrichten sehen? (y/n): ")
    if choose == "y":
        print("\n")
        print(colored("Hauptnachrichten:", "green"))
        print("")
        for i in range(5):
            print(colored(main_article_heading[i], "green"))
            print(main_article_text[i])
            print("-"*50)
            print("\n")
    else:
        choose = input("Möchtest du die Nachrichten in einzelne Segmente sehen? (y/n) ")
        if choose == "y":
            articles_to_see = 3
            print("\n")
            print(colored("Inland:", "green"))
            print("")
            for i in range(articles_to_see):
                print(f"{i+1}. {article_inland_heading[i]}")
                print(f"{article_inland_text[i]}")
                print("-"*50)
                print("\n")
            print(colored("Ausland:", "yellow"))
            print("")
            for i in range(articles_to_see):
                print(f"{i+1}. {article_ausland_heading[i]}")
                print(f"{article_ausland_text[i]}")
                print("-"*50)
                print("\n")
            print(colored("Wirtschaft:", "magenta"))
            print("")
            for i in range(articles_to_see):
                print(f"{i+1}. {article_wirtschaft_heading[i]}")
                print(f"{article_wirtschaft_text[i]}")
                print("-"*50)
                print("\n")
            print(colored(article_wetter_heading[0], "cyan"))
            print(article_wetter_text[0])
            print("-"*50)
            print("\n")

article_to_see()