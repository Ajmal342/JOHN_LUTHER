# MIT License

# Copyright (c) 2022 Muhammed

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Movie Group Link : https://telegram.dog/filim_factory_king
# Repo Link : THARULLA
# License Link :

from pyrogram import Client as lucifermoringstar_robot , filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from LuciferMoringstar_Robot import ADMINS, CREATOR_USERNAME

@lucifermoringstar_robot.on_message((filters.group | filters.private) & filters.command('leave') & filters.user(ADMINS))
async def leave_bot(bot, update):
    if len(update.command) == 1:
        return await update.reply_text("πΆπΈππ΄ πΌπ΄ π° πΆππΎππΏ πΈπ³")
    chat = update.command[1]
    try:
        chat = int(chat)
    except:
        chat = chat
    try:
        pr0fess0r_99 = [[ InlineKeyboardButton('πΆπ΄π πππΏπΏπΎππ', url=f'https://t.me/{CREATOR_USERNAME}') ]]
        pr0fess0r_99 = InlineKeyboardMarkup(pr0fess0r_99)
        await bot.send_message(chat_id=chat, text="Hello makale,\nπΌπ πΌπ°πππ΄π π·π°π ππΎπ»π³ πΌπ΄ ππΎ π»π΄π°ππ΄ π΅ππΎπΌ πΆππΎππΏ. ππΎ πΈ πΆπΎ π. πΈπ΅ ππΎπ ππ°π½π½π° π°π³π³ πΌπ΄ π°πΆπ°πΈπ½ π²πΎπ½ππ°π²π πΌπ΄", reply_markup=pr0fess0r_99)
        await bot.leave_chat(chat)
        await update.reply(f"π»π΄π΅π ππ·π΄ π²π·π°π `{chat}`")
    except Exception as e:
        await update.reply(f'π΄πππΎπ - {e}')
