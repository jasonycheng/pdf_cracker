import pikepdf
from tqdm import tqdm

def pdf_crack(pdf_file, passwords):
# iterate over passwords
# load password list
    passwords = [ line.strip() for line in open("pwdlist.txt") ]
    for password in tqdm(passwords, "Decrypting PDF"):
        try:
        # open PDF file
            with pikepdf.open(pdf_file, password=password) as pdf:
            # Password decrypted successfully, break out of the loop
                print("[+] Password found:", password)
            break
        except pikepdf._qpdf.PasswordError as e:
        # wrong password, just continue in the loop
            continue

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="PDF Bruteforce Python script.")
    parser.add_argument("-f", "--pdf_file", help="Filename of PDF to bruteforce.")
    parser.add_argument("-P", "--passlist", help="File that contain password list in each line.")

    # parse passed arguments
    args = parser.parse_args()
    host = args.pdf_file
    passlist = args.passlist
    # read the file
    pdf_crack(host, passlist)
