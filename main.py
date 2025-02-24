from solution import Solution

def main():
    solution = Solution()
    a = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(f"Original array: {a}")
    solution.rotate(a, k)
    print(f"Array after rotating {k} steps: {a}")

if __name__ == "__main__":
    main()
