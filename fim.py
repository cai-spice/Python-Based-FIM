import hashlib
import os

# check if file exists

def calculate_file_hash(filepath):
    if not os.path.exists(filepath):
        return None

# read files contents and generate secure hash

    with open(filepath, "rb") as f:
        file_bytes = f.read()
        file_hash = hashlib.sha256(file_bytes).hexdigest()

    return file_hash

# save original hash, check integrity, and output verdict to user

def run_monitor():
    target_file = "important_document.txt"
    baseline_file = "hash_baseline.txt"

    print("----File Integrity Monitor----")
    choice = input("Type '1' to set baseline or type '2' to check integrity: ")

    if choice == "1":
        current_hash = calculate_file_hash(target_file)
        if current_hash:
            with open(baseline_file, "w") as f:
                f.write(current_hash)
            print(f"[-] Baseline set successfully for {target_file}.")

        else:
            print(f"[-] Error: {target_file} not found.")
        
    elif choice == "2":
        if not os.path.exists(baseline_file):
            print(f"Error: No baseline found. Run option 2 first.")
            return

        with open(baseline_file, "r") as f:
            saved_hash = f.read().strip()

        current_hash = calculate_file_hash(target_file)

        if current_hash == saved_hash:
            print("SAFE: File has not been modified.")

        else:
            print("ALERT: File has been MODIFIED!")

    else: 
        print("Invalid choice")

if __name__ == "__main__":
    run_monitor()
