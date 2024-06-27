import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Вставьте ваш токен ниже
TOKEN = '7413028484:AAG04TTImMneLNirCq8SeESdorD-0m9uv_A'

# Включение логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(name)

# Обработчик команды /start
def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Заведения", callback_data='1'),
            InlineKeyboardButton("Мануалы", url='https://telegra.ph/Konsum-manual-03-08'),
        ],
        [
            InlineKeyboardButton("Где искать?", callback_data='3'),
            InlineKeyboardButton("Шаблон", callback_data='4'),
        ],
        [
            InlineKeyboardButton("Топ", callback_data='5'),
            InlineKeyboardButton("Запреты", callback_data='6'),
        ],
        [
            InlineKeyboardButton("Чат", url='https://t.me/+PGwd_Cuf9X01ZTli'),
            InlineKeyboardButton("Выплаты", url='https://t.me/+B8mWIB8vq8czZGMy'),
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Замените путь к файлу на путь к вашему изображению
    with open('https://a.radikalfoto.host/2024/06/27/photo_2024-01-28_14-50-38.jpeg', 'rb') as photo:
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo)
    update.message.reply_text('Выберите опцию:', reply_markup=reply_markup)

# Обработчик кнопок
def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    if query.data == '1':
        query.edit_message_text(text="ПЕРВАЯ ТОЧКА!\n\n"
                                     "Ⓜ️Метро: БЕГОВАЯ - 7 фиолетовая линия\n"
                                     "1 • 2 Выход ВСТРЕЧАЮТ\n\n"
                                     "📍Адреса:\n\n"
                                     "➡️1-й Хорошёвский проезд, 12к1(аптека)\n"
                                     "➡️1-й Хорошёвский проезд, 14к1 (магазин продуктов-ароматный мир)\n"
                                     "➡️1-й Хорошёвский проезд, 5(НИИ мин.обороны)\n"
                                     "➡️Хорошёвское шоссе 16с3 (ТЦ на беговой+парковка)\n"
                                     "➡️Беговая 1А (копия Москва- ремонт фотоаппаратов)\n\n"
                                     "🕖 ГРАФИК РАБОТЫ ЗАВЕДЕНИЯ:\n\n"
                                     "Пн-Пт: 18:00-01:00\n"
                                     "Сб-Вс: 18:00-01:30\n\n"
                                     "ВТОРАЯ ТОЧКА !!\n\n"
                                     "🏠МЕТРО: Крылатское (3,4,5,6,7 выходы,3 синяя линия)🚉\n"
                                     "НА 1,2 ВЫХОД НЕ ВЕДЕМ💗💗💗\n\n"
                                     "ВЕДЕМ СТРОГО НА АДРЕСА\n\n"
                                     "💗Осенний бульвар, 8к2 (жилой дом )\n"
                                     "💗Осенний бульвар, 3 (жилой дом )\n"
                                     "💗Осенний бульвар, 10к1 (жилой дом)\n"
                                     "💗Осенний бульвар, 12к3 (жилой дом )\n"
                                     "💗Осенний бульвар, 16к2(жилой дом)\n\n"
                                     "ПАРКОВКА 🤍\n"
                                     "АБСОЛЮТНО У КАЖДОГО АДРЕСА ЕСТЬ ГДЕ ПОСТАВИТЬ ТАЧКУ!\n"
                                     "Это жилые дома 🏠\n\n"
                                     "Время работы \n"
                                     "С 17:00-01:00+-02:00\n\n"
                                     "ТРЕТЬЯ ТОЧКА !!\n\n"
                                     "📍Метро: Университет (красная ветка, 2 выход, возле метро НЕ встречают, вести на адреса)\n"
                                     "Выходишь, идешь прямо к главной дороге, на ломоносовском проспекте идешь на право\n\n"
                                     "✨АДРЕС ВСТРЕЧИ:\n"
                                     "🟡Ленинский проспект 68 (шоколадница)\n"
                                     "🟡Ломоносовский проспект 15 (жилой дом)\n\n"
                                     "✨ПАРКОВКИ:\n"
                                     "🟡Ломоносовский проспект 17 (театр Джигарханяна)\n"
                                     "🟡Ломоносовский проспект 19 (жилой дом)")
    elif query.data == '3':
        query.edit_message_text(text="➡️https://beboo.ru\n"
                                     "➡️https://tabor.ru\n"
                                     "➡️https://love.mail.ru\n"
                                     "➡️http://loveplanet.ru\n"
                                     "➡️https://juliadates.com\n"
                                     "➡️https://linkyou.ru\n"
                                     "➡️https://topface.com\n"
                                     "➡️https://www.mamba.ru\n"
                                     "➡️https://vk.com\n"
                                     "➡️https://badoo.ru\n"
                                     "➡️https://www.edarling.ru\n"
                                     "➡️https://dating.ru\n"
                                     "➡️https://love.ru\n"
                                     "➡️https://loveplanet.ru\n"
                                     "➡️https://fotostrana.ru\n"
                                     "➡️https://azbyka.ru/znakomstva\n"
                                     "➡️https://onlynudes.net\n"
                                     "➡️https://t.me/Swipix_Bot\n"
                                     "➡️https://t.me/leomatchbot")
    elif query.data == '4':
        query.edit_message_text(text="Создание анкеты\n"
                                     "Анкета пишется одним сообщением, для повышения читаемости анкеты между блоками можете поставить отсутп 2 строки.\n\n"
                                     "1. О столе:\n"
                                     "1. Имя 'Стола'\n\n"
                                     "2. Возраст 'Стола'\n\n"
                                     "3. Национальность 'Стола'\n\n"
                                     "4. Профессия и место работы 'Стола'\n\n"
                                     "5. Номер телефона 'Стола'\n\n"
                                     "6. Дополнительная информация о 'Столе' (хобби, увлечения, события про которые говорил, о чем шла речь и прочие моменты, которые могут упоминаться или о которых может пойти речь, когда промо встретит стол)\n\n"
                                     "2. О девушке:\n"
                                     "1. Фото 'Девушки'\n\n"
                                     "2. Имя 'Девушки'\n\n"
                                     "3. Возраст 'Девушки'\n\n"
                                     "4. Профессия 'Девушки'\n\n"
                                     "5. Дополнительная информация о 'Девушке' (хобби, увлечения, с кем живёт, события про которые говорилось, и прочие моменты, о которых стол может спросить промо, или о которых может пойти речь)\n\n"
                                     "3. Встреча:\n"
                                     "1. Время встречи (мск)\n\n"
                                     "2. Адрес встречи\n\n"
                                     "3. Цель встречи (ужин/кальян/свидание и прочее)\n\n"
                                     "4. Где и когда познакомились (сайт знакомства, чат и прочее)\n\n"
                                     "5. Где велось общение\n\n"
                                     "4. Прикрепить:\n"
                                     "Фотография 'стола' (1 шт.)\n"
                                     "Фотография девушки (1 шт.)\n"
                                     "Скриншот сообщения, где он говорил что согласен поужинать/посидеть в каком-то заведении/выбрать заведение на месте\n"
                                     "Анкеты на нетиповые столы\n"
                                     "В случае, если стол - парка/банкет/трио, также обязательно прикрепляются фотографии всех участников стола, и о каждом из участников обязательно заполняется имя, возраст, нация, место работы.\n\n"
                                     "Номера телефона достаточно одного")
        elif query.data == '5':
        query.edit_message_text(text="🏆 Статистика команды за всё время:\n\n"
                                     "💸 Топ 5 лучших оператора по кассе:\n"
                                     "/id1 - 466676₽\n"
                                     "/id3 - 189829₽\n"
                                     "/id7 - 160915₽\n"
                                     "/id2 - 149198₽\n"
                                     "/id85 - 130650₽\n"
                                     "________________________\n"
                                     "💳 Топ 5 лучших оператора по количеству оплат:\n"
                                     "/id1 - 20\n"
                                     "/id2 - 12\n"
                                     "/id94 - 6\n"
                                     "/id3 - 5\n"
                                     "/id7 - 5\n"
                                     "________________________\n"
                                     "🧾 Топ 5 больших чекa:\n"
                                     "/id3 - 112900₽\n"
                                     "/id33 - 85620₽\n"
                                     "/id7 - 52000₽\n"
                                     "/id1 - 50000₽\n"
                                     "/id85 - 47000₽\n"
                                     "________________________\n"
                                     "💰 Общая касса: 1557390₽")
    elif query.data == '6':
        query.edit_message_text(text="Нации:\n"
                                     "Дагестан Кавказ : аварцы, агулы, даргинцы, осетины, кабардинцев, кумыки, лакцы, лезгины, таты, табасараны, рутульцы, цахуры, чеченцы-аккинцы, андийцы, арчинцы, ахвахцы, багулалы, бежтинцы, ботлихцы, гинухцы, годоберинцы, гунзибцы, каратинцы, тиндинцы, хваршины, чамалинцы, цезы, кайтагцы, кубачинцы, лезгины, кабардинцы, осетины\n"
                                     "❌Чеченцы\n"
                                     "❌Ингуши\n"
                                     "❌Негры\n"
                                     "❌Еврей\n"
                                     "❌Кубинец\n"
                                     "❌Индус\n"
                                     "❌Памирцы\n\n"
                                     "📝СПИСОК ЗАПРЕТ МАМОНТОВ ❌\n\n"
                                     "🐰(ВЫУЧИТЬ КАК МОЛИТВУ И НЕ СПРАШИВАТЬ ПО МИЛЛИОН РАЗ)\n\n"
                                     "🍭ПРОФЕССИИ:\n"
                                     "     ❌МВД\n"
                                     "     ❌Следственный комитет\n"
                                     "     ❌Юристы\n"
                                     "     ❌Адвокаты\n"
                                     "     ❌Прокуроры\n"
                                     "     ❌Росгврадия\n"
                                     "     ❌ОМОН\n"
                                     "     ❌ФСБ\n"
                                     "     ❌ФСО\n"
                                     "     ❌Работники посольства любой страны\n"
                                     "     ❌Прокуроры\n"
                                     "     ❌Журналисты\n"
                                     "     ❌Профессии, которые связаны с\n"
                                     "     ❌СМИ в предоставлении материалов\n"
                                     "     ❌Блогеры (ютуберы, тиктокеры, инста блогеры)\n"
                                     "     ❌Налоговая(не вся, но уточняйте)\n"
                                     "     ✅МЧС, РЖД, ВОЕННЫХ, ВРАЧЕЙ И Т.Д МОЖНО\n\n"
                                     "😑ЕСЛИ У СТОЛА ЕСТЬ ДРУЗЬЯ ПРОКУРОРЫ/МВД/ОМОН и тд, ТО НЕЛЬЗЯ ВЕСТИ ЭТОТ СТОЛ😑\n\n"
                                     "❌Также не водим инвалидов и стариков по моральным соображениям❌\n\n"
                                     "🤩Возраст от:\n"
                                     "👍21-60 (Ру желательно 23+, если меньше то Ваш стол должен был обработан на рестик/бар/кальян)")
        # Обработчик команды /adr
