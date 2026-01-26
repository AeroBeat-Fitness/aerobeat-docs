import os

# Mapping of local documentation paths to their GitHub repositories
PLACEHOLDERS = {
    "docs/api/core": {
        "title": "Core Contracts",
        "repo": "https://github.com/AeroBeat-Workouts/aerobeat-core"
    },
    "docs/api/assembly": {
        "title": "Assembly (Community)",
        "repo": "https://github.com/AeroBeat-Workouts/aerobeat-assembly-community"
    },
    "docs/api/features/boxing": {
        "title": "Boxing Feature",
        "repo": "https://github.com/AeroBeat-Workouts/aerobeat-feature-boxing"
    },
     "docs/api/features/flow": {
        "title": "Flow Feature",
        "repo": "https://github.com/AeroBeat-Workouts/aerobeat-feature-flow"
    },
     "docs/api/features/dance": {
        "title": "Dance Feature",
        "repo": "https://github.com/AeroBeat-Workouts/aerobeat-feature-dance"
    },
     "docs/api/features/step": {
        "title": "Step Feature",
        "repo": "https://github.com/AeroBeat-Workouts/aerobeat-feature-step"
    },
    "docs/api/inputs/keyboard": {
        "title": "Keyboard Input",
        "repo": "https://github.com/AeroBeat-Workouts/aerobeat-input-keyboard"
    },
    "docs/api/inputs/mouse": {
        "title": "Mouse Input",
        "repo": "https://github.com/AeroBeat-Workouts/aerobeat-input-mouse"
    },
    "docs/api/inputs/touch": {
        "title": "Touch Input",
        "repo": "https://github.com/AeroBeat-Workouts/aerobeat-input-touch"
    },
    "docs/api/inputs/gamepad": {
        "title": "Gamepad Input",
        "repo": "https://github.com/AeroBeat-Workouts/aerobeat-input-gamepad"
    },
    "docs/api/inputs/mediapipe_python": {
        "title": "MediaPipe Python Input",
        "repo": "https://github.com/AeroBeat-Workouts/aerobeat-input-mediapipe-python"
    },
    "docs/api/inputs/mediapipe_native": {
        "title": "MediaPipe Native Input",
        "repo": "https://github.com/AeroBeat-Workouts/aerobeat-input-mediapipe-native"
    },
    "docs/api/inputs/joycon": {
        "title": "Joycon Input",
        "repo": "https://github.com/AeroBeat-Workouts/aerobeat-input-joycon-hid"
    },
    "docs/api/assets/prototypes": {
        "title": "Prototype Assets",
        "repo": "https://github.com/AeroBeat-Workouts/aerobeat-asset-prototypes"
    }
}

def main():
    print("Checking for missing documentation placeholders...")
    for path, data in PLACEHOLDERS.items():
        # Ensure directory exists
        os.makedirs(path, exist_ok=True)
        
        index_file = os.path.join(path, "index.md")
        if not os.path.exists(index_file):
            print(f"  + Creating placeholder for: {data['title']}")
            with open(index_file, "w", encoding="utf-8") as f:
                f.write(f"# {data['title']}\n\n")
                f.write("🚧 **Work In Progress**\n\n")
                f.write("This module has not been documented yet.\n\n")
                f.write(f"View the source code on GitHub: [{data['repo']}]({data['repo']})\n")

if __name__ == "__main__":
    main()