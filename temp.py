import random
import sys
import asyncio

loop = asyncio.get_event_loop()

def _generate_temp(min:float, max:float, days:int):
    if days == 0:
        return "days cannot use 0"
    
    if days == 1:
        return round(random.uniform(min, max), 2)
    else:
        return [round(random.uniform(min, max), 2) for i in range(days)]

def get_temp():
    args = sys.argv
    return _generate_temp(args[0], args[1], args[3])

if __name__ == "__main__":
    loop.run_until_complete(get_temp())
