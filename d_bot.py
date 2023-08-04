import telebot
import random

bot = telebot.TeleBot("API_KEY", parse_mode=None)

# Load messages from the file, if it exists
try:
    with open('messages.txt', 'r') as f:
        messages = [line.strip() for line in f]
except FileNotFoundError:
    messages = []

# Load sent messages from the file, if it exists
try:
    with open('sent_messages.txt', 'r') as f:
        sent_messages = [line.strip() for line in f]
except FileNotFoundError:
    sent_messages = []

@bot.message_handler(commands=['denerbot'])
def send_random_message(message):
    if len(sent_messages) == len(messages):
        sent_messages.clear()
        with open('sent_messages.txt', 'w') as f:
            f.write('')  # Clear the contents of the sent_messages.txt file# Clear the list of sent messages
    remaining_messages = list(set(messages) - set(sent_messages))
    random_message = random.choice(remaining_messages)
    sent_messages.append(random_message)
    bot.reply_to(message, random_message)
    # Save the updated sent_messages list to a file
    with open('sent_messages.txt', 'w') as f:
        f.write('\n'.join(sent_messages))
        print(sent_messages)

@bot.message_handler(commands=['denerbot_add'])
def add_message(message):
    # Check if the message is a reply to another message
    if message.reply_to_message:
        # Get the username of the original message's sender
        original_sender_username = message.reply_to_message.from_user.username
        print(original_sender_username)
        # Check if the original message's sender is 'denersmiranda'
        if original_sender_username == 'denersmiranda':
            # Add the text of the replied message to the list
            messages.append(message.reply_to_message.text)
            print(message.reply_to_message.text)
            # Write the new message to the file
            with open('messages.txt', 'a') as f:
                f.write(message.reply_to_message.text + '\n')
            bot.reply_to(message, "Frase adicionada rs")
        else:
            bot.reply_to(
                message, "Responda à minha mensagem com o comando /denerbot_add para adicionar uma nova frase. Voce nao estudou, amigo? rs")
    else:
        bot.reply_to(
            message, "Responda à minha mensagem com o comando /denerbot_add para adicionar uma nova frase. Voce nao estudou, amigo? rs")

bot.infinity_polling()
