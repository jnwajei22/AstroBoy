import datetime
import time
import winsound
import subprocess
import threading

# Global variable to indicate whether the alarm should continue
alarm_running = True

def set_alarm(alarm_time):
    alarm_hour, alarm_minute = map(int, alarm_time.split(':'))
    while True:
        now = datetime.datetime.now()
        if now.hour == alarm_hour and now.minute == alarm_minute:
            alarm_sound_thread = threading.Thread(target=play_alarm_sound)
            alarm_sound_thread.start()
            threading.Thread(target=stop_alarm).start()  # Start listening for Enter key press
            display_alarm_message()
            alarm_sound_thread.join()  # Wait for the alarm sound thread to finish
            break
        time.sleep(20)  # Check every 20 seconds

def play_alarm_sound():
    # Play system default sound for the alarm repeatedly until interrupted
    while alarm_running:
        winsound.PlaySound("*", winsound.SND_ALIAS)

def display_alarm_message():
    # Run a separate Python script to display the alarm message in a new command prompt window
    subprocess.Popen(["cmd.exe", "/c", "python", "alarm_message.py"])

def stop_alarm():
    global alarm_running
    input("Press Enter to stop the alarm.")
    alarm_running = False
    # Stop the alarm sound
    winsound.PlaySound(None, winsound.SND_PURGE)

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM): ")
    set_alarm(alarm_time)
