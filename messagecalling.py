import logger
import os
import time
import uuid
from db import channels, users
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from logger import Logger

def on_new_message(ws=None, message_data=None, server_data=None):
    try:
        if message_data is None:
            return
        content = message_data.get('content', '').strip()
        channel = message_data.get('channel')
        if not content or not channel:
            return

        print(f"[{channel}] {message_data.get('user', 'Unknown')}: {content}")
        return content.lower() 
    except Exception as e:
        logger.error(f"ExamplePlugin on_new_message error: {e}")

def send_message_to_channel(user, channel, content, server_data):
    """Send a message to a channel through the server's broadcast system"""
    import asyncio
    
    # Create a message object similar to how regular messages are created
    out_msg = {
        "user": user,
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