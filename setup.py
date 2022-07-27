# Programa de configuração para o cx_Freeze poder "Buildar"
import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"], "includes": ["tkinter"], "include_files": ["ico.ico"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Boot",
    version="1.0",
    description="Um robô que baixa toda base de dados da Agência Nacional",
    options={"build_exe": build_exe_options},
    executables=[Executable(script="Boot.py", base=base, icon="ico.ico")]
)

# Fim Config