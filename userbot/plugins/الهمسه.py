from . import reply_id as rd
from userbot.tosh import *


WPIC = "https://telegra.ph/1127044647-02-12"
T = "𓆰 𝗦𝗢𝗨𝗥𝗖𝗘 STARK - 𝑺𝑬𝑪𝑹𝑬𝑻 𝑴𝑺𝑮 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n**⌔∮ قائـمه اوامر الهمسه :** \n⪼ `.الهمسه` لعرض كيفيه ارسال الهمسه من بوتك\n⪼ `.همسه` لارسال همسه عن طريق بوت الهمسه  \n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n𓆩 𝗦𝗢𝗨𝗥𝗖𝗘 STARK - [قناة السورس](t.me/XRXNR) 𓆪"

@bot.on(admin_cmd(pattern="م21"))
@bot.on(sudo_cmd(pattern="م21", allow_sudo=True))
async def wspr(kimo):
    await eor(kimo, T)


# Wespr - همسه
@bot.on(admin_cmd(pattern="الهمسه$"))
@bot.on(sudo_cmd(pattern="الهمسه$", allow_sudo=True))
async def kimo(lon):
    if lon.fwd_from:
        return
    ld = await rd(lon)
    if WPIC:
        ics_c = f"**- يمكنك ارسال همسة لعده اشخاص مره واحده**\n**- يمكنك همس ( ملصق - صوره - صوت - متحرك - فيديو ) فقط ارسل كلمة همسه للبوت** @nnbbot \n**- يوصل اشععار من شاهد همستك فقط اذا كانت الهمسه نص**\n\n**-ميزه ممطروقه بالبوت :**\n**يمكنك عمل همسه بالرد ع الشخص فقط اضف البوت للمجموعه وقم بالرد ع الشخص بكلمة همسه 🧸🎁**\n\n𓆰 𝗦𝗢𝗨𝗥𝗖𝗘 STARK -** @XRXNR"
        ics_c += f"**- قم بنسخ :**\n `@nnbbot الرساله ثم معرف الشخص`"
        await lon.client.send_file(lon.chat_id, WPIC, caption=ics_c, reply_to=ld)


# Wespr - همسه
@bot.on(admin_cmd(pattern="همسه$"))
@bot.on(sudo_cmd(pattern="همسه$", allow_sudo=True))
async def kimo(lon):
    if lon.fwd_from:
        return
    ld = await rd(lon)
    if WPIC:
        ics_c = f"**- يمكنك ارسال همسة لعده اشخاص مره واحده**\n**- يمكنك همس ( ملصق - صوره - صوت - متحرك - فيديو ) فقط ارسل كلمة همسه للبوت** @nnbbot \n**- يوصل اشععار من شاهد همستك فقط اذا كانت الهمسه نص**\n\n**-ميزه ممطروقه بالبوت :**\n**يمكنك عمل همسه بالرد ع الشخص فقط اضف البوت للمجموعه وقم بالرد ع الشخص بكلمة همسه 🧸🎁**\n\n𓆰 𝗦𝗢𝗨𝗥𝗖𝗘 STARK -** @XRXNR"
        ics_c += f"**- قم بنسخ :**\n `@nnbbot الرساله ثم معرف الشخص`"
        await lon.client.send_file(lon.chat_id, WPIC, caption=ics_c, reply_to=ld)

