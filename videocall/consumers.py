import json

from channels.generic.websocket import AsyncWebsocketConsumer


class VideoCallSignalConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super(VideoCallSignalConsumer, self).__init__(*args, **kwargs)

    async def connect(self):
        """
        join user to a general group and accept the connection
        """
        print('Signal connect')
        self.room_group_name = 'general_group'
        # join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, code):
        print('Signal disconnect')
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        """
        its called when UI websocket sends(). So its called only once
        irrespective of number of users in a group
        """
        print(' Signal receive')
        text_data_json = json.loads(text_data)

        # Send message to room group. its high level app-to-app communication
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                # func that will receive this data and send data to socket
                'type': 'signal_message',
                'data': text_data_json,
                'sender_channel_name': self.channel_name
            }
        )

    async def signal_message(self, event):
        """
        its not called directly from UI websocket. Its called from
        django receive() func.
        if 2 users (each user has a unique channel_name) in a group,
        this func will be called 2 times.
        """
        data = event['data']

        # Send message to all channels except parent channel
        if self.channel_name != event['sender_channel_name']:
            print('channel name != ')
            await self.send(text_data=json.dumps({
                'type': data['type'],
                'message': data['message']
            }))
