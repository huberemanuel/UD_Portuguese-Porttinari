import argparse

import conllu
from sklearn.model_selection import train_test_split


def main():
    parser = argparse.ArgumentParser("Split dataset")
    parser.add_argument("data_path", help="Path to raw porttinari-base")
    parser.add_argument("--test_size", default=0.13)
    parser.add_argument("--seed", default=42)
    args = parser.parse_args()
    data = conllu.parse(open(args.data_path, "r").read())
    train, test = train_test_split(
        data, test_size=args.test_size, random_state=args.seed
    )

    with open("porttinari-base-train.conllu", "w") as out_f:
        out_f.writelines([sentence.serialize() + "\n" for sentence in train])
    with open("porttinari-base-test.conllu", "w") as out_f:
        out_f.writelines([sentence.serialize() + "\n" for sentence in test])


if __name__ == "__main__":
    main()
