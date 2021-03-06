import fileinput


def calculate_minimum_friends(max_shyness, audience):
    friends_needed = 0
    currently_standing = audience[0]

    for shyness, num_sitting in enumerate(audience[1:], start=1):
        if num_sitting and currently_standing < shyness:
            deficit = shyness - currently_standing
            friends_needed += deficit
            currently_standing += deficit
        currently_standing += num_sitting

    return friends_needed


def main():
    inputs = [line.strip() for line in fileinput.input()][1:]

    for case, i in enumerate(inputs, start=1):
        max_shyness, audience = i.split()
        print "Case #{case}: {min_friends}".format(
                case=case,
                min_friends=calculate_minimum_friends(int(max_shyness),
                                                      map(int, audience)))


if __name__ == '__main__':
    main()
