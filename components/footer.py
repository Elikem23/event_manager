from nicegui import ui


def show_footer():
    with ui.element().classes("w-full bg-[#03045e] items-center flex flex-col rounded-b justify-between"):
        with ui.row().classes("font-bold text-3xl"):
            ui.label("Event").classes("text-white")
            ui.label("Hive").classes("text-purple")
        with ui.row().classes("flex flex-row justify-center items-center"):
            ui.input(placeholder="enter your mail").classes("rounded text-sm bg-white w-[300px]").props("outlined dense flat") 
            ui.button("Subscribe") 
        with ui.row().classes("text-white flex"):
            ui.label("Home")
            ui.label("About")
            ui.label("Services")
            ui.label("Get In Touch")  
            ui.label("FAQs")

        ui.html("<hr>").classes("my-4  w-2/3")
        

         

