from logger import Logger
import plugin_manager
Logger.distinct("Example Plugin loaded successfully!")
import os
import json
import time
import uuid
from db import channels, users
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from logger import Logger

def setup():
    """Called when the plugin is loaded"""
    # Access plugin_manager and listen for events
    plugin_manager.register_event_listener("new_message", handle_new_message)

def handle_new_message(ws, message_data, server_data):
    """Handle new messages from the server"""
    content = message_data.get("content")
    channel = message_data.get("channel")
    username = message_data.get("username")
    
    if content == "!helloworld":
        send_message_to_channel(channel, "Hello, World!", None)

    Logger.distinct(f"[{channel}] {username}: {content}")

def send_message_to_channel(channel, content, server_data):
    """Send a message to a channel through the server's broadcast system"""
    import asyncio
    
    # Create a message object similar to how regular messages are created
    out_msg = {
        "user": "OriginChats",
        "content": content.strip(),
        "timestamp": time.time(),
        "type": "message",
        "pinned": False,
        "id": str(uuid.uuid4())
    }
    
    # Save to channel
    channels.save_channel_message(channel, out_msg)
    
    # Broadcast the message if we have server data
    if server_data and "connected_clients" in server_data:
        message = {"cmd": "message_new", "message": out_msg, "channel": channel, "global": True}
        # Schedule this to run in the event loop
        from handlers.websocket_utils import broadcast_to_all
        try:
            loop = asyncio.get_event_loop()
            loop.create_task(broadcast_to_all(server_data["connected_clients"], message))
        except Exception as e:
            Logger.error(f"Welcome Plugin: Error broadcasting message: {e}")

# ---------------------------------------------------------------------------------------------------------------- #
setup()
send_message_to_channel("general", "Example Plugin has been loaded!", None)

