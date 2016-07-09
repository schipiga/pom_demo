# -*- coding: utf-8 -*-

def test_google_search(google_steps, app):
    google_steps.search('selenium')
    assert u"Что такое Selenium?" in app.page_search.list_search.rows[0].value
