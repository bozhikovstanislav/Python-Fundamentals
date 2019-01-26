data = input()
social_media_dict = {}
while not data == 'drop the media':
    command = data.split()[0]
    post_name = data.split()[1]
    if command == 'post':
        social_media_dict[post_name] = {'likes': 0, 'dislikes': 0, 'comments': []}
    elif command == 'like':
        if post_name in social_media_dict.keys():
            social_media_dict[post_name]['likes'] += 1
    elif command == 'dislike':
        if post_name in social_media_dict.keys():
            social_media_dict[post_name]['dislikes'] += 1
    elif command == 'comment':
        author = data.split()[2]
        content = data.split()[3:]
        if post_name in social_media_dict.keys():
            comment = {author: content}
            social_media_dict[post_name]['comments'].append(comment)

    data = input()
for post_name, post_data in social_media_dict.items():
    print(f'Post: {post_name} | Likes: {post_data["likes"]} | Dislikes: {post_data["dislikes"]}')
    print('Comments:')
    if not post_data['comments']:
        print('None')
        continue
    for comment in post_data['comments']:
        for current_post in comment:
            print(f'*  {current_post}: {" ".join(comment[current_post])}')
