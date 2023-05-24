# ITiP_labs
Лабораторные работы по ИТиП

Еременко Алина БСТ1951

Python+Django

Лабораторная работа №1

Задание 1: Вам необходимо написать функцию фильтрации студентов по средней оценке, так, чтобы на экран выводился список студентов, средний балл которых выше заданного. Средний балл, по которому будет проводиться фильтрация, вводится пользователем с клавиатуры.

Задание 2: Чтобы создать таблицы базы данных, необходимо перейти в директорию project_name и через командную строку выполнить команду: python3 manage.py migrate Затем создаем суперпользователя (при создании необходимо ввести логин, email и пароль пользователя): python manage.py createsuperuser Теперь необходимо запустить сервер, если он не был запущен до этого, командой: python manage.py runserver и в браузере пройти по адресу http://127.0.0.1:8000/admin/. После этого должно появиться окно входа, куда необходимо ввести данные, которые вы указали при создании суперпользователя. Когда вы успешно войдете в аккаунт суперюзера, перед вами откроется главная страница административной панели, через которую вы можете управлять вашими приложениями, редактируя существующие записи в базе данных или генерируя новые. • Изучите интерфейс административного приложения django; • Через интерфейс административного приложения создайте нового пользователя с правами суперпользователя; • Через интерфейс административного приложения создайте нового пользователя без прав суперпользователя; • Через интерфейс административного приложения «забаньте» одного из пользователей (сделайте пользователя «неактивным»); • Загрузите ваш проект на любой гит-репозиторий (GitHub, GitLab, Google Code, Bitbucket и т.п.).

Лабораторная работа №2

Задание 1: • Сделайте так, чтобы по адресу http://127.0.0.1:8000/hello/ возвращался тот же самый текст; • Уберите указание типа возвращаемого ответа (если классу HttpResponse напрямую не указать тип ответа, то будет выставлено значение по умолчанию). Сравните полученные результаты.

Задание 2: • Добавьте к созданной таблице 2 строки и 2 столбца; • Добавьте границы для таблицы; • Сделайте заголовки списков (нумерованного и маркированного) подзаголовками четвертого уровня; • Создайте абсолютно идентичный шаблон, изменив только название на «static_handler.html». В следующих заданиях при выполнении этой лабораторной работы изменяйте именно этот файл.

Задание 3: • Установите для заголовка первого уровня шрифт с засечками; • Добавьте картинку и сделайте ее высотой 30px; • Измените размер шрифта для подзаголовков четвертого уровня; • Сделайте ширину таблицы на 100% экрана; • Загрузите ваш проект на любой гит-репозиторий (GitHub, GitLab, Google Code, Bitbucket и т.п.).

Лабораторная работа №3

Задание 1: • Перейдите во вкладку Articles и создайте 3 статьи, заполнив все поля. • С помощью программы управления базами данных sqlite3 (например, SQLite Manager) откройте файл вашей базы данных текущего проекта, который хранится в папке проекта с именем, объявленным в настройках проектах в переменной «DATABASES.NAME». Найдите созданные в предыдущем пункте задания экземпляры записей. Измените текст одной записи и название статьи для другой. Создайте еще одну статью.

Задание 2: • Откройте файл базы данных, где хранятся экземпляры статей текущего проекта, с помощью программы управления базами данных sqlite3 и добавьте новую запись в блог через менеджер базы; • Загрузите ваш проект на любой гит-репозиторий (GitHub, GitLab, Google Code, Bitbucket и т.п.).

Лабораторная работа №4

Задание 1: • Теперь у определенной записи есть отдельная страница, а значит на странице списка постов каждый заголовок можно сделать ссылкой. Сделайте так, чтобы при клике по названию статьи происходил переход на страницу указанной записи. Для этого достаточно воспользоваться тегом , которому в атрибуте href указать адрес перехода.

Задание 2: • Создайте стили, соответствующие макету для страницы определенной записи. Не забудьте добавить ссылку «Все записи»; • Загрузите ваш проект на любой гит-репозиторий (GitHub, GitLab, Google Code, Bitbucket и т.п.).

Лабораторная работа №5

Задание: • Создайте несколько статей через созданную форму; • Создайте стили, подключив CSS-файл к шаблону; • Добавьте проверку на то, что введенное название статьи уникально; • Загрузите ваш проект на любой гит-репозиторий (GitHub, GitLab, Google Code, Bitbucket и т.п.).

Лабораторная работа №6

Задание 1: • Создайте шаблон и настройте адрес для отображения формы регистрации; • Создайте представление, которое будет обрабатывать поступающие запросы и регистрировать новых пользователей. Не забудьте сделать проверку на то, что отправленные поля не являются пустыми, а введенное имя пользователя уникально; • Создайте стили, подключив CSS-файл к шаблону; • Добавьте в шапку страницы всех записей и страницы для определенных статей, ссылку на регистрацию в верхнем правом углу (стиль ссылки сделать такой же, как у ссылки “Все статьи” на собственных страницах постов в предыдущих работах). • Измените отображение ссылок в шапке сайта в соответствие с состоянием пользователя. Например, если пользователь находится под своей учётной записью, то в шапке должны находиться ссылки: “Создать статью”, “Выход из аккаунта” и приветственная надпись с именем пользователя, иначе “Авторизация”, “Регистрация”. Можно использовать следующую конструкцию в шаблоне: {% if request.user.is_authenticated %} {% else %} {% endif %}

Задание 2: • Создайте шаблон и настройте адрес для отображения формы авторизации; • Сделайте недоступными для авторизованных пользователей страницы с регистрацией и авторизацией. • Создайте представление, которое будет обрабатывать поступающие запросы и авторизировать зарегистрированных пользователей. Не забудьте сделать проверку на то, что отправленные поля не являются пустыми, а введенные имя пользователя и пароль соответствуют одному из зарегистрированных аккаунтов; • Создайте стили, подключив CSS-файл к шаблону; • Загрузите ваш проект на любой гит-репозиторий (GitHub, GitLab, Google Code, Bitbucket и т.п.).
