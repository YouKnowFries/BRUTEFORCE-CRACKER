import hashlib

hashed_password = input("Enter the hashed password: ")

# Open a dictionary file containing a list of words
with open("dictionary.txt", "r") as f:
    # Read the words in the file and store them in a list
    words = f.readlines()

# Iterate through the list of words
for word in words:
    # Strip the newline character from the word
    word = word.strip()
    # Hash the word using the SHA-256 algorithm
    test_hash = hashlib.sha256(word.encode()).hexdigest()
    # Compare the test hash to the hashed password
    if test_hash == hashed_password:
        # If the hashes match, print the original word and exit the loop
        print(f"The original password is: {word}")
        break
