import os
import subprocess
from pathlib import Path


HOME = Path.home()


# ---------- Helper ---------- #

def _open_path(path: Path, name: str):

    try:

        if path.exists():

            os.startfile(path)

            return f"Opening {name}."

        return f"{name} folder not found."

    except Exception as e:

        return f"Unable to open {name}. ({e})"


# ---------- User Folders ---------- #

def open_desktop():

    return _open_path(
        HOME / "Desktop",
        "Desktop"
    )


def open_documents():

    return _open_path(
        HOME / "Documents",
        "Documents"
    )


def open_downloads():

    return _open_path(
        HOME / "Downloads",
        "Downloads"
    )


def open_pictures():

    return _open_path(
        HOME / "Pictures",
        "Pictures"
    )


def open_music():

    return _open_path(
        HOME / "Music",
        "Music"
    )


def open_videos():

    return _open_path(
        HOME / "Videos",
        "Videos"
    )


# ---------- Drives ---------- #

def open_c_drive():

    return _open_path(
        Path("C:/"),
        "C Drive"
    )


def open_d_drive():

    return _open_path(
        Path("D:/"),
        "D Drive"
    )


# ---------- Explorer ---------- #

def open_this_pc():

    try:

        subprocess.Popen("explorer shell:MyComputerFolder")

        return "Opening This PC."

    except Exception as e:

        return f"Unable to open This PC. ({e})"


# ---------- Recycle Bin ---------- #

def open_recycle_bin():

    try:

        subprocess.Popen(
            "explorer shell:RecycleBinFolder"
        )

        return "Opening Recycle Bin."

    except Exception as e:

        return f"Unable to open Recycle Bin. ({e})"


# ---------- Temp Folder ---------- #

def open_temp():

    return _open_path(
        Path(os.environ["TEMP"]),
        "Temporary Files"
    )


# ---------- Startup Folder ---------- #

def open_startup():

    startup = Path(
        os.getenv("APPDATA")
    ) / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "Startup"

    return _open_path(
        startup,
        "Startup Folder"
    )


# ---------- Recent Files ---------- #

def open_recent():

    recent = Path(
        os.getenv("APPDATA")
    ) / "Microsoft" / "Windows" / "Recent"

    return _open_path(
        recent,
        "Recent Files"
    )