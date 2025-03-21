import asyncio
import threading
import time
import multiprocessing
import aiohttp


#
#
# async def say_hello():
#     print("Hello")
#     await asyncio.sleep(2)
#     print("World")
#
#
# async def main():
#     await say_hello()
#
#
# asyncio.run(main())
#
#
# def print_numbers():
#     for n in range(10):
#         time.sleep(1)
#         print(n)
#
#
# def print_letters():
#     for l in "abcdefgh":
#         time.sleep(1)
#         print(l)
#
#
# # Створюємо потік
# thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_letters)
# # Запускаємо потік
# thread1.start()
# thread2.start()
# # Чекаємо завершення потоку
# thread1.join()
# thread2.join()
#
# print("Потік завершено")
#
#
# def print_numbers2():
#     for n in range(10):
#         print(n)
#
#
# process = multiprocessing.Process(target=print_numbers2)
# process.start()
# process.join()
# print("Процес завершено")
#
#
# def factorial(n):
#     factorial_n = 1
#     for i in range(1, n + 1):
#         factorial_n *= i
#     return factorial_n
#
#
# def process_factorial(n):
#     print(f"Факторіал {n}: {factorial(n)}")
#
#
# if __name__ == "__main__":
#     numbers = [5, 7, 10]
#     processes = []
#
#     for n in numbers:
#         p = multiprocessing.Process(target=process_factorial, args=(n,))
#         processes.append(p)
#         p.start()
#
#     for p in processes:
#         p.join()
#
#     print("Усі процеси завершено!")

async def fetch_page(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    urls = ["https://www.example.com", "https://www.python.org", "https://www.github.com"]
    tasks = [fetch_page(url) for url in urls]
    pages = await asyncio.gather(*tasks)

    for page in pages:
        print(f"Page length: {len(page)}")

asyncio.run(main())

