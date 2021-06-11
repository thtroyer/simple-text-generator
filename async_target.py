from time import sleep


def printfunc():
    for x in range(0, 5):
        for y in range(0, 25):
            print(f"{x},{y}")
        sleep(1)

if __name__ == "__main__":
    printfunc()
print(*a, file = sys.stderr)
