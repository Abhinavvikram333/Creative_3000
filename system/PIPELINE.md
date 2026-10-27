# Production pipeline: script → finished Short (Blender 5.2 + ChatGPT image model)

Written 2026-10-27. This file is the recommendation for automating the series.

It builds on:
- `system/CAMERA_LANGUAGE.md`: camera grammar and Blender recipes
- `system/schema/shot_plan.schema.json`: the contract between stages
- `system/examples/05_shot_plan.json`: video 05 as a valid plan
- `system/STYLE_GUIDE.md` and `system/COLOR_SYSTEM.md` / `color_system.json`: style lock, face system, caption spec and grades, written in parallel
- the research in `system/research/`, cited by file and section rather than repeated

**Constraints:**
- Linux cloud container: no After Effects, no GPU.
- Blender **5.2.x LTS**.
- Assets from the **ChatGPT image model** (`gpt-image-2.5-sunburst` / `-flare`).
- Remotion/ffmpeg are allowed as helpers.
- Audio is not a focus (CLAUDE.md rule 5), but the voiceover drives all timing.

---

## 1. The pipeline at a glance

```
script.md ──► VO (TTS) ──► word timings ──► beats ──► shot_plan.json ──► validate
                                                        │
             ┌──────────────────────────────────────────┤
             ▼                                          ▼
   asset generation (GPT-image 2.5)           camera/face/prop timelines
   masters → heads → emotions/poses             (already in the plan)
   backgrounds, props, unique images
   + face alignment + alpha checks
             │                                          │
             └──────────────► shot rendering ◄──────────┘
                    Blender 5.2 headless, one scene per shot
                    (image planes 2.5D, camera rig, face-sprite swaps,
                     counters/overlays, compositor FX)
                    + I2V only for flagged segments
                                  │
                                  ▼
          assembly: dissolves (4–8 f) + captions + VO  → 720×1280 H.264
                                  │
                                  ▼
          QA: tools/metrics.py on the render vs plan targets / reference
```

The plan is the single source of truth. Every stage reads `shot_plan.json` and writes only to its own output folder, so any stage can be re-run without touching the others.

---

## 2. Folder layout

```
system/
  CAMERA_LANGUAGE.md  PIPELINE.md
  schema/shot_plan.schema.json
  examples/05_shot_plan.json
  prompts/                       # to build: style bibles + prompt templates as files (from research §4–6)
  fonts/                         # Montserrat-Black.ttf (SIL OFL) or Poppins-ExtraBold
library/                         # existing: crops + prompts per CLAUDE.md rule 2/3
  characters/<Name>/
    character.md  reference/  poses/  emotions/        (existing decode crops + prompts)
    generated/                                         # NEW: approved, reusable across videos
      master_front.png  head_neutral.png
      emotions/<emotion>.png  poses/<pose>.png  face_index.json
  backgrounds/ assets_3d/ unique_images/ overlays_ui/  (existing, per source video)
productions/<NN_slug>/                                 # NEW: one folder per Short
  script.md  beats.json
  audio/vo.wav  audio/words.json
  plan/shot_plan.json  plan/history/
  assets/{backgrounds,assets_3d,unique_images,overlays}/<asset_id>.png
  blend/S01.blend …                                    # generated, reproducible (gitignore)
  renders/S01/f_00001.png …                            # with ±4 handle frames (gitignore)
  i2v/<shot>_<a>_<b>.mp4
  captions/captions.ass
  out/<NN_slug>.mp4
  qa/frame_metrics.csv  qa/report.md  qa/grids/sec_000.jpg …
tools/                                                 # existing: extract, metrics, motion, palette, crop
  plan/  assets/  blender/  i2v/  assemble/  qa/       # NEW (see §5)
```

**Where assets live:**
- Character assets go in `library/characters/<Name>/generated/` because characters recur across videos.
- Per-video plates and props go in `productions/<slug>/assets/`.
- The 05 example already points `generated_file` at these locations.

---

## 3. Stages in detail

### 3.1 Script → voiceover → word timings
- **Script rules:**
  - second person ("you"), 3.5–3.6 words/s (05: 3.62 w/s, 04: 3.58 w/s)
  - a hook sentence of 3.5–5.3 s
  - a beat arc hook → escalation ×2–3 → turn → explanation → payoff, with no outro card
  - Templates are in `analysis/videos/*/script.md` §2–4.
