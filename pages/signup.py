from nicegui import ui, Tailwind
from components.navbar import show_navbar


@ui.page("/signup")
def show_signup_page():

    with ui.grid(columns=2).classes(
        "w-full h-screen items-center justify-center rounded-lg"
    ):
        # Image with text
        with ui.column().classes(
            "bg-[url(/assets/signup.jpg)] w-full h-screen bg-cover flex flex-col items-center justify-center h-screen rounded-l"
        ):
            ui.html("<h2>Welcome Back</h2>").classes("text-white text-2xl")
            ui.label(
                "To keep connected with us provide us with your information"
            ).classes("text-white text-xl")
            ui.button("Signin").classes("capitalize")
            # form
        with ui.column().classes(
            " w-full h-screen items-center justify-center justify-start"
        ):
            with ui.row():
                ui.label("Event").classes(" text-xl font-bold  ")
                ui.label("Hive").classes("text-purple-700 font-bold text-xl  ")
            ui.label("Sign up to event hive").classes("capitalize font-bold text-2xl ")

            with ui.column().classes("w-full "):
                ui.label("FIRST NAME")
                ui.input("").props("outlined ").classes("w-full")
                ui.label("SURNAME")
                ui.input("").props("outlined ").classes(
                    "w-full  font-bold border-transparent"
                )
                ui.label("PASSWORD")
                ui.input("").props("outlined type=password").classes(
                    "w-full  font-bold"
                )
                ui.label("CONFIRM PASSWORD")
                ui.input("").props("outlined type=password").classes("w-full font-bold")

            ui.button("Sign Up")
            ui.label("Or")
            ui.button("Sign up with Google").classes("bg-white text-black")
