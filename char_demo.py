import os
import sys
import time

# Stick Figures 
FRAME_1 = """
   o
  /|\\
  / \\
"""

FRAME_2 = """
  \\o/
   |
  / \\
"""

FRAME_3 = """
  ~o~
   |
  / \\
"""

FRAME_4 = """
  _o_
  \\|/
  / \\
"""

def clear_terminal():
    """Clears the console screen across Windows, Mac, and Linux."""
    os.system("cls" if os.name == "nt" else "clear")

def dance_routine(duration_seconds=10, speed=0.3):
    """Loops through the ASCII frames to animate the character."""
    frames = [FRAME_1, FRAME_2, FRAME_3, FRAME_4]
    end_time = time.time() + duration_seconds
    
    time.sleep(1.5)
    
    try:
        while time.time() < end_time:
            for frame in frames:
                clear_terminal()
                print("\n" * 5) 
                print(frame)
                time.sleep(speed)
                
        clear_terminal()
        print("\n\n   o_/\n   |\n  / \\")
        
    except KeyboardInterrupt:
        clear_terminal()
        print("\nDance interrupted!")

if __name__ == "__main__":
    dance_routine(duration_seconds=4, speed=0.25)