- **VO:** use any TTS (out of scope per rule 5). It must exist before planning, because frames come from audio.
- **Word timings:** run WhisperX forced alignment against the known script (`face_animation_github.md` §7). This writes `script.lines[].words[]` and `captions.cards[]`.
- **Card paging:** 1–2 words per card, about 80 % single words, average hold about 10 f, hard cuts, no gaps (measured over all five videos: 95–191 cards per video, median hold 9–10 f).

### 3.2 Beats → `shot_plan.json`
Rules from `CAMERA_LANGUAGE.md` §6–7:
- one shot per 1–2 clauses (2.5–4.5 s)
- 1–2 long explainer shots of 6–9 s with internal camera phases
- transitions within ±6 f of a phrase-opening word
- 75 % of joins are 6-f dissolves; about 1 zoom-through per new "world"
- camera phase changes every 1–1.5 s; the camera is never static for more than about 1.5 s
- a face or prop event on every stressed word

**How the planner works:**
- An LLM fills the plan with these rules in its prompt.
- `tools/plan/validate_plan.py` checks JSON Schema plus semantic rules: frame ranges inside shots, every `asset_id` in the registry, emotions only in visible ranges, captions contiguous, beats covering the whole timeline.
- Choose a `render.mode` per shot:

| Mode | When |
|---|---|
| `blender_2_5d` | Default: image planes, camera rig, face swaps (05 S1–S5) |
| `blender_3d_blockout` | Hinges, wireframes, orbits, crane-to-aerial: a simple box/plane geometry carries the textures (05 S6, S8) |
| `hybrid` + `i2v_segments` | Morphs, walks or falls that cards can't sell (05 S7 #768–778 strip→wheel morph) |
| `remotion_2d` | Optional for pure UI screens / diagrams if Remotion is adopted (open decision §7) |

### 3.3 Asset generation
- **Model and API:**
  - `gpt-image-2.5-sunburst` for masters and backgrounds; `gpt-image-2.5-flare` for emotion, pose and prop variants.
  - Use `images.edits` with saved reference images. There are no seeds; reproducibility comes from references plus a fixed style lock.
  - Transparency only from the 2.5 series; `gpt-image-2` rejects it.
  - All in `chatgpt_image_prompting_2026.md` §1–2.
