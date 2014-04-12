#!/usr/bin/python
import fileinput

BASE_COOKIES = 2


def get_input():
    return [line.strip() for line in fileinput.input()]


def cookie_solver(farm_cost, extra_cookies, win_num):
    def solve(time, bases=0, prev_time=None):
        base_time = win_num / (BASE_COOKIES + (bases * extra_cookies))
        new_time = time + base_time
        if new_time < prev_time:
            _time = time + (farm_cost / (BASE_COOKIES + (bases * extra_cookies)))
            return solve(_time, bases + 1, prev_time=new_time)
        else:
            return prev_time

    bases = 0
    _time = (farm_cost / (BASE_COOKIES + (bases * extra_cookies)))
    return solve(_time, bases + 1, prev_time=(win_num / BASE_COOKIES))


def main():
    input = get_input()
    num_cases = input.pop(0)

    for foo in input:
        farm_cost, extra_cookies, win_num = [float(i) for i in foo.split()]
        print cookie_solver(farm_cost, extra_cookies, win_num)


if __name__ == '__main__':
    main()
