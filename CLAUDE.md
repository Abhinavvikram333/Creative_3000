# Creative_3000 — Project Rules

## Goal
Decode the owner's hand-made Shorts style (folders `1/` … `18/`, each with an MP4 + timestamped SRT)
into a reusable system so new videos can be produced automatically
(image-generation models for assets, Blender / After Effects / code for layout, camera and animation).

## Hard rules (set by the owner — do not change without asking)
1. **Analyse every frame at 30 fps. Never use a key-frame / sampling method.**
   Review method: one grid image per second of video (30 frames, numbered), every grid looked at.
2. Asset library = location of the asset in the frame + reference crop + a regeneration prompt
   (ChatGPT latest image model). No manual cut-outs.
3. Faces: each character gets its own folder with an `emotions/` sub-folder; write prompts for the same
   face in each emotion on a transparent background so faces can be swapped.
4. The owner does not disclose how the videos were made — researching the likely toolchain
   (After Effects, Blender, others) and a replication pipeline is part of the task. Use the web; do not rely only on training data.
5. Audio / SFX is not a focus. Voiceover is English; the script comes from the SRT files.
6. Repo may be public — owner knows, do not warn about it again.
7. Work in batches: pilot = videos 1–5. Remaining videos only after the owner reviews the pilot.
8. Develop on branch `claude/loving-ritchie-va4ydw`; never push to `main` without permission.

## Output layout
- `analysis/videos/<NN_slug>/` — per-video report, shot list, beats, camera, colors (Markdown + JSON)
- `library/characters/<Name>/` — character sheet, `poses/`, `emotions/`, prompts
- `library/backgrounds/`, `library/assets_3d/`, `library/unique_images/`, `library/overlays_ui/`
- `system/` — style guide, color system, JSON schema, prompt templates, pipeline research
