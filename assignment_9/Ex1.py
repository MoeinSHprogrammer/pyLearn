import telebot
import random
from khayyam import JalaliDate
import re
from gtts import gTTS
import os
import qrcode

game_in_progress = False
age_in_progress =False
textToSpeech_in_progress = False
maxFinder_in_progress = False
maxIndexFinder_in_progress = False
qrcodeMaker_in_progress = False
secret_number = None
# Replace 'YOUR_BOT_TOKEN' with your actual bot token obtained from BotFather
bot = telebot.TeleBot('Token')

# Handler for the /start command
@bot.message_handler(commands=['start'])
def welcome(message):
    # Extracting the user's first name from the message
    user_name = message.from_user.first_name
    # Sending the welcome message
    bot.reply_to(message, f"Welcome {user_name}! How can I assist you today?")

# Handler for all other messages
@bot.message_handler(commands=['game'])
def start_game(message):
    global game_in_progress
    game_in_progress = True
    bot.reply_to(message, "Welcome to the number guessing game! I'm thinking of a number between 1 and 100. Try to guess it!")

@bot.message_handler(commands=['age'])
def start_age_calculation(message):
    global age_in_progress
    age_in_progress = True
    bot.reply_to(message, "Enter your birthdate in Hijri format YYYY-MM-DD: ")

@bot.message_handler(commands=['voice'])
def text_to_speech(message):
    global textToSpeech_in_progress
    textToSpeech_in_progress = True
    bot.reply_to(message, "Send me Your English Sentences ")
    
@bot.message_handler(commands=['max'])
def maximum_finder(message):
    global maxFinder_in_progress
    maxFinder_in_progress = True
    bot.reply_to(message, "Send me an array in form a,b,c,...")

@bot.message_handler(commands=['argmax'])
def maximum_index_finder(message):
    global maxIndexFinder_in_progress
    maxIndexFinder_in_progress = True
    bot.reply_to(message, "Send me an array in form a,b,c,...")

@bot.message_handler(commands=['qrcode'])
def qrcode_maker(message):
    global qrcodeMaker_in_progress
    qrcodeMaker_in_progress = True
    bot.reply_to(message, "Send me Your English Sentences ")

@bot.message_handler(commands=['help'])
def helper(message):
    bot.reply_to(message, "/start startBot\n/game playing guess number\n/age calculate your age\n/voice your text to speech\n/max maximum number in array's elements\n/argmax index of maximum number in array's elements\n/qrcode your text to qrcode ")

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Handler for inline keyboard buttons
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    global secret_number , game_in_progress, age_in_progress

    if call.data == 'new_game':
        secret_number = random.randint(1, 100)
        game_in_progress = True
        bot.send_message(call.message.chat.id, "New game started! I'm thinking of a number between 1 and 100. Try to guess it!")
    if call.data == 'exit':
        bot.send_message(call.message.chat.id, "You Exit Game")
        game_in_progress = False
        age_in_progress = False

# Handler for text messages
@bot.message_handler(func=lambda message: True)
def processor(message):
    global secret_number, game_in_progress, age_in_progress, textToSpeech_in_progress
    global maxFinder_in_progress , maxIndexFinder_in_progress , qrcodeMaker_in_progress

    if game_in_progress:
        try:
            markup2 = telebot.types.InlineKeyboardMarkup()
            button2 = telebot.types.InlineKeyboardButton(text="Exit Game" , callback_data="exit")
            markup2.add(button2)
            guess = int(message.text)
            if guess < secret_number:
                bot.reply_to(message, "Go higher!", reply_markup=markup2)
            elif guess > secret_number:
                bot.reply_to(message, "Go lower!", reply_markup=markup2)
            else:
                bot.reply_to(message, "Congratulations! You guessed it right!")
                # Offer a new game button
                markup1 = telebot.types.InlineKeyboardMarkup()
                button1 = telebot.types.InlineKeyboardButton(text='New Game', callback_data='new_game')
                markup1.add(button1)
                bot.send_message(message.chat.id, "Would you like to start a new game?", reply_markup=markup1)
                game_in_progress = False
            markup2 = telebot.types.InlineKeyboardMarkup()
            button2 = telebot.types.InlineKeyboardButton(text="Exit Game" , callback_data="exit")
            markup2.add(button2)
        except ValueError:
            bot.reply_to(message, "Please enter a valid number!")

    if age_in_progress:
        def is_valid_date(date_str):
            # Define the regular expression pattern for YYYY-MM-DD format
            pattern = r'^\d{4}-\d{2}-\d{2}$'
            
            # Use the match() function to search for the pattern in the input string
            if re.match(pattern, date_str):
                return True
            else:
                return False
        if (not is_valid_date(message.text)):
            bot.reply_to(message, "Wrong Format")
            markup2 = telebot.types.InlineKeyboardMarkup()
            button2 = telebot.types.InlineKeyboardButton(text="Exit Calculation" , callback_data="exit")
            markup2.add(button2)
        else:
            correctionCheck = True
            birthdate_str = message.text
            birthdate = JalaliDate.strptime(birthdate_str, '%Y-%m-%d')
            birthdate_jalali = JalaliDate(birthdate.year, birthdate.month, birthdate.day)
            
            # Get the current date
            current_date = JalaliDate.today()
            
            # Calculate the difference in years
            if current_date < birthdate_jalali:
                correctionCheck = False
            else:
                age = current_date.year - birthdate_jalali.year
            
            # Check if the birthday has already occurred this year
            if (current_date.month, current_date.day) < (birthdate_jalali.month, birthdate_jalali.day):
                age -= 1
            if correctionCheck:
                bot.reply_to(message, f"You are up to {age} years")
            else:
                bot.reply_to(message, "You are not born yet")
            age_in_progress = False
    
    if textToSpeech_in_progress:
        
        tts = gTTS(text=message.text, lang='en')  # You can specify the language here
        tts.save("message.mp3")
        
        # Send the voice message
        voice_message = open("message.mp3", 'rb')
        bot.send_voice(message.chat.id, voice_message)
        voice_message.close()
        
        # Remove the temporary audio file
        os.remove("message.mp3")
        textToSpeech_in_progress = False
    
    if maxFinder_in_progress:
        arr = (message.text).split(",")
        bot.reply_to(message , f"the maximum of inputs is {max(arr)}")
    if maxIndexFinder_in_progress:
        arr = (message.text).split(",")
        bot.reply_to(message , f"the maximum of inputs is {arr.index(max(arr))}")
    if qrcodeMaker_in_progress:
        txt = message.text
        img = qrcode.make(str(txt))
        img.save("txt.png")
        pic = open("txt.png" , "rb")
        bot.send_photo(message.chat.id , pic)
        pic.close()


    

# Start the bot
bot.infinity_polling()
