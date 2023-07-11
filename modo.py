DEBUG = False

def cambia_modo():
    global DEBUG
    DEBUG = not DEBUG


def get_mode():
    return DEBUG