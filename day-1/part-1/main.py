def get_location_ids(line):
    """Obtain the two numbers from a line of the puzzle input."""
    line = line.strip().split(' ')
    return [int(num) for num in line if num]


def get_total_distance(*, left_list, right_list):
    """Get the total distance between the left and right lists of numbers."""
    # Sort the two lists in ascending order
    left_list.sort()
    right_list.sort()

    # We assume the puzzle input lists are the same size and use
    # zip to iterate through both lists, creating the pairs and finding
    # the difference between them to get the distance
    distance = 0
    for pair in zip(left_list, right_list):
        distance += abs(pair[0] - pair[1])
    return distance

if __name__ == "__main__":
    left_list = []
    right_list = []
    with open("../input.txt", "r") as f:
        for line in f:
            ids = get_location_ids(line)
            if ids:
                # Assume two numbers for each line
                left_list.append(ids[0])
                right_list.append(ids[1])
        distance = get_total_distance(left_list=left_list, right_list=right_list)    
        print(f"The total distance is {distance}")
