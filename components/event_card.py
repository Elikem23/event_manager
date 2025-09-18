from nicegui import ui


def show_event_card(event):
     with ui.card().on(
          type=
          "click",
          handler=lambda: ui.navigate.to(f"/events?id={event["id"]}")):
        # ui.label(text=event["title"])
         ui.image(source=event["image"]).classes("rounded-lg h-[300px]")
         ui.label(text=event["title"])
         ui.label(text=event["start_date"])
         ui.label(text=event["venue"])