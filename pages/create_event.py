from nicegui import ui
from components.navbar import show_navbar


@ui.page("/create_event")
def show_create_event_page():
    show_navbar()
    with ui.element("div").classes("w-full h-screen  items-center justify-center flex flex-col"):
        ui.label("Create Event").classes("font-bold text-3xl")
        with ui.card().classes("w-3/4 max-w-3xl p-8 space-y-4"):
            ui.label('Event Title')
            ui.input(placeholder='Enter event title').classes("w-full text-lg p-3")
            ui.label("Enter Event Venue")
            ui.input(placeholder="Enter Venue")
         #time
            with ui.row().classes('flex flex-row justify-around w-full'):
                with ui.input("Start Time").props("outlined") as time_input:
                    with time_input.add_slot('append'):
                      ui.icon("schedule").on('click',lambda: menu.open()).classes('cursor-pointer')
                    with ui.menu() as menu:
                        ui.time().bind_value(time_input)

                with ui.input('End Time').props('outlined') as time_input:
                    with time_input.add_slot("append"):
                      ui.icon("schedule").on('click', lambda: menu.open()).classes('cursor-pointer')
                    with ui.menu() as menu: 
                         ui.time().bind_value(time_input)
            #date
            with ui.row().classes('flex flex-row justify-around w-full'):
                with ui.input("Start Date").props("outlined") as date:
                    with date.add_slot('append'):
                      ui.icon("schedule").on('click',lambda: menu.open()).classes('cursor-pointer')
                    with ui.menu() as menu:
                        ui.date().bind_value(date)
                with ui.input("End Date").props("outlined") as date:
                    with date.add_slot('append'):
                      ui.icon("schedule").on('click',lambda: menu.open()).classes('cursor-pointer')
                    with ui.menu() as menu:
                        ui.date().bind_value(date)
       
              
        #event description        
    with ui.element('div').classes("w-full h-full  items-center justify-center flex flex-col"):
        ui.label("Event Description").classes("font-bold text-3xl")    
        with ui.card().classes("w-3/4 max-w-3xl p-8 space-y-4"):
            ui.label("Event Image")     
            ui.upload(label="Upload image").classes("w-full") 
            ui.label("Event description")
            ui.input(placeholder="type here")
        ui.button("Create Event").classes("bg-violet w-1/2")    