import faust
from messaging.app import app, p, CONCURRENCY


class ApiResponse(faust.Record):
    response_code: str


response_handler_topic = app.topic('response_handler', value_type=ApiResponse)


@app.agent(response_handler_topic, use_reply_headers=True, concurrency=CONCURRENCY)
async def api_response(stream):
    count = 0
    async for response in stream:
        count += 1
        p(f'[api_response]({count}) Received: {response}')
