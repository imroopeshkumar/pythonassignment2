# x = 'hellothere'
# y=x.replace("hello", 'faf')
# print(y)
#
# import pandas as pd
# y = pd.to_datetime('2015-09-09T16:51:12.223')
# print(y.year)
#
import re
# s = r"please. let! this3 wor'k"
# x = re.findall(r'[^\s!,.?":;0-9]+', s)
# print(x)

# translator = str.maketrans('', '', str.punctuation)
# def remove_puncts(input_string):
#     return input_string.translate(translator)
#
# input_string = r"hello there it's a punctuation"
# print(remove_puncts(input_string))

# s = "string. With. Punctuati-on's"
# s = re.sub(r'[^\w\s]','',s)
# print(s)
import re
mylist = 'Although I use Mac, I do not like Mac.'
mylist = re.sub(r'[^\w\s]', '', mylist)
mylist = mylist.split()

mylist = list(dict.fromkeys(mylist))
print(mylist)
