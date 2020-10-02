import time

def fetch_data():
    """Simulate a delayed fetch."""
    print("Fetching data...")
    time.sleep(5)

def serve_plot():
    print("My Blocked Plot")

fetch_data()
serve_plot()
