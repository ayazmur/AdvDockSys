

![logo](doc/ads_logo.svg)

------------------

[![GitHub релиз (последний по дате)](https://img.shields.io/github/v/release/githubuser0xFFFF/Qt-Advanced-Docking-System?color=%23ff9833)](https://github.com/githubuser0xFFFF/Qt-Advanced-Docking-System/releases/latest)
[![Лицензич: LGPL v2.1](https://img.shields.io/badge/License-LGPL%20v2.1-blue.svg)](gnu-lgpl-v2.1.md)
[![Статус разработки](https://github.com/githubuser0xFFFF/Qt-Advanced-Docking-System/workflows/linux-builds/badge.svg)](https://github.com/githubuser0xFFFF/Qt-Advanced-Docking-System/actions?query=workflow%3Alinux-builds)
[![Статус разработки](https://ci.appveyor.com/api/projects/status/qcfb3cy932jw9mpy/branch/master?svg=true)](https://ci.appveyor.com/project/githubuser0xFFFF/qt-advanced-docking-system/branch/master)
[![GitHub участники](https://img.shields.io/github/contributors/githubuser0xFFFF/Qt-Advanced-Docking-System?color=ffdf00)](https://github.com/githubuser0xFFFF/Qt-Advanced-Docking-System/graphs/contributors)

Qt Advanced Docking System позволяет создавать настраиваемые макеты с использованием полнофункциональной
докинг-окна, аналогичный тому, что имеется во многих популярных интегрированных средах разработки (IDE), таких как Visual Studio.
интегрированных средах разработки (IDE), таких как Visual Studio.

- [Что нового...](https://github.com/githubuser0xFFFF/Qt-Advanced-Docking-System/releases/latest)
- [Документация](doc/user-guide.md)
- Оригинальный репозиторий: https://github.com/githubuser0xFFFF/Qt-Advanced-Docking-System

[![Видео Advanced Docking](doc/advanced-docking_video.png)](https://www.youtube.com/watch?v=7pdNfafg3Qc)

## New and Noteworthy

В выпуске [4.1](https://github.com/githubuser0xFFFF/Qt-Advanced-Docking-System/releases/latest) значительно улучшена функциональность автоскрытия, а также усовершенствована функция 
для перетаскивания виджетов док-станции на вкладки док-области. Вот основные моменты новой версии:

#### Drag & Drop to Auto-Hide

Nвы можете легко перетащить любой виджет дока или любой плавающий виджет к границам
границы окна, чтобы закрепить его в качестве автоскрывающейся вкладки в одной из четырех боковых панелей.
При перетаскивании док-виджета вблизи одной из четырех границ окна отображаются специальные
Если перетащить док-виджет вплотную к границам одного из четырех окон, будут показаны специальные накладки, указывающие на область падения для автоскрывающихся виджетов:

![Auo-Hide drag to Sidebar](doc/AutoHide_Drag_to_Sidebar.gif)

Разумеется, это относится и к доковым зонам:

![Auo-Hide drag Dock Area](doc/AutoHide_Drag_DockArea.gif)

Если перетащить виджет док-станции или область док-станции в боковую панель, то можно даже
контроль над тем, куда вставляются вкладки. Просто проведите мышью по определенной
автоскрывающейся вкладки, и перетащенный док-виджет будет вставлен перед этой вкладкой.
Перетащите мышь в область боковой панели за последней вкладкой, и перетащенный виджет будет
будет добавлен в качестве последней вкладки. На следующем снимке экрана виджет **Image Viewer 1** будет
будет вставлен перед **Table 0** Вкладка Автоскрытие и **Image Viewer 2**
добавляется за последней вкладкой:

![Auo-Hide tab insert order](doc/AutoHide_Tab_Insert_Order.gif)

#### Auto-Hide Tab Insertion Order

Также можно перетаскивать вкладки Auto-Hide в новое положение автоскрытия.
Это означает, что их можно перетащить на другую границу или боковую панель:

![Auto-Hide change sidebar](doc/AutoHide_Change_Sidebar.gif)

#### Auto-Hide Tab Sorting

Вкладки Auto-Hide можно перетащить на новую позицию в текущей боковой панели 
для их сортировки:

![Auo-Hide sort tabs](doc/AutoHide_Sort_Tabs.gif)

#### Auto-Hide Drag to Float / Dock

Но это еще не все. Вы также можете просто переместить вкладки Auto-Hide на другой
плавающий виджет или пристыковать их с помощью перетаскивания:
![Auo-Hide drag to float or dock](doc/AutoHide_Drag_to_Float_or_Dock.gif)

#### Auto-Hide Context Menu

Все вкладки Auto-Hide теперь имеют контекстное меню, которое предоставляет все функциональные возможности
знакомые по вкладкам виджета Dock. С помощью пункта **Pin To...** из контекстного меню
контекстного меню можно легко переместить вкладку Auto-Hide в другую боковую панель Auto-Hide
боковая панель:

![Auo-Hide context menu](doc/AutoHide_Context_Menu.png)

#### Dock Area Tab Insert Order

И, наконец, в новой версии также улучшена стыковка виджетов
во вкладки области Dock. Как и в случае с автоскрытием вкладок, теперь можно определить позицию, в которую будет вставлена вкладка, наведя курсор мыши на уже существующую вкладку (вставка перед вкладкой) или за последней вкладкой 
(добавление):

![Dock area tab insert order](doc/DockArea_Tab_Insertion_Order.gif)

В [релиз 4.0](https://github.com/githubuser0xFFFF/Qt-Advanced-Docking-System/releases/latest)
добавлены следующие возможности:

- Функциональность автоскрытия ([Читать больше...](#auto-hide-functionality))

![Auto Hide Functionality](doc/AutoHide_Animation.gif)

- Улучшенное демо-приложение с новыми док-виджетами для просмотра изображений
  
![Auto Hide Functionality](doc/Feature_ImageViewer.png)

- Visual Studio как CSS-тема в демонстрационном приложении

В [релиз 3.8](https://github.com/githubuser0xFFFF/Qt-Advanced-Docking-System/releases/3.8.3)
добавлены следующие возможности:

- возможность закрытия вкладок средней кнопкой мыши
- флаг `DeleteContentOnClose` для динамического удаления и создания виджета дока
  содержимое
- улучшена функциональность подсветки фокуса

В [релиз 3.7](https://github.com/githubuser0xFFFF/Qt-Advanced-Docking-System/releases/tag/3.7.2)
добавляет следующие возможности:

- поддержка **Qt6.**
- поддержка для [empty dock area](doc/user-guide.md#empty-dock-area)

В [релиз 3.6](https://github.com/githubuser0xFFFF/Qt-Advanced-Docking-System/releases/tag/3.6.3)
добавляет несколько новых приятных возможностей:

- поддержка [central widget](doc/user-guide.md#central-widget) концепт

![Central Widget](doc/central_widget.gif)

- поддержка [native floating widgets](doc/user-guide.md#floatingcontainerforcenativetitlebar-linux-only) на Линуксе

![FloatingContainerForceNativeTitleBar true](doc/cfg_flag_FloatingContainerForceNativeTitleBar_true.png)

Обе возможности являются вкладом пользователей ADS. Прочитайте [документацию](doc/user-guide.md)
чтобы узнать больше об обеих новых возможностях.

В [релизе 3.5](https://github.com/githubuser0xFFFF/Qt-Advanced-Docking-System/releases/tag/3.5.0)
добавлена новая функция [focus highlighting](doc/user-guide.md#focushighlighting).
Эта опциональная возможность позволяет подсвечивать сфокусированный виджет дока так, как вы
как в Visual Studio.

![FocusHighlighting](doc/cfg_flag_FocusHighlighting.gif)

 [learn more...](doc/user-guide.md#focushighlighting)

## Features

### Overview

- [New and Noteworthy](#new-and-noteworthy)
    - [Drag \& Drop to Auto-Hide](#drag--drop-to-auto-hide)
    - [Auto-Hide Tab Insertion Order](#auto-hide-tab-insertion-order)
    - [Auto-Hide Tab Sorting](#auto-hide-tab-sorting)
    - [Auto-Hide Drag to Float / Dock](#auto-hide-drag-to-float--dock)
    - [Auto-Hide Context Menu](#auto-hide-context-menu)
    - [Dock Area Tab Insert Order](#dock-area-tab-insert-order)
- [Features](#features)
  - [Overview](#overview)
  - [Docking everywhere - no central widget](#docking-everywhere---no-central-widget)
  - [Docking inside floating windows](#docking-inside-floating-windows)
  - [Grouped dragging](#grouped-dragging)
  - [Perspectives for fast switching of the complete main window layout](#perspectives-for-fast-switching-of-the-complete-main-window-layout)
  - [Opaque and non-opaque splitter resizing](#opaque-and-non-opaque-splitter-resizing)
  - [Cancelable docking process](#cancelable-docking-process)
  - [Tab-menu for easy handling of many tabbed dock widgets](#tab-menu-for-easy-handling-of-many-tabbed-dock-widgets)
  - [Many different ways to detach dock widgets](#many-different-ways-to-detach-dock-widgets)
  - [Supports deletion of dynamically created dock widgets](#supports-deletion-of-dynamically-created-dock-widgets)
  - [Auto-Hide Functionality](#auto-hide-functionality)
- [Python Bindings](#python-bindings)
  - [PySide6](#pyside6)
  - [PyQt5](#pyqt5)
- [Tested Compatible Environments](#tested-compatible-environments)
  - [Supported Qt Versions](#supported-qt-versions)
  - [Windows](#windows)
  - [macOS](#macos)
  - [Linux](#linux)
- [Build](#build)
  - [Qt5 on Ubuntu 18.04 or 20.04](#qt5-on-ubuntu-1804-or-2004)
  - [Qt5 on Ubuntu 22.04](#qt5-on-ubuntu-2204)
  - [Qt6 on Ubuntu 22.04](#qt6-on-ubuntu-2204)
- [Getting started / Example](#getting-started--example)
- [License information](#license-information)
- [Donation](#donation)
- [Showcase](#showcase)
  - [Qt Creator IDE](#qt-creator-ide)
  - [Qt Design Studio](#qt-design-studio)
  - [CETONI Elements](#cetoni-elements)
  - [ezEditor](#ezeditor)
  - [D-Tect X](#d-tect-x)
  - [HiveWE](#hivewe)
  - [Ramses Composer](#ramses-composer)
  - [Plot Juggler](#plot-juggler)
  - [Notepad Next](#notepad-next)
  - [MetGem](#metgem)
  - [PRE Workbench](#pre-workbench)
  - [RDE – Robox Development Environment](#rde--robox-development-environment)
  - [ResInsight](#resinsight)
  - [ADTF 3](#adtf-3)
  - [DREAM.3D NX](#dream3d-nx)
  - [LabPlot](#labplot)
- [Alternative Docking System Implementations](#alternative-docking-system-implementations)
  - [KDDockWidgets](#kddockwidgets)
  - [QtitanDocking](#qtitandocking)
  - [DockingPanes](#dockingpanes)

### Docking everywhere - no central widget

Здесь нет центрального виджета, как в системе докинга Qt. Вы можете пристыковаться к каждой
границе главного окна или в каждой области дока - таким образом, вы можете пристыковаться практически везде.
можно стыковаться практически везде.

![Dropping widgets](doc/preview-dragndrop.png)

![Dropping widgets](doc/preview-dragndrop_dark.png)

### Docking inside floating windows

Разницы между главным окном и плавающим окном нет. Стыковка
в плавающие окна поддерживается.

![Docking inside floating windows](doc/floating-widget-dragndrop.png)

![Docking inside floating windows](doc/floating-widget-dragndrop_dark.png)

### Grouped dragging

При перетаскивании панели заголовков док-станции перетаскиваются все вкладки, на которых она установлена. 
будут перетащены. Таким образом, можно перемещать целые группы виджетов с вкладками в
плавающий виджет или из одной области дока в другую.

![Grouped dragging](doc/grouped-dragging.gif)

![Grouped dragging](doc/grouped-dragging_dark.png)

### Perspectives for fast switching of the complete main window layout

Перспектива определяет набор и расположение док-окон в главном окне
окне. Вы можете сохранить текущее расположение док-менеджера в именованной
перспективу, чтобы создать свою собственную перспективу. В дальнейшем можно просто
выбрать перспективу из списка перспектив, чтобы быстро переключить весь 
расположение главного окна.

![Perspective](doc/perspectives.gif)

![Perspective](doc/perspectives_dark.png)

### Opaque and non-opaque splitter resizing

Усовершенствованная система докинга использует стандартные QSplitters в качестве разделителей размеров и, таким образом, поддерживает непрозрачные и непрозрачные функции изменения размеров QSplitter. В некоторых редких случаях, для очень сложных виджетов или на медленных машинах, изменение размера через разделитель на лету может привести к мерцанию и бликованию отрисованного содержимого внутри виджета. Глобальный флаг док-менеджера `OpaqueSplitterResize` настраивает поведение сплиттеров при изменении размера. Если этот флаг установлен, то при интерактивном перемещении разделителей размеры виджетов будут изменяться динамически (непрозрачно).

![Opaque resizing](doc/opaque_resizing.gif)

Если этот флаг сброшен, то изменение размеров виджета откладывается до отпускания кнопки мыши - это своего рода разделитель ленивого изменения размеров.

![Non-opaque resizing](doc/non_opaque_resizing.gif)

### Cancelable docking process

В отличие от стандартной системы докинга Qt, докинг с помощью ADS больше похож на операцию перетаскивания. Это означает, что перетащенный док-виджет или док-область не разворачивается немедленно. Вместо этого создается виджет предварительного просмотра и перетаскивается, чтобы указать будущее положение док-виджета или док-области. Сама операция стыковки выполняется только при отпускании кнопки мыши. Это позволяет отменить активную операцию перетаскивания с помощью клавиши escape.

Виджет предварительного просмотра при перетаскивании может быть настроен с помощью ряда глобальных флагов докменеджера:
- `DragPreviewIsDynamic`: если этот флаг включен, то предварительный просмотр будет динамически подстраиваться под область падения
- `DragPreviewShowsContentPixmap`: созданное окно предварительного просмотра при перетаскивании отображает статическую копию содержимого перетаскиваемого док-виджета/док-области
- `DragPreviewHasWindowFrame`: этот флаг устанавливает, будет ли окно предварительного просмотра при перетаскивании без рамки, как QRubberBand, или будет выглядеть как настоящее окно

### Tab-menu for easy handling of many tabbed dock widgets

Вкладки - это хороший способ быстрого переключения между док-виджетами в док-области. Однако если количество док-виджетов в док-области слишком велико, это может повлиять на удобство использования панели вкладок. Чтобы не потеряться в этой ситуации, можно воспользоваться меню вкладок. Меню позволяет быстро выбрать из выпадающего меню тот доквиджет, который необходимо активизировать.

![Tab menu](doc/tab_menu.gif)

### Many different ways to detach dock widgets

Отсоединить док-виджеты, а также док-области можно следующими способами:

- перетаскиванием вкладки виджета дока или строки заголовка области дока
- двойным щелчком на вкладке или строке заголовка
- с помощью пункта меню Отсоединить из выпадающего меню вкладки и строки заголовка

### Supports deletion of dynamically created dock widgets

Обычно при нажатии на кнопку закрытия виджета док-станции он просто скрывается, и пользователь может снова показать его с помощью действия toggleView() виджета док-станции. Это предназначено для пользовательских интерфейсов со статическим количеством виджетов. Однако усовершенствованная система докинга поддерживает и динамические док-виджеты, которые будут удаляться при закрытии. Если для определенного док-виджета установить флаг `DockWidgetDeleteOnClose`, то при закрытии этого док-виджета он будет удален. Это позволяет реализовать пользовательские интерфейсы с динамически создаваемыми редакторами, например, в текстовых редакторах или средствах разработки исходного кода.

### Auto-Hide Functionality

В версии 4.0 ADS добавлена новая функция **Auto-Hide**. Благодаря
[первоначальному вкладу](https://github.com/githubuser0xFFFF/Qt-Advanced-Docking-System/pull/452) Ахмада Сярифуддина (Ahmad Syarifuddin)](https://github.com/SyarifFakhri) удалось закрыть этот давний [запрос](https://github.com/SyarifFakhri).
удалось закрыть этот давний [запрос](https://github.com/githubuser0xFFFF/Qt-Advanced-Docking-System/issues/147). Функция "Auto-Hide"
позволяет отображать больше информации, используя меньше места на экране, скрывая или показывая
окна, прикрепленные к одной из четырех границ док-контейнера.

![Auto-Hide Movie](doc/AutoHide_Movie.gif)

Система Advanced Docking
Система поддерживает функцию "Auto-Hide" для **всех** док-контейнеров - то есть,
для главного окна и для каждого плавающего виджета. Ниже приведен краткий список всех
функций автоскрытия:

- поддерживается для главного окна и всех плавающих док-контейнеров
- поддержка показа и скрытия по щелчку или наведению мыши
- поддерживает флаг изменения размера непрозрачного/непрозрачного сплиттера
- контекстное меню для прикрепления виджета дока или всей области дока к определенной границе
- опция конфигурации для настройки того, должна ли кнопка прикрепления прикреплять текущую вкладку док-виджета или всю область дока к определенной границе
  вкладку док-виджета или всю область дока
- щелчок на кнопке, удерживая клавишу Ctrl, позволяет закрепить всю область дока
- возможность полной стилизации под CSS
- обратно совместимый формат файла состояния - можно загружать старые версии док менеджера
  файлы состояний без поддержки автоскрытия, а старые версии могут загружать новые состояния
  файлы с информацией о состоянии Auto-Hide

Подробнее о параметрах конфигурации автоматического скрытия в [интерактивной документации...](doc/user-guide.md#auto-hide-configuration-flags)

## Python Bindings

![Python Logo](doc/python_logo.png)

Благодаря вкладу нескольких пользователей, система Advanced Docking System поставляется с полной интеграцией в Python
полностью интегрирована с Python. Доступны привязки к Python для **PyQt5** и
**PySide6**.

### PySide6

Пакет PySide6 ADS доступен через PyPi и может быть установлен на Windows,
macOS и Linux:

```bash
pip install PySide6-QtAds
```

Код примеров доступен [здесь](https://github.com/mborgerson/Qt-Advanced-Docking-System/tree/pyside6/examples). Для работы примеров необходимо также установить последнюю версию qtpy
из исходного кода (pip install https://github.com/spyder-ide/qtpy/archive/refs/heads/master.zip).
В создании связки PySide6 принимали участие:

- [mborgerson](https://github.com/mborgerson)

Для отслеживания проблем, связанных с PySide6-QtAds, просьба отправлять их в форк [pyside6_qtads](https://github.com/mborgerson/pyside6_qtads). Для получения дополнительной информации о связке PySide6 читайте [this](https://github.com/githubuser0xFFFF/Qt-Advanced-Docking-System/issues/298) issue.

### PyQt5

Пакет доступен через [conda-forge](https://github.com/conda-forge/pyqtads-feedstock).
Интеграция в python была сделана следующими людьми:

- [n-elie](https://github.com/n-elie)
- [Hugo Slepicka](https://github.com/hhslepicka)
- [K Lauer](https://github.com/klauer)

AИнтеграция с Python также доступна через PyPi. Вы можете установить
[PyQtAds](https://pypi.org/project/PyQtAds/) с помощью программы pip. Эта возможность была
Вклад в этот проект внесли:

- [Mira Weller](https://github.com/luelista)

## Tested Compatible Environments

### Supported Qt Versions

Библиотека поддерживает **Qt5** и **Qt6**.

### Windows

Windows 10 [![Статус сборки](https://ci.appveyor.com/api/projects/status/qcfb3cy932jw9mpy/branch/master?svg=true)](https://ci.appveyor.com/project/githubuser0xFFFF/qt-advanced-docking-system/branch/master)

Библиотека разрабатывалась под Windows и для Windows. Она используется в коммерческом Windows-приложении и поэтому постоянно тестируется.

### macOS

macOS [![Статус сборки](https://travis-ci.org/githubuser0xFFFF/Qt-Advanced-Docking-System.svg?branch=master)](https://travis-ci.org/githubuser0xFFFF/Qt-Advanced-Docking-System)

Приложение может быть скомпилировано для macOS. Один из пользователей сообщил, что библиотека работает на macOS. Мы это не проверяли.

![Advanced Docking on macOS](doc/macos.png)

### Linux

[![Build Status](https://travis-ci.org/githubuser0xFFFF/Qt-Advanced-Docking-System.svg?branch=master)](https://travis-ci.org/githubuser0xFFFF/Qt-Advanced-Docking-System)
[![Build status](https://github.com/githubuser0xFFFF/Qt-Advanced-Docking-System/workflows/linux-builds/badge.svg)](https://github.com/githubuser0xFFFF/Qt-Advanced-Docking-System/actions?query=workflow%3Alinux-builds)

К сожалению, не существует такого понятия, как операционная система Linux. Linux - это гетерогенная среда с множеством различных дистрибутивов. Поэтому невозможно поддерживать "Linux", как это возможно для Windows. Можно лишь поддерживать и тестировать небольшое подмножество дистрибутивов Linux. Библиотека может быть скомпилирована для некоторых дистрибутивов Linux, а также была разработана и протестирована. В зависимости от используемого оконного менеджера или композитора, виджеты дока
с собственными полосами заголовков поддерживаются или нет. Если собственные строки заголовков не поддерживаются,
библиотека переключается на виджеты заголовков на основе `QWidget`..

- **Kubuntu 18.04 and 19.10** - Используется KWin - нет собственных строк заголовков
- **Ubuntu 18.04, 19.10 and 20.04** - Поддерживаются собственные строки заголовков
- **Ubuntu 22.04** - Используется Wayland -> нет родных строк заголовков

К дистрибутиву Linux предъявляются некоторые требования:

- X-сервер, поддерживающий ARGB-визуализацию, и оконный менеджер композитинга. Это необходимо для отображения полупрозрачных оверлеев доков ([https://doc.qt.io/qt-5/qwidget.html#creating-translucent-windows](https://doc.qt.io/qt-5/qwidget.html#creating-translucent-windows)). Если ваш дистрибутив Linux этого не поддерживает или если вы отключили эту возможность, то, скорее всего, вы увидите проблему [#95](https://github.com/githubuser0xFFFF/Qt-Advanced-Docking-System/issues/95).
- Wayland пока не поддерживается Qt должным образом. Если вы используете Wayland, то необходимо установить тип сессии x11: `XDG_SESSION_TYPE=x11 ./AdvancedDockingSystemDemo`. Более подробную информацию об этом вы найдете в выпуске [#288](https://github.com/githubuser0xFFFF/Qt-Advanced-Docking-System/issues/288).

Screenshot Kubuntu:
![Advanced Docking on Kubuntu Linux](doc/linux_kubuntu_1804.png)

Screenshot Ubuntu:
![Advanced Docking on Ubuntu Linux](doc/linux_ubuntu_1910.png)

## Build

Для сборки Linux требуются собственные заголовочные файлы. Убедитесь, что они установлены.
Библиотека использует SVG-иконки, поэтому убедитесь, что установлена поддержка Qt SVG. Демоверсия
приложение создает `QQuickWidget` для тестирования, поэтому убедитесь, что необходимые
библиотеки установлены.

### Qt5 on Ubuntu 18.04 or 20.04

```bash
sudo apt install qt5-default qtbase5-private-dev
```

### Qt5 on Ubuntu 22.04

```bash
sudo apt install qtbase5-dev qtbase5-private-dev qtbase5-dev-tools libqt5svg5 libqt5qml5 qtdeclarative5-dev
```

### Qt6 on Ubuntu 22.04

```bash
sudo apt install qt6-default qt6-base-dev qt6-base-private-dev qt6-tools-dev libqt6svg6 qt6-qtdeclarative
```

Откройте файл `ads.pro` с помощью QtCreator и запустите сборку, вот и все.
Вы можете запустить демонстрационный проект и протестировать его самостоятельно.

## Getting started / Example

В следующем примере приведен минимальный код, необходимый для использования расширенной системы докинга Qt.

*MainWindow.h*

```cpp
#include <QMainWindow>
#include "DockManager.h"

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private:
    Ui::MainWindow *ui;
    
    // Основной контейнер для докинга
    ads::CDockManager* m_DockManager;
};
```

*MainWindow.cpp*

```cpp
#include "MainWindow.h"
#include "ui_MainWindow.h"

#include <QLabel>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    // Создание док-менеджера после настройки пользовательского интерфейса. Поскольку
    // родительским параметром является QMainWindow, докменеджер регистрирует
    // себя в качестве центрального виджета, поэтому пользовательский интерфейс должен быть настроен первым.
    m_DockManager = new ads::CDockManager(this);

    // Создайте пример ярлыка содержимого - это может быть любой специфический для приложения
    // виджет
    QLabel* l = new QLabel();
    l->setWordWrap(true);
    l->setAlignment(Qt::AlignTop | Qt::AlignLeft);
    l->setText("Lorem ipsum dolor sit amet, consectetuer adipiscing elit. ");

    // Создаем док-виджет с заголовком Label 1 и устанавливаем созданный ярлык
    // в качестве содержимого док-виджета
    ads::CDockWidget* DockWidget = new ads::CDockWidget("Label 1");
    DockWidget->setWidget(l);

    // Добавьте в меню действие toggleViewAction виджета док-станции, чтобы дать // пользователю возможность показать виджет док-станции, если он закрыт.
    // пользователю возможность показать виджет дока, если он был закрыт
    ui->menuView->addAction(DockWidget->toggleViewAction());

    // Добавление виджета док-станции в верхнюю область виджетов док-станции
    m_DockManager->addDockWidget(ads::TopDockWidgetArea, DockWidget);
}

MainWindow::~MainWindow()
{
    delete ui;
}
```

## License information

[![License: LGPL v2.1](https://img.shields.io/badge/License-LGPL%20v2.1-blue.svg)](gnu-lgpl-v2.1.md)
Этот проект использует [LGPLv2.1 license](gnu-lgpl-v2.1.md)

## Donation

Если этот проект поможет вам сократить время разработки или просто понравится, можете угостить меня чашечкой кофе :coffee::wink:.

<a href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=85R64TMMSY9T6">
  <img src="doc/donate.png" alt="Donate with PayPal" width="160"/>
</a>

## Showcase

### [Qt Creator IDE](https://www.qt.io/development-tools)

Начиная с версии 4.12, Qt Creator использует Advanced Docking Framework для своего
Qt Quick Designer. Это повышает удобство работы при использовании нескольких экранов.

![Qt Creator](doc/showcase_qtcreator.png)

### [Qt Design Studio](https://www.qt.io/ui-design-tools)

Взято из [Qt Blog](https://www.qt.io/blog/qt-design-studio-1.5-beta-released):

> Наиболее очевидным изменением в [Qt Design Studio 1.5](https://www.qt.io/blog/qt-design-studio-1.5-beta-released) является интеграция док-виджетов с использованием системы Qt Advanced Docking System. Это позволяет пользователю полностью настраивать рабочее пространство, а также разворачивать любое представление в собственное окно верхнего уровня. Это особенно повышает удобство работы при использовании нескольких экранов.

[![Qt Design Studio](doc/showcase_qt_design_studio_video.png)](https://youtu.be/za9KBWcFXEw?t=84)

