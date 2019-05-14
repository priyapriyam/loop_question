 import request
counter ="https://www.geeksforgeeks.org/basic-concepts-of-object-oriented-programming-using-c/"
url=requests.get(counter)
print url.content
