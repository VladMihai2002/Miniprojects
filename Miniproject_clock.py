# The provided Python program creates a simple digital clock that displays the current time in the format HH:MM:SS. Here’s how it works:
#
# The program runs an infinite loop using while True.
# Inside the loop:
# It gets the current local time using time.localtime().
# Extracts the hour, minute, and second components.
# Formats each component with leading zeros if it’s less than 10.
# Constructs the clock display in the format HH:MM:SS.
# Prints the clock display.
# Waits for 1 second using time.sleep(1) before updating the display for the next second.

import time

def display_clock():
    while True:
        # Get the current local time
        current_time = time.localtime()
        hour = current_time.tm_hour % 24
        minute = current_time.tm_min
        second = current_time.tm_sec

        # Format hours, minutes, and seconds with leading zeros if less than 10
        formatted_hour = f"{hour:02}"
        formatted_minute = f"{minute:02}"
        formatted_second = f"{second:02}"

        # Construct the clock display
        clock_text = f"{formatted_hour}:{formatted_minute}:{formatted_second}"

        # Print the clock
        print(clock_text)

        # Wait for 1 second
        time.sleep(1)

if __name__ == "__main__":
    display_clock()