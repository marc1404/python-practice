def main():
    print("Reverse comparison:")
    print("abap", is_palindrome("abap"))
    print("abba", is_palindrome("abba"))
    print()
    print("Iteration with early return:")
    print("abap", is_palindrome_fast("abap"))
    print("abba", is_palindrome_fast("abba"))
    print()
    print("Recursive:")
    print("abap", is_palindrome_recursive("abap"))
    print("abba", is_palindrome_recursive("abba"))


def is_palindrome(input):
    return input == reverse(input)


def is_palindrome_fast(input):
    length = len(input)

    for i, ch in enumerate(input):
        if ch != input[length - 1 - i]:
            return False

    return True


def is_palindrome_recursive(input):
    if len(input) <= 1:
        return True
    
    if (input[0] != input[len(input) - 1]):
        return False

    return is_palindrome_recursive(input[1:len(input) - 1])


def reverse(input):
    return input[::-1]


main()
