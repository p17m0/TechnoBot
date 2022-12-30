import logging, time, datetime

from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (Application,
                          CommandHandler,
                          ContextTypes,
                          MessageHandler,
                          filters,
                          ConversationHandler,)

import data.database as db
import data.core as core


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Приветствие бота."""
    user = update.effective_user
    time_alarm = datetime.datetime.now()
    if time_alarm.strftime('%d.%m.%y') in ('30.12.22',):
        if not db.check_user(user.id):
            
            await update.message.reply_text(core.start_phrase)
            time.sleep(1)
            keyboard = [
                ['Заполнить форму для участия'],
            ]
            reply_markup_start = ReplyKeyboardMarkup(keyboard)
            photo = open('data/for_bot/first.jpg', 'rb')
            await update.message.reply_photo(photo)
            await update.message.reply_text("Для участия в Январском квесте, просим вас заполнить короткую форму с именем ребенка",
                                            reply_markup=reply_markup_start)
            print(datetime.datetime.now())
            time_alarm = datetime.datetime(2022, 12, 31, 17, 0)
            user_data = context.user_data
            # Запускает таймер регистрации
            job = context.job_queue.run_once(registration_alarm, time_alarm, chat_id=user.id)
            user_data[f'{user.id}job'] = job.id
        else:
            reply_markup_menu = ReplyKeyboardMarkup(core.keyboard_menu)
            await update.message.reply_text("Вы перезапустили меня :)", reply_markup=reply_markup_menu)

async def registration_alarm(context: ContextTypes.DEFAULT_TYPE) -> None:
    """Напоминает о регистрации в 20:00."""
    logger.info('Сработал таймер регистрации.')
    job = context.job
    await context.bot.send_message(job.chat_id, text='Для участия в Январском квесте,просим вас заполнить короткую форму с именем ребенка.')
    job.schedule_removal()

async def first_day_alarm(context: ContextTypes.DEFAULT_TYPE) -> None:
    """Открытие вопроса №1."""
    logger.info('Сработал 1 день.')
    job = context.job
    await context.bot.send_message(job.chat_id, text="Вопрос №1 открыт!🎓")
    job.schedule_removal()

async def second_day_alarm(context: ContextTypes.DEFAULT_TYPE) -> None:
    """Открытие вопроса №2."""
    logger.info('Сработал 2 день.')
    job = context.job
    await context.bot.send_message(job.chat_id, text="Вопрос №2 открыт!🎓")
    job.schedule_removal()

async def third_day_alarm(context: ContextTypes.DEFAULT_TYPE) -> None:
    """Открытие вопроса №3."""
    logger.info('Сработал 3 день.')
    job = context.job
    await context.bot.send_message(job.chat_id, text="Вопрос №3 открыт!🎓")
    job.schedule_removal()

async def fourth_day_alarm(context: ContextTypes.DEFAULT_TYPE) -> None:
    """Открытие вопроса №4."""
    logger.info('Сработал 4 день.')
    job = context.job
    await context.bot.send_message(job.chat_id, text="Вопрос №4 открыт!🎓")
    job.schedule_removal()

async def fifth_day_alarm(context: ContextTypes.DEFAULT_TYPE) -> None:
    """Открытие вопроса №5."""
    logger.info('Сработал 5 день.')
    job = context.job
    await context.bot.send_message(job.chat_id, text="Вопрос №5 открыт!🎓")
    job.schedule_removal()

async def sixth_day_alarm(context: ContextTypes.DEFAULT_TYPE) -> None:
    """Открытие вопроса №5."""
    logger.info('Сработал 6 день.')
    job = context.job
    await context.bot.send_message(job.chat_id, text="Вопрос №6 открыт!🎓")
    job.schedule_removal()

async def seventh_day_alarm(context: ContextTypes.DEFAULT_TYPE) -> None:
    """Открытие вопроса №5."""
    logger.info('Сработал 5 день.')
    job = context.job
    await context.bot.send_message(job.chat_id, text="Вопрос №7 открыт!🎓")
    job.schedule_removal()

async def eighth_day_alarm(context: ContextTypes.DEFAULT_TYPE) -> None:
    """Открытие вопроса №5."""
    logger.info('Сработал 5 день.')
    job = context.job
    await context.bot.send_message(job.chat_id, text="Вопрос №8 открыт!🎓")
    job.schedule_removal()

async def notification_1(context: ContextTypes.DEFAULT_TYPE) -> None:
    """Напоминание 1."""
    logger.info('Сработало напоминание дня 1.')
    job = context.job
    await context.bot.send_message(job.chat_id, text="Я до сих пор не получил от вас ответа 👀")
    job.schedule_removal()

async def notification_2(context: ContextTypes.DEFAULT_TYPE) -> None:
    """Напоминание 2."""
    logger.info('Сработало напоминание дня 2.')
    job = context.job
    await context.bot.send_message(job.chat_id, text="Я до сих пор не получил от вас ответа 👀")
    job.schedule_removal()

async def notification_3(context: ContextTypes.DEFAULT_TYPE) -> None:
    """Напоминание 3."""
    logger.info('Сработало напоминание дня 3.')
    job = context.job
    await context.bot.send_message(job.chat_id, text="Я до сих пор не получил от вас ответа 👀")
    job.schedule_removal()

async def notification_4(context: ContextTypes.DEFAULT_TYPE) -> None:
    """Напоминание 4."""
    logger.info('Сработало напоминание дня 4.')
    job = context.job
    await context.bot.send_message(job.chat_id, text="Я до сих пор не получил от вас ответа 👀")
    job.schedule_removal()

async def notification_5(context: ContextTypes.DEFAULT_TYPE) -> None:
    """Напоминание 5."""
    logger.info('Сработало напоминание дня 5.')
    job = context.job
    await context.bot.send_message(job.chat_id, text="Я до сих пор не получил от вас ответа 👀")
    job.schedule_removal()

async def notification_6(context: ContextTypes.DEFAULT_TYPE) -> None:
    """Напоминание 6."""
    logger.info('Сработало напоминание дня 6.')
    job = context.job
    await context.bot.send_message(job.chat_id, text="Я до сих пор не получил от вас ответа 👀")
    job.schedule_removal()

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Помощь."""
    await update.message.reply_text("Привет! Я - ТехноРобби, чатбот центра ТЕХНОШКОЛЫ! Есть вопросы ко мне? - Звоните: 8(495)150-17-12")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Помощь."""
    await update.message.reply_text("Прости, но не я не понимаю человеческий, я запрограммирован предоставлять вопросы")

async def data(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Данные."""
    db.take_all_info()
    data = open("data/from_bot/data.xlsx", 'rb')
    await update.message.reply_document(data)


