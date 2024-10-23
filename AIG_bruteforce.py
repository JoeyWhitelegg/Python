'''
Forage AIG Cybersecurity Program
Bruteforce starter template
'''

from zipfile import ZipFile
import sys

# Use a method to attempt to extract the zip file with a given password
def attempt_extract(zf_handle, password):
    try:
        # Attempt to extract the zip file using the current password
        zf_handle.extractall(pwd=password)
        print(f"[+] Password found: {password.decode('utf-8')}") 
        return True # Password is correct
    except RuntimeError as e:
        # Raised when the password is incorrect
        return False # Incorrect password
    except Exception as e:
        # Handle other potential exceptoins, Like a bad zip file
        print(f"[-] Error occurred: {e}")
        return False

def main():
    print("[+] Beginning bruteforce ")
    with ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'rb') as f:
            # Write your logic here...
            # Iterate through password entries in rockyou.txt
            for line in f:
                password = line.strip() # Strip any extra spaces/newlines
                

                # Attempt to extract the zip file using each password
                if attempt_extract(zf, password):
                    # If password is found, break out of the Loop
                        break
            else:
                # If no password was successful
                print("]+] Password not found in list")

            # Handle correct password extract versus incorrect password attempt)

    #print("[+] Password not found in list")

if __name__ == "__main__":
    main()