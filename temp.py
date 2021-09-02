import random
import asyncio

loop = asyncio.get_event_loop()

def _generate_temp(min:float=36.0, max:float=37.0, days:int=1):
    if days == 0:
        return "days cannot use 0"
    
    if days == 1:
        return round(random.uniform(min, max), 2)
    else:
        return [round(random.uniform(min, max), 2) for i in range(int(days))]

async def get_temp():
    return _generate_temp()

if __name__ == "__main__":
    loop.run_until_complete(get_temp())
