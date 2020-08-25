import asyncio
import panel as pn

pn.extension()


async def fetch_data():
    """Simulate a delayed fetch."""
    asyncio.sleep(5)


def serve_dashboard():
    dashboard = pn.Column("# My Async Dashboard")
    return dashboard.servable()


loop = asyncio.get_event_loop()

task = loop.create_task(fetch_data())
serve_dashboard()
