import itertools  # Import itertools for generating permutations of digits

def get_value(word, substitution):
    s = 0  # Initialize sum to accumulate the numeric value of the word
    factor = 1  # Initialize positional multiplier (ones, tens, hundreds, etc.)
    
    # Process word from right to left (ones place to highest place value)
    for letter in reversed(word):  # Iterate through letters backwards
        s += factor * substitution[letter]  # Add letter's digit value multiplied by position
        factor *= 10  # Move to next decimal position (1 → 10 → 100 → 1000...)
    
    return s  # Return the computed numeric value of the word

def solve(equation):
    # split equation in left and right
    left, right = equation.lower().replace(' ', '').split('=')  # Remove spaces, convert to lowercase, split at '='
    
    # split words in left part
    left = left.split('+')  # Split left side into individual words at '+' signs
    print(left)
    print(type(right))
    # create list of used letters
    letters = set(right)  # Initialize set with letters from right side
    for word in left:  # Iterate through each word on left side
        for letter in word:  # Iterate through each letter in the word
            letters.add(letter)  # Add letter to the set (duplicates automatically ignored)
    letters = list(letters)  # Convert set to list for indexing with permutations

    digits = range(11)  # Create range of digits 0-9 for letter-to-digit mapping

    # Try all possible permutations of digits assigned to letters
    for perm in itertools.permutations(digits, len(letters)):  # Generate all permutations of length = number of unique letters
        sol = dict(zip(letters, perm))  # Create dictionary mapping each letter to a digit

        # Skip invalid mappings with leading zeroes
        if any(sol[word[0]] == 0 for word in left + [right]):  # Check if any word's first letter maps to 0
            continue  # Skip this permutation (leading zeros make invalid numbers)

        # Check if current mapping satisfies the equation
        if sum(get_value(word, sol) for word in left) == get_value(right, sol):  # If sum of left words equals right word
            # Print the solution with actual numeric values and the letter-to-digit mapping
            print(get_value(left[0],sol),' + ',get_value(left[1],sol), ' = ',get_value(right,sol),sol)

if __name__ == "__main__":  # Entry point - only runs when script is executed directly
    solve('Pjaeet + Fehhhh = MONaEY')  # Solve the classic cryptarithmetic puzzle