import re
import long_responses as long


# The msg probability function has different parameters, check for recognised words and increment message certainty by 1. 
def message_probability(user_message, recognized_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty += 1

#percentage value is calculated with no. of recognized words.
    percentage = float(message_certainty) / float(len(recognized_words))

#if it has no required works, then break statement is executed.
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

#if it has required words, then return percentage or else zero.
    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0


def check_messages(message):
    highest_prob_list = {} #empty dictionary

    def response(bot_response, list_of_words, single_response=False,required_words=[]): #function to provide bot response
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words) #highest_prob_list will store bot response, 
#which is decided after checking the probability.


    #list of words in the [] and the most required word to provide bot responses. However this is done by finding the best match 
    response('Hello!', ['hello', 'hi', 'whats up', 'hey', 'hej'],single_response=True)
    response('I am doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('Thank you', ['i', 'love', 'chat bot'], required_words=['love'])

    
    best_match = max(highest_prob_list , key=highest_prob_list.get)
    print(highest_prob_list)

    return best_match

file = open("index.html", "w") #we can save the output to a html to open in browser as well.


# The get_response function takes the user_input, splits the message and removes symbols, converts then to lower case, 
# finally check_messages function will the split message and provides response.
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_messages(split_message)
    message = response 
    print('Bot saying: ' + message)
    file.write(message)
    return response 


while True:  #this is always set to true, to consistently send input and receive bot responses
    inn=input('You: ')
    print('You ask: '+ inn)
    print('Chatbot Bot: ' + get_response(inn))
    file.write("\n")
    file.write(inn)
    file.close()
    