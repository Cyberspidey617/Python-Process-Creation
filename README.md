# T3: Python Process Creation — `os.fork()` and `subprocess`

## Aim
To demonstrate process creation in Python, display process IDs, and wait for a child process to finish. Use `os.fork()` on supported Unix-like systems and `subprocess.Popen()` on Windows.

## Files
- `fork_demo.py` — Uses `os.fork()` and `os.waitpid()` on Linux/macOS.
- `subprocess_demo.py` — Uses `subprocess.Popen()` on Windows, Linux, or macOS.

## Tools and versions
| Tool | Version | Platform |
|---|---|---|
| Python | 3.8 or later; record the actual version | Linux/macOS/Windows 10 or 11 |
| `os` and `subprocess` | Python standard library | Platform support differs for `os.fork()` |

Check the installed version with `python3 --version` or `py --version`.

## Run on Linux/macOS: os.fork()
```bash
python3 fork_demo.py
```
While the child is sleeping, inspect processes in another terminal:
```bash
ps -o pid,ppid,stat,comm -ax | grep '[p]ython'
```
**Note:** `os.fork()` is not supported on native Windows.

## Run on Windows: subprocess
In PowerShell:
```powershell
py subprocess_demo.py
```
Alternatively:
```powershell
python subprocess_demo.py
```
The portable subprocess example also runs on Linux/macOS:
```bash
python3 subprocess_demo.py
```

## Illustrative sample output
PIDs and message order may vary. These are examples, not verified execution results.

`fork_demo.py`:
```text
Parent Process
Parent PID: 5200
Child PID: 5201
Child Process
Child PID: 5201
Parent PID: 5200
Child process finishing
Waited for child PID: 5201
Child exit status: 0
```

`subprocess_demo.py`:
```text
Parent Process
Parent PID: 6200
Child PID: 6312
Child Process
Child PID: 6312
Parent PID: 6200
Child process finishing
Child exit status: 0
```

## Result
Process creation was demonstrated using `os.fork()` on supported Unix-like systems and `subprocess.Popen()` on Windows and other supported platforms. Process IDs and exit status were used to observe process relationships and completion.

## Comparison
| Feature | `os.fork()` | `subprocess.Popen()` |
|---|---|---|
| Purpose | Creates a child from the current process | Starts a specified process |
| Windows support | No | Yes |
| Wait mechanism | `os.waitpid()` | `Popen.wait()` |

## Screenshots
Insert genuine screenshots of execution. Each screenshot must show roll number 3 in the terminal prompt, user name, or window title as required by the lab instructions.
- Figure T3-1: `os.fork()` execution on Linux/macOS.
- Figure T3-2: `subprocess_demo.py` execution on Windows.
- Figure T3-3: Process list while the child is running.

## Viva questions
1. **What is `os.fork()`?** It creates a child process on supported Unix-like systems.
2. **What does `fork()` return?** Zero in the child and the child PID in the parent.
3. **Why is `os.fork()` unavailable on Windows?** Native Windows does not provide the POSIX `fork()` interface.
4. **What does `subprocess.Popen()` do?** It starts another process and returns an object to manage it.
5. **How do you wait for a child?** Use `os.waitpid()` or `Popen.wait()`, depending on the method.

## Common errors
| Message / symptom | Cause | Fix |
|---|---|---|
| `os` has no attribute `fork` | Running on Windows or unsupported platform | Run `fork_demo.py` on Linux/macOS; use `subprocess_demo.py` on Windows. |
| `python3` not found | Interpreter command differs or Python is not on PATH | Try `py` on Windows or use the configured interpreter. |
| Output order varies | Processes run concurrently | Do not assume a fixed order. |
| Child missing from process list | Child already finished | Inspect while the script is sleeping. |

## References
- Python documentation: `os` and `subprocess` modules.

## AI assistance declaration
AI assistance was used to organize and explain the experiment. Test the code, verify actual outputs, and capture your own screenshots before submission.
