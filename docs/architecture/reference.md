# Directory Structure Reference

### A. The Core Project (`aerobeat-core`)
```
aerobeat-core/
├── contracts/          # Interfaces (AeroInputStrategy)
├── data_types/         # Resources (AeroSessionContext, BeatData)
├── globals/            # Static Consts (AeroConst, AeroEvents)
└── utils/              # Math Helpers (KalmanFilter)
```

### B. A Feature Project (`aerobeat-feat-input`)
```
aerobeat-input-mediapipe-python/
├── python_mediapipe/       # CV Sidecar Code
├── scripts/
│   ├── strategies/     # Logic Implementation
│   │   ├── strategy_mediapipe.gd
│   │   └── strategy_debug.gd
│   └── input_manager.gd
├── .testbed/           # Ignored Ghost Project
└── plugin.cfg
```

### C. The UI-Kit Project (`aerobeat-ui-kit`)
```
aerobeat-ui-kit/
├── atoms/
│   ├── aero_button/
│   │   ├── AeroButton.tscn
│   │   ├── AeroButton.gd
│   │   └── AeroButton_Test.tscn  <-- The Atomic Test
│   └── aero_slider/ ...
├── molecules/
│   ├── song_card/
│   │   ├── SongCard.tscn         <-- Uses AeroButton + AeroLabel
│   │   └── SongCard_Test.tscn
├── scripts/
│   └── theme_utils.gd            <-- Shared logic
└── sync_manifest.json            <-- Defines exports
```