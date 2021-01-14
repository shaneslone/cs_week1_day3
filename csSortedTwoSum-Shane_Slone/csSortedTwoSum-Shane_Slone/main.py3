def csSortedTwoSum(numbers, target):
    p1 = 0
    p2 = len(numbers) - 1
    while (p1 < p2):
        current = numbers[p1] + numbers[p2]
        if current == target:
            return [p1, p2]
        elif current < target:
            p1 += 1
        else:
            p2 -= 1
        
            

