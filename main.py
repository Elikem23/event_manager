from nicegui import ui, app
import os
from pages.home import *
from pages.signin import *
from pages.signup import *
from pages.events import *
from pages.college import *
from pages.create_event import *
from pages.not_found import *


app.add_static_files("/assets", "assets")


ui.run()
