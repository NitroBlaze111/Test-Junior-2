from typing import Dict, List

def find_busiest_intersections(intersections: Dict[str, int]) -> List[str]:

    if not intersections:
        return []

    max_vehicles = max(intersections.values())
    return [intersection for intersection, vehicles in intersections.items() if vehicles == max_vehicles]