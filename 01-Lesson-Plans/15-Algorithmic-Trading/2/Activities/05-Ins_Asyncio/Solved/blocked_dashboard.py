import time
import panel as pn

pn.extension()


def fetch_data():
    """Simulate a delayed fetch."""
    time.sleep(5)


def serve_dashboard():
    dashboard = pn.Column("# My Blocked Dashboard")
    return dashboard.servable()


fetch_data()
serve_dashboard()
