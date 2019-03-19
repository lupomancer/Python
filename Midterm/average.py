#! /usr/bin/env python3

def main():
    nums = input("Enter numbers to average: ").split()
    nums = list(map(int, nums))
    average = sum(nums) / len(nums)
    print(average)

if __name__ == "__main__":
    main()
