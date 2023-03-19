# Set
## Install Playwright
```bash
pip install pytest-playwright
playwright install
```

## Launch a browser using CDP
```bash
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --no-first-run --no-default-browser-check --user-data-dir=$(mktemp -d -t 'chrome-remote_data_dir')
```
Paste the outputted string into the "connect_over_cdp" function in main.py

## Run the program
```bash
python3 set/main.py
```
