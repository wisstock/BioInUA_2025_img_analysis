Image Analysis with Python and Napari
================================

[![Stand With Ukraine](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/banner-direct-single.svg)](https://stand-with-ukraine.pp.ua)

<p align="left">
<a href="#logo" name="logo"><img src="pic/logo_kau.png" width="150"></a>
</p>

<p align="left">
<a href="#logo" name="logo"><img src="pic/logo_bioin.png" width="250"></a>
</p>

_Bioinformatics for Ukraine course, 6-24 October 2025, Kyiv, Ukraine._

> [!WARNING]
> Матеріали репозиторію будуть оновлюватись і доповнюватись впродовж курсу!
> 

---


# Структура і зміст курсу

## Загальний опис
Курс має декілька незалежних цілей:

- Зрозуміти загальні методи та бібліотеки для роботи із цифровими зображеннями з використанням python.
- Вивчити/пригадати загальні підходи для роботи з кодом на python для його ефективного повторного використання.
- Розглянути окремі етапи попередньої обробки та аналізу біологічних зображень на прикладах реальних даних різної структури.
- Знайомство із [napari](https://napari.org/stable/), python-based програми для відображення та обробки зображень.

Основним форматом завдань для самостійної роботи буде перетворення пройденого на занятті матеріалу у набір зручних для самих студентів інструментів. Упаковка окремих етапів обробки чи аналізу зображень в функції, функцій в модулі чи класи, а модулів в пакети. З погляду навичок програмування в цьому курсі буде акцент саме на створенні коду для повторного використання, а не одноразових скриптів чи ноутбуків. Вітається наявність власних візуальних даних із якими можна було б працювати впродовж курсу. Даних будь-яких різновидів флуоресцентної мікроскопії, томографії, візуалізації результатів гель-електрофорезу і блотів. Дані класичної світлової мікроскопії (світлопольної, темнопольної, фазово-контрастної) будуть дещо складнішими для аналізу, тому прошу їх уникати.

> [!IMPORTANT]
>
> Оскільки працювати доведеться на власних машинах, зважайте на це при виборі даних. Згрубша розмір зображень має бути принаймні у 2-2.5 рази меншим за обсяг оперативної пам'яті Вашого комп'ютера.
>

Курс розрахований на слухачів або із попереднім досвідом програмування на python Необхідними є загальні уявлення про типи даних (`str`, `int`, `float`, `list`, `dict`, `bool`, etc.) та основні оператори й синтаксичні конструкції (`if-else`, `for loop`).

> [!NOTE]
> Типи даних в Python [українською](https://w3schoolsua.github.io/python/python_datatypes.html#gsc.tab=0) та [англійською](https://www.w3schools.com/python/python_datatypes.asp).

> [!NOTE]
> Синтаксис конструкцій [if-else](https://w3schoolsua.github.io/python/python_conditions.html#gsc.tab=0) та [for loop](https://w3schoolsua.github.io/python/python_for_loops.html#gsc.tab=0) українською й [if-else](https://www.w3schools.com/python/python_conditions.asp) та [for loop](https://www.w3schools.com/python/python_for_loops.asp) англійською.

> [!NOTE]
> Синтаксис функцій та класів в Python [українською](https://w3schoolsua.github.io/python/python_functions.html#gsc.tab=0) та [англійською](https://www.w3schools.com/python/python_functions.asp).

| Формат             | Опис                                                         |
| ------------------ | ------------------------------------------------------------ |
| Вступна зустріч    | Огляд загальної структури курсу, огляд матеріалів курсу та даних, завершення підготовки до роботи (за потреби допомога із встановлення IDE, створенням робочих оточень, встановлення бібліотек тощо). |
| Практичні заняття  | 4х заняття по 1.5 години протягом 2-х тижнів. Заняття складається з 10-15 хв відповіді на питання та розгляду домашнього завдання, 30-40 хв пояснення матеріалу та практичної роботи до кінця уроку. Для кожної зустрічі буде доступний окремий jupiter-notebook, що матиме пояснення та приклади, практичну роботу та домашнє завдання. |
| Підготовка проєкту | По завершенню практичних занять впродовж останнього тижня курсу запланована самостійна робота. Побудувати набір інструментів для аналізу власних даних використавши набуті навички. Впродовж самостійної роботи продовжимо підтримувати зв'язок у чаті групи, і організуємо як мінімум 1 онлайн зустріч для обговорення прогресу і розв'язання проблем. Для студентів, які поки що не мають власних зображень, будуть доступні різні навчальні дані. |

> [!IMPORTANT]
>
> До початку курсу прошу підготуватись: встановити всі необхідні пакети та підготувати IDE. Всі необхідні кроки описані в розділі __Підготовка до роботи__, а якщо виникнуть неочікувані проблеми, вирішимо їх на вступній зустрічі.
>

## Зміст зустрічей

| # | Bio | Py              | Homework      | Lib            |
| ------ | -------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 0 | Огляд підходів оптичної мікроскопії та даних, що отримуються на мікроскопах. Обговорення даних, що будуть використані впродовж курсу (_опціонально - обговорення власних даних слухачів_). | Перевірка, чи у всіх слухачів вийшло успішно встановити IDE, створити оточення та встановити необхідні бібліотеки. | Додатковий час для самостійного пригадування синтаксису python та заверешення підготовки. | pip |
| 1 | Зображення як багатовимірні масиви, відображення багатоканальних і тривимірних зображень, псевдокольори (color maps / lookup table). | Завантаження/збереження зображень, маніпуляції з масивами numpy, відображення зображень. | Відпрацювання маніпуляцій із масивами numpy: виділення окремих регіонів на зображеннях для подальшого аналізу, підбір оптимальних налаштувань для відображення зображень. | numpy, matplotlib, tifffile |
| 2 | Попередня обробка зображень, детекція та сегментація об'єктів на зображеннях. | Фільтрація зображень, методи побудови бінарних і багаторівневих масок, морфологічні операції над масками. Функції. | Оформлення окремих етапів процесингу зображень в функції (для фільтрації, початкової детекції об'єктів, отримання кінцевих масок об'єктів тощо). | scikit-image, scipy/ndimage |
| 3 | Отримання кількісних даних з зображень та збереження результатів аналізу. | Оцінка морфологічних параметрів масок, оцінка зміни параметрів в масках в часі, збереження результатів аналізу в табличному форматі. Модулі/класи. | Оформлення окремих етапів аналізу зображень і збереження результатів аналізу в функції; перенесення набору створених функцій у модуль. | pandas |
| 4 | napari -  open source для переглядання та аналізу зображень | Упаковка результатів роботи у модулі та перетворення їх у плагін для  napari. Пакети python. | Перетворення функцій створених на попередніх зустрічах у віджети napari. | napari |

---

# Підготовка до роботи

## Структура репозиторію курсу
```
└── BioInUA_2025_img_abalysis/
    ├── course_data/                     # папка для розміщення Ваших даних та коду, не лякайтесь качки
    ├── demo_data/                       # демонстраційні і навчальні дані, НЕ видаляйте їх і НЕ змінюйте назви
    │      ├── ...
    │      └── DESCRIPTION.md                # опис демонстраційних та навчальних даних
    │
    ├── pic/                             # зображення для README
    ├── slides/                          # презентації до курсу
    ├── templates/                       # приклади структур python для різних зустрічей
    │   ├── package-template/                # приклад пакета python
    │   ├── plugin-template/                 # приклад пакета python оформленого в плагін для napari
    │   ├── __init__.py                      # службовий файл директорії що дозволяє імпортувати модуль
    │   └── module_template.py               # приклад модуля python
    │
    ├── .git/                             # дані системи контролю версій git
    |
    ├── 1_img_as_arrays.ipynb             # jupiter-notebook для першої зустрічі 
    ├── 2_preproc_and_segmentation.ipynb  # jupiter-notebook для другої зустрічі
    ├── 3_features_and_analysis.ipynb     # jupiter-notebook для третьої зустрічі
    ├── 4_napari_plugins.ipynb            # jupiter-notebook для четвертої зустрічі
    |
    ├── LICENSE                           # ліцензія матеріалів курсу, CC BY 4.0 
    └── README.md                         # файл опису курсу
```

## Необхідні бібліотеки
- Jupyter
- NumPy
- Pandas
- SciPy
- Scikit-Image
- Matplotlib
- napari

## Встановлення miniconda
При роботі з python-проєктами менеджер оточень (_environment management system_) використовуються для встановлення бібліотек з віддалених серверів, _репозиторіїв_, або цілих груп серверів - _каналів_. Це дозволяє запобігти конфліктам версій та залежностей. До найбільш вживаних відносяться [venv](https://docs.python.org/3/library/venv.html) та  [conda](https://docs.conda.io/en/latest/).

Для роботи з jupyter-notebook  впродовж перших трьох зустрічей потрібно створити робоче оточення за допомогою conda і встановити в нього всі необхідні бібліотеки.

[Встановіть](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) менеджер оточень __miniconda__ для Вашої операційної системи.

> [!WARNING]
> Рекомендую встановлювати саме miniconda, оскільки anaconda одразу містить багато непотрібних для курсу бібліотек і важить > 2GB.

## Створення та підготовка оточення
Спілкування з miniconda відбувається шляхом текстових команд в _Unix-терміналі_ (у випадку Linux або MacOS) або запустивши _Anaconda Prompt_ (у випадку Windows).

> [!TIP]
> Короткий перелік [основних команд conda](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf).

### Створення оточення однією командою (перевірено на miniconda 25.7.0 )
Створення оточення з необхідним набором бібліотек:

```
conda create -n bioin-img python jupyter numpy pandas scipy scikit-image matplotlib-base -y
```

Пошук, завантаження і встановлення бібліотек можуть зайняти понад 10 хвилин, а по завершенню miniconda може запропонувати Вам активувати новостворене оточення.

Для запуску нашого оточення в _Unix-термінал/Anaconda Prompt_ використовується команда:

```
conda activate bioin-img
```

А для виходу з оточення:

```
conda deactivate
```




> [!CAUTION]
>
> Якщо після першого запуску miniconda при спробі створити оточення виникає помилка
>
> ```
> CondaToSNonInteractiveError: Terms of Service have not been accepted for the following channels. Please accept or remove them before proceeding:
>     - https://repo.anaconda.com/pkgs/main
>     - https://repo.anaconda.com/pkgs/r
> 
> To accept these channels' Terms of Service, run the following commands:
>     conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main
>     conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r
> ```
>
> просто погоджуйтесь і робіть те, що воно Вас попросило :(
>
> Послідовно виконайте в _Unix-термінал/Anaconda Prompt_ дві запропоновані miniconda команди, щоб прийняти ліцензійні умови репозиторіїв:
>
> ```
> conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main
>```
> ```
> conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r
> ```

### Plan B (якщо щось пішло не так)
Якщо виникла інша помилка і не вдалось створити оточення, раджу перевірити перелік доступних каналів, звідки conda може встановлювати пакети. 

Для цього виконайте:

```
conda config --show channels
```

Якщо у переліку присутні лише `defaults`, необхідно додати канал `conda-forge` що містить велику кількість корисних бібліотек: 

```
conda config --add channels conda-forge
```

Після цього створення оточення за допомогою однієї команди має пройти вдало.


## Встановлення napari

[napari](https://napari.org/stable/) є відкритим програмним забезпеченням для візуалізації та аналізу багатовимірних зображень. Окрім можливості перегляду зображень napari надає зручний графічний інтерфейс та простий framework для інтеграції нового функціоналу у вигляді плагінів. Доступні плагіни можна знайти на [napari-hub](https://www.napari-hub.org/).

Встановлення за допомогою `pip` через _Unix-термінал/Anaconda Prompt_, встановлювати слід в оточенні __bioin-img__:
```
python -m pip install "napari[all]"
```

Для запуску графічного інтерфейсу переглядача зображень виконайте команду ```napari``` в _Unix-терміналі/Anaconda Prompt_ в оточені __bioin-img__, завантаження може зайняти до декількох хвилин.

> [!TIP]
> До початку курсу можете також ознайомитись з  матеріалами [napari how-to guides](https://napari.org/stable/howtos/index.html).


## Встановлення IDE

Інтегроване середовище розробки (_Integrated Development Environment - IDE_) значно спростить роботу з оточеннями conda та jupyter-notebook з яких складається цей курс.

Встановлення та налаштування:
- [Встановіть](https://code.visualstudio.com/) __Visual Studio Code__ для Вашої операційної системи
- Для роботи з кодом python та jupyter-ноутбуками користуючись вкладкою _Розширення_ (_Extensions_) на лівій панелі IDE встановіть розширення __python__ та __jupyter__
- Для запуску jupyter-notebook в створеному раніше оточенні conda натисніть на меню _Select Kernel_ у верхньому правому кутку вікна відкритого jupyter-notebook, оберіть пункт _Python Environment_ та необхідне нам оточення  __bioin-img__ серед запропонованих варіантів інтерпретаторів чи оточень (у випадку такого підключення попередній запуск оточення через Unix-термінал/Anaconda Prompt не потрібен).

---

# Робота з пакетами python/плагінами napari

## Структура директорії пакету python
```
└── package-template/          # директорія пакету
    ├── src/                       # загальна директорія із вихідним кодом пакету
    │   └── package_template/      # директорія із модулями пакету
    │       ├── __init__.py        # службовий файл директорії
    │       └── module.py          # код модуля у складі пакету
    │
    ├── pyproject.toml        # конфігураційний файл
    ├── README.md             # файл опису
    ├── LICENSE               # ліцензія
    └── .gitignore            # службовий файл git
```

Файли `__init.py__` вказують, що вміст директорії містить в собі модулі python, а не довільні файли. Додаткову інформацію про створення пакетів можна подивитись в офіційній документації python про [модулі](https://docs.python.org/3/tutorial/modules.html) та [пакети](https://packaging.python.org/en/latest/tutorials/packaging-projects/).


## Структура директорії плагіну napari

```
└── plugin-template/          # директорія плагіну
    ├── src/                  # загальна директорія із вихідним кодом
    │   └── plugin_template/      # директорія із модулями плагіну
    │       ├── __init__.py       # службовий файл директорії
    │       ├── napari.yaml       # маніфест napari
    │       └── _widget.py        # код віджетів плагіну
    │
    ├─── pyproject.toml       # конфігураційний файл
    ├─── README.md            # файл опису
    ├─── LICENSE              # ліцензія
    └─── .gitignore           # службовий файл git
```

Додатковий службовий файл `napari.yaml` у директорії із вихідним кодом, маніфест, містить вказівки на приналежність конкретних функцій в складі модулів до елементів плагіну і додаткову інформацію для відображенні в графічному інтерфейсі napari. Додаткову інформацію про створення плагінів можна подивитись в [офіціфній документації napari](https://napari.org/dev/plugins/building_a_plugin/first_plugin.html).

## Встановлення пакету/плагіну з використанням pip

Для встановлення створеного власноруч пакету чи плагіну необхідно користуючись _Unix-терміналом/Anaconda Prompt_ перейти в директорії проєкту та виконати наступну команду:

```
python -m pip install -e .
```

Флаг `-e` забезпечує встановлення з можливітю редагування (_editable install_), тому всі зміни в вихідному коді пакету/плагіну будуть одразу доступні до використання після перезаванатажаення інтепритатора python. 

---

# Матеріали до курсу

## Корисні посилання

- [Scikit-image examples](https://scikit-image.org/docs/stable/auto_examples/index.html)
- [Image processing learning resorces](https://homepages.inf.ed.ac.uk/rbf/HIPR2/hipr_top.htm)
- [Analyzing fluorescence microscopy images with ImageJ](https://petebankhead.gitbooks.io/imagej-intro/content/)
- [The Carl Zeiss Microscopy Online Campus](https://zeiss-campus.magnet.fsu.edu/index.html)
- [Scientific Volume Imaging](https://svi.nl/Huygens-Imaging-Academy)
- [Introduction to Modeling for Neuroscience](https://dabane-ghassan.github.io/ModNeuro/)
- [Convolutions in image processing, YouTube](https://www.youtube.com/watch?v=8rrHTtUzyZA)
- [Python for Data Science](https://aeturrell.github.io/python4DS/welcome.html)
- [R for Data Science](https://r4ds.hadley.nz/)


## Література

- [Fundamentals of Fluorescence Imaging](https://www.taylorfrancis.com/books/edit/10.1201/9781351129404/fundamentals-fluorescence-imaging-guy-cox)
- [Imaging Cellular and Molecular Biological Functions](https://link.springer.com/book/10.1007/978-3-540-71331-9)
- [Handbook of Biological Confocal Microscopy](https://link.springer.com/book/10.1007/978-0-387-45524-2)
- [An introduction to optical super-resolution microscopy for the adventurous biologist](https://www.researchgate.net/publication/323073291_An_introduction_to_optical_super-resolution_microscopy_for_the_adventurous_biologist)
- [Nanoscopy and Multidimensional Optical Fluorescence Microscopy](https://www.tandfonline.com/doi/pdf/10.1080/00107514.2011.580375)

---

# Ліцензія
Всі матеріали курсу, включно із кодом, демонстраційними даними та візуальними матеріалами ліцензовані на умовах [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1). Ви можете вільно використовувати, поширювати, змінювати та адаптувати матеріали курсу для будь-яких цілей, за умови вказання відповідного авторства.

 <p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/wisstock/BioIn_2025_img_analysis">Image Analysis with Python and Napari, BioInUA course </a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/wisstock">Borys Olifirov</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></a></p> 