async def start_form(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Запуск формы регистрации."""
    user = update.message.from_user
    user_data = context.user_data
    user_data[user.id] = {}
    await update.message.reply_text(
        "Укажите ФИО ученика в формате: 'Иванов Иван Иванович'",
        reply_markup=ReplyKeyboardRemove()
    )
    return core.FIO

async def fio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the selected FIO and asks for a number."""
    user = update.message.from_user
    user_data = context.user_data
    user_data[user.id].update({'fio': update.message.text})
    logger.info("name of %s: %s", user.first_name, update.message.text)
    await update.message.reply_text(
        "Укажите в номер телефона",
    )

    return core.TELEPHONE_NUMBER


async def number(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the selected number."""
    user = update.message.from_user
    user_data = context.user_data
    user_data[user.id].update({'number': update.message.text})
    logger.info("name of %s: %s", user.first_name, update.message.text)

    reply_markup_menu = ReplyKeyboardMarkup(core.keyboard_menu)

    await update.message.reply_text(
        "Спасибо за регистрацию!\nПервое задание откроется 1го января в 11:00. С новым годом!😉",
        reply_markup=reply_markup_menu
    )
    job = context.job_queue
    try:
        job.scheduler.remove_job(user_data[f'{user.id}job'])
    except Exception as e:
        logger.info(e)
    
    db.insert_pupil((user_data[user.id]['fio'], user_data[user.id]['number'], user.id))
    # запуск викторин
    # викторина 1го дня
    time_alarm_day_1 = datetime.datetime(2023, 1, 1, 8, 0)
    context.job_queue.run_once(first_day_alarm, time_alarm_day_1, chat_id=user.id)
    # notification 
    time_alarm_notification_1 = datetime.datetime(2023, 1, 1, 16, 0)
    job = context.job_queue.run_once(time_alarm_notification_1, notification_1, chat_id=user.id)
    user_data[f'{user.id}jobnote1'] = job.id
    # викторина 2го дня
    time_alarm_day_2 = datetime.datetime(2023, 1, 2, 6, 0)
    context.job_queue.run_once(second_day_alarm, time_alarm_day_2, chat_id=user.id)
    # notification
    time_alarm_notification_2 = datetime.datetime(2023, 1, 2, 16, 0)
    job = context.job_queue.run_once(time_alarm_notification_2, notification_2, chat_id=user.id)
    user_data[f'{user.id}jobnote2'] = job.id
    # викторина 3го дня
    time_alarm_day_3 = datetime.datetime(2023, 1, 3, 6, 0)
    context.job_queue.run_once(third_day_alarm, time_alarm_day_3, chat_id=user.id)
    # notification
    time_alarm_notification_3 = datetime.datetime(2023, 1, 3, 16, 0)
    job = context.job_queue.run_once(time_alarm_notification_3, notification_3, chat_id=user.id)
    user_data[f'{user.id}jobnote3'] = job.id
    # викторина 4го дня
    time_alarm_day_4 = datetime.datetime(2023, 1, 4, 6, 0)
    context.job_queue.run_once(fourth_day_alarm, time_alarm_day_4, chat_id=user.id)
    # notification
    time_alarm_notification_4 = datetime.datetime(2023, 1, 4, 16, 0)
    job = context.job_queue.run_once(time_alarm_notification_4, notification_4, chat_id=user.id)
    user_data[f'{user.id}jobnote4'] = job.id
    # викторина 5го дня
    time_alarm_day_5 = datetime.datetime(2023, 1, 5, 6, 0)
    context.job_queue.run_once(fifth_day_alarm, time_alarm_day_5, chat_id=user.id)
    # notification
    time_alarm_notification_5 = datetime.datetime(2023, 1, 5, 16, 0)
    job = context.job_queue.run_once(time_alarm_notification_5, notification_5, chat_id=user.id)
    user_data[f'{user.id}jobnote5'] = job.id
    # викторина 6го дня
    time_alarm_day_6 = datetime.datetime(2023, 1, 6, 6, 0)
    context.job_queue.run_once(sixth_day_alarm, time_alarm_day_6, chat_id=user.id)
    # notification
    time_alarm_notification_6 = datetime.datetime(2023, 1, 6, 16, 0)
    job = context.job_queue.run_once(time_alarm_notification_6, notification_6, chat_id=user.id)
    user_data[f'{user.id}jobnote6'] = job.id
    # викторина 7го дня
    time_alarm_day_7 = datetime.datetime(2023, 1, 7, 6, 0)
    context.job_queue.run_once(seventh_day_alarm, time_alarm_day_7, chat_id=user.id)
    # викторина 8го дня
    time_alarm_day_8 = datetime.datetime(2023, 1, 8, 6, 0)
    context.job_queue.run_once(eighth_day_alarm, time_alarm_day_8, chat_id=user.id)

    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    await update.message.reply_text(
        "Вы вышли из регистрации :("
    )
    return ConversationHandler.END


async def first_day_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Запуск вопроса 1."""
    user = update.message.from_user
    day = datetime.datetime.now()
    if day.strftime('%d.%m.%y') in (core.day_1, core.day_2, core.day_3, core.day_4):
        if db.answer_is_none(user.id, "dayfirst"):
            await update.message.reply_text(
                core.day_1_phrase,
            )
            user_data = context.user_data
            job = context.job_queue
            try:
                job.scheduler.remove_job(user_data[f'{user.id}jobnote1'])
            except Exception as e:
                logger.info(e)
            return core.ANSWER
        else:
            await update.message.reply_text(
                'Вы уже ответили на этот вопрос.'
            )
            return ConversationHandler.END
    else:
        await update.message.reply_text(
                    'Вопрос закрыт.'
                )
    return ConversationHandler.END

async def answer_1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Получение ответа вопрос."""
    user = update.message.from_user
    logger.info("answer of %s: %s", user.first_name, update.message.text)
    datum = datetime.datetime.now()
    date = datum.strftime('Дата: %d.%m.%y Время: %H:%M:%S')
    db.insert_answer('dayfirst', update.message.text, user.id, date)
    await update.message.reply_text(
        "Ответ на 1й вопрос записан!"
    )
    return ConversationHandler.END

async def second_day_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Запуск вопроса 2."""
    user = update.message.from_user
    day = datetime.datetime.now()
    if day.strftime('%d.%m.%y') in (core.day_2, core.day_3, core.day_4):
        if db.answer_is_none(user.id, "daysecond"):
            photo_1 = open('data/for_bot/daytwo_shifr.png', 'rb')
            await update.message.reply_photo(photo_1)
            await update.message.reply_text(
                core.day_2_phrase,
            )
            photo_1 = open('data/for_bot/daytwo_answer.png', 'rb')
            await update.message.reply_photo(photo_1)
            user_data = context.user_data
            job = context.job_queue
            try:
                job.scheduler.remove_job(user_data[f'{user.id}jobnote2'])
            except Exception as e:
                logger.info(e)
            return core.ANSWER
        else:
            await update.message.reply_text(
                'Вы уже ответили на этот вопрос.'
            )
            return ConversationHandler.END
    else:
        await update.message.reply_text(
                    'Вопрос закрыт.'
                )
    return ConversationHandler.END

async def answer_2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Получение ответа вопрос."""
    user = update.message.from_user
    logger.info("answer of %s: %s", user.first_name, update.message.text)
    datum = datetime.datetime.now()
    date = datum.strftime('Дата: %d.%m.%y Время: %H:%M:%S')
    db.insert_answer('daysecond', update.message.text, user.id, date)
    await update.message.reply_text(
        "Ответ на 2й вопрос записан!"
    )
    return ConversationHandler.END

async def third_day_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Запуск вопроса 3."""
    user = update.message.from_user
    day = datetime.datetime.now()
    if day.strftime('%d.%m.%y') in (core.day_3, core.day_4):
        if db.answer_is_none(user.id, "daythird"):
            await update.message.reply_text(
                core.day_3_phrase,
            )
            user_data = context.user_data
            job = context.job_queue
            try:
                job.scheduler.remove_job(user_data[f'{user.id}jobnote3'])
            except Exception as e:
                logger.info(e)
            return core.ANSWER
        else:
            await update.message.reply_text(
                'Вы уже ответили на этот вопрос.'
            )
            return ConversationHandler.END
    else:
        await update.message.reply_text(
                    'Вопрос закрыт.'
                )
    return ConversationHandler.END

async def answer_3(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Получение ответа вопрос."""
    user = update.message.from_user
    logger.info("answer of %s: %s", user.first_name, update.message.text)
    datum = datetime.datetime.now()
    date = datum.strftime('Дата: %d.%m.%y Время: %H:%M:%S')
    db.insert_answer('daythird', update.message.text, user.id, date)
    await update.message.reply_text(
        "Ответ на 3й вопрос записан!"
    )
    return ConversationHandler.END

async def fourth_day_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Запуск вопроса 4."""
    user = update.message.from_user
    day = datetime.datetime.now()
    if day.strftime('%d.%m.%y') in (core.day_4, core.day_5):
        if db.answer_is_none(user.id, 'dayfourth'):
            await update.message.reply_text(
                core.day_4_phrase,
            )
            user_data = context.user_data
            job = context.job_queue
            try:
                job.scheduler.remove_job(user_data[f'{user.id}jobnote4'])
            except Exception as e:
                logger.info(e)
            return core.ANSWER
        else:
            await update.message.reply_text(
                'Вы уже ответили на этот вопрос.'
            )
            return ConversationHandler.END
    else:
        await update.message.reply_text(
                    'Вопрос закрыт.'
                )
    return ConversationHandler.END

async def answer_4(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Получение ответа вопрос."""
    user = update.message.from_user
    logger.info("answer of %s: %s", user.first_name, update.message.text)
    datum = datetime.datetime.now()
    date = datum.strftime('Дата: %d.%m.%y Время: %H:%M:%S')
    db.insert_answer('dayfourth', update.message.text, user.id, date)
    await update.message.reply_text(
        "Ответ на 4й вопрос записан!"
    )
    return ConversationHandler.END

async def fifth_day_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Запуск вопроса 5."""
    user = update.message.from_user
    day = datetime.datetime.now()
    if day.strftime('%d.%m.%y') in (core.day_5, core.day_6, core.day_7):
        if db.answer_is_none(user.id, "dayfifth"):
            await update.message.reply_text(
                core.day_5_phrase_1,
            )
            photo_1 = open('data/for_bot/dayfifth.png', 'rb')
            await update.message.reply_photo(photo_1)
            await update.message.reply_text(
                core.day_5_phrase_2,
            )
            user_data = context.user_data
            job = context.job_queue
            try:
                job.scheduler.remove_job(user_data[f'{user.id}jobnote5'])
            except Exception as e:
                logger.info(e)
            return core.ANSWER
        else:
            await update.message.reply_text(
                'Вы уже ответили на этот вопрос.'
            )
            return ConversationHandler.END
    else:
        await update.message.reply_text(
                    'Вопрос закрыт.'
                )
    return ConversationHandler.END

async def answer_5(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Получение ответа вопрос."""
    user = update.message.from_user
    logger.info("answer of %s: %s", user.first_name, update.message.text)
    datum = datetime.datetime.now()
    date = datum.strftime('Дата: %d.%m.%y Время: %H:%M:%S')
    db.insert_answer("dayfifth", update.message.text, user.id, date)
    await update.message.reply_text(
        "Ответ на 5й вопрос записан!"
    )
    return ConversationHandler.END

async def sixth_day_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Запуск вопроса 6."""
    user = update.message.from_user
    day = datetime.datetime.now()
    if day.strftime('%d.%m.%y') in (core.day_6, core.day_7):
        if db.answer_is_none(user.id, "daysixth"):
            await update.message.reply_text(
                core.day_6_phrase,
            )
            user_data = context.user_data
            job = context.job_queue
            try:
                job.scheduler.remove_job(user_data[f'{user.id}jobnote6'])
            except Exception as e:
                logger.info(e)
            return core.ANSWER
        else:
            await update.message.reply_text(
                'Вы уже ответили на этот вопрос.'
            )
            return ConversationHandler.END
    else:
        await update.message.reply_text(
                    'Вопрос закрыт.'
                )
    return ConversationHandler.END

async def answer_6(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Получение ответа вопрос."""
    user = update.message.from_user
    logger.info("answer of %s: %s", user.first_name, update.message.text)
    datum = datetime.datetime.now()
    date = datum.strftime('Дата: %d.%m.%y Время: %H:%M:%S')
    db.insert_answer('daysixth', update.message.text, user.id, date)
    await update.message.reply_text(
        "Ответ на 6й вопрос записан!"
    )
    return ConversationHandler.END

async def seventh_day_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Запуск вопроса 7."""
    user = update.message.from_user
    day = datetime.datetime.now()
    if day.strftime('%d.%m.%y') in (core.day_7, core.day_8):
        if db.answer_is_none(user.id, "dayseventh"):
            await update.message.reply_text(
                core.day_7_phrase,
            )
            return core.ANSWER
        else:
            await update.message.reply_text(
                'Вы уже ответили на этот вопрос.'
            )
            return ConversationHandler.END
    else:
        await update.message.reply_text(
                    'Вопрос закрыт.'
                )
    return ConversationHandler.END

async def answer_7(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Получение ответа вопрос."""
    user = update.message.from_user
    logger.info("answer of %s: %s", user.first_name, update.message.text)
    datum = datetime.datetime.now()
    date = datum.strftime('Дата: %d.%m.%y Время: %H:%M:%S')
    db.insert_answer('dayseventh', update.message.text, user.id, date)
    await update.message.reply_text(
        "Ответ на 7й вопрос записан!"
    )
    return ConversationHandler.END

async def eighth_day_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Запуск вопроса 8."""
    user = update.message.from_user
    day = datetime.datetime.now()
    if day.strftime('%d.%m.%y') in (core.day_8, ):
        if db.answer_is_none(user.id, "dayeighth"):
            await update.message.reply_text(
                core.day_8_phrase,
            )
            return core.ANSWER
        else:
            await update.message.reply_text(
                'Вы уже ответили на этот вопрос.'
            )
            return ConversationHandler.END
    else:
        await update.message.reply_text(
                    'Вопрос закрыт.'
                )
    return ConversationHandler.END

async def answer_8(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Получение ответа вопрос."""
    user = update.message.from_user
    logger.info("answer of %s: %s", user.first_name, update.message.text)
    datum = datetime.datetime.now()
    date = datum.strftime('Дата: %d.%m.%y Время: %H:%M:%S')
    photo_file = await update.message.photo[-1].get_file()
    name = db.select_pupils_name(user.id)
    await photo_file.download_to_drive(f'data/from_bot/{name}_{user.id}.jpg')
    db.insert_answer('dayeighth', 'Фото загружено', user.id, date)
    await update.message.reply_text(
        "Ответ на 8й вопрос записан!"
    )
    return ConversationHandler.END

def main() -> None:
    """Start the bot."""
    application = Application.builder().token("5555322200:AAGM0Sw9hFe41Bfp-5wFDA-67Roub40sc_Q").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("admindata", data))
    application.add_handler(MessageHandler(filters.Regex('Помощь с ботом'), help_command))


    registration_handler = ConversationHandler(
        entry_points=[MessageHandler(filters.Regex('Заполнить форму для участия'), start_form)],
        states={
            core.FIO: [MessageHandler(filters.TEXT, fio)],
            core.TELEPHONE_NUMBER: [MessageHandler(filters.TEXT, number)],
        },
        conversation_timeout=core.TIME_FOR_REGISTRATION,
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    application.add_handler(registration_handler)

    first_day_handler = ConversationHandler(
        entry_points=[MessageHandler(filters.Regex('Вопрос от 1 января 📍'), first_day_answer)],
        states={
            core.ANSWER: [MessageHandler(filters.TEXT, answer_1)],
        },
        conversation_timeout=core.TIME_FOR_ANSWER,
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    application.add_handler(first_day_handler)

    second_day_handler = ConversationHandler(
        entry_points=[MessageHandler(filters.Regex('Вопрос от 2 января 👨‍🚀'), second_day_answer)],
        states={
            core.ANSWER: [MessageHandler(filters.TEXT, answer_2)],
        },
        conversation_timeout=core.TIME_FOR_ANSWER,
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    application.add_handler(second_day_handler)

    third_day_handler = ConversationHandler(
        entry_points=[MessageHandler(filters.Regex('Вопрос от 3 января 🔢'), third_day_answer)],
        states={
            core.ANSWER: [MessageHandler(filters.TEXT, answer_3)],
        },
        conversation_timeout=core.TIME_FOR_ANSWER,
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    application.add_handler(third_day_handler)

    fourth_day_handler = ConversationHandler(
        entry_points=[MessageHandler(filters.Regex('Вопрос от 4 января ❄️'), fourth_day_answer)],
        states={
            core.ANSWER: [MessageHandler(filters.TEXT, answer_4)],
        },
        conversation_timeout=core.TIME_FOR_ANSWER,
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    application.add_handler(fourth_day_handler)

    fifth_day_handler = ConversationHandler(
        entry_points=[MessageHandler(filters.Regex('Вопрос от 5 января 🎭'), fifth_day_answer)],
        states={
            core.ANSWER: [MessageHandler(filters.TEXT, answer_5)],
        },
        conversation_timeout=core.TIME_FOR_ANSWER,
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    application.add_handler(fifth_day_handler)

    sixth_day_handler = ConversationHandler(
        entry_points=[MessageHandler(filters.Regex('Вопрос от 6 января 🤹‍♀️'), sixth_day_answer)],
        states={
            core.ANSWER: [MessageHandler(filters.TEXT, answer_6)],
        },
        conversation_timeout=core.TIME_FOR_ANSWER,
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    application.add_handler(sixth_day_handler)

    seventh_day_handler = ConversationHandler(
        entry_points=[MessageHandler(filters.Regex('Вопрос от 7 января 🧚'), seventh_day_answer)],
        states={
            core.ANSWER: [MessageHandler(filters.TEXT, answer_7)],
        },
        conversation_timeout=core.TIME_FOR_ANSWER,
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    application.add_handler(seventh_day_handler)

    eighth_day_handler = ConversationHandler(
        entry_points=[MessageHandler(filters.Regex('Вопрос от 8 января 📥'), eighth_day_answer)],
        states={
            core.ANSWER: [MessageHandler(filters.PHOTO, answer_8)],
        },
        conversation_timeout=core.TIME_FOR_ANSWER,
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    application.add_handler(eighth_day_handler)

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()
