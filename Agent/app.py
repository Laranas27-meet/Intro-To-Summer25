import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
# set up everything before we begin the conversation
client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    sum = 0
    print('You: (type exit to quit)')
    Ai_personality = input("what personality should the ai have?")
    system_message = Ai_personality
    history = []

    while True:
        #repeat the same input and constantly ask the user until they type exit
        print(f"turn {len(history)//2}- you: ")
        user_input = input('>> ')

        if user_input.lower() == 'exit':
            break
        if user_input.lower() == 'reset':
            history = []
            print("history cleared")

        history.append({'role': 'user', 'content': user_input})
        #print('History:', history)
        #the messages in the history become more than three because the bot doesnt just remember what we tell it to do but it also needs to remeber it's own respone and have it in the history list, it's as if it's remebering the full conversation flow so it can keep it going 
#       #send data to an external service
        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=300,
            #When i change the max tokens it basically limits the ai's respone, if the max tokens is 5 the respone must be five words or less.
            temperature=1,
            #im assuming the temperature actually controls let's say the patience of the bot so one thing to note is that whne the temperature was 0 the bot stopped repeating the same respone after the second time whereas when i changed the temp to 1 it kept repeating it over and over           system=system_message,
            messages=history
        )
        reply = response.content[0].text
        #print(response)
        print(f'Claude: {reply}')
        print(f'the total tokens used: {sum}')
        total = response.usage.input_tokens + response.usage.output_tokens
        sum = sum + response.usage.input_tokens
        print(f'Tokens used: {response.usage.input_tokens} | Out: {response.usage.output_tokens} | total {total}')
        history.append({'role': 'assistant', 'content': reply})

run_chat()


#personal analogy: I feel like when i meet new people the conversation wouldn't be successful if i dont tell them my history or background because if they dont have that information about me the convo will eventually lead to a dead end with no result 
#when you delete the history.append part you're practically deleting all the conversation history and data, when the ai model deosnt have any data to work with it'll never successfuly continue a conversation or remember information about you the user like your name or preferences 
#when you delete the load.env() line you're basically never loading the ai model since it's stored in the environment we used, everything else will run natrually but when you get to the chatting part with the bot it'll break 
#when you delete this line nothing visible actually changes and it doesnt affect the conversation flow 
#when you type "exit" like loop will break and it'll stop asking you for respones 

# one of the first bugs i encountered is the api key, i changed it multiple times and it never seemed to work and when i tried to run the code it told me api key was not found, turns out i was using a different one the whole time so that was a fun experience 

#usage.input tokens practically represent how many tokens the ai can use to input a message and output is how many tokens it needs to output a message 

#refelection lab2:
#ironically it's quite similar to a bank account, when you make payments on your credit card you don't exactly realize how the price adds up but it all gets counted in ur bank account
#I predict if I delete the history append line the bot will have no messages to work with, it's as if you're in a conversation and you didnt hear what the person asked you. if the bot has no history to work with it'll quite literally not know how to answer you 
#I also think if we deleted the history.append({'role': 'assistant', 'content': reply}) the bot wouldn't even remeber it's own response and the conversation wouldn't flow natrualy in addtion the rate of the token count will change because the ai doesnt even remeber how many tokens it used in it's answer 
#I dont think the ai would behave any differently since the history is still there in the backend code we just dont see it in the terminal because we didnt print it 

#I think the only bug i faced is with the sum because i put it outside of our main function so when i use the variable sum in the function it wouldn't have any value because it's original value was outside of the function 
