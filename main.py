import tkinter as tk
import time
import datetime
from tkinter import messagebox

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock by Jaswanth")
        self.root.geometry("400x250")
        self.root.configure(bg="#222831")
        self.time_format_24hr = True

        # Clock label
        self.clock_label = tk.Label(root, font=("Arial", 40), bg="#393e46", fg="#fafafa")
        self.clock_label.pack(pady=10)

        # Date label
        self.date_label = tk.Label(root, font=("Arial", 18), bg="#393e46", fg="#00adb5")
        self.date_label.pack(pady=5)
        
        # Alarm Widgets
        self.alarm_frame = tk.Frame(root, bg="#222831")
        self.alarm_frame.pack(pady=10)
        tk.Label(self.alarm_frame, text="Set Alarm (HH:MM:SS):", bg="#222831", fg="#eeeeee", font=("Arial", 10)).pack(side='left')
        self.alarm_entry = tk.Entry(self.alarm_frame, width=10, font=("Arial", 12))
        self.alarm_entry.pack(side='left', padx=5)
        self.set_alarm_btn = tk.Button(self.alarm_frame, text="Set", command=self.set_alarm, bg="#00adb5", fg="#eeeeee")
        self.set_alarm_btn.pack(side='left')

        self.toggle_btn = tk.Button(root, text="Switch to 12-hour", command=self.toggle_format, bg="#00adb5", fg="#eeeeee")
        self.toggle_btn.pack(pady=8)

        self.alarm_time = ""

        self.update_clock()

    def update_clock(self):
        now = time.localtime()
        if self.time_format_24hr:
            hour = time.strftime("%H:%M:%S", now)
        else:
            hour = time.strftime("%I:%M:%S %p", now)
        date = time.strftime("%A, %B %d, %Y", now)

        self.clock_label.config(text=hour)
        self.date_label.config(text=date)

        # Check alarm
        if self.alarm_time:
            curr_time = time.strftime("%H:%M:%S", now)
            if curr_time == self.alarm_time:
                messagebox.showinfo("Alarm", "Time's up!")
                self.alarm_time = ""  # Reset alarm

        self.root.after(1000, self.update_clock)

    def toggle_format(self):
        self.time_format_24hr = not self.time_format_24hr
        text = "Switch to 24-hour" if not self.time_format_24hr else "Switch to 12-hour"
        self.toggle_btn.config(text=text)

    def set_alarm(self):
        alarm_val = self.alarm_entry.get()
        try:
            time.strptime(alarm_val, "%H:%M:%S")
            self.alarm_time = alarm_val
            messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_val}")
        except ValueError:
            messagebox.showerror("Invalid Time", "Please enter time as HH:MM:SS (24-hour format).")

if __name__ == "__main__":
    root = tk.Tk()
    app = DigitalClock(root)
    root.mainloop()
