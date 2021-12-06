def part1():
    input = [int(i) for i in open("input").read().split(',')]

    for day in range(80):
        tmp = []
        for i in input:
            if i == 0:
                tmp.append(8)
                tmp.append(6)
            else:
                tmp.append(i-1)

        input = tmp

    print("Part 1: ", len(tmp))


def part2():
    input = [int(i) for i in open("input").read().split(',')]
    ages = {i: 0 for i in range(9)}

    for age in input:
        ages[age] += 1

    for day in range(256):
        new_ages = {i: 0 for i in range(9)}
        for age in ages:
            if age == 0:
                new_ages[8] += ages[0]
                new_ages[6] += ages[0]
            else:
                new_ages[age-1] += ages[age]
        ages = new_ages

    print("After 256 days: ", sum(ages.values()))


if __name__ == "__main__":
    part1()
    part2()