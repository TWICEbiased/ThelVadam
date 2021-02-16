#ThelVadam, bot para Discord hecho por Memo Flores, versión Beta v0.6.0

""" This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>."""

import discord
import abc
import os
import time
import random
from random import randint
from discord.ext import commands, tasks
import asyncio
import datetime as dt
from linereader import copen
from keep_alive import keep_alive

keep_alive()
client = discord.Client()

@client.event
async def on_ready():
    intentos = 1
    atte = str(intentos)
    try:
        print('We hebben ingelogd als {0.user} na '.format(client) + atte + ' poging(en)')
        #message_channel = client.get_channel(805855767206166599)
        #await message_channel.send("¡Hola! :3.")
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a quién ayudar :3"))
        print("Status 3 geselecteerd")
        print("Este software se encuentra licenciado bajo la GNU GPL v3")
    except:
        intentos = intentos + 1
        client.run('ODA2MjAzMTI3NDUxNjE1MjUy.YBmBLA.oGty49z0tDr92ENq_tQdyqNxpCk')
            
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    mensaje1 = message.content
    listamensaje = list(mensaje1.split(" "))
    if "jueputa" in listamensaje:
        nombre1 = str(message.author.id)
        await message.channel.send(' Epale pinche  <@' + nombre1 + '>. Tantito respeto por el servidor carnal ;)')
    elif "hijueputa" in listamensaje:
        nombre1 = str(message.author.id)
        await message.channel.send(' Epale pinche  <@' + nombre1 + '>. Tantito respeto por el servidor carnal ;)')
    elif "gonorrea" in listamensaje:
        nombre1 = str(message.author.id)
        await message.channel.send(' Epale pinche  <@' + nombre1 + '>. Tantito respeto por el servidor carnal ;). Además a ti ya te dio gonorrea y no lo quieres aceptar XD.')
    elif "malparida" in listamensaje:
        nombre1 = str(message.author.id)
        await message.channel.send(' Epale pinche  <@' + nombre1 + '>. Tantito respeto por el servidor carnal ;)')
    elif "malparido" in listamensaje:
        nombre1 = str(message.author.id)
        await message.channel.send(' Epale pinche  <@' + nombre1 + '>. Tantito respeto por el servidor carnal ;)')
    elif "Jueputa" in listamensaje:
        nombre1 = str(message.author.id)
        await message.channel.send(' Epale pinche  <@' + nombre1 + '>. Tantito respeto por el servidor carnal ;)')
    elif "Hijueputa" in listamensaje:
        nombre1 = str(message.author.id)
        await message.channel.send(' Epale pinche  <@' + nombre1 + '>. Tantito respeto por el servidor carnal ;)')
    elif "ijueputa" in listamensaje:
        nombre1 = str(message.author.id)
        await message.channel.send(' Epale pinche  <@' + nombre1 + '>. Tantito respeto por el servidor carnal ;)')
    elif "Ijueputa" in listamensaje:
        nombre1 = str(message.author.id)
        await message.channel.send(' Epale pinche  <@' + nombre1 + '>. Tantito respeto por el servidor carnal ;)')
    elif "Malparido" in listamensaje:
        nombre1 = str(message.author.id)
        await message.channel.send(' Epale pinche  <@' + nombre1 + '>. Tantito respeto por el servidor carnal ;)')
    elif "Malparida" in listamensaje:
        nombre1 = str(message.author.id)
        await message.channel.send(' Epale pinche  <@' + nombre1 + '>. Tantito respeto por el servidor carnal ;)')
    elif "Gonorrea" in listamensaje:
        nombre1 = str(message.author.id)
        await message.channel.send(' Epale pinche  <@' + nombre1 + '>. Tantito respeto por el servidor carnal ;). Además a ti ya te dio gonorrea y no lo quieres aceptar XD.')
    elif "puto" in listamensaje:
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        if nombre2 == "<@!721920162005123142>":
            return
        else:
            await message.channel.send(' Puto tú,  <@' + nombre1 + '>. Tantito respeto por el servidor carnal ;).')
    elif "Puto" in listamensaje:
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        if nombre2 == "<@!721920162005123142>":
            return
        else:
            await message.channel.send(' Puto tú,  <@' + nombre1 + '>. Tantito respeto por el servidor carnal ;).')
    elif "puta" in listamensaje:
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        if nombre2 == "<@!721920162005123142>":
            return
        else:
            await message.channel.send(' Puta tú,  <@' + nombre1 + '>. Tantito respeto por el servidor carnal ;).')
    elif "Puta" in listamensaje:
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        if nombre2 == "<@!721920162005123142>":
            return
        else:
            await message.channel.send(' Puta tú,  <@' + nombre1 + '>. Tantito respeto por el servidor carnal ;).')
    if message.content.startswith('hola'):
        nombre1 = str(message.author.id)
        await message.channel.send(' ¡Hola,  <@' + nombre1 + '>! ¿Qué tal te va?')
    if message.content.startswith('Hola Bien Y Tu? :D'):
        await message.channel.send('Bien, bien :3 Me alegro que estés bien, saluda al Jefe Maestro de mi parte :).')
    elif message.content.startswith('Hola'):
        nombre1 = str(message.author.id)
        await message.channel.send('¡Hola, <@' + nombre1 + '>! ¿Cómo estás?')
    elif message.content.startswith('Wenas'):
        nombre1 = str(message.author.id)
        await message.channel.send('¡Hola, <@' + nombre1 + '>! ¿Cómo te sientes hoy?')
    elif message.content.startswith('wenas'):
        nombre1 = str(message.author.id)
        await message.channel.send('¡Hola, <@' + nombre1 + '>! ¿Todo bien? Me alegro que estés bien :3')
    elif message.content.startswith('Buenas'):
        nombre1 = str(message.author.id)
        await message.channel.send('¡Hola, <@' + nombre1 + '>! ¿Cómo te sientes hoy?')
    elif message.content.startswith('buenas'):
        nombre1 = str(message.author.id)
        await message.channel.send('¡Hola, <@' + nombre1 + '>! ¿Todo bien? Me alegro que estés bien :3')
    elif message.content.startswith('Buenos dias'):
        nombre1 = str(message.author.id)
        await message.channel.send('¡Buenos días, <@' + nombre1 + '>! ¿Todo bien?')
    elif message.content.startswith('Buenos días'):
        nombre1 = str(message.author.id)
        await message.channel.send('¡Buenos días, <@' + nombre1 + '>! ¿Cómo va todo?')
    elif message.content.startswith('¡Hola! Soy Cortana.'):
        nombre1 = str(message.author.id)
        await message.channel.send('¡Hola, <@' + nombre1 + '>! ¿Cómo va todo?')
    elif message.content.startswith('buenos dias'):
        nombre1 = str(message.author.id)
        await message.channel.send('¡Buenos días, <@' + nombre1 + '>! ¿Ya tomaste agüita? :3')
    elif message.content.startswith('buenos días'):
        nombre1 = str(message.author.id)
        await message.channel.send('¡Buenos días, <@' + nombre1 + '>!')
    elif message.content.startswith('buen día'):
        nombre1 = str(message.author.id)
        await message.channel.send('¡Buen día, <@' + nombre1 + '>! Espero que estés bien ^_^')
    elif message.content.startswith('buen dia'):
        nombre1 = str(message.author.id)
        await message.channel.send('¡Buen día, <@' + nombre1 + '>! ¿Ya recargaste tus escudos?')
    elif message.content.startswith('Buen dia'):
        nombre1 = str(message.author.id)
        await message.channel.send('¡Buen día, <@' + nombre1 + '>!')
    elif message.content.startswith('Buen día'):
        nombre1 = str(message.author.id)
        await message.channel.send('¡Buen día, <@' + nombre1 + '>! No olvides cuidarte de la infección del flood :3')
    elif message.content.startswith('que hora es'):
        hora = time.strftime("%H:%M:%S")
        await message.channel.send('Son las ' + hora)
    elif message.content.startswith('qué hora es'):
        hora = time.strftime("%H:%M:%S")
        await message.channel.send('Son las ' + hora)
    elif message.content.startswith('que hora son'):
        hora = time.strftime("%H:%M:%S")
        await message.channel.send('Son las ' + hora)
    elif message.content.startswith('qué hora son'):
        hora = time.strftime("%H:%M:%S")
        await message.channel.send('Son las ' + hora)
    elif message.content.startswith('Que hora es'):
        hora = time.strftime("%H:%M:%S")
        await message.channel.send('Son las ' + hora)
    elif message.content.startswith('Qué hora es'):
        hora = time.strftime("%H:%M:%S")
        await message.channel.send('Son las ' + hora)
    elif message.content.startswith('Que hora son'):
        hora = time.strftime("%H:%M:%S")
        await message.channel.send('Son las ' + hora)
    elif message.content.startswith('Qué hora son'):
        hora = time.strftime("%H:%M:%S")
        await message.channel.send('Son las ' + hora)
    elif message.content.startswith('!tv me ama'):
        await desicionamor(message)
    elif message.content.startswith('!tv ayuda'):
        await ayuda(message)
    elif message.content.startswith('!tv help'):
        await ayuda(message)
    elif message.content.startswith('!tv es pendejo'):
        await desicionpendejo(message)
    elif message.content.startswith('!tv status1'):
            nombre1 = str(message.author.id)
            nombre2 = "<@!" + nombre1 + ">"
            if nombre2 == "<@!721920162005123142>":
                await client.change_presence(activity=discord.Game(name="!tv ayuda"))
                await message.channel.send('Estado #1 establecido')
            else:
                await message.channel.send('Lo siento, no tienes permiso para ejecutar este comando ^_^')
    elif message.content.startswith('!tv status2'):
            nombre1 = str(message.author.id)
            nombre2 = "<@!" + nombre1 + ">"
            if nombre2 == "<@!721920162005123142>":
                await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="ayuda"))
                await message.channel.send('Estado #2 establecido')
            else:
                await message.channel.send('Lo siento, no tienes permiso para ejecutar este comando ^_^')

    elif message.content.startswith('!tv status3'):
            nombre1 = str(message.author.id)
            nombre2 = "<@!" + nombre1 + ">"
            if nombre2 == "<@!721920162005123142>":
                await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a quién ayudar :3"))
                await message.channel.send('Estado #3 establecido')
            else:
                await message.channel.send('Lo siento, no tienes permiso para ejecutar este comando ^_^')
        
    elif message.content.startswith('!tv noticia'):
        handler = open('noticia.txt')
        noticia = handler.read()
        #message_channel = client.get_channel(803850947734011925)
        await message.channel.send(noticia)
    elif message.content.startswith('wat ben ik'):
            nombre1 = str(message.author.id)
            nombre2 = "<@!" + nombre1 + ">"
            if nombre2 == "<@!721920162005123142>":
                await message.channel.send('Je bent een mooie vrouw :3')
            else:
                await message.channel.send('Lo siento, no tienes permiso para ejecutar este comando ^_^')

    elif message.content.startswith('!tv beso'):
        await besar(message)
    elif message.content.startswith('!tv besar'):
        await besar(message)
    elif message.content.startswith('!tv kiss'):
        await besar(message)
    elif message.content.startswith('inquisidor sabe dar masajes en los pies'):
        await message.channel.send('Recuerdo cuando mi pelotón me preguntaba eso cuando nuestra misión era cazar al Líder Hereje. Era asqueroso, pero daba sensación de fraternidad.')
    elif message.content.startswith('Inquisidor sabe dar masajes en los pies'):
        await message.channel.send('Recuerdo cuando mi pelotón me preguntaba eso cuando nuestra misión era cazar al Líder Hereje. Era asqueroso, pero daba sensación de fraternidad.')
    elif message.content.startswith('!tv meme'):
        await desicionmeme(message)
    elif message.content.startswith('takaimayo'):
        await message.channel.send('Watashi wa takaimayo to oniichan aishiteru :3.')
    elif message.content.startswith('Takaimayo'):
        await message.channel.send('Watashi wa takaimayo to oniichan aishiteru :3.')
    elif message.content.startswith('!tv nl'):
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        if nombre2 == "<@!721920162005123142>":
            await nederlands(message)
        else:
            await message.channel.send('Lo siento, no tienes permiso para ejecutar este comando ^_^')
    elif message.content.startswith('!tv chocolat o tu'):
        await message.channel.send('Chocolat es muy buena amiga y BOT. Los dos hacemos bien nuestro trabajo :3.')
    elif message.content.startswith('!tv tu o chocolat'):
        await message.channel.send('Chocolat es muy buena amiga y BOT. Los dos hacemos bien nuestro trabajo :3.')
    elif message.content.startswith("!tv diversity"):
        await message.delete()
        await diversity(message)
    elif message.content.startswith("!tv lgbt"):
        await message.delete()
        await diversity(message)
    elif message.content.startswith("!tv lgtb"):
        await message.delete()
        await message.channel.send('La B va antes de la T :3.')
    elif message.content.startswith("!tv LGBT"):
        await message.delete()
        await diversity(message)
    elif message.content.startswith("!tv LGTB"):
        await message.delete()
        await message.channel.send('La B va antes de la T :3.')


