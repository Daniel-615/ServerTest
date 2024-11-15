import discord
from discord.ext import commands
import os
from datetime import datetime  # Importar datetime para obtener la fecha y hora
from dotenv import load_dotenv

load_dotenv()
# Configurar los intents
intents = discord.Intents.default()
intents.messages = True  # Activa los intents de mensajes
intents.guilds = True  # Activa los intents de servidores
intents.message_content = True  # Necesario para que el bot pueda leer el contenido de los mensajes

# Crear una instancia del bot con los intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user} ha iniciado sesión.')

    channel = discord.utils.get(bot.get_all_channels(), name='backups')

    if channel is not None:
        file_path = '/workspaces/ServerTest/respaldos/world_respaldo.zip'
        config_path='/workspaces/ServerTest/respaldos/plugins_respaldo.zip'

        # Verifica si el archivo existe antes de enviarlo
        if os.path.exists(file_path):
            # Obtener la fecha y hora actuales
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            await channel.send(f"Respaldo enviado a las: {current_time}", file=discord.File(file_path))
            await channel.send(f"Respaldo enviado a las: {current_time}", file=discord.File(config_path))
        else:
            await channel.send("El archivo de respaldo no existe o la ruta es incorrecta.")
    else:
        print("No se encontró el canal.")

# Ejecutar el bot
bot.run(os.getenv('DISCORD_TOKEN'))
