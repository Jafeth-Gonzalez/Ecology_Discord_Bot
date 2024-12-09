import discord
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$',  intents=intents)
api = "his api"
@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')
    canal = bot.get_channel(1315423418312818688)  # Reemplaza con el ID de un canal conocido
    await canal.send("¡Hola! El bot está ahora en línea. 😊")
@bot.command(help ="Proporciona consejos ecológicos 🌍 para reducir la contaminación 🌫️ y residuos 🗑️, como consejos sobre reciclaje ♻️, reducción de plásticos 🛍️, etc.")
async def tip(ctx):
    await ctx.send("🌍 Para reducir la contaminación y los residuos: ♻️ recicla correctamente separando papel 📄, vidrio 🍾 y plásticos 🛍️; usa bolsas reutilizables 👜; opta por productos sin envases plásticos 🚫📦; elige productos reciclados ✅; evita artículos de un solo uso 🥤❌; reutiliza objetos siempre que sea posible 🔄 y consume localmente 🛒🌱 para reducir la huella de carbono 🌿.")
@bot.command(help ="Informa sobre cómo empezar el compostaje en casa 🏡🌱, una forma ecológica de reducir residuos orgánicos ♻️🍎.")
async def compost(ctx):
    await ctx.send("El compostaje en casa es fácil y ecológico 🌱. Usa una compostera o haz una con un recipiente ventilado 🛠️. Mezcla residuos orgánicos como cáscaras de frutas 🍎 y restos de verduras 🥕 con hojas secas 🍂 o papel. Mantén la mezcla aireada y húmeda 💧, evitando alimentos grasos o carne 🚫. En pocas semanas, tendrás compost para tus plantas 🌷. ¡Reduce residuos y nutre la tierra! 🌎✨")
@bot.command(help ="Sugerencias de productos y marcas ecológicas 🌱 que los usuarios pueden utilizar para reducir su impacto ambiental 🌎.")
async def eco_friendly(ctx):
    await ctx.send("Para reducir tu impacto ambiental 🌎, opta por productos ecológicos como las botellas reutilizables de S'well 🍼, pañales biodegradables de Bambo Nature 🌿, ropa sostenible de Patagonia 👕, y cosméticos naturales de Lush 💚. También elige electrodomésticos eficientes como los de Bosch 🔋 y utensilios de cocina de BambooMN 🍴. ¡Haz la diferencia con cada elección!")
@bot.command(help =" Explica las propiedades ecológicas 🌿 de productos, como la biodegradabilidad 🌱, reciclabilidad ♻️, etc.")
async def caracteristicas(ctx):
    await ctx.send("Los productos ecológicos tienen propiedades como la biodegradabilidad 🌱, que les permite descomponerse de forma natural sin contaminar. También son reciclables ♻️, lo que facilita su reutilización y reduce el desperdicio. Otros atributos incluyen la reducción de emisiones 🌍 y el uso de materiales sostenibles 🌿, lo que favorece el cuidado del medio ambiente.")


bot.run(api)