async def desicionamor(message):
    try:
        amor1 = message.content
        listaamor = list(amor1.split(" "))
        desicionlista = ["1","2","3","4","5","6","7","8","9","10","11","12"]
        desicion = ""
        desicion = random.choice(desicionlista)
        if desicion == "1":
            await message.channel.send('Sí uwu. ' + listaamor[3] + 'te ama <3')
            desicion = random.choice(desicionlista)
        elif desicion == "2":
            await message.channel.send('No ¬¬. ' + listaamor[3] + 'no tiene sentimientos >:(')
            desicion = random.choice(desicionlista)
        elif desicion == "3":
            await message.channel.send('Tal vez ' + listaamor[3] + ' te ama XD.')
            desicion = random.choice(desicionlista)
        elif desicion == "4":
            await message.channel.send('Tal vez ' + listaamor[3] + ' no te ama ¬¬.')
            desicion = "1"
        elif desicion == "5":
            nombre1 = str(message.author.id)
            await message.channel.send('Puede ser :p. Oye ' + listaamor[3] + ', ¿amas a <@' + nombre1 + '>? O.O')
            desicion = random.choice(desicionlista)
        elif desicion == "10":
            await message.channel.send('No creo que ' + listaamor[3] + ' te ame pero ps va XD.')
            desicion = random.choice(desicionlista)
        elif desicion == "7":
            await message.channel.send('Tú y ' + listaamor[3] + ' son el amor de sus vidas <3.')
            desicion = random.choice(desicionlista)
        elif desicion == "8":
            await message.channel.send('Nah, bien tóxico el ' + listaamor[3] + ' XD.')
            desicion = random.choice(desicionlista)
        elif desicion == "9":
            nombre1 = str(message.author.id)
            await message.channel.send('Yo les pago la boda pts. <@' + nombre1 + '>' + ' + ' + listaamor[2])
            desicion = random.choice(desicionlista)
        elif desicion == "10":
            await message.channel.send('Ps... creo que ' + listaamor[3] + 'sí te ama, pero mejor pregúntale.')
            desicion = random.choice(desicionlista)
        elif desicion == "11":
            await message.channel.send('Tú y ' + listaamor[3] + ' nacieron para odiarse >:3.')
            desicion = "2"
        elif desicion == "12":
            await message.channel.send('Tú y ' + listaamor[3] + 'serían una hermosa pareja uwu.')
            desicion = random.choice(desicionlista)
        else:
            await message.channel.send('¿Eh? No entendí. Repite por favor :).')
    except:
        await message.channel.send('No seas burro mano, tienes que mencionar a alguien ¬¬.')

