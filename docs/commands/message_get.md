# Command: message_get

**Request:**
```json
{
  "cmd": "message_get",
  "channel": "<channel_name>",
  "id": "<message_id>"
}
```

- `channel`: Channel name.
- `id`: Message ID.

**Response:**
- On success:
```json
{
  "cmd": "message_get",
  "channel": "<channel_name>",
  "message": { ...message object... }
}
```
The message object also contains "position" which tells you where in the channel the message is
- On error: see [common errors](errors.md).

**Notes:**
- User must be authenticated and have access to the channel.

See implementation: [`handlers/message.py`](../handlers/message.py) (search for `case "message_get":`).
