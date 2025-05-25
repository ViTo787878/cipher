import argparse
from pathlib import Path
from subcipher.analysis import get_bigrams, transition_matrix
from subcipher.cipher import substitute_decrypt
from subcipher.utils import load_textfile, normalize_text, save_textfile, log_to_percentage
from subcipher.mh_solver import metropolis_hastings
from subcipher.constants import ALPHABET


def main():
    parser = argparse.ArgumentParser(description='SubCipher - Substitution Cipher Analysis Tool')
    parser.add_argument('--input', '-i', type=str, help='Path to encrypted file')
    parser.add_argument('--reference', '-r', type=str,
                        default="data_samples/krakatit.txt",
                        help='Path to reference file for bigram matrix creation')
    parser.add_argument('--all', '-a', action='store_true',
                        help='Process all sample files in data_samples/encrypted')

    args = parser.parse_args()

    # Load and prepare reference text
    try:
        reference_text = load_textfile(args.reference)
        normalized_ref = normalize_text(reference_text)
        bigrams = get_bigrams(normalized_ref)
        bigram_matrix = transition_matrix(bigrams, ALPHABET)
    except Exception as e:
        print(f"Error preparing reference data: {str(e)}")
        return

    if args.all:
        encrypted_dir = Path("data_samples/encrypted")
        if not encrypted_dir.exists():
            print(f"Directory {encrypted_dir} does not exist!")
            return

        for file in encrypted_dir.glob("text_*_sample_*_ciphertext.txt"):
            print(f"\nProcessing file: {file.name}")
            try:
                ciphertext = load_textfile(str(file))
                best_key, best_score = metropolis_hastings(ciphertext, bigram_matrix)
                plaintext = substitute_decrypt(ciphertext, best_key)

                output_dir = Path("output")
                save_textfile(plaintext, output_dir / f"{file.stem}_plaintext.txt")
                save_textfile(best_key, output_dir / f"{file.stem}_key.txt")

                print(f"Successfully decrypted:")
                print(f"Key: {best_key}")
                print(f"Score: {log_to_percentage(best_score):.2f}%")
                print(f"Text (first 100 characters):")
                print(plaintext[:100] + "..." if len(plaintext) > 100 else plaintext)
            except Exception as e:
                print(f"Error processing file {file.name}: {str(e)}")
                continue

    elif args.input:
        try:
            ciphertext = load_textfile(args.input)
            best_key, best_score = metropolis_hastings(ciphertext, bigram_matrix)
            plaintext = substitute_decrypt(ciphertext, best_key)

            output_dir = Path("output")
            input_file = Path(args.input)
            save_textfile(plaintext, output_dir / f"{input_file.stem}_plaintext.txt")
            save_textfile(best_key, output_dir / f"{input_file.stem}_key.txt")

            print(f"\nSuccessfully decrypted:")
            print(f"Key: {best_key}")
            print(f"Score: {log_to_percentage(best_score):.2f}%")
            print(f"Decrypted text:")
            print(plaintext)
        except Exception as e:
            print(f"Error processing file: {str(e)}")
    else:
        print("You must specify either --input for a single file or --all for processing all sample files")
        parser.print_help()


if __name__ == "__main__":
    main()