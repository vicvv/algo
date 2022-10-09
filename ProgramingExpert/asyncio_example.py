import asyncio
import time


# Here we fake the download of a large file by sleeping 1 second.
async def download_large_file(file_name):
    await asyncio.sleep(1)
    print(f"{file_name} was downloaded successfully")
    return f"{file_name}: OK"


# These are the files to download. Since each file takes 1 second
# to download, it would take 5 seconds without using asyncio.
FILES_TO_DOWNLOAD = [
    "textures.zip",
    "models.zip",
    "physics_engine.exe",
    "game.exe",
    "achievements.exe",
]


async def main():
    start_time = time.time()
    downloads = [download_large_file(file_name) for file_name in FILES_TO_DOWNLOAD]
    download_statuses = await asyncio.gather(*downloads)
    total_time = time.time() - start_time
    print(f"Finished downloading {len(download_statuses)} files in {total_time} seconds!")


asyncio.run(main())