async def desicionpendejo(message):
    try:
        pendejo1 = message.content
        listapendejo = list(pendejo1.split(" "))
        pendejo2 = listapendejo[3]
        print("Es pendejo " + pendejo2 +" XD")
        desicionlistapen = ["1","2","3","4","5","6","7","8","9","10","11","12"]
        desicionpen = ""
        desicionpen = random.choice(desicionlistapen)
        if desicionpen == "1":
            await message.channel.send('Sí XD.')
            desicionpen = random.choice(desicionlistapen)
        elif desicionpen == "2":
            await message.channel.send('No xdd.')
            desicionpen = random.choice(desicionlistapen)
        elif desicionpen == "3":
            await message.channel.send('Tal vez XD.')
            desicionpen = random.choice(desicionlistapen)
        elif desicionpen == "4":
            await message.channel.send('No creo, ese we me madreó en un 1v1 XD.')
            desicionpen = "1"
        elif desicionpen == "5":
            await message.channel.send('Puede ser :p.')
            desicionpen = random.choice(desicionlistapen)
        elif desicionpen == "10":
            await message.channel.send('No creo pero ps va XD.')
            desicionpen = random.choice(desicionlistapen)
        elif desicionpen == "7":
            await message.channel.send('Si llega a un concurso de pendejos, pierde por pendejo XD [JODA].')
            desicionpen = random.choice(desicionlistapen)
        elif desicionpen == "8":
            await message.channel.send('Nah, se ve listillo el parce.')
            desicionpen = random.choice(desicionlistapen)
        elif desicionpen == "9":
            await message.channel.send('Epale aguas con mi pana no lo esté molestando.')
            desicionpen = random.choice(desicionlistapen)
        elif desicionpen == "10":
            await message.channel.send('Ps... creo que sí.')
            desicionpen = random.choice(desicionlistapen)
        elif desicionpen == "11":
            await message.channel.send('El pendejo es uste xd.')
            desicionpen = "2"
        elif desicionpen == "12":
            await message.channel.send('¿Es joda verdad?')
            desicionpen = random.choice(desicionlistapen)
        else:
            await message.channel.send('¿Eh? No entendí. Repite por favor :).')
    except:
        await message.channel.send('No seas pendejo mijo :3. Menciona a alguien ._.')
