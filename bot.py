from telegram import Update
from telegram.ext import Updater , CommandHandler, CallbackQueryHandler, CallbackContext,Filters,MessageHandler
import os

Token =os.environ.get("BOT_TOKEN",None)
updater = Updater( Token ,use_context = True )
def sum(a,b):
    return a+b



def start(updater,context):
 updater.message.reply_text('''Hi iam welcome messanger bot 
Add me to your group 
 
 

  ''')
def help(updater,context):
 updater.message.reply_text("Add me to your group ")
 

def add_group(update: Update, context: CallbackContext):
    for member in update.message.new_chat_members:
        update.message.reply_text(f'Hello {member.full_name}' +''' Benvenuto in BIT PoliMi!🚀

🎓 Siamo la prima associazione del Politecnico di Milano che si occupa di Bitcoin e crypto. Proponiamo progetti innovativi in grado di formarti su questo nuovo mondo.

📱Social:
Instagram: https://instagram.com/bitpolimi


📚 Materiale utile:
Mega: https://mega.nz/folder/juphlCAJ#VqPTgjSETFy8POmyW4W1kQ

📝 Ci sono poche regole da seguire:
- No scam
- No trading e finanza 
- No politica''', disable_web_page_preview=True)

def hello(string):
    print(f'Hello {string}')


add_group_handle = MessageHandler(Filters.status_update.new_chat_members, add_group)
updater.dispatcher.add_handler(add_group_handle)

dp =updater.dispatcher.add_handler
dp(CommandHandler('start',start))
dp(CommandHandler('help',help))

updater.start_polling()
updater.idle()
