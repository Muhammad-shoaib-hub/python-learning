# ==========================================
# DAY 78: ARGPARSE - TOY CAR CLI
# ==========================================

import argparse

# 1. MAKE THE RECEIVER (The Box)
# You create a parser object to hold all your commands.

parser = argparse.ArgumentParser(description="My Toy Car controller ")

# 2. DEFINE THE BUTTONS (The Flags)
# You tell Python what options the user is allowed to pass.

# very very important part

parser.add_argument("--color", type=str, default="red", help="color of the Car")
parser.add_argument("--speed", type=int, default=5, help="speed from 1 to 10")

# 3. CATCH THE COMMANDS (Read the remote control)
# Python grabs whatever you typed in the terminal!

args = parser.parse_args()

# NOW USE THEM!

print(f"🏎️ Driving a {args.color} car at speed {args.speed}!")




