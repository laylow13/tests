#!/usr/bin/env python3

import asyncio
from mavsdk import System
from mavsdk.geofence import Point, Polygon

async def Create_GeoFence(drone):

    # Fetch the home location coordinates, in order to set a boundary around the home location
    print("Fetching home location coordinates...")
    async for terrain_info in drone.telemetry.home():
        latitude = terrain_info.latitude_deg
        longitude = terrain_info.longitude_deg
        break

    await asyncio.sleep(1)

    # Define your geofence boundary
    p1 = Point(latitude - 0.0001, longitude - 0.0001)
    p2 = Point(latitude + 0.0001, longitude - 0.0001)
    p3 = Point(latitude + 0.0001, longitude + 0.0001)
    p4 = Point(latitude - 0.0001, longitude + 0.0001)

    # Create a polygon object using your points
    polygon = Polygon([p1, p2, p3, p4], Polygon.FenceType.INCLUSION)

    # Upload the geofence to your vehicle
    print("Uploading geofence...")
    await drone.geofence.upload_geofence([polygon])

    print("Geofence uploaded!")