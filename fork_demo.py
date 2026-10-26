"""T3: Python os.fork() demonstration. Linux/macOS only."""
import os
import time

pid = os.fork()

if pid == 0:
    print("Child Process", flush=True)
    print(f"Child PID: {os.getpid()}", flush=True)
    print(f"Parent PID: {os.getppid()}", flush=True)
    time.sleep(3)
    print("Child process finishing", flush=True)
    os._exit(0)
elif pid > 0:
    print("Parent Process", flush=True)
    print(f"Parent PID: {os.getpid()}", flush=True)
    print(f"Child PID: {pid}", flush=True)
    waited_pid, status = os.waitpid(pid, 0)
    print(f"Waited for child PID: {waited_pid}", flush=True)
    print(f"Child exit status: {os.waitstatus_to_exitcode(status)}", flush=True)
else:
    raise RuntimeError("Process creation failed")
