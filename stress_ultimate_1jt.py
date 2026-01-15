import asyncio
import aiohttp
import time

URL = "http://localhost:8080/api/v1/task" # Sesuaikan endpoint NeoEngine Anda
TOTAL_LOAD = 1000000
CONCURRENCY = 1000 # Jumlah request per detik agar tidak instan diblokir OS

async def send_task(session, i):
    payload = {
        "agent": "TaskAgent",
        "command": "STRESS_TEST",
        "data": {"id": i, "content": "Simulation Sovereign Load"}
    }
    try:
        async with session.post(URL, json=payload) as resp:
            return resp.status
    except:
        return 500

async def main():
    print(f"🚀 STARTING SOVEREIGN STRESS TEST: {TOTAL_LOAD} TASKS")
    start_time = time.time()
    
    connector = aiohttp.TCPConnector(limit=CONCURRENCY)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = []
        for i in range(TOTAL_LOAD):
            tasks.append(send_task(session, i))
            if len(tasks) >= CONCURRENCY:
                await asyncio.gather(*tasks)
                tasks = []
                if i % 10000 == 0:
                    print(f"📊 Processed: {i} / {TOTAL_LOAD}")

    end_time = time.time()
    print(f"✅ STRESS TEST COMPLETE in {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
