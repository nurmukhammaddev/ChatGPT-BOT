import openai
import telebot
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")
bot = telebot.TeleBot(os.environ.get("TELEGRAM_BOT_TOKEN"))


@bot.message_handler(func=lambda _: True)
def handle_message(message):
    response = openai.Completion.create(
        engine="davinci",
        prompt=message.text,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n", " Human:", " AI:"],
    )
    bot.reply_to(message, response["choices"][0]["text"], parse_mode="Markdown")


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Hello, I am ChatGPT-3 bot. I can talk to you. Ask me anything")

    




if __name__ == "__main__":
    bot.polling()
    

