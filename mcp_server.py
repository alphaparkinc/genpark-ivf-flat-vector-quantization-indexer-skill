import sys
import json
from client import IVFFlatIndex

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "search":
        ivf = IVFFlatIndex(params.get("centroids", [[0, 0]]))
        for item in params.get("items", []):
            ivf.add(item["id"], item["vec"])
        return {"results": ivf.search(params.get("query", [0, 0]), top_k=params.get("top_k", 2))}
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
