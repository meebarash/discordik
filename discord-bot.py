import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Вечер в хату'):
        await message.channel.send('и тебе не хворать')

    if message.content.startswith('мибараш гей'):
        await message.channel.send(f' {message.author.mention} не играй с судьбой,фраерок')

    if message.content.startswith('Теорема виетта?'):
        await message.channel.send(f' {message.author.mention} сумма корней равна второму коэффициенту с противоположным знаком, а произведение корней равняется свободному члену.')

    if message.content.startswith('Дискриминант'):
        await message.channel.send(f' {message.author.mention} не ебу,решай через Виетта. ')

    if message.content.startswith('Зачем детей в подвале расстрелял?'):
        await message.channel.send(f' {message.author.mention} чтобы познать величие слияния с бесконечно-вечным а еще я состою в ИГИЛе')

    if message.content.startswith('Формула мефедрона?'):
        await message.channel.send(f' {message.author.mention} C11H15NO')

    if message.content.startswith('Формула героина?'):
        await message.channel.send(f' {message.author.mention} C21H23NO5')

    if message.content.startswith('Ссылки'):
        await message.channel.send(f' {message.author.mention} Донат: https://qiwi.com/payment/form/99999?extra[%27accountType%27]=phone&extra%5B%27account%27%5D=79264136681 , TT: https://www.tiktok.com/@post_anonimus?lang=ru-RU')

    if message.content.startswith('Команды'):
        await message.channel.send(f' {message.author.mention} Вечер в хату-поздороваться с ботом, Теорема виетта?-узнать теорему, дискриминант-(самого дискриминанта тут не будет, Зачем детей в подвале расстрелял?-насущный воспрос боту, Формула героина/мефедрона?-осторожней с этим, Ссылки-пост анонимуса')
        
client.run('OTIzMjYwOTEyNzU5MTAzNTA4.YcNbug.K-SJO8kqHSshfKI5dXc0-onMK9w')