- **Prompt templates:**
  - Use the `[REFERENCE] [SUBJECT] [POSE / EMOTION / STATE] [STYLE LOCK] [COMPOSITION] [LIGHTING] [BACKGROUND] [AVOID]` blocks already written for every asset in `library/**/*.md`.
  - The registry carries each prompt inline plus a `prompt_ref`; see the 05 example, where 60 of 65 assets have inline prompts.
  - The style lock comes from `meta.style_lock` (each video's `visuals.md`).
  - Templates for new assets are in `chatgpt_image_prompting_2026.md` §4–6.
- **Reference crops:** attach `asset.reference_crops`, the library crops cut from the decoded frames (CLAUDE.md rule 2). Downscale them to about 1024 px to save input tokens (§2 of the same file).
- **Characters (rule 3):**
  1. `master_front.png`: transparent, generated n=4, best one picked and frozen.
  2. `head_neutral.png`: a head-only crop at a fixed canvas and circle diameter.
  3. Each emotion: an edit **from `head_neutral.png` only** (never chained from another emotion), transparent background.
  4. Post-align the head circle (HoughCircles or an alpha fit) to the master's centre and diameter.
  5. Check that alpha contains 0.
  - Recipe: `chatgpt_image_prompting_2026.md` §5 and §6.1–6.2.
  - Write `face_index.json` (emotion → sequence index, anchor px) for the face-swap rig.
- **Backgrounds:**
  - 1152×2048 opaque, clean plates without characters.
  - For pull-backs beyond ×3, use 2160×3840, or generate a **detail inset** plate of the start framing (`CAMERA_LANGUAGE.md` M3, resolution budget).
  - Generate lighting variants as edits of the day/master plate (`chatgpt_image_prompting_2026.md` §6.5).
  - For parallax, split far/mid/near either by generating separate layer plates (machine row, stools) or by using Depth-Anything to cut layers (`face_animation_github.md` §9).
- **Code-built assets, never image-generated:**
  - captions; counters (CREDITS, tally, LED tickers); glints; stamp impact lines; dissolve streaks; dust particles; wireframes
  - These have `generated_file: null` and `generator.endpoint: code|blender` in the registry.
- **Statuses:** `planned → generated → approved/rejected`. Only `approved` assets are rendered. Cache by hashing the prompt and inputs.

### 3.4 Shot rendering (Blender 5.2, headless)
- **Invocation:**
  ```bash
  blender -b --factory-startup --python-exit-code 1 -P tools/blender/build_shot.py -- --plan plan.json --shot S1
  ```
  - Alternatively use `pip install bpy==5.2.3`. The `cp313` manylinux wheel exists, about 400 MB, and downloads in this container, which runs Python 3.13.
  - Render a PNG sequence and mux with system ffmpeg (`blender_5_2_notes.md` §4).
- **Write 5.x-native code:** `strips`, `compositing_node_group`, channelbag F-curves, `media_type` before `FFMPEG` (`blender_5_2_notes.md` §2, §6).
- **Scene build per shot:**
  - **Planes:** build the meshes directly rather than through the import operator (`blender_5_2_notes.md` §3.2). Use an Image Texture → Emission plus Transparent mix with alpha blend, and the Standard view transform so the GPT colours survive.
    - Place each layer at its `transform.depth_m`, sized `height = 36·d/f`, times the shot's overscan.
    - Cards follow their `motion` keys; poses swap per `poses[]`.
  - **Camera:** build the rig from `CAMERA_LANGUAGE.md` §3.1. Bake each `camera.moves[]` per frame in log-zoom space with `bake_move()` (§3.4 there). Use `params` as targets, `zoom_mode` dolly/focal, `pan_mode` translate/rotate, and the `reference_layer` depth. Add DOF, motion blur and Noise modifiers from `params`.
  - **Face sprite swapping:**
    - A head/face plane is parented to the pose card at the pose's `face_anchor_px`.
    - Its Image Texture uses `source='SEQUENCE'` over the character's emotion PNGs, ordered by `face_index.json`.
    - The emotion timeline becomes CONSTANT keys on a custom property `emotion_idx`. A **driver** maps it to `image_user.frame_offset`.
    - `blend_frames > 0` (e.g. 05 #49 manic, #72 smug) uses a second face plane with a 2–3-f opacity cross-blend.
    - `lip_flap` alternates the open and closed emotions with the given hold range (05 Bling: 2–9 f).
    - Planner rule: blinks are exactly 2 f.
    - Fallbacks: per-emotion planes with keyed `hide_render`, or a `frame_change_pre` handler (`blender_5_2_notes.md` §3.2).
  - **Props and overlays:**
    - Counters are text or 7-segment textures driven from `keys[].value`. Use the 5.2 compositor String To Image node or pre-rendered digit sprites.
    - Badges, stamps and imprints are planes that switch on at their key frames.
    - The hinged door is a plane rotated about its edge; the wheel is a disc rotated with `ease_out` to its landing frame; the wireframe is a Wireframe modifier with emission.
  - **VFX:**
    - Compositor node group: Glare for glints and bloom, Blur for the POV blur-out, Mask to SDF for outlines (`blender_5_2_notes.md` §2, §3.4).
    - Dust uses a particle system.
- **Engine:**
  - Cycles CPU, 4–8 samples, denoise, 0 bounces (emission-only planes).
  - EEVEE needs a GPU (`blender_5_2_notes.md` §4).
  - **Render time is untested.** The guess is 1–3 s per frame on this 4-core box, i.e. 15–45 min per 30-s Short.
- **Output:** frames `start − handles … end + handles` (4 f handles) so dissolves overlap moving cameras.
- **I2V segments** (only where `render.i2v_segments` is set):
  1. Render the start frame (and end frame or end asset) from Blender.
  2. Send them with the short motion prompt to the chosen model: Kling 3.0 start+end frame / Veo 3.1 / Seedance 2.0, or self-hosted Wan 2.2 (`toolchain_hypotheses.md` §2 H1, §4; `face_animation_github.md` §9).
  3. Conform to 30 fps and 720×1280.
  4. Overlay code-built captions and counters afterwards, because I2V smears small text (`visuals.md` §2 of 05).

### 3.5 Captions and assembly
- **v1 (fully headless, no Node), recommended to start:**
  - ffmpeg concatenates the shots with `xfade=fade` at each `transition_in.frames` (4–8 f). Hard, jump and match cuts use plain concatenation.
  - Zoom-throughs are already composited inside the shot render.
  - Captions go to an `.ass` file generated from `captions.cards` and `captions.style` (white #f8f7f8, 4–5 px black outline, soft shadow, centre y≈900, cut-on). Burn in with `ffmpeg -vf ass=` (`face_animation_github.md` §7). Then mux the VO.
- **Alternative A, Blender VSE:**
  - An "edit" scene with Scene strips per shot, cross strips or the 5.2 Compositor effect strip for dissolves, and TEXT strips for the cards.
  - Strip API in `blender_5_2_notes.md` §3.5.
  - Everything stays in one tool, but caption styling is harder to match.
- **Alternative B, Remotion:**
  - The best captions, counters and UI layers (`face_animation_github.md` §2, §10).
  - Needs Node (present: `/opt/node22`).
  - The Remotion licence is free only for companies of 3 or fewer people.

### 3.6 QA (compare against measured metrics with `tools/`)
1. `python3 tools/metrics.py <render_dir> productions/<slug>/qa` measures every frame of the output.
2. **Per camera move:** `python3 tools/motion.py qa/frame_metrics.csv range a b`, compared with `camera.moves[].params`.
   - Pass when zoom is within ±5 % and pan within ±30 px.
   - Moves with `measured.reliable:false` are reviewed by eye.
   - The roll sign is checked on the first render (`CAMERA_LANGUAGE.md` §3.2).
3. **Global style stats vs the series** (`CAMERA_LANGUAGE.md` §2, §5–6):
   - share of near-static seconds ≤ 15 %
   - slow-push median 3–7 %/s
   - dissolve length 4–8 f
   - shot-length median 2.5–4.5 s
   - caption hold median 9–10 f and centre y 880–920
4. **Colour:** `tools/palette.py` per shot vs `shot.background.palette`, warning when ΔE > 10.
5. **Rebuilds of an analysed video:** per-second 30-frame grids of render vs reference side by side (`tools/extract.py`). This is the same per-frame review as CLAUDE.md rule 1, checked by a human or an agent.
6. **Assets:** alpha present, head circle within ±2 % of the master, shirt palette (`chatgpt_image_prompting_2026.md` §5 step 6).
7. Write `qa/report.md` with pass/fail per check, linking to the grids.

---

## 4. What can be automated now vs what needs tests first

| Step | Status | Why / what to test |
|---|---|---|
| Plan schema + validation | **Now** | Schema done; 05 example validates (`jsonschema` Draft 2020-12) |
| Decoded video → plan (rebuilds of 01–05) | **Now** | The 05 plan was generated by a script from `shots.json`, the frame-log captions and the `emotions.md` timelines. Promote it to `tools/plan/analysis_to_plan.py` |
| Caption cards → `.ass` → burn-in; ffmpeg dissolves/assembly | **Now** | ffmpeg is installed; deterministic |
| Image generation calls and the registry loop | **Now (needs API key)** | Endpoints and parameters documented; cost per Short unknown, so log tokens |
| Face alignment, alpha and palette checks | **Now** | OpenCV is already used by `tools/metrics.py` |
| QA metrics on renders | **Now** | Reuses `tools/metrics.py`/`motion.py`/`palette.py` unchanged |
| Blender install / headless bpy | **Test** | The `bpy==5.2.3` cp313 wheel is available; run a 1-frame smoke test (planes + emission + Standard) |
| Camera rig + `bake_move` | **Test** | Untested sketch. Render 05 S1 and S4 and compare with `motion.py`; verify the roll and pan signs |
| Face-swap driver on SEQUENCE textures | **Test** | Check `frame_offset` driven per frame in `-b -a` renders; fallback is the handler |
| Cycles CPU render time / quality | **Test** | Measure s/frame at 4–8 samples; decide whether a GPU (EEVEE) is needed |
| GPT-image character consistency across 11 emotions and 10 poses | **Test** | Generate Lenny's set, run the alignment and validation thresholds, and have the owner review |
| Flat cards under orbit / crane-to-aerial / 3D hinge | **Test** | Billboard + pose swap vs simple 3D blockout vs I2V; compare with 02 S4, 04 S2, 05 S6 |
| Big pull-backs (×4) on generated plates | **Test** | 4K plate vs detail inset; check sharpness at f1 |
| I2V segments (morph, walk) | **Test + budget** | Quality, cost and consistency of Kling/Veo/Seedance vs Wan 2.2 on 05 S7 #768–778 and 05 S2's walk |
| LLM planner (beats → plan for a new script) | **Test** | Score drafts with `validate_plan.py` plus the style-stat checks before rendering |

---

## 5. Scripts to build next (in order)

1. `tools/plan/validate_plan.py`: JSON Schema plus semantic lint (frame bounds, asset ids, visibility, caption contiguity, style-stat warnings).
2. `tools/plan/analysis_to_plan.py`: converts a decoded `analysis/videos/<slug>/` into a shot plan. This generalises the script that produced `05_shot_plan.json` to videos 01–04.
3. `tools/blender/camera_rig.py`: the `make_rig` / `bake_move` library from `CAMERA_LANGUAGE.md` §3.4, with the easing table.
4. `tools/blender/build_shot.py`: plan + shot id → .blend + PNG sequence (planes, depth, rig, poses, face-swap driver, props, overlays, compositor FX).
5. `tools/blender/face_rig.py`: emotion timeline → `emotion_idx` constant keys + driver, cross-blend planes, lip flap, auto 2-f blinks.
6. `tools/qa/qa_render.py`: metrics on the render vs plan targets and series stats, written to `qa/report.md`.
7. `tools/qa/compare_reference.py`: per-second side-by-side 30-frame grids of render vs reference for rebuilds.
8. `tools/assets/gen_assets.py`: walks the registry and calls `images.generate/edit` with references; writes `generated_file`, status and a cost log.
9. `tools/assets/align_faces.py`: head-circle detection, normalisation to the master, alpha check, `face_index.json`.
10. `tools/assets/check_assets.py`: size, alpha, palette and identity checks per asset type.
11. `tools/audio/align_words.py`: WhisperX alignment → `script.lines[].words` and 1–2-word `captions.cards`.
12. `tools/assemble/captions_ass.py`: cards + style → `.ass`.
13. `tools/assemble/assemble.py`: shot renders → ffmpeg `xfade`/concat per `transition_in`, burn captions, mux VO → `out/*.mp4`.
14. `tools/i2v/run_segment.py`: start/end frames + prompt → I2V provider → conformed clip spliced into the shot frames.
15. `tools/plan/beats_to_plan.py`: LLM-assisted planner for new scripts. It applies the `CAMERA_LANGUAGE.md` rules and must pass `validate_plan.py`.

**Milestone 1:** scripts 1–7 rebuild video 05 from library crops with placeholder assets (the crops themselves as textures). The camera and timing are then QA'd against the reference before any image spend.

**Milestone 2:** scripts 8–13 generate the real assets and produce a full Short.

---

## 6. How the 05 example maps to the stages
- `script`: 10 narration lines and 112 words, timed from the 95 decoded caption cards. Two-word cards are split evenly until a WhisperX pass replaces them.
- `shots`: the 8 real shots, frame-exact (1–133 … 779–928), with transitions as decoded (jump cut #134, dissolves of 4–6 f, zoom-through #542).
- **Camera:** 19 camera phases with measured `zoom/dx/dy/roll` from `shots.json`. Three polluted phases (S7 #560–640 and #768–778, S8 #800–886) are marked `reliable:false`, with visual-estimate params.
- **Characters:** pose timelines and frame-level emotion timelines for Lenny, Bling and Beanie, copied from `library/characters/*/emotions/emotions.md`.
- **Props, overlays, VFX:** CREDITS 1→100 #404–414, tally x01→x14 at the 14 stamp frames, LED ticker values, glints, x1 badge, door hinge, wheel landing, X-ray fade.
- `assets`: 65 entries pointing at real library crops (all paths verified to exist) and the planned `generated_file` locations.

---

## 7. Open decisions for the owner
1. **Renderer split.** Blender for every shot (one tool, GPL), or Blender for camera shots plus Remotion for UI screens, counters and captions? Remotion is free only for companies of 3 or fewer people.
2. **Assembly and captions.** ffmpeg + ASS (recommended v1), Blender VSE, or Remotion.
3. **I2V policy and budget.** Which shot classes may use I2V (morphs, walks, falls, crane-to-aerial) and which vendor: Kling 3.0 / Veo 3.1 / Seedance 2.0 (commercial) vs self-hosted Wan 2.2 (needs a large GPU).
4. **GPU.** Is a GPU worker available? It decides EEVEE vs Cycles CPU and whether self-hosted I2V is possible.
5. **Fidelity target.** Exact rebuilds of the analysed videos (QA against the reference metrics) as the acceptance test, or straight to new scripts "in the style"?
6. **Faces.** Whole-face sprites per emotion, as now (rule 3), or layered eyes/brows/mouth parts for more combinations? Both fit the swap rig.
7. **Sets.** Pure generated 2.5D plates, or simple 3D blockouts for recurring sets (slot machine, desk, stage) that the plates are projected onto, giving better orbits and hinges?
8. **Image-model budget per Short** and approval flow: who approves masters before variants are generated?
9. **Voice.** Which TTS, and whether WhisperX alignment is acceptable as the timing source.
10. **Higgsfield test.** Run the one-off Explainer test suggested in `toolchain_hypotheses.md` §5 (costs credits)?
11. **Storage.** Where generated PNGs, renders and blends live: git LFS, a bucket, or gitignored with regeneration from the plan.
12. **Next batch.** Videos 6–18 are decoded only after the owner reviews this pilot (CLAUDE.md rule 7).
