
import os

class Config:

    BOT_TOKEN = os.environ.get('BOT_TOKEN', '6784187459:AAFDry6G2ebpf25CVA77O1nb665J08eD884')
    APP_ID = os.environ.get('APP_ID', '20738903')
    API_HASH = os.environ.get('API_HASH', 'f14bc2de0f71c54d385ce25948058e52')

    #comma seperated user id of users who are allowed to use
    ALLOWED_USERS = [x.strip(' ') for x in os.environ.get('ALLOWED_USERS','800209209').split(',')]

    DOWNLOAD_DIR = 'downloads'