async def ayuda(message):
    handler = open('help.txt')
    ayuda1 = handler.read()
    embed = discord.Embed(

        title="Ayuda de ThelVadam",
        description=ayuda1,
        color=discord.Colour.random()

    )
    #message_channel = client.get_channel(803850947734011925)
    await message.author.send(embed = embed)
    await message.channel.send("Revisa tu chat privado ^_^")

async def besar(message):
    try:
        besar1 = message.content
        listabesar = list(besar1.split(" "))
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        if listabesar[2] == nombre2:
            await message.channel.send('¿Te besarás a tí mismo? O.o')
        elif listabesar[2] == "<@!806203127451615252>":
            await message.channel.send('Ejem... Aquí no, hay niños o///o')
        else:
            await message.channel.send('<@' + nombre1 + '> ha besado a ' + listabesar[2] + '! <3')
            await gifbeso(message)
    except:
        await message.channel.send('No seas burro. Tienes que mencionar a alguien ._.')



async def gifbeso(message):
    embed = discord.Embed(

        title="ThelVadam",
        color=discord.Colour.magenta()

    )
    linea = ""
    file = copen("besoimagen.txt")
    lines = file.count('\n')
    random_line = file.getline(randint(1, lines))
    linea = random_line
    print(linea)
    embed.set_image(url=linea)
    await message.channel.send(embed=embed)

