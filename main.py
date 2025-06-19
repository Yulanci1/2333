# main.py

import threading
from bot import run_bot
from scheduler import run_scheduler

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    threading.Thread(target=run_scheduler).start()