import sys

if __name__ == "__main__":
    # Print each argument along with its index
    for i, arg in enumerate(sys.argv[1:], 1):
        print(f"{arg}", end=' ')
