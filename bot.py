import discord
from discord.ext import commands
import os
from datetime import datetime  # Importar datetime para obtener la fecha y hora

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

    # Aquí buscamos un canal donde el bot puede enviar el mensaje
    # Puedes reemplazar 'nombre-del-canal' con el nombre del canal que desees
    channel = discord.utils.get(bot.get_all_channels(), name='backups')

    if channel is not None:
        file_path = '/workspaces/ServerTest/respaldos/world_respaldo.zip'

        # Verifica si el archivo existe antes de enviarlo
        if os.path.exists(file_path):
            # Obtener la fecha y hora actuales
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            await channel.send(f"Respaldo enviado a las: {current_time}", file=discord.File(file_path))
        else:
            await channel.send("El archivo de respaldo no existe o la ruta es incorrecta.")
    else:
        print("No se encontró el canal.")

# Ejecutar el bot
bot.run('MTI5MzMyNDYxNTgxMjM4NzAzNw.GXqDcX.bh8onHBCAFbNr6XkD6ROcZxt7HB_qO9qOyzHHY')
