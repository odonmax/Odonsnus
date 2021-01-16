

bot_token = '1497960082:AAHQyL48zNZh0YDcTnUhhEVcnZPNkYm6e' # токен бота
LOGIN_BOT = '@SnusovozBestbot' # логин бота
CHANNEL_ID = 1429682522 # id канала куда будет отсылаться информация, ид без -100 в начале (например: 124873248)

admin_id = 817679816 # id админа

LOGIN_ADMIN = '@dead_luka' # тг логин спамера, нужен для информации

QIWI_NUMBER = '+79652561694'    # номер киви
QIWI_TOKEN = '6d59d1f210a65aeac9e9968ed7a51bfb'           # токен киви


PERCENT_SPAM = 0.5  # Процент спамеру (0.5 = 50%) #не работает в версии без спамеров
PERCENT_OWN = 0.5   # Процент вам (0.5 = 50%)

main_bd = '/home/TiredCat/Admin bot/main.db'


info = 'Информация\n' \
'Telegram поддержки @dead_luka' \

text_purchase = '❕ Вы выбрали: ' \
                '{name}\n\n' \
                '{info}\n\n' \
                '💠 Цена: {price} рублей\n' \
                '💠 Товар: {amount}\n' \
  '💠 Введите ваш адрес после оплаты' \


replenish_balance = '➖➖➖➖➖➖➖➖➖➖➖\n' \
                    '💰 Пополнение баланса\n\n' \
                    '🥝 Оплата киви: \n\n' \
                    '👉 Номер  {number}\n' \
                    '👉 Комментарий  {code}\n' \
                    '👉 Сумма  от 1 до 15000 рублей\n' \
                    '➖➖➖➖➖➖➖➖➖➖➖\n' \

profile = '🧾 Профиль\n\n' \
          '❕ Ваш id - {id}\n' \
          '❕ Ваш логин - {login}\n' \
          '❕ Дата регистрации - {data}\n\n' \
          '💰 Ваш баланс - {balance} рублей'
