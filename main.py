def countWellFormedParenthesis(n):
    result = 1
    for i in range(n):
        result = result * 2 * (2 * i + 1) // (i + 2)
    return result

if __name__ == "__main__":
    print(countWellFormedParenthesis(6))