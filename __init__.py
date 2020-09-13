# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo
# import all of the Qt GUI library
from aqt.qt import *


# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.


def add_note():
    did = mw.col.decks.id_for_name("test")
    mid = mw.col.models.id_for_name("cc Chinese")
    showInfo("deck id for the deck test: {}. Model id for cc Chinese: {}".format(did, mid))


def show_card_count():
    # get the number of cards in the current collection, which is stored in
    # the main window
    card_count = mw.col.cardCount()
    # show a message box
    showInfo("Card count: %d" % card_count)


# create a new menu item, "test"
action = QAction("test", mw)
# set it to call testFunction when it's clicked
action.triggered.connect(add_note)
# and add it to the tools menu
mw.form.menuTools.addAction(action)
