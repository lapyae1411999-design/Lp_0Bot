import telebot

TOKEN = '7131767175:AAHkt0NVixjfuJmzikVEcgvkYp_GGXUnXt4' 
bot = telebot.TeleBot(TOKEN)

RESPONSES = {
    'လီး': "မမိုက်ရိုင်းနဲ့!",
    'bot': "ခင်ဗျာ",
    'လပြည့်': "မခေါ်နဲ့မရှိဘူး",
    'အောင်ဖြိုးပိုင်': "အဲ့ကောင်ကgayနေတာ🫠",
    'ဖြိုးဇော်အောင်': "စော်ကြောက်ကောင်",
    'ဇင်မင်းထွန်း': "မအေလိုး",
    'ဟုပ်လား': "အင်း",
    'ဖင်ချ': "လာလာ",
    'ဟ': "မဟနဲ့စိထား",
    'ဖိုးဇေ': "သွားမခေါ်နဲ့Ygမှာဖx်ခံနေတာ🗿",
   'ဘာဖစ်လဲ': "ဖx်ချချင်တာ",
   'ဟိုင်း': "ဟယ်လိုအချောလေး",
   'ဘယ်သူမှမရှိ': "mgဘော့ရှိပါတယ်",
   'ပျင်း': "ဖx်ခံကြည့်",
   'aw': "မအော်နဲ့လေ",
   'mmsp': "အဲ့တာဘာလဲ",
   'ရိုင်း': "ရိုးသားကြိုးစားတဲ့ မောင်ဘော့လေးပါ"}

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "ဘာမှမလုပ်ဘူးဘာမှလာမခိုင်းနဲ့")

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    user_text_lower = message.text.strip().lower() 
    
    found_keyword = None
    
    for keyword, reply_text in RESPONSES.items():
        if keyword in user_text_lower:
            found_keyword = keyword
            break 
            
    if found_keyword:
        bot.reply_to(message, RESPONSES[found_keyword])

print("Bot Started...")
bot.polling()
