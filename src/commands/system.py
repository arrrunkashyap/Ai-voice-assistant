import ctypes
import os
import shutil
import subprocess

import psutil


# ---------- Lock Computer ---------- #

def lock_pc():

    try:

        ctypes.windll.user32.LockWorkStation()

        return "Locking your computer."

    except Exception as e:

        return f"Unable to lock computer. ({e})"


# ---------- Shutdown ---------- #

def shutdown(delay: int = 5):

    try:

        os.system(f"shutdown /s /t {delay}")

        return f"Shutting down in {delay} seconds."

    except Exception as e:

        return f"Shutdown failed. ({e})"


# ---------- Restart ---------- #

def restart(delay: int = 5):

    try:

        os.system(f"shutdown /r /t {delay}")

        return f"Restarting in {delay} seconds."

    except Exception as e:

        return f"Restart failed. ({e})"


# ---------- Logout ---------- #

def logout():

    try:

        os.system("shutdown /l")

        return "Logging out."

    except Exception as e:

        return f"Logout failed. ({e})"


# ---------- Cancel Shutdown ---------- #

def cancel_shutdown():

    try:

        os.system("shutdown /a")

        return "Shutdown cancelled."

    except Exception as e:

        return f"Unable to cancel shutdown. ({e})"


# ---------- Sleep ---------- #

def sleep():

    try:

        os.system(
            "rundll32.exe powrprof.dll,SetSuspendState 0,1,0"
        )

        return "Putting computer to sleep."

    except Exception as e:

        return f"Sleep failed. ({e})"


# ---------- Hibernate ---------- #

def hibernate():

    try:

        os.system("shutdown /h")

        return "Hibernating computer."

    except Exception as e:

        return f"Hibernate failed. ({e})"


# ---------- Empty Recycle Bin ---------- #

def empty_recycle_bin():

    try:

        subprocess.run(
            [
                "powershell",
                "-Command",
                "Clear-RecycleBin -Force"
            ],
            check=True,
            capture_output=True
        )

        return "Recycle Bin emptied."

    except Exception as e:

        return f"Unable to empty Recycle Bin. ({e})"


# ---------- CPU Usage ---------- #

def cpu_usage():

    return f"CPU usage is {psutil.cpu_percent(interval=1)} percent."


# ---------- RAM Usage ---------- #

def ram_usage():

    ram = psutil.virtual_memory()

    return (
        f"RAM usage is {ram.percent} percent. "
        f"{round(ram.used / (1024**3),2)} GB used of "
        f"{round(ram.total / (1024**3),2)} GB."
    )


# ---------- Disk Usage ---------- #

def disk_usage():

    disk = shutil.disk_usage("C:\\")

    used = round(disk.used / (1024**3), 2)

    total = round(disk.total / (1024**3), 2)

    percent = round((disk.used / disk.total) * 100, 1)

    return (
        f"Disk usage is {percent} percent. "
        f"{used} GB used of {total} GB."
    )


# ---------- System Uptime ---------- #

def uptime():

    boot = psutil.boot_time()

    from datetime import datetime

    boot_time = datetime.fromtimestamp(boot)

    return (
        f"System started at "
        f"{boot_time.strftime('%I:%M %p on %d %B %Y')}."
    )


# ---------- Battery ---------- #

def battery_status():

    battery = psutil.sensors_battery()

    if battery is None:

        return "Battery information is unavailable."

    status = "charging" if battery.power_plugged else "not charging"

    return (
        f"Battery is {battery.percent}% "
        f"and is currently {status}."
    )