from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer
from components.event_card import show_event_card
import requests
from utils.api import base_url



@ui.page("/")
def show_home_page():
    ui.query(".nicegui-content").classes("m-0 p-2 gap-0")
    show_navbar()
    with ui.element("section").classes(
        "w-full flex flex-row justify-center items-center"
    ):
        # hero page
        with ui.element("div").classes(
            " w-full h-[100%] flex justify-center h-screen items-center text-center bg-[url('/assets/hero.jpg')] bg-cover bg-center rounded-lg"
        ):
           # text
            with ui.element("div").classes(""):
                ui.label("MADE FOR THOSE").classes(
                    "text-white text-7xl font-bold text-center"
                )
                ui.label("WHO DO").classes("text-white text-7xl font-bold")
            # image
        with ui.element("div").classes("bg-[#03045e] w-4/5 mx-auto p-6 rounded-lg -mt-16"):
            
              with ui.row().classes("gap-6 justify-center"):
            # select button
                with ui.column():
                    ui.label("Looking for").classes("text-white text-sm font-medium")
                    ui.select(label="Choose event type",
                        options=["Party", "Concert", "Festival"],
                        value=None,
                    ).classes("bg-white text-black rounded-md w-72")

    
                with ui.column().classes("w-80"):
                    ui.label("Location").classes("text-white text-sm font-medium")
                    ui.select(label="choose location",
                        options=["Accra", "Kumasi", "Takoradi", "Tamale"],
                        value=None,
                    ).classes("bg-white text-black rounded-md w-72")

    
                with ui.column():
                    ui.label("When").classes("text-white text-sm font-medium")
                    ui.select(label="Choose date and time",
                        options=["Today", "This Week", "This Month"],
                        value=None,
                    ).classes("bg-white text-black rounded-md w-72")
         # second select button
        with ui.row().classes(
            "flex flex-row justify-between items-center bg-navy-blue w-full px-10 py-5 w-full "
        ):
            with ui.row().classes("text-3xl "):
                ui.label("Upcoming")
                ui.label("Events").classes("text-primary")
            with ui.row():
                weekdays = [
                    "Weekdays",
                    "Mondays",
                    "Tuesday",
                    "Wednesday",
                    "Thursday",
                    "Friday",
                    "Saturday",
                    "Sunday",
                ]
                ui.select(label="", value="Weekdays", options=weekdays)

                event_type = ["Event", "Party", "Concert", "Festival"]
                ui.select(label="", value="Event", options=event_type)

                category = ["Category", "Corporate", "Social", "charity", "Sports"]
                ui.select(label="", value="Category", options=category)
        # Upcoming events
        with ui.grid(columns=3).classes("w-full h-full rounded-lg p-4"):
            response = requests.get(f"{base_url}/events?limit=0")
            json_data = response.json()
            for event in json_data["data"]:
               show_event_card(event)

        with ui.row().classes("w-full justify-center"):
            ui.button("Load More").classes("bg-[#03045e] rounded")

        ui.separator().classes('h-10 bg-white')
        # brands
    with ui.column().classes("bg-[#03045e] h-[300px] w-full  mt-20 gap-10"):
        with ui.grid(columns=2).classes("w-full h-full"):
            with ui.column().classes("relative"):
                ui.image("assets/hero1.png").classes("w-[550px] absolute bottom-10")

            with ui.column().classes("w-full items-center justify-center items-end"
            ):
                ui.label("Make your own Event").classes(
                        "text-3xl font-bold text-white"
                    )
                ui.button("Create Events").classes("mt-2")
    ui.image("assets/Brand.png")
    
    with ui.element("div").classes("w-full"):
        with ui.row().classes("font-bold text-2xl"):
                ui.label("Trending")
                ui.label("Colleges").classes("text-purple")
        with ui.grid(columns=3).classes("w-4/5 items-stretch justify-center mb-20 w-full"):
            for i in range(3):
                with ui.card():
                    ui.image("assets/Havard.png").classes(" w-[20rem] h-[20rem] rounded w-full")
                    ui.label("Havard University")
                    ui.label("Cambrigde, Massachusetts")
        with ui.element("div").classes("flex text-center justify-center"): 
           ui.button("Load More")       
        # blogs
    with ui.element("div").classes("w-full"):
        with ui.row().classes("font-bold text-3xl"): 
            ui.label("Our")
            ui.label("Blogs").classes("text-purple") 
        with ui.grid(columns=3):
            for i in range(3):  
                with ui.card():
                     ui.image("assets/blog.jpg")  
                     ui.label("BestSeller Book bootcamp-write, market and publish ypur book")   
                 











    show_footer()
