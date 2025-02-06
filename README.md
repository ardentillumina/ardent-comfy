# Ardent Nodes for ComfyUI

My first ComfyUI nodes repo, I think it helps me a lot, if you like it, please give it a star.

## Nodes

### 1. `Show Text`

This node displays a text in a widget with a `text` input.

![CleanShot 2025-02-06 at 23 01 46](https://github.com/user-attachments/assets/a89b5a0b-0e40-4a1e-a1cf-fd0a7a2ecf01)

### 2. `FilenamePrefix By Date`

This node generates a `filename_prefix` by current date and time

![CleanShot 2025-02-06 at 23 03 42](https://github.com/user-attachments/assets/6c1bdc36-d576-4f35-b265-6ef07536ea0f)

- Inputs:
  - `seed`: optional
  - `suffix`: optional
- Outputs:
  - `STRING`:
    - `YYYYMMDD/YYYYMMDD_HHMM`
    - `YYYYMMDD/YYYYMMDD_HHMM_{suffix}`
    - `YYYYMMDD/YYYYMMDD_HHMM_{seed}`
    - `YYYYMMDD/YYYYMMDD_HHMM_{seed}_{suffix}`
- The path delimiter will be automatically determined based on the operating system, using either `/` or `\`
