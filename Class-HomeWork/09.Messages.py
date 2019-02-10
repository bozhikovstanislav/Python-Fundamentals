class User:
    def __init__(self, username, messages=""):
        self.__username = self.set_username(username)
        self.__messages = self.set_messages(messages)

    def set_username(self, username):
        if isinstance(username, str):
            return username

    def get_username(self):
        return self.__username

    def set_messages(self, messages):
        if isinstance(messages, list):
            return messages

    def get_messages(self):
        return self.__messages

    def __str__(self):
        return f'{self.get_username()}'


class Message:
    def __init__(self, content, sender):
        self.__content = self.set_content(content)
        self.__sender = self.set_sender(sender)

    def set_content(self, content):
        if isinstance(content, str):
            return content

    def get_content(self):
        return self.__content

    def set_sender(self, sender):
        if isinstance(sender, User):
            return sender

    def get_sender(self):
        return self.__sender


data = input()
user_lst_history = []
lst_messages = []
while data != "exit":
    data_i = data.split(' ')
    if data_i[0] == "register":
        user_name = data_i[1]
        us = User(user_name)
        user_lst_history.append(us)
    if len(data_i) > 2:
        usr_send = data_i[0]
        user_recip = data_i[2]
        content_i = data_i[3]
        for x in user_lst_history:
            if user_recip == x.get_username():
                message_i = Message(content_i, x)
                lst_messages.append(message_i)
                x.set_messages(lst_messages)
    data = input()
for x in lst_messages:
    print(x.get_sender(), x.get_content())
