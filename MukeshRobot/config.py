
class Config(object):
    LOGGER = True

    #####

    ANILIST_CLIENT = getenv("ANILIST_CLIENT", "8679")
  
    ANILIST_SECRET = getenv("ANILIST_SECRET", "NeCEq9A1hVnjsjZlTZyNvqK11krQ4HtSliaM7rTN")
  
    API_ID = getenv("API_ID", None)
   
    API_HASH = getenv("API_HASH",None)
   
    TOKEN = getenv("TOKEN", None)
  
    OWNER_ID = getenv("OWNER_ID", "5730490876") 

    OWNER_USERNAME = ("OWNER_USERNAME", "yt_farman")
    
    SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/NKD_Korean_Group")
   
    START_IMG = getenv("START_IMG", "https://graph.org/file/6b7ba5df9b008e44203b8.jpg")

    JOIN_LOGGER = getenv("JOIN_LOGGER", "-1001961907996")
   
    EVENT_LOGS = getenv("EVENT_LOGS",  "-1001961907996")
  
    ERROR_LOGS = getenv("ERROR_LOGS", "-1001961907996")

    MONGO_DB_URI= getenv("MONGO_DB_URI", None)
   
    LOG_CHANNEL = getenv("LOG_CHANNEL", "-1001961907996")
   
    BOT_USERNAME = getenv("BOT_USERNAME" , "Doreamon_ro_bot")
   
    DATABASE_URL = getenv("DATABASE_URL", "postgres://jvktgwnb:WbxYrXTbIhjtva-rFyoxz83HHSco9I4I@flora.db.elephantsql.com/jvktgwnb")

    CASH_API_KEY = getenv("CASH_API_KEY", "V48U2FLLKRHSVD4X")
    
    TIME_API_KEY = getenv("TIME_API_KEY", "1CUBX1HXGNHW")

    SPAMWATCH_API = getenv("SPAMWATCH_API", "3624487efd8e4ca9c949f1ab99654ad1e4de854f41a14afd00f3ca82d808dc8c")
    
    SPAMWATCH_SUPPORT_CHAT = getenv("SPAMWATCH_SUPPORT_CHAT", "h_cc_help")
    
    WALL_API = getenv("WALL_API", "2455acab48f3a935a8e703e54e26d121")
    
    REM_BG_API_KEY = getenv("REM_BG_API_KEY", "xYCR1ZyK3ZsofjH7Y6hPcyzC")
    
    OPENWEATHERMAP_ID = getenv("OPENWEATHERMAP_ID", "887da2c60d9f13fe78b0f9d0c5cbaade")

    BAN_STICKER = getenv("BAN_STICKER", "CAACAgUAAx0CdPBXHAACR0JmMFNFz1IKdi1G0zEUVVxKjyEJBQAC3wsAAo5XqFUhagM3X7NqhzQE")

    HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

    HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
    
    # Optional fields
    
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
    
