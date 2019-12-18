import faust

from messaging.app import app, p, CONCURRENCY
from messaging.api.agents import EventApi, event_api


class Message(faust.Record):
    event: dict
    data: dict


message_topic = app.topic('message', value_type=Message)


@app.agent(message_topic, use_reply_headers=True, concurrency=CONCURRENCY)
async def message(stream):
    count = 0
    async for data in stream:
        count += 1
        p(f'[message]({count}) Received: data={data}')
        data.event.update(data.data)
        payload = {'url': 'http://example.com',
                   'json_data': data}
        await event_api.send(value=EventApi(data=payload))
