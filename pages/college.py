from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer


@ui.page("/college_page")
def show_college_page():
    show_navbar()
    ui.label("This is the college page")

    show_footer()
