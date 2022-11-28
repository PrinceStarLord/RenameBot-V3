import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user
from helper.progress import humanbytes
@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"<b>Total Users :</b> {total_user()}\n\n<b>Name :</b> RenameBot4Gb\n\n<b>Creater :</b> <a href=https://t.me/Prince_Star_Lord>ֆȶǟʀ ʟօʀɖ</a>\n\n<b>Total Renamed Files :</b>{total_rename}\n\n<b>Total Size Renamed :</b>{humanbytes(int(total_size))} ",quote=True)
