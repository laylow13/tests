#!/usr/bin/env python3

import asyncio
from mavsdk import System


async def run():

    Drone1 = System(mavsdk_server_address="localhost", port=50040)
    Drone2 = System(mavsdk_server_address="localhost", port=50041)
    await Drone1.connect(system_address="udp://:14540")
    print("Waiting for Drone1 to connect...")
    await Drone2.connect(system_address="udp://:14541")
    print("Waiting for Drone2 to connect...")
    async for state in Drone1.core.connection_state():
        if state.is_connected:
            print(f"Drone1 discovered with UUID: {state.uuid}")
            break
    async for state in Drone2.core.connection_state():
        if state.is_connected:
            print(f"Drone2 discovered with UUID: {state.uuid}")
            break

    print("Waiting for Drone1 to have a global position estimate...")
    print("Waiting for Drone2 to have a global position estimate...")
    async for health in Drone1.telemetry.health():
        if health.is_global_position_ok:
            print("1 Global position estimate ok")
            break
    async for health in Drone2.telemetry.health():
        if health.is_global_position_ok:
            print("2 Global position estimate ok")
            break

    print("-- Drone1 Arming")
    await Drone1.action.arm()
    print("-- Drone2 Arming")
    await Drone2.action.arm()

    print("--Drone1 Taking off")
    await Drone1.action.takeoff()
    print("--Drone2 Taking off")
    await Drone2.action.takeoff()

    await asyncio.sleep(10)

    print("--Drone1 Landing")
    await Drone1.action.land()
    print("--Drone2 Landing")
    await Drone2.action.land()
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
