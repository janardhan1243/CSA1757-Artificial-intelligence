class MapColoringCSP:
    def __init__(self, regions, neighbors, colors):
        self.regions = regions
        self.neighbors = neighbors
        self.colors = colors
        self.assignments = {}

    def is_valid(self, region, color):
        for neighbor in self.neighbors.get(region, []):
            if neighbor in self.assignments and self.assignments[neighbor] == color:
                return False
        return True

    def backtrack(self):
        if len(self.assignments) == len(self.regions):
            return self.assignments

        unassigned_regions = [r for r in self.regions if r not in self.assignments]
        region = unassigned_regions[0]

        for color in self.colors:
            if self.is_valid(region, color):
                self.assignments[region] = color
                result = self.backtrack()
                if result:
                    return result
                del self.assignments[region]

        return None

regions = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}
colors = ['Red', 'Green', 'Blue']

map_csp = MapColoringCSP(regions, neighbors, colors)
solution = map_csp.backtrack()

if solution:
    print("Map Coloring Solution:")
    for region, color in solution.items():
        print(f"{region}: {color}")
else:
    print("No solution found.")
