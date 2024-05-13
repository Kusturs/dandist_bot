from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

menu_kb = ReplyKeyboardMarkup(
	resize_keyboard = True,
	one_time_keyboard = True,
	keyboard = [[KeyboardButton(text = 'Меню')]]
)

menu_service = InlineKeyboardMarkup(
	inline_keyboard = [
		[InlineKeyboardButton(text = 'Услуги', callback_data = 'services')],
		[InlineKeyboardButton(text = 'Записаться', url = 'https://t.me/Aeto_y')],
		[InlineKeyboardButton(text = 'Оставить отзыв', callback_data = 'feedback')],
		[InlineKeyboardButton(text = "Отзывы", callback_data = "reviews")]
	]
)

back = InlineKeyboardMarkup(inline_keyboard = [[InlineKeyboardButton(text = 'Назад', callback_data = 'back')]])

service_buttons = InlineKeyboardMarkup(
	inline_keyboard = [
		[InlineKeyboardButton(text = 'Профессиональная гигиена полости рта', callback_data = 'professional hygiene')],
		[InlineKeyboardButton(text = 'Лечение кариеса', callback_data = 'caries treatment')],
		[InlineKeyboardButton(text = 'Отбеливание зубов', callback_data = 'teeth whitening')],
		[InlineKeyboardButton(text = 'Протезирование', callback_data = 'prosthetics')],
		[InlineKeyboardButton(text = 'Назад', callback_data = 'menu services')]
	]
)

whitening_menu = InlineKeyboardMarkup(
	inline_keyboard = [
		[InlineKeyboardButton(text = 'Химическое отбеливание', callback_data = 'chemical_bleaching')],
		[InlineKeyboardButton(text = 'Фото отбеливания', callback_data = 'photo_bleaching')],
		[InlineKeyboardButton(text = 'Назад', callback_data = 'back')]
	]
)

back_to_whitening_menu = InlineKeyboardMarkup(
	inline_keyboard = [[InlineKeyboardButton(text = 'Назад', callback_data = 'teeth whitening')]]
)

prosthetic_menu = InlineKeyboardMarkup(
	inline_keyboard = [
		[InlineKeyboardButton(text = 'коронок и мостовидных протезов', callback_data = 'pros_1')],
		[InlineKeyboardButton(text = 'съёмных конструкций', callback_data = 'pros_2')],
		[InlineKeyboardButton(text = 'Назад', callback_data = 'back')]
	]
)

back_to_prosthetic_menu = InlineKeyboardMarkup(
	inline_keyboard = [[InlineKeyboardButton(text = 'Назад', callback_data = 'prosthetics')]]
)

scroll_reviews = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton(text = 'Предыдущий', callback_data = 'previous_review'),
			InlineKeyboardButton(text = 'Следующий', callback_data = 'next_review')
		],
		[InlineKeyboardButton(text = 'Назад', callback_data = 'menu services')]
	]
)

marks_kb = ReplyKeyboardMarkup(
	resize_keyboard = True,
	input_field_placeholder = 'Выберите оценку...',
	keyboard = [
		[KeyboardButton(text = '1'), KeyboardButton(text = '2')],
		[KeyboardButton(text = '3'), KeyboardButton(text = '4')],
		[KeyboardButton(text = '5')]
	]
)
