faust -A messaging.app worker -l info &
sleep 5
PYTHONPATH=. python messaging/msg_gen/generate.py
