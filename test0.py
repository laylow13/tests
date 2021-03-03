#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio

from mavsdk import System

from mavsdk.mission import (MissionItem, MissionPlan)

from mavsdk.geofence import Point, Polygon

# 米转换为经纬度常量
lon_const = 0.00001141
lat_const = 0.00000899


async def run():
    # drone = System("localhost", 50040)
    drones = [System(mavsdk_server_address='localhost', port=i) for i in range(50040, 50042, 1)]

    for i in range(0, 2):
        await drones[i].connect(system_address=f"udp://:{14540 + i}")

    home_lat = []
    home_lon = []
    home_abs_alt = []
    # home = [home_lat, home_lon, home_abs_alt]
    # des1 = [des_lat, des_lon, des_abs_alt]

    print("Waiting for drones to connect...")
    for i in range(0, 2):
        async for state in drones[i].core.connection_state():
            if state.is_connected:
                print(f"Drone[{i}] discovered with UUID: {state.uuid}")
                break

        print(f"Waiting for drone[{i}] to have a global position estimate...")
        async for health in drones[i].telemetry.health():
            if health.is_global_position_ok:
                print(f"Drone[{i}] Global position estimate ok")
                break

        print("Fetching home location coordinates...")
        async for terrain_info in drones[i].telemetry.home():
            home_lat.append(terrain_info.latitude_deg)
            home_lon.append(terrain_info.longitude_deg)
            home_abs_alt.append(terrain_info.absolute_altitude_m)
            print(f'drone[{i}] home location coordinates is ok',home_lat[i],home_lon[i],home_abs_alt[i])
            break

    print("-- Arming --")
    for i in range(0, 2):
        await drones[i].action.arm()
        print(f'{4 - i} drones is left')

    await asyncio.sleep(10)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
