import os
import datetime
from telethon import TelegramClient, events

# ▒█▀▀▀ ▒█▀▀▀█ ▒█▄░▒█ ▀█▀ ▀▄▒▄▀ 
# ▒█▀▀▀ ░▀▀▀▄▄ ▒█▒█▒█ ▒█░ ░▒█░░ 
# ▒█▄▄▄ ▒█▄▄▄█ ▒█░░▀█ ▄█▄ ▄▀▒▀▄
api_id = '27430835'
api_hash = '99a495c31546000c0768945e6d1e8953'
phone_number = '+201010738262'

client = TelegramClient('Joker_AutoSave', api_id, api_hash)

ARABIC_DAYS = {
    'Monday': 'الاثنين 🌙',
    'Tuesday': 'الثلاثاء 🌀',
    'Wednesday': 'الأربعاء 🌪',
    'Thursday': 'الخميس 🔥',
    'Friday': 'الجمعة 🕌',
    'Saturday': 'السبت 🌅',
    'Sunday': 'الأحد 🌞'
}

async def save_media_handler(event, reply_msg):
    """دالة معالجة حفظ الميديا بإبداع"""
    try:
        media_path = await reply_msg.download_media()
        caption = f"""
𓏺 𝙎𝘼𝙑𝙀𝘿 𝙈𝙀𝘿𝙄𝘼 𓏺
• التاريخ : {datetime.datetime.now().strftime("%Y-%m-%d")}
• اليوم : {ARABIC_DAYS[datetime.datetime.now().strftime("%A")]}
• تم الحفظ بواسطة : [𓏺 𝙅𝙊𝙆𝙀𝙍 𓏺](tg://user?id={event.sender_id})
        """
        await client.send_file('me', media_path, caption=caption)
        await event.delete()
        os.remove(media_path)
    except Exception as e:
        await event.reply(f'𓆰 خطأ: {e}')

@client.on(events.NewMessage(pattern='^1$'))
async def trigger_save(event):
    """عند الرد برقم 1 يحفظ الميديا"""
    if event.is_reply:
        reply_msg = await event.get_reply_message()
        if reply_msg.media:
            await save_media_handler(event, reply_msg)

@client.on(events.NewMessage(incoming=True))
async def auto_save(event):
    """الحفظ التلقائي بدون أي أوامر"""
    if event.is_private and event.media:
        try:
            media_path = await event.download_media()
            caption = f"""
𓏺 𝘼𝙐𝙏𝙊 𝙎𝘼𝙑𝙀𝘿 𓏺
• المرسل : {event.sender.first_name}
• التاريخ : {event.date.strftime("%Y-%m-%d")}
• اليوم : {ARABIC_DAYS[event.date.strftime("%A")]}
            """
            await client.send_file('me', media_path, caption=caption)
            os.remove(media_path)
        except Exception as e:
            print(f'𓆰 خطأ تلقائي: {e}')

if __name__ == "__main__":
    print("𓆰 جاري تشغيل نظام الجوكر الذكي..")
    client.start(phone=phone_number)
    print("𓆰 النظام يعمل الآن بشكل مثالي!")
    client.run_until_disconnected()
