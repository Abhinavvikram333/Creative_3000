# How were these Shorts most likely made? Toolchain hypotheses (Oct 2026)

Researched 2026-10-27. Web sources are cited inline and listed at the end. Reddit, YouTube watch pages, blender.org and adobe.com could not be fetched from this sandbox, so community evidence comes from web-search extracts and GitHub.

**Bottom line**
- The strongest evidence points to an **AI pipeline**:
  - character-consistent AI **still images** (painterly backgrounds plus bean-head characters)
  - animated shot by shot with an **AI image-to-video model**
  - assembled in an editor with **dissolves**, **auto word-by-word captions** and an **AI voice**
- This may come from an all-in-one "faceless explainer" product. Higgsfield Explainer even ships a 9:16 **"Stickman Cartoon"** preset.
- Classic After Effects or Blender character rigging is possible for a few simpler shots, but it is **not** the main engine.
- For *our* automated replication, I recommend a **hybrid**:
  - GPT-image 2.5 assets
  - deterministic 2.5D shots rendered in code (Remotion; Blender 5.2 where real parallax is needed)
  - AI image-to-video only for shots with complex motion
  - WhisperX-timed captions

---

## 1. Forensic evidence from the sample files (spot checks)

> These are *toolchain* spot checks: contact sheets plus a few consecutive-frame strips and ffmpeg scene detection. They do **not** replace the per-frame 30 fps review required by CLAUDE.md rule 1. Reproduce with `ffmpeg -i in.mp4 -vf "select='not(mod(n,4))',scale=180:320,tile=8x4" -frames:v 1 sheet.jpg`.

| # | Observation | Where | What it implies |
|---|---|---|---|
| E1 | All 18 MP4s: H.264 Main, 720×1280, 30 fps, AAC 44.1 kHz, about 1.0–1.4 Mb/s. `handler_name = "ISO Media file produced by Google Inc."`, `encoder = Lavf60.16.100` | `ffprobe` on all files | These are **YouTube re-downloads** (yt-dlp/ffmpeg remux). **No authoring metadata survives**, so the toolchain must be inferred from the pixels |
| E2 | The SRTs are YouTube-transcript style: line-level `[hh:mm:ss]` stamps every 1–2 s and tags like `[music]` | `1/SRT.txt`, `3/srt.txt` | Not exported from the editor. Word timing must be re-derived (WhisperX) |
| E3 | Video 1, 0–4 s: the character **walks, sits down with smooth in-betweens, then falls over** and the head detaches. Then one **continuous camera crane pull-back** from the beach tree to an aerial island view with **full perspective change** of sand, sea and foliage | `1/This Tree Hates You.mp4`, frames 1–120 | Smooth organic in-betweens plus a continuous 3D move over a *painted* world is the signature of **AI image-to-video**. A 2.5D layer setup can't change the perspective of a painted plate, and a rigged character in AE would show rigid pinned parts |
| E4 | Close-up of the red-faced character: the **smoke puffs "boil"/morph every frame**, the face lines jitter slightly, and a ~5-frame **cross-dissolve** leads into the X-ray screen | video 1, frames 1200–1223 | Per-frame morphing is typical of generative video. The dissolve is an editor transition |
| E5 | Burglar shot: the camera arcs around the couch with **true 3D perspective change** of the furniture and a ruler on the floor. In the living-room shot the dolly-in shows parallax, and the cat changes shape and scale slightly over the move | `12/The Burglar…`, ~3.5–7.5 s | Same as E3: AI video. Painted 2D plates with perspective re-projection and slight identity drift |
| E6 | **Very few hard cuts.** ffmpeg `scene>0.15` finds only 2 events in video 1 (68 s), both at 7.5 s; `scene>0.25` finds 0 in videos 1 and 12 and 1 in video 3 | ffmpeg `select=gt(scene,…)` | Shots are joined by **short dissolves** or continuous AI camera moves rather than hard cuts. The "cut every 1–3 s" feel comes from dissolves and in-clip camera changes |
| E7 | Fake-UI screens ("SATELLITE · LIVE / NIGHT 1 · 9:42 PM / SEVERE STORM", "X-RAY / THROAT: ON FIRE", "THERMAL / LUNGS: 207°F → 451°F"). The text is crisp and stable, while the radar clouds and sweep line animate underneath | video 1: radar ~16.5–17.3 s (frames 495–520), X-ray ~40–43 s, thermal ~63 s | Consistent with a **GPT-image-quality still** (good text rendering) animated by I2V, or text overlaid in the editor. The 207→451 °F change is a **second image or an edited overlay**, not a ticking counter |
| E8 | Captions: one word (sometimes two) per page, white heavy sans with dark outline and shadow, centred just above mid-frame, timed to the voice | all | **Auto-caption feature** of CapCut-class editors or an explainer platform. Easily reproduced with WhisperX + an ASS or Remotion renderer |
| E9 | Character consistency is good but not pixel-perfect between shots. Shirt flower placement and cat shape drift; head outline weight varies | videos 1 and 12 | **Reference-image-conditioned generation** (image model plus I2V "elements/ingredients"), not a single vector rig. A rig would be pixel-identical |