async def desicionmeme(message):
    nombre1 = str(message.author.id)
    nombre2 = "<@" + nombre1 + ">"
    embed = discord.Embed(

        title="ThelVadam",
        color=discord.Colour.magenta()

    )
    linea = ""
    file = copen("memeimagen.txt")
    lines = file.count('\n')
    random_line = file.getline(randint(1, lines))
    linea = random_line
    print(linea)
    embed.set_image(url=linea)
    await message.channel.send(nombre2)
    await message.channel.send(embed=embed)

async def nederlands(message):
        nederlandslist = ["1","2","3","4","5","6","7","8","9","10","11","12"]
        desicionnl = ""
        desicionnl = random.choice(nederlandslist)
        if desicionnl == "1":
            await message.channel.send('Ik kan je beloven dit doet niet voor altijd pijn :3')
            desicionnl = "3"
        elif desicionnl == "2":
            await message.channel.send('Al voelt het onterecht maar het wordt beter met de tijd :3')
            desicionnl = random.choice(nederlandslist)
        elif desicionnl == "3":
            await message.channel.send('Ik ben blij dat je hier bent :)')
            desicionnl = random.choice(nederlandslist)
        elif desicionnl == "4":
            await message.channel.send('Het is een nacht, die je normaal aleen in films ziet...')
            desicionnl = "12"
        elif desicionnl == "5":
            await message.channel.send('De dag wordt de nacht en die wacht totdat jij weer schijnt :3')
            desicionnl = random.choice(nederlandslist)
        elif desicionnl == "10":
            await message.channel.send('Zoen me, voel me, morgenvroeg...')
            desicionnl = random.choice(nederlandslist)
        elif desicionnl == "7":
            await message.channel.send('Wat je vertelt houdt me nuchter en warm :3')
            desicionnl = random.choice(nederlandslist)
        elif desicionnl == "8":
            await message.channel.send('Maakte me toch al nooit uit waar we waren :3')
            desicionnl = random.choice(nederlandslist)
        elif desicionnl == "9":
            await message.channel.send('Je bent de mooiste vrouw in de wereld <3')
            desicionnl = random.choice(nederlandslist)
        elif desicionnl == "10":
            await message.channel.send('Ga je voor zilver of ga je voor goud?...')
            desicionnl = random.choice(nederlandslist)
        elif desicionnl == "11":
            await message.channel.send('Wat ik voor je voel is geen geheim <3')
            desicionnl = "9"
        elif desicionnl == "12":
            await message.channel.send('Ik hou van jou <3')
            desicionnl = random.choice(nederlandslist)
        else:
            await message.channel.send('Ik hou alleen nog maar van jou <3 :3')  
async def diversity(message):
    nombre1 = str(message.author.id)
    nombre2 = "<@" + nombre1 + ">"
    embed = discord.Embed(

        title="ThelVadam",
        color=discord.Colour.magenta(),

    )
    linea = ""
    file = copen("lgbtqplus.txt")
    lines = file.count('\n')
    random_line = file.getline(randint(1, lines))
    linea = random_line
    print(linea)
    embed.set_image(url=linea)
    embed.set_footer(text="Comando secreto 1/1")
    await message.channel.send(nombre2)
    await message.channel.send(embed=embed)

client.run(os.getenv('TOKEN'))