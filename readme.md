# My Translation App

My Translation App is a local AI translation software that uses the NLLB-200 model for translation. It supports multiple languages and can translate text, PDF, Word, and TXT documents.

## Features

- Translate text in real-time
- Translate PDF, Word, and TXT documents
- Polishing translations using facebook/nllb-200-distilled-600M
- System tray icon for easy access
- Adjustable font size for translation bubble

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/my_translation_app.git
   cd my_translation_app
   
    ```
   
2. Install the dependencies:
3. Run the app:
   ```bash
   python my_translation_app.py
   ```
4. How to use translate:
    - open the text you want to translate (support text, PDF, Word, and TXT documents and broswer)
    - Select the source and target languages
    - Click the translate button
    - The translation will appear in the translation bubble
    - Use your mouse wheel to adjust the font size of the translation bubble
    - Click the copy button (ctrl + c) to copy the translation to the clipboard
5. How to use file translate:
    - Click the file translate button
    - Select the file you want to translate
    - Select the source and target languages
    - Select the file it will automatically translate and save the file in the same directory
