def update_high_scores(player_score, max_scores=5):

    scores = []
    try:
        with open("high_scores.txt", "r") as f:
            for line in f.readlines():
                try:
                    # Strip whitespace and convert to int
                    score = int(line.strip())
                    scores.append(score)
                except ValueError:
                    # Skip lines that can't be converted to int
                    print(f"Warning: Could not convert '{line.strip()}' to integer")
    except FileNotFoundError:
        print("High scores file not found, creating new one")
    
    # Add new score
    scores.append(player_score)

    # Sort scores in descending order
    scores.sort(reverse=True)
    
    # Keep only the top scores
    scores = scores[:max_scores]
    
    # Debug output
    print(f"Top {max_scores} scores: {scores}")
    
    # Write updated scores back to file
    with open("high_scores.txt", "w") as f:
        for score in scores:
            f.write(f"{score}\n")

