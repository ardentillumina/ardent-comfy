# Ardent Nodes for ComfyUI

My first ComfyUI nodes repo, I think it helps me a lot, if you like it, please give it a star.

## Nodes

### Filename Prefix By Date

- This node generates a `filename_prefix` by current date and time
- Inputs:
  - `seed`: optional
  - `suffix`: optional
- Output:
  - `STRING`:
    - `YYYYMMDD/YYYYMMDD_HHMM`
    - `YYYYMMDD/YYYYMMDD_HHMM_{suffix}`
    - `YYYYMMDD/YYYYMMDD_HHMM_{seed}`
    - `YYYYMMDD/YYYYMMDD_HHMM_{seed}_{suffix}`
- The path delimiter will be automatically determined based on the operating system, using either `/` or `\`
