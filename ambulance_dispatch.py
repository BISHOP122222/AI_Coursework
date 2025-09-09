import heapq
import math

class AmbulanceDispatch:
    def __init__(self, city_map, hospitals, ambulances):
        self.city_map = city_map  # Dictionary with travel times between nodes
        self.hospitals = hospitals
        self.ambulances = ambulances  # Current locations of ambulances
        self.emergencies = []
    
    def add_emergency(self, location, priority=1):
        self.emergencies.append((location, priority))
    
    def heuristic(self, a, b):
        # Manhattan distance heuristic (better for grid-based navigation)
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    def a_star_search(self, start, goal):
        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {start: 0}
        f_score = {start: self.heuristic(start, goal)}
        
        while open_set:
            current = heapq.heappop(open_set)[1]
            
            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                return path[::-1]
            
            for neighbor, weight in self.city_map.get(current, []):
                tentative_g_score = g_score[current] + weight
                
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
        
        return None  # No path found
    
    def dispatch_ambulance(self):
        if not self.emergencies:
            return "No emergencies"
        
        # Find the most critical emergency (highest priority)
        emergency_location, priority = max(self.emergencies, key=lambda x: x[1])
        
        # Find the nearest available ambulance
        best_ambulance = None
        best_time = float('inf')
        best_path = None
        
        for ambulance_id, ambulance_loc in self.ambulances.items():
            path = self.a_star_search(ambulance_loc, emergency_location)
            if path:
                # FIXED: Calculate total time correctly
                time = 0
                for i in range(len(path) - 1):
                    current_node = path[i]
                    next_node = path[i + 1]
                    
                    # Find the weight between these two nodes
                    for neighbor, weight in self.city_map.get(current_node, []):
                        if neighbor == next_node:
                            time += weight
                            break
                
                if time < best_time:
                    best_time = time
                    best_ambulance = ambulance_id
                    best_path = path
        
        if best_ambulance:
            # Update ambulance location
            self.ambulances[best_ambulance] = emergency_location
            # Remove the emergency
            self.emergencies = [e for e in self.emergencies if e[0] != emergency_location or e[1] != priority]
            return f"Dispatch ambulance {best_ambulance} to {emergency_location}. Path: {best_path}. Estimated time: {best_time}"
        
        return "No available ambulance can reach the emergency"

# Example usage
if __name__ == "__main__":
    # Simplified city map (in real implementation, this would be more complex)
    # Format: {node: [(neighbor, travel_time), ...]}
    city_map = {
        (0, 0): [((0, 1), 5), ((1, 0), 5)],
        (0, 1): [((0, 0), 5), ((0, 2), 5), ((1, 1), 7)],
        (0, 2): [((0, 1), 5), ((1, 2), 5)],
        (1, 0): [((0, 0), 5), ((1, 1), 5), ((2, 0), 5)],
        (1, 1): [((0, 1), 7), ((1, 0), 5), ((1, 2), 5), ((2, 1), 5)],
        (1, 2): [((0, 2), 5), ((1, 1), 5), ((2, 2), 5)],
        (2, 0): [((1, 0), 5), ((2, 1), 5)],
        (2, 1): [((2, 0), 5), ((1, 1), 5), ((2, 2), 5)],
        (2, 2): [((1, 2), 5), ((2, 1), 5)]
    }
    
    hospitals = [(2, 2)]
    ambulances = {'A1': (0, 0), 'A2': (1, 1)}
    
    dispatch_system = AmbulanceDispatch(city_map, hospitals, ambulances)
    
    # Add emergencies
    dispatch_system.add_emergency((2, 0), priority=2)
    dispatch_system.add_emergency((0, 2), priority=1)
    
    # Dispatch ambulances
    print("Emergency Dispatch System:")
    print("=" * 50)
    
    result1 = dispatch_system.dispatch_ambulance()
    print("First dispatch:", result1)
    
    result2 = dispatch_system.dispatch_ambulance()
    print("Second dispatch:", result2)
    
    # Try to dispatch again (should show no emergencies)
    result3 = dispatch_system.dispatch_ambulance()
    print("Third dispatch:", result3)