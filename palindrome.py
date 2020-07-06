def main():
    print("Reverse comparison:")
    print("abap", isPalindrome("abap"))
    print("abba", isPalindrome("abba"))
    print()
    print("Iteration with early return:")
    print("abap", isPalindromeFast("abap"))
    print("abba", isPalindromeFast("abba"))
    print()
    print("Recursive:")
    print("abap", isPalindromeRecursive("abap"))
    print("abba", isPalindromeRecursive("abba"))


def isPalindrome(input):
    return input == reverse(input)


def isPalindromeFast(input):
    length = len(input)

    for i, ch in enumerate(input):
        if ch != input[length - 1 - i]:
            return False

    return True


def isPalindromeRecursive(input):
    if len(input) <= 1:
        return True
    
    if (input[0] != input[len(input) - 1]):
        return False

    return isPalindromeRecursive(input[1:len(input) - 1])


def reverse(input):
    return input[::-1]


main()
