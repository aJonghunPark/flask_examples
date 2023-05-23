from splinter import Browser


def test_index():
    browser = Browser()
    url = "http://127.0.0.1:8000/tdd/"
    browser.visit(url)
    assert browser.is_text_present("hello world")
    browser.quit()
