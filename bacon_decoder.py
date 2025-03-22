import sys
import re
import argparse

# Bacon Cipher dictionary
BACON_DICT = {
    'AAAAA': 'A', 'AAAAB': 'B', 'AAABA': 'C', 'AAABB': 'D', 'AABAA': 'E',
    'AABAB': 'F', 'AABBA': 'G', 'AABBB': 'H', 'ABAAA': 'I', 'ABAAB': 'J',
    'ABABA': 'K', 'ABABB': 'L', 'ABBAA': 'M', 'ABBAB': 'N', 'ABBBA': 'O',
    'ABBBB': 'P', 'BAAAA': 'Q', 'BAAAB': 'R', 'BAABA': 'S', 'BAABB': 'T',
    'BABAA': 'U', 'BABAB': 'V', 'BABBA': 'W', 'BABBB': 'X', 'BBAAA': 'Y',
    'BBAAB': 'Z',
    'aaaaa': 'a', 'aaaab': 'b', 'aaaba': 'c', 'aaabb': 'd', 'aabaa': 'e',
    'aabab': 'f', 'aabba': 'g', 'aabbb': 'h', 'abaaa': 'i', 'abaab': 'j',
    'ababa': 'k', 'ababb': 'l', 'abbaa': 'm', 'abbab': 'n', 'abbba': 'o',
    'abbbb': 'p', 'baaaa': 'q', 'baaab': 'r', 'baaba': 's', 'baabb': 't',
    'babaa': 'u', 'babab': 'v', 'babba': 'w', 'babbb': 'x', 'bbaaa': 'y',
    'bbaab': 'z'
}

def decode_bacon_cipher(cipher_text, debug=False):
    """
    Decodes a given cipher text using Bacon's Cipher.
    
    :param cipher_text: The text to decode.
    :param debug: If True, prints debug information.
    :return: The decoded text.
    """
    # Split cipher_text into groups of five characters, preserving non-alphabet characters
    cipher_groups = re.findall(r'[ABab]{5}|[^ABab]', cipher_text)

    if debug:
        print(f"Cipher Groups: {cipher_groups}")

    # Decode each group
    decoded_text = ''.join([BACON_DICT.get(group, group) for group in cipher_groups])

    if debug:
        print(f"Decoded Text: {decoded_text}")

    return decoded_text

def read_file(file_path):
    """
    Reads the content of a file.
    
    :param file_path: Path to the file.
    :return: The content of the file.
    :raises: FileNotFoundError if the file does not exist.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")

def main():
    parser = argparse.ArgumentParser(description="Decode Bacon's Cipher.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--file', dest='file_path', help="Path to the encrypted text file.")
    group.add_argument('--text', dest='cipher_text', help="Encrypted text directly from command line.")
    parser.add_argument('--debug', action='store_true', help="Enable debug mode.")
    args = parser.parse_args()

    try:
        if args.file_path:
            cipher_text = read_file(args.file_path)
        else:
            cipher_text = args.cipher_text.strip()

        decoded_text = decode_bacon_cipher(cipher_text, args.debug)
        print(decoded_text)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
