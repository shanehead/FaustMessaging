import faust

from messaging.app import app, p
from messaging.api.agents import EventApi, event_api


class Message(faust.Record):
    event: dict
    data: dict


message_topic = app.topic('message', value_type=Message)


@app.agent(message_topic)
async def message(stream):
    async for data in stream:
        p(f'Received: data={data}')
        data.event.update(data.data)
        payload = {'url': 'http://example.com',
                   'json_data': data}
        await event_api.send(value=EventApi(data=payload))
