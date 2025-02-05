# Ardent ComfyUI

My first ComfyUI nodes repo, I think it will help me a lot, if you like it, please give it a star.

## Nodes

### Format Filename Prefix By Date

- This node generates a `filename_prefix` by current date and time, with an optional seed
- The output **STRING** will be in the format `YYYYMMDD/YYYYMMDD_HHMM` or `YYYYMMDD/YYYYMMDD_HHMM_{seed}`
- The path delimiter will be automatically determined based on the operating system, using either `/` or `\`
