# Ardent Nodes for ComfyUI

My first ComfyUI nodes repo, I think it helps me a lot, if you like it, please give it a star.

## Nodes

### FilenamePrefix By Date

This node generates a `filename_prefix` by current date and time

![CleanShot 2025-02-05 at 16 05 52](https://github.com/user-attachments/assets/445fc882-801f-436f-b298-50c625a32d91)

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
