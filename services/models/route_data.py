from .location import Location
from .route_step import RouteStep

class RouteData:
    """Full route info."""
    def __init__(self, start: Location, end: Location, steps: list,
                 geometry: list, total_time_min: float):
        pass
