## File Integrity Monitoring Script
This Python script provides tools to efficiently check the integrity of files within a directory by comparing their hashes against a known list of valid hashes.

### Features

Calculates MD5 hashes for file integrity verification.
Recursively scans specified directories.
Loads valid hashes from an external file for comparison.
Includes robust error handling for common file exceptions (permission errors, file not found, etc.).
Monitors its own memory usage and provides warnings if a threshold is exceeded.
Prints informative progress updates during execution.
Usage

Clone this repository.

Install required modules: pip install hashlib psutil

Create a text file containing known valid MD5 hashes (one hash per line)
or download from http://virusshare.com/hashes

Execute the script:

Bash
python file_integrity_checker.py <directory_to_scan> <hash_file_path>
Use code with caution.
Example

Bash
python file_integrity_checker.py /home/user/documents /path/to/valid_hashes.txt
Use code with caution.
Customization

The MEMORY_THRESHOLD_MB variable within the script can be adjusted to control when memory usage warnings are triggered.
Applications

Malware detection (by comparing against a database of known malware signatures)
Intrusion detection on critical system files
Forensic analysis to ensure the integrity of collected evidence
License

This project is licensed under the GNU General Public License v3.0. See the LICENSE file for details.

Contributions

Contributions and suggestions are welcome! Feel free to open issues or submit pull requests.

Additional Notes

## Malware Scanning: Suggested Locations & Precautions

**Focus Areas:**

* **Downloads:** `/home/your_user/Downloads` – Common location for downloaded files.
* **Temporary  Files:** `/tmp` – Potential location for malicious files.
* **Web Server Content:** `/var/www` (or your web server's directory) – Critical for web server security.
* **External Storage:**  `/mnt` or `/media` –  Mounted drives often contain shared files.

**Precautions:**

* **Be cautious:** Avoid system-critical directories (like /bin, /sbin, /lib, /usr, and /etc) unless you're absolutely sure about what you're doing, as false positives or accidental modifications in these areas can destabilize your system.
* **Run as a regular user:** Running the script as a regular user (as opposed to root) minimizes the risk of accidental damage to system-critical files.
* **Backup important data:** Always ensure you have up-to-date backups of important data before running such scripts, especially if they might modify or remove files.
* **Update your hash database:** Ensure that the database of malicious hashes you're using is up-to-date to increase the chances of detecting recent malware.

_Remember, using hash-based detection is just one part of a comprehensive security strategy. Malware authors frequently modify their creations to evade such detection, so consider using additional security measures and practices alongside hash checks._
