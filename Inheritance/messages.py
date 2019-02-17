import math

#defining class user
#creating a list as a default parameter for the messages in constructor (__init__()) is very dangerous, because it is a reference type #and we MUST creating new list every time we make a new user see this line 'user_to_recieve.received_messages = []'

class User:
    def __init__(self, username, messages=[]):
        self.username = username
        self.received_messages = messages


class Message:
    def __init__(self, content, sender):
        self.content = content
        self.sender = sender


data = input()

users = []

while not data == 'exit':
#we check if we have to register a user
    if data.split()[0] == 'register':
        user = User(data.split()[1])
        users.append(user)
#here we receive a message
    else:
        sender = data.split()[0]
        recipient = data.split()[2]
        content = data.split()[3:]
		
		#we make a list from all of our users names using map()
        user_names_list = list(map(lambda user: user.username, users))

		#we check if this if we have such name in our list for sender AND also for recipient
        if sender in user_names_list and recipient in user_names_list:
			#we create a new message
            message = Message(content[0], sender)
			# we take the recipient OBJECT filtering our users (list of objects not just the names list) using filter and we say [0],
			#because we want the object not the list
            user_to_recieve = list(filter(lambda usr: usr.username == recipient, users))[0]

			#Here is the dangerous par. We first should check if this user has already any messages, if it so we append BUT if the user 
			#do not have any we create A NEW LIST

            if user_to_recieve.received_messages:
                user_to_recieve.received_messages.append(message)
            else:
                user_to_recieve.received_messages = []
                user_to_recieve.received_messages.append(message)



    data = input()

first_user, second_user = input().split()

#after we have the names of the users we should find the objects
first_user_obj = list(filter(lambda user: user.username == first_user, users))[0]
second_user_obj = list(filter(lambda user: user.username == second_user, users))[0]


#here we take a list of all received messages of USER2 FROM USER1
received_m_from_user_1 = list(filter(lambda m: m.sender == first_user, second_user_obj.received_messages))
#here we take a list of all received messages of USER1 FROM USER2
received_m_from_user_2 = list(filter(lambda m: m.sender == second_user, first_user_obj.received_messages))
# we take all send messages from user 1
send_form_user_1 = list(filter(lambda m: m.sender == first_user, second_user_obj.received_messages))

#Here is the heavy part. Because the lists of messages could be with different length. Clever way to deal with that is to take smaller #list length and iterating over it first through the both lists at the same time. After that we will take from that index to the end of #the longer list with second separate for loop 

smallest_list = min(len(received_m_from_user_1), len(received_m_from_user_2))
longest_list = max(len(received_m_from_user_1), len(received_m_from_user_2))

#we check if first user is a sender of a some of the received messages of user 2
messages_1 = first_user in list(map(lambda user: user.sender, second_user_obj.received_messages))

#we check if second user is a sender of a some of the received messages of user 1
messages_2 = second_user in list(map(lambda user: user.sender, first_user_obj.received_messages))


#we check with or NOT with and because it is enough just one of them to send a message. We do not look for responses according the #exercises description

if messages_1 or messages_2:
	# we use 'for in range' in order to get just the indexes and be able to go through the both list in one for loop 
    for index in range(smallest_list):
        print(f'{received_m_from_user_1[index].sender}: {received_m_from_user_1[index].content}')
        print(f'{received_m_from_user_2[index].content} :{received_m_from_user_2[index].sender}')

    for index in range(smallest_list, longest_list):
        if len(received_m_from_user_2) > len(received_m_from_user_1):
            print(f'{received_m_from_user_2[index].content} :{received_m_from_user_2[index].sender}')
        else:
            print(f'{received_m_from_user_1[index].sender}: {received_m_from_user_1[index].content}')

else:
    print('No messages')