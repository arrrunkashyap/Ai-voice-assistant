import webbrowser
from urllib.parse import quote


# ---------- Open Websites ---------- #

def open_google():

    webbrowser.open("https://www.google.com")

    return "Opening Google."


def open_youtube():

    webbrowser.open("https://www.youtube.com")

    return "Opening YouTube."


def open_github():

    webbrowser.open("https://github.com")

    return "Opening GitHub."


def open_chatgpt():

    webbrowser.open("https://chat.openai.com")

    return "Opening ChatGPT."


def open_linkedin():

    webbrowser.open("https://www.linkedin.com")

    return "Opening LinkedIn."


def open_stackoverflow():

    webbrowser.open("https://stackoverflow.com")

    return "Opening Stack Overflow."


def open_leetcode():

    webbrowser.open("https://leetcode.com")

    return "Opening LeetCode."


def open_gmail():

    webbrowser.open("https://mail.google.com")

    return "Opening Gmail."


# ---------- Google Search ---------- #

def search_google(query: str):

    query = quote(query)

    webbrowser.open(
        f"https://www.google.com/search?q={query}"
    )

    return f"Searching Google for {query.replace('%20', ' ')}."


# ---------- YouTube Search ---------- #

def search_youtube(query: str):

    query = quote(query)

    webbrowser.open(
        f"https://www.youtube.com/results?search_query={query}"
    )

    return f"Searching YouTube for {query.replace('%20', ' ')}."


# ---------- GitHub Search ---------- #

def search_github(query: str):

    query = quote(query)

    webbrowser.open(
        f"https://github.com/search?q={query}"
    )

    return f"Searching GitHub for {query.replace('%20', ' ')}."


# ---------- Maps ---------- #

def open_maps():

    webbrowser.open(
        "https://maps.google.com"
    )

    return "Opening Google Maps."


def search_maps(place: str):

    place = quote(place)

    webbrowser.open(
        f"https://www.google.com/maps/search/{place}"
    )

    return f"Searching Google Maps for {place.replace('%20', ' ')}."


# ---------- Wikipedia ---------- #

def search_wikipedia(topic: str):

    topic = quote(topic)

    webbrowser.open(
        f"https://en.wikipedia.org/wiki/{topic}"
    )

    return f"Opening Wikipedia for {topic.replace('%20', ' ')}."