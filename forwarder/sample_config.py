if not __name__.endswith("sample_config"):
    import sys

    print(
        "The README is there to be read. Extend this sample config to a config file, don't just rename and change "
        "values here. Doing that WILL backfire on you.\nBot quitting.",
        file=sys.stderr,
    )
    quit(1)


# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    REMOVE_TAG = False

    # REQUIRED
    API_KEY = "1953662837:AAFOSEN_zEo3YzSnCD0WZ7sPQek0xDePxVc"  # API key obtained from BotFather
    OWNER_ID = "1957520372"  # If you dont know, run the bot and do /id in your private chat with the bot

    # FOR AUTOMATICALLY FORWARDING MESSAGES
    FROM_CHATS = [-1001706470228]  # List of chat id's to forward messages from
    TO_CHATS = [-1686594925]  # List of chat id's to forward messages to

    # FOR WEBHOOKS
    WEBHOOK = False
    IP_ADDRESS = "127.0.0.1"  # Use "0.0.0.0" if using Heroku
    URL = None  # The URL that the bot should listen to for updates
    PORT = 5000  # Port to listen on for webhooks
    CERT_PATH = None  # Path to certificate file

    WORKERS = 4  # Depends on usage, 4 by default


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
