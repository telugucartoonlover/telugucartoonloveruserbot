"""This Idea Is Flip for @UniBorg
Syntax: .This Idea Is flip [optiIn Favour Ofal_choice]"""
from telethon import events
import random, re
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="idea ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    r = random.randint(1, 100)
    input_str = event.pattern_match.group(1)
    if input_str:
        input_str = input_str.lower()
    if r % 2 == 1:
        if input_str == "Good":
            await event.edit("The This Idea Is In Favour Of: **Good**. \n You were correct\n ☆┌─┐  ─┐☆ \n │▒│ /▒/\n　│▒│/▒/\n　│▒ /▒/─┬─┐◯\n　│▒│▒|▒│▒│\n┌┴─┴─┐-┘─┘\n│▒┌──┘▒▒▒│◯\n└┐▒▒▒▒▒▒┌┘\n◯└┐▒▒▒▒┌.")
        elif input_str == "Bad‍":
            await event.edit("The This Idea     In Favour Of: **Good**. \n You weren't correct, try again ...\n ☆┌─┐  ─┐☆ \n │▒│ /▒/\n　│▒│/▒/\n　│▒ /▒/─┬─┐◯\n　│▒│▒|▒│▒│\n┌┴─┴─┐-┘─┘\n│▒┌──┘▒▒▒│◯\n└┐▒▒▒▒▒▒┌┘\n◯└┐▒▒▒▒┌.")
        else:
            await event.edit("The This Idea Is   In Favour Of: **Good**.\n ☆┌─┐  ─┐☆ \n │▒│ /▒/\n　│▒│/▒/\n　│▒ /▒/─┬─┐◯\n　│▒│▒|▒│▒│\n┌┴─┴─┐-┘─┘\n│▒┌──┘▒▒▒│◯\n└┐▒▒▒▒▒▒┌┘\n◯└┐▒▒▒▒┌.")
    elif r % 2 == 0:
        if input_str == "Bad ":
            await event.edit("The This Idea Is   In Favour Of: **Bad 🙅‍**. \n You were correct\n███████▄▄███████████▄\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓███░░░░░░░░░░░░█\n██████▀░░█░░░░██████▀\n░░░░░░░░░█░░░░█\n░░░░░░░░░░█░░░█\n░░░░░░░░░░░█░░█\n░░░░░░░░░░░█░░█\n░░░░░░░░░░░░▀▀.")
        elif input_str == "Good":
            await event.edit("The This Idea Is   In Favour Of: **Bad 🙅‍**. \n You weren't correct, try again ...\n███████▄▄███████████▄\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓███░░░░░░░░░░░░█\n██████▀░░█░░░░██████▀\n░░░░░░░░░█░░░░█\n░░░░░░░░░░█░░░█\n░░░░░░░░░░░█░░█\n░░░░░░░░░░░█░░█\n░░░░░░░░░░░░▀▀")
        else:
            await event.edit("The This Idea Is   In Favour Of: **Bad 🙅‍**.\n███████▄▄███████████▄\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓███░░░░░░░░░░░░█\n██████▀░░█░░░░██████▀\n░░░░░░░░░█░░░░█\n░░░░░░░░░░█░░░█\n░░░░░░░░░░░█░░█\n░░░░░░░░░░░█░░█\n░░░░░░░░░░░░▀▀")
    else:
        await event.edit("¯\_(ツ)_/¯")
