# Copyright 2023 Qewertyy, MIT License

import uvloop
uvloop.install()
import datetime,logging, sys
from pyrogram import Client
from lexica import Client as ApiClient
from config import Config
from Utils.telegraph import GraphClient

# Get logging configurations
logging.basicConfig(
    format="%(asctime)s - [BOT] - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("logs.txt"), logging.StreamHandler()],
    level=logging.INFO,
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("httpx").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

StartTime = None
Models = None

TelegraphClient = GraphClient(
    "LexicaAPI",
    "https://t.me/LexicaAPI",
    "LexicaAPI"
)
TelegraphClient.createAccount()

class Bot(Client):
    global StartTime,Models
    StartTime = datetime.datetime.now()
    api = ApiClient()
    Models = api.getModels()['models']['image']
    #print(Models)
    def __init__(self):
        super().__init__(
            "SDWaifuRobot",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            plugins=dict(root="plugins"),
        )
    async def start(self):
        await super().start()
        LOGGER.info(f""" \n\n       
                                                   
                  
                                 
   ____ ___  ____  _____ _____ _     _____  __  ____   ___ _____ ____   
  / ___/ _ \|  _ \| ____|  ___| |   |_ _\ \/ / | __ ) / _ \_   _/ ___|  
 | |  | | | | | | |  _| | |_  | |    | | \  /  |  _ \| | | || | \___ \  
 | |__| |_| | |_| | |___|  _| | |___ | | /  \  | |_) | |_| || |  ___) | 
  \____\___/|____/|_____|_|   |_____|___/_/\_\ |____/ \___/ |_| |____/  
                                                                        
                                                                      
                                                                                 
                              
                                          """)

    if Models is None:
        LOGGER.error("Models are empty!")
        sys.exit(1)

    async def stop(self):
        await super().stop()
        LOGGER.info("Stopped Services")

if __name__ == "__main__":
    Bot().run()
