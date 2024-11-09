# jadsBot.py
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Definir a variável bot_token a partir das variáveis carregadas
bot_token = os.getenv('BOT_TOKEN')

# Inicializar o bot
intents = discord.Intents.default()
intents.messages = True  # Ativar eventos de mensagens

bot = commands.Bot(command_prefix='!', intents=intents)

# Evento de exemplo para garantir que o bot está funcionando corretamente
@bot.event
async def on_ready():
    print(f'Logado como {bot.user}')

# Comando simples para responder a uma mensagem "!ping"
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Rodar o bot com o token do arquivo .env
if __name__ == "__main__":
    bot.run(bot_token)