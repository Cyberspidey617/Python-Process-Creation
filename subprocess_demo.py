"""T3: Portable Python subprocess demonstration."""
import os
import subprocess
import sys

child_code = (
    "import os, time; "
    "print('Child Process', flush=True); "
    "print(f'Child PID: {os.getpid()}', flush=True); "
    "print(f'Parent PID: {os.getppid()}', flush=True); "
    "time.sleep(3); "
    "print('Child process finishing', flush=True)"
)

print("Parent Process", flush=True)
print(f"Parent PID: {os.getpid()}", flush=True)
child = subprocess.Popen([sys.executable, "-c", child_code])
print(f"Child PID: {child.pid}", flush=True)
print(f"Child exit status: {child.wait()}", flush=True)
