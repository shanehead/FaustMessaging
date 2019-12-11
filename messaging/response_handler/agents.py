import faust
from messaging.app import app, p


class ApiResponse(faust.Record):
    response_code: str


response_handler_topic = app.topic('response_handler', value_type=ApiResponse)


@app.agent(response_handler_topic)
async def api_response(stream):
    async for response in stream:
        p(f'Received: {response}')
