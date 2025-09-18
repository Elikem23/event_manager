from nicegui import ui


def show_navbar():
    with ui.row():
        ui.link("home", "/")
        ui.link("Signup", "/signup")
        ui.link("Signin", "/signin")
        ui.link("create event", "/create_event")
        ui.link("college", "/college")
        ui.link("not found", "/not_found")
        
        
   # with ui.element("div").classes("font-bold w-full flex items-center justify-between px-6 py-4"):
    #    with ui.row().classes("text-lg items-center gap-2"):
    #        ui.label("Event")
    #        ui.label("Hive").classes("text-[#03045e] text-white px-2 py-1")
    #    with ui.row():
    #         ui.label("login")  
    #         ui.button("Signup")  