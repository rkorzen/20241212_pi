import sys

from pathlib import Path
import time

if len(sys.argv) < 2:
    directory = Path(".")
else:
    directory = Path(sys.argv[1])


def monitor_directory(directory, interval=0.5):
    """Monitoruje zmiany w katalogu."""
    
    previous_state = set(directory.glob('*'))
    print(f"Monitoring {directory.absolute()}")
    try:
        while True:
            
            time.sleep(interval)
            current_state = set(directory.glob('*'))
            
            # Sprawdzenie zmian
            new_files = current_state - previous_state
            deleted_files = previous_state - current_state
            
            if new_files:
                print("\nNowe pliki lub foldery:")
                for file in new_files:
                    print(f"+ {file.name}")
            
            if deleted_files:
                print("\nUsunięte pliki pliki lub foldery:")
                for file in deleted_files:
                    print(f"- {file.name}")
            
            previous_state = current_state
            
    except KeyboardInterrupt:
        print("\nZakończono monitorowanie")

# Przykład użycia (uruchom w osobnym wątku)
monitor_directory(directory)
