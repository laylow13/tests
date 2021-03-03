!/usr/bin/env python3

import asyncio

from mavsdk import System

from mavsdk.mission import (MissionItem, MissionPlan)

from mavsdk.geofence import Point, Polygon


async def run():

    #drone = System(mavsdk_server_address="localhost", port=50040)
    drone1 = System(mavsdk_server_address="localhost", port=50040)
    drone2 = System(mavsdk_server_address="localhost", port=50041)
    drone3 = System(mavsdk_server_address="localhost", port=50042)
    drone4 = System(mavsdk_server_address="localhost", port=50043)
    drone5 = System(mavsdk_server_address="localhost", port=50044)
    drone6 = System(mavsdk_server_address="localhost", port=50045)
    drone7 = System(mavsdk_server_address="localhost", port=50046)
    drone8 = System(mavsdk_server_address="localhost", port=50047)
    drone9 = System(mavsdk_server_address="localhost", port=50048)
    #drone10 = System(mavsdk_server_address="localhost", port=50049)
    #drone11 = System(mavsdk_server_address="localhost", port=50049)

    await drone1.connect(system_address="udp://:14540")
    await drone2.connect(system_address="udp://:14541")
    await drone3.connect(system_address="udp://:14542")
    await drone4.connect(system_address="udp://:14543")
    await drone5.connect(system_address="udp://:14544")
    await drone6.connect(system_address="udp://:14545")
    await drone7.connect(system_address="udp://:14546")
    await drone8.connect(system_address="udp://:14547")
    await drone9.connect(system_address="udp://:14548")
    #await drone10.connect(system_address="udp://:14549")
    #await drone11.connect(system_address="udp://:14549")


    print("Waiting for drone to connect...")
    async for state in drone1.core.connection_state():
        if state.is_connected:
            print(f"Drone1 discovered with UUID: {state.uuid}")
            break
    async for state in drone2.core.connection_state():
        if state.is_connected:
            print(f"Drone2 discovered with UUID: {state.uuid}")
            break
    async for state in drone3.core.connection_state():
        if state.is_connected:
            print(f"Drone3 discovered with UUID: {state.uuid}")
            break
    async for state in drone4.core.connection_state():
        if state.is_connected:
            print(f"Drone4 discovered with UUID: {state.uuid}")
            break
    async for state in drone5.core.connection_state():
        if state.is_connected:
            print(f"Drone5 discovered with UUID: {state.uuid}")
            break
    async for state in drone6.core.connection_state():
        if state.is_connected:
            print(f"Drone6 discovered with UUID: {state.uuid}")
            break
    async for state in drone7.core.connection_state():
        if state.is_connected:
            print(f"Drone7 discovered with UUID: {state.uuid}")
            break
    async for state in drone8.core.connection_state():
        if state.is_connected:
            print(f"Drone8 discovered with UUID: {state.uuid}")
            break
    async for state in drone9.core.connection_state():
        if state.is_connected:
            print(f"Drone9 discovered with UUID: {state.uuid}")
            break
    #async for state in drone10.core.connection_state():
    #    if state.is_connected:
         #   print(f"Drone10 discovered with UUID: {state.uuid}")
        #    break
    #async for state in drone11.core.connection_state():
     #   if state.is_connected:
      #      print(f"Drone11 discovered with UUID: {state.uuid}")
       #     break

    print("Waiting for drone to have a global position estimate...")
    async for health in drone1.telemetry.health():
        if health.is_global_position_ok:
            print("Global position estimate ok")
            break

    # Fetch the home location coordinates, in order to set a boundary around the home location
    print("Fetching home location coordinates...")
    async for terrain_info in drone1.telemetry.home():
        home_lat = terrain_info.latitude_deg
        home_lon = terrain_info.longitude_deg
        home_abs_alt=terrain_info.absolute_altitude_m
        break

    await drone1.action.set_takeoff_altitude(0.5)
    await drone2.action.set_takeoff_altitude(0.5)
    await drone3.action.set_takeoff_altitude(0.5)
    await drone4.action.set_takeoff_altitude(0.5)
    await drone5.action.set_takeoff_altitude(0.5)
    await drone6.action.set_takeoff_altitude(0.5)
    await drone7.action.set_takeoff_altitude(0.5)
    await drone8.action.set_takeoff_altitude(0.5)
    await drone9.action.set_takeoff_altitude(0.5)
    #await drone10.action.set_takeoff_altitude(0.5)
    #await drone11.action.set_takeoff_altitude(0.5)

    await drone1.action.set_return_to_launch_altitude(0.5)
    await drone2.action.set_return_to_launch_altitude(0.5)
    await drone3.action.set_return_to_launch_altitude(0.5)
    await drone4.action.set_return_to_launch_altitude(0.5)
    await drone5.action.set_return_to_launch_altitude(0.5)
    await drone6.action.set_return_to_launch_altitude(0.5)
    await drone7.action.set_return_to_launch_altitude(0.5)
    await drone8.action.set_return_to_launch_altitude(0.5)
    await drone9.action.set_return_to_launch_altitude(0.5)
    #await drone10.action.set_return_to_launch_altitude(0.5)
    #await drone11.action.set_return_to_launch_altitude(0.5)


    print("-- Arming")
    await drone1.action.arm()
    await drone2.action.arm()
    await drone3.action.arm()
    await drone4.action.arm()
    await drone5.action.arm()
    await drone6.action.arm()
    await drone7.action.arm()
    await drone8.action.arm()
    await drone9.action.arm()
    #await drone10.action.arm()
    #await drone11.action.arm()

    print("-- Taking off")
    await drone1.action.takeoff()
    await drone2.action.takeoff()
    await drone3.action.takeoff()
    await drone4.action.takeoff()
    await drone5.action.takeoff()
    await drone6.action.takeoff()
    await drone7.action.takeoff()
    await drone8.action.takeoff()
    await drone9.action.takeoff()
    #await drone10.action.takeoff()
    #await drone11.action.takeoff()
    
    print('--flying to the specified position')
    await drone1.action.goto_location(home_lat,home_lon,home_abs_alt+0.7,0)
    await drone2.action.goto_location(home_lat,home_lon,home_abs_alt+1.4,0)
    await drone3.action.goto_location(home_lat,home_lon,home_abs_alt+2.1,0)
    await drone4.action.goto_location(home_lat,home_lon,home_abs_alt+2.8,0)
    await drone5.action.goto_location(home_lat,home_lon+0.000012,home_abs_alt+1.75,0)
    await drone6.action.goto_location(home_lat,home_lon+0.000024,home_abs_alt+0.7,0)
    await drone7.action.goto_location(home_lat,home_lon+0.000024,home_abs_alt+1.4,0)
    await drone8.action.goto_location(home_lat,home_lon+0.000024,home_abs_alt+2.1,0)
    await drone9.action.goto_location(home_lat,home_lon+0.000024,home_abs_alt+2.8,0)
    #await drone10.action.goto_location(home_lat,home_lon+0.000030,home_abs_alt+2.8,0)
    #await drone11.action.goto_location(home_lat,home_lon+0.000030,home_abs_alt+3.5,0)

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
    await drone2.action.return_to_launch()
    await drone3.action.return_to_launch()
    await drone4.action.return_to_launch()
    await drone5.action.return_to_launch()
    await drone6.action.return_to_launch()
    await drone7.action.return_to_launch()
    await drone8.action.return_to_launch()
    await drone9.action.return_to_launch()
    #await drone10.action.return_to_launch()
    #await drone11.action.return_to_launch()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
