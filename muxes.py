def mux4(A: int, B: int, C: int, D: int, S0: int, S1: int) -> int:
    return (
        (A & (S1 ^ 1) & (S0 ^ 1)) |
        (B & (S1 ^ 1) & S0) |
        (C & S1 & (S0 ^ 1)) |
        (D & S1 & S0)
    )

def mux3(A: int, B: int, C: int, S0: int, S1: int) -> int:
    return (
        (A & (S1 ^ 1) & (S0 ^ 1)) |
        (B & (S1 ^ 1) & S0) |
        (C & S1 & (S0 ^ 1))
    )

def mux2(A: int, B: int, S0: int) -> int:
    return (
        (A & (S0 ^ 1)) |
        (B & S0)
    )