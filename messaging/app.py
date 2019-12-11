import faust
from datetime import datetime

app = faust.App('messaging',
                broker='kafka://localhost',
                autodiscover=True,
                origin='messaging')


def p(msg):
    print(f'[{datetime.now()}] {msg}')


def main() -> None:
    app.main()
