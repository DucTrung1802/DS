from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple

# SETTINGS
SEED = 14

POLYNOMIAL_COEFFICIENTS = [-3, -2, 5, 4]
NUM_POINTS = 16
STD_DEV = 0.7


# MODELS
@dataclass
class Point:
    x: float
    y: float

    def round_x(self, ndigits: int = 2):
        return round(self.x, ndigits)

    def round_y(self, ndigits: int = 2):
        return round(self.y, ndigits)


@dataclass
class Polynomial:
    coefficients: List[float]

    def __str__(self):
        return (
            " + ".join(
                (
                    f"{round(coef, 3)}"
                    if degree == 0
                    else (
                        f"{round(coef, 3)}x"
                        if degree == 1
                        else f"{round(coef, 3)}x^{degree}"
                    )
                )
                for degree, coef in zip(
                    range(len(self.coefficients) - 1, -1, -1), self.coefficients
                )
                if coef  # Exclude zero coefficients
            )
            or "0"
        )  # Handle case where all coefficients are zero


# METHODS
def generate_polynomial_points(
    polynomial: Polynomial,
    num_points: int = 16,
    x_range: Tuple[float, float] = [-10, 10],
    y_range: Tuple[float, float] = [-10, 10],
    std_dev: int = 0,
) -> List[Point]:
    """
    Generates points lying on a k-degree polynomial.

    Args:
        coefficients: A list of coefficients for the polynomial,
                      starting with the highest degree term.
                      e.g., [1, -2, 1] represents x^2 - 2x + 1
        num_points: The number of points to generate.
        x_range: A tuple (min_x, max_x) representing the range for x-values.
        y_range: A tuple (min_y, max_y) representing the range for y-values.

    Returns:
        A list of tuples, where each tuple is an (x, y) point.
        Returns None if it's impossible to generate points within the range.
    """

    if num_points < 4:
        raise ValueError("Number of points must be at least 4.")

    min_x, max_x = x_range
    min_y, max_y = y_range

    points: List[Point] = []
    for _ in range(num_points):
        # Try generating points until a valid one is found or a limit is reached
        max_tries = 100  # Avoid infinite loop if range is impossible
        for _ in range(max_tries):
            x = np.random.uniform(min_x, max_x)  # Generate random x within x_range

            noise = 0
            if std_dev:
                noise = np.random.normal(0, std_dev)  # Generate noise

            y = (
                np.polyval(polynomial.coefficients, x) + noise
            )  # Calculate y using polynomial

            if min_y <= y <= max_y:  # Check if y is within y_range
                points.append(Point(x, y))
                break  # Point found, move to the next point
        else:  # No valid point found after max_tries
            return None  # Indicates failure to satisfy range constraints

    return points


def plot_polynomial(
    polynomial: Polynomial,
    x_range: Tuple[float, float] = [-10, 10],
    y_range: Tuple[float, float] = [-10, 10],
    points: List[Point] = None,
    enable_line: bool = True,
    enable_points: bool = True,
):
    if (
        not polynomial
        or not isinstance(polynomial, Polynomial)
        or not polynomial.coefficients
    ):
        return

    # Plot polynomial
    x_plot = np.linspace(x_range[0], x_range[1], 1000)
    y_plot = np.polyval(polynomial.coefficients, x_plot)

    if enable_line:
        plt.plot(x_plot, y_plot, color="red", label="Polynomial")

    # Plot points
    if isinstance(points, List) and len(points) > 0 and enable_points:
        x_scatter = [point.x for point in points]
        y_scatter = [point.y for point in points]
        plt.scatter(x_scatter, y_scatter, color="black")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.xlim(x_range)
    plt.ylim(y_range)
    plt.title("Points on a Polynomial")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def print_template(polynomial: Polynomial, points: List[Point]):
    print_problem(polynomial, points)
    print_solution(polynomial, points)


def print_problem(polynomial: Polynomial, points: List[Point]):

    text = f"Cho {len(points)} điểm dữ liệu: [{', '.join(f"({point.round_x()}, {point.round_y()})" for point in points)}]"
    print(text)

    text = f"Tìm hàm đa thức bậc {len(polynomial.coefficients) - 1} khớp với các điểm dữ liệu nhất."
    print(text)


