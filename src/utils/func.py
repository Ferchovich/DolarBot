import requests, json
from datetime import datetime
from discord import Embed
from discord.ext import commands

def getCurrency(moneda:str, compraOVenta:str) -> str:
    url = "https://api.bluelytics.com.ar/v2/latest"
    response = requests.get(url).json()
    return f"${response[moneda][compraOVenta]}"

def getCurrencyByDay(moneda:str, date_str:str):
    date_formatted = datetime.strptime(date_str, "%Y-%m-%d").date()
    response = requests.get("https://api.bluelytics.com.ar/v2/evolution.json").json()
    for dic in response:
        date = datetime.strptime(dic["date"], "%Y-%m-%d").date()
        if dic["source"] == moneda.capitalize() and date == date_formatted:
            return dic
    return None


def getConfig() -> dict:
    with open("./src/utils/config.json") as f:
        config = json.load(f)
        
    return config



class CreateResponse:
    def __init__(self, title, post_content, color = int("3377FF", 16)):
        self.title = title
        self.content = post_content
        self.response = Embed(title=self.title, description=self.content, colour=color)

    @property
    def send(self):
        return self.response
    
    def createFields(self, data: dict) -> None:
        # {"Oficial": getCurrency("oficial", "value_avg"), ...}
        
        for _, (name, value) in enumerate(data.items()):
            
            self.response.add_field(name=name, value=value, inline=False)
        self.response.set_footer(text="Fuente: https://www.valordolarblue.com.ar", icon_url="https://i.imgur.com/0FOvHM4.png")
    
class CustomHelpCommand(commands.HelpCommand):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    async def send_bot_help(self, mapping):
        prefix = self.bot.command_prefix
        bot_commands = await self.filter_commands(self.bot.commands, sort=True)
        help_message = "Estos son los comandos disponibles\n"
        
        for command in bot_commands:
            help_message += f"`{prefix}{command.name}`: {command.help}\n"

        await self.get_destination().send(help_message)

