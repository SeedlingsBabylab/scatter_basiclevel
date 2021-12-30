# Do not use!

Use `scatterbl.py` from the [scatter](https://github.com/SeedlingsBabylab/scatter) repo. See instructions [here](https://bergelsonlab.gitbook.io/blab/data-pipeline/scatter).

# Outdated

## scatter_basiclevel


This script takes a folder with all basic level files in it, and sends them back to their correct location in
Subject_Files

### usage

```
$: python scatterbl.py  folder_with_all_bl_files  path_to_subject_files  [--audio] [--video]
```

The --audio and --video flags tells the script whether this folder has all audio files in it, or all video files.
This determines where they'll end up in Subject_Files. You have to choose either/or. Can't have both.


