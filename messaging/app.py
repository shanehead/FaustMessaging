from datetime import datetime
import faust
from faust.web import Request, Response, View
import os

CONCURRENCY = int(os.environ.get('FAUST_CONCURRENCY', 50))

app = faust.App('messaging',
                autodiscover=True,
                origin='messaging')


def p(msg):
    msg = f'[{datetime.now()}] {msg}'
    print(msg)


@app.on_configured.connect
def configure(the_app, conf, **kwargs):
    p('Configure')
    conf.broker = os.environ.get('FAUST_BROKER')


@app.page('/status/')
class status(View):
    async def get(self, request: Request, **kwargs) -> Response:
        return self.json({'messages_active': app.monitor.messages_active,
                          'messages_s': app.monitor.messages_s,
                          'messages_received_total': app.monitor.messages_received_total})
