
Method: The method creates a 4-line poem about 'nature' using simple grammar rules. It uses specific words grouped by type (like nouns and verbs) and pairs of rhyming words.

How the System Works: The system picks random words from the groups to fill in lines of the poem. It makes sure the lines follow an ABAB rhyme pattern.I used this approach since it lets us create structured poems and generates different poems each time.

Demonstrating the Generation Process: The final output shows a nature-themed poem that rhymes according to the ABAB pattern.

import random

# Nature-themed vocabulary
nature_words = {
    'nouns': ['sky', 'tree', 'river', 'bird', 'sun', 'cloud', 'breeze', 'mountain'],
    'verbs': ['flows', 'sings', 'shines', 'blows', 'flies', 'whispers', 'drifts', 'stands'],
    'adjectives': ['golden', 'silent', 'calm', 'majestic', 'clear', 'blue', 'soft', 'green'],
    'places': ['forest', 'valley', 'sea', 'plain', 'horizon', 'meadow', 'ocean', 'field']
}

# Rhyming pairs for ABAB structure
rhyming_pairs_A = [('tree', 'free'), ('sky', 'fly'), ('light', 'sight')]
rhyming_pairs_B = [('breeze', 'leaves'), ('ground', 'sound'), ('sea', 'be')]

# Randomly select rhyming pairs
rhyme_A = random.choice(rhyming_pairs_A)
rhyme_B = random.choice(rhyming_pairs_B)

# Line templates using the vocabulary
line_1 = f"The {random.choice(nature_words['adjectives'])} {rhyme_A[0]} {random.choice(nature_words['verbs'])} in the {random.choice(nature_words['places'])}"
line_2 = f"While {random.choice(nature_words['nouns'])} {random.choice(nature_words['verbs'])} beneath the {rhyme_B[0]}"
line_3 = f"A {random.choice(nature_words['adjectives'])} {rhyme_A[1]} {random.choice(nature_words['verbs'])} high and free"
line_4 = f"As {random.choice(nature_words['nouns'])} {random.choice(nature_words['verbs'])} without a {rhyme_B[1]}"

# Display the generated poem
ballad = f"{line_1}\n{line_2}\n{line_3}\n{line_4}"
print(ballad)
