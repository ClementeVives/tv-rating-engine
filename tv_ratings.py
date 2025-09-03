# This function takes a TV's attributes and calculates a score and tier (A/B/C)
def tv_ratings(tv, price, inch, screen):
    score = 0  # Start the score at 0

# Evaluate price and adjust score accordingly
    if price <= 20000:
        score += 3  # Excellent price
    elif price <= 30000:
        score += 1  # Decent price
    else:
        score -= 1  # Too expensive

# Evaluate screen size and adjust score
    if inch < 55:
        score -= 1  # Small screen
    elif inch == 55:
        score += 1  # Standard size
    else:
        score += 2  # Large screen is better

# Dictionary mapping screen types to score values
    screen_scores = {
        "mini led": 2,
        "oled": 2,
        "qled": 1,
        "led": -1  # Lowest-rated screen type
    }

# Add screen type points using dictionary lookup (default to 0 if not found)
    score += screen_scores.get(screen.lower(), 0)

# Determine the tier based on final score
    if score >= 4:
        tier = "A"
    elif score >= 2:
        tier = "B"
    else:
        tier = "C"

# Return all important results
    return (tv, tier, score)


# List to store all rated TVs
tv_results = []

# Add TVs manually to the list using the main() function
tv_results.append(tv_ratings("lg", 35000, 65, "oled"))
tv_results.append(tv_ratings("samsung", 40000, 55, "led"))
tv_results.append(tv_ratings("tcl", 18000, 55, "qled"))
tv_results.append(tv_ratings("sony", 25000, 50, "mini led"))

# Sort the list by score in descending order (best score first)
sorted_by_score = sorted(tv_results, key=lambda x: x[2], reverse=True)

# Display the results in a clean, readable format
print("TVs sorted by score:")
for name, tier, score in sorted_by_score:
    print(f"- {name}: rating: {tier}, score: {score}")
