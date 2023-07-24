from project import current_location, check_areas, distance_to_swim


def test_current_location():
    assert current_location("London") == {"lat": 51.5072178, "lng": -0.1275862}
    assert current_location(
        "Studio Tour Dr, Leavesden, Watford WD25 7LR, United Kingdom"
    ) == {"lat": 51.6897515, "lng": -0.4181465}


def test_distance_to_swim():
    swimming_locations_data = [
        {
            "area": "Cornwall",
            "name": "Golitha Falls",
            "lat": "[50.4903515]",
            "long": "[-4.505363099999999]",
        }
    ]
    assert distance_to_swim("St Cleer", swimming_locations_data) == [
        "4 mins, Golitha Falls, https://www.google.com/maps/search/?api=1&query=50.4903515,-4.505363099999999"
    ]

    swimming_locations_data = [
        {
            "area": "Cumbria",
            "name": "Lake District",
            "lat": "54.461913",
            "long": "-3.0333548",
        }
    ]
    assert distance_to_swim("Great Langdale", swimming_locations_data) == [
        "28 mins, Lake District, https://www.google.com/maps/search/?api=1&query=54.461913,-3.0333548",
    ]


def test_check_areas():
    assert check_areas()[:3] == [
        {
            "area": "Ayrshire",
            "name": "Portencross",
            "lat": "[55.7005205]",
            "long": "[-4.900692299999999]",
        },
        {
            "area": "Bath",
            "name": "River Avon",
            "lat": "[51.3781018]",
            "long": "[-2.3596827]",
        },
        {
            "area": "Cheshire",
            "name": "River Dee",
            "lat": "[53.14351627367295]",
            "long": "[-3.226531211950963]",
        },
    ]
