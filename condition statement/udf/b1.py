books=[
    {'title':'Python','price':100},
    {'title':'Java','price':200},
    {'title':'C','price':300},
    {'title':'C++','price':400},
    {'title':'ruby','price':500},
    {'title':'php','price':600},
    {'title':'Javascript','price':700},
    {'title':'C#','price':800},
    {'title':'Go','price':900},
    {'title':'Swift','price':1000}
]
def filter_books(books, min_price):
    return [book for book in books if book['price'] > min_price]

print(filter_books(books, 501))  