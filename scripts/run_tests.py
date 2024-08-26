import subprocess
import sys
import webbrowser
from pathlib import Path


# Run the tests with coverage
print("Running tests...")
subprocess.run(['coverage', 'run', '-m', 'unittest', 'discover', 'test', '--quiet'], check=True)

# Generate the HTML coverage report and html
print("generating report..")
subprocess.run(['coverage', 'report'], check=True)
print("generating coverage..")
subprocess.run(['coverage', 'html'], check=True)

if '--open' in sys.argv:
    htmldoc_fullpath = Path(Path(__file__).parent.parent, 'htmlcov/index.html')
    webbrowser.open(htmldoc_fullpath)
