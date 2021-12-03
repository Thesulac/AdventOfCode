def part1():
    nums = [i.strip() for i in open("input")]

    gamma = list(nums[0])

    for bit in range(len(nums[0])):
        bits = [j[bit] for j in nums]

        gamma[bit] = str(int(bits.count('1') > bits.count('0') * 1))

    epsilon = int(''.join(gamma).replace(
        '0', 'x').replace('1', '0').replace('x', '1') , 2)
    gamma = int(''.join(gamma),2)
    

    print("part 1 : ", gamma * epsilon)


def part2():

    nums_oxy = [i.strip() for i in open("input")]
    nums_car = nums_oxy.copy()

    for bit in range(len(nums_oxy[0])):

        bits_oxy = [j[bit] for j in nums_oxy]

        if bits_oxy.count('1') >= bits_oxy.count('0'):
            nums_oxy = [j for j in nums_oxy if j[bit] == '1']
        else:
            nums_oxy = [j for j in nums_oxy if j[bit] == '0']

        if len(nums_oxy) == 1:
            break

    for bit in range(len(nums_car[0])):

        bits_car = [j[bit] for j in nums_car]

        if bits_car.count('1') >= bits_car.count('0'):
            nums_car = [j for j in nums_car if j[bit] == '0']
        else:
            nums_car = [j for j in nums_car if j[bit] == '1']

        if len(nums_car) == 1:
            break

    print("part 2 : ", int(nums_oxy[0], 2) * int(nums_car[0], 2))


if __name__ == "__main__":

    part1()
    part2()
