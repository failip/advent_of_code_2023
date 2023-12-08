from __future__ import annotations
from itertools import pairwise

class ElfMap:
    def __init__(self) -> None:
        self.ranges = []

    def addMappingRange(self, destination_range_start : int, source_range_start : int, range_length : int):
        self.ranges.append((destination_range_start, source_range_start, range_length))
    
    def sort(self):
        self.ranges.sort(key=lambda x: x[1])
    
    def getDestination(self, source : int) -> int:
        for destination_range_start, source_range_start, range_length in self.ranges:
            if source_range_start <= source < source_range_start + range_length:
                return destination_range_start + (source - source_range_start)
        return source
    
    def getMappingRange(self, source: int) -> tuple[int, int, int]:
        for destination_range_start, source_range_start, range_length in self.ranges:
            if source_range_start <= source < source_range_start + range_length:
                return (destination_range_start, source_range_start, range_length)
        raise ValueError("Should never happen")
    
    def isInMappingRange(self, source: int) -> bool:
        for destination_range_start, source_range_start, range_length in self.ranges:
            if source_range_start <= source < source_range_start + range_length:
                return True
        return False
    
def meissnerBlocking(mapped_untill, seed, elf_map) -> tuple():
        seed_start, seed_range = seed
        seed_end = seed_start + seed_range - 1
        if elf_map.isInMappingRange(mapped_untill):
            mapping_range = elf_map.getMappingRange(mapped_untill)
            destination = elf_map.getDestination(mapped_untill)
            map_end = mapping_range[2] + mapping_range[1]
            is_map_end_larger_than_seed_end = map_end >= seed_end
            if is_map_end_larger_than_seed_end:
                return seed_end, (destination, destination + seed_end - mapped_untill)
            else:
                return map_end, (destination, destination + (map_end - mapped_untill))
        else:
            for destination_range_start, source_range_start, range_length in elf_map.ranges:
                mapping_range_starts_in_seed_range = source_range_start >= seed_start and source_range_start < seed_start + seed_range
                mapping_range_is_larger_than_mapped_untill = source_range_start + range_length > mapped_untill
                if mapping_range_starts_in_seed_range and mapping_range_is_larger_than_mapped_untill:
                    return source_range_start, (mapped_untill, source_range_start)

        return seed_end, (mapped_untill, seed_end)

    
with open("input.txt", "r") as almanac:
    maps = []
    seeds = [int(x) for x in almanac.readline().split(" ")[1:]]
    seeds = list(pairwise(seeds))

    for line in almanac:
        if line == "\n":
            continue
        if "map" in line:
            maps.append(ElfMap())
            continue
        destination_range_start, source_range_start, range_length = [int(x) for x in line.split(" ")]
        elf_map = maps[-1]
        elf_map.addMappingRange(destination_range_start, source_range_start, range_length)
        elf_map.sort()
    
    locations = []
   
    seeds = seeds[::2]

    for elf_map in maps:
        blocks = []
        for seed in seeds:
            mapped_untill = seed[0]
            while mapped_untill != seed[0] + seed[1] - 1:
                mapped_untill, block = meissnerBlocking(mapped_untill, seed, elf_map)
                blocks.append(block)

        seeds = [(block[0], block[1] - block[0] + 1) for block in blocks]
        seeds = sorted(seeds, key=lambda x: x[0])

    print(min([seed[0] for seed in seeds]))
