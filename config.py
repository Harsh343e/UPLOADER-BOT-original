import os

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6127937943:AAHOzm_n6fbT0TbUPmJmFj26-QZvJcFHbVE")
    
    API_ID = int(os.environ.get("API_ID", 21941890))
    
    API_HASH = os.environ.get("API_HASH","a192de10945cf3685dbe8ae711b238d8")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 50000000

    TG_MAX_FILE_SIZE = 2097152000

    FREE_USER_MAX_FILE_SIZE = 50000000
    
    CHUNK_SIZE = int(128)

    HTTP_PROXY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 3600
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "1366318700"))

    SESSION_NAME = "MyURL1432_bot"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Chiku:Harsh9421806556@cluster0.t613z7i.mongodb.net/?retryWrites=true&w=majority")

    MAX_RESULTS = "50"
