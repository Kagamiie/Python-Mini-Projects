from rich.console import Console
from rich.panel import Panel

NAME = "Torch"
VERSION_NAME = "1.3.0 [ Ruby / Aqua ]"

RESET = '\x1b[0m'
BOLD = '\x1b[1m\x1b'
GREEN = '\x1b[1;32m'
BLUE = '\033[0;34m'
RED = '\033[1m\033[91m'
REDS = '\033[0m'
CLS = "\033[2J\033[H"

WARNING = f"[{RED} ! {REDS}] {RED}WARNING{REDS}:"
SUCCESS = f"[{GREEN} + {RESET}]"
INTEROGATION = f"[{BLUE} ? {RESET}]"

def pheader():
    console = Console()
    console.print(
        Panel(
            f"{NAME}", 
            title="", 
            subtitle=f"{VERSION_NAME}",
            padding=(1, 10, 1, 10)
            ), 
        justify="center"
        )