from nicegui import ui
from components.navbar import show_navbar


@ui.page("/signin")
def show_signin_page():
    with ui.grid(columns=2).classes(
        "w-full h-screen items-center justify-center h-screen rounded-xl"
    ):
        # Form
        with ui.column().classes(
            " w-full h-screen items-center justify-center justify-start space-y-6"
        ):
            with ui.row().classes(""):
                ui.label("Event").classes(" text-xl font-bold ")
                ui.label("Hive").classes("text-purple-700 font-bold text-xl  ")
            ui.label("Sign In To Event Hive").classes("font-bold text-2xl ")

            with ui.column().classes("w-full "):
                ui.label("YOUR EMAIL")
                ui.input("").props("outlined type=password").classes(
                    "w-full  font-bold"
                )
                ui.label("PASSWORD")
                ui.input("").props("outlined type=password").classes("w-full font-bold")

            ui.button("Sign In")
            ui.label("Or")
            ui.button("Sign up with Google").classes("bg-white text-black")
        # Image with text
        with ui.column().classes(
            "bg-[url(/assets/signin.jpg)] w-full h-screen bg-cover flex flex-col items-center justify-center h-screen rounded-r"
        ):
            ui.html("<h2>Hello Friend</h2>").classes("text-white text-2xl")
            ui.label(
                "To keep connected with us provide us with your information"
            ).classes("text-white text-xl")
            ui.button("Signin").classes("capitalize")
