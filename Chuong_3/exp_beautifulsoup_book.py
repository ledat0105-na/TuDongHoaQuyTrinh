from bs4 import BeautifulSoup
import requests

URL = "http://books.toscrape.com"
response = requests.get(URL)
content_response = response.content
soup = BeautifulSoup(content_response, "html.parser")

product_books = soup.find_all("article", class_="product_pod")
print(product_books)
for i_book in product_books:
    # print (i_book)
    # name
    name = i_book.h3.a["title"]
    print(name)

    price = i_book.find("p", class_="price_color").text
    print(price)

    start_rating = i_book.p["class"][1]
    print(start_rating)

    in_stock = i_book.find("p", class_="instock availability").text.strip()
    print(in_stock)

    dict_book = {
        "name": name,
        "price": price,
        "start_rating": start_rating,
        "in_stock": in_stock
    }

    data_book.append(dict_book) 
print(data_books)
print("-------------------------------")
df_input = pd.DataFrame(data=data_books)

print(df_input)

