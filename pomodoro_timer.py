import time

def pomodoro_timer():
    print("Welcome to the Pomodoro Timer!")
    custom = input("Would you like to customize the timer? (yes/no): ").strip().lower()
    
    if custom in ["yes", "y"]:
        try:
            work_duration = int(input("Enter work duration in minutes: "))
            break_duration = int(input("Enter break duration in minutes: "))
            cycles = int(input("Enter number of cycles: "))
        except ValueError:
            print("Invalid input. Using default settings.")
            work_duration, break_duration, cycles = 25, 5, 4
    else:
        work_duration, break_duration, cycles = 25, 5, 4
    
    print(f"Timer set to {work_duration} minutes work, {break_duration} minutes break, {cycles} cycles.")
    
    for i in range(1, cycles + 1):
        print(f"\nCycle {i}: Work session starts.")
        countdown(work_duration)
        print("Work session complete.")
        
        if i < cycles:
            print("Break time.")
            countdown(break_duration)
            print("Break over.")
    
    print("\nAll cycles complete. Well done!")

def countdown(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        print(f"{mins:02}:{secs:02}", end="\r", flush=True)
        time.sleep(1)
        seconds -= 1
    print("00:00", flush=True)

if __name__ == "__main__":
    pomodoro_timer()
