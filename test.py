from pathlib import Path
import platform
import socket
import sys
from datetime import datetime


def main() -> None:
    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)

    report = {
        "message": "Hello from Windows compute node",
        "time": datetime.now().isoformat(timespec="seconds"),
        "hostname": socket.gethostname(),
        "python": sys.version,
        "platform": platform.platform(),
        "cwd": str(Path.cwd()),
    }

    text = "\n".join(f"{key}: {value}" for key, value in report.items()) + "\n"
    print(text)
    (results_dir / "result.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
