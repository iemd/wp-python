# Implement the Bisection Method

def square_root_bisection(num, t=1e-7, itr=80):
    
    if num < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    elif num == 0 or num == 1:
        print(f"The square root of {num} is {num}")
        return num
    else:
        low = 0
        high = max(1, num)
        mid = (low + high) / 2
        root = None
        
        for i in range(itr):
            mid = (low + high) / 2
            mid_square = mid ** 2

            if (high - low) <= t:
                root = mid
                break
            elif mid_square < num:
                low = mid
            else:
                high = mid
        
        if root is None:
            print(f"Failed to converge within {itr} iterations")
        else:
            print(f"The square root of {num} is approximately {root}")
        return root

square_root_bisection(0)
square_root_bisection(1)

square_root_bisection(0.001, 1e-7, 50)
square_root_bisection(225, 1e-7, 10)