def adr(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("ПЕРВАЯ ТОЧКА!\n\n"
                              "Ⓜ️Метро: БЕГОВАЯ - 7 фиолетовая линия\n"
                              "1 • 2 Выход ВСТРЕЧАЮТ\n\n"
                              "📍Адреса:\n\n"
                              "➡️1-й Хорошёвский проезд, 12к1(аптека)\n"
                              "➡️1-й Хорошёвский проезд, 14к1 (магазин продуктов-ароматный мир)\n"
                              "➡️1-й Хорошёвский проезд, 5(НИИ мин.обороны)\n"
                              "➡️Хорошёвское шоссе 16с3 (ТЦ на беговой+парковка)\n"
                              "➡️Беговая 1А (копия Москва- ремонт фотоаппаратов)\n\n"
                              "🕖 ГРАФИК РАБОТЫ ЗАВЕДЕНИЯ:\n\n"
                              "Пн-Пт: 18:00-01:00\n"
                              "Сб-Вс: 18:00-01:30\n\n"
                              "ВТОРАЯ ТОЧКА !!\n\n"
                              "🏠МЕТРО: Крылатское (3,4,5,6,7 выходы,3 синяя линия)🚉\n"
                              "НА 1,2 ВЫХОД НЕ ВЕДЕМ💗💗💗\n\n"
                              "ВЕДЕМ СТРОГО НА АДРЕСА\n\n"
                              "💗Осенний бульвар, 8к2 (жилой дом )\n"
                              "💗Осенний бульвар, 3 (жилой дом )\n"
                              "💗Осенний бульвар, 10к1 (жилой дом)\n"
                              "💗Осенний бульвар, 12к3 (жилой дом )\n"
                              "💗Осенний бульвар, 16к2(жилой дом)\n\n"
                              "ПАРКОВКА 🤍\n"
                              "АБСОЛЮТНО У КАЖДОГО АДРЕСА ЕСТЬ ГДЕ ПОСТАВИТЬ ТАЧКУ!\n"
                              "Это жилые дома 🏠\n\n"
                              "Время работы\n"
                              "С 17:00-01:00+-02:00\n\n"
                              "ТРЕТЬЯ ТОЧКА !!\n\n"
                              "📍Метро: Университет (красная ветка, 2 выход, возле метро НЕ встречают, вести на адреса)\n"
                              "Выходишь, идешь прямо к главной дороге, на ломоносовском проспекте идешь на право\n\n"
                              "✨АДРЕС ВСТРЕЧИ:\n"
                              "🟡Ленинский проспект 68 (шоколадница)\n"
                              "🟡Ломоносовский проспект 15 (жилой дом)\n\n"
                              "✨ПАРКОВКИ:\n"
                              "🟡Ломоносовский проспект 17 (театр Джигарханяна)\n"
                              "🟡Ломоносовский проспект 19 (жилой дом)")

# Обработчик команды /top
def top(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("🏆 Статистика команды за всё время:\n\n"
                              "💸 Топ 5 лучших оператора по кассе:\n"
                              "/id1 - 466676₽\n"
                              "/id3 - 189829₽\n"
                              "/id7 - 160915₽\n"
                              "/id2 - 149198₽\n"
                              "/id85 - 130650₽\n"
                              "________________________\n"
                              "💳 Топ 5 лучших оператора по количеству оплат:\n"
                              "/id1 - 20\n"
                              "/id2 - 12\n"
                              "/id94 - 6\n"
                              "/id3 - 5\n"
                              "/id7 - 5\n"
                              "________________________\n"
                              "🧾 Топ 5 больших чекa:\n"
                              "/id3 - 112900₽\n"
                              "/id33 - 85620₽\n"
                              "/id7 - 52000₽\n"
                              "/id1 - 50000₽\n"
                              "/id85 - 47000₽\n"
                              "________________________\n"
                              "💰 Общая касса: 1557390₽")

def main() -> None:
    # Создаем объект Updater и передаем ему токен вашего бота
    updater = Updater("7413028484:AAG04TTImMneLNirCq8SeESdorD-0m9uv_A")

    # Получаем диспетчер для регистрации обработчиков
    dispatcher = updater.dispatcher
    # Регистрируем обработчик для команды /start
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button))

    # Регистрируем обработчики для команд /adr и /top
    dispatcher.add_handler(CommandHandler("adr", adr))
    dispatcher.add_handler(CommandHandler("top", top))

    # Запускаем бота
    updater.start_polling()

    # Запускаем бота до тех пор, пока пользователь не нажмет Ctrl-C
    updater.idle()

if name == 'main':
    main()