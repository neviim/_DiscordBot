import discord
from discord.ext import commands
from dotenv import load_dotenv

import os
import requests
#import secrets 

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Definir a variável bot_token a partir das variáveis carregadas
bot_token = os.getenv('BOT_TOKEN')

# Inicializar o bot
intents = discord.Intents.default()
intents.message_content = True  # Ativar eventos de mensagens

bot = commands.Bot(command_prefix='$', intents=intents)
# -----------------------------------------------------

@bot.command()
async def poke(ctx, arg):
    #print(f'Passo 0: {arg}')
    try:
        pokemon = arg.split(' ',1)[0].lower()
        result = requests.get('https://pokeapi.co/api/v2/pokemon/'+pokemon)
        #print(f'Passo 1: {result}')

        if result.text == 'Not Found':
            await ctx.send('Pokemon não Encontrado!')
        else:
            image_url = result.json()['sprites']['front_default']
            #print(image_url)
            await ctx.send(image_url)

    except Exception as e:
        print('Error: ', e)

@poke.error
async def error_type(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send('Precisa passar um Pokemon.') # 9:14

# -----------------------------------------------------------------------
# Evento de exemplo para garantir que o bot está funcionando corretamente
@bot.event
async def on_ready():
    print(f'Logado como {bot.user}')

# Limpar o canal
@bot.command()
async def limpar(ctx):
    await ctx.channel.purge()
    await ctx.send('Mensagens eliminadas!', delete_after=3)

# Rodar o bot com o token do arquivo .env
if __name__ == "__main__":
    bot.run(bot_token)


# Pikachu, Charizard, mew
# $poke pikachu
# $poke charizand
# $poke mew
#
# $limpar
