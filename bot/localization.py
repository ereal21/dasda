LANGUAGES = {
    'en': {
        'hello': '👋 Hello, {user}!',
        'balance': '💰 Balance: {balance} EUR',
        'overpay': '💳 Send the exact amount. Overpayments will be credited.',
        'shop': '🛍 Shop',
        'profile': '👤 Profile',
        'top_up': '💸 Top Up',
        'reviews': '⭐ Reviews',
        'price_list': '💲 Price List',
        'language': '🌐 Language',
        'admin_panel': '🎛 Admin Panel',
        'help': '❓ Help',
        'help_info': (
            'Use the main menu to work with the bot:\n'
            '🛍 Shop – browse categories and choose a product.\n'
            '   • Select an item and confirm to purchase it.\n'
            '👤 Profile – view your balance and purchased items.\n'
            '💸 Top Up – choose a payment method and follow the instructions to add funds.\n'
            '🌐 Language – switch the interface language.\n'
            '🎁 Purchased items – available in Profile after you buy something.\n'
            'If you need assistance, contact {helper}.'
        ),
        'admin_help_info': (
            'Admin panel functions:\n'
            '🛠 Assign assistants – manage assistant accounts.\n'
            '📦 View Stock – browse and delete available product stock.\n'
            '🏪 Parduotuvės valdymas – manage shop categories and items.\n'
            '👥 Vartotojų valdymas – manage user balances and roles.\n'
            '📢 Pranešimų siuntimas – send messages to all users.'
        ),
        'assistant_help_info': (
            'Assistant panel functions:\n'
            '🖼 Assign photos – attach photos to items.\n'
            'Use Back to menu to return.'
        ),
        'choose_language': 'Please choose a language',
        'invoice_message': (
            '🧾 <b>Payment Invoice Created</b>\n\n'
            '<b>Amount:</b> <code>{amount}</code> {currency}\n'
            '🏦 <b>Payment Address:</b>\n<code>{address}</code>\n\n'
            '⏳ <b>Expires At:</b> {expires_at} LT\n'
            '⚠️ <b>Payment must be completed within 30 minutes of invoice creation.</b>\n\n'
            '❗️ <b>Important:</b> Send <u>exactly</u> this amount of {currency}.\n\n'
            '✅ <b>Confirmation is automatic via webhook after network confirmation.</b>'
        ),
        'cancel': 'Cancel',
        'cancel_payment': '❌ Cancel Payment',
        'payment_successful': '✅ Payment confirmed. Balance increased by {amount}€',
        'back_home': 'Back Home',
        'invoice_cancelled': 'Payment failed/expired. Your items are no longer reserved.',
        'total_purchases': '📦 Total Purchases: {count}',
        'note': '⚠️ Note: No refunds. Please ensure you send the exact amount for payments, as underpayments will not be confirmed.',
        'feedback_service': '🛎️ How was your experience with the service?\n✍️ Leave a hand review in our group: https://t.me/+QVDtC4t9OglmZDVk',
        'feedback_product': 'Opinion on the product?',
        'thanks_feedback': 'Thanks for your feedback!',
        'tip_prompt': '💁 Would you like to leave a tip for the service?',
        'tip_thanks': '🙏 Thank you for your tip!',
        'tip_no_balance': '❌ Not enough balance for that tip.',
        'tip_cancelled': '🚫 Tip canceled.',
        'blackjack_rules_button': '📜 Rules',
        'blackjack_rules': (
            '🃏 <b>Blackjack Rules</b>\n'
            '• Get as close to 21 as possible without going over.\n'
            '• 2-10 count face value, J/Q/K = 10.\n'
            '• Ace is 1 or 11.\n'
            '• Dealer draws to 17.\n'
            '• Bust over 21.\n'
            'Use 🃏 Hit to draw and 🛑 Stand to hold.\n'
            'Good luck!'
        ),
        'confirm_purchase': 'Confirm purchase of {item} for {price}€?',
        'confirm_purchase_details': (
            '💳 Balance available: {balance}€\n'
            '🧾 Amount due after credits: {due}€\n\n'
            'Choose how you want to pay:'
        ),
        'pay_with_balance': 'Pay with balance ({amount}€)',
        'pay_with_crypto': 'Pay fully with crypto ({amount}€)',
        'pay_with_crypto_after_credits': 'Use {credits}€ credits & pay {due}€',
        'crypto_selection_prompt': 'Choose a cryptocurrency to pay {amount}€ for {item}.',
        'purchase_invoice_caption': (
            '🧾 <b>Invoice for {item}</b>\n'
            'Amount due: <code>{amount}</code> {currency}\n'
            'Your applied credits: {credits}€\n'
            'Send exactly this amount to the address below:'
        ),
        'purchase_invoice_paid': '✅ Payment received for {item}. Delivering your order…',
        'purchase_invoice_cancelled': '🚫 Purchase canceled. No payment received.',
        'purchase_invoice_timeout': '⌛ Payment window expired. Invoice canceled.',
        'purchase_invoice_check_failed': '❌ Payment not found yet. Please try again later.',
        'not_enough_balance_for_credit': '❌ You no longer have enough credits for that deduction.',
        'purchase_out_of_stock': '❌ Item is no longer in stock. Please contact support.',
        'apply_promo': 'Apply promo code',
        'promo_prompt': 'Send promo code:',
        'promo_invalid': '❌ Invalid or expired promo code',
        'promo_applied': '✅ Promo code applied. New price: {price}€',

        'choose_subcategory': '🏘️ Choose a district:',
        'select_product': '🏪 Select a product',


        'choose_subcategory': '🏘️ Choose a district:',
        'select_product': '🏪 Select a product',


    },
    'ru': {
        'hello': '👋 Привет, {user}!',
        'balance': '💰 Баланс: {balance} EUR',
        'overpay': '💳 Отправьте точную сумму. Переплаты будут зачислены.',
        'shop': '🛍 Магазин',
        'profile': '👤 Профиль',
        'top_up': '💸 Пополнить',
        'reviews': '⭐ Отзывы',
        'price_list': '💲 Прайс-лист',
        'language': '🌐 Язык',
        'admin_panel': '🎛 Админ панель',
        'help': '❓ Помощь',
        'help_info': (
            'Используйте главное меню для работы с ботом:\n'
            '🛍 Магазин – просматривайте категории и выбирайте товар.\n'
            '   • Выберите товар и подтвердите покупку.\n'
            '👤 Профиль – ваш баланс и купленные товары.\n'
            '💸 Пополнить – выберите способ оплаты и следуйте инструкциям.\n'
            '🌐 Язык – сменить язык интерфейса.\n'
            '🎁 Купленные товары – доступны в профиле после покупки.\n'
            'Если нужна помощь, обратитесь к {helper}.'
        ),
        'admin_help_info': (
            'Функции админ-панели:\n'
            '🛠 Назначить ассистентов – управление помощниками.\n'
            '📦 Просмотр склада – список товаров и удаление остатков.\n'
            '🏪 Parduotuvės valdymas – управление магазином.\n'
            '👥 Vartotojų valdymas – управление пользователями.\n'
            '📢 Pranešimų siuntimas – рассылка сообщений.'
        ),
        'assistant_help_info': (
            'Функции панели ассистента:\n'
            '🖼 Привязать фото – добавление фотографий к товарам.\n'
            'Используйте "Назад в меню" для возврата.'
        ),
        'choose_language': 'Пожалуйста, выберите язык',
        'invoice_message': (
            '🧾 <b>Создан инвойс на оплату</b>\n\n'
            '<b>Сумма:</b> <code>{amount}</code> {currency}\n'
            '🏦 <b>Адрес оплаты:</b>\n<code>{address}</code>\n\n'
            '⏳ <b>Действителен до:</b> {expires_at} LT\n'
            '⚠️ <b>Оплата должна быть выполнена в течение 30 минут после создания.</b>\n\n'
            '❗️ <b>Важно:</b> Отправьте <u>ровно</u> это количество {currency}.\n\n'
            '✅ <b>Подтверждение произойдет автоматически через вебхук после подтверждения сети.</b>'
        ),
        'cancel': 'Отмена',
        'cancel_payment': '❌ Отменить оплату',
        'payment_successful': '✅ Платёж подтверждён. Баланс пополнен на {amount}€',
        'back_home': 'Назад домой',
        'invoice_cancelled': 'Оплата не завершена/истекла. Ваши товары больше не зарезервированы.',
        'total_purchases': '📦 Всего покупок: {count}',
        'note': '⚠️ Возврат средств невозможен. Отправляйте точную сумму, недоплаты не подтверждаются.',
        'feedback_service': '🛎️ Как вам обслуживание?\n✍️ Напишите отзыв вручную в группе: https://t.me/+QVDtC4t9OglmZDVk',
        'feedback_product': 'Мнение о товаре?',
        'thanks_feedback': 'Спасибо за отзыв!',
        'tip_prompt': '💁 Хотите оставить чаевые за обслуживание?',
        'tip_thanks': '🙏 Спасибо за чаевые!',
        'tip_no_balance': '❌ Недостаточно средств для чаевых.',
        'tip_cancelled': '🚫 Чаевые отменены.',
        'blackjack_rules_button': '📜 Правила',
        'blackjack_rules': (
            '🃏 <b>Правила Blackjack</b>\n'
            '• Наберите сумму карт как можно ближе к 21, не превышая.\n'
            '• Карты 2-10 по номиналу, J/Q/K — 10.\n'
            '• Туз — 1 или 11.\n'
            '• Дилер берёт до 17.\n'
            '• Перебор больше 21 — проигрыш.\n'
            'Нажмите 🃏 Hit, чтобы взять карту, или 🛑 Stand, чтобы остановиться.\n'
            'Удачи!'
        ),
        'confirm_purchase': 'Подтвердить покупку {item} за {price}€?',
        'confirm_purchase_details': (
            '💳 Доступно на балансе: {balance}€\n'
            '🧾 К оплате после списания: {due}€\n\n'
            'Выберите способ оплаты:'
        ),
        'pay_with_balance': 'Оплатить с баланса ({amount}€)',
        'pay_with_crypto': 'Оплатить полностью криптой ({amount}€)',
        'pay_with_crypto_after_credits': 'Списать {credits}€ и оплатить {due}€ криптой',
        'crypto_selection_prompt': 'Выберите криптовалюту для оплаты {amount}€ за {item}.',
        'purchase_invoice_caption': (
            '🧾 <b>Инвойс за {item}</b>\n'
            'Сумма к оплате: <code>{amount}</code> {currency}\n'
            'Применённые кредиты: {credits}€\n'
            'Отправьте точно эту сумму на адрес ниже:'
        ),
        'purchase_invoice_paid': '✅ Платёж за {item} получен. Высылаем заказ…',
        'purchase_invoice_cancelled': '🚫 Покупка отменена. Платёж не поступил.',
        'purchase_invoice_timeout': '⌛ Время на оплату истекло. Инвойс отменён.',
        'purchase_invoice_check_failed': '❌ Платёж ещё не найден. Попробуйте позже.',
        'not_enough_balance_for_credit': '❌ Недостаточно средств на балансе для такого списания.',
        'purchase_out_of_stock': '❌ Товар закончился. Свяжитесь с поддержкой.',
        'apply_promo': 'Применить промокод',
        'promo_prompt': 'Введите промокод:',
        'promo_invalid': '❌ Недействительный или просроченный промокод',
        'promo_applied': '✅ Промокод применён. Новая цена: {price}€',

        'choose_subcategory': '🏘️ Выберите район:',
        'select_product': '🏪 Выберите товар',


        'choose_subcategory': '🏘️ Выберите район:',
        'select_product': '🏪 Выберите товар',

    },
    'lt': {
        'hello': '👋 Sveiki, {user}!',
        'balance': '💰 Balansas: {balance} EUR',
        'overpay': '💳 Siųskite tikslią sumą. Permokos bus įskaitytos.',
        'shop': '🛍 Parduotuvė',
        'profile': '👤 Profilis',
        'top_up': '💸 Papildyti',
        'reviews': '⭐ Atsiliepimai',
        'price_list': '💲 Kainoraštis',
        'language': '🌐 Kalba',
        'admin_panel': '🎛 Admin pultas',
        'help': '❓ Pagalba',
        'help_info': (
            'Naudokite pagrindinį meniu darbui su botu:\n'
            '🛍 Parduotuvė – naršykite kategorijas ir pasirinkite prekę.\n'
            '   • Pasirinkite prekę ir patvirtinkite pirkimą.\n'
            '👤 Profilis – jūsų balansas ir nupirktos prekės.\n'
            '💸 Papildyti – pasirinkite mokėjimo būdą ir vykdykite instrukcijas.\n'
            '🌐 Kalba – pakeisti sąsajos kalbą.\n'
            '🎁 Nupirktos prekės – matomos profilyje po pirkimo.\n'
            'Jei reikia pagalbos, susisiekite su {helper}.'
        ),
        'admin_help_info': (
            'Admin pulto funkcijos:\n'
            '🛠 Asistentų priskyrimas – valdykite asistentų paskyras.\n'
            '📦 Peržiūrėti likučius – naršykite prekes ir trinkite likučius.\n'
            '🏪 Parduotuvės valdymas – prekių ir kategorijų valdymas.\n'
            '👥 Vartotojų valdymas – naudotojų balansai ir rolės.\n'
            '📢 Pranešimų siuntimas – siųsti žinutes vartotojams.'
        ),
        'assistant_help_info': (
            'Asistento pulto funkcijos:\n'
            '🖼 Nuotraukų priskyrimas – pridėkite nuotraukas prie prekių.\n'
            'Naudokite „Atgal į meniu“ norėdami grįžti.'
        ),
        'choose_language': 'Pasirinkite kalbą',
        'invoice_message': (
            '🧾 <b>Sukurta mokėjimo sąskaita</b>\n\n'
            '<b>Suma:</b> <code>{amount}</code> {currency}\n'
            '🏦 <b>Mokėjimo adresas:</b>\n<code>{address}</code>\n\n'
            '⏳ <b>Galioja iki:</b> {expires_at} LT\n'
            '⚠️ <b>Mokėjimą reikia atlikti per 30 minučių nuo sąskaitos sukūrimo.</b>\n\n'
            '❗️ <b>Svarbu:</b> Nusiųskite <u>tiksliai</u> tiek {currency} į šį adresą.\n\n'
            '✅ <b>Patvirtinimas vyks automatiškai per webhook po tinklo patvirtinimo.</b>'
        ),
        'cancel': 'Atšaukti',
        'cancel_payment': '❌ Atšaukti mokėjimą',
        'payment_successful': '✅ Mokėjimas patvirtintas. Balansas padidintas {amount}€',
        'back_home': 'Grįžti į pradžią',
        'invoice_cancelled': 'Mokėjimas nepavyko/baigėsi. Jūsų prekės nebėra rezervuotos.',
        'total_purchases': '📦 Viso pirkinių: {count}',
        'note': '⚠️ Pastaba: grąžinimų nėra. Įsitikinkite, kad siunčiate tikslią sumą, nes nepakankamos sumos nebus patvirtintos.',
        'feedback_service': '🛎️ Kaip vertinate aptarnavimą?\n✍️ Parašykite atsiliepimą šioje grupėje: https://t.me/+QVDtC4t9OglmZDVk',
        'feedback_product': 'Kokia nuomonė apie prekę?',
        'thanks_feedback': 'Ačiū už atsiliepimą!',
        'tip_prompt': '💁 Ar norėtumėte palikti arbatpinigių už paslaugą?',
        'tip_thanks': '🙏 Ačiū už arbatpinigius!',
        'tip_no_balance': '❌ Nepakanka lėšų arbatpinigiams.',
        'tip_cancelled': '🚫 Arbatpinigiai atšaukti.',
        'blackjack_rules_button': '📜 Taisyklės',
        'blackjack_rules': (
            '🃏 <b>Blackjack taisyklės</b>\n'
            '• Surinkite kuo arčiau 21, neviršydami.\n'
            '• 2-10 verti savo skaičiaus, J/Q/K – 10.\n'
            '• Tūzas – 1 arba 11.\n'
            '• Dileris traukia iki 17.\n'
            '• Viršijus 21 – pralaimėjimas.\n'
            'Naudokite 🃏 Hit, kad trauktumėte, ir 🛑 Stand, kad sustotumėte.\n'
            'Sėkmės!'
        ),
        'confirm_purchase': 'Patvirtinti {item} pirkimą už {price}€?',
        'confirm_purchase_details': (
            '💳 Turimas kreditas: {balance}€\n'
            '🧾 Suma po kreditų: {due}€\n\n'
            'Pasirinkite apmokėjimo būdą:'
        ),
        'pay_with_balance': 'Apmokėti iš balanso ({amount}€)',
        'pay_with_crypto': 'Visą sumą mokėti kriptovaliuta ({amount}€)',
        'pay_with_crypto_after_credits': 'Naudoti {credits}€ kreditų ir mokėti {due}€',
        'crypto_selection_prompt': 'Pasirinkite kriptovaliutą sumokėti {amount}€ už {item}.',
        'purchase_invoice_caption': (
            '🧾 <b>Sąskaita už {item}</b>\n'
            'Mokėtina suma: <code>{amount}</code> {currency}\n'
            'Pritaikyti kreditai: {credits}€\n'
            'Išsiųskite tiksliai šią sumą žemiau pateiktu adresu:'
        ),
        'purchase_invoice_paid': '✅ Gauta {item} apmokėjimas. Paruošiame užsakymą…',
        'purchase_invoice_cancelled': '🚫 Pirkimas atšauktas. Apmokėjimo negauta.',
        'purchase_invoice_timeout': '⌛ Apmokėjimo laikas baigėsi. Sąskaita atšaukta.',
        'purchase_invoice_check_failed': '❌ Apmokėjimas dar negautas. Pabandykite vėliau.',
        'not_enough_balance_for_credit': '❌ Nebepakanka kreditų šiam nurašymui.',
        'purchase_out_of_stock': '❌ Prekės nebėra sandėlyje. Susisiekite su palaikymu.',
        'apply_promo': 'Taikyti nuolaidos kodą',
        'promo_prompt': 'Įveskite nuolaidos kodą:',
        'promo_invalid': '❌ Neteisingas arba pasibaigęs kodas',
        'promo_applied': '✅ Kodas pritaikytas. Nauja kaina: {price}€',

        'choose_subcategory': '🏘️ Pasirinkite rajoną:',
        'select_product': '🏪 Pasirinkite prekę',


        'choose_subcategory': '🏘️ Pasirinkite rajoną:',
        'select_product': '🏪 Pasirinkite prekę',


    },
}

def t(lang: str, key: str, **kwargs) -> str:
    lang_data = LANGUAGES.get(lang, LANGUAGES['en'])
    template = lang_data.get(key, '')
    return template.format(**kwargs)
