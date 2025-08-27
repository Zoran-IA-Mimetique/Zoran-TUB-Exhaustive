import json
from typing import Dict

def compute_vx(params: Dict[str, float]) -> Dict[str, float]:
    p = float(params.get("p", 0.5))
    I = float(params.get("I", 5.0))
    E = float(params.get("E", 5.0))
    X = float(params.get("X", 5.0))
    v = float(params.get("v", 5.0))
    R = float(params.get("R", 5.0))
    H = float(params.get("H", 3.0))
    D = float(params.get("D", 5.0))
    K = float(params.get("K", 5.0))
    C = float(params.get("C", 0.7))
    s = float(params.get("s", 50.0))

    raw_num = (p * I) * (1 + E/10) * (1 + X/10) * (1 + v/10) * (1 + R/10) * (1 + H/10)
    raw_den = (1 + D/10) * (1 + K/10)
    Raw = raw_num / raw_den if raw_den != 0 else float("inf")

    V = 100.0 * Raw / (Raw + s) if Raw != float("inf") else 100.0
    V_conf = V * (0.5 + 0.5*C)
    return {"Raw": Raw, "V": V, "V_conf": V_conf}

if __name__ == '__main__':
    example = { "p":0.65,"I":8,"E":9,"X":8,"v":8,"R":6,"H":4,"D":4,"K":5,"C":0.7,"s":50 }
    print(json.dumps(compute_vx(example), indent=2))