#!/usr/bin/env python3
"""Entry point used for the published experiments."""

import argparse
import json


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/default.json")
    args = parser.parse_args()
    with open(args.config, "r", encoding="utf-8") as handle:
        config = json.load(handle)
    print("running experiment with", config)


if __name__ == "__main__":
    main()
