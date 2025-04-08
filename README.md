# *DolarBot*

- Index
  - [Summarize](#summarize)
  - [How to download it](#how-to-download-it)
  - [Installation and (Linux, MacOS)](#installation-and-linux-macos)
  - [Usage](#usage)
  - [Resources](#resources)
  - [Developers](#developers)
## **Summarize**
Our Project is going to be a bot that you will be able to use on any discord server, it will be informing you about the live price of the dollar blue and the official dollar, with various commands the bot will give you will be responding at the moment depending on the command used

---

## How to download it
- Clone/Download the repository [here](https://github.com/)
- Create discord bot [here](https://discord.com/developers/applications)
- Get your token
- Invite your bot on servers using the following invite: https://discord.com/oauth2/authorize?&client_id=YOUR_APPLICATION_ID_HERE&scope=bot+applications.commands (Replace `YOUR_APPLICATION_ID_HERE` with your aplication id given that can be get at the bottom of this page: https://discord.com/developers/applications/YOUR_APPLICATION_ID_HERE/bot)

---
## How to start
To start the bot you simply need to launch, either your terminal (Linux, Mac & Windows), or your Command Prompt (Windows)

Before running the bot you will need to install all the requirements for this project installed listed in the Pipfile
>you need [`pipenv`](https://gist.github.com/planetceres/8adb62494717c71e93c96d8adad26f5c) and [`pyenv`](https://ubunlog.com/en/pyenv-instala-multiples-versiones-de-python-en-tu-sistema/) to install and run the app

```
$ pipenv install  
```
> You'll have to enter to the environment using this command: 
```
pipenv shell
```
After that you can it with
```
(venv)$ python src/main.py
```
---

## Resources
- Discord.py
- Request

---
## Developers
App made by: 
- [Ferreyra](https://github.com/Ferchovich)
- [Mendez](https://github.com/FabricioMendez)
- [Puig](https://github.com/HermesPuig)