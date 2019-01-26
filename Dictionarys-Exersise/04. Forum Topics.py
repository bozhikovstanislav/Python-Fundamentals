data = input()
forum_dict = {}

while not data == 'filter':
    topic = data.split(' -> ')[0]
    hashtags = data.split(' -> ')[1].split(', ')
    if topic in forum_dict.keys():
        forum_dict[topic].extend(hashtags)
    else:
        forum_dict[topic] = hashtags
    data = input()

hashtags_reg = input().split(', ')

for topic, hashtags in forum_dict.items():
    unique_tags_list = sorted(set(hashtags), key=hashtags.index)
    forum_dict[topic] = unique_tags_list
    hashtags_reg_set = set(hashtags_reg)
    if hashtags_reg_set.issubset(hashtags):
        print(f'{topic} | ', end='')
        print(f'''{", ".join(list(map(lambda x:'#'+x, unique_tags_list)))}''')
