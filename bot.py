#библиотеки, которые загружаем из вне
# В google colab добавить: !pip install pyTelegramBotAPI
import telebot
TOKEN = 'Вставь сюда свой токен'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("🧡 Мой репозиторий")
	item2 = types.KeyboardButton("😋 Написать мне в личку")
	item3 = types.KeyboardButton("🎸 Плейлист для осеннего настроения")
	item4 = types.KeyboardButton("📚 Почитать побольше про тестирование")

	markup.add(item1, item2, item3, item4)

	bot.send_message(message.chat.id, "Привет тебе от котика, {0.first_name}!".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == '🧡 Мой репозиторий':
			bot.send_message(message.chat.id, 'https://github.com/Koteonova?tab=repositories')
		elif message.text == '😋 Написать мне в личку':
			bot.send_message(message.chat.id, 'https://t.me/Koteonova')
		elif message.text == '🎸 Плейлист для осеннего настроения':
			bot.send_message(message.chat.id, 'https://music.yandex.ru/users/ya.indietronica/playlists/1013?utm_medium=copy_link')
		elif message.text == '📚 Почитать побольше про тестирование':
			bot.send_message(message.chat.id, 'http://www.protesting.ru/')		
		else:
			bot.send_message(message.chat.id, 'Не знаю что ответить😢')


bot.polling(none_stop=True)

 







#https://core.telegram.org/bots/api#available-methods