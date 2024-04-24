import os
from environs import Env
from dotenv import load_dotenv
load_dotenv()
# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = os.getenv('ADMINS')  # adminlar ro'yxati
# IP = env.str("ip")  # Xosting ip manzili
CHANNEL = ['@hayotiy_tajribam_uz', '@Ibodati_islomiya_D']
