
# def show_expensive_books(books):
#     return [book for book in books if book['price'] > 500]

# books=[
#     {'title':'Python','price':100},
#     {'title':'Java','price':200},
#     {'title':'C','price':300},
#     {'title':'C++','price':400},
#     {'title':'ruby','price':500},
#     {'title':'php','price':600},
#     {'title':'Javascript','price':700},
#     {'title':'C#','price':800},
#     {'title':'Go','price':900},
#     {'title':'Swift','price':1000}
# ]

# print(show_expensive_books(books))
# OR

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
def filterData(book):
    return book['price']>500

print(list(filter(filterData,books)))
