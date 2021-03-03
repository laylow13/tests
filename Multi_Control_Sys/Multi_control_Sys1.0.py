#!/usr/bin/env python3

import asyncio

from mavsdk import System

from mavsdk.mission import (MissionItem, MissionPlan)

import GeoFence


async def run():

    #drone1 = System(mavsdk_server_address="localhost", port=50040)
    drone1 = System()

    await drone1.connect(system_address="udp://:14540")

    print("Waiting for drone to connect...")
    async for state in drone1.core.connection_state():
        if state.is_connected:
            print(f"Drone1 discovered with UUID: {state.uuid}")
            break

    print("Waiting for drone to have a global position estimate...")
    async for health in drone1.telemetry.health():
        if health.is_global_position_ok:
            print("Global position estimate ok")
            break
    
    GeoFence.Create_GeoFence(drone1)

    # Fetch the home location coordinates, in order to set a boundary around the home location
    print("Fetching home location coordinates...")
    async for terrain_info in drone1.telemetry.home():
        home_lat = terrain_info.latitude_deg
        home_lon = terrain_info.longitude_deg
        home_abs_alt=terrain_info.absolute_altitude_m
        break

    await drone1.action.set_takeoff_altitude(0.5)

    await drone1.action.set_return_to_launch_altitude(0.5)

    print("-- Taking off")
    await drone1.action.takeoff()

    
    print('--flying to the specified position')
    await drone1.action.goto_location(home_lat,home_lon,home_abs_alt+0.7,0)

    pre_mode= None
    async for flight_mode in drone9.telemetry.flight_mode():
        if pre_mode != flight_mode:
            print('Current flightmode: ',flight_mode)
            pre_mode=flight_mode
        if flight_mode is flight_mode.HOLD:
            print('sleep for     seconds')
            await asyncio.sleep(40)
            break

    print("-- Returning to launch")
    await drone1.action.return_to_launch()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
