# jadsBot.py
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import webserver

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Definir a variável bot_token a partir das variáveis carregadas
bot_token = os.getenv('BOT_TOKEN')

# Inicializar o bot
intents = discord.Intents.default()
intents.messages = True  # Ativar eventos de mensagens

bot = commands.Bot(command_prefix='!', intents=intents)

# Notificação quando o usuário específico "neviim" envia uma mensagem no canal "dev"
@bot.event
async def on_message(message):
    print(f'Nome: {message.author.name} Canal: {message.channel.name}')

    if message.author.name == "Xpto" and message.channel.name == "dev":
        user_jads = discord.utils.get(message.guild.members, name="Ypto")
        print('Passo 1')
        
        if user_jads:
            await user_jads.send(f'O usuário {message.author.name} enviou uma mensagem no canal #dev: {message.content}')
    await bot.process_commands(message)

# Evento de exemplo para garantir que o bot está funcionando corretamente
@bot.event
async def on_ready():
    print(f'Logado como {bot.user}')

# Comando simples para responder a uma mensagem "!ping"
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def off(ctx):
    await ctx.send('Bot desativado!')


# Rodar o bot com o token do arquivo .env
if __name__ == "__main__":
    webserver.keep_alive()
    bot.run(bot_token)