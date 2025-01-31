Basically I first cloned it and did the code work in my vscode but it was written there to fork and use it so i uploded my code and output here.
# Solution Considered
- Reads line-by-line.
- linear scan
   
# Final Solution Summary
- Used Python file streaming to handle large files.
- Efficient filtering using .startswith(date).
- minimal RAM usage

# Steps to Run
- fork the repo.
- download the logs using the link given.
- imported sys and os (for no compatiblity issue).
- run the script: python src/extract_logs.py YYYY-MM-DD.
- find logs in output/output_YYYY-MM-DD.txt.
