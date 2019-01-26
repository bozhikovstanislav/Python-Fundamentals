'''
Write a program, which searches for a key and value inside of several key-value pairs.
Input
On the first line, you will receive a key.
On the second line, you will receive a value.
On the third line, you will receive N.
On the next N lines, you will receive strings in the following format:
“key => {value 1};{value 2};…{value X}”
After you receive N key -> values pairs, your task is to go through them and print only the keys,
 which contain the key and the values, which contain the value. Print them in the following format:

{key}:
-{value1}
-{value2}
…
-{valueN}
'''

str_key = input()
str_value = input()
str_n = int(input())

str_to_dic = {}
for i in range(0, str_n):
    str_dic_list = input().split(' => ')
    key = str_dic_list[0]
    value_dic = str_dic_list[1].split(";")
    if key not in str_to_dic:
        str_to_dic[key] = value_dic


for key, v in str_to_dic.items():
    if str_key in key:
        print(f'{key}:')
        print(end="")
        for val in range(len(v)):
            if str_value in v[val]:
                print(f'-{v[val]}')
