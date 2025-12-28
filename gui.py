import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QComboBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

from download import download_url

documents_folder = Path.home() / "Documents"
documents_folder.mkdir(parents=True, exist_ok=True)

SETTINGS_FILE = documents_folder / "yt_dl_settings.json"

if SETTINGS_FILE.exists():
    with open(SETTINGS_FILE, "r") as f:
        settings = json.load(f)
else:
    settings = {"format": "wav"}


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.executor = ThreadPoolExecutor()
        self.setWindowTitle("YT-Downloader")
        self.resize(600, 300)
        self.setStyleSheet("background-color: #141414;")

        # ── Format selector (top-left)
        self.format_selector = QComboBox()
        self.format_selector.addItems(
            ["wav", "mp3", "m4a", "flac", "alac", "ogg", "mp4", "mov", "avi", "flv"]
        )
        self.format_selector.setFixedWidth(90)
        self.format_selector.setCurrentText(settings["format"])
        self.format_selector.currentTextChanged.connect(self.save_format)

        top_layout = QHBoxLayout()
        top_layout.addWidget(self.format_selector)
        top_layout.addStretch()

        # ── Update label (subtle, centered)
        self.update_label = QLabel("")
        self.update_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.update_label.setSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed
        )

        # ── Title
        self.title_label = QLabel("YT-Downloader")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setStyleSheet(
            "font-family: Arial; font-size: 32px; color: deeppink; font-weight: bold;"
        )
        self.title_label.setSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed
        )

        # ── URL input + Generate button (modern row)
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Enter URL Here:")
        self.url_input.setMinimumHeight(40)

        self.generate_btn = QPushButton("Generate")
        self.generate_btn.setStyleSheet(
            "font-family: Arial; font-size: 21px; color: deeppink;"
            "background-color: #1F1F1F; border: 1px solid deeppink;"
            "border-radius: 2px; padding: 8px 16px; margin: 6px;"
        )
        self.generate_btn.clicked.connect(self.on_generate)

        input_layout = QHBoxLayout()
        input_layout.addWidget(self.url_input, stretch=1)
        input_layout.addWidget(self.generate_btn)

        # ── Main layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 16, 20, 16)
        main_layout.setSpacing(10)

        main_layout.addLayout(top_layout)
        main_layout.addSpacing(6)
        main_layout.addWidget(self.update_label)
        main_layout.addWidget(self.title_label)
        main_layout.addStretch()
        main_layout.addLayout(input_layout)

        self.setLayout(main_layout)

    def save_format(self, value):
        settings["format"] = value
        with open(SETTINGS_FILE, "w") as f:
            json.dump(settings, f)

    def on_generate(self):
        url = self.url_input.text().strip()
        selected_format = self.format_selector.currentText().strip().lower()

        if not url:
            self.update_label.setText("Please enter a valid URL!")
            return

        self.update_label.setText("Generating Audio/Video from URL...")

        self.executor.submit(download_url, url, selected_format)
