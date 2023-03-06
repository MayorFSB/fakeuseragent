# -*- coding: utf-8 -*-
DB = 'browsers.json'
BROWSER_BASE_PAGE = "https://useragentstring.com/pages/{browser}/"  # noqa0

BROWSERS_COUNT_LIMIT = 50

REPLACEMENTS = {" ": "", "_": ""}

SHORTCUTS = {
    "internetexplorer": "internet explorer",
    "ie": "internet explorer",
    "msie": "internet explorer",
    "microsoft edge": "edge",
    "google": "chrome",
    "googlechrome": "chrome",
    "ff": "firefox",
}

OVERRIDES = {
    "Edge/IE": "Internet Explorer",
    "IE/Edge": "Internet Explorer",
}

HTTP_TIMEOUT = 5

HTTP_RETRIES = 2

HTTP_DELAY = 0.1