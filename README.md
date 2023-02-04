# ToF Overlay - Overlay for Tower of Fantasy

Shows an estimation of your background weapon&apos;s cooldown (last seen number). It ain&apos;t feature rich but it&apos;s better than counting in your head or checking manually.
Left to right: Q E R

![image](https://user-images.githubusercontent.com/107941092/216790094-44998a4b-29d8-4173-b66a-d37fde2fa23e.png)

## Requirements

- 1080p monitor
- In game shortcut is on (press F1)
- Your keybind is Q E R

![Screenshot 2023-02-05 042108](https://user-images.githubusercontent.com/107941092/216790045-59472467-8e09-4fa8-89c6-228ffd08433a.png)
- Fullscreen window

## What this overlay can NOT do (yet)

- Track cooldown reduction / cooldown reset
- Multi usage weapons such as Lin

## Installation

- Install the latest version [here](https://github.com/pdr-999/tof-overlay/releases/download/v1.0.0-beta/tof-overlay.zip) or [releases page](https://github.com/pdr-999/tof-overlay/releases)
- (Optional) Install Oxanium.ttf font

## Usage

- Run main.exe
- Hold Ctrl + click and drag to move the window around. Hold Alt + Ctrl + click if you&apos;re in-game
- Press X button to close

## FAQ

Q: How does it work?

A: Takes a small snapshot of your left weapon&apos;s keybind, right weapon&apos;s keybind, and your active weapon&apos;s cooldown many times (i forgot) every second with Tesseract OCR.

Q: CPU / RAM usage?

A: On my PC it&apos;s ~4% CPU and ~60 MB of RAM (from task manager).

Q: Bannable?

A: Nah trust me bro.

Q: Does it do anything sus (virus/malware)?

A: No, you can bundle it yourself if you&apos;re unsure.

## Bundle it yourself

1. Download [Tesseract OCR](https://tesseract-ocr.github.io/tessdoc/) and install it to root folder
2. Open `./identify.py` and modify this line
   `pytesseract.pytesseract.tesseract_cmd = r'./Tesseract-OCR-5/tesseract.exe'` to point to your installed Tesseract OCR&apos;s .exe file.
3. Run `$ pyinstaller --onefile --noconsole main.py`
4. Copy `samples` folder and your tesseract folder to `dist`
5. Run `dist/main.exe`

## Alternatives

Check out [Maygi&apos;s ToF overlay](https://github.com/Maygi/tof-overlay).

## Suggestions / Improvements / Bugs

Message me on discord `pon-de-ring#0122` or submit an Issue with the corresponding label. Your feedback is very welcome!

## Roadmap

- Support other resolutions
- Track cooldown reduction / cooldown reset
- Multi usage weapons such as Lin
- I only spent $2 in this game so I can't test all weapons
- Support custom keybinds
