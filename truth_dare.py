# Truth or Dare

from random import choice
from time import sleep

truth = [
   "What was the last lie you told?",
   "What is your biggest fear?",
   "Who was the last person you stalked on social media?",
   "If you could be invisible for a day, what would you do?"
]

dare = [
 "Imitate a chicken for 15 seconds.", "Speak with a funny accent until your next turn.", "Send an audio message to your third WhatsApp contact singing 'Baby Shark'.", "Do 10 jumping jacks now."
]

def start_time(seconds):
    while seconds > 0:
        print(f"Time remaining: {seconds} seconds", end="\r")
        sleep(1)
        seconds -= 1
    print('\nTime out!')
    
while True:
	print('---TRUTH OR DARE?---')
	
	user_choice = str(input('Truth or Dare?\n')).strip().lower()[0]
	
	if user_choice == 't':
		print(choice(truth))
		start_time(60)
	elif user_choice == 'd':
		print(choice(dare))
		start_time(60)
		
	user_continue = str(input('Continue?[Y/N]\n')).strip().lower()[0]
	
	if user_continue == 'n':
		print('Thanks for playing!')
		break