# Copifier
A simple a copying program that allows to copy things into stack !

#### Demo
The link below shows example demo in Youtube. 
[![Watch the video](https://youtu.be/lNGmti2pGqk)


#### Requirements

1. **Operating System Compatibility**:
   - The program should be compatible with common operating systems such as Windows, macOS, and Linux.

2. **Python Version**:
   - The program requires Python 3.x installed on the system.

3. **Python Libraries**:
   - `pyperclip`: Required for accessing the system clipboard.
   - `time`: Standard Python library for time-related functions.
   - `collections`: Standard Python library for data structures. Specifically, `deque` is used.
   - `keyboard`: Required for monitoring keyboard events.

#### Installation Instructions

1. Install Python 3.x from the official Python website or package manager of your operating system.
2. Install required Python libraries using pip:
   ```
   pip install pyperclip keyboard
   ```
   Note: `time` and `collections` are part of the Python standard library and do not require separate installation.

#### Configuration

No specific configuration is required for this program.

#### Running the Program

1. Ensure Python is installed on your system.
2. Install required Python libraries (see Installation Instructions).
3. Run the program by executing the script:
   ```
   python copifier.py
   ```
   Replace `copifier.py` with the actual filename if different.

#### Usage

- Once the program is running, it will continuously monitor the system clipboard.
- Whenever a new item is copied to the clipboard, it will be added to the clipboard history.
- Pressing `Ctrl+V` will paste the last copied item from the history.
- The program can be stopped by pressing `Ctrl+C`.

#### Support

For any issues or questions regarding the program, please create an issue on the project's GitHub repository or reach out to the project maintainers.

#### License

This program is distributed under the MIT License. See the `LICENSE` file for more details.

#### Additional Notes

- Ensure that the program has necessary permissions to access the system clipboard.
- This program is intended for personal use and may require modifications for specific use cases or environments.
