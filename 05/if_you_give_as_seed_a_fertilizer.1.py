class ElfMap:
    def __init__(self) -> None:
        self.ranges = []

    def addMappingRange(self, destination_range_start : int, source_range_start : int, range_length : int):
        self.ranges.append((destination_range_start, source_range_start, range_length))
    
    def getDestination(self, source : int) -> int:
        for destination_range_start, source_range_start, range_length in self.ranges:
            if source_range_start <= source < source_range_start + range_length:
                return destination_range_start + (source - source_range_start)
        return source


with open("input.txt", "r") as almanac:
    maps = []
    seeds = [int(x) for x in almanac.readline().split(" ")[1:]]

    for line in almanac:
        if line == "\n":
            continue
        if "map" in line:
            maps.append(ElfMap())
            continue
        destination_range_start, source_range_start, range_length = [int(x) for x in line.split(" ")]
        elf_map = maps[-1]
        elf_map.addMappingRange(destination_range_start, source_range_start, range_length)
    
    locations = []
    for seed in seeds:
        for elf_map in maps:
            seed = elf_map.getDestination(seed)
        locations.append(seed)
    
    print(min(locations))


