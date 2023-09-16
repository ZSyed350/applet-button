
import time

seconds = 0

while True:
    try:
        seconds = int(input("Enter the number of seconds to run for: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number of seconds.")

start_time = time.time()
end_time = start_time + seconds

while time.time() < end_time:
    pass

print("Timer finished!")
