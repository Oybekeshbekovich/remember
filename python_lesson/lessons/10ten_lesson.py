# #1-exec
# def str_capitalize(names2):
#     return names2.capitalize()
#
# names = ['alfred', 'tabitha', 'william', 'arla']
# names2=list(map(lambda x:str(x).capitalize(),names))
# print(names2)
#
# #2-exec
# scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
#
# def over_seventy(element):
#     return  element>=75
#
#
# scores1=list(filter(over_seventy, scores))
# print(scores1)
#
# scores2=list(filter(lambda x:x>=75, scores))
# print(scores2)
#
# # 3-exec
# words = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']
# palindrome = list(filter(lambda word: word.lower() == word.lower()[::-1], words))
# print(palindrome)