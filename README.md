# Steps to Translate the Project

## The **`create_translation.py`** script
### Googletrans library
The command below installs the `googletrans` python library used for the translation.
> pip install googletrans==4.0.0-rc.1

### Generating the .ts files
The command below looks through the source files `gpPREGUNTAS.py` and `gpPREGUNTAS_ui.py`, and gets all the texts passed to the `translate()` function and add them all in to an `en.ts` files.
> pylupdate5 gpPREGUNTAS.py gpPREGUNTAS_ui.py -ts en.ts

### qt5-tools library
The command below installs the `qt5-tools` library which is needed to create the `.qm` files that is loaded into the `QTranslator` instance.
> pip install qt5-tools

### main function
In the `main()` function of the `create_translation.py` file, the function does the following operations:
- runs the `pylupdate5 gpPREGUNTAS.py gpPREGUNTAS_ui.py -ts en.ts` command above to generate an `en.ts` file.
- generates the translation of the `en.ts` file using the `googletrans.Translator` object and saves the translation in the corresponding files:
    - english.ts
    - spanish.ts
    - catalan.ts
    - galician.ts
- then, the `qt5-tools lrelease ` command is ran, this compiles and generates the following files:
    - english.qm
    - spanish.qm
    - catalan.qm
    - galician.qm

        these files are then used in the `self.trans.load()` method.

        the above files can be added to the resource `.qrc` file to generate a `_rc.py` resource file e.g ``
- the following lines are added to the `gpICONOS.qrc` file:
    ```xml
    <qresource prefix="qms">
        <file alias="catalan">qms/catalan.qm</file>
        <file alias="english">qms/english.qm</file>
        <file alias="galician">qms/galician.qm</file>
        <file alias="spanish">qms/spanish.qm</file>
    </qresource>
    ```
- the `pyrcc5 gpICONOS.qrc -o gpICONOS_rc.py` command is then ran to generate the `gpICONOS_rc.py` PyQt resource file to be imported.

## Use in the **`gpPREGUNTAS.py`** file.

The `languages_qm` dict object is to keep track of the name used to store the translated `.qm` files in the `gpICONOS_rc.py` file.
```py
languages_qm = {
    "es Español": "spanish",
    "ca Catalá": "catalan",
    "gl Galego": "galician",
    "en English": "english",
}
```
The implemeted classes all have a method `retranslateUI()`
```py
class RichTextEditor(QtWidgets.QDialog):
    ...
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    ...
class Login(QtWidgets.QWidget):
    ...
class MainWindowWithLogin(QtWidgets.QMainWindow):
    ...
```
### Changing language

The `for loop` and the `on_language_chosen` method below are both implemented in the `MainWindow` and the `Login` classes.
<br>
<br>
The instance of `QtWidgets.QComboBox()` is stored in the `self.cboxLang` instance variable by:
```py
self.cboxLang = QtWidgets.QComboBox()
```
The code block below loops through the `languages_qm` dict and sets the values as `ItemData` in the `self.cboxLang` instance variable.
<br>
When an item is selected in the QCombobox, a `currentIndexChanged` even is trigger and the `on_language_chosen` method or slot is called.

```py
# language
for index, language in enumerate(languages_qm.values()):
    self.cboxLang.setItemData(index, language)
self.cboxLang.currentIndexChanged.connect(self.on_language_chosen)

```
In the `on_language_chosen`, the current itemData of the `QCombobox`vis passed to the `change_func` method of the `MainWindowWithLogin` class.
```py
def on_language_chosen(self, index: int):
    self.window().change_func(self.cboxLang.itemData(index))
```

In the `MainWindowWithLogin` class:
- `change_func` method is implemented, the method loads the language from the Qt resource and installs it using the `QtWidgets.QApplication.instance().installTranslator()`
- `changeEvent` method is overriden to check for a particular event which is `QtCore.QEvent.LanguageChange`, on that event the `retranslateUI` method of the `MainWindowWithLogin` class is called, which in turn calls the `retranslateUI` of both the `Login` and the `MainWindow` classes.

```py
class MainWindowWithLogin(QtWidgets.QMainWindow):
    ...
    ...

    def change_func(self, language: str):
        if self.trans.load(f":/qms/{language}"):
            QtWidgets.QApplication.instance().installTranslator(self.trans)

    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.LanguageChange:
            self.retranslateUi()
        super().changeEvent(event)

    def retranslateUi(self):
        self.login.retranslateUi()
        self.mainWindow.retranslateUi(self.mainWindow)

```
