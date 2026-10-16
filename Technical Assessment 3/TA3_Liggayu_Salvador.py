# ==========================================
# CASE-BASED REASONING (CBR)
# Intelligent Tutoring System
# ==========================================

# 1. CASE BASE
# These are previous student cases.
case_base = [
    {
        "topic": "Algebra",
        "error": "wrong formula",
        "solution": "Review the correct algebra formula."
    },
    {
        "topic": "Algebra",
        "error": "calculation error",
        "solution": "Practice basic calculations."
    },
    {
        "topic": "Geometry",
        "error": "wrong formula",
        "solution": "Review the correct geometry formula."
    },
    {
        "topic": "Geometry",
        "error": "calculation error",
        "solution": "Practice geometry calculations."
    }
]


# 2. NEW PROBLEM
print("=== INTELLIGENT TUTORING SYSTEM ===")

topic = input("Enter topic (Algebra/Geometry): ")
error = input("Enter error (wrong formula/calculation error): ")

new_case = {
    "topic": topic,
    "error": error
}


# 3. RETRIEVE
# Find the most similar previous case.
best_case = None
highest_score = -1

for case in case_base:

    score = 0

    if case["topic"].lower() == topic.lower():
        score += 1

    if case["error"].lower() == error.lower():
        score += 1

    print("Similarity Score:", score)

    if score > highest_score:
        highest_score = score
        best_case = case


# Display retrieved case
print("\n=== RETRIEVED CASE ===")
print("Topic:", best_case["topic"])
print("Error:", best_case["error"])
print("Similarity Score:", highest_score)


# 4. REUSE AND ADAPT
print("\n=== ADAPTED SOLUTION ===")

if error.lower() == "wrong formula":
    solution = "Review the correct formula and practice similar problems."
else:
    solution = "Practice solving problems carefully and check your calculations."

print(solution)


# 5. RETAIN
# Save the new case to the case base.
new_case["solution"] = solution
case_base.append(new_case)

print("\n=== RETENTION ===")
print("New case saved!")


# 6. UPDATED CASE BASE
print("\n=== UPDATED CASE BASE ===")

for case in case_base:
    print(case)