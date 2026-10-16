facts = {
    "temperature": 32,
    "is_raining": True,
    "humidity": 80,
    "has_class": True,
    "is_tired": True
}

print("==========================================")
print("KNOWLEDGE REPRESENTATION")
print("==========================================")
print("Knowledge Base:")
for key, value in facts.items():
    print(f"- {key}: {value}")


# PART 2 - RULE-BASED REASONING (RBR)


# Rule 1
def rule_hot(facts):
    if facts["temperature"] > 30:
        return "Turn on the air conditioner."


# Rule 2
def rule_raining(facts):
    if facts["is_raining"]:
        return "Bring an umbrella."


# Rule 3
def rule_tired(facts):
    if facts["is_tired"]:
        return "Take a short rest."


# Rule 4
def rule_class(facts):
    if facts["has_class"]:
        return "Prepare for class."


# Inference Engine
def inference_engine(facts):
    rules = [
        rule_hot,
        rule_raining,
        rule_tired,
        rule_class
    ]

    actions = []

    for rule in rules:
        result = rule(facts)

        if result:
            actions.append(result)

    return actions


# Display RBR Output
print("\n==========================================")
print("RULE-BASED REASONING")
print("==========================================")

actions = inference_engine(facts)

print("Rule-Based Reasoning Actions:")
for action in actions:
    print("- " + action)

# PART 3 - CASE-BASED REASONING (CBR)

# Case Base
# Contains previous student problems and their solutions.

case_base = [
    {
        "problem": {
            "temperature": 32,
            "is_raining": True,
            "is_tired": True
        },
        "solution": "Bring an umbrella, turn on the air conditioner, and take a short rest."
    },
    {
        "problem": {
            "temperature": 25,
            "is_raining": True,
            "is_tired": False
        },
        "solution": "Bring an umbrella and wear comfortable clothes."
    },
    {
        "problem": {
            "temperature": 35,
            "is_raining": False,
            "is_tired": True
        },
        "solution": "Turn on the air conditioner and take a short rest."
    }
]


# New Problem
new_problem = {
    "temperature": 33,
    "is_raining": True,
    "is_tired": True
}


# Task 3B - Retrieve Step
# Calculates similarity based on matching features.

def calculate_similarity(problem1, problem2):
    matches = 0

    for key in problem1:
        if key in problem2 and problem1[key] == problem2[key]:
            matches += 1

    return matches


def retrieve_case(new_problem, case_base):
    best_case = None
    best_score = -1

    for case in case_base:
        score = calculate_similarity(
            new_problem,
            case["problem"]
        )

        if score > best_score:
            best_score = score
            best_case = case

    return best_case, best_score


# Task 3C - Reuse Step
# Reuses the solution from the most similar case.

best_case, similarity = retrieve_case(new_problem, case_base)

reused_solution = best_case["solution"]


# Task 3D - Revise Step
# In this example, the retrieved solution is accepted
# without changes.

revised_solution = reused_solution


# Task 3E - Retain Step
# Adds the new problem and solution to the case base.

new_case = {
    "problem": new_problem,
    "solution": revised_solution
}

case_base.append(new_case)


# Display CBR Output
print("\n==========================================")
print("CASE-BASED REASONING")
print("==========================================")

print("New Problem:")
for key, value in new_problem.items():
    print(f"- {key}: {value}")

print("\nMost Similar Past Case:")
for key, value in best_case["problem"].items():
    print(f"- {key}: {value}")

print(f"\nSimilarity Score: {similarity}")
print(f"Reused Solution: {reused_solution}")
print(f"Revised Solution: {revised_solution}")

print("\nRetain Step:")
print("The new case has been added to the case base.")

print("\nUpdated Number of Cases:", len(case_base))