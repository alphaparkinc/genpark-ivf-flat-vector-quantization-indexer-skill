class IVFFlatIndex:
    """Inverted File Flat (IVF-Flat) Vector Index."""
    def __init__(self, centroids: list[list[float]]):
        self.centroids = centroids
        self.inverted_lists = {i: [] for i in range(len(centroids))}

    def _dist_sq(self, v1: list[float], v2: list[float]) -> float:
        return sum((a - b) ** 2 for a, b in zip(v1, v2))

    def add(self, doc_id: str, vector: list[float]):
        best_cluster = min(range(len(self.centroids)), key=lambda i: self._dist_sq(vector, self.centroids[i]))
        self.inverted_lists[best_cluster].append((doc_id, vector))

    def search(self, query_vec: list[float], top_k: int = 3, nprobe: int = 1) -> list[dict]:
        # Rank closest centroids
        centroid_ranks = sorted(range(len(self.centroids)), key=lambda i: self._dist_sq(query_vec, self.centroids[i]))

        candidates = []
        for cluster_id in centroid_ranks[:nprobe]:
            candidates.extend(self.inverted_lists[cluster_id])

        ranked = sorted(candidates, key=lambda item: self._dist_sq(query_vec, item[1]))
        return [{"id": doc_id, "dist_sq": round(self._dist_sq(query_vec, vec), 4)} for doc_id, vec in ranked[:top_k]]
