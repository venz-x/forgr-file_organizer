# FORGR ⚡

A fast, interactive command-line file organizer for Linux.

FORGR is a native Python CLI tool designed to instantly sort cluttered directories. Instead of writing long scripts or manually dragging files, FORGR drops you into an interactive shell where you can safely categorize and copy files based on their extensions.

## Installation

Install FORGR globally on your Linux system using the web installer:

```bash
curl -sL https://raw.githubusercontent.com/venz-x/forgr-file_organizer/refs/heads/main/install.sh | sudo bash
```

## 🛠️ Usage

You can run basic checks directly from your normal Linux terminal:

```bash
forgr --help     # Show the help menu and syntax guide
forgr --version  # Check your current installed version
```

To start organizing files, launch the interactive shell by typing:

```bash
forgr
```

Once inside the `forgr>` prompt, use the `run` command.

**Syntax:**

```text
run s="<source_directory>" d="<destination_directory>" ex="<extension_group>"
```

**Examples:**

```text
# Organize all images from Downloads to a specific Pictures folder
forgr> run s="/home/user/Downloads" d="/home/user/Pictures/Saved" ex="images"

# Extract all code files from a messy project folder
forgr> run s="/var/www/messy_folder" d="/var/www/clean_code" ex="code"
```

---

## Supported Extension Groups

`FORGR` uses predefined groups to intelligently sort files. When using the `ex=` parameter, pass the **Group Name** to instantly target all associated file types.

* **`images`**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.svg`, `.webp`, `.heic`, `.heif`, `.tiff`, `.tif`, `.psd`, `.ai`, `.ico`, `.bmp`, `.dng`, `.cr2`, `.cr3`, `.nef`, `.arw`
* **`docs`**: `.txt`, `.pdf`, `.docx`, `.doc`, `.md`, `.csv`, `.rtf`, `.odt`, `.ods`, `.odp`, `.xls`, `.xlsx`, `.ppt`, `.pptx`, `.tex`
* **`code`**: `.py`, `.sh`, `.bash`, `.c`, `.cpp`, `.h`, `.go`, `.rs`, `.js`, `.ts`, `.java`
* **`web`**: `.html`, `.htm`, `.css`, `.scss`, `.json`, `.xml`, `.yaml`, `.yml`, `.ini`
* **`audio`**: `.mp3`, `.wav`, `.ogg`, `.flac`, `.m4a`, `.aac`, `.opus`
* **`video`**: `.mp4`, `.mkv`, `.avi`, `.mov`, `.wmv`, `.flv`, `.webm`
* **`archives`**: `.zip`, `.tar`, `.gz`, `.bz2`, `.xz`, `.7z`, `.rar`, `.tgz`
* **`binaries`**: `.bin`, `.exe`, `.out`, `.appimage`
* **`packages`**: `.deb`, `.rpm`, `.apk`, `.snap`
* **`libraries`**: `.so`, `.a`, `.o`, `.ko`
* **`database`**: `.db`, `.sqlite`, `.sqlite3`, `.sql`, `.mdb`
* **`backup`**: `.bak`, `.old`, `.tmp`, `.swp`