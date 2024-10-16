import os

def main(hostname, password, search_level):
    # Simulate some processing based on input
    score = calculate_score(search_level)
    log_file_path = create_log_file(hostname, password, score)
    return score, log_file_path

def calculate_score(search_level):
    # Simulate score calculation based on the search level
    return search_level * 250  # Example scoring logic

def create_log_file(hostname, password, score):
    # Define the log file name and path
    log_filename = "analysis_log.txt"
    log_content = f"Hostname: {hostname}\nPassword: {password}\nScore: {score}\n"
    
    # Save the log to the current working directory
    with open(log_filename, "w") as log_file:
        log_file.write(log_content)
    
    return log_filename
