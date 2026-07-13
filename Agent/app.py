import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
# set up everything before we begin the conversation
client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    Ai_personality = input("what personality should the ai have?")
    system_message = "Your name is anora. You are a cute old lady who shares her wisdom and who helps students learn about life. You explain things clearly and always encourage curiosity."
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
#       #send data to an external service
        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=300,
            temperature=0.7,
            system=system_message,
            messages=history
        )

        reply = response.content[0].text
        print(f'Claude: {reply}')
        history.append({'role': 'assistant', 'content': reply})

run_chat()

#personal analogy: I feel like when i meet new people the conversation wouldn't be successful if i dont tell them my history or background because if they dont have that information about me the convo will eventually lead to a dead end with no result 
#when you delete the history.append part you're practically deleting all the conversation history and data, when the ai model deosnt have any data to work with it'll never successfuly continue a conversation or remember information about you the user like your name or preferences 
#when you delete the load.env() line you're basically never loading the ai model since it's stored in the environment we used, everything else will run natrually but when you get to the chatting part with the bot it'll break 
#when you delete this line nothing visible actually changes and it doesnt affect the conversation flow 
#when you type "exit" like loop will break and it'll stop asking you for respones 

# one of the first bugs i encountered is the api key, i changed it multiple times and it never seemed to work and when i tried to run the code it told me api key was not found, turns out i was using a different one the whole time so that was a fun experience 
