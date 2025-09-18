from nicegui import ui
from components.navbar import show_navbar
import requests
from utils.api import base_url

_event_image = None

def _handle_image_upload(event):
    global _event_image
    _event_image = event.content

def _post_event(data, files):
    response = requests.post(f"{base_url}/events", data=data, files=files)
    print(response.status_code, response.content)
    if response.status_code == 200:
        ui.notify(
            message="Event added succesfully!",
            type="positive")
        return ui.navigate.to("/")
    elif response.status_code == 422:
        return ui.notify(
            message="Please ensure all inputs are filled!",
            type="warning")
    
    
        

@ui.page("/create_event")
def show_create_event_page():
    show_navbar()
    with ui.element("div").classes("w-full h-full items-center flex flex-col bg-slate-100"):
        # "Create Event" section
        ui.label("Create Event").classes("font-bold text-3xl mb-4 mt-10") # Reduced top margin
        with ui.card().classes("font-bold shadow-xl w-3/5"):
            ui.label("Event Title").classes("text-slate-500 font-normal text-sm")
            event_title =  ui.input(placeholder="Enter your title").props("outlined").classes("w-full")
            ui.label("Event Venue").classes("text-slate-500 font-normal text-sm")
            event_venue = ui.input(placeholder="Enter your venue").props("outlined").classes("w-full")
            
            # Start and End Time section with time inputs
            with ui.row().classes("w-full justify-between gap-4"):
                with ui.element('div').classes("flex flex-col grow"):
                    ui.label("Start time").classes("text-slate-500 font-normal text-sm")
                    event_start_time = ui.input().props("outlined type=time").classes("w-full")
                with ui.element('div').classes("flex flex-col grow"):
                    ui.label("End time").classes("text-slate-500 font-normal text-sm")
                    event_end_time = ui.input().props("outlined type=time").classes("w-full")

            # Start and End Date section with date inputs
            with ui.row().classes("w-full justify-between gap-4"):
                with ui.element('div').classes("flex flex-col grow"):
                    ui.label("Start date").classes("text-slate-500 font-normal text-sm")
                    event_start_date = ui.input().props("outlined type=date").classes("w-full")
                with ui.element('div').classes("flex flex-col grow"):
                    ui.label("End date").classes("text-slate-500 font-normal text-sm")
                    event_end_date = ui.input().props("outlined type=date").classes("w-full")
       
              
        with ui.element("div").classes("w-full items-center flex flex-col bg-slate-100 mt-10"): 
        # Added a positive margin for separation
        # "Event Description" section
             ui.label("Event Description").classes("font-bold text-3xl mb-4")
        with ui.card().classes("font-bold shadow-xl mb-8 w-3/5"):
            ui.label("Event Image").classes("text-slate-500 font-normal text-sm")
            # Image upload component
            ui.upload(label="Click or drop an image to upload",auto_upload=True, on_upload=_handle_image_upload).classes("w-full h-48 bg-slate-200 rounded")
            ui.label("Event Description").classes("text-slate-500 font-normal text-sm mt-4")
            event_description = ui.input(placeholder="Type here...").props("outlined type=textarea").classes("w-full h-32")

        ui.button("Create Event", on_click=lambda: _post_event(
            data={"title": event_title.value,
                 "venue": event_venue.value,
                 "start_time": event_start_time.value,
                 "end_time": event_end_time.value,
                 "start_date": event_start_date.value,
                 "end_date": event_end_date.value,
                 "description": event_description.value},
            files={"image": _event_image}     
        )).classes("w-3/5 h-12 mb-20 bg-purple-700 hover:bg-purple-800")
    