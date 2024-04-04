import numpy as np

def viterbi(sentence, states, start_prob, transition_prob, emission_prob):
    n, m = len(sentence), len(states)
    viterbi_matrix = np.zeros((m, n))
    backpointer = np.zeros((m, n), dtype=int)

    for s in range(m):
        viterbi_matrix[s, 0] = start_prob[states[s]] * emission_prob[states[s]][sentence[0]]

    for t in range(1, n):
        for s in range(m):
            max_prob, max_state = max((viterbi_matrix[prev_s, t-1] * transition_prob[states[prev_s]][states[s]] * emission_prob[states[s]][sentence[t]], prev_s) for prev_s in range(m))
            viterbi_matrix[s, t] = max_prob
            backpointer[s, t] = max_state

    best_seq, last_state = [], np.argmax(viterbi_matrix[:, n-1])
    best_seq.append(last_state)
    for t in range(n-1, 0, -1):
        last_state = backpointer[last_state, t]
        best_seq.insert(0, last_state)

    return [states[i] for i in best_seq]

# Example usage
sentence = ["I", "saw", "a", "man", "with", "a", "telescope"]
states = ["NOUN", "VERB", "DET", "ADP", "ADV"]
start_prob = {"NOUN": 0.3, "VERB": 0.2, "DET": 0.1, "ADP": 0.1, "ADV": 0.05}
transition_prob = { "NOUN": {"NOUN": 0.1, "VERB": 0.2, "DET": 0.4, "ADP": 0.2, "ADV": 0.1}, "VERB": {"NOUN": 0.3, "VERB": 0.1, "DET": 0.1, "ADP": 0.3, "ADV": 0.2}, "DET": {"NOUN": 0.6, "VERB": 0.1, "DET": 0.2, "ADP": 0.05, "ADV": 0.05}, "ADP": {"NOUN": 0.2, "VERB": 0.1, "DET": 0.5, "ADP": 0.1, "ADV": 0.1}, "ADV": {"NOUN": 0.1, "VERB": 0.2, "DET": 0.1, "ADP": 0.3, "ADV": 0.3} }
emission_prob = { "NOUN": {"I": 0.1, "saw": 0.1, "a": 0.5, "man": 0.1, "with": 0.1, "telescope": 0.1}, "VERB": {"I": 0.1, "saw": 0.5, "a": 0.1, "man": 0.1, "with": 0.1, "telescope": 0.1}, "DET": {"I": 0.2, "saw": 0.1, "a": 0.5, "man": 0.1, "with": 0.1, "telescope": 0.1}, "ADP": {"I": 0.1, "saw": 0.1, "a": 0.1, "man": 0.2, "with": 0.4, "telescope": 0.1}, "ADV": {"I": 0.1, "saw": 0.1, "a": 0.1, "man": 0.1, "with": 0.1, "telescope": 0.5} }

best_tags = viterbi(sentence, states, start_prob, transition_prob, emission_prob)
print("Sentence:",sentence)
print("Predicted Tags:",best_tags)
