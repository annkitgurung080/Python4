categoryData=[
    {'id':1,'name':'laptop'},
    {'id':2,'name':'mobile'},
    {'id':3,'name':'tablet'},
    {'id':4,'name':'desktop'}
]

productsData=[
    {'id':1,'name':'dell','category_id':1},
    {'id':2,'name':'mac','category_id':1},
    {'id':3,'name':'iphone','category_id':2},
    {'id':4,'name':'samsung','category_id':2},
    {'id':5,'name':'ipad','category_id':3},
    {'id':6,'name':'samsung tab','category_id':3}
]

# for category in categoryData:
#     print(category['name'])
#     for product in productsData:
#         if category['id']==product['category_id']:
#             print('\t',product['name'])


name=input("Enter Your category name ::(laptop,mobile,tablet,desktop)")
for category in categoryData:
    print(category['name']==name)
    print(category['name'])
    for product in productsData:
        if category['id']==product['category_id']:
            print('\t',product['name'])