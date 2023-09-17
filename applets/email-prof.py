import time

def timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        print(f"Time remaining: {seconds} seconds")
        time.sleep(1)
        seconds -= 1
    print("Time is up!")

# Example usage
timer(5)