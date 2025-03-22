# Bacon Cipher Decoder

A Python script to decode text encoded using Bacon's Cipher. Bacon's Cipher is a steganographic method of hiding messages using two different typefaces or symbols. This tool supports decoding messages encoded with the standard Bacon Cipher.

## Features
- Decodes text encoded with Bacon's Cipher.
- Supports both uppercase and lowercase letters.
- Handles non-alphabet characters (e.g., spaces, punctuation) gracefully.
- Debug mode for troubleshooting.
- Input can be provided via a file or directly from the command line.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/bacon-cipher-decoder.git
   cd bacon-cipher-decoder
   ```

2. **Ensure Python is installed**:
   This script requires Python 3.x. You can check your Python version by running:
   ```bash
   python --version
   ```

3. **Install dependencies**:
   No external dependencies are required. The script uses only the Python standard library.

## Usage

### Command Line Arguments
The script accepts the following arguments:
- `--file`: Path to a file containing the cipher text.
- `--text`: Cipher text provided directly from the command line.
- `--debug`: Enable debug mode to print intermediate steps.

### Examples

1. **Decode from a file**:
   ```bash
   python bacon_decoder.py --file encrypted.txt --debug
   ```

2. **Decode from command line input**:
   ```bash
   python bacon_decoder.py --text "AABBA AABBB ABAAA" --debug
   ```

3. **Decode without debug mode**:
   ```bash
   python bacon_decoder.py --file encrypted.txt
   ```

### Input Format
- The input text should consist of groups of 5 `A` or `B` characters (case-insensitive).
- Non-alphabet characters (e.g., spaces, punctuation) are preserved in the output.

### Output
The decoded text is printed to the console.

## Example

### Input File (`encrypted.txt`):
```
AABBB AABAA ABABB ababb abbba! This is a test.
```

### Command:
```bash
python bacon_decoder.py --file encrypted.txt --debug
```

### Output:
```
Cipher Groups: ['AABBB', ' ', 'AABAA', ' ', 'ABABB', ' ', 'ababb', ' ', 'abbba', '!', ' ', 'T', 'h', 'i', 's', ' ', 'i', 's', ' ', ' ', 't', 'e', 's', 't', '.']
Decoded Text: H E L l o! This is  test.
```

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request. 

---

Enjoy decoding messages with Bacon's Cipher! 🥓
