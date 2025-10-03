# Store 5 tudents as tuples (name, age)
students = [ ("Chipo", 21), ("Humphery", 22), ("Bright", 24), ("Mwale", 30), ("Jacob", 25) ]

# Create two sets representing different clubs 
club_A = {("chipo", 21), ("Bright", 24), ("Jacob", 25)}
club_B = {("chipo", 21), ("Humphery", 22), ("Mwale", 30)}

# Dispaly all members of each club
print("=== Club A Members ===")
for member in club_A:
    print(member)

print("=== Club B Members ===")
for member in club_B:
    print(member)

# Find common member
common_members = club_A & club_B
print("=== Common Member (Both clubs) ===")
for member in common_members:
    print(member)

# Find members unique to Club A
unique_A = club_A - club_B
print("=== Members Unique to Club A ===")
for member in unique_A:
    print(member)

# Find members unique to Club B
unique_B = club_B - club_A
print("=== Members Unique to Club B ===")
for member in unique_B:
    print(member)
