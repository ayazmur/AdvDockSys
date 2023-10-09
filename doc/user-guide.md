# Руководство пользователя

- [Configuration Flags](#configuration-flags)
  - [Setting Configuration Flags](#setting-configuration-flags)
  - [`ActiveTabHasCloseButton`](#activetabhasclosebutton)
  - [`DockAreaHasCloseButton`](#dockareahasclosebutton)
  - [`DockAreaCloseButtonClosesTab`](#dockareaclosebuttonclosestab)
  - [`OpaqueSplitterResize`](#opaquesplitterresize)
  - [`XmlAutoFormattingEnabled`](#xmlautoformattingenabled)
  - [`XmlCompressionEnabled`](#xmlcompressionenabled)
  - [`TabCloseButtonIsToolButton`](#tabclosebuttonistoolbutton)
  - [`AllTabsHaveCloseButton`](#alltabshaveclosebutton)
  - [`RetainTabSizeWhenCloseButtonHidden`](#retaintabsizewhenclosebuttonhidden)
  - [`DragPreviewIsDynamic`](#dragpreviewisdynamic)
  - [`DragPreviewShowsContentPixmap`](#dragpreviewshowscontentpixmap)
  - [`DragPreviewHasWindowFrame`](#dragpreviewhaswindowframe)
  - [`AlwaysShowTabs`](#alwaysshowtabs)
  - [`DockAreaHasUndockButton`](#dockareahasundockbutton)
  - [`DockAreaHasTabsMenuButton`](#dockareahastabsmenubutton)
  - [`DockAreaHideDisabledButtons`](#dockareahidedisabledbuttons)
  - [`DockAreaDynamicTabsMenuButtonVisibility`](#dockareadynamictabsmenubuttonvisibility)
  - [`FloatingContainerHasWidgetTitle`](#floatingcontainerhaswidgettitle)
  - [`FloatingContainerHasWidgetIcon`](#floatingcontainerhaswidgeticon)
  - [`HideSingleCentralWidgetTitleBar`](#hidesinglecentralwidgettitlebar)
  - [`FocusHighlighting`](#focushighlighting)
  - [`EqualSplitOnInsertion`](#equalsplitoninsertion)
  - [`FloatingContainerForceNativeTitleBar` (Linux only)](#floatingcontainerforcenativetitlebar-linux-only)
  - [`FloatingContainerForceQWidgetTitleBar` (Linux only)](#floatingcontainerforceqwidgettitlebar-linux-only)
  - [`MiddleMouseButtonClosesTab`](#middlemousebuttonclosestab)
  - [`DisableTabTextEliding`](#disabletabtexteliding)
- [Auto-Hide Configuration Flags](#auto-hide-configuration-flags)
  - [Auto Hide Dock Widgets](#auto-hide-dock-widgets)
  - [Pinning Auto-Hide Widgets to a certain border](#pinning-auto-hide-widgets-to-a-certain-border)
  - [Show / Hide Auto-Hide Widgets via Mouse Over](#show--hide-auto-hide-widgets-via-mouse-over)
  - [Adding Auto Hide Widgets](#adding-auto-hide-widgets)
  - [Setting Auto-Hide Flags](#setting-auto-hide-flags)
  - [`AutoHideFeatureEnabled`](#autohidefeatureenabled)
  - [`DockAreaHasAutoHideButton`](#dockareahasautohidebutton)
  - [`AutoHideButtonTogglesArea`](#autohidebuttontogglesarea)
  - [`AutoHideButtonCheckable`](#autohidebuttoncheckable)
  - [`AutoHideSideBarsIconOnly`](#autohidesidebarsicononly)
  - [`AutoHideShowOnMouseOver`](#autohideshowonmouseover)
  - [`AutoHideCloseButtonCollapsesDock`](#autohideclosebuttoncollapsesdock)
- [DockWidget Feature Flags](#dockwidget-feature-flags)
  - [`DockWidgetClosable`](#dockwidgetclosable)
  - [`DockWidgetMovable`](#dockwidgetmovable)
  - [`DockWidgetFloatable`](#dockwidgetfloatable)
  - [`DockWidgetDeleteOnClose`](#dockwidgetdeleteonclose)
  - [`CustomCloseHandling`](#customclosehandling)
  - [`DockWidgetFocusable`](#dockwidgetfocusable)
  - [`DockWidgetForceCloseWithArea`](#dockwidgetforceclosewitharea)
  - [`NoTab`](#notab)
  - [`DeleteContentOnClose`](#deletecontentonclose)
- [Central Widget](#central-widget)
- [Empty Dock Area](#empty-dock-area)
- [Custom Close Handling](#custom-close-handling)
- [Styling](#styling)
  - [Disabling the Internal Style Sheet](#disabling-the-internal-style-sheet)

## Флаги конфигурации

Система Advanced Docking System имеет ряд глобальных опций конфигурации, позволяющих
конфигурирования дизайна и функциональности стыковочной системы. Каждая опция
подробно рассматривается в следующих разделах.

### Установка флагов конфигурации

Перед созданием экземпляра док-менеджера необходимо установить флаги конфигурации
иначе менеджер не будет создан корректно и произойдет
произойдет аварийное завершение работы. Таким образом, установка конфигурационных флагов
это первое, что необходимо сделать, если вы используете данную библиотеку.

```c++
CDockManager::setConfigFlags(CDockManager::DefaultOpaqueConfig);
CDockManager::setConfigFlag(CDockManager::RetainTabSizeWhenCloseButtonHidden, true);
...
d->DockManager = new CDockManager(this);
```

При установке флагов конфигурации можно установить отдельные флаги с помощью функции `CDockManager::setConfigFlag
функцию `CDockManager::setConfigFlag` или установить все флаги с помощью функции `CDockManager::setConfigFlags`.
функцию `CDockManager::setConfigFlags`. Вместо того чтобы устанавливать все
флагов по отдельности, лучше выбрать предопределенный набор конфигурационных
флагов, а затем изменять отдельные флаги. Ниже приведены предопределенные
конфигурации

- `DefaultNonOpaqueConfig` - использует непрозрачный сплиттер для изменения размеров и непрозрачную стыковку
- `DefaultOpaqueConfig` - используется изменение размеров непрозрачного сплиттера и непрозрачная стыковка

Выберите одну из этих предопределенных конфигураций, а затем измените следующие
флаги конфигурации, чтобы настроить стыковочную систему под свои нужды.

### `ActiveTabHasCloseButton`

Если этот флаг установлен (конфигурация по умолчанию), то активная вкладка в области вкладок имеет
кнопку закрытия.

![ActiveTabHasCloseButton true](cfg_flag_ActiveTabHasCloseButton_true.png)

Если этот флаг снят, то активная вкладка не имеет кнопки закрытия. Вы можете комбинировать
этот флаг с флагом `DockAreaCloseButtonClosesTab`, чтобы использовать кнопку закрытия
док-зоны для закрытия отдельных вкладок.

![ActiveTabHasCloseButton true](cfg_flag_ActiveTabHasCloseButton_false.png)

### `DockAreaHasCloseButton`

Если флаг установлен (конфигурация по умолчанию), то каждая док-зона имеет кнопку закрытия.

![DockAreaHasCloseButton true](cfg_flag_DockAreaHasCloseButton_true.png)

Если этот флаг сброшен, то док-зоны не имеют кнопки закрытия.

![DockAreaHasCloseButton true](cfg_flag_DockAreaHasCloseButton_false.png)

### `DockAreaCloseButtonClosesTab`.

Если флаг установлен, кнопка закрытия док-зоны закрывает активную вкладку,
если флаг не установлен, то закрывается вся док-область (по умолчанию).

### `OpaqueSplitterResize`

Усовершенствованная система докинга использует стандартные `QSplitters` в качестве разделителей размеров и, таким образом, поддерживает непрозрачные и непрозрачные функции изменения размеров `QSplitter`. В некоторых редких случаях, для очень сложных виджетов или на медленных машинах, изменение размера через разделитель на лету может привести к мерцанию и бликованию отрисованного содержимого внутри виджета. Этот глобальный флаг док-менеджера настраивает поведение разделителей при изменении размера. Если флаг установлен, то при интерактивном перемещении разделителей размеры виджетов будут изменяться динамически (непрозрачно). Если выбрать предопределенную конфигурацию `DefaultOpaqueConfig`, то именно такое поведение будет задано.

![Opaque resizing](opaque_resizing.gif)

Если этот флаг сброшен, то изменение размеров виджета откладывается до отпускания кнопки мыши - это своего рода разделитель ленивого изменения размеров. Если выбрать предопределенную
конфигурацию `DefaultNonOpaqueConfig`, то это и есть настроенное поведение.

![Non-opaque resizing](non_opaque_resizing.gif)

### `XmlAutoFormattingEnabled`

Если эта опция включена, то программа написания XML автоматически добавляет переносы строк и отступы к
пустые участки между элементами (ignorable whitespace). Это используется, когда
сохранении текущего состояния или перспективы. По умолчанию эта функция отключена.

### `XmlCompressionEnabled`

Если эта опция включена, то XML-вывод будет сжат и перестанет быть человекочитаемым.
Эта опция включена по умолчанию, чтобы минимизировать размер сохраняемых данных.
### `TabCloseButtonIsToolButton`

При включении кнопки закрытия вкладок будут `QToolButtons`, а не `QPushButtons` - по умолчанию отключены. 
отключенные по умолчанию. Обычно конфигурация по умолчанию не вызывает затруднений, но если в вашем
приложение требует `QToolButtons` вместо `QPushButtons` по соображениям стилистики
или по каким-либо другим причинам, то вы можете включить этот флаг.

### `AllTabsHaveCloseButton`

Если этот флаг установлен, то на всех закрываемых вкладках отображается кнопка закрытия. Преимущество
Преимущество этой настройки заключается в том, что размер вкладок не изменяется, и пользователь может сразу же закрыть каждую вкладку.
пользователь может сразу закрыть каждую вкладку. Недостатком является то, что все вкладки занимают
больше места.

![AllTabsHaveCloseButton true](cfg_flag_AllTabsHaveCloseButton_true.png)

Если этот флаг сброшен, то кнопка закрытия будет только у активной вкладки (по умолчанию)
и, следовательно, вкладкам требуется меньше места.

![AllTabsHaveCloseButton false](cfg_flag_ActiveTabHasCloseButton_true.png)

### `RetainTabSizeWhenCloseButtonHidden`

Если этот флаг установлен, то место для кнопки закрытия будет зарезервировано, даже если кнопка не видна.
кнопка закрытия не видна. По умолчанию этот флаг отключен. Если этот флаг
отключен, размер вкладки динамически изменяется, если кнопка закрытия
видимой / скрытой на вкладке. Если этот флаг включен, то размер вкладки всегда остается
постоянным, то есть, если флаг включен, вкладкам требуется больше места.

![AllTabsHaveCloseButton false](cfg_flag_RetainTabSizeWhenCloseButtonHidden_true.png)

### `DragPreviewIsDynamic`

Если включена непрозрачная разблокировка, то этот флаг определяет поведение окна предварительного просмотра при перетаскивании. 
окна предварительного просмотра. Если этот флаг установлен, то у пользователя будет создаваться впечатление, что
впечатление, что плавающее окно предварительного просмотра перетаскивания динамически подстраивается под область падения
области. Для того чтобы создать правильное впечатление, следует отключить флаги
`DragPreviewShowsContentPixmap` и `DragPreviewHasWindowFrame`.

```c++
CDockManager::setConfigFlag(CDockManager::DragPreviewIsDynamic, true);
CDockManager::setConfigFlag(CDockManager::DragPreviewShowsContentPixmap, false);
CDockManager::setConfigFlag(CDockManager::DragPreviewHasWindowFrame, false);
```

![DragPreviewIsDynamic true](dynamic_drag_preview.gif)

### `DragPreviewShowsContentPixmap`

Если включена непрозрачная отстыковка, то в созданном окне предварительного просмотра перетаскивания отображается 
копию содержимого перетаскиваемого док-виджета/дока, если этот флаг включен (по умолчанию).
флаг включен (по умолчанию).

![DragPreviewShowsContentPixmap true](cfg_flag_DragPreviewShowsContentPixmap_true.png)

Если этот флаг отключен, то предварительный просмотр при перетаскивании будет представлять собой только прозрачное `QRubberBand`
как окно без какого-либо содержимого.

![DragPreviewShowsContentPixmap true](cfg_flag_DragPreviewShowsContentPixmap_false.png)

### `DragPreviewHasWindowFrame`

Если включена непрозрачная разблокировка, то этот флаг определяет, будет ли предварительный просмотр при перетаскивании без рамки (по умолчанию) или будет выглядеть как реальное окно. 
без рамки (по умолчанию) или выглядеть как реальное окно. Если флаг включен,
то предварительный просмотр при перетаскивании будет представлять собой прозрачное окно с рамкой системного окна.

![DragPreviewHasWindowFrame true](cfg_flag_DragPreviewHasWindowFrame_true.png)

### `AlwaysShowTabs`

Если эта опция включена, то вкладка док-виджета отображается всегда - даже если это единственный видимый док-виджет в плавающем виджете.
если он является единственным видимым виджетом док-станции в плавающем виджете. На рисунке ниже
слева флаг отключен (по умолчанию), а справа - включен
включен.

![AlwaysShowTabs false true](cfg_flag_AlwaysShowTabs_false_true.png)

### `DockAreaHasUndockButton`

Если флаг установлен (по умолчанию), то каждая док-зона имеет кнопку отстыковки (правое
изображение). Если флаг сброшен, то док-зона не имеет кнопки отстыковки (левое изображение)

![DockAreaHasUndockButton false true](cfg_flag_DockAreaHasUndockButton_false_true.png)

### `DockAreaHasTabsMenuButton`

Вкладки - это хороший способ быстрого переключения между док-виджетами в док-области.
Однако если количество док-виджетов в док-области слишком велико, это может повлиять на
удобство использования панели вкладок. Для отслеживания в такой ситуации можно использовать
меню вкладок. Меню позволяет быстро выбрать нужный доквиджет из выпадающего меню.
активизировать из выпадающего меню. Этот флаг показывает / скрывает кнопку меню вкладок
в строке заголовка док-области. В левой части флаг кнопки меню вкладок
снят.

![DockAreaHasTabsMenuButton false true](cfg_flag_DockAreaHasTabsMenuButton_false_true.png)

### `DockAreaHideDisabledButtons`

Если у док-виджета отключены некоторые флаги, например `DockWidgetClosable` или
`DockWidgetFloatable`, то соответствующие кнопки док-области, такие как кнопка закрытия
или отсоединения, будут отключены (выделены серым цветом). Это настройка по умолчанию
настройка.
![DockAreaHideDisabledButtons false](cfg_flag_DockAreaHideDisabledButtons_false.png)

Если флаг установлен, то отключенные кнопки док-области вообще не будут отображаться на панели инструментов - они будут скрыты.
- они будут скрыты.

![DockAreaHideDisabledButtons true](cfg_flag_DockAreaHideDisabledButtons_true.png)

### `DockAreaDynamicTabsMenuButtonVisibility`

Если этот флаг сброшен, то кнопка меню вкладок всегда видна. Это
настройка по умолчанию. Если флаг установлен, то кнопка меню вкладок будет отображаться
только тогда, когда это необходимо, т.е. если вкладки скрыты.

![DockAreaDynamicTabsMenuButtonVisibility false](cfg_flag_DockAreaDynamicTabsMenuButtonVisibility_true_visible.png)

Если вкладки не элиминированы, то кнопка меню вкладок скрыта.

![DockAreaDynamicTabsMenuButtonVisibility false](cfg_flag_DockAreaDynamicTabsMenuButtonVisibility_true_hidden.png)

### `FloatingContainerHasWidgetTitle`

Если установлено (по умолчанию), то заголовок окна плавающего виджета отражает заголовок текущего док-виджета
текущего виджета док-станции.

![FloatingContainerHasWidgetTitle true](cfg_flag_FloatingContainerHasWidgetTitle_true.png)

в противном случае в качестве заголовка окна отображается заголовок, установленный с помощью `CDockManager::setFloatingContainersTitle` или
имя приложения в качестве заголовка окна.

![FloatingContainerHasWidgetTitle false](cfg_flag_FloatingContainerHasWidgetTitle_false.png)

### `FloatingContainerHasWidgetIcon`

Если установлено, то значок плавающего виджета отражает значок текущего виджета док-станции

![FloatingContainerHasWidgetIcon true](cfg_flag_FloatingContainerHasWidgetIcon_true.png)

В противном случае (по умолчанию) отображается значок приложения.

![FloatingContainerHasWidgetIcon false](cfg_flag_FloatingContainerHasWidgetIcon_false.png)

### `HideSingleCentralWidgetTitleBar`

Если в главном док-контейнере (менеджере доков) имеется только один единственный видимый док-виджет
и если этот флаг установлен, то панель заголовка этого док-виджета будет скрыта.
Это имеет смысл только для неперетаскиваемых и неплавающих док-виджетов и позволяет
создание некоего "центрального" статического виджета. Поскольку панель заголовка скрыта
скрыта, невозможно перетащить центральный виджет, чтобы сделать его плавающим
или закрыть его с помощью кнопки закрытия.

![HideSingleCentralWidgetTitleBar true](cfg_flag_HideSingleCentralWidgetTitleBar_true.png)

Система Advanced Docking System предназначена для приложений без центрального статического виджета и обычно не знает о центральном статическом виджете.
виджета и обычно ничего не знает о центральном статическом виджете.
Поэтому по умолчанию этот флаг отключен, и центральный одиночный док-виджет
по-прежнему имеет панель заголовка, чтобы вытащить его из главного окна.

![HideSingleCentralWidgetTitleBar false](cfg_flag_HideSingleCentralWidgetTitleBar_false.png)

### `FocusHighlighting`

Если эта опция включена, то система докинга может выделять вкладку и компоненты
компоненты док-области другим стилем (т.е. другим цветом).
По умолчанию эта опция отключена и должна быть включена явно
поскольку она создает дополнительные накладные расходы. Менеджер док-станции должен реагировать на изменение фокуса
и перетаскивание док-виджета для выделения нужного док-виджета. Вам следует
включать эту функцию только в том случае, если она действительно необходима для вашего приложения.

Если функция включена, вы также можете подключиться к новому докменеджеру
сигнал `focusedDockWidgetChanged(CDockWidget* old, CDockWidget* now)`, чтобы
реагировать на изменение фокуса и подготавливать содержимое сфокусированного док-виджета
виджета.

Для фокусировки док-виджета можно щелкнуть на вкладке, панели заголовка или содержимом док-виджета
чтобы сфокусировать его.

![FocusHighlighting](cfg_flag_FocusHighlighting.gif)

Для сфокусированного виджета дока и вкладки виджета дока свойство `focused` будет установлено в true, и это свойство можно использовать для стилизации сфокусированного виджета дока.
будет установлено в true, и вы сможете использовать это свойство для придания сфокусированному виджету дока другого стиля
виджета. На рисунке выше используется следующая стилизация:

```css
/* Раскрасьте вкладку цветом выделения */
ads--CDockWidgetTab[focused="true"]
{
    background: palette(highlight);
    border-color: palette(highlight);
}

/* Используйте другой цвет значка кнопки закрытия, чтобы он соответствовал цвету теста */
ads--CDockWidgetTab[focused="true"] > #tabCloseButton
{
	qproperty-icon: url(:/ads/images/close-button-focused.svg)
}

/* Сделать наведенную кнопку закрытия фокуса немного светлее */
ads--CDockWidgetTab[focused="true"] > #tabCloseButton:hover
{
	background: rgba(255, 255, 255, 48);
}

/* Сделать нажатую кнопку закрытия еще более светлой */
ads--CDockWidgetTab[focused="true"] > #tabCloseButton:pressed
{
	background: rgba(255, 255, 255, 92);
}

/* Использовать другой цвет для ярлыка вкладки */
ads--CDockWidgetTab[focused="true"] QLabel
{
    color: palette(light);
}

/* Нарисуйте красивую сплошную линию для всей строки заголовка, чтобы создать иллюзию
   активной вкладки */
ads--CDockAreaWidget[focused="true"] ads--CDockAreaTitleBar
{
	background: transparent;
	border-bottom: 2px solid palette(highlight);
	padding-bottom: 0px;
}
```

Если у вас есть виджет содержимого, который по каким-либо причинам не поддерживает фокусировку
(например, `QVTKOpenGLStereoWidget` из библиотеки [VTK](https://github.com/Kitware/VTK)),
то можно вручную переключать фокус, реагируя на события мыши. На 
В следующем коде показано, как установить фильтр событий en на `QVTKOpenGLStereoWidget`
для корректного переключения фокуса по событию `QEvent::MouseButtonPress`:

```c++
static ads::CDockWidget* createVTK2DWindow(QMenu* ViewMenu, QObject* EventFilter)
{
    QVTKOpenGLStereoWidget* qvtkOpenGLStereoWidget = new QVTKOpenGLStereoWidget;
    ads::CDockWidget* DockWidget = new ads::CDockWidget("2D Window");
    DockWidget->setWidget(qvtkOpenGLStereoWidget);
    qvtkOpenGLStereoWidget->installEventFilter(EventFilter);
    qvtkOpenGLStereoWidget->setProperty("DockWidget", QVariant::fromValue(DockWidget));
    return DockWidget;
}
```

Теперь мы можем использовать функцию фильтра событий для реагирования на события мыши, а затем
использовать функцию док менеджера `setDockWidgetFocused()` для переключения фокуса:

```c++
bool CMainWindow::eventFilter(QObject *watched, QEvent *event)
{
    if (event->type() == QEvent::MouseButtonPress)
    {
        QVTKOpenGLStereoWidget* vtkWidget =  qobject_cast<QVTKOpenGLStereoWidget*>(watched);
        auto vDockWidget = vtkWidget->property("DockWidget");
        ads::CDockWidget* DockWidget = nullptr;
        if (vDockWidget.isValid())
        {
            DockWidget = qvariant_cast<ads::CDockWidget*>(vDockWidget);
        }

        if (DockWidget)
        {
            d->DockManager->setDockWidgetFocused(DockWidget);
        }
    }
    return false;
}
```

### `EqualSplitOnInsertion`

Этот флаг определяет, как будет распределяться пространство, если новый виджет дока будет вставлен в существующую область дока
вставляется в существующую область дока. По умолчанию флаг отключен. Если в существующую область дока вставлено 3 
док-виджетов вставляются со следующим кодом

```c++
d->DockManager->addDockWidget(ads::RightDockWidgetArea, DockWidget, EditorArea);
```

то вот результат, если флаг отключен:

![EqualSplitOnInsertion false](cfg_flag_EqualSplitOnInsertion_false.png)

Если флаг установлен, то пространство распределяется поровну между всеми виджетами 
в сплиттере:

![EqualSplitOnInsertion true](cfg_flag_EqualSplitOnInsertion_true.png)


### `FloatingContainerForceNativeTitleBar` (Linux only)

Начиная с версии 3.6 библиотека поддерживает собственные строки заголовков и украшения окон
для плавающих виджетов в Linux (благодаря вкладу пользователя).
Родные строки заголовка и оформление окон поддерживаются большинством оконных менеджеров Linux
менеджеров, таких как Compiz или Xfwm. Некоторые оконные менеджеры, например KWin, не поддерживают эту функцию должным образом
не поддерживают эту функцию. Родные плавающие виджеты выглядят лучше благодаря родному
стилистики и поддержки всех функций оконного менеджера, таких как привязка к границам окна
границы окна или максимизацию. Библиотека пытается определить оконный менеджер во время
во время выполнения программы и, если возможно, активизирует нативные элементы оформления окна:

![FloatingContainerForceNativeTitleBar true](cfg_flag_FloatingContainerForceNativeTitleBar_true.png)

Если вы хотите отменить это автоопределение, то можете активизировать этот флаг
флаг для принудительного использования собственных заголовков окон. Вы можете отменить автоопределение и этот
флаг, если установить переменную окружения `ADS_UseNativeTitle` в 0 или 1.

### `FloatingContainerForceQWidgetTitleBar` (Linux only)

Если ваш оконный менеджер (например, KWin) не поддерживает должным образом встроенные плавающие окна
окна, библиотека докинга возвращается к плавающим виджетам на основе QWidget
строки заголовка.

![FloatingContainerForceNativeTitleBar false](cfg_flag_FloatingContainerForceNativeTitleBar_false.png)

Если вы хотите отменить автоопределение, то можете активизировать этот флаг
для принудительного использования строк заголовков на основе QWidget. Вы можете отменить автоопределение и этот флаг, если установите переменную окружения `ADS_UseNativeTitle
флаг, если установить переменную окружения `ADS_UseNativeTitle` в 0 или 1.

### `MiddleMouseButtonClosesTab`

Если флаг установлен, то пользователь может использовать среднюю кнопку мыши для закрытия вкладки
под мышью. Таким образом, для закрытия вкладки не нужно точно нажимать кнопку закрытия вкладки.
закрыть вкладку. Достаточно просто щелкнуть средней кнопкой мыши на вкладке, как это
возможно в различных веб-браузерах.

![MiddleMouseButtonClosesTab true](cfg_flag_MiddleMouseButtonClosesTab.gif)

### `DisableTabTextEliding`

Установите этот флаг, чтобы отключить выравнивание текстов вкладок в закладках док-области.

## Auto-Hide Configuration Flags

### Auto Hide Dock Widgets

Система Advanced Docking System поддерживает функцию "Auto-Hide" для **all**
док-контейнеров. Функция "Auto Hide" позволяет отображать больше информации
используя меньше места на экране, скрывая или показывая окна, прикрепленные к одной из четырех границ док-контейнера 
четырех границ док-контейнера.

Включение этой функции добавляет кнопку со значком булавки в каждую область док-станции.

![DockAreaHasAutoHideButton true](cfg_flag_DockAreaHasAutoHideButton.png)

При нажатии на эту кнопку текущий виджет дока (или вся область - в зависимости от флагов конфигурации) будет прижат к определенной границе
флагов конфигурации) будет прикреплен к определенной границе. Граница выбирается
в зависимости от расположения док-области. Если щелкнуть на кнопке pin, удерживая клавишу
удерживая клавишу **Ctrl**, то вся область дока будет прикреплена к определенной границе
границе.

### Прикрепление виджетов автоскрытия к определенной границе

Если вы хотите прикрепить виджет док-станции или область док-станции к определенной границе,
то можно щелкнуть правой кнопкой мыши на вкладке док-виджета или на строке заголовка док-области
чтобы вызвать контекстное меню. Затем можно выбрать местоположение с помощью меню **Pin to**:

![Pin to](AutoHide_PinTo.png)

### Показ / скрытие автоскрытия виджетов при наведении мыши

Обычно виджеты Auto-Hide отображаются при щелчке на вкладке Auto-Hide и скрываются при повторном щелчке на вкладке Auto-Hide или при щелчке на любом другом виджете дока.
щелчком на вкладке Auto-Hide или щелчком на любом другом виджете док-станции в том же контейнере.
том же контейнере. Если установлен флаг конфигурации Auto-Hide `AutoHideShowOnMouseOver`,
виджет Auto-Hide будет показан, если пользователь наведет курсор мыши на вкладку Auto-Hide, и свернут, если курсор мыши наведет курсор на вкладку Auto-Hide.
сворачивается, если курсор мыши покидает виджет Auto-Hide. Показ и скрытие
по щелчку мыши по-прежнему работают, если эта функция включена.

### Добавление виджетов с автоматическим скрытием

Добавление виджета автоскрытия аналогично добавлению виджета дока, просто вызовите функцию
`dockManager->addAutoHideDockWidget()`.

```c++
CDockManager::setAutoHideConfigFlags(CDockManager::DefaultAutoHideConfig);
d->DockManager = new CDockManager(this);
CDockWidget* TableDockWidget = new CDockWidget("Table 1");
DockManager->addAutoHideDockWidget(SideBarLeft, TableDockWidget);
```

Как это работает, смотрите в примере `autohide` или в демонстрационном приложении.

### Установка флагов автоскрытия

Система Advanced Docking System имеет ряд флагов глобальной конфигурации для настройки
для настройки функции Auto-Hide. Флаги Auto-Hide следует устанавливать до
создания экземпляра менеджера доков. Это означает, что флаги Auto-Hide следует устанавливать после установки флагов конфигурации.
после установки флагов конфигурации.

```c++
CDockManager::setConfigFlag(CDockManager::FocusHighlighting, true);
CDockManager::setAutoHideConfigFlags(CDockManager::DefaultAutoHideConfig);
CDockManager::setAutoHideConfigFlag(CDockManager::AutoHideShowOnMouseOver, true);
...
d->DockManager = new CDockManager(this);
```

Если вы установили флаги Auto-Hide, то можно установить отдельные флаги с помощью функции `CDockManager::setAutoHideConfigFlag
функцию `CDockManager::setAutoHideConfigFlag` или установить все флаги с помощью функции
функции `CDockManager::setAutoHideConfigFlags`. Вместо того чтобы устанавливать все
флагов по отдельности, лучше выбрать предопределенный набор конфигурационных
флагов, а затем изменять отдельные флаги. Ниже приведены предопределенные
конфигурации

- `DefaultAutoHideConfig` - конфигурация автоматического скрытия по умолчанию

Выберите одну из этих предопределенных конфигураций, а затем измените следующие
флаги конфигурации, чтобы настроить систему стыковки под свои нужды.

### `AutoHideFeatureEnabled`

Включает/выключает функцию Auto-Hide. Только если этот флаг включен,
будут оцениваться и другие флаги Auto-Hide.

### `DockAreaHasAutoHideButton`

Если этот флаг установлен (по умолчанию), то каждая док-область имеет кнопку в строке заголовка для переключения автоскрытия. 
для переключения состояния Auto-Hide.

![DockAreaHasAutoHideButton true](cfg_flag_DockAreaHasAutoHideButton.png)

### `AutoHideButtonTogglesArea`

Если этот параметр установлен, то кнопка-фиксатор в строке заголовка док-области переключает всю область.
Если значение не установлено (по умолчанию), то кнопка переключает текущую активную вкладку/виджет док-станции.
виджета, а нажатие клавиши **Ctrl** при щелчке на кнопке переключает всю область.
полный ара.

### `AutoHideButtonCheckable`

Обычно кнопка pin в строке заголовка док-области не является проверяемой. Если этот
флаг установлен, то кнопка является проверяемой. Это означает, что если кнопка отмечена,
виджет док-станции будет прикреплен.

### `AutoHideSideBarsIconOnly`.

Обычно на вкладках Auto-Hide отображаются иконка и заголовок виджета док-станции:

![AutoHideSideBarsIconOnly false](cfg_flag_AutoHideSideBarsIconOnly_false.png)

Вы можете установить этот флаг, если хотите, чтобы на вкладках Auto-Hide отображались только значки
вместо иконок и заголовков док-виджетов. Если флаг установлен, то вкладка Auto-Hide
займет меньше места. При этом во всплывающей подсказке каждой вкладки по-прежнему отображается заголовок док-виджета.

![AutoHideSideBarsIconOnly true](cfg_flag_AutoHideSideBarsIconOnly_true.png)

### `AutoHideShowOnMouseOver`

Обычно виджеты Auto-Hide отображаются при щелчке на вкладке Auto-Hide и скрываются при повторном щелчке на вкладке Auto-Hide или при щелчке на другом месте.
скрываются при повторном щелчке на вкладке Auto-Hide или при щелчке на любом другом
док-виджет в том же контейнере. Если этот флаг установлен, то виджет Auto-Hide
будет показан, если пользователь наведет курсор на вкладку Auto-Hide или переместит мышь за пределы виджета Auto-Hide.
мышь за пределы виджета Auto-Hide. Показ и скрытие по щелчку мыши по-прежнему
работают, если эта функция включена.

### `AutoHideCloseButtonCollapsesDock`

Некоторые пользователи не понимают разницы между закрытием автоматически скрываемого дока и
сворачиванием автоскрывающегося дока. Это может привести к ситуации, когда пользователь нажимает кнопку
кнопку закрытия (при этом виджет боковой вкладки теряется) вместо того, чтобы просто щелкнуть мышью за пределами автоскрывающегося дока (сворачивание дока).
(сворачивание дока).

![AutoHideCloseButtonCollapsesDock false](cfg_flag_AutoHideCloseButtonCollapsesDock_false.gif)

Если активна опция `AutoHideCloseButtonCollapsesDock`, то кнопка закрытия в виджете автоскрытия сворачивает виджет автоскрытия вместо кнопки закрытия.
кнопка закрытия в виджете автоскрытия сворачивает виджет автоскрытия, а не закрывает его
закрытия.

![AutoHideCloseButtonCollapsesDock true](cfg_flag_AutoHideCloseButtonCollapsesDock_true.gif)

## Флаги возможностей(фишек) DockWidget

### `DockWidgetClosable`

Если значение установлено, то виджет док-станции будет иметь кнопку закрытия.

### `DockWidgetMovable`

Если виджет дока является подвижным, то он может быть перемещен в новую позицию в текущем контейнере дока.
текущем док-контейнере. Отключите этот флаг, чтобы предотвратить перемещение док-виджета
с помощью мыши.

### `DockWidgetFloatable`

Если значение установлено, то виджет док-станции можно перетащить в плавающее окно.

### `DockWidgetDeleteOnClose`

Удаляет виджет дока и его содержимое после его закрытия.

### `CustomCloseHandling`

При нажатии на кнопку закрытия виджет дока не закрывается, а вместо этого выдается сигнал
`closeRequested()`. Это позволяет приложению реализовать
пользовательскую обработку закрытия.

### `DockWidgetFocusable`

Если эта опция включена, то виджет док-станции может получить подсветку фокуса.

### `DockWidgetForceCloseWithArea`

Виджет дока будет закрыт, когда будет закрыта область дока, размещающая его. Если для виджета дока включена функция
функция `DockWidgetDeleteOnClose` включена для док-виджета, то он будет удален, если пользователь нажмет кнопку закрытия этого док-виджета.
будет удален, если пользователь нажмет на кнопку закрытия этого док-виджета. Если
пользователь нажимает кнопку закрытия док-области, содержащей этот виджет,
то переключается только видимость док-виджета. Если флаг этой функции
установлен, то при закрытии док-области закрывается и док-виджет. Это означает, что если
для виджетов док-станции установлена функция `DockWidgetDeleteOnClose`, то все виджеты док-станции
в док-области, то при закрытии док-области все док-виджеты будут удалены.

### `NoTab`

При установке этого флага вкладка виджета дока никогда не будет показана.

### `DeleteContentOnClose`

Удаляет только содержащийся виджет при закрытии, сохраняя виджет дока нетронутым и на месте
на своем месте. Пытается перестроить виджет содержимого при показе, если имеется фабрика виджетов
factory set. Подробнее см. в [issue #365](https://github.com/githubuser0xFFFF/Qt-Advanced-Docking-System/pull/365).

## Central Widget

Система Advanced Docking System была разработана для преодоления ограничений
родной системы докинга Qt с ее концепцией центрального виджета. Именно по этой причине
причиной того, что до версии 3.6 в библиотеке отсутствовала поддержка такой вещи, как центральный виджет.
как центральный виджет. Благодаря вкладу одного из пользователей библиотека
теперь поддерживает центральный виджет.

В системе Advanced Docking System центральный виджет - это виджет стыковки, который не является ни закрываемым, ни перемещаемым, ни плавающим.
ни закрываемым, ни перемещаемым, ни плавающим. Центральный виджет не имеет строки заголовка
и поэтому пользователь не может скрыть, закрыть или перетащить центральный виджет.
виджет. Если есть центральный виджет, то и распределение размеров
для виджетов док-станции вокруг центрального виджета:

- **без центрального виджета (по умолчанию)** - при изменении размера доступное пространство распределяется
распределяется между всеми виджетами док-станции - размеры всех виджетов док-станции
уменьшается или увеличивается
- **с центральным виджетом** - при изменении размера изменяется размер только центрального виджета - виджеты дока вокруг центрального виджета уменьшаются или увеличиваются.
док-виджеты вокруг центрального виджета сохраняют свои размеры (см. анимацию ниже)

![Центральный виджет](central_widget.gif)

Чтобы установить центральный виджет, достаточно передать центральный виджет дока
в функцию докменеджера `setCentralWidget`:

```c++
auto* CentralDockArea = DockManager->setCentralWidget(CentralDockWidget);
```

Как это работает, смотрите в примере `centralwidget`.

> ##### Примечание
> Центральный виджет должен быть первым виджетом дока, который добавляется в
> менеджера доков. Функция не работает и возвращает `nullptr`, если
> уже зарегистрированы другие док-виджеты. Поэтому `setCentralWidget` должна быть
> первой функцией, вызываемой при добавлении док-виджетов.

## Empty Dock Area

В некоторых приложениях требуется фиксированная DockArea, которая всегда видна, даже если она не содержит никаких DockWidgets.
не содержит никаких DockWidgets. Т.е. DockArea в этом случае является своего рода
центрального виджета, который всегда виден (см.
[issue](https://github.com/githubuser0xFFFF/Qt-Advanced-Docking-System/issues/199)).

Начиная с версии 3.7.1 расширенная система докинга поддерживает эту возможность. На сайте
Пример `emptydockarea` показывает, как это может быть реализовано с помощью библиотеки. Вам
достаточно создать док-виджет и установить флаг свойства `CDockWidget::NoTab`.
Это навсегда скрывает виджет вкладки данной области и удаляет его из меню вкладки
меню. Для этого специального док-виджета необходимо также отключить все остальные функции
(подвижные, закрываемые и плавающие), чтобы предотвратить закрытие и перемещение этого виджета.
Если использовать функцию `CDockManager::setCentralWidget`, как в примере
код ниже, то отключать эти возможности не нужно, так как это делается в функции `setCentralWidget
в функции `setCentralWidget`.

```c++
QLabel* label = new QLabel();
label->setText("This is a DockArea which is always visible, even if it does not contain any DockWidgets.");
label->setAlignment(Qt::AlignCenter);
CDockWidget* CentralDockWidget = new CDockWidget("CentralWidget");
CentralDockWidget->setWidget(label);
CentralDockWidget->setFeature(ads::CDockWidget::NoTab, true);// set the flag before adding the widget to dock manager
auto* CentralDockArea = DockManager->setCentralWidget(CentralDockWidget);
```

## Пользовательское открытие/скрытие виджетов

Обычно при нажатии на кнопку закрытия виджета док-станции он просто скрывается, и пользователь может снова показать его с помощью действия `toggleView()` виджета док-станции. Это предназначено для пользовательских интерфейсов со статическим количеством виджетов. Однако усовершенствованная система докинга поддерживает и динамические док-виджеты, которые будут удаляться при закрытии. Если для определенного док-виджета установить флаг `DockWidgetDeleteOnClose`, то при закрытии этого док-виджета он будет удален. Это позволяет реализовать пользовательские интерфейсы с динамически создаваемыми редакторами, например, в текстовых редакторах или средствах разработки исходного кода.

При закрытии всей области по умолчанию происходит скрытие содержащихся в ней док-виджетов независимо от флага `DockWidgetDeleteOnClose`, за исключением случаев, когда имеется только один док-виджет. В этом особом случае флаг `DockWidgetDeleteOnClose` выполняется. Такое поведение можно изменить, установив флаг `DockWidgetForceCloseWithArea` для всех виджетов дока, которые необходимо закрыть вместе с их областью.

## Стайлинг

Advanced Docking System поддерживает стилизацию с помощью [Qt Style Sheets](https://doc.qt.io/qt-5/stylesheet.html). Все компоненты, такие как сплиттеры, вкладки, кнопки, панели заголовков и
иконки, могут быть стилизованы таким образом.

### Отключение внутренней таблицы стилей

Менеджер доков использует внутреннюю таблицу стилей для стилизации своих компонентов. Это
это означает, что стиль, который вы видите в демонстрационном приложении, формируется из
внутренних таблиц стилей, которые находятся в папке `src/stylesheets. Если вы захотите
отключить эту внутреннюю таблицу стилей, поскольку ваше приложение использует свою собственную,
просто вызовите функцию настройки таблицы стилей с пустой строкой.

```c++
DockManager->setStyleSheet("");
```

