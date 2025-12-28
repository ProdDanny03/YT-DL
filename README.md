# YT Downloader

## Table Of Contents
- [YT Downloader](#yt-downloader)
  - [Table Of Contents](#table-of-contents)
  - [About](#about)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)

## About

This is a simple audio/video downloader for (but not limited to) youtube

## Features

- Format selection
- Link parsing (separates video/audio from playlists)
- Downloads to Video/Music folder automatically

## Installation

Download from releases section or build the binary yourself:
(Microsoft Visual Studio MSVC is required to build)
```bash
git clone https://github.com/ProdDanny03/YT-DL.git

cd project-name

pip install -r requirements.txt

nuitka --msvc=latest --onefile --enable-plugin=pyside6 --nofollow-import-to=yt_dlp.extractor.lazy_extractors --windows-console-mode=disable --windows-icon-from-ico=icon.ico --remove-output --output-filename="YT-DL.exe" main.py
```

## Usage

put url of website containing video/audio in url search box, select format in top left and click download, its that easy