import telebot
bot = telebot.TeleBot('1143631384:AAHK53ua9WCbwR_g2I0bSTGgISDgSFS0DZQ')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	@bot.message_handler(content_types=['text', 'document', 'audio'])
	if message.text == 'Hi':
		bot.send_message(message.from_user.id, 'Hi, what you want?')

	elif message.text == '/help':
		bot.send_message(message.from_user.id, 'Type Hi')

	else:
		bot.send_message(message.from_user.id, 'Pshel naxui')


bot.polling(none_stop=False, intercal=0)

