#!/usr/bin/env python3
import os
import subprocess
from pathlib import Path

WALLPAPER_DIR = Path("/home/vishesh/Pictures")


def sync_wallpapers():
    video_extensions = [".mp4", ".mkv", ".webm"]
    image_extensions = [".jpg", ".jpeg", ".png"]

    # 1. Check videos and create missing JPGs
    for video_ext in video_extensions:
        for video_file in WALLPAPER_DIR.glob(f"*{video_ext}"):
            jpg_file = video_file.with_suffix(".jpg")

            if not jpg_file.exists():
                print(f"Generating thumbnail for {video_file.name}...")
                subprocess.run(
                    [
                        "ffmpeg",
                        "-i",
                        str(video_file),
                        "-vframes",
                        "1",
                        "-q:v",
                        "2",
                        str(jpg_file),
                    ],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
                print(f"Created {jpg_file.name}")

    # 2. Check JPGs/PNGs and create standard, compliant MP4s
    for img_ext in image_extensions:
        for img_file in WALLPAPER_DIR.glob(f"*{img_ext}"):
            has_video = any(
                img_file.with_suffix(ext).exists() for ext in video_extensions
            )

            if not has_video:
                mp4_file = img_file.with_suffix(".mp4")
                print(f"Generating safe video loop for {img_file.name}...")
                subprocess.run(
                    [
                        "ffmpeg",
                        "-loop",
                        "1",
                        "-framerate",
                        "30",
                        "-i",
                        str(img_file),
                        "-c:v",
                        "libx264",
                        "-t",
                        "3",
                        "-pix_fmt",
                        "yuv420p",
                        "-vf",
                        "scale=trunc(iw/2)*2:trunc(ih/2)*2",
                        "-an",
                        str(mp4_file),
                    ],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
                print(f"Created {mp4_file.name}")


if __name__ == "__main__":
    sync_wallpapers()
