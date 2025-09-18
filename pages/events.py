from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer
from components.event_card import show_event_card
import requests
from utils.api import base_url


@ui.page("/events")
def show_events_page():
    show_navbar()
    event_id = ui.context.client.request.query_params.get("id")
    response = requests.get(f"{base_url}/events/{event_id}")
    if response.status_code ==200:
        json_data = response.json()
        event = json_data["data"]
        with ui.column().classes(f"bg-[url({event["image"]})] w-full h-screen bg-center bg-cover flex gap-20 "):
            with ui.row().classes('flex flex-col p-30 ml-30 w-full h-full bg-black/30 gap-30 justify-betweeen '):

                with ui.column().classes('ml-20 mt-60'):
                    ui.label(text=event["title"]).classes("text-6xl text-white text-bold ")
                    ui.label('IIIT Sonepat').classes('text-white text-bold text-2xl')

                    ui.label(text=event["description"]).classes("text-white")
                    ui.label('at 5 PM. The workshop taught participants the magic of creating stunning 3D models and ').classes("text-white")
                    ui.label("animations using Blender. It was suitable for both beginners and experienced users.").classes("text-white")
                    ui.label("The event was followed by a blender-render competition, which added to the excitement.").classes("text-white")

                with ui.card().classes("w-[300px] h-[300px] mx-auto p-6 bg-white shadow-xl mt-10 items-center  mt-60"):
                    ui.label('Date & Time').classes('text-blue text-bold text-2xl')
                    ui.label('sunday 16th November 9:30pm').classes("text-gray-600")
                    ui.label('Add to calender').classes("text-gray-600")
                    ui.button("Book Now").classes('bg-black')
                    ui.button('Programe Prompter').classes('bg-black')
                    ui.label('No Refund').classes("text-gray-600")

        with ui.grid(columns=2).classes("gap-20"):
            with ui.column().classes('ml-10 mt-10'):
                ui.label('Description').classes('text-bold text-2xl')
                ui.label('DesignHub organized a 3D Modeling Workshop using Blender on 16th February at 5 PM. The workshop taught participants the magic of creating stunning 3D models and animations using Blender.').classes('text-gray-600')
                ui.label('It was suitable for both beginners and experienced users. The event was followed by a blender-render competition, which added to the excitement.').classes('text-gray-600')
                ui.label('DesignHub organized a 3D Modeling Workshop using Blender on 16th February at 5 PM. The workshop taught participants the magic of creating stunning 3D models and animations using Blender. ').classes('text-gray-600')
                ui.label('It was suitable for both beginners and experienced users. The event was followed by a blender-render competition, which added to the excitement.').classes('text-gray-600')
                ui.label("Hours").classes("text-bold text-2xl")
                with ui.row():
                    ui.label("Weekdays hour:").classes('text-gray-600')
                    ui.label("7pm-10pm").classes('text-blue text-bold')
                with ui.row():    
                    ui.label("Sunday hour:").classes('text-gray-600')
                    ui.label("7pm-10pm").classes('text-blue text-bold')
                ui.label("Organizer Contact").classes("text-bold text-2xl") 
                ui.label("Please go to www.sneakypeeks.com and refer the FAQ section for more detail").classes('text-gray-600')

            with ui.column().classes("mt-10 mr-10"):
                ui.label("Event Location").classes('text-bold text-2xl') 
                with ui.card().classes("w-[400px] h-[300px] mx-auto p-6 bg-white shadow-xl item-center "): 
                    ui.image('assets/event3.jpg').classes("w-[300px] h-[350px]")

                    ui.label("Dream World Wide in Jakata").classes("text-bold text-2xl")
                    ui.label("Dummy location generation model by RSU ... Our approach generates more realistic dummy locations ").classes('text-gray-600')


        with ui.grid(columns=3).classes("w-full mt-20 gap-6"):
            for i in range(6):
                with ui.card().classes("w-[400px] h-[400px]"):
                    ui.image("assets/event.jpg").classes("rounded")

                    ui.label("Bestseller Book Bootcamp-write, Market & Publish your books-Lucknow").classes('text-bold text-2xl')
                    ui.label("Sunday 16 November").classes("text-blue")
                ui.label("online-event: join anywhere").classes('text-gray-700')
    elif response.status_code == 422:
        ui.label(text="Something went wrong")            
         
    show_footer()