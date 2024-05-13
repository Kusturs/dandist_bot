from aiogram import F, Router

from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keyboords as kb
import app.database.requests as rq

from sqlalchemy.orm.exc import NoResultFound


router = Router()
review_state = rq.ReviewState()


class Review(StatesGroup):
	review = State()
	mark = State()


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
	await rq.set_user(message.from_user.id)
	await message.answer(
		text =
		f'Привет, {message.from_user.full_name}, '
		f'я студент 5ого курса стоматологического факультета БГМУ,'
		f' в поиске пациентов для расширения личного портфолио. Нажмите на "Меню" для просмотра меню услуг.',
		reply_markup = kb.menu_kb
	)


@router.message(F.text == 'Меню')
async def cmd_start(message: Message) -> None:
	await message.delete()
	await message.answer(
		text = 'Для записи или дополнительной информации нажмите на "Записаться".\nВыберите вариант:',
		reply_markup = kb.menu_service
	)


@router.callback_query(F.data == 'services')
async def services_menu(callback: CallbackQuery) -> None:
	await callback.message.edit_text(
		text = 'Предоставляемые услуги:',
		reply_markup = kb.service_buttons
	)


@router.callback_query(F.data == 'professional hygiene')
async def services_menu(callback: CallbackQuery) -> None:
	await callback.message.edit_text(
		text = """
Профессиональная гигиена полости рта.
		
Процедура состоит из трёх этапов:

1 - Ультразвуковая чистка : 
проводится на специальном оборудовании – ультразвуковом скайлере. Оборудование излучает ультразвуковые волны различной амплитуды и частоты, ультразвуковая чистка помогает избавиться от затвердевшего налета, с которым невозможно справиться в ходе ежедневных гигиенических процедур. Даже при условии регулярной чистки и полоскании ротовой полости в труднодоступных местах могут скапливаться мелкие частицы пищи. Постепенно они трансформируются в налет и зубной камень. Справиться с ним может лишь профессиональный стоматолог в условиях специально оборудованного кабинета. Обеспечивающие эффективное очищение зубов от скопившихся на них отложений. 

2 - Полировка :
Полировка зубов предполагает использование стоматологических паст, каждая из которых имеет разную степень зернистости. Для придания блеска врач задействует аппаратные насадки – диски, головки, чашечки и т.д. После проведения процедуры зубы выглядят ровными, гладкими и здоровыми.


3 - Покрытие зубов фтор-лаком : 
Фторлак — это лекарственное средство предназначенное для профилактики кариозных поражений и укрепление эмали. Дополнительными его свойствами являются антибактериальный эффект и повышение эстетической привлекательности за счёт здорового блеска. Благодаря своим защитным свойствам лак не допускает микробного поражения и развития кариеса. Некоторые пациенты также отмечают снижение чувствительности после использования.""",
		reply_markup = kb.back
	)


@router.callback_query(F.data == 'caries treatment')
async def services_menu(callback: CallbackQuery) -> None:
	await callback.message.edit_text(
		text = """
Кариес – это процесс разрушения твердых тканей зуба, протекающий при участии кариесогенных бактерий полости рта (в составе зубного налета), а также перерабатываемых ими пищевых остатков. Вырабатываемые бактериями органические кислоты постепенно разрушают сначала зубную эмаль, а потом и подлежащий дентин. В результате этого в зубе формируется кариозная полость, стенки которой заполнены мягким распадом гниющих зубных тканей и большим количеством кариесогенных бактерий.

Лечение кариеса:
		
Лечение кариеса зубов – это процесс, который заключается в удалении пораженных кариесом участков зуба при помощи бормашины, после чего форма зуба восстанавливается при помощи пломбировочного материала. В качестве последних могут выступать композиты светового отверждения, компомеры или стеклоиономерные пломбировочные материалы.""",
		reply_markup = kb.back
	)


@router.callback_query(F.data == 'teeth whitening')
async def services_menu(callback: CallbackQuery) -> None:
	await callback.message.edit_text(
		text = 'Способ отбеливания:',
		reply_markup = kb.whitening_menu
	)


@router.callback_query(F.data == 'chemical_bleaching')
async def chemical_bleaching_info(callback: CallbackQuery) -> None:
	await callback.message.edit_text(
		text = """
Химическое отбеливание зубов:
		 
Лучший выбор, если вы хотите стать счастливым обладателем белоснежной голливудской улыбки быстро и без дополнительных рисков. Эта методика основана на применении состава с высокой концентрацией осветляющего вещества, оказывающего необходимое воздействие на эмаль, и всегда дает отличный результат ( 5 - 9 тонов )""",
		reply_markup = kb.back_to_whitening_menu
		)


@router.callback_query(F.data == 'photo_bleaching')
async def chemical_bleaching_info(callback: CallbackQuery) -> None:
	await callback.message.edit_text(
			text = """
Фото отбеливания:

Тличительной чертой является использование специального активного вещества – карбамида или перекиси водорода. Концентрация его в геле, который наносится на весь зубной ряд, может достигать до 35 %. Именно поэтому процедура занимает гораздо меньше времени, чем другие подобные отбеливающие методы. Активное вещество проникает внутрь ткани зуба и обесцвечивает пигментные участки. Для усиления эффективности геля используется свет и тепло специальной галогеновой лампы , эффект можно получить на 8 - 14 тонов .

Световой луч лампы запускает окислительные процессы, которые воздействуют только на органические соединения. При этом структура и состав зубной ткани не изменяется. Минеральные компоненты остаются на месте, поэтому эмаль не страдает. Метод абсолютно безопасен и не приводит к чрезмерной чувствительности зубов. Но концентрация активного вещества и время воздействия подбирается только врачом индивидуально, исходя из состояния эмали.""",
			reply_markup = kb.back_to_whitening_menu
			)


@router.callback_query(F.data == 'prosthetics')
async def back_to_menu(callback: CallbackQuery) -> None:
	await callback.message.edit_text(text = 'Протезирование с помощью', reply_markup = kb.prosthetic_menu)


@router.callback_query(F.data == 'pros_1')
async def services_menu(callback: CallbackQuery) -> None:
	await callback.message.edit_text(
		text = """
Протезирование с помощью коронок и мостовидных протезов:

Один из методов протезирования, направленный на восстановление зубной единицы. Данная технология протезирования зубов позволяет достичь сразу нескольких целей. Коронка позволяет защитить зуб, обеспечить его прочность, восстановить эстетику улыбки. Благодаря коронке зуб надежно защищен от негативных внешних воздействий и сохраняет привлекательность на долгие годы.
Протезирование зубов коронками рекомендовано в случаях, когда необходимо восстановить единицу, пострадавшую от кариеса, механической травмы или инфекции. Также метод позволяет скорректировать форму зуба, его размер, оттенок эмали.
Такая технология протезирования не оказывает негативного воздействия на мягкие ткани , а также позволяет изготовить коронку на 1 зуб или мост (при множественном отсутствии единиц).""",
		reply_markup = kb.back_to_prosthetic_menu
	)


@router.callback_query(F.data == 'pros_2')
async def services_menu(callback: CallbackQuery) -> None:
	await callback.message.edit_text(
		text = """
Протезирование с помощью съёмных конструкций : 

Съемные протезы – это конструкции, предназначенные для восстановления утраченных зубов, которые могут быть сняты и установлены пациентом самостоятельно.

Различают следующие виды съемных конструкций :
-Полные – крепятся к слизистой оболочке полости рта и поддерживаются при помощи вакуума, который создается между изделием и слизистыми тканями. Рекомендованы при полной адентии.
-Частичные – крепятся к оставшимся зубам с помощью крючков или других типов крепления. Крючки обеспечивают устойчивость и предотвращают смещение аппарата. Используются в случаях, когда пациенту не достает собственных зубов для установки несъемного аппарата.""",
		reply_markup = kb.back_to_prosthetic_menu
	)


@router.callback_query(F.data == 'back')
async def back_to_menu(callback: CallbackQuery) -> None:
	await callback.message.edit_text(text = 'Предоставляемые услуги', reply_markup = kb.service_buttons)


@router.callback_query(F.data == 'menu services')
async def services_menu(callback: CallbackQuery) -> None:
	await callback.message.edit_text(
		text = 'Для записи или дополнительной информации нажмите на "Записаться".\nВыберите вариант:',
		reply_markup = kb.menu_service
	)


@router.callback_query(F.data == 'feedback')
async def get_rev(callback: CallbackQuery, state: FSMContext) -> None:
	await callback.answer()
	await state.set_state(Review.review)
	await callback.message.answer("Введите отзыв:")


@router.message(Review.review)
async def get_mark(message: Message, state: FSMContext) -> None:
	review = message.text
	if not review or len(review) > 1500:
		await message.answer(text = "Длина отзыва не более чем 1500 символов, попробуйте еще раз.")
	else:
		await state.update_data(review = review)
		await state.set_state(Review.mark)
		await message.answer(text = 'Выберите оценку: ', reply_markup = kb.marks_kb)


@router.message(Review.mark)
async def set_data(message: Message, state: FSMContext) -> None:
	mark = message.text
	if not mark.isdigit() or int(mark) < 1 or int(mark) > 5:
		await message.answer(
			text = "Вы ввели некорректную оценку. Пожалуйста, введите число от 1 до 5.",
			reply_markup = kb.marks_kb
		)
	else:
		await state.update_data(mark = mark)
		data = await state.get_data()
		await rq.set_user_review(
			tg_id = message.from_user.id, review = data['review'], mark = data['mark']
		)
		await message.answer(text = f'Спасибо за ваш отзыв', reply_markup = kb.menu_kb)
		await state.clear()


@router.callback_query(F.data == 'reviews')
async def check_reviews(callback: CallbackQuery) -> None:
	try:
		formatted_text = await review_state.get_review()
		await callback.answer()
		await callback.message.edit_text(text = formatted_text, reply_markup = kb.scroll_reviews)
	except NoResultFound:
		await callback.answer("Отзывов пока нет. Вы можете оставить свой отзыв!")


@router.callback_query(F.data == 'next_review')
async def next_review(callback: CallbackQuery) -> None:
	max_user_id = await rq.get_max_review_id()
	if review_state.user_id < max_user_id:
		review_state.user_id += 1
	else:
		review_state.user_id = 1
	formatted_text = await review_state.get_review()
	await callback.answer()
	await callback.message.edit_text(text = formatted_text, reply_markup = kb.scroll_reviews)


@router.callback_query(F.data == 'previous_review')
async def previous_review(callback: CallbackQuery) -> None:
	if review_state.user_id > 1:
		review_state.user_id -= 1
	else:
		max_user_id = await rq.get_max_review_id()
		review_state.user_id = max_user_id
	formatted_text = await review_state.get_review()
	await callback.answer()
	await callback.message.edit_text(text = formatted_text, reply_markup = kb.scroll_reviews)
