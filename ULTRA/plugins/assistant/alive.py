# COPYRIGHT (C) 2021-2022 BY FLAMING22
# modify by madboy482 and alain_champion

from ULTRA import bot
from ULTRAX import xbot, ID
import heroku3
from telethon import events
from ULTRA import StartTime
import time
import datetime
from . import *
from telethon import events, Button, custom
import re, os
from ULTRAX import PHOTO, xbot, BOT, VERSION
from ULTRA import bot
@xbot.on(events.NewMessage(pattern=("/alive")))
async def awake(event):
  FLAMING = f"Hᴇʟʟᴏ !! Tʜɪs ɪs **{BOT}**\n\n"
  FLAMING += "**Aʟʟ sʏsᴛᴇᴍs ᴡᴏʀᴋɪɴɢ ᴘʀᴏᴘᴇʀʟʏ...**\n\n"
  FLAMING += f"**{BOT} Vᴇʀsɪᴏɴ** : `{VERSION}`\n\n"
  FLAMING += f"**Usᴇʀ** : @{bot.me.username}\n\n"
  FLAMING += "**Fᴜʟʟʏ ᴜᴘᴅᴀᴛᴇᴅ ʙᴏᴛ...**\n\n"
  FLAMING += "**Tᴇʟᴇᴛʜᴏɴ** : `1.20`\n\n"
  FLAMING += "~~ **Tʜᴀɴᴋs ғᴏʀ ᴄʜᴇᴄᴋɪɴɢ ᴍᴇ** !!"
  BUTTON = [[Button.url("Mᴀsᴛᴇʀ", f"https://t.me/{bot.me.username}"), Button.url(f"{BOT} Rᴇᴘᴏ", "https://github.com/ITS-FLAMINGBOT/ITS-FLAMING")]]
  BUTTON += [[custom.Button.inline("Rᴇᴘᴏsɪᴛᴏʀɪᴇs »»", data="FLAMING")]]
  await xbot.send_file(event.chat_id, PHOTO, caption=FLAMING,  buttons=BUTTON)




@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"FLAMING")))
async def callback_query_handler(event):
# inline by FLAMING22 and PROBOY22 🔥
  FLAMING = [[Button.url("REPO FLAMING", "https://github.com/ITS-FLAMINGBOT/ITS-FLAMING")]]
  FLAMING +=[[Button.url("DEPLOY FLAMING", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FITS-FLAMINGBOT%2FHEROKU&template=https%3A%2F%2Fgithub.com%2FITS-FLAMING%2FHEROKU")]]
  FLAMING +=[[Button.url("Tᴜᴛᴏʀɪᴀʟ", "https://youtu.be/rFPsS4Q"), Button.url("Sᴛʀɪɴɢ Sᴇssɪᴏɴ", "https://replit.com#main.py")]]
  FLAMING +=[[Button.url("Aᴘɪ Iᴅ & Aᴘɪ Hᴀsʜ", "https://t.me/usetgxbot"), Button.url("Rᴇᴅɪs", "https://redislabs.com")]]
  FLAMING +=[[Button.url("Sᴜᴘᴘᴏʀᴛ Cʜᴀɴɴᴇʟ", "https://t.me/flamingchat"), Button.url("Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ", "https://t.me/flamingub")]]
  FLAMING +=[[custom.Button.inline("«« Aʟɪᴠᴇ", data="PROBOY")]]
  await event.edit(text=f"Aʟʟ Dᴇᴛᴀɪʟs Oғ Rᴇᴘᴏs", buttons=FLAMING)


@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"PROBOY")))
async def callback_query_handler(event):
# inline by FLAMING22 and PROBOY22 🔥
  FLAMING = f"Hᴇʟʟᴏ !! Tʜɪs ɪs **{BOT}**\n\n"
  FLAMING += "**Aʟʟ sʏsᴛᴇᴍs ᴡᴏʀᴋɪɴɢ ᴘʀᴏᴘᴇʀʟʏ...**\n\n"
  FLAMING += f"**{BOT} Vᴇʀsɪᴏɴ** : `{VERSION}`\n\n"
  FLAMING += f"**Usᴇʀ** : @{bot.me.username}\n\n"
  FLAMING += "**Fᴜʟʟʏ ᴜᴘᴅᴀᴛᴇᴅ ʙᴏᴛ...**\n\n"
  FLAMING += "**Tᴇʟᴇᴛʜᴏɴ** : `1.20`\n\n"
  FLAMING += "~~ **Tʜᴀɴᴋs ғᴏʀ ᴄʜᴇᴄᴋɪɴɢ ᴍᴇ** !!"
  BUTTONS = [[Button.url("Mᴀsᴛᴇʀ", f"https://t.me/{bot.me.username}"), Button.url(f"{BOT} Rᴇᴘᴏ", "https://github.com/ITS-FLAMINGBOT/ITS-FLAMING")]]
  BUTTONS += [[custom.Button.inline("Rᴇᴘᴏsɪᴛᴏʀɪᴇs »»", data="FLAMING")]]
  await event.edit(text=FLAMING, buttons=BUTTONS)


@xbot.on(events.NewMessage(pattern=("/repo")))
async def repo(event):
  await xbot.send_message(event.chat, "**Hᴇʀᴇ Is Tʜᴇ Rᴇᴘᴏ Fᴏʀ FLAMING Usᴇʀʙᴏᴛ** \n\nFᴏʀ Aɴʏ Hᴇʟᴘ :- @flamingchat", buttons=[[Button.url("⚜️ Rᴇᴘᴏ ⚜️", "https://github.com/ITS-FLAMINGBOT/ITS-FLAMING"), Button.url("🔰 Dᴇᴘʟᴏʏ 🔰", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FITS-FLAMINGBOT%2FHEROKU&template=https%3A%2F%2Fgithub.com%2FITS-FLAMING%2FHEROKU")]])


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@xbot.on(events.NewMessage(pattern=None))
async def ok(event):
    msg = str(event.text)
    if not msg == "/ping":
     return

    start_time = datetime.datetime.now()
    message = await event.reply("_.._.._Pinging_.._.._")
    end_time = datetime.datetime.now()
    pingtime = end_time - start_time
    telegram_ping = str(round(pingtime.total_seconds(), 2)) + "s"
    uptime = get_readable_time((time.time() - StartTime))
    await message.edit(
        "<b><i>☞ Pᴏɴɢ !!</i></b>\n"
        "<b>➥ Tɪᴍᴇ Tᴀᴋᴇɴ:</b> <code>{}</code>\n"
        "<b>➥ Sᴇʀᴠɪᴄᴇ Uᴘᴛɪᴍᴇ:</b> <code>{}</code>".format(telegram_ping, uptime),
        parse_mode="html",
    )
