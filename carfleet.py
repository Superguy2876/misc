def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    times = []
    for cSpeed, cPostion in zip(speed, position):
        time = (target - cPostion)/cSpeed
        times.append((time, cPostion))
    
    times.sort(key= lambda x : x[1])
    print(times)

    

    pass


if __name__ == "__main__":
    #Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
    print(carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))
    # target = 10, position = [3], speed = [3]
    print(carFleet(10, [3], [3]))
    # target = 100, position = [0,2,4], speed = [4,2,1]
    print(carFleet(100, [0,2,4], [4,2,1]))