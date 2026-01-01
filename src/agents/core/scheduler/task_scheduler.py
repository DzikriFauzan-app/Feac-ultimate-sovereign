import threading
import queue
import time

class TaskScheduler:
    def __init__(self, message_bus):
        self.message_bus = message_bus
        self.tasks = queue.Queue()
        self.running = False
        self.worker_thread = threading.Thread(target=self._worker_loop, daemon=True)

    def start(self):
        self.running = True
        self.worker_thread.start()

    def stop(self):
        self.running = False

    def add_task(self, agent_name, command, params):
        self.tasks.put((agent_name, command, params))

    def _worker_loop(self):
        while self.running:
            try:
                agent_name, command, params = self.tasks.get(timeout=0.2)
                self.message_bus.emit("task", {
                    "agent": agent_name,
                    "command": command,
                    "params": params
                })
            except queue.Empty:
                pass
            except Exception as e:
                print("[TaskScheduler ERROR]", e)

            time.sleep(0.01)