def solve(polynomial: Polynomial, points: List[Point]):

    # Initialize
    m = len(points)
    n = len(polynomial.coefficients) - 1
    x_0 = np.array([point.x for point in points]).reshape(m, 1)
    b = np.array([point.y for point in points]).reshape(m, 1)

    A = np.ones((m, 1))

    for _ in range(1, n + 1):
        A = np.concatenate([A, x_0**_], axis=1)

    # Step 1: Compute the reduced QR factorization matrix A = Q_hat * R_hat
    Q_hat, R_hat = np.linalg.qr(A, mode="reduced")

    # Step 2: Compute the vector Q_hat_star * b
    Q_hat_star_b = Q_hat.T @ b

    # Step 3: Solve the upper-triangular system R_hat * x = Q_hat_star * b for x
    x = np.linalg.solve(R_hat, Q_hat_star_b)

    # Calculate the residual
    r = float(np.linalg.norm(b - A @ x))

    return (A, b, Q_hat, R_hat, Q_hat_star_b, x[::-1].flatten().tolist(), r)


def print_solution(polynomial: Polynomial, points: List[Point]):

    print(f"\nBài giải:")

    A, b, Q_hat, R_hat, Q_hat_star_b, x, r = solve(polynomial, points)

    print(f"Áp dụng công thức từ hệ Vandermonde:")

    print(
        f"[■(1&x_1&⋯&x_1^(n-1)@1&x_2&⋯&x_2^(n-1)@1&x_3&⋯&x_3^(n-1)@⋮&⋮&⋱&⋮@1&x_m&⋯&x_m^(n-1) )][█(c_0@c_1@⋮@c_(n-1) )]≈[█(y_1@y_2@y_3@⋮@y_m )]"
    )

    print(f"Ta có ma trận A:")

    text_A = ""
    if A.shape[1] == 2:
        text_A = f"A=[■({round(A[0][0], 3)}&{round(A[0][1], 3)}@{round(A[1][0], 3)}&{round(A[1][1], 3)}@⋮&⋮@{round(A[-1][0], 3)}&{round(A[-1][1], 3)} )]"
    elif A.shape[1] == 3:
        text_A = f"A=[■({round(A[0][0], 3)}&{round(A[0][1], 3)}&{round(A[0][2], 3)}@{round(A[1][0], 3)}&{round(A[1][1], 3)}&{round(A[1][2], 3)}@⋮&⋮&⋮@{round(A[-1][0], 3)}&{round(A[-1][1], 3)}&{round(A[-1][2], 3)} )]"
    else:
        text_A = f"A=[■({round(A[0][0], 3)}&{round(A[0][1], 3)}&⋯&{round(A[0][-1], 3)}@{round(A[1][0], 3)}&{round(A[1][1], 3)}&⋯&{round(A[1][-1], 3)}@⋮&⋮&⋱&⋮@{round(A[-1][0], 3)}&{round(A[-1][1], 3)}&⋯&{round(A[-1][-1], 3)} )]"
    print(text_A)

    print(f"Ta có vector b:")

    text_b = ""
    if b.shape[0] == 2:
        text_b = f"b=[█({round(b[0][0], 3)}@{round(b[1][0], 3)} )]"
    if b.shape[0] == 3:
        text_b = f"b=[█({round(b[0][0], 3)}@{round(b[1][0], 3)}@{round(b[2][0], 3)} )]"
    else:
        text_b = (
            f"b=[█({round(b[0][0], 3)}@{round(b[1][0], 3)}@⋮@{round(b[-1][0], 3)} )]"
        )
    print(text_b)

    text = f"Ta có phương trình cần giải:"
    print(text)

    print(f"{text_A[2:]}x={text_b[2:]}")

    print(f"Thực hiện phân tích QR rút gọn ma trận A.\nTính được (□Q) ̂ ")

    text_Q_hat = ""
    if Q_hat.shape[1] == 2:
        text_Q_hat = f"(Q) ̂=[■({round(Q_hat[0][0], 3)}&{round(Q_hat[0][1], 3)}@{round(Q_hat[1][0], 3)}&{round(Q_hat[1][1], 3)}@⋮&⋮@{round(Q_hat[-1][0], 3)}&{round(Q_hat[-1][1], 3)} )]"
    elif Q_hat.shape[1] == 3:
        text_Q_hat = f"(Q) ̂=[■({round(Q_hat[0][0], 3)}&{round(Q_hat[0][1], 3)}&{round(Q_hat[0][2], 3)}@{round(Q_hat[1][0], 3)}&{round(Q_hat[1][1], 3)}&{round(Q_hat[1][2], 3)}@⋮&⋮&⋮@{round(Q_hat[-1][0], 3)}&{round(Q_hat[-1][1], 3)}&{round(Q_hat[-1][2], 3)} )]"
    else:
        text_Q_hat = f"(Q) ̂=[■({round(Q_hat[0][0], 3)}&{round(Q_hat[0][1], 3)}&⋯&{round(Q_hat[0][-1], 3)}@{round(Q_hat[1][0], 3)}&{round(Q_hat[1][1], 3)}&⋯&{round(Q_hat[1][-1], 3)}@⋮&⋮&⋱&⋮@{round(Q_hat[-1][0], 3)}&{round(Q_hat[-1][1], 3)}&⋯&{round(Q_hat[-1][-1], 3)} )]"
    print(text_Q_hat)

    print(f"Tính được (R) ̂ ")

    text_R_hat = ""
    if R_hat.shape[0] == 2:
        text_R_hat = f"(R) ̂ =[█({round(R_hat[0][0], 3)}@{round(R_hat[1][0], 3)} )]"
    if R_hat.shape[0] == 3:
        text_R_hat = f"(R) ̂ =[█({round(R_hat[0][0], 3)}@{round(R_hat[1][0], 3)}@{round(R_hat[2][0], 3)} )]"
    else:
        text_R_hat = f"(R) ̂ =[█({round(R_hat[0][0], 3)}@{round(R_hat[1][0], 3)}@⋮@{round(R_hat[-1][0], 3)} )]"
    print(text_R_hat)

    if Q_hat_star_b.shape[0] == 2:
        text_Q_hat_star_b = f"→(Q) ̂^* b=[█({round(Q_hat_star_b[0][0], 3)}@{round(Q_hat_star_b[1][0], 3)} )]"
    if Q_hat_star_b.shape[0] == 3:
        text_Q_hat_star_b = f"→(Q) ̂^* b=[█({round(Q_hat_star_b[0][0], 3)}@{round(Q_hat_star_b[1][0], 3)}@{round(Q_hat_star_b[2][0], 3)} )]"
    else:
        text_Q_hat_star_b = f"→(Q) ̂^* b=[█({round(Q_hat_star_b[0][0], 3)}@{round(Q_hat_star_b[1][0], 3)}@⋮@{round(Q_hat_star_b[-1][0], 3)} )]"
    print(text_Q_hat_star_b)

    print(f"=> Có phương trình:")
    print(f"(R) ̂ x=(Q) ̂^* b")
    print(f"→x=[█({"@".join([str(round(x_coe, 3)) for x_coe in x])} )]")

    solution_polynomial = Polynomial(x)
    print(f"Ta có đa thức: f(x)={str(solution_polynomial)}")

    print(f"Ta có hình vẽ:")
    plot_polynomial(polynomial=solution_polynomial, points=points, y_range=(-10, 10))


def main():
    np.random.seed(SEED)

    polynomial = Polynomial(POLYNOMIAL_COEFFICIENTS)
    points = generate_polynomial_points(
        polynomial=polynomial, num_points=NUM_POINTS, std_dev=STD_DEV
    )

    # plot_polynomial(
    #     polynomial=polynomial, points=points, y_range=(-10, 10), enable_line=False
    # )

    print_template(polynomial, points)


if __name__ == "__main__":
    main()
