"""Welcome to Reflex!."""

# Import all the pages.
from farm_reflex.pages import *

import reflex as rx


class State(rx.State):
    """Define empty state to allow access to rx.State.router."""


# Create the app.
app = rx.App()
