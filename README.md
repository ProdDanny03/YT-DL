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
| Features          | Description                                                 |
| :---------------- | :---------------------------------------------------------- |
| Format Selection  | Select format to download file in                           |
| Link Parsing      | Automatically separates video/audio from possible playlists |
| Download Location | Automatically downloads videos/audio to Videos/Music        |

## Installation

Download from releases section or build the binary yourself:
> *Microsoft Visual Studio MSVC and python3.13 is required to build*

```bash
git clone https://github.com/ProdDanny03/YT-DL.git

cd YT-DL

pip install -r requirements.txt

nuitka --msvc=latest --onefile --enable-plugin=pyside6 --nofollow-import-to=yt_dlp.extractor.lazy_extractors --windows-console-mode=disable --windows-icon-from-ico=icon.ico --remove-output --output-filename="YT-DL.exe" main.py
```

## Usage

put url of website containing video/audio in url search box, select format in top left and click download, its that easy