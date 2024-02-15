import logging
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, filters, MessageHandler, ContextTypes

load_dotenv()
API_KEY=os.getenv('API_KEY')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
originalText = ""
newText1 = ""
newText2 = ""
shill = True





# Function to find and replace all text before the designated string
def before_string(input_string, search_string):
    index = input_string.find(search_string)
    print(index) # remove later when working
    if index != -1:  # if the search string is found
        return input_string[index:]
    return input_string

#Function to find and replace all text after the designated string
def after_string(input_string, search_string):
    index = input_string.find(search_string)
    if index != -1:  # if the search string is found
        return input_string[:index + len(search_string)]
    return input_string







async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def toggle_shill(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global shill
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Shill Toggled!")
    if (shill == True):
        shill = not shill
        print("set shill false")
    else:
        shill = not shill
        print("set shill true")








async def replace(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global shill
    if update.message.text.__contains__("https://twitter.com"):
        #set the source text to originalText
        originalText = update.message.text
        print("origninal: " + originalText)
        #find and delete everything BEFORE the url
        newText1 = before_string(originalText, "https://twitter.com")
        print("text before deleted:"  + newText1)
        #find and delete everything AFTER the url
        newText2 = after_string(after_string(newText1, " "), "\n")
        print("text before and after deleted: " + newText2)
        #replace the original link with the embeddable one
        finalText = newText2.replace("https://twitter.com", "https://fxtwitter.com")
        print("final with link replaced: " + finalText)
        #send the new link back to the chat
        await context.bot.send_message(chat_id=update.effective_chat.id,text=finalText)
        if shill == True:
            await context.bot.send_message(chat_id=update.effective_chat.id, disable_web_page_preview=True,text=f'Thanks for using ***AutoEmbedder***\\! check out the [GitHub Repo](https://github\\.com\\/stationswift001\\/AutoEmbedder) for more info',parse_mode='MarkdownV2')

    else:
        if update.message.text.__contains__("https://x.com"):
            # set the source text to originalText
            originalText = update.message.text
            print("origninal: " + originalText)
            # find and delete everything BEFORE the url
            newText1 = before_string(originalText, "https://x.com")
            print("text before deleted:" + newText1)
            # find and delete everything AFTER the url
            newText2 = after_string(after_string(newText1, " "), "\n")
            print("text before and after deleted: " + newText2)
            # replace the original link with the embeddable one
            finalText = newText2.replace("https://x.com", "https://fixupx.com")
            print("final with link replaced: " + finalText)
            # send the new link back to the chat
            await context.bot.send_message(chat_id=update.effective_chat.id, text=finalText)
            if shill == True:
                await context.bot.send_message(chat_id=update.effective_chat.id, disable_web_page_preview=True, text=f'Thanks for using ***AutoEmbedder***\\! check out the [GitHub Repo](https://github\\.com\\/stationswift001\\/AutoEmbedder) for more info', parse_mode='MarkdownV2')
        else:
            if update.message.text.__contains__("https://www.instagram.com"):
                # set the source text to originalText
                originalText = update.message.text
                print("origninal: " + originalText)
                # find and delete everything BEFORE the url
                newText1 = before_string(originalText, "https://www.instagram.com")
                print("text before deleted:" + newText1)
                # find and delete everything AFTER the url
                newText2 = after_string(after_string(newText1, " "), "\n")
                print("text before and after deleted: " + newText2)
                # replace the original link with the embeddable one
                finalText = newText2.replace("https://www.instagram.com", "https://www.ddinstagram.com")
                print("final with link replaced: " + finalText)
                # send the new link back to the chat
                await context.bot.send_message(chat_id=update.effective_chat.id, text=finalText)
                if shill == True:
                    await context.bot.send_message(chat_id=update.effective_chat.id, disable_web_page_preview=True, text=f'Thanks for using ***AutoEmbedder***\\! check out the [GitHub Repo](https://github\\.com\\/stationswift001\\/AutoEmbedder) for more info', parse_mode='MarkdownV2')
            else:
                if update.message.text.__contains__("https://www.tiktok.com"):
                    # set the source text to originalText
                    originalText = update.message.text
                    print("origninal: " + originalText)
                    # find and delete everything BEFORE the url
                    newText1 = before_string(originalText, "https://www.tiktok.com")
                    print("text before deleted:" + newText1)
                    # find and delete everything AFTER the url
                    newText2 = after_string(after_string(newText1, " "), "\n")
                    # replace the original link with the embeddable one
                    finalText = newText2.replace("https://www.tiktok.com", "https://www.vxtiktok.com")
                    print("final with link replaced: " + finalText)
                    # send the new link back to the chat
                    await context.bot.send_message(chat_id=update.effective_chat.id, text=finalText)
                    if shill == True:
                        await context.bot.send_message(chat_id=update.effective_chat.id, disable_web_page_preview=True, text=f'Thanks for using ***AutoEmbedder***\\! check out the [GitHub Repo](https://github\\.com\\/stationswift001\\/AutoEmbedder) for more info', parse_mode='MarkdownV2')


if __name__ == '__main__':
    application = ApplicationBuilder().token(API_KEY).build()
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), replace)
    start_handler = CommandHandler('start', start)
    shill_handler = CommandHandler('ToggleShill', toggle_shill)
    application.add_handler(start_handler)
    application.add_handler(shill_handler)
    application.add_handler(echo_handler)
    application.run_polling()
