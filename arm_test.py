#!/usr/bin/env python3

import asyncio

from mavsdk import System

from mavsdk.mission import (MissionItem, MissionPlan)

from mavsdk.geofence import Point, Polygon


async def run():

    #drone = System(mavsdk_server_address="localhost", port=50043)
    drone = System()
    await drone.connect(system_address="udp://:14544")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"Drone discovered with UUID: {state.uuid}")
            break

    print("Waiting for drone to have a global position estimate...")
    async for health in drone.telemetry.health():
        if health.is_global_position_ok:
            print("Global position estimate ok")
            break

    print("Fetching home location coordinates...")
    async for terrain_info in drone.telemetry.home():
        home_lat = terrain_info.latitude_deg
        home_lon = terrain_info.longitude_deg
        home_abs_alt=terrain_info.absolute_altitude_m
        print(home_lat,home_lon,home_abs_alt)
        break

    print("-- Arming")
    await drone.action.arm()
    await asyncio.sleep(8)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
