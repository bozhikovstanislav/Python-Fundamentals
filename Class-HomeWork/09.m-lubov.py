import itertools

class Message:
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content

    def print_msg_sender(self):
        print(f"{self.content} :{self.sender}")

    def print_sender_msg(self):
        print(f"{self.sender}: {self.content}")


class User:
    def __init__(self, name):
        self.name = name
        self.received_msg_list = []

    def add_msg(self, msg):
        received_msg_list.append(msg)

    def extract_list_of_msgs_by(self, sender):
        list_of_msg_by = []
        for msg in self.received_msg_list:
            if msg.sender == sender:
                list_of_msg_by.append(msg)
        return list_of_msg_by


user_names_list = []
users_list = []

while True:
    str_line = input()
    if str_line == "exit":
        break
    else:
        str_line_split = str_line.split()
        if str_line_split[0] == "register":
            name = str_line_split[1]
            user = User(name)
            user_names_list.append(name)
            users_list.append(user)
        if str_line_split[1] == "send":
            sender = str_line_split[0]
            recipient = str_line_split[2]
            content = str_line_split[3]
            msg = Message(sender, content)
            for user in users_list:
                if sender in user_names_list and user.name == recipient:
                    user.add_msg(msg)

correspondence = input()
from_ = correspondence.split()[0]
to_ = correspondence.split()[1]

# Define which is the longer list of messages and the way they are to be printed out.
for user1, user2 in itertools.combinations(users_list, 2):
    if user1.name == from_ and user2.name == to_:
        from_list = user1.extract_list_of_msgs_by(user2.name)
        to_list = user2.extract_list_of_msgs_by(user1.name)
    elif user2.name == from_ and user1.name == to_:
        from_list = user2.extract_list_of_msgs_by(user1.name)
        to_list = user1.extract_list_of_msgs_by(user2.name)

if len(from_list) <= len(to_list):
    min_len = len(from_list)
    max_list = to_list
else:
    min_len = len(to_list)
    max_list = from_list

if from_list == [] and to_list == []:
    print("No messages")
else:
    i = 0
    while i < min_len: #prints the messages from the 1st and 2nd user one after the other, until the shorter msg list is exhausted.
        to_list[i].print_sender_msg()
        from_list[i].print_msg_sender()
        i += 1
    if len(from_list) != len(to_list): #prints the rest of the messages if one msg list is longer than the other
        for j in range(min_len, len(max_list)):
            if max_list == from_list:
                from_list[j].print_msg_sender()
            elif max_list == to_list:
                to_list[j].print_sender_msg()