#!/usr/bin/env python3
import os
import subprocess

TMP_FILE = "/tmp/dms_current_wallpaper.txt"
WALLPAPER_DIR = "/home/vishesh/Pictures"


def main():
    if not os.path.exists(TMP_FILE):
        print("??1")
        return

    with open(TMP_FILE, "r") as f:
        raw_path = f.read().strip().strip("'").strip('"')

    if not raw_path:
        print("??2")
        return

    filename = os.path.basename(raw_path)
    base_name = os.path.splitext(filename)[0]

    video_path = None
    for ext in [".mp4", ".mkv", ".webm", ".jpg", ".png"]:
        potential_video = os.path.join(WALLPAPER_DIR, f"{base_name}{ext}")
        print(potential_video)
        if os.path.exists(potential_video):
            video_path = potential_video
            break
    print(video_path)
    if video_path:
        subprocess.run(["wayvid-ctl", "apply", video_path])
    else:
        print("here??")
        # subprocess.run(["pkill", "-f", "wayvid"], stderr=subprocess.DEVNULL)


if __name__ == "__main__":
    main()
