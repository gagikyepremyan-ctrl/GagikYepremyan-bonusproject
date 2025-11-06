import sys
import time
from typing import Optional


def parse_duration(s: str) -> Optional[int]:
    """Parse duration strings into total seconds.

    Accepts:
      - SS (e.g. "10")
      - MM:SS (e.g. "2:30")
      - HH:MM:SS (e.g. "1:02:03")

    Returns total seconds or None on parse error.
    """
    parts = s.split(":")
    try:
        if len(parts) == 1:
            # seconds
            return int(parts[0])
        elif len(parts) == 2:
            minutes, seconds = parts
            return int(minutes) * 60 + int(seconds)
        elif len(parts) == 3:
            hours, minutes, seconds = parts
            return int(hours) * 3600 + int(minutes) * 60 + int(seconds)
    except ValueError:
        return None
    return None


def fmt_seconds(total: int) -> str:
    """Format seconds into H:MM:SS or M:SS depending on size."""
    if total < 0:
        total = 0
    hours = total // 3600
    minutes = (total % 3600) // 60
    seconds = total % 60
    if hours:
        return f"{hours}:{minutes:02d}:{seconds:02d}"
    else:
        return f"{minutes}:{seconds:02d}"


def countdown(total_seconds: int) -> None:
    """Run countdown in the terminal, printing one line per second.

    Important: first printed remaining time appears after one second.
    """
    if total_seconds <= 0:
        print("0:00")
        return


    remaining = total_seconds
    try:
        while remaining > 0:
            time.sleep(1)
            remaining -= 1
            print(fmt_seconds(remaining), end='\r')
    except KeyboardInterrupt:
        print("\nTimer canceled by user.")


def main(argv: Optional[list] = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    if not argv:
        print("Usage: python timer.py <duration>\nExample durations: 10, 2:30, 1:00:00")
        return 1

    dur = parse_duration(argv[0])
    if dur is None:
        print(f"Invalid duration: {argv[0]}")
        return 2

    print(f"Starting timer for {fmt_seconds(dur)}. Press Ctrl-C to cancel.")
    countdown(dur)
    print("Time's up!")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

   
