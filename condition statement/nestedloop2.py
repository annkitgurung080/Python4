productData={
    {'id':1,'name':'laptop','quantity':10,'price':50000},
    {'id':2,'name':'mobile','quantity':20,'price':20000},
    {'id':3,'name':'tablet','quantity':30,'price':10000},
    {'id':4,'name':'desktop','quantity':40,'price':40000}
}
name=input("Enter Your category name ::(laptop,mobile,tablet,desktop)")
for product in productData:
        if name==product['name']:
            print('\t',product['name'])