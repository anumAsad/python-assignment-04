import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)  # Convert seconds into MM:SS format
        timer_display = f"{mins:02d}:{secs:02d}"
        print(f"⏳ Time left: {timer_display}", end="\r")  # Overwrites the same line
        time.sleep(1)  # Pause for 1 second
        seconds -= 1

    print("\n🎉 Time's up!")

if __name__ == "__main__":
    seconds = int(input("Enter the countdown time in seconds: "))
    countdown_timer(seconds)
