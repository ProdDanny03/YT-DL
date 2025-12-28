from pathlib import Path
from typing import Any

from yt_dlp import YoutubeDL

AUDIO_ONLY_FORMATS = ["wav", "mp3", "m4a", "flac", "alac", "ogg"]
VIDEO_FORMATS = ["mp4", "mov", "avi", "flv"]


def download_url(url: str, output_format: str):
    if "&list=" in url:
        url = url.split("&list=")[0]

    if output_format in AUDIO_ONLY_FORMATS:
        downloads_path = Path.home() / "Music"
    elif output_format in VIDEO_FORMATS:
        downloads_path = Path.home() / "Videos"
    else:
        downloads_path = Path.home() / "Desktop"

    # ── Decide download strategy
    if output_format in AUDIO_ONLY_FORMATS:
        ydl_format = "bestaudio/best"
        postprocessors = [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": output_format,
            }
        ]

    elif output_format in VIDEO_FORMATS:
        ydl_format = "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4"
        postprocessors = []

    else:
        print(f"Unknown format '{output_format}', defaulting to wav")
        ydl_format = "bestaudio/best"
        postprocessors = [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "wav",
            }
        ]

    # ── yt-dlp options
    ydl_opts: Any = {
        "format": ydl_format,
        "outtmpl": str(downloads_path / "%(title)s.%(ext)s"),
        "noplaylists": True,
    }

    if postprocessors:
        ydl_opts["postprocessors"] = postprocessors

    # ── Download
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
