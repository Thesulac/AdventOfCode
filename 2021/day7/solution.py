def part1():
    input = list(map(int, open("input").read().split(',')))

    total = min([sum(map(lambda x:  abs(x-i), input)) for i in input])

    print("Total fuel part 1: ", total)


def fuel(distance):
    return (distance * (distance + 1)) // 2

def part2():
  
    input = list(map(int, open("input").read().split(',')))
    #Note: dont loop over input, but over positions! 
    #Optimal position does not have to exist in input!
    total = min([sum(map(lambda x: fuel(abs(x-i)), input)) for i in range(1300)])

    print("Total Fuel part 2: ", total)



if __name__ == "__main__":
  part1()
  part2()