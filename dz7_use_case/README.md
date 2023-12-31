# Макет сайта по обучению языку программирования Rust ![](cover.png)

### Схема общей структуры сайта

На главной странице пользователь имеет возможность:
1. посмотреть видео-презентацию как будет проходить учебный процесс
2. опробовать пробный курс, чтобы чуть подробнее ознакомиться с процессом
3. зарегистрироваться и/или пройти в личный кабинет
4. обратиться в службу поддержки во имеющимся вопросам

Первоначально пользователю доступно только "Пробный курс" по завершению которого будет предложение 
зарегистрироваться в личном кабинете, если еще этого не сделал и оплатить подписку.
Пройдя регистрацию и оплатив курс, пользователь получит доступ к самому обучению,
где ему будет предоставлены возможности:
1. узнать историю и возможности языка
2. выполнение практических задач
3. обсуждение задач с другими учениками и преподавателями

По окончанию обучения пользователь получит сертификат об окончании обучения. 

Блок "Справочник" открывается в новом окне.

Так же доступ к сайту имеют преподаватели и администраторы через соответствующие 
служебные кабинеты и правами доступа для выполнения своих рабочих задач.

![](_Rust_.jpg)

- Стрелочки показывают как живые пользователи могут передвигаться по сайту. 
- Пунктиром выделена связь блоков, которая происходит на программном уровне без участия человека.
- Широкие стрелочки показывают туже связь, что и пунктирные линии, но в одностороннем порядке.

### Пример главной страницы сайта

![](title.png)

Как и описывалось выше, пользователю доступны видео с ознакомлением, пробный курс, 
войти в личный кабинет, регистрация на сайте и обратиться в службу поддержки, нажав на кнопку или иконку с крабиком в самом низу сайта. 

На слайде показаны две кнопки "Начать пробный курс" и "Продолжить обучение" с пояснениями.
Первоначально будет только кнопка "Начать пробный курс", а после прохождения регистрации и оплаты подписки
она будет заменена на "Продолжить обучение", чтобы пользователь мог сразу перейти к урокам.
Так же 

### Пример рабочей страницы

![](work_page.png)

В левой части экрана иконки:
- логотип Rust - перейти на главную страницу 
- книжка - перейти на страницу со справочным материалом
- блокнот с ручкой - откроется блокнот для собственных заметок
- крабик - откроет чат-бот со службой поддержки


Чуть правее расположено окно с переключателями:
- "Привет, мир!" - кнопка не имеет собственного названия и вызывает план занятий. Пользователь может посмотреть какие уроки он прошел и какие его ожидают. Название кнопки отражает название текущего урока.
- "Терминал" - тут выводится результат кода
- "Обсуждение" - откроет чат текущего урока для обсуждения с другими пользователями
- "Древо файлов" - откроет окно, где будет видно структуру папок и файлов

В правом верхнем углу расположена иконка для перехода в личный кабинет.

Ниже расположен редактор кода, куда пользователь пишет код и может его запустить, остановить или запустить пошагово

В нижней части страницы расположена структура автотеста, чтобы пользователю было более понятно что он него ждут и как будет проверяться код 

### Пример личного кабинета

![](account.png)

В левой части экрана иконки:
- логотип Rust - перейти на главную страницу 
- белая книжка - перейти на страницу со справочным материалом
- оранжевая книжка - перейти на рабочую страницу
- крабик - откроет чат-бот со службой поддержки

Пользователь может загрузить свое фото в большой круг нажав на иконку "+".
Маленький круг покажет, как будет выглядеть фото в правой части экрана на других страницах сайта.
Все важные для регистрации данные будут сказу перенесены в личный кабинет.
Пользователь так же сможет подключить и другие сервисы, с помощью которых он так же может пройти регистрацию на сайте.
Так же видно сколько уроков пройдено и когда было последнее посещение сайта.
В нижней части указана выбранная подписка и срок ее действия.
При прохождении всех уроков и выполнении всех занятий, активируется кнопка "Получить сертификат".
Другие пользователи так же могут попасть в ваш личный кабинет без права редактирование,
а также им не будет видна ваша подписка.

### Пример базы данных

![](data_base.png)

Взаимосвязь между пользователем и пройденными уроками.
Программа отслеживает пройденный материал чтобы не выдать сертификат раньше,
а также, чтобы пользователь не мог перейти на поздние уроки, не пройдя предыдущие.  

Таблица guide находится на отдельном столе, содержит в себе данные о макросах Rust и
ни как не связана с основной логикой.
___

___

1.1 Определение целей и задач приложения:
- Основная цель: Создать сайт для обучения основам и синтаксису языка программирования Rust.
- Задачи:
  - Разработать удобный и понятный интерфейс для работы с кодом и материалом для изучения.
  - Реализовать систему автотестов для качественной проверки заданий.
  - Создать систему общения между пользователями и преподавателем, для решения сложных задач.


1.2 Анализ аудитории и исследование рынка:
- Целевая аудитория: Люди всех возрастов, интересующиеся языком программирования Rust.
- Исследование рынка: Проанализированы другие обучающие сайты и он-лайн школы, определены их особенности и недостатки.

1.3 Создание общего описания концепции и функциональности:
- Концепция: Объяснить и научить максимально доступным и простым языком со множеством интересных задач.
- Основные функции:
  - Редактирование и запуск кода.
  - Проверка автотестами.
  - Безопасность и изолированность использования.
  - Система авторизации и возможность просмотра ранее пройденных уроков.

1.4 Выбор бизнес-модели:
- Модель монетизации: Продажа курса по срочной и без срочной подпискам.

1.5 Оценка ресурсов и бюджета:
- Ресурсы: Доступен бюджет для найма разработчиков, дизайнеров и рекламных кампаний.
- Бюджет: Оценка расходов на разработку, дизайн, маркетинг и обслуживание приложения.

1.6 Планирование времени:
- Временной график:
  - Определение требований и разработка концепции: 6 месяцев.
  - Проектирование интерфейса и прототипирование: 3 недели.
  - Разработка фронтенда и бэкенда: 4 месяцев.
  - Тестирование и доработка: 3 недели.
  - Деплой и подготовка к запуску: 1 неделя.

1.7 Проектирование прототипа:
- Создание прототипа интерфейса с основными элементами:
  - Главная страница с возможностью ознакомления.
  - Страница с обучающим приложением.
  - Страница авторизации и регистрации.
  - Страница со справочником.
  - Пользовательский чат. 