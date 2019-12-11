import asyncio
from messaging.app import p
from messaging.msg_worker.agents import Message, message

event = {'event_id': 1, 'type': 'MESG'}
data = {'auth_id': 5, 'amount': 5.00}

msg = Message(event=event, data=data)


async def send() -> None:
    p('Sending')
    await message.send(value=msg)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send())
