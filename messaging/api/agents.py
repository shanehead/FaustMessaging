from asyncio import sleep
import faust

from messaging.app import app, p, CONCURRENCY
from messaging.response_handler.agents import ApiResponse, api_response


class EventApi(faust.Record):
    data: dict


event_api_topic = app.topic('event_api', value_type=EventApi)


@app.agent(event_api_topic, use_reply_headers=True, concurrency=CONCURRENCY)
async def event_api(stream):
    async for data in stream:
        p(f'[event_api] Received: data={data}')
        await sleep(0.25)
        await api_response.send(value=ApiResponse(response_code='00'))
