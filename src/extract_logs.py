import sys
import os

def extract_logs(date, log_file="logs_2024.log", output_dir="output"):
    output_file = os.path.join(output_dir, f"output_{date}.txt")
    try:
        with open(log_file, "r") as f, open(output_file, "w") as out:
            for line in f:
                if line.startswith(date):
                    out.write(line)
        
        print(f"Logs extracted to: {output_file}")
    except FileNotFoundError:
        print("Log file not found. Download it first.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py YYYY-MM-DD")
        sys.exit(1)

    extract_logs(sys.argv[1])
