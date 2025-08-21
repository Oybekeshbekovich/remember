#from pprint import pprint
#import json
#import requests

#json_data=[]
#
# while True:
#     name=input("Enter your name: ")
#     if name.lower()=="stop":
#         pprint(json_data,sort_dicts=False)
#         with open ("json_data.json","w",encoding="utf-8") as f:
#             json.dump(json_data,f,ensure_ascii=False,indent=4)
#         break
#     lastname=input("Enter your last name: ")
#     age=int(input("Enter your age: "))
#     json_data.append({"name":name,
#                       "lastname":lastname,
#                       "age":age})

#
# json_string = '{"name": "Alice", "age": 30, "city": "New York"}'
# data = json.loads(json_string)
#
# print(data)

# users=requests.get("https://jsonplaceholder.typicode.com/users").json()
# #print(users)
# for user in users:
#     pprint(user['name'],sort_dicts=False)


# parametrs={
#     'appid':'787ef893f279189c345e07f5f58c6015',
#     'unit':'metric',
#     'lang':'ru',
# }
# while True:
#     city=input("Enter the city name: ")
#     if city.lower()=='stop':
#         with open("json_data.json",mode="w",encoding="utf-8") as f:
#             json.dump(json_data,f,indent=4,ensure_ascii=False)
#         break
#     parametrs['q']=city
#     response = requests.get('https://api.openweathermap.org/data/2.5/weather?',params=parametrs)
#     data = response.json()
#     json_data.append({
#         'city':city,
#         'temp':data['main']['temp'],
#         'description':data['weather'][0]['description'],
#         'icon':data['weather'][0]['icon'],
#     })
