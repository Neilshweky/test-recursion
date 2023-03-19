from playwright.sync_api import sync_playwright
from parseset import SetParser
import time

def run(playwright):
    browser = playwright.chromium.connect_over_cdp("ws://127.0.0.1:9222/devtools/browser/4c6fed30-30c3-4cf4-a925-dabff8214b93")
    default_context = browser.contexts[0]
    page = default_context.new_page()
    sets = SetParser.parseTodays()
    page.goto("https://www.setgame.com/set/puzzle")

    for set in sets:
      page.evaluate("""() => {{
        board.cardClicked({id0});
        board.cardClicked({id1});
        board.cardClicked({id2});
      }}
      """.format(id0=set[0].id, id1=set[1].id, id2=set[2].id))
      # time.sleep(1)
with sync_playwright() as playwright:
    run(playwright)