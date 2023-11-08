from pymongo import MongoClient
cluster=MongoClient("mongodb://localhost:27017")
from pprint import pprint

print(cluster.list_database_names())

# #create database ecommerce
db=cluster["ecommerce"]
# #list collections
customers = db["customers"]
#inserting values
# data= {'first_name':'Bruce', 'last_name': 'Wayne', 'email':'bruce.wayne@example.com'}
# customers.insert_one(data)

# data= [{'first_name':'John','last_name':'Doe','email':'john.doe@example.com'}, 
#        {'first_name':'Bruce', 'last_name': 'Wayne', 'email':'bruce.wayne@example.com'} ]
# customers.insert_many(data)

# customers.delete_one({"first_name":"Bruce","last_name":"Wayne"})
# customers.delete_many({})


# one-to-one relationship embedded document
# customers.update_one({"first_name":"Jane"},{"$set":{"Address":{"street":"downing street1","code":6000,"country":"UK"}}})
# customers.update_one({"first_name":"John"},{"$set":{"Address":{"street":"downing street2","code":6001,"country":"USA"}}})
# customers.update_one({"first_name":"Peter"},{"$set":{"Address":{"street":"downing street3","code":6002,"country":"India"}}})
# customers.update_one({"first_name":"Mary"},{"$set":{"Address":{"street":"downing street4","code":6003,"country":"India"}}})
# customers.update_one({"first_name":"Bruce"},{"$set":{"Address":{"street":"downing street5","code":6004,"country":"USA"}}})


#one to many relationship embedded documents
# customers.update_one({"first_name":"Jane"},{"$set":{"Address":[{"street":"downing street1","code":6000,"country":"UK"}, {"street":"city center","code":6232,"country":"UK"}]}})
# customers.update_one({"first_name":"John"},{"$set":{"Address":[{"street":"downing street2","code":6001,"country":"USA"},{"street":"city center1","code":6233,"country":"USA"}]}})
# customers.update_one({"first_name":"Peter"},{"$set":{"Address":[{"street":"downing street3","code":6002,"country":"India"},{"street":"city center2","code":6234,"country":"India"}]}})
# customers.update_one({"first_name":"Mary"},{"$set":{"Address":[{"street":"downing street4","code":6003,"country":"India"},{"street":"city center3","code":6235,"country":"India"}]}})
# customers.update_one({"first_name":"Bruce"},{"$set":{"Address":[{"street":"downing street5","code":6004,"country":"USA"},{"street":"city center4","code":6236,"country":"USA"}]}})



# one to one relationship with document reference
from bson.objectid import ObjectId
verification=db['verification']
# data= [ {'customer_id':ObjectId("653fb3ffa2a720521e125432"),'verification_number':12345}, 
#         {'customer_id':ObjectId("653fb52513d9f2899d18107f"),'verification_number':67859},
#         {'customer_id':ObjectId("653fb52513d9f2899d181080"),'verification_number':18273},
#         {'customer_id':ObjectId("6540f741bf56545438a9d82e"),'verification_number':49042},
#         {'customer_id':ObjectId("65438b7daab45799eddc2c90"),'verification_number':12233} ]
# verification.insert_many(data)

# output=verification.aggregate([
#     {"$lookup":{"from":"customers", "localField":"customer_id", "foreignField" : "_id", "as": "verify"} }])

# output=customers.aggregate([
#     {"$lookup":{"from":"verification", "localField":"_id", "foreignField" : "customer_id", "as": "verify"} }])
# for document in output:
#     pprint(document["verify"])


#products collection
# products=db['products']
# data={"name":'iPhone 14 Pro Max', "description":'Latest iPhone.', "price":1099, "category":'Electronics'}

# products.insert_one(data)

# products=db['products']
# products_list = [('iPhone 14 Pro Max', 'Latest iPhone.', 1099.00, 'Electronics'),
#  ('Galaxy S22 Ultra', 'Best Android phone.', 1199.00, 'Electronics'),
#   ('MacBook Air M2', 'Popular Apple laptop.', 999.00, 'Electronics'),
#   ('iPad Pro 2023', 'Best tablet for power users.', 799.00, 'Electronics'),
#   ('Sony WH-1000XM5', 'Best noise-cancelling headphones.', 399.00, 'Electronics'),
#   ('Air Jordan 1', 'Popular sneaker.', 175.00, 'Clothing'),
#   ('Yeezy Boost 350 v2', 'Another popular sneaker.', 220.00, 'Clothing'),
#   ('Instant Pot Duo Plus', 'Multi-cooker.', 129.00, 'Home & Garden'),
#   ('Ninja Air Fryer Max', 'Air fryer.', 99.00, 'Home & Garden'),
#   ('Vitamix 5200 Blender', 'Powerful blender.', 499.00, 'Home & Garden'),
#   ('iRobot Roomba j7+', 'Self-emptying robot vacuum.', 799.00, 'Home & Garden'),
#   ('Google Nest Hub Max', 'Smart display.', 229.00, 'Home & Garden')]

# products_data = [{"name": product[0], "description": product[1], "price":product[2], "category":product[3]} for product in products_list]
# print(products_data)
# products.insert_many(products_data)

# products=db['products']
# products.update_many({"category":"Electronics"},{"$set":{"color":["black", "white","red"]}})
# products.update_many({"category":"Home & Garden"},{"$set":{"color":["grey", "silver"]}})
# products.update_many({"category":"Clothing"},{"$set":{"color":["red", "blue", "green","black","white"]}})


# one to many relationship document reference
# order_items collection
# order_items = db['order_items']
# order_items_data = [{"order":[{"product_id":ObjectId("654255fc54d068ebd3068864"),"quantity":2}, {"product_id":ObjectId("6540dd08ba702507964aad29"),"quantity":2}]},
#                     {"order":[{"product_id":ObjectId("6540dd08ba702507964aad2a"),"quantity":3}, {"product_id":ObjectId("654255fc54d068ebd3068867"),"quantity":4}]},
#                     {"order":[{"product_id":ObjectId("654255fc54d068ebd3068868"),"quantity":5}]}]
# order_items.insert_many(order_items_data)


# order_items = db["order_items"]
# output=order_items.aggregate([
#     {"$lookup":{"from":"products", "localField":"order.product_id", "foreignField" : "_id", "as": "product_details"} },
#     {"$project":{"product_details":1,"order":1}}
#     ])
# for document in output:
#     pprint(document)


# output=order_items.aggregate([
#     {"$lookup":{"from":"products", "localField":"order.product_id", "foreignField" : "_id", "as": "product_details"} },
#     {"$project":{"product_details.name":1,"order.product_id":1}}
#     ])
# for document in output:
#     pprint(document)








