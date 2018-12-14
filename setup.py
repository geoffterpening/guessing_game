import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"includes":[],"packages": ["os"], "include_files":['prize_easy.txt', 'prize_medium.txt', 'prize_hard.txt']}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Console"

setup(  name = "guessing_game",
        version = "0.1",
        description = "A guessing game!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("app.py", base=base)])