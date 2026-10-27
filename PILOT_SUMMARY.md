# Pilot Summary — videos 1–5 (read this first)

**Status:** pilot complete. Videos 6–18 are waiting for your review (as you asked).
**Method:** every frame at 30 fps — one numbered grid of 30 frames per second of video, every grid looked at.
No key-frame sampling. 5 videos = **6,756 frames, 228 grids, all reviewed** (each video's `frame_log.md` has one entry per second as proof).

---

## 1. Where everything is

| What you asked for | Where to look |
|---|---|
| 1. 3D assets | `library/assets_3d/<video>/index.md` (63 crops + prompts) |
| 2. Backgrounds | `library/backgrounds/<video>/index.md` (61 crops + prompts) |
| 3. Unique images | `library/unique_images/<video>/index.md` (35 crops + prompts) |
| 4. Characters (own folder each) | `library/characters/<Name>/character.md` — 25 characters |
| 5. Character poses | `library/characters/<Name>/poses/` (97 pose crops + prompts) |
| 6. Faces / emotions | `library/characters/<Name>/emotions/` (140 face crops, frame-exact expression timelines, per-emotion prompts) |
| 7. Camera poses & motion | `analysis/videos/<video>/camera.md` + series rules in `system/CAMERA_LANGUAGE.md` (with Blender 5.2 recipes) |
| 8. Script | `analysis/videos/<video>/script.md` |
| 9. Scene-beat scripts | same file, "beats" section + reusable beat template in `system/STYLE_GUIDE.md` §6 |
| 10. Visuals overall | `analysis/videos/<video>/visuals.md` + `system/STYLE_GUIDE.md` |
| 11. Colour style system | `system/COLOR_SYSTEM.md`, `system/color_system.json`, `system/palette_swatches.png` |
| Asset library index | `library/README.md` |
| Frame-by-frame log | `analysis/videos/<video>/frame_log.md` |
| Machine-readable shot list | `analysis/videos/<video>/shots.json`, `assets_index.json` |
| How it was likely made + tools research | `system/research/` (4 files) and `system/STYLE_GUIDE.md` §8 |
| Automation plan | `system/PIPELINE.md` + JSON format `system/schema/shot_plan.schema.json` + worked example `system/examples/05_shot_plan.json` |
| Permanent rules (30 fps, no key frames, etc.) | `CLAUDE.md` |

Video folders: `01_this_tree_hates_you`, `02_your_brains_secret_idea_zone`, `03_why_humans_cant_pick_random_numbers`,
`04_the_scientists_insane_time_test`, `05_the_science_behind_slot_machines`.

---

## 2. Numbers per video

| Video | Frames | Shots | Characters | Emotion crops (main char) | Backgrounds | 3D assets | Unique images | Overlays/VFX |
|---|---|---|---|---|---|---|---|---|
| 01 Tree | 2,043 | 21 | 1 (Kai) | 36 (24 distinct) | 16 | 10 | 4 | 30 |
| 02 Idea Zone | 1,172 | 9 | 2 (Theo, Edison) | 21 | 9 | 11 | 8 | 17 |
| 03 Random Numbers | 1,413 | 12 | 4 (Rico, Marge, Officer Dale, Nina) | 21 (Rico) | 13 | 18 | 9 | 14 |
| 04 Time Test | 1,200 | 10 | 15 (Dex, Dr Klaus, Noggin + cast) | 11 (Dex) | 16 | 11 | 10 | 16 |
| 05 Slot Machines | 928 | 8 | 3 (Lenny, Bling, Beanie) | 11 (Lenny) | 7 | 13 | 4 | 8 |

---

## 3. Your style, decoded (short version)

- **Characters:** one shared body template — big round warm off-white head, dark brown-black outline (~1 % of frame width),
  ~4.2 heads tall, bean/capsule torso, noodle stick limbs with ball hands, no nose/ears. Identity = **hair + clothing**.
  (Video 1 is the outlier: lavender head, navy outline.)
- **Faces:** whole-face swaps, no in-betweens (video 5 has 1–2 soft blend frames). A face holds ~17 frames (median);
  ~20 % are 2–3-frame gag flashes; blinks are ~2 frames. Swaps land on the **first frame of the stressed word**.
  → Recommended system: whole-face transparent sprites, 1024×1024 canvas, head disc 600 px, anchored at centre,
  35 standard emotion names (mapping in `STYLE_GUIDE.md` §3).
- **Camera:** it almost never stops — moving in 89 % of seconds; default is a slow push-in of ~4 % zoom per second.
  Big reveals are S-curve pull-backs/crane-outs. Shots ~3.2 s (median).
- **Transitions:** ~75 % are short dissolves (median 6 frames), ~11 % zoom-throughs (into an eye, a page, a door).
  Almost no hard cuts. Video 4 ends on a seamless loop back to its first frame.
- **Captions:** white, ~4 px black outline, Montserrat Black look, centred at 70 % height, 1–2 words per card, no animation.
- **Pacing:** ~3.55 words/second, 3–5 s hook, second-person storytelling with escalation and a punchline.
- **Colour:** 13 reusable lighting "grades" (day, sunset, night, firelight, casino, underwater, X-ray, thermal, blueprint, …).
  Dark scenes are the most saturated; brightness follows the story beats.

## 4. How it was most likely made (your challenge)

Based on the frame evidence + web research (`system/research/toolchain_hypotheses.md`, `STYLE_GUIDE.md` §8):
- **Backgrounds / sets:** look like AI-generated stills (painterly 2.5D, with correctly spelled in-image text).
- **Big camera moves** (crane-outs, orbits with real perspective change): look like **AI image-to-video**.
- **Character acting:** not fully settled. The instant face swaps and held poses point to **layered compositing
  (After Effects / Blender style, sprite face swaps)**; video 5's soft morphs point to AI video.
- **Captions / dissolves:** an editor with auto word captions.
This is inference from pixels — the files are YouTube re-downloads, so no project metadata survives. Tell me if I'm close!

## 5. Can it be automated?

Yes — `system/PIPELINE.md` lays it out: script → beats → `shot_plan.json` → image generation (prompts + your reference crops,
transparent faces) → Blender 5.2 renders (image planes + camera rig + face-swap) → captions + dissolves (ffmpeg) → QA against
the measured numbers of your real videos. The JSON format already describes video 5 completely and passes validation.
Plan: first **rebuild video 5** from the library and compare it frame-by-frame with your original, then make new videos.

---

## 6. Honest caveats

- Crops are taken from the video, so they include the background behind the character (as you asked: pinpoint + prompt, no cut-outs).
- Some camera numbers are polluted where objects move a lot (flagged `reliable:false` / "direction only" in the files).
- A few faces were tiny or blurred (e.g. Deb in video 4) — marked in the files. Some colour codes are estimates (marked ≈).
- Video 2's agent hit an image-loading limit and had to re-read grids; I verified all 40 seconds are logged and spot-checked
  second 21 against the real frames (it matched; I fixed one missing caption word).
- The Blender camera/face-swap code is a **sketch, not yet tested** (Blender isn't installed here yet; the Blender 5.2.3 Python
  package is installable — that's the first test).
- The latest ChatGPT image model name/parameters came from web search results; verify on first use.
- Character names are my choices — rename freely.

## 7. Decisions I need from you (when you're ready)

1. Approve the pilot format → then I run videos 6–18 the same way.
2. Blender for everything, or Blender + a code tool (Remotion) for captions/UI screens? (`PIPELINE.md` §7 lists 12 decisions;
   the main ones: renderer split, AI-video budget/vendor, GPU availability, fidelity target "rebuild exactly first?").
3. Can I run one paid test on the connected Higgsfield account (its "Stickman Cartoon" explainer preset) to compare with your style?
4. Merge this branch into `main`? (I'll show you the one-click steps.)

## How to view this on GitHub
Open https://github.com/Abhinavvikram333/Creative_3000 → click the branch dropdown (says `main`) → choose
`claude/loving-ritchie-va4ydw` → click `PILOT_SUMMARY.md`. Folders and images open by clicking them.
