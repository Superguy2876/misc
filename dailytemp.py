def dailyTemperatures(temperatures: list[int]) -> list[int]:
    stack = []
    days_to_wait = [0] * len(temperatures)
    for i, temp in enumerate(temperatures):
        while stack and (temp > stack[-1][0]):
            current_temp, index = stack.pop()
            days_to_wait[index] = i - index
        stack.append((temp, i))
    return days_to_wait
            



if __name__ == "__main__":
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(dailyTemperatures(temperatures))

