import folium
import numpy as np
import directions


def generate_map(coordinates, names, directs):

    route_points = directs
    lat_centre = np.mean([x for (x, y) in coordinates])
    lon_centre = np.mean([y for (x, y) in coordinates])
    centre = lat_centre, lon_centre

    m = folium.Map(location=centre, zoom_start=1, zoom_control=True)

    # plot the route line
    folium.PolyLine(route_points, color='red', weight=2).add_to(m)
    
    # plot each point with a hover tooltip  
    for i, (point, name) in enumerate(zip(coordinates, names)):
        folium.CircleMarker(location=point,
                      tooltip=f'{i}: {name}',
                      radius=5).add_to(m)

    custom_tile_layer = folium.TileLayer(
        tiles='http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png',
        attr='CartoDB Positron',
        name='Positron',
        overlay=True,
        control=True,
        opacity=0.0  # Adjust opacity to control the level of greying out
    )

    custom_tile_layer.add_to(m)
    folium.LayerControl().add_to(m)

    sw = (np.min([x for (x, y) in coordinates]), np.min([y for (x, y) in coordinates]))
    ne = (np.max([x for (x, y) in coordinates]), np.max([y for (x, y) in coordinates]))
    m.fit_bounds([sw, ne])

    return m


def run():
    waypoints = directions.run()
    coords_ordered = waypoints[0]
    names_ordered = waypoints[1]
    directs = waypoints[2]
    generate_map(coords_ordered, names_ordered, directs).save('ontario.html')

if __name__ == "__main__":
    run()



