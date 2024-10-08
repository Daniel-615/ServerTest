import discord
from discord.ext import commands
import os

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

# Comando para enviar un archivo
@bot.command()
async def enviar(ctx):
    file_path = '/workspaces/ServerTest/respaldos/world_respaldo.zip'
    
    # Verifica si el archivo existe antes de enviarlo
    if os.path.exists(file_path):
        await ctx.send(file=discord.File(file_path))
    else:
        await ctx.send("El archivo de respaldo no existe o la ruta es incorrecta.")

# Ejecutar el bot
bot.run('MTI5MzMyNDYxNTgxMjM4NzAzNw.GXqDcX.bh8onHBCAFbNr6XkD6ROcZxt7HB_qO9qOyzHHY')
