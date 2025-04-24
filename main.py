def countWellFormedParenthesis(n):
    def backtrack(open_count, close_count):
        if open_count == n and close_count == n:
            return 1
        count = 0
        if open_count < n:
            count += backtrack(open_count + 1, close_count)
        if close_count < open_count:
            count += backtrack(open_count, close_count + 1)
        return count

    return backtrack(0, 0)

if __name__ == "__main__":
    print(countWellFormedParenthesis(6))