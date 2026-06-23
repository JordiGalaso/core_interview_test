import asyncio

async def search_items(query: str) -> list[str]:
    """Mock async data source with 500ms latency."""
    await asyncio.sleep(0.5)
    data = ["apple", "banana", "grape", "orange", "pineapple"]
    return [item for item in data if query.lower() in item]
