# Running the Bot 

This README provides step-by-step instructions for running the Python telegram bot script. 

## Prerequisites
Before running the script, you will need:

- Python installed on your system. If you don't have Python installed, you can download it from the [official Python website](https://www.python.org/downloads/).
- The `telebot` module. This can be installed using pip:
  
        pip install pyTelegramBotAPI


## Running the Script

1. **Clone the repository**: First, clone the GitHub repository containing the Python script to your local machine.

2. **Set up the API key**: Replace `"API_KEY"` in the line `bot = telebot.TeleBot("API_KEY", parse_mode=None)` the actual Telegram Bot API key.

3. **Run the script**: To run the script, open up a terminal, navigate to the directory containing the script, and enter the following command:

        python d_bot.py
   

## Usage

Once the bot is running, you can interact with it using the following commands:

- `/denerbot`: The bot will send a random message from the `messages.txt` file. If all messages from the file have been sent, it will start over.

- `/denerbot_add`: If you reply to a message from the user 'denersmiranda' with this command, the bot will add the text of the replied message to the `messages.txt` file.

## Troubleshooting

If you encounter any issues while running the script, make sure that:

- You've replaced `"API_KEY"` with your actual Telegram Bot API key.
- Your Python environment has the `telebot` module installed.
- The `messages.txt` and `sent_messages.txt` files exist in the same directory as the script. If they don't, the script will create them.

