#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | Modified By > @DC4_WARRIOR


from pyrogram import Client as Clinton
from plugins.youtube_dl_button import youtube_dl_call_back
from plugins.dl_button import ddl_call_back

from translation import Translation

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery



@Clinton.on_callback_query()
async def button(bot, update):

    cb_data = update.data
    if "|" in cb_data:
        await youtube_dl_call_back(bot, update)
    elif "=" in cb_data:
        await ddl_call_back(bot, update)
    elif "aboutbot" in cb_data:
        await update.message.edit(
            text=Translation.ABOUT_TEXT,
            parse_mode="html",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
					[
						InlineKeyboardButton("👥 𝗛𝗲𝗹𝗽", callback_data="help"),
						InlineKeyboardButton("🌐 𝗨𝗽𝗱𝗮𝘁𝗲𝘀", url="https://t.me/ullastv")
					],
					[
						InlineKeyboardButton("🏠 𝗛𝗼𝗺𝗲", callback_data="gotohome") 
					]
	        ]
            )
        )

    elif "help" in cb_data:
        await update.message.edit(
            text=Translation.HELP_USER,
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                                        [
						InlineKeyboardButton("𝗨𝗽𝗱𝗮𝘁𝗲𝘀 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url="https://t.me/ullastv")
					],
					[
						InlineKeyboardButton("👥 𝗔𝗯𝗼𝘂𝘁", callback_data="aboutbot"),
						InlineKeyboardButton("🏠 𝗛𝗼𝗺𝗲", callback_data="gotohome")
					]
                ]
            )
        )

    elif "gotohome" in cb_data:
        await update.message.edit(
            text=Translation.START_TEXT.format(update.from_user.mention),
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
						InlineKeyboardButton("𝗦𝘂𝗽𝗽𝗼𝗿𝘁", url="https://t.me/m8u3_bot"),
						InlineKeyboardButton("𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url="https://t.me/ullastv")
					],
					[
						InlineKeyboardButton("👥 𝗔𝗯𝗼𝘂𝘁 ", callback_data="aboutbot"),
						InlineKeyboardButton("🗣️ 𝗛𝗲𝗹𝗽 ", callback_data="help")
					], 
                                        [
						InlineKeyboardButton("🌐 𝗠𝗼𝘃𝗶𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 ", url="https://t.me/ullastv"),
						InlineKeyboardButton("📢 𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗕𝘆", url="https://t.me/ibyomkesh2")
	            ]
                ]
            )
        )

@Clinton.on_callback_query()
async def button(bot, update):
 
      if  'close'  in update.data:
                await update.message.delete()
