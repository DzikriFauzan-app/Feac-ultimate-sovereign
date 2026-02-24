import asyncio
import aiohttp
import time

# Alamat jembatan Neo Engine kamu
URL = "https://76de158318ec3378-182-2-178-71.serveousercontent.com/"

async def send_request(session, req_id):
    try:
        # Kita kirim dummy data simulasi beban game
        async with session.get(URL, timeout=5) as response:
            return response.status
    except Exception:
        return None

async def main():
    total_requests = 5000000
    concurrency = 500  # Jumlah tembakan serentak
    print(f"🔥 STRESS TEST DIMULAI: 5 Juta Request ke Neo Engine...")
    print(f"🔗 Target: {URL}")
    
    start_time = time.time()
    success_count = 0
    fail_count = 0
    
    async with aiohttp.ClientSession() as session:
        for i in range(0, total_requests, concurrency):
            tasks = [send_request(session, j) for j in range(concurrency)]
            results = await asyncio.gather(*tasks)
            
            for res in results:
                if res == 200:
                    success_count += 1
                else:
                    fail_count += 1
            
            if i % 5000 == 0:
                elapsed = time.time() - start_time
                rps = i / elapsed if elapsed > 0 else 0
                print(f"📊 Progress: {i}/{total_requests} | Success: {success_count} | Fail: {fail_count} | Speed: {rps:.2f} req/s")

    print(f"🏁 TEST SELESAI dalam {time.time() - start_time:.2f} detik")

if __name__ == "__main__":
    asyncio.run(main())
