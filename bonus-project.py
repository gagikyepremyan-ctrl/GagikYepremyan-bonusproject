import time
import sys

def start_timer(Hours, Mins, Secs):

    total_seconds = Hours * 3600 + Mins * 60 + Secs
    print(f"Timer started for {total_seconds} seconds...\n")
    
    while total_seconds >= 0:

        hours, remainder = divmod(total_seconds, 3600)
        mins, secs = divmod(remainder, 60)

        timer_display = f"{hours:02d}:{mins:02d}:{secs:02d}"

        print(f"\rTime Remaining: {timer_display}", end="")
        
       
        time.sleep(1)
        sys.stdout.flush()
        total_seconds -= 1
        if total_seconds < 0:
            break

    print("\n\nTime's up!")

if __name__ == "__main__":
    try:
        user_input = input("Insert time to count down (h:m:s) ")
        hours, minutes, seconds = map(int, user_input.split(":"))
        start_timer(hours, minutes, seconds)
    except ValueError:
        print("Invalid input! Please enter a whole number of seconds.")