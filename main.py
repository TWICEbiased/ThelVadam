#ThelVadam, bot para Discord hecho por Memo Flores, v2.5

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
from discord.ext.commands import Bot
import asyncio
import datetime as dt
from linereader import copen
from keep_alive import keep_alive
import requests
from bs4 import BeautifulSoup
import urllib.request

keep_alive()
client = discord.Client()

@client.event
async def on_ready():
    intentos = 1
    atte = str(intentos)
    print('We hebben ingelogd als {0.user} na '.format(client) + atte + ' poging(en)')
    #message_channel = client.get_channel(805855767206166599)
    #await message_channel.send("¡Hola! :3.")
    await client.change_presence(activity=discord.Game(name="!tv ayuda"))
    print("Status één geselecteerd")
    print("Este software se encuentra licenciado bajo la GNU GPL v3")

            
@client.event
async def on_message(message): 
          
    if message.author == client.user:
        return
    mensaje1 = message.content
    listamensaje = list(mensaje1.split(" "))
    if "jueputa" in listamensaje:
        await groserias(message)
    elif "hijueputa" in listamensaje:
        nombre1 = str(message.author.id)
        await groserias(message)
    elif "gonorrea" in listamensaje:
        nombre1 = str(message.author.id)
        await groserias(message)
    elif "malparida" in listamensaje:
        nombre1 = str(message.author.id)
        await groserias(message)
    elif "malparido" in listamensaje:
        nombre1 = str(message.author.id)
        await groserias(message)
    elif "Jueputa" in listamensaje:
        nombre1 = str(message.author.id)
        await groserias(message)
    elif "Hijueputa" in listamensaje:
        nombre1 = str(message.author.id)
        await groserias(message)
    elif "ijueputa" in listamensaje:
        nombre1 = str(message.author.id)
        await groserias(message)
    elif "Ijueputa" in listamensaje:
        nombre1 = str(message.author.id)
        await groserias(message)
    elif "Malparido" in listamensaje:
        nombre1 = str(message.author.id)
        await groserias(message)
    elif "Malparida" in listamensaje:
        nombre1 = str(message.author.id)
        await groserias(message)
    elif "Gonorrea" in listamensaje:
        nombre1 = str(message.author.id)
        await groserias(message)
    elif "puto" in listamensaje:
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        if nombre2 == "<@!721920162005123142>":
            return
        else:
            await groserias(message)
    elif "Puto" in listamensaje:
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        if nombre2 == "<@!721920162005123142>":
            return
        else:
            await groserias(message)
    elif "puta" in listamensaje:
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        if nombre2 == "<@!721920162005123142>":
            return
        else:
            await groserias(message)
    elif "Puta" in listamensaje:
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        if nombre2 == "<@!721920162005123142>":
            return
        else:
            await groserias(message)
    elif "hijo de p" in listamensaje:
        await groserias(message)
    elif "Hijo de p" in listamensaje:
        await groserias(message)
    elif "Hija de p" in listamensaje:
        await groserias(message)
    elif "hija de p" in listamensaje:
        await groserias(message)
    elif "pt" in listamensaje:
        await groserias(message)
    elif "mierda" in listamensaje:
        await agresivo(message)
    elif "Mierda" in listamensaje:
        await agresivo(message)
    elif "mierd" in listamensaje:
        await agresivo(message)
    elif "Mierd" in listamensaje:
        await agresivo(message)
    elif "mrd" in listamensaje:
        await agresivo(message)
    elif "Mrd" in listamensaje:
        await agresivo(message)
    elif "fuck" in listamensaje:
        await groserias(message)
    elif "Fuck" in listamensaje:
        await groserias(message)
    elif "bullshit" in listamensaje:
        await groserias(message)
    elif "Bullshit" in listamensaje:
        await groserias(message)
    elif "bitch" in listamensaje:
        await groserias(message)
    elif "Bitch" in listamensaje:
        await groserias(message)
    elif "bitch?" in listamensaje:
        await groserias(message)
    elif "Bitch?" in listamensaje:
        await groserias(message)
    elif "qliao" in listamensaje:
        await groserias(message)
    elif "Qliao" in listamensaje:
        await groserias(message)
    elif "culiao" in listamensaje:
        await groserias(message)
    elif "Culiao" in listamensaje:
        await groserias(message)
    elif "perra" in listamensaje:
        await groserias(message)
    """elif "perro" in listamensaje:
        await groserias(message)
    elif "Perra" in listamensaje:
        await groserias(message)
    elif "Perro" in listamensaje:
        await groserias(message)
    elif "prra" in listamensaje:
        await groserias(message)
    elif "prro" in listamensaje:
        await groserias(message)
    elif "Prra" in listamensaje:
        await groserias(message)
    elif "Prro" in listamensaje:
        await groserias(message)"""
    if "mk" in listamensaje:
        await groserias(message)
    elif "Mk" in listamensaje:
        await groserias(message)
    elif ":regional_indicator_h:ijueputa" in listamensaje:
        await groserias(message)
    elif "<@&788840600640290849>" in listamensaje:
            nombre1 = str(message.author.id)
            nombre2 = "<@!" + nombre1 + ">"
            if nombre2 == "<@!721920162005123142>":
                return
            if nombre2 == "<@!757406459167244288>":
                return
            elif nombre2 == "<@!758192182389375006>":
                return
            elif nombre2 == "<@!734412668789850172>":
                return
            elif nombre2 == "<@!656335364256169996>":
                return
            else:
                await repormiembros(message)
    """if message.content.startswith('hola'):
        nombre1 = str(message.author.id)
        await message.channel.send(' ¡Hola,  <@' + nombre1 + '>! ¿Qué tal te va?')
    elif message.content.startswith('Hola Bien Y Tu? :D'):
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
        await message.channel.send('¡Buen día, <@' + nombre1 + '>! No olvides cuidarte de la infección del flood :3')"""
    if message.content.startswith("no te pregun"):
        await agresivo(message)
    elif message.content.startswith("No te pregun"):
        await agresivo(message)
    elif message.content.startswith("no le pregun"):
        await agresivo(message)
    elif message.content.startswith("No le pregun"):
        await agresivo(message)
    elif message.content.startswith("no me interesa"):
        await agresivo(message)
    elif message.content.startswith("No me interesa"):
        await agresivo(message)
    elif message.content.startswith("chinga tu"):
        await agresivo(message)
    elif message.content.startswith("Chinga tu"):
        await agresivo(message)
    elif message.content.startswith("chingas a tu"):
        await agresivo(message)
    elif message.content.startswith("Chingas a tu"):
        await agresivo(message)
    elif message.content.startswith("chinga a tu"):
        await agresivo(message)
    elif message.content.startswith("Chinga a tu"):
        await agresivo(message)
    elif message.content.startswith("tu put"):
        await agresivo(message)
    elif message.content.startswith("Tu put"):
        await agresivo(message)
    elif message.content.startswith("tu pinc"):
        await agresivo(message)
    elif message.content.startswith("Tu pinc"):
        await agresivo(message)
    elif message.content.startswith("tu col"):
        await agresivo(message)
    elif message.content.startswith("Tu col"):
        await agresivo(message)
    elif message.content.startswith("tu cul"):
        await agresivo(message)
    elif message.content.startswith("Tu cul"):
        await agresivo(message)
    elif message.content.startswith("callese"):
        await agresivo(message)
    elif message.content.startswith("Callese"):
        await agresivo(message)
    elif message.content.startswith("calle"):
        await agresivo(message)
    elif message.content.startswith("Calle"):
        await agresivo(message)
    elif message.content.startswith("calla"):
        await agresivo(message)
    elif message.content.startswith("Calla"):
        await agresivo(message)
    elif message.content.startswith("Callate"):
        await agresivo(message)
    elif message.content.startswith("callate"):
        await agresivo(message)
    elif message.content.startswith("se calla"):
        await agresivo(message)
    elif message.content.startswith("Se calla"):
        await agresivo(message)
    elif message.content.startswith("te callas"):
        await agresivo(message)
    elif message.content.startswith("Te callas"):
        await agresivo(message)
    elif message.content.startswith('que hora es'):
        await timehora(message)
    elif message.content.startswith('qué hora es'):
        await timehora(message)
    elif message.content.startswith('que hora son'):
        await timehora(message)
    elif message.content.startswith('qué hora son'):
        await timehora(message)
    elif message.content.startswith('Que hora es'):
        await timehora(message)
    elif message.content.startswith('Qué hora es'):
        await timehora(message)
    elif message.content.startswith('Que hora son'):
        await timehora(message)
    elif message.content.startswith('Qué hora son'):
        await timehora(message)
    elif message.content.startswith('!tv ayuda'):
        await ayuda(message)
    elif message.content.startswith('!tv help'):
        await ayuda(message)
    canal = str(message.channel.id)
    if message.content.startswith('!tv me ama'):
        if canal == "815063141741363230":
            await desicionamor(message)
        else:
            await bots(message)
    elif message.content.startswith('!tv es pendejo'):
        if canal == "815063141741363230":
            await desicionpendejo(message)
        else:
            await bots(message)
    elif message.content.startswith('!tv es pendeja'):
        if canal == "815063141741363230":
            await desicionpendejo(message)
        else:
            await bots(message)
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
    elif message.content.startswith('!tv status 1'):
            nombre1 = str(message.author.id)
            nombre2 = "<@!" + nombre1 + ">"
            if nombre2 == "<@!721920162005123142>":
                await client.change_presence(activity=discord.Game(name="!tv ayuda"))
                await message.channel.send('Estado #1 establecido')
            else:
                await message.channel.send('Lo siento, no tienes permiso para ejecutar este comando ^_^')
    elif message.content.startswith('!tv status 2'):
            nombre1 = str(message.author.id)
            nombre2 = "<@!" + nombre1 + ">"
            if nombre2 == "<@!721920162005123142>":
                await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="ayuda"))
                await message.channel.send('Estado #2 establecido')
            else:
                await message.channel.send('Lo siento, no tienes permiso para ejecutar este comando ^_^')

    elif message.content.startswith('!tv status 3'):
            nombre1 = str(message.author.id)
            nombre2 = "<@!" + nombre1 + ">"
            if nombre2 == "<@!721920162005123142>":
                await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a quién ayudar :3"))
                await message.channel.send('Estado #3 establecido')
            else:
                await message.channel.send('Lo siento, no tienes permiso para ejecutar este comando ^_^')
            
    elif message.content.startswith('!tv noticia'):
            # the target we want to open     
            url='https://www.3djuegos.com/n3/1058/0/halo/'
          
            #open with GET method 
            resp=requests.get(url) 
          
            #http_respone 200 means OK status 
            if resp.status_code==200: 
                print("Successfully opened the web page") 
          
                # we need a parser,Python built-in HTML parser is enough . 
                soup=BeautifulSoup(resp.text,'html.parser')     
      
                # l is the list which contains all the text i.e news  
                l=soup.find("div",{"class":"s4 c3"}) 
          
                #now we want to print only the text part of the anchor. 
                #find all the elements of a, i.e anchor 
                nott = soup.find_all('article') 
                noticion = str(nott[0].text)
                listanot = list(noticion.split("Leer más »"))
                noticiota = str(listanot[0])
                if "Leer más »" in listanot:
                    listanot.remove("Leer más »")

                  #f = open("noticia.txt","w")
                  #f.write(noticiota)
            else: 
                print("Error") 

            await message.delete()

            embed = discord.Embed(

                title="Noticia semanal de HALO",
                description=noticiota,
                color=discord.Colour.magenta()
                  
              )
            await message.channel.send(embed=embed)

    elif message.content.startswith('wat ben ik'):
                nombre1 = str(message.author.id)
                nombre2 = "<@!" + nombre1 + ">"
                if nombre2 == "<@!721920162005123142>":
                    await message.channel.send('Je bent een mooie vrouw :3')
                else:
                    await message.channel.send('Lo siento, no tienes permiso para ejecutar este comando ^_^')

    elif message.content.startswith('!tv beso'):
        if canal == "815063141741363230":
            await besar(message)
        else:
            await bots(message)
    elif message.content.startswith('!tv besar'):
        if canal == "815063141741363230":
            await besar(message)
        else:
            await bots(message)
    elif message.content.startswith('!tv kiss'):
        if canal == "815063141741363230":
            await besar(message)
        else:
            await bots(message)
    elif message.content.startswith('inquisidor sabe dar masajes en los pies'):
            await message.channel.send('Recuerdo cuando mi pelotón me preguntaba eso cuando nuestra misión era cazar al Líder Hereje. Era asqueroso, pero daba sensación de fraternidad.')
    elif message.content.startswith('Inquisidor sabe dar masajes en los pies'):
            await message.channel.send('Recuerdo cuando mi pelotón me preguntaba eso cuando nuestra misión era cazar al Líder Hereje. Era asqueroso, pero daba sensación de fraternidad.')
    elif message.content.startswith('!tv meme'):
        if canal == "815063141741363230":
            await desicionmeme(message)
        elif canal == "788838176281985104":
            await desicionmeme(message)
        else:
            await botmeme(message)
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
        if canal == "815063141741363230":
            await message.delete()
            await diversity(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv diversidad"):
        if canal == "815063141741363230":
            await message.delete()
            await diversity(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv lgbt"):
        if canal == "815063141741363230":
            await message.delete()
            await diversity(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv lgtb"):
        if canal == "815063141741363230":
            await message.delete()
            await message.channel.send('La B va antes de la T :3.')
        else:
            await bots(message)
    elif message.content.startswith("!tv LGBT"):
        if canal == "815063141741363230":
            await message.delete()
            await diversity(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv LGTB"):
        if canal == "815063141741363230":
            await message.delete()
            await message.channel.send('La B va antes de la T :3.')
        else:
            await bots(message)
    elif message.content.startswith("!tv horoscopo"):
        if canal == "815063141741363230":
            await horoscopo(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv horóscopo"):
        if canal == "815063141741363230":
            await horoscopo(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv autobiografia"):
            await auto1(message)
    elif message.content.startswith("!tv autobiografía"):
            await auto1(message)
    elif message.content.startswith("!tv sobreti"):
        if canal == "815063141741363230":
            await sobremi(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv warthog"):
        if canal == "815063141741363230":
            await espachurrar(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv ghost"):
        if canal == "815063141741363230":
            await espachurrar(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv run"):
        if canal == "815063141741363230":
            await espachurrar(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv espachurrar"):
        if canal == "815063141741363230":
            await espachurrar(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv kill"):
        if canal == "815063141741363230":
            await matar(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv matar"):
        if canal == "815063141741363230":
            await matar(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv scorpion"):
        if canal == "815063141741363230":
            await scorpion(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv tank"):
        if canal == "815063141741363230":
            await scorpion(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv tanque"):
        if canal == "815063141741363230":
            await scorpion(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv sniper"):
        if canal == "815063141741363230":
            await sniper(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv snipe"):
        if canal == "815063141741363230":
            await sniper(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv teabag"):
        if canal == "815063141741363230":
            await teabag(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv banshee"):
        if canal == "815063141741363230":
            await banshee(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv nade"):
        if canal == "815063141741363230":
            await granada(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv 8ball"):
        if canal == "815063141741363230":
            await ball(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv bola8"):
        if canal == "815063141741363230":
            await bola8(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv bolaocho"):
        if canal == "815063141741363230":
            await bolaocho(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv bolanegra"):
        if canal == "815063141741363230":
            await bolanegra(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv pregúnta"):
        if canal == "815063141741363230":
            await question(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv pregunta"):
        if canal == "815063141741363230":
            await pregunta(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv question"):
        if canal == "815063141741363230":
            await question2(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv espada"):
        if canal == "815063141741363230":
            await espada(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv sword"):
        if canal == "815063141741363230":
            await espada(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv escopada"):
        if canal == "815063141741363230":
            await espada(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv 8 ball"):
        if canal == "815063141741363230":
            await message.channel.send("Mira we, si no quieres que explote como lo hizo 343 Guilty Spark, pon 8ball, no 8 ball.")
        else:
            await bots(message)
    elif message.content.startswith("!tv encuesta"):
            await encuesta(message)
    elif message.content.startswith("!tv poll"):
            await poll(message)
    elif message.content.startswith("!tv update"):
            nombre1 = str(message.author.id)
            nombre2 = "<@!" + nombre1 + ">"
            if nombre2 == "<@!721920162005123142>":
                await update(message)
            else:
                await message.channel.send('Lo siento, no tienes permiso para ejecutar este comando ^_^')
    elif message.content.startswith("!tv avatar"):
        if canal == "815063141741363230":
            await avatar(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv foto"):
        if canal == "815063141741363230":
            await avatar(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv confesion"):
        if canal == "815063141741363230":
            await confesion(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv confession"):
        if canal == "815063141741363230":
            await confession(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv confesión"):
        if canal == "815063141741363230":
            await confesionn(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv equipo"):
        if canal == "815063141741363230":
            await equipo(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv team"):
        if canal == "815063141741363230":
            await equipo(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv peek"):
        if canal == "815063141741363230":
            await espiar(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv espiar"):
        if canal == "815063141741363230":
            await espiar(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv apuntar"):
        if canal == "815063141741363230":
            await espiar(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv wraith"):
        if canal == "815063141741363230":
            await wraith(message)
        else:
            await bots(message)  
    elif message.content.startswith("!tv warith"):
        if canal == "815063141741363230":
            await wraith(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv wairth"):
        if canal == "815063141741363230":
            await wraith(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv wrait"):
        if canal == "815063141741363230":
            await wraith(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv wraih"):
        if canal == "815063141741363230":
            await wraith(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv scorpion covenant"):
        if canal == "815063141741363230":
            await wraith(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv covenant scorpion"):
        if canal == "815063141741363230":
            await wraith(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv covenant tank"):
        if canal == "815063141741363230":
            await wraith(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv tanque covenant"):
        if canal == "815063141741363230":
            await wraith(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv covenant tanq"):
        if canal == "815063141741363230":
            await wraith(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv scarab"):
        if canal == "815063141741363230":
            await message.channel.send("Ya quisieras poder manejar un scarab XD.")
        else:
            await bots(message)
    elif message.content.startswith("!tv rocket"):
        if canal == "815063141741363230":
            await rocket(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv rox"):
        if canal == "815063141741363230":
            await rocket(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv cohete"):
        if canal == "815063141741363230":
            await rocket(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv bazuca"):
        if canal == "815063141741363230":
            await rocket(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv basuca"):
        if canal == "815063141741363230":
            await rocket(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv lanzacohete"):
        if canal == "815063141741363230":
            await rocket(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv lanza coh"):
        if canal == "815063141741363230":
            await message.channel.send("Escribe 'Lanzacohetes', no 'Lanza cohetes' que me la pones difícil pelotudo.")
        else:
            await bots(message)
    elif message.content.startswith("ch!"):
        if canal == "815063141741363230":
            return
        elif canal == "788838176281985104":
            return
        else:
            await asyncio.sleep(1)
            await message.channel.purge(limit=1)
            await bots(message)
    elif message.content.startswith("$chnick"):
            await asyncio.sleep(1)
            await message.delete()
    elif message.content.startswith("!tv del"):
            delt1 = message.content
            listadel = list(delt1.split(" "))
            n = int(listadel[2])         
            await message.channel.purge(limit=n)
    elif message.content.startswith("!tv feedback"):
        if canal == "815063141741363230":
            await feedback(message)
        else:
            await bots(message)
    elif message.content.startswith("!tv mejo"):
            nombre1 = str(message.author.id)
            nombre2 = "<@!" + nombre1 + ">"
            if nombre2 == "<@!721920162005123142>":
                await mejoden(message)
            else:
                await message.channel.send('No tienes permiso para ejecutar este comando.')
    elif message.content.startswith("!tv jodbot"):
            nombre1 = str(message.author.id)
            nombre2 = "<@!" + nombre1 + ">"
            if nombre2 == "<@!721920162005123142>":
                await jodbot(message)
            else:
                await message.channel.send('No tienes permiso para ejecutar este comando.') 

async def timehora(message):

    hora = time.strftime("%H:%M:%S")
    await message.channel.send('Son las ' + hora)

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
            await message.channel.send('No ¬¬. ' + listaamor[3] + ' no tiene sentimientos >:(')
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
            await message.channel.send('Yo les pago la boda pts. <@' + nombre1 + '>' + ' + ' + listaamor[3])
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
        file = copen("pendejo.txt")
        lines = file.count('\n')
        random_line = file.getline(randint(1, lines))
        linea = random_line
        await message.channel.send(linea)
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
    embed.set_footer(text="v2.5")
    await message.author.send(embed = embed)
    await message.channel.send("Revisa tu chat privado ^_^")

async def besar(message):
    try:
        besar1 = message.content
        listabesar = list(besar1.split(" "))
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        nombre3 = "<@" + nombre1 + ">"
        if listabesar[2] == nombre2:
            await message.channel.send('¿Te besarás a tí mismo? O.o')
        elif listabesar[2] == nombre3:
            await message.channel.send('¿Te besarás a tí mismo? O.o')
        elif listabesar[2] == "<@!813874482182619166>":
            await message.channel.send('Ejem... Aquí no, hay niños o///o')
        elif listabesar[2] == "<@813874482182619166>":
            await message.channel.send('Ejem... Aquí no, hay niños o///o')
        else:
            await message.channel.send('<@' + nombre1 + '> ha besado a ' + listabesar[2] + '! :revolving_hearts:')
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
    embed.set_footer(text="Comando secreto 1/5")
    await message.channel.send(nombre2)
    await message.channel.send(embed=embed)

async def horoscopo(message):
    try:
        horosc = message.content
        listahorosc = list(horosc.split(" "))
        if  "aries" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open     
            url='https://www.msn.com/es-mx/estilo-de-vida/horoscopos/aries-hor%C3%B3scopo-diario-gratis/ar-AAyQCeq/'
      
            #open with GET method 
            resp=requests.get(url) 
      
            #http_respone 200 means OK status 
            if resp.status_code==200: 
                print("Successfully opened the web page") 
      
                # we need a parser,Python built-in HTML parser is enough . 
                soup=BeautifulSoup(resp.text,'html.parser')     
  
                hor = soup.find_all('p') 
                hors = str(hor[0].text)


            else: 
                print("Error")

        elif  "Aries" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open     
            url='https://www.msn.com/es-mx/estilo-de-vida/horoscopos/aries-hor%C3%B3scopo-diario-gratis/ar-AAyQCeq/'
      
            #open with GET method 
            resp=requests.get(url) 
      
            #http_respone 200 means OK status 
            if resp.status_code==200: 
                print("Successfully opened the web page") 
      
                # we need a parser,Python built-in HTML parser is enough . 
                soup=BeautifulSoup(resp.text,'html.parser')     
  
                hor = soup.find_all('p') 
                hors = str(hor[0].text)


            else: 
                print("Error")

        elif  "tauro" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open     
            url='https://www.msn.com/es-mx/estilo-de-vida/horoscopos/tauro-hor%C3%B3scopo-diario-gratis/ar-AAyQHkq'
      
            #open with GET method 
            resp=requests.get(url) 
      
            #http_respone 200 means OK status 
            if resp.status_code==200: 
                print("Successfully opened the web page") 
      
                # we need a parser,Python built-in HTML parser is enough . 
                soup=BeautifulSoup(resp.text,'html.parser')     
  
                hor = soup.find_all('p') 
                hors = str(hor[0].text)


            else: 
                print("Error")

        elif  "Tauro" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open     
            url='https://www.msn.com/es-mx/estilo-de-vida/horoscopos/tauro-hor%C3%B3scopo-diario-gratis/ar-AAyQHkq'
      
            #open with GET method 
            resp=requests.get(url) 
      
            #http_respone 200 means OK status 
            if resp.status_code==200: 
                print("Successfully opened the web page") 
      
                # we need a parser,Python built-in HTML parser is enough . 
                soup=BeautifulSoup(resp.text,'html.parser')     
  
                hor = soup.find_all('p') 
                hors = str(hor[0].text)


            else: 
                print("Error")

        elif  "geminis" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open     
            url='https://www.msn.com/es-mx/estilo-de-vida/horoscopos/g%C3%A9minis-hor%C3%B3scopo-diario-gratis/ar-AAyQM8E'
      
            #open with GET method 
            resp=requests.get(url) 
      
            #http_respone 200 means OK status 
            if resp.status_code==200: 
                print("Successfully opened the web page") 
      
                # we need a parser,Python built-in HTML parser is enough . 
                soup=BeautifulSoup(resp.text,'html.parser')     
  
                hor = soup.find_all('p') 
                hors = str(hor[0].text)


            else: 
                print("Error")

        elif  "Geminis" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open     
            url='https://www.msn.com/es-mx/estilo-de-vida/horoscopos/g%C3%A9minis-hor%C3%B3scopo-diario-gratis/ar-AAyQM8E'
      
            #open with GET method 
            resp=requests.get(url) 
      
            #http_respone 200 means OK status 
            if resp.status_code==200: 
                print("Successfully opened the web page") 
      
                # we need a parser,Python built-in HTML parser is enough . 
                soup=BeautifulSoup(resp.text,'html.parser')     
  
                hor = soup.find_all('p') 
                hors = str(hor[0].text)


            else: 
                print("Error")

        elif  "géminis" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open     
            url='https://www.msn.com/es-mx/estilo-de-vida/horoscopos/g%C3%A9minis-hor%C3%B3scopo-diario-gratis/ar-AAyQM8E'
      
            #open with GET method 
            resp=requests.get(url) 
      
            #http_respone 200 means OK status 
            if resp.status_code==200: 
                print("Successfully opened the web page") 
      
                # we need a parser,Python built-in HTML parser is enough . 
                soup=BeautifulSoup(resp.text,'html.parser')     
  
                hor = soup.find_all('p') 
                hors = str(hor[0].text)


            else: 
                print("Error")

        elif  "Géminis" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open     
            url='https://www.msn.com/es-mx/estilo-de-vida/horoscopos/g%C3%A9minis-hor%C3%B3scopo-diario-gratis/ar-AAyQM8E'
      
            #open with GET method 
            resp=requests.get(url) 
      
            #http_respone 200 means OK status 
            if resp.status_code==200: 
                print("Successfully opened the web page") 
      
                # we need a parser,Python built-in HTML parser is enough . 
                soup=BeautifulSoup(resp.text,'html.parser')     
  
                hor = soup.find_all('p') 
                hors = str(hor[0].text)


            else: 
                print("Error")

        elif  "cancer" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open     
            url='https://www.msn.com/es-mx/estilo-de-vida/horoscopos/c%C3%A1ncer-hor%C3%B3scopo-diario-gratis/ar-AAyQvc6'
      
            #open with GET method 
            resp=requests.get(url) 
      
            #http_respone 200 means OK status 
            if resp.status_code==200: 
                print("Successfully opened the web page") 
      
                # we need a parser,Python built-in HTML parser is enough . 
                soup=BeautifulSoup(resp.text,'html.parser')     
  
                hor = soup.find_all('p') 
                hors = str(hor[0].text)


            else: 
                print("Error")

        elif  "Cancer" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open     
            url='https://www.msn.com/es-mx/estilo-de-vida/horoscopos/c%C3%A1ncer-hor%C3%B3scopo-diario-gratis/ar-AAyQvc6'
      
            #open with GET method 
            resp=requests.get(url) 
      
            #http_respone 200 means OK status 
            if resp.status_code==200: 
                print("Successfully opened the web page") 
      
                # we need a parser,Python built-in HTML parser is enough . 
                soup=BeautifulSoup(resp.text,'html.parser')     
  
                hor = soup.find_all('p') 
                hors = str(hor[0].text)


            else: 
                print("Error")

        elif  "cáncer" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open     
            url='https://www.msn.com/es-mx/estilo-de-vida/horoscopos/c%C3%A1ncer-hor%C3%B3scopo-diario-gratis/ar-AAyQvc6'
      
            #open with GET method 
            resp=requests.get(url) 
      
            #http_respone 200 means OK status 
            if resp.status_code==200: 
                print("Successfully opened the web page") 
      
                # we need a parser,Python built-in HTML parser is enough . 
                soup=BeautifulSoup(resp.text,'html.parser')     
  
                hor = soup.find_all('p') 
                hors = str(hor[0].text)


            else: 
                print("Error")

        elif  "Cáncer" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open     
            url='https://www.msn.com/es-mx/estilo-de-vida/horoscopos/c%C3%A1ncer-hor%C3%B3scopo-diario-gratis/ar-AAyQvc6'
      
            #open with GET method 
            resp=requests.get(url) 
      
            #http_respone 200 means OK status 
            if resp.status_code==200: 
                print("Successfully opened the web page") 
      
                # we need a parser,Python built-in HTML parser is enough . 
                soup=BeautifulSoup(resp.text,'html.parser')     
  
                hor = soup.find_all('p') 
                hors = str(hor[0].text)


            else: 
                print("Error")

        elif  "leo" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open     
            url='https://www.msn.com/es-mx/estilo-de-vida/horoscopos/leo-hor%C3%B3scopo-diario-gratis/ar-AAyQEMt'
      
            #open with GET method 
            resp=requests.get(url) 
      
            #http_respone 200 means OK status 
            if resp.status_code==200: 
                print("Successfully opened the web page") 
      
                # we need a parser,Python built-in HTML parser is enough . 
                soup=BeautifulSoup(resp.text,'html.parser')     
  
                hor = soup.find_all('p') 
                hors = str(hor[0].text)


            else: 
                print("Error")

        elif  "Leo" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open     
            url='https://www.msn.com/es-mx/estilo-de-vida/horoscopos/leo-hor%C3%B3scopo-diario-gratis/ar-AAyQEMt'
      
            #open with GET method 
            resp=requests.get(url) 
      
            #http_respone 200 means OK status 
            if resp.status_code==200: 
                print("Successfully opened the web page") 
      
                # we need a parser,Python built-in HTML parser is enough . 
                soup=BeautifulSoup(resp.text,'html.parser')     
  
                hor = soup.find_all('p') 
                hors = str(hor[0].text)


            else: 
                print("Error")

        elif  "virgo" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open     
            url='https://www.msn.com/es-mx/estilo-de-vida/horoscopos/virgo-hor%C3%B3scopo-diario-gratis/ar-AAyQEMw'
      
            #open with GET method 
            resp=requests.get(url) 
      
            #http_respone 200 means OK status 
            if resp.status_code==200: 
                print("Successfully opened the web page") 
      
                # we need a parser,Python built-in HTML parser is enough . 
                soup=BeautifulSoup(resp.text,'html.parser')     
  
                hor = soup.find_all('p') 
                hors = str(hor[0].text)


            else: 
                print("Error")

        elif  "Virgo" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open     
            url='https://www.msn.com/es-mx/estilo-de-vida/horoscopos/virgo-hor%C3%B3scopo-diario-gratis/ar-AAyQEMw'
      
            #open with GET method 
            resp=requests.get(url) 
      
            #http_respone 200 means OK status 
            if resp.status_code==200: 
                print("Successfully opened the web page") 
      
                # we need a parser,Python built-in HTML parser is enough . 
                soup=BeautifulSoup(resp.text,'html.parser')     
  
                hor = soup.find_all('p') 
                hors = str(hor[0].text)


            else: 
                print("Error")

        elif  "libra" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open     
            url='https://www.msn.com/es-mx/estilo-de-vida/horoscopos/libra-hor%C3%B3scopo-diario-gratis/ar-AAyQEMC'
      
            #open with GET method 
            resp=requests.get(url) 
      
            #http_respone 200 means OK status 
            if resp.status_code==200: 
                print("Successfully opened the web page") 
      
                # we need a parser,Python built-in HTML parser is enough . 
                soup=BeautifulSoup(resp.text,'html.parser')     
  
                hor = soup.find_all('p') 
                hors = str(hor[0].text)


            else: 
                print("Error")

        elif  "Libra" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open     
            url='https://www.msn.com/es-mx/estilo-de-vida/horoscopos/libra-hor%C3%B3scopo-diario-gratis/ar-AAyQEMC'
      
            #open with GET method 
            resp=requests.get(url) 
      
            #http_respone 200 means OK status 
            if resp.status_code==200: 
                print("Successfully opened the web page") 
      
                # we need a parser,Python built-in HTML parser is enough . 
                soup=BeautifulSoup(resp.text,'html.parser')     
  
                hor = soup.find_all('p') 
                hors = str(hor[0].text)


            else: 
                print("Error")

        elif  "escorpio" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open     
            url='https://www.msn.com/es-mx/estilo-de-vida/horoscopos/escorpio-hor%C3%B3scopo-diario-gratis/ar-AAyQJBT'
      
            #open with GET method 
            resp=requests.get(url) 
      
            #http_respone 200 means OK status 
            if resp.status_code==200: 
                print("Successfully opened the web page") 
      
                # we need a parser,Python built-in HTML parser is enough . 
                soup=BeautifulSoup(resp.text,'html.parser')     
  
                hor = soup.find_all('p') 
                hors = str(hor[0].text)


            else: 
                print("Error")

        elif  "Escorpio" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open     
            url='https://www.msn.com/es-mx/estilo-de-vida/horoscopos/escorpio-hor%C3%B3scopo-diario-gratis/ar-AAyQJBT'
      
            #open with GET method 
            resp=requests.get(url) 
      
            #http_respone 200 means OK status 
            if resp.status_code==200: 
                print("Successfully opened the web page") 
      
                # we need a parser,Python built-in HTML parser is enough . 
                soup=BeautifulSoup(resp.text,'html.parser')     
  
                hor = soup.find_all('p') 
                hors = str(hor[0].text)


            else: 
                print("Error")

        elif  "sagitario" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open     
            url='https://www.msn.com/es-mx/estilo-de-vida/horoscopos/sagitario-hor%C3%B3scopo-diario-gratis/ar-AAyQQQv'
      
            #open with GET method 
            resp=requests.get(url) 
      
            #http_respone 200 means OK status 
            if resp.status_code==200: 
                print("Successfully opened the web page") 
      
                # we need a parser,Python built-in HTML parser is enough . 
                soup=BeautifulSoup(resp.text,'html.parser')     
  
                hor = soup.find_all('p') 
                hors = str(hor[0].text)


            else: 
                print("Error")

        elif  "Sagitario" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open     
            url='https://www.msn.com/es-mx/estilo-de-vida/horoscopos/sagitario-hor%C3%B3scopo-diario-gratis/ar-AAyQQQv'
      
            #open with GET method 
            resp=requests.get(url) 
      
            #http_respone 200 means OK status 
            if resp.status_code==200: 
                print("Successfully opened the web page") 
      
                # we need a parser,Python built-in HTML parser is enough . 
                soup=BeautifulSoup(resp.text,'html.parser')     
  
                hor = soup.find_all('p') 
                hors = str(hor[0].text)


            else: 
                print("Error")

        elif  "capricornio" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open     
            url='https://www.msn.com/es-mx/estilo-de-vida/horoscopos/capricornio-hor%C3%B3scopo-diario-gratis/ar-AAyQHkM'
      
            #open with GET method 
            resp=requests.get(url) 
      
            #http_respone 200 means OK status 
            if resp.status_code==200: 
                print("Successfully opened the web page") 
      
                # we need a parser,Python built-in HTML parser is enough . 
                soup=BeautifulSoup(resp.text,'html.parser')     
  
                hor = soup.find_all('p') 
                hors = str(hor[0].text)


            else: 
                print("Error")

        elif  "Capricornio" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open     
            url='https://www.msn.com/es-mx/estilo-de-vida/horoscopos/capricornio-hor%C3%B3scopo-diario-gratis/ar-AAyQHkM'
      
            #open with GET method 
            resp=requests.get(url) 
      
            #http_respone 200 means OK status 
            if resp.status_code==200: 
                print("Successfully opened the web page") 
      
                # we need a parser,Python built-in HTML parser is enough . 
                soup=BeautifulSoup(resp.text,'html.parser')     
  
                hor = soup.find_all('p') 
                hors = str(hor[0].text)


            else: 
                print("Error")

        elif  "acuario" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open     
            url='https://www.msn.com/es-mx/estilo-de-vida/horoscopos/acuario-hor%C3%B3scopo-diario-gratis/ar-AAyQwZ9'
      
            #open with GET method 
            resp=requests.get(url) 
      
            #http_respone 200 means OK status 
            if resp.status_code==200: 
                print("Successfully opened the web page") 
      
                # we need a parser,Python built-in HTML parser is enough . 
                soup=BeautifulSoup(resp.text,'html.parser')     
  
                hor = soup.find_all('p') 
                hors = str(hor[0].text)


            else: 
                print("Error")

        elif  "Acuario" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open     
            url='https://www.msn.com/es-mx/estilo-de-vida/horoscopos/acuario-hor%C3%B3scopo-diario-gratis/ar-AAyQwZ9'
      
            #open with GET method 
            resp=requests.get(url) 
      
            #http_respone 200 means OK status 
            if resp.status_code==200: 
                print("Successfully opened the web page") 
      
                # we need a parser,Python built-in HTML parser is enough . 
                soup=BeautifulSoup(resp.text,'html.parser')     
  
                hor = soup.find_all('p') 
                hors = str(hor[0].text)


            else: 
                print("Error")

        elif  "piscis" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open     
            url='https://www.msn.com/es-mx/estilo-de-vida/horoscopos/piscis-hor%C3%B3scopo-diario-gratis/ar-AAyQvcC'
      
            #open with GET method 
            resp=requests.get(url) 
      
            #http_respone 200 means OK status 
            if resp.status_code==200: 
                print("Successfully opened the web page") 
      
                # we need a parser,Python built-in HTML parser is enough . 
                soup=BeautifulSoup(resp.text,'html.parser')     
  
                hor = soup.find_all('p') 
                hors = str(hor[0].text)


            else: 
                print("Error")

        elif  "Piscis" in listahorosc:
            tuhoroscopo = str(listahorosc[2])
            horsemanal = "Horóscopo diario para " + tuhoroscopo
            # the target we want to open     
            url='https://www.msn.com/es-mx/estilo-de-vida/horoscopos/piscis-hor%C3%B3scopo-diario-gratis/ar-AAyQvcC'
      
            #open with GET method 
            resp=requests.get(url) 
      
            #http_respone 200 means OK status 
            if resp.status_code==200: 
                print("Successfully opened the web page") 
      
                # we need a parser,Python built-in HTML parser is enough . 
                soup=BeautifulSoup(resp.text,'html.parser')     
  
                hor = soup.find_all('p') 
                hors = str(hor[0].text)


            else: 
                print("Error")
    
        else:
            await message.delete()
            await message.channel.send("Hmm... Creo que lo escribiste mal, revisa por favor :3.")

        embed = discord.Embed(

            title=horsemanal,
            description=hors,
            color=discord.Colour.magenta()
              
        )          
        piehor = "Más información en: " + url
        embed.set_footer(text="Comando secreto 3/5.")
        await message.author.send(embed=embed)
        await message.author.send(piehor)
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        await message.delete()
        await message.channel.send("Revisa tu chat privado uwu, " + nombre2 + ". Comando secreto 3/5.")

    
    except:
        await message.delete()
        await message.channel.send("Escribiste mal el comando, a ver si descubres la forma correcta XD.")

async def auto1(message):
    handler = open('auto1.txt')
    autobio1 = handler.read()
    embed = discord.Embed(

        title="Biografía de ThelVadam",
        description=autobio1,
        color=discord.Colour.random()

    )
    #message_channel = client.get_channel(803850947734011925)
    await message.channel.send(embed = embed)
  
async def sobremi(message):

    await message.channel.send("Revisa tu chat privado :3. Comando secreto 4/5.")
    handler = open('sobrethel.txt')
    sobrethel = handler.read()
    embed = discord.Embed(

        title="Sobre ThelVadam",
        description=sobrethel,
        color=discord.Colour.random()

    )
    #message_channel = client.get_channel(803850947734011925)
    await message.author.send(embed = embed)
    await message.delete()

async def espachurrar(message):
    try:
        espa1 = message.content
        listaespa = list(espa1.split(" "))
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        nombre3 = "<@" + nombre1 + ">"
        if listaespa[2] == nombre2:
            await message.channel.send('¿Te espachurarrás a tí mismo? O.o')
        elif listaespa[2] == nombre3:
            await message.channel.send('¿Te espachurarrás a tí mismo? O.o')
        elif listaespa[2] == "<@!813874482182619166>":
            await message.channel.send('Ejem... Mejor no lo haga compa, si no quiere salir volando hasta Paraguay (que por cierto no existe XD)')
        elif listaespa[2] == "<@813874482182619166>":
            await message.channel.send('Ejem... Mejor no lo haga compa, si no quiere salir volando hasta Paraguay (que por cierto no existe XD)')
        else:
            await message.channel.send('<@' + nombre1 + '> ha espachurrado a ' + listaespa[2] + '! O.o')
            await gifespa(message)
    except:
        await message.channel.send('No seas burro. Tienes que mencionar a alguien ._.')

async def gifespa(message):
    embed = discord.Embed(

        title="ThelVadam",
        color=discord.Colour.random()

    )
    linea = ""
    file = copen("espachimagen.txt")
    lines = file.count('\n')
    random_line = file.getline(randint(1, lines))
    linea = random_line
    print(linea)
    embed.set_image(url=linea)
    await message.channel.send(embed=embed)    

async def matar(message):
    try:
        mat1 = message.content
        listamatar = list(mat1.split(" "))
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        nombre3 = "<@" + nombre1 + ">"
        if listamatar[2] == nombre2:
            await message.channel.send('No compa no lo haga, el suic1dio nunca es la opción, tiene muchas razones para vivir :c')
        if listamatar[2] == nombre3:
            await message.channel.send('No compa no lo haga, el suic1dio nunca es la opción, tiene muchas razones para vivir :c')
        elif listamatar[2] == "<@!813874482182619166>":
            await message.channel.send('Acércate pt, vas a ver que te hago caca en 2 segundos...')
        elif listamatar[2] == "<@813874482182619166>":
            await message.channel.send('Acércate pt, vas a ver que te hago caca en 2 segundos...')
        else:
            await message.channel.send('<@' + nombre1 + '> le dio en su maiz a ' + listamatar[2] + '! D:')
            await gifmat(message)
    except:
        await message.channel.send('No seas burro. Si no quieres que te mate yo, tienes que mencionar a alguien ._.')

async def gifmat(message):
    embed = discord.Embed(

        title="ThelVadam",
        color=discord.Colour.random()

    )
    linea = ""
    file = copen("mattimagen.txt")
    lines = file.count('\n')
    random_line = file.getline(randint(1, lines))
    linea = random_line
    print(linea)
    embed.set_image(url=linea)
    await message.channel.send(embed=embed)

async def scorpion(message):
    try:
        scor1 = message.content
        listascor = list(scor1.split(" "))
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        nombre3 = "<@" + nombre1 + ">"
        if listascor[2] == nombre2:
            await message.channel.send('¿Te dispararás a tí mismo? O.o')
        elif listascor[2] == nombre3:
            await message.channel.send('¿Te dispararás a vos mismo? O.o')
        elif listascor[2] == "<@!813874482182619166>":
            await message.channel.send('Ejem... Mejor no lo haga compa, si no quiere explotar ni lo intente...')
        elif listascor[2] == "<@813874482182619166>":
            await message.channel.send('Ejem... Mejor no lo haga compa, si no quiere explotar ni lo intente...')
        else:
            await message.channel.send('<@' + nombre1 + '> le ha disparado con un scorpion a ' + listascor[2] + '! O.o')
            await gifscor(message)
    except:
        await message.channel.send('No seas burro. Tienes que mencionar a alguien ._.')

async def gifscor(message):
    embed = discord.Embed(

        title="ThelVadam",
        color=discord.Colour.random()

    )
    linea = ""
    file = copen("scorimagen.txt")
    lines = file.count('\n')
    random_line = file.getline(randint(1, lines))
    linea = random_line
    print(linea)
    embed.set_image(url=linea)
    await message.channel.send(embed=embed)

async def sniper(message):
    try:
        sniper1 = message.content
        listasniper = list(sniper1.split(" "))
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        nombre3 = "<@" + nombre1 + ">"
        if listasniper[2] == nombre2:
            await message.channel.send('¿Te dispararás a tí mismo? O.o')
        if listasniper[2] == nombre3:
            await message.channel.send('¿Te dispararás a tí mismo? O.o')
        elif listasniper[2] == "<@!813874482182619166>":
            await message.channel.send('Ejem... Mejor no lo haga compa, si no quiere una bala en su cola ni lo intente...')
        elif listasniper[2] == "<@813874482182619166>":
            await message.channel.send('Ejem... Mejor no lo haga compa, si no quiere una bala en su cola ni lo intente...')
        else:
            await message.channel.send('<@' + nombre1 + '> ha snipeado a ' + listasniper[2] + '! Bien pro.')
            await gifsniper(message)
    except:
        await message.channel.send('No seas burro. Tienes que mencionar a alguien ._.')

async def gifsniper(message):
    embed = discord.Embed(

        title="ThelVadam",
        color=discord.Colour.random()

    )
    linea = ""
    file = copen("sniperimagen.txt")
    lines = file.count('\n')
    random_line = file.getline(randint(1, lines))
    linea = random_line
    print(linea)
    embed.set_image(url=linea)
    await message.channel.send(embed=embed)

async def teabag(message):
    try:
        tea1 = message.content
        listatea = list(tea1.split(" "))
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        nombre3 = "<@" + nombre1 + ">"
        if listatea[2] == nombre2:
            await message.channel.send('¿Te vas a chupar los huevos tú mismo? O.o')
        elif listatea[2] == nombre3:
            await message.channel.send('¿Te vas a chupar los huevos vos mismo? O.o')
        elif listatea[2] == "<@!813874482182619166>":
            await message.channel.send('Yo te voy a teabaguear a ti pt.')
        elif listatea[2] == "<@813874482182619166>":
            await message.channel.send('Yo te voy a teabaguear a ti pt.')
        else:
            await message.channel.send('TEABAG FATALITY A ' + listatea[2] + '!')
            await gifteabag(message)
    except:
        await message.channel.send('No seas burro. Tienes que mencionar a alguien ._.')

async def gifteabag(message):
    embed = discord.Embed(

        title="ThelVadam",
        color=discord.Colour.random()

    )
    linea = ""
    file = copen("teaimagen.txt")
    lines = file.count('\n')
    random_line = file.getline(randint(1, lines))
    linea = random_line
    print(linea)
    embed.set_image(url=linea)
    await message.channel.send(embed=embed)

async def banshee(message):
    try:
        bans1 = message.content
        listabans = list(bans1.split(" "))
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        nombre3 = "<@" + nombre1 + ">"
        if listabans[2] == nombre2:
            await message.channel.send('A veces eres raro, no entiendo cómo te vas a matar a tí mismo con un banshee xd._.')
        if listabans[2] == nombre3:
            await message.channel.send('A veces eres raro, no entiendo cómo te vas a matar a vos mismo con un banshee xd._.')
        elif listabans[2] == "<@!813874482182619166>":
            await message.channel.send('Vente para acá hijo de tu pm vas a ver quien se muere...')
        elif listabans[2] == "<@813874482182619166>":
            await message.channel.send('Vente para acá hijo de tu pm vas a ver quien se muere...')
        else:
            await message.channel.send('<@' + nombre1 + '> ha matado a ' + listabans[2] + ' con un Banshee!')
            await gifbans(message)
    except:
        await message.channel.send('No seas burro. Tienes que mencionar a alguien ._.')

async def gifbans(message):
    embed = discord.Embed(

        title="ThelVadam",
        color=discord.Colour.random()

    )
    linea = ""
    file = copen("bansimagen.txt")
    lines = file.count('\n')
    random_line = file.getline(randint(1, lines))
    linea = random_line
    print(linea)
    embed.set_image(url=linea)
    await message.channel.send(embed=embed)

async def granada(message):
    try:
        grans1 = message.content
        listagrans = list(grans1.split(" "))
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        nombre3 = "<@" + nombre1 + ">"
        await message.delete()
        if listagrans[2] == nombre2:
            await message.channel.send('Yo no lo haría si fuera tú... Comando secreto 5/5')
        elif listagrans[2] == nombre3:
            await message.channel.send('Yo no lo haría si fuera vos... Comando secreto 5/5')
        elif listagrans[2] == "<@!813874482182619166>":
            await message.channel.send('Primero aprende a jugar XD. Comando secreto 5/5')
        elif listagrans[2] == "<@813874482182619166>":
            await message.channel.send('Primero aprende a jugar XD. Comando secreto 5/5')
        else:
            await message.channel.send('<@' + nombre1 + '> ha matado a ' + listagrans[2] + ' con granadas!')
            await gifgrans(message)
    except:
        await message.channel.send('No seas burro. Tienes que mencionar a alguien ._. Comando secreto 5/5')

async def gifgrans(message):
    embed = discord.Embed(

        title="ThelVadam",
        color=discord.Colour.random()

    )
    linea = ""
    file = copen("gransimagen.txt")
    lines = file.count('\n')
    random_line = file.getline(randint(1, lines))
    linea = random_line
    print(linea)
    embed.set_image(url=linea)
    embed.set_footer(text="Comando secreto 5/5")
    await message.channel.send(embed=embed)

async def ball(message):
    try:
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        msg = message.content
        mensaje1 = list(msg.split(" "))
        mensaje1.remove("!tv")
        mensaje1.remove("8ball")
        mensaje2 = ' '.join([str(item) for item in mensaje1 ])
        linea = ""
        file = copen("bolaocho.txt")
        lines = file.count('\n')
        random_line = file.getline(randint(1, lines))
        linea = random_line

        embed = discord.Embed(

            title=":8ball: ThelVadam 8ball",
            color=discord.Colour.random()

        )
        embed.add_field(name=f":question: {message.author.name} pregunta:", value=mensaje2, inline=False)
        embed.add_field(name=":100: Respuesta de Thel 'Vadam:", value=linea, inline=False)
        await message.channel.send(embed=embed)
    except:
        await message.channel.send("We, pero escribe algo._.")

async def espada(message):
    try:
        sword1 = message.content
        listasword = list(sword1.split(" "))
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        nombre3 = "<@" + nombre1 + ">"
        if listasword[2] == nombre2:
            await message.channel.send('¿Te auto espadearás? O.o')
        elif listasword[2] == nombre3:
            await message.channel.send('¿Te auto espadearás? O.o')
        elif listasword[2] == "<@!813874482182619166>":
            await message.channel.send('Ejem... Soy experto en espadas, si no quieres que te rebane como sushi ni te me acerques...')
        elif listasword[2] == "<@813874482182619166>":
            await message.channel.send('Ejem... Soy experto en espadas, si no quieres que te rebane como sushi ni te me acerques...')
        else:
            await message.channel.send('<@' + nombre1 + '> ha espadeado a ' + listasword[2] + '!')
            await gifsword(message)
    except:
        await message.channel.send('No seas burro. Tienes que mencionar a alguien ._.')

async def gifsword(message):
    embed = discord.Embed(

        title="ThelVadam",
        color=discord.Colour.random()

    )
    linea = ""
    file = copen("swordimagen.txt")
    lines = file.count('\n')
    random_line = file.getline(randint(1, lines))
    linea = random_line
    print(linea)
    embed.set_image(url=linea)
    await message.channel.send(embed=embed)

async def bola8(message):
    try:
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        msg = message.content
        mensaje1 = list(msg.split(" "))
        mensaje1.remove("!tv")
        mensaje1.remove("bola8")
        mensaje2 = ' '.join([str(item) for item in mensaje1 ])
        linea = ""
        file = copen("bolaocho.txt")
        lines = file.count('\n')
        random_line = file.getline(randint(1, lines))
        linea = random_line

        embed = discord.Embed(

            title=":8ball: ThelVadam 8ball",
            color=discord.Colour.random()

        )
        embed.add_field(name=f":question: {message.author.name} pregunta:", value=mensaje2, inline=False)
        embed.add_field(name=":100: Respuesta de Thel 'Vadam:", value=linea, inline=False)
        await message.channel.send(embed=embed)
    except:
        await message.channel.send("We, pero escribe algo._.")

async def bolaocho(message):
    try:
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        msg = message.content
        mensaje1 = list(msg.split(" "))
        mensaje1.remove("!tv")
        mensaje1.remove("bolaocho")
        mensaje2 = ' '.join([str(item) for item in mensaje1 ])
        linea = ""
        file = copen("bolaocho.txt")
        lines = file.count('\n')
        random_line = file.getline(randint(1, lines))
        linea = random_line

        embed = discord.Embed(

            title=":8ball: ThelVadam 8ball",
            color=discord.Colour.random()

        )
        embed.add_field(name=f":question: {message.author.name} pregunta:", value=mensaje2, inline=False)
        embed.add_field(name=":100: Respuesta de Thel 'Vadam:", value=linea, inline=False)
        await message.channel.send(embed=embed)
    except:
        await message.channel.send("We, pero escribe algo._.")

async def pregunta(message):
    try:
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        msg = message.content
        mensaje1 = list(msg.split(" "))
        mensaje1.remove("!tv")
        mensaje1.remove("pregunta")
        mensaje2 = ' '.join([str(item) for item in mensaje1 ])
        linea = ""
        file = copen("bolaocho.txt")
        lines = file.count('\n')
        random_line = file.getline(randint(1, lines))
        linea = random_line

        embed = discord.Embed(

            title=":8ball: ThelVadam 8ball",
            color=discord.Colour.random()

        )
        embed.add_field(name=f":question: {message.author.name} pregunta:", value=mensaje2, inline=False)
        embed.add_field(name=":100: Respuesta de Thel 'Vadam:", value=linea, inline=False)
        await message.channel.send(embed=embed)
    except:
        await message.channel.send("We, pero escribe algo._.")

async def bolanegra(message):
    try:
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        msg = message.content
        mensaje1 = list(msg.split(" "))
        mensaje1.remove("!tv")
        mensaje1.remove("bolanegra")
        mensaje2 = ' '.join([str(item) for item in mensaje1 ])
        linea = ""
        file = copen("bolaocho.txt")
        lines = file.count('\n')
        random_line = file.getline(randint(1, lines))
        linea = random_line

        embed = discord.Embed(

            title=":8ball: ThelVadam 8ball",
            color=discord.Colour.random()

        )
        embed.add_field(name=f":question: {message.author.name} pregunta:", value=mensaje2, inline=False)
        embed.add_field(name=":100: Respuesta de Thel 'Vadam:", value=linea, inline=False)
        await message.channel.send(embed=embed)
    except:
        await message.channel.send("We, pero escribe algo._.")

async def question(message):
    try:
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        msg = message.content
        mensaje1 = list(msg.split(" "))
        mensaje1.remove("!tv")
        mensaje1.remove("pregúnta")
        mensaje2 = ' '.join([str(item) for item in mensaje1 ])
        linea = ""
        file = copen("bolaocho.txt")
        lines = file.count('\n')
        random_line = file.getline(randint(1, lines))
        linea = random_line

        embed = discord.Embed(

            title=":8ball: ThelVadam 8ball",
            color=discord.Colour.random()

        )
        embed.add_field(name=f":question: {message.author.name} pregunta:", value=mensaje2, inline=False)
        embed.add_field(name=":100: Respuesta de Thel 'Vadam:", value=linea, inline=False)
        await message.channel.send(embed=embed)
    except:
        await message.channel.send("We, pero escribe algo._.")

async def question2(message):
    try:
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        msg = message.content
        mensaje1 = list(msg.split(" "))
        mensaje1.remove("!tv")
        mensaje1.remove("question")
        mensaje2 = ' '.join([str(item) for item in mensaje1 ])
        linea = ""
        file = copen("bolaocho.txt")
        lines = file.count('\n')
        random_line = file.getline(randint(1, lines))
        linea = random_line

        embed = discord.Embed(

            title=":8ball: ThelVadam 8ball",
            color=discord.Colour.random()

        )
        embed.add_field(name=f":question: {message.author.name} pregunta:", value=mensaje2, inline=False)
        embed.add_field(name=":100: Respuesta de Thel 'Vadam:", value=linea, inline=False)
        await message.channel.send(embed=embed)
    except:
        await message.channel.send("We, pero escribe algo._.")

async def encuesta(message):
    try:
        msg = message.content
        mensaje1 = list(msg.split(" "))
        mensaje1.remove("!tv")
        mensaje1.remove("encuesta")
        mensaje2 = ' '.join([str(item) for item in mensaje1 ])

        embed = discord.Embed(

            title="Encuesta de Thel 'Vadam",
            color=discord.Colour.random()

        )
        embed.add_field(name=":question: Encuesta:", value=mensaje2, inline=False)
        embed.add_field(name="Respuesta 1", value=":white_check_mark: Sí", inline=True)
        embed.add_field(name="Respuesta 2", value="⛔ No", inline=True)
        await message.delete()
        message = await message.channel.send(embed=embed)
        await message.add_reaction("✅")
        await message.add_reaction("⛔")
    except:
        await message.channel.send("We, pero escribe algo._.")

async def poll(message):
    try:
        msg = message.content
        mensaje1 = list(msg.split(" "))
        mensaje1.remove("!tv")
        mensaje1.remove("poll")
        mensaje2 = ' '.join([str(item) for item in mensaje1 ])

        embed = discord.Embed(

            title="Encuesta de Thel 'Vadam",
            color=discord.Colour.random()

        )
        embed.add_field(name=":question: Encuesta:", value=mensaje2, inline=False)
        embed.add_field(name="Respuesta 1", value=":white_check_mark: Sí", inline=True)
        embed.add_field(name="Respuesta 2", value="⛔ No", inline=True)
        await message.delete()
        message = await message.channel.send(embed=embed)
        await message.add_reaction("✅")
        await message.add_reaction("⛔")
    except:
        await message.channel.send("We, pero escribe algo._.")

async def update(message):
    handler = open('msgdia.txt')
    msgdia1 = handler.read()
    embed = discord.Embed(

        title="Novedades de Thel 'Vadam",
        description=msgdia1,
        color=discord.Colour.random()

    )
    message_channel = client.get_channel(789385421083508737)
    await message.delete()
    await message_channel.send(embed = embed)

async def avatar(message):
    try:
        try:
            avatar1 = message.content
            listavatar = list(avatar1.split(" "))
            nombre1 = message.author
            nombre2 = str(listavatar[2])
            nombrelist = list(nombre2.split("<@!"))
            #print(nombrelist)
            nombre4 = str(nombrelist[1])
            nombrelist2 = list(nombre4.split(">"))
            nombre5 = str(nombrelist2[0])
            userid = int(nombre5)
            user = await client.fetch_user(userid)
            us = str(user)
            usuario = list(us.split("#"))
            persona = str(usuario[0])
            nombre3 = "Avatar de " + persona
            peticion = f"Pedido por: {message.author.name}"
            pfp = user.avatar_url
            foto = str(pfp)
            embed = discord.Embed(

                title=nombre3,
                url = foto,
                color=discord.Colour.random()

            )
            #username = user.name
            embed.set_image(url=pfp)
            embed.set_footer(text=peticion)
            await message.channel.send(embed=embed)

        except:
            nombre4 = str(nombrelist[0])
            nombrelist2 = list(nombre4.split("<@")) 
            nombre41 = str(nombrelist2[1])      
            nombrelist3 = list(nombre41.split(">"))   
            nombre5 = str(nombrelist3[0])    
            userid = int(nombre5)
            user = await client.fetch_user(userid)
            us = str(user)
            usuario = list(us.split("#"))
            persona = str(usuario[0])
            nombre3 = "Avatar de " + persona
            peticion = f"Pedido por: {message.author.name}"
            pfp = user.avatar_url
            foto = str(pfp)
        
            embed = discord.Embed(

                title=nombre3,
                url=foto,
                color=discord.Colour.random()

            )
            #username = user.name
            embed.set_image(url=pfp)
            embed.set_footer(text=peticion)
            await message.channel.send(embed=embed)  
    except:
        nombre3 = f"Avatar de {message.author.name}"
        autor = message.author
        pfp2 = autor.avatar_url
        foto2 = str(pfp2)
        embed = discord.Embed(

            title=nombre3,
            url=foto2,
            color=discord.Colour.random()

        )
        embed.set_image(url=pfp2)
        await message.channel.send(embed=embed)

async def confesion(message):
    try:
        msg = message.content
        mensaje1 = list(msg.split(" "))
        mensaje1.remove("!tv")
        mensaje1.remove("confesion")
        mensaje2 = ' '.join([str(item) for item in mensaje1 ])

        embed = discord.Embed(

            title="Confesión:",
            description=mensaje2,
            color=discord.Colour.random()

        )
        await message.channel.send(embed=embed)
        await message.delete()
    except:
        await message.delete()
        await message.channel.send("We, pero escribe algo._.")

async def confession(message):
    try:
        msg = message.content
        mensaje1 = list(msg.split(" "))
        mensaje1.remove("!tv")
        mensaje1.remove("confession")
        mensaje2 = ' '.join([str(item) for item in mensaje1 ])


        embed = discord.Embed(

            title="Confesión:",
            description=mensaje2,
            color=discord.Colour.random()

        )
        await message.channel.send(embed=embed)
        await message.delete()
    except:
        await message.delete()
        await message.channel.send("We, pero escribe algo._.")

async def confesionn(message):
    try:
        msg = message.content
        mensaje1 = list(msg.split(" "))
        mensaje1.remove("!tv")
        mensaje1.remove("confesión")
        mensaje2 = ' '.join([str(item) for item in mensaje1 ])


        embed = discord.Embed(

            title="Confesión:",
            description=mensaje2,
            color=discord.Colour.random()

        )
        await message.channel.send(embed=embed)
        await message.delete()
    except:
        await message.delete()
        await message.channel.send("We, pero escribe algo._.")

async def equipo(message):
    try:
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        msg = message.content
        mensaje1 = list(msg.split(" "))
        usuario = mensaje1[2] 
        linea = ""
        file = copen("equipo.txt")
        lines = file.count('\n')
        random_line = file.getline(randint(1, lines))
        linea = random_line
        lin = list(linea.split("\n"))
        if "0" in lin:
            mensaje = "0 % [. . . . . . .] \n**No son compatibles para hacer equipo, lo mejor es que no intenten jugar un vs juntos.**"
            await message.channel.send(mensaje)
        elif "25" in lin:
            mensaje = "25 % [███ . . . . .]\n**Son muy poco compatibles. Quizás podrían hacerla en un versus aunque claramente uno hará todo el trabajo.**"
            await message.channel.send(mensaje)
        elif "50" in lin:
            mensaje = "50 % [████ . . . .]\n**Son compatibles. Tienen 50% de probabilidades de ganar un vs como equipo.**"
            await message.channel.send(mensaje)
        elif "75" in lin:
            mensaje = "75 % [████████ . . .]\n**Son altamente compatibles, tienen una alta probabilidad de ganar la mayoría de los vs juntos.**"
            await message.channel.send(mensaje)
        elif "100" in lin:
            mensaje = "100 % [███████████]\n**Son totalmente compatibles, seguramente ganarán todos sus vs juntos.**"
            await message.channel.send(mensaje)

        await gifcompat(message)

    except:
        await message.channel.send("Pero menciona a alguien mi buen._.")

async def gifcompat(message):
    embed = discord.Embed(

        title="ThelVadam",
        color=discord.Colour.random()

    )
    linea = ""
    file = copen("swordimagen.txt")
    lines = file.count('\n')
    random_line = file.getline(randint(1, lines))
    linea = random_line
    print(linea)
    embed.set_image(url=linea)
    await message.channel.send(embed=embed)

async def espiar(message):
    try:
        espiar1 = message.content
        listaespiar = list(espiar1.split(" "))
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        nombre3 = "<@" + nombre1 + ">"
        if listaespiar[2] == nombre2:
            await message.channel.send('¿Te apuntarás con un sniper a tí mismo? O.o')
        elif listaespiar[2] == nombre3:
            await message.channel.send('¿Te apuntarás con un sniper a vos mismo? O.o')
        elif listaespiar[2] == "<@!813874482182619166>":
            await message.channel.send('Quita ese sniper de mi cara boludo.')
        elif listaespiar[2] == "<@813874482182619166>":
            await message.channel.send('Quita ese sniper de mi cara boludo.')
        else:
            await message.channel.send('¡ <@' + nombre1 + '> tiene en la mira a ' + listaespiar[2] + ' !')
            await gifespiar(message)
            await asyncio.sleep(30)
            await message.channel.send("¡ " + listaespiar[2] + ' fue snipeado por <@' + nombre1 + '> !')
            await gifsniper(message)
    except:
        await message.channel.send('No seas burro. Tienes que mencionar a alguien ._.')

async def gifespiar(message):
    embed = discord.Embed(

        title="ThelVadam",
        color=discord.Colour.random()

    )
    linea = ""
    file = copen("sniperimagen.txt")
    lines = file.count('\n')
    random_line = file.getline(randint(1, lines))
    linea = random_line
    print(linea)
    embed.set_image(url=linea)
    await message.channel.send(embed=embed)

async def wraith(message):
    try:
        scor1 = message.content
        listascor = list(scor1.split(" "))
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        nombre3 = "<@" + nombre1 + ">"
        if listascor[2] == nombre2:
            await message.channel.send('¿Te dispararás a tí mismo? O.o')
        elif listascor[2] == nombre3:
            await message.channel.send('¿Te dispararás a vos mismo? O.o')
        elif listascor[2] == "<@!813874482182619166>":
            await message.channel.send('Ejem... Mejor no lo haga compa, si no quiere explotar ni lo intente...')
        elif listascor[2] == "<@813874482182619166>":
            await message.channel.send('Ejem... Mejor no lo haga compa, si no quiere explotar ni lo intente...')
        else:
            await message.channel.send('<@' + nombre1 + '> le ha disparado una bola enorme de plasma a ' + listascor[2] + ' con un wraith! O.o')
            await gifwr(message)
    except:
        await message.channel.send('No seas burro. Tienes que mencionar a alguien ._.')

async def gifwr(message):
    embed = discord.Embed(

        title="ThelVadam",
        color=discord.Colour.random()

    )
    linea = ""
    file = copen("wraith.txt")
    lines = file.count('\n')
    random_line = file.getline(randint(1, lines))
    linea = random_line
    print(linea)
    embed.set_image(url=linea)
    await message.channel.send(embed=embed)

async def rocket(message):
    try:
        rock1 = message.content
        listarock = list(rock1.split(" "))
        nombre1 = str(message.author.id)
        nombre2 = "<@!" + nombre1 + ">"
        nombre3 = "<@" + nombre1 + ">"
        if listarock[2] == nombre2:
            await message.channel.send('¿Te dispararás a tí mismo? O.o')
        elif listarock[2] == nombre3:
            await message.channel.send('¿Te dispararás a vos mismo? O.o')
        elif listarock[2] == "<@!813874482182619166>":
            await message.channel.send('Ejem... Mejor no lo haga compa, si no quiere explotar ni lo intente...')
        elif listarock[2] == "<@813874482182619166>":
            await message.channel.send('Ejem... Mejor no lo haga compa, si no quiere explotar ni lo intente...')
        else:
            await message.channel.send('<@' + nombre1 + '> ha sacado volando a ' + listarock[2] + ' con un rocket! O.o')
            await gifrock(message)
    except:
        await message.channel.send('No seas burro. Tienes que mencionar a alguien ._.')

async def gifrock(message):
    embed = discord.Embed(

        title="ThelVadam",
        color=discord.Colour.random()

    )
    linea = ""
    file = copen("rocket.txt")
    lines = file.count('\n')
    random_line = file.getline(randint(1, lines))
    linea = random_line
    print(linea)
    embed.set_image(url=linea)
    await message.channel.send(embed=embed)

async def groserias(message):
    mensaje = str(message.content)
    autor = f"{message.author.name}"
    embed = discord.Embed(

        title=f"Aviso a {message.author.name}:",
        description="Uso de malas palabras.",
        color=discord.Colour.random()

    )
    await message.channel.send(embed=embed)
    await message.delete()

    embed2 = discord.Embed(

        title="Reporte de " + autor + ":",
        description="Uso de malas palabras.",
        color=discord.Colour.random()

    )
    embed2.add_field(name="Mensaje: ", value=mensaje, inline=False)
    message_channel = client.get_channel(815063853494829066)    
    await message_channel.send(embed=embed2)

async def bots(message):
    try:
        mensaje = str(message.content)
        autor = f"{message.author.name}"
        embed = discord.Embed(

            title=f"Aviso a {message.author.name}:",
            description="Uso de bot fuera de canal #comandos-bot💻.",
            color=discord.Colour.random()

        )
        await message.channel.send(embed=embed)
        #message_channel = client.get_channel(815063853494829066)    
        #await message_channel.send(embed=embed)
        await message.delete()
        
    except:
        return

async def botmeme(message):
    embed = discord.Embed(

        title=f"Aviso a {message.author.name}:",
        description="Uso de bot fuera de canal #😂-memes.",
        color=discord.Colour.random()

    )
    await message.channel.send(embed=embed)
    #message_channel = client.get_channel(815063853494829066)    
    #await message_channel.send(embed=embed)
    await message.delete()

async def repormiembros(message):
    embed = discord.Embed(

        title=f"Aviso a {message.author.name}:",
        description="Mención indebida de @Miembros del clan",
        color=discord.Colour.random()

    )
    await message.channel.send(embed=embed)
    message_channel = client.get_channel(815063853494829066)    
    await message_channel.send(embed=embed)
    await message.delete()

async def agresivo(message):
    mensaje = str(message.content)
    autor = f"{message.author.name}"
    embed = discord.Embed(

        title=f"Aviso a {message.author.name}:",
        description="Agresividad innecesaria.",
        color=discord.Colour.random()

    )
    await message.channel.send(embed=embed)
    await message.delete()

    embed2 = discord.Embed(

        title="Reporte de " + autor + ":",
        description="Agresividad innecesaria.",
        color=discord.Colour.random()

    )
    embed2.add_field(name="Mensaje: ", value=mensaje, inline=False)
    message_channel = client.get_channel(815063853494829066)
    await message_channel.send(embed=embed2)

async def feedback(message):
    try:
        mensaje = message.content
        listamensaje = list(mensaje.split(" "))
        uy = listamensaje[2]
        listamensaje.remove("!tv")
        listamensaje.remove("feedback")
        mensaje2 = ' '.join([str(item) for item in listamensaje])
        f=open("feedback.txt", "a+")
        f.write("\n" + mensaje2)
        await message.channel.send("Feedback recibido. ¡Gracias por tus comentarios!")
        await message.delete()
        await asyncio.sleep(1)
        await message.channel.purge(limit=1)
    except:
        await message.channel.send("Tienes que escribir tu feedback después del comando.")
        await message.delete()
        await asyncio.sleep(1)
        await message.channel.purge(limit=1)

async def mejoden(message):
    try:
        mensaje = message.content
        listamensaje = list(mensaje.split(" "))
        usuario = listamensaje[2]
        mensaje = str(message.content)
        autor = f"{message.author.name}"
        embed = discord.Embed(

            title=f"Aviso a " + usuario,
            description="Comenzó a molestar a Olivia",
            color=discord.Colour.random()

        )
        await message.channel.send(embed=embed)
        message_channel = client.get_channel(815063853494829066)    
        await message_channel.send(embed=embed)
        await message.delete()
        
    except:
        await message.delete()

async def jodbot(message):
    try:
        mensaje = message.content
        listamensaje = list(mensaje.split(" "))
        usuario = listamensaje[2]
        mensaje = str(message.content)
        autor = f"{message.author.name}"
        embed = discord.Embed(

            title=f"Aviso a " + usuario,
            description="Insultó al bot.",
            color=discord.Colour.random()

        )
        await message.channel.send(embed=embed)
        message_channel = client.get_channel(815063853494829066)    
        await message_channel.send(embed=embed)
        await message.delete()
        
    except:
        await message.delete()


client.run(os.getenv('TOKEN'))