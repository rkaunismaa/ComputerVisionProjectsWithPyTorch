def main() -> None:
    """Main function."""
    parser = argparse.ArgumentParser(
        description="Generate a list of all the files in a directory tree."
    )
    parser.add_argument(
        "path",
        metavar="PATH",
        type=str,
        help="The path to the