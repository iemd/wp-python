# Implement the Tower of Hanoi Algorithm

def move(src, dest):
    if not src:
        src.append(dest.pop())
    elif not dest:
        dest.append(src.pop())
    elif src[-1] > dest[-1]:
        src.append(dest.pop())
    else:
        dest.append(src.pop())

def hanoi_solver(n):
    src, aux, dest = list(range(n, 0, -1)), [], []

    total_moves = 2**n - 1
    rods = f"{src} {aux} {dest}"
    
    # For EVEN n, the 1st legal move is src -> aux
    for i in range(1, total_moves + 1):
        if i % 3 == 1:            
            if n % 2 == 0:
                move(src, aux)
            else:
                move(src, dest)
            rods += f"\n{src} {aux} {dest}"
        elif i % 3 == 2:
            if n % 2 == 0:
                move(src, dest)
            else:
                move(src, aux)
            rods += f"\n{src} {aux} {dest}"
        elif i % 3 == 0:
            move(aux, dest)
            rods += f"\n{src} {aux} {dest}"

    return rods

if __name__ == "__main__":
    print(hanoi_solver(3))
