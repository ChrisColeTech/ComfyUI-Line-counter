from .line_counter import  NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
import random

tech_rambling = [
    "Beep-boop-a-loop!", "Clickity-clack boom!", "Wires are wiggling!", "Tech magic happening!",
    "Gadget giggles!", "Quantum giggle!", "Data dance-off!", "Binary boogie!"
]

print(f"\033[1;34m[CCTech Suite]: 🤖🤖🤖 \033[96m\033[3m{random.choice(tech_rambling)}\033[0m 🤖🤖🤖")
print(f"\033[1;34m[CCTech Suite]:\033[0m Activated \033[96m{len(NODE_CLASS_MAPPINGS)}\033[0m counter nodes.")

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']


WEB_DIRECTORY = "./web"
