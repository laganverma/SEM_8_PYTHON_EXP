from collections import defaultdict

def add_one_smoothing(corpus):
    ngrams = defaultdict(int)
    context_counts = defaultdict(int)

    # Count bigrams and their contexts
    for i in range(len(corpus) - 1):
        bigram = (corpus[i], corpus[i + 1])
        ngrams[bigram] += 1
        context_counts[bigram[0]] += 1  # Count the context of each bigram

    # Calculate probabilities with add-one smoothing
    probabilities = {}
    for bigram, count in ngrams.items():
        context = bigram[0]
        context_count = context_counts[context]
        probabilities[bigram] = (count + 1) / (context_count + len(set(corpus)))

    return probabilities

# Test Input
corpus = "people don't want to go to that extra mile".split()

# Apply add-one smoothing
probabilities = add_one_smoothing(corpus)

# Print Result
print("Add-One Smoothing Probabilities:")
for bigram, prob in probabilities.items():
    print(f"{bigram}: {prob:.4f}")