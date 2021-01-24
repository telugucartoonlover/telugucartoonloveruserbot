"""Emoji
Available Commands:
.TCL
Credits to @telugucartoonlover
"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd


@borg.on(admin_cmd("TCL"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1.5
    animation_ttl = range(0,36)
    #input_str = event.pattern_match.group(1)
   # if input_str == "TCL":
    await event.edit("@telugucartoonlover")
    animation_chars = [
            "@telugucartoonlover tera baap",
            "@telugucartoonlover is bot ka creator",
            "@telugucartoonlover bot ko jaan dene wala",
            "@telugucartoonlover owner of TCLUserBot ",
            "tujhe aur kya chaiye vo hai mere sath",
            "tera baap",
            "@telugucartoonlover"
         ]
            

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
