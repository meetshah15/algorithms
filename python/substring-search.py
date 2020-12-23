import collections

# Mind == blown.

def findSubstring(s: str, words):
    if not s or not words:
      return []

    n, m = map(len, (words, words[0]))
    counter, result = collections.Counter(words), []

    for i in range(m):
      q, local = collections.deque(), collections.Counter()
      for j in range(i, len(s), m):
        word = s[j:j+m]
        q.append(word)
        local[word] += 1

        while local[word] > counter[word]:
          local[q.popleft()] -= 1

        if len(q) == n:
          result.append(j+m-m*n)
    return result



findSubstring('barfoothefoobarman', ["foo","bar"])