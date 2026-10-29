# K-Means Clustering for 1D Data
data = [2, 4, 10, 12, 3, 20, 30, 11, 25]

# Initial centroids
m1 = 4
m2 = 11

for iteration in range(2, 4):
    # Assign points to the nearest centroid
    c1 = []
    c2 = []

    for point in data:
        if abs(point - m1) <= abs(point - m2):
            c1.append(point)
        else:
            c2.append(point)

    # Calculate new centroids
    new_m1 = sum(c1) / len(c1)
    new_m2 = sum(c2) / len(c2)

    print(f"\nIteration {iteration}")
    print("C1 =", c1)
    print("C2 =", c2)
    print("M1 =", new_m1)
    print("M2 =", new_m2)

    # Update centroids
    m1 = new_m1
    m2 = new_m2
