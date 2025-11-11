# Here’s a fast, memory-safe solution for **Maximize It!** that avoids the exponential Cartesian product by folding modulo-sum states:
#
# ```python
# HackerRank: Maximize It!

if __name__ == "__main__":
    K, M = map(int, input().split())
    lists = []
    for _ in range(K):
        parts = list(map(int, input().split()))
        lists.append(parts[1:])                      # skip the count

    # Dynamic set of achievable sums modulo M
    sums = {0}
    for arr in lists:
        arr_mod = [(x * x) % M for x in arr]
        sums = { (s + a) % M for s in sums for a in arr_mod }
        # Optional micro-optimization: cap size at M
        if len(sums) > M:
            # No need to keep more than M distinct residues
            sums = set(list(sums)[:M])

    print(max(sums))

# ```

### Why this works
#
# * For each list, we update the set of reachable sums (modulo `M`) by adding each squared choice.
# * The set never needs to exceed `M` elements (there are only `M` distinct residues), so the approach is efficient even when individual list sizes are larger.
# * Time complexity is roughly (O!\left(\sum_i |L_i| \cdot |S|\right)) with (|S|\le M), which fits the problem constraints.
