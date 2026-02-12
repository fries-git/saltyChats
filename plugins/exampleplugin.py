from logger import Logger
import os
import random
from db import channels, users
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from messagecalling import on_new_message, send_message_to_channel

Logger.success("Example Plugin loaded successfully!")
send_message_to_channel("SaltyChats", "general", "Example Plugin has been loaded!", None)

def getInfo():
    return {
        "name": "Example Plugin",
        "description": "Simple example plugin that responds to ?hello",
        "version": "1.0.0",
        "author": "Server",
        "handles": ["new_message"]
    }

def on_new_message(ws, message_data, server_data=None):
    content = message_data.get('content', '').strip().lower()
    if content == "?rtd":
        roll = random.randint(1, 10)
        send_message_to_channel("fries", message_data.get('channel'), f"You rolled a {roll} on a 10-sided die!", server_data)