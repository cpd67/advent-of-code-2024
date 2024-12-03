def get_location_ids(line):
    """Obtain the two numbers from a line of the puzzle input."""
    line = line.strip().split(' ')
    return [int(num) for num in line if num]


def get_similarity_score(*, left_list, right_list):
    """Obtain the similarity score between our two lists."""
    # TODO potentially improve this so we don't have to iterate the right list
    #      for *every* left number
    score = 0
    for left_num in left_list:
        seen = 0
        for right_num in right_list:
            if left_num == right_num:
                seen += 1
        score += (left_num * seen)
    return score


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
        score = get_similarity_score(left_list=left_list, right_list=right_list)
        print(f"The similarity score is {score}")
