# Ardent Nodes for ComfyUI

My first ComfyUI nodes repo, I think it helps me a lot, if you like it, please give it a star.

## Nodes

### 1. `Show Text`

This node displays a text in a widget with a `text` input.

![CleanShot 2025-02-06 at 13 47 43](https://github.com/user-attachments/assets/3ea06ff8-03a5-44ea-b239-2f9c189ceaa2)


### 2. `FilenamePrefix By Date`

This node generates a `filename_prefix` by current date and time

![CleanShot 2025-02-06 at 13 50 29](https://github.com/user-attachments/assets/b950dee3-cd0e-43c1-b804-45428bb8107f)

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
