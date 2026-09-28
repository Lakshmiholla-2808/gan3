import asyncio, time

async def fetch(name, delay):
    await asyncio.sleep(delay)
    return f"{name} done"

async def main():
    start = time.perf_counter()
    results = await asyncio.gather(*(fetch(f"svc{i}", 1) for i in range(5)))
    print(results, f"{time.perf_counter() - start:.1f}s")

asyncio.run(main())
