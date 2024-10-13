"""Main."""
import argparse

from gost_distance_calculater import GhostDistanceCalculator


def main() -> None:
    """Parse arguments, calculate ghost distances, and print results."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--board", type=str, help="Path to the board file (.npy)")
    args = parser.parse_args()

    calculator = GhostDistanceCalculator()
    calculator.load_file(file_path=args.board)
    result = calculator.calculate_distances()
    print(result)  # noqa: T201

if __name__ == "__main__":
    main()