**Verdict from the evidence:** motion is predominantly **generative**, and the editing layer adds dissolves, captions and SFX. Some shots (simple push-ins on static compositions) *could* be 2.5D layer moves, but they are indistinguishable from low-motion I2V clips at this bitrate.

---

## 2. Hypotheses, ranked

### H1: AI stills → AI image-to-video → NLE with auto captions and AI voice (most likely, ~65%)
**Pipeline:**
1. LLM script in second person ("Imagine you're stranded…").
2. Style-locked keyframe stills for each beat, from an image model with reference images: GPT Image 2/2.5, Nano Banana Pro, Seedream, Midjourney and the like.
3. Each still animated with an I2V model using start/end frames and short camera-move prompts: Kling 3.0, Veo 3.1, Seedance 2.0/2.5, Hailuo, Grok Imagine, Gemini Omni Flash.
4. Clips assembled in CapCut, Premiere or Resolve with 3–6-frame dissolves and SFX.
5. Auto word-by-word captions and a TTS narrator (ElevenLabs-class).

**Supporting evidence:**
- E3–E6 and E9 above.
- The market and tooling for exactly this look in 2026:
  - **Higgsfield Explainer** lists **9:16 presets including "Stickman Cartoon", "2D Illustrator", "Pastel Flat 2D", "Hand Drawn", "Editorial Motion Graphics"**. The product writes the script, scenes, voiceover and final video, up to 10 min, 9:16 or 16:9. It also ships a "Stickman Cartoon Explainer" skill reachable from Claude or ChatGPT via MCP ([Higgsfield changelog](https://higgsfield.ai/creator-hub/changelog), [Stickman cartoon skill](https://higgsfield.ai/skills/stickman-cartoon), [Higgsfield MCP stickman](https://higgsfield.ai/mcp/stickman-explainer), [explainer page](https://higgsfield.ai/ai-explainer-video-maker)). The preset catalogue was confirmed live through the Higgsfield MCP `get_explainer_presets` call on 2026-10-27; it returned 22 presets, all 9:16 including "Stickman Cartoon". A reviewer notes that Explainer uses a preset AI voice ([growpalz](https://growpalz.com/reviews/higgsfield-reviews-real-examples/)).
  - **kaomei/stickman-video-director** (MIT, **3.2k★**, created Aug 2026): an agent-skill pipeline for "faceless YouTube" stickman channels. Clips are generated in **Google Flow** (Veo), then edited and captioned in **CapCut**. The style catalogue includes round-headed figures with "solid white round heads… black oval eyes" in "fully illustrated 2D environments" ([GitHub](https://github.com/kaomei/stickman-video-director), [README.en](https://github.com/kaomei/stickman-video-director/blob/main/README.en.md)).
  - **Hermoso** offers a "Stickman cartoon" explainer style with round heads. Its pipeline "renders a single style key image first, then locks every subsequent frame to it" ([hermoso.ai](https://hermoso.ai/recipes/explainer-styles/stickman/)).
  - Workflow guides recommend generating explicit **start (and end) frames** and letting I2V fill the motion, in shots of about 3–6 s ([Neolemon](https://www.neolemon.com/blog/ai-storyboard-to-animation-pipeline-workflow/), [Neolemon consistency](https://www.neolemon.com/blog/how-to-create-consistent-characters-in-ai-videos-complete-guide/)). Stickman guides finish in **CapCut/Premiere/Resolve** ([HitPaw](https://www.hitpaw.com/creative-video-tips/ai-stickman-animation-video.html)).
  - Freelance marketplaces sell "**AI Stick Figure Animation Videos for YouTube (High Retention)**" ([Upwork](https://www.upwork.com/services/product/video-audio-ai-stick-figure-animation-videos-for-youtube-high-retention-2045011823092056739), [Fiverr examples](https://fiverr.com/chris_techpuls/create-2d-stickman-animation-or-stick-figure-video)).
- The model capabilities needed exist in 2026:
  - **Kling 3.0**: start+end frames, multi-shot (up to 6 cuts per generation), "Elements" character references (2–4 images), clips up to about 15 s ([Kling 3.0 guide](https://kling.ai/quickstart/klingai-video-3-model-user-guide), [Kling Elements](https://kling.ai/quickstart/klingai-element-library-3-user-guide), [kingy review](https://kingy.ai/news/kling-3-0-review-a-serious-step-toward-ai-video-as-a-production-system/)).
  - **Veo 3.1**: "Ingredients to Video" with **native 9:16**, plus first/last-frame "Frame to Video" in Flow ([Google blog](https://blog.google/innovation-and-ai/technology/developers-tools/veo-3-1-gemini-api/), [PetaPixel](https://petapixel.com/2025/10/16/google-veo-3-1-lets-you-combine-different-photos-into-seemless-ai-video), [fonearena](https://www.fonearena.com/blog/?p=473509)).
  - **Seedance 2.0**: multimodal references (about 9 images, 3 videos, 3 audio), 4–15 s, up to 1080p ([BytePlus docs](https://docs.byteplus.com/docs/ModelArk/2291680), [Together quickstart](https://docs.together.ai/docs/seedance2.0-quickstart)).
  - Current arena leaders for I2V include Gemini Omni Flash, Seedance 2.0 and Grok Imagine 1.5 ([Pixazo comparison](https://www.pixazo.ai/blog/ai-video-generation-models-comparison), [OpenRouter](https://openrouter.ai/blog/insights/image-to-video-models-compared/)).

**Against / open questions:**
- The rapid face swaps every few frames look snappier than typical I2V. They may be **separate short clips** per emotion, or explicit expression prompts mid-clip.
- UI-screen text is unusually stable for I2V. It could be overlaid, or the camera motion on those shots may be minimal.

### H2: Hybrid: AI stills plus After Effects 2.5D compositing, with some AI-video shots (~20%)
**Pipeline:**
- AI-generated backgrounds and character cut-outs (transparent PNGs).
- AE 3D layers with a 3D camera for push-ins and drift.
- Puppet pin or **DUIK Ángela** (free, GPL-3, v17.x) for limb wiggles.
- **Joysticks 'n Sliders** pose-based face rigs, or simple *time-remapped image sequences* for expression swaps.
- CC Particle/Particular for sparkles and smoke.
- Lottie or shape-layer FX, and auto-captions via Premiere's speech-to-text or a script.
- AI I2V only for the hard shots (falling, crane).

**For:** the static-composition push-in shots and the crisp UI screens fit this well. A one-person "hand-made" claim fits AE (the CLAUDE.md wording is "hand-made Shorts style"). **Against:** E3/E5-type shots dominate the samples I checked, and the AE rigging look (rigid parts, pin bends) is not visible.
**Tools if true:** DUIK Ángela (current 17.1.x/17.2 alpha; note that Bassel throws errors in AE 2026) ([RxLaboratory](https://rxlaboratorio.org/rx-tool/duik/), [Adobe community](https://community.adobe.com/announcements-527/free-resource-duik-angela-the-industry-standard-for-rigging-and-animation-in-after-effects-1627639), [Bassel AE2026](https://community.adobe.com/questions-529/duik-bassel-on-ae2026-1549922)), Joysticks 'n Sliders ([aescripts](https://aescripts.com/joystick-n-sliders), [head-rig tutorial](https://aescripts.com/learn/head-rig-and-facial-animation-using-joysticks-n-sliders-in-after-effects)), RubberHose 3 / Limber (Lite is free) for stick limbs ([aescripts RubberHose+JnS](https://aescripts.com/learn/character-rigging-with-rubberhose-and-joysticks-n-sliders), [Limber Lite](https://animatabledotco.gumroad.com/l/limberlite)), Overlord (Illustrator → AE shapes).

### H3: Fully hand-rigged 2D animation, in AE + Character Animator or Moho (~8%)
**Character Animator:**
- Swap sets and triggers give instant expression changes, the Lip Sync behaviour handles mouths, and replays reuse performances ([Adobe community: swap sets/triggers](https://community.adobe.com/questions-571/regular-mouth-and-sad-mouth-are-conflicting-when-i-make-triggers-254239), [Packt chapter](https://packtpub.com/en-cl/product/real-time-animation-with-adobe-character-animator-9781803246949/chapter/chapter-7-assigning-mouths-and-props-with-triggers-and-swap-sets-9/section/summary-summary)).
- Note: a Jan-2026 forum post says Character Animator "hasn't had an update in over a year" ([Adobe community](https://community.adobe.com/questions-571/support-for-more-languages-when-computing-lip-sync-1548008)).

**Moho 14:** smart bones, switch layers and auto lip-sync ([Moho features](https://mohoanimation.com/pages/features)).

**Against:** the cost of producing about 25 distinct painted, perspective-changing scenes per 60-s video by hand, three videos a week. The camera moves in E3/E5 are not plausible as hand animation.

### H4: Blender (Grease Pencil v3 + image planes) (~5%)
- Blender 4.3+/5.x Grease Pencil v3, built-in Images as Planes, camera rigs, compositor glow.
- **Against:** no render tells (EEVEE shading, GP line style), and the characters' painted shading and drift look generated, not GP-drawn.
- Still a strong *replication* option (see §4).

### H5: Cavalry / Rive / Spine / Toon Boom (~2%)
- Rive and Spine are app/game runtimes, and both need manual vector rebuilding.
- Cavalry is now free for individuals, but CLI rendering is Enterprise-only ([3dart](https://www.3dart.it/en/cavalry-pro-is-now-completely-free-the-after-effects-alternative-rides-in/), [Cavalry CLI](https://cavalry.studio/docs/applications/cavalry-cli/)).
- Nothing in the footage suggests any of these.

---

## 3. Component-by-component: likely source and how we reproduce it

| Component | Most likely original | Our reproduction (automatable) |
|---|---|---|
| Script / narration | LLM script; TTS voice (single narrator) | Script from SRT; TTS of choice (out of scope per CLAUDE.md rule 5) |
| Backgrounds (painterly 2.5D look, lighting variants) | AI image model, style-locked | **GPT-image 2.5 Sunburst**, 1152×2048, day master → lighting edits (`chatgpt_image_prompting_2026.md` §6.5) |
| Characters + emotions | AI image refs (I2V "elements"/"ingredients") | GPT-image 2.5 transparent masters + per-emotion edits, post-aligned in code |
| Camera push-ins / drift / punch-ins | Mostly inside I2V clips; some may be editor zooms | Remotion `interpolate` on layers, or a **Blender 5.2** perspective camera over depth-spaced planes; DepthFlow for single-image parallax |
| Complex motion (walk, sit, fall, crane, morph FX) | I2V | I2V per shot: commercial **Kling 3.0 / Veo 3.1 / Seedance 2.0** with start+end frames composed from our assets, or self-hosted **Wan 2.2 / LTX-2** (+ style LoRA) |
| Face swaps every few frames | Separate clips or explicit prompting | Deterministic sprite-swap timeline (Remotion/Blender); optional I2V for in-between morphs |
| Fake UI screens, posters, diagrams | AI stills with text; maybe editor overlays | GPT-image stills for art, plus **code-rendered text** (Remotion/CSS) for anything that changes |
| FX (red X, smoke puffs, sparkles, sweat, tears) | Generated in clip or editor stickers | Transparent PNG variants cycled every 2–3 frames ("boil"), or Lottie FX |
| Transitions | 3–6-frame dissolves | Crossfade in Remotion/ffmpeg `xfade`/Blender VSE |
| Captions | CapCut-style auto captions | WhisperX alignment → one-word pages, white Montserrat/Poppins ExtraBold, dark stroke and shadow, centred |

---

## 4. Choosing the automatable engine: Blender 5.2 vs After Effects vs code

| Criterion | **Blender 5.2 (Python)** | **After Effects (ExtendScript/expressions)** | **Remotion** (Motion Canvas / Manim alternatives) |
|---|---|---|---|
| Runs headless on Linux (this repo's environment) | Yes: `blender -b -P` (EEVEE needs a GPU; use Cycles CPU otherwise) ([5.2 manual: EEVEE limits](https://docs.blender.org/manual/en/latest/render/eevee/limitations/limitations.html)) | **No.** Windows/macOS only; `aerender` needs a licensed AE install ([Adobe aerender](https://helpx.adobe.com/after-effects/desktop/render-and-export/automate-rendering/automated-rendering-network-rendering.html)) | Yes: Node + headless Chromium |
| Scripting future-proofing | 5.x API settled (strips, channelbags, compositing_node_group); 5.2 LTS until 2028 | ExtendScript is legacy; **AE UXP scripting still beta** (min v27.0 per a third-party skill doc) ([mapsoft](https://mapsoft.com/posts/extendscript.html), [TerminalSkills](https://github.com/TerminalSkills/skills/blob/main/skills/after-effects/SKILL.md)) | Plain TypeScript/React |
| True 2.5D parallax / DOF / relighting | **Best** (real camera, depth, DOF, lights, GP limbs) | Very good (3D layers/camera, plugins) | Fake parallax only (unless three.js) |
| Captions / UI text / overlays | OK (VSE text strips; 5.2 presets; ASS burn-in easier) | Excellent | **Best** (`@remotion/captions`, CSS) |
| Face-swap timelines | Image-sequence textures / handlers | Time-remap / JnS / Character Animator | Trivial (frame → src lookup) |
| Rig ecosystem | GP v3, armatures, nijiGPen | **Richest** (DUIK, RubberHose, JnS, Limber) | DIY SVG |
| Licensing / cost | GPL, free | Subscription + paid plugins | Free ≤3-person company; paid above ([Remotion license](https://remotion.dev/license)) |
| Iteration speed for an agent | Medium (render to check) | Low (GUI-centric) | High (hot reload, JSON props) |
| Overall fit for **this** project | ★★★★ for camera-heavy 2.5D shots | ★★ (fine by hand, poor to automate here) | ★★★★★ for assembly, captions, overlays and most 2.5D shots |

### Recommended pipeline
1. **Plan:** SRT → beats → `shot_plan.json`. Each 1–3 s shot gets: background id, lighting variant, characters (pose id, emotion timeline at frame resolution), camera move (type, from/to, easing), overlays and FX, transition, and caption words.
2. **Assets:** GPT-image **2.5 Sunburst** masters, **Flare** variants; transparent PNG/WebP for characters, faces and FX. Store prompt + reference + crop per asset (CLAUDE.md rule 2).
3. **Render each shot by class:**
   - **2.5D shot** (static pose, push-in/drift, face swaps, bob/squash): Remotion composition (default), or Blender 5.2 when the move needs real depth (fisheye POV, big dolly with occlusion). Blender: planes plus a perspective camera, Standard view transform, Cycles/EEVEE (`blender_5_2_notes.md`).
   - **Motion shot** (walk, sit, fall, crane, morphing FX): compose start and end frames from our assets in code, then run I2V with a short camera/motion prompt. Pick the model per shot: Kling 3.0 for explicit camera moves and elements; Veo 3.1 for native 9:16 ingredients; Seedance 2.0 for multi-reference. Self-hosted Wan 2.2/LTX-2 if cost or privacy matters.
   - **UI / diagram shot:** GPT-image art layer plus Remotion text layers (ticking clocks, temperature counters).
4. **Assemble** in Remotion: clips, 3–6-frame crossfades, FX overlays, word captions (WhisperX timing) and VO. Render 720×1280, 30 fps, H.264 (`npx remotion render … --codec h264`).
5. **QA:** run the repo's `tools/metrics.py`, `motion.py` and `palette.py` against the reference stats: shot length, motion energy, colour palette, caption position.

**Why not AE as the core:** it is the most capable *manual* tool and plausibly part of the original (H2). But this repo runs on Linux containers, AE cannot render here, and its scripting stack is mid-migration (ExtendScript → UXP beta). Keep AE as an optional manual-polish path.

**Why not Blender alone:** captions, UI typography and fast iteration are more cumbersome. Note too that EEVEE needs a GPU, which most CI/agent containers lack. Use Blender for the shots that benefit from real 3D.

---

## 5. Other notes and open questions
- **Higgsfield Explainer as a shortcut:** we have a Higgsfield MCP connected. A one-off test render with the "Stickman Cartoon" or "2D Illustrator" preset on one of the scripts would quickly confirm or refute H1 by comparison. It costs credits, so ask the owner first. It is also a potential production path, though with less control: a preset voice, and no custom assets per the review above.
- Midjourney and Flux could also produce the backgrounds, but the prominent, correctly spelled in-image text (MANCHINEEL poster, UI screens) favours **GPT-Image 2/2.5 or Nano Banana Pro**, which lead on text rendering ([digitalapplied](https://www.digitalapplied.com/blog/chatgpt-images-2-0-features-use-cases-impact), [wavespeed Nano Banana Pro](https://wavespeed.ai/blog/posts/google-nano-banana-pro-complete-guide-2026)). This is inference, not proof.
- Not verified, because the sources were inaccessible: Reddit threads (r/AfterEffects, r/blender, r/NewTubers) and YouTube "how I make" videos for this exact look. A human check of a few channel "about/behind the scenes" pages would strengthen the ranking.

---

## Sources
- Higgsfield: changelog https://higgsfield.ai/creator-hub/changelog ; Stickman skill https://higgsfield.ai/skills/stickman-cartoon ; MCP stickman https://higgsfield.ai/mcp/stickman-explainer ; Explainer https://higgsfield.ai/ai-explainer-video-maker ; faceless blog https://higgsfield.ai/blog/faceless-channel-one-prompt ; Kling 3.0 on Higgsfield https://higgsfield.ai/blog/Kling-3.0-is-on-Higgsfield-User-Guide-AI-Video-Generation
- Higgsfield review: https://growpalz.com/reviews/higgsfield-reviews-real-examples/
- Hermoso stickman style: https://hermoso.ai/recipes/explainer-styles/stickman/
- kaomei/stickman-video-director: https://github.com/kaomei/stickman-video-director ; https://github.com/kaomei/stickman-video-director/blob/main/README.en.md
- azeemgujjar stickman prompt workflow: https://github.com/azeemgujjar/STICKMAN-ANIMATION-VIDEO-GENERATOR-PROMPT
- Neolemon workflows: https://www.neolemon.com/blog/ai-storyboard-to-animation-pipeline-workflow/ ; https://www.neolemon.com/blog/how-to-create-consistent-characters-in-ai-videos-complete-guide/
- HitPaw stickman guide: https://www.hitpaw.com/creative-video-tips/ai-stickman-animation-video.html
- Upwork / Fiverr listings: https://www.upwork.com/services/product/video-audio-ai-stick-figure-animation-videos-for-youtube-high-retention-2045011823092056739 ; https://fiverr.com/chris_techpuls/create-2d-stickman-animation-or-stick-figure-video
- Podcast ("Bad Drawing" empire): https://metacast.app/podcast/ai-fire-daily/YfRCG9xp/43-robin-the-61k-mo-bad-drawing-empire-and-claude-code-s-youtube-automation-takeover/EHRVSuYN
- Kling 3.0: https://kling.ai/quickstart/klingai-video-3-model-user-guide ; https://kling.ai/quickstart/klingai-element-library-3-user-guide ; https://kingy.ai/news/kling-3-0-review-a-serious-step-toward-ai-video-as-a-production-system/ ; https://magichour.ai/blog/kling-30-reference-guide
- Veo 3.1: https://blog.google/innovation-and-ai/technology/developers-tools/veo-3-1-gemini-api/ ; https://petapixel.com/2025/10/16/google-veo-3-1-lets-you-combine-different-photos-into-seemless-ai-video ; https://www.fonearena.com/blog/?p=473509
- Seedance 2.0: https://docs.byteplus.com/docs/ModelArk/2291680 ; https://docs.together.ai/docs/seedance2.0-quickstart
- I2V comparisons: https://www.pixazo.ai/blog/ai-video-generation-models-comparison ; https://openrouter.ai/blog/insights/image-to-video-models-compared/ ; https://videogen.io/best-ai-video-models
- AI explainer tool roundups: https://tedpress.com/best-ai-animated-explainer-video-tools-2026-ranked-for-script-to-video-scene-level-editing-and-character-consistency/ ; https://www.neolemon.com/blog/best-ai-tools-for-animated-storytelling/
- DUIK: https://rxlaboratorio.org/rx-tool/duik/ ; https://community.adobe.com/announcements-527/free-resource-duik-angela-the-industry-standard-for-rigging-and-animation-in-after-effects-1627639 ; https://community.adobe.com/questions-529/duik-bassel-on-ae2026-1549922 ; https://www.toolfarm.com/news/duik-angela/
- Joysticks 'n Sliders / RubberHose: https://aescripts.com/joystick-n-sliders ; https://aescripts.com/learn/head-rig-and-facial-animation-using-joysticks-n-sliders-in-after-effects ; https://aescripts.com/learn/character-rigging-with-rubberhose-and-joysticks-n-sliders
- Limber Lite: https://animatabledotco.gumroad.com/l/limberlite
- Character Animator: https://community.adobe.com/questions-571/regular-mouth-and-sad-mouth-are-conflicting-when-i-make-triggers-254239 ; https://community.adobe.com/questions-571/support-for-more-languages-when-computing-lip-sync-1548008 ; https://packtpub.com/en-cl/product/real-time-animation-with-adobe-character-animator-9781803246949/chapter/chapter-7-assigning-mouths-and-props-with-triggers-and-swap-sets-9/section/summary-summary
- Moho: https://mohoanimation.com/pages/features ; https://moho.lostmarble.com/blogs/news/moho-14-2-is-here-free-update-for-moho-14-owners
- Cavalry: https://www.3dart.it/en/cavalry-pro-is-now-completely-free-the-after-effects-alternative-rides-in/ ; https://cavalry.studio/docs/applications/cavalry-cli/
- AE automation: https://helpx.adobe.com/after-effects/desktop/render-and-export/automate-rendering/automated-rendering-network-rendering.html ; https://mapsoft.com/posts/extendscript.html ; https://github.com/TerminalSkills/skills/blob/main/skills/after-effects/SKILL.md ; https://github.com/jhd3197/after-effects-automation
- Blender 5.2: https://developer.blender.org/docs/release_notes/5.2/ ; https://docs.blender.org/manual/en/latest/render/eevee/limitations/limitations.html (more in `blender_5_2_notes.md`)
- Remotion license: https://remotion.dev/license
- Image-model text rendering: https://www.digitalapplied.com/blog/chatgpt-images-2-0-features-use-cases-impact ; https://wavespeed.ai/blog/posts/google-nano-banana-pro-complete-guide-2026
- Companion files: `chatgpt_image_prompting_2026.md`, `face_animation_github.md`, `blender_5_2_notes.md` (same folder)
