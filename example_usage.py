from client import IVFFlatIndex

def main():
    print("=== IVF-Flat Vector Quantization Indexer ===")
    centroids = [
        [0.0, 0.0],
        [10.0, 10.0],
        [-10.0, -10.0]
    ]
    ivf = IVFFlatIndex(centroids)

    ivf.add("item_origin_1", [0.2, 0.1])
    ivf.add("item_origin_2", [-0.1, 0.3])
    ivf.add("item_far_top", [10.2, 9.8])

    results = ivf.search([0.0, 0.0], top_k=2, nprobe=1)
    print("Top-2 Search Results:", results)
    assert len(results) == 2
    assert results[0]["id"] in ("item_origin_1", "item_origin_2")

    print("IVF-Flat Indexer verified successfully!")

if __name__ == "__main__":
    main()
