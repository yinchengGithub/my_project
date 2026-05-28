from pathlib import Path
import platform
import socket
import sys
from datetime import datetime


def build_svg() -> str:
    return """<svg xmlns="http://www.w3.org/2000/svg" width="640" height="420" viewBox="0 0 640 420">
  <rect width="640" height="420" fill="#f6f7fb"/>
  <circle cx="320" cy="190" r="110" fill="#4f8cff" opacity="0.9"/>
  <rect x="220" y="120" width="200" height="140" rx="18" fill="#ffffff" opacity="0.92"/>
  <path d="M230 285 C275 230, 365 340, 430 255" fill="none" stroke="#ff6b35" stroke-width="18" stroke-linecap="round"/>
  <circle cx="265" cy="175" r="18" fill="#1f2937"/>
  <circle cx="375" cy="175" r="18" fill="#1f2937"/>
  <text x="320" y="355" text-anchor="middle" font-family="Arial, sans-serif" font-size="28" fill="#111827">
    drawn on Windows by Python
  </text>
</svg>
"""


def main() -> None:
    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)

    svg_path = results_dir / "shape.svg"
    svg_path.write_text(build_svg(), encoding="utf-8")

    report = {
        "message": "Created an SVG drawing on Windows",
        "time": datetime.now().isoformat(timespec="seconds"),
        "hostname": socket.gethostname(),
        "python": sys.version,
        "platform": platform.platform(),
        "cwd": str(Path.cwd()),
        "image": str(svg_path),
    }

    text = "\n".join(f"{key}: {value}" for key, value in report.items()) + "\n"
    print(text)
    (results_dir / "result.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
