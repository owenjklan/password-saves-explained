#!/usr/bin/env python3

levels = {
    0x0000: 0,      # Level 1
    0x4775: 1,      # Level 2
    0x18b3: 2,      # Level 3
    0xF83B: 3,      # Level 4
}

pwd_alphabet_to_char = {
    0x0: "A",
    0x1: "B",
    0x2: "C",
    0x3: "F",
    0x4: "H",
    0x5: "I",
    0x6: "J",
    0x7: "L",
    0x8: "M",
    0x9: "O",
    0xA: "P",
    0xB: "S",
    0xC: "T",
    0xD: "V",
    0xE: "X",
    0xF: "Z",
}

pwd_alphabet_to_bin = {
    "A": 0x0,
    "B": 0x1,
    "C": 0x2,
    "F": 0x3,
    "H": 0x4,
    "I": 0x5,
    "J": 0x6,
    "L": 0x7,
    "M": 0x8,
    "O": 0x9,
    "P": 0xA,
    "S": 0xB,
    "T": 0xC,
    "V": 0xD,
    "X": 0xE,
    "Z": 0xF,
}


def decode_password_string(password: str) -> None:
    in_password = password[0:4]
    print(password, " -> ", in_password)
    password_int = 0

    for i in range(0, len(password)):
        # byte_mask = (1 << (i * (4 + 1)) + 4) - 1
        # print(f"Byte mask: {byte_mask:b}")
        print(f"i = {i}")
        password_int += (pwd_alphabet_to_bin[password[i]] << (i * 4))

    print(f"Final password int:  {password_int:04x}")

    message = f"Level {levels[password_int] + 1} unlocked!" if password_int in levels else "Unknown key!"
    print(message)


def decode_password_string_with_score(password: str):
    in_password = password[0:4]
    score_string = password[4:8]
    password_int = 0
    print(f"(w/ Score): score string: {score_string}")

    for i in range(0, len(in_password)):
        # byte_mask = (1 << (i * (4 + 1)) + 4) - 1
        # print(f"Byte mask: {byte_mask:b}")
        print(f"i = {i}")
        password_int += (pwd_alphabet_to_bin[in_password[i]] << (i * 4))

    print(f"(w/ Score): Final password int:  {password_int:04x}")

    score_int = 0
    for i in range(0, len(score_string)):
        # byte_mask = (1 << (i * (4 + 1)) + 4) - 1
        # print(f"Byte mask: {byte_mask:b}")
        score_int += (pwd_alphabet_to_bin[score_string[i]] << (i * 4))

    level_message = f"Level {levels[password_int] + 1} unlocked!" if password_int in levels else "Unknown key!"
    message = f"Score: {score_int * 100}"
    print(f"{level_message}. Starting {message}")


def main():
    decode_password_string("FSMB")
    decode_password_string("AAAA")
    decode_password_string("BBBB")

    decode_password_string_with_score("SFMZAHIA")


if __name__ == "__main__":
    main()
