# Open-source tools for code-driven 2D cartoon faces, stick-figure bodies, lip-sync and word captions

Researched 2026-10-27. Star counts were read from the GitHub search API on 2026-10-27. "Last push" is shown where the API returned it. Licenses were read from the repository pages or LICENSE files.

**Target look (from the brief and our own frame checks):**
- Bean-head characters: a big round pale head, thick dark outline, dot eyes, rosy cheeks, a capsule torso in a patterned shirt, and stick limbs.
- Expressions change every few frames.
- Bodies hold poses with small bob and squash.
- Detailed painterly backgrounds, 2.5D camera drift, punch-ins, fake-UI overlays.
- Bold white word-by-word captions in the centre of the frame.

**What the reference actually is:** frame-level inspection suggests that most of the motion in the reference is **AI image-to-video**, not rigs. Look at the continuous 3D crane moves, the boiling smoke, and the character sitting and falling with smooth in-betweens (see `toolchain_hypotheses.md`). The tools below are therefore judged on two questions:
- (a) Can they *replace* that AI motion with deterministic code?
- (b) Can they serve as the *overlay, caption and face-swap layer* on top of AI clips?

---

## 1. Quick verdict

| Need | Best open-source pick | Why |
|---|---|---|
| Frame-by-frame expression swapping from a PNG emotion library | **Your own sprite-swap layer** in Remotion, Blender or ffmpeg (no special library needed) | The reference faces are discrete drawings. Swapping images on a timeline is the exact equivalent |
| Procedural bean-head faces with smooth tweening | **Remotion** or **Motion Canvas** with custom SVG/vector components | The style is geometric (circle, ovals, arcs), so it can be drawn and tweened in code at any resolution |
| Stick limbs and body bob/squash | SVG paths (Remotion/Motion Canvas) or **Blender Grease Pencil v3** strokes driven by Python | Thin dark lines are trivial to generate procedurally. IK is optional |
| 2.5D camera and parallax on painted plates | **Blender 5.2** (planes + perspective camera) or **DepthFlow** (single image + depth) | True parallax and DOF; Blender is fully scriptable headless |
| Word-level timing for captions | **WhisperX** (BSD-2) or **faster-whisper** (MIT). Use forced alignment against the known script | You already have the script, so alignment beats transcription |
| Caption rendering | **Remotion `@remotion/captions` → `createTikTokStyleCaptions`**, an ffmpeg/ASS burn-in, or Blender text strips | |
| Mouth lip-sync (if ever needed) | **Rhubarb Lip Sync** (MIT) | The reference narrator is off-screen and mouths barely move, so this is low priority |
| AI motion fallback, self-hosted | **Wan 2.2** (Apache-2.0), **LTX-2** | For shots where code animation looks too stiff |
| In-betweens between two expression drawings | **ToonCrafter** (Apache-2.0) | Experimental and low resolution |

---

## 2. Code-driven video frameworks (assembly, faces, captions)

### Remotion: https://github.com/remotion-dev/remotion
- **68.2k★**, very active (pushes daily). **License: Remotion License**, free for individuals, for-profit companies with **up to 3 employees**, and non-profits. Larger companies need a paid company license; "Automators" pricing is $0.01/render with a $100/month minimum. The license is expected to "slightly change" in Remotion 5.0 ([remotion.dev/license](https://remotion.dev/license), [pricing](https://www.remotion.dev/docs/pricing), [LICENSE.md](https://github.com/remotion-dev/remotion/blob/main/LICENSE.md)).
- **Fit:** compositions are React components rendered frame by frame by headless Chromium plus ffmpeg (`npx remotion render`), and props come from JSON. The 9:16 30 fps 720×1280 output is a one-liner. Features that map to the reference:
  - `<Img>` / `<OffthreadVideo>` layers with `interpolate()` and `spring()` for push-ins, bobs and punch-ins.
  - Face swaps via `frame → emotion` lookup tables.
  - SVG for procedural faces and limbs.
  - CSS for fake-UI screens: crisp, editable text such as the "NIGHT 1 · 9:42 PM" clock that can actually tick.
- **Captions:** `@remotion/captions` exports `createTikTokStyleCaptions`, `parseSrt`, `serializeSrt` and others (verified in [packages/captions/src/index.ts](https://raw.githubusercontent.com/remotion-dev/remotion/main/packages/captions/src/index.ts)). The official **template-tiktok** (294★) shows Whisper.cpp → word-by-word captions ([github.com/remotion-dev/template-tiktok](https://github.com/remotion-dev/template-tiktok)). There is also an official **Agent Skills** repo, `remotion-dev/skills` (5.8k★), for driving Remotion from Claude or Codex.
- **Style match:** excellent for captions, UI overlays, 2D transforms and procedural vector faces. **Gap:** there is no true 3D parallax. You can fake it with per-layer translate/scale, which is enough for the drift seen in most shots, or embed three.js through `@remotion/three`. Painterly backgrounds must come from AI images. **Tune:** caption font (Montserrat/Poppins ExtraBold 800–900, white, 6–8 px dark stroke, soft shadow) and per-word pop (scale 1.15 → 1.0 over 3 frames).

### Motion Canvas: https://github.com/motion-canvas/motion-canvas
- **19.5k★**, **MIT**. TypeScript generator-based timeline with a live editor. The latest documented release is 3.x, which added an FFmpeg video exporter ([blog 3.8.0](https://motioncanvas.io/blog/version-3.8.0)).
- **Fit:** great for procedural vector characters and tweening. Rendering is editor- and browser-centric, and I found no official headless CLI, which makes it weaker for unattended batch rendering than Remotion ([Remotion comparison](https://www.remotion.dev/docs/compare/motion-canvas)).
- **Fork: Revideo**, https://github.com/redotvideo/revideo, **4.1k★, MIT**. Adds `renderVideo()` headless rendering, a render endpoint and parallel workers. Good if you want Motion Canvas ergonomics plus a fully MIT, server-side pipeline. Recent activity could not be confirmed.

### Manim (Community): https://github.com/ManimCommunity/manim
- **41.9k★**, MIT. A Python framework for mathematical animation.
- **Fit:** useful for diagram beats such as number-distribution bars in "Why Humans Can't Pick Random Numbers" or labelled macro diagrams. **Gap:** not built for character or raster-heavy compositing, and its look is "math video" unless heavily styled. Use it only for diagram inserts.

### MoviePy: https://github.com/Zulko/moviepy
- **15.0k★**, MIT. Python compositing over ffmpeg. Fine for simple layer stacking and caption burn-in, but slow at 30 fps with many layers. A last-mile tool only.

---

## 3. Rigging / runtime formats (Rive, Lottie, Spine, Live2D-likes)

### Rive: https://github.com/rive-app/rive-runtime (and rive-wasm, rive-react)
- Runtimes are **MIT**: rive-runtime 1.2k★, rive-wasm 1.0k★, rive-react 1.2k★, rive-flutter 1.5k★. The **editor is a proprietary SaaS** and is not open source.
- **Fit:** state machines with discrete expression states (neutral/shocked/crying), blend states, bones and mesh deformation. Ideal for a reusable bean-head puppet whose emotion is set by an input. Render in Remotion via the `@remotion/rive` component, or headlessly with the C++ runtime.
- **Style match:** good for flat vector. **Gaps:** the reference characters carry painterly shading and AI-drawn detail. Rebuilding each character as vectors in the Rive editor is manual and not automatable. Licensing the editor is a cost.

### Lottie / bodymovin: https://github.com/airbnb/lottie-web
- **32.3k★** (lottie-android 35.8k, lottie-ios 26.9k), MIT. dotLottie web player, Rust + WASM via ThorVG: https://github.com/LottieFiles/dotlottie-web (929★).
- **Fit:** export After Effects (bodymovin) or Glaxnimate vector animations of FX overlays (sweat drops, sparkles, red X draw-ons, smoke puffs) and play them over video in Remotion (`@remotion/lottie`). **Gap:** raster AI art inside Lottie is clumsy, so use Lottie only for vector FX.
- **Glaxnimate** (open-source Lottie/SVG animator, KDE): https://github.com/KDE/glaxnimate (mirror, 42★; main development is on KDE GitLab).

### Spine runtimes: https://github.com/EsotericSoftware/spine-runtimes
- **5.3k★**, default branch 4.3. **License: Spine Runtimes License.** Integration is free, but **every user needs a Spine editor license**, and you may not use the runtimes to build new software without one ([repo](https://github.com/EsotericSoftware/spine-runtimes)).
- **Fit:** skeletal cut-out with attachment swapping (perfect for face swaps) and mesh deform. **Gap:** the commercial editor is required, and the rig authoring step is manual. Overkill for stick limbs.

### Inochi2D (open Live2D alternative): https://github.com/Inochi2D/inochi2d
- SDK **1.8k★, BSD-2-Clause, last push 2026-10-03**. Rigging app **inochi-creator** 1.3k★, BSD-2, last push 2025-06-16. Rust port inox2d 300★.
- **Fit:** deformable 2D puppets from layered PSDs with parameters such as eye open and mouth form. Built for VTubers. **Gaps:** the D-language toolchain, the creator app is slow-moving, and offline batch rendering is not its focus. The bean-head style needs no mesh deformation, so it is overkill.

### pixi-live2d-display: https://github.com/guansss/pixi-live2d-display
- **1.5k★**, MIT, but it **needs the proprietary Live2D Cubism Core** (Cubism 4; Cubism 5 is not mentioned). The same caveat as Live2D in general applies: a commercial SDK license and manual rigging in Cubism Editor. Not recommended.

### Moho / Toon Boom / Cavalry (commercial, for context)
- **Moho 14** (14.2 update): smart bones, switch layers, automatic audio lip-sync, and Lua scripts runnable from the command line at startup ([Moho 14.2](https://moho.lostmarble.com/blogs/news/moho-14-2-is-here-free-update-for-moho-14-owners), [features](https://mohoanimation.com/pages/features)).
- **Cavalry** (Canva) is now **free for individuals including commercial use**, with JavaScript scripting. **CLI rendering is listed under Enterprise** ([3dart](https://www.3dart.it/en/cavalry-pro-is-now-completely-free-the-after-effects-alternative-rides-in/), [Cavalry CLI docs](https://cavalry.studio/docs/applications/cavalry-cli/)).
- These are capable, but not open source and not easily batch-automated.

---

## 4. Blender-side (Grease Pencil, cut-out, 2D tools)

- **Blender 5.2 GP v3 Python API**: layers/frames/drawings, `drawing.add_strokes`, attribute access. Details and a code sample are in `blender_5_2_notes.md`. Stick arms and legs as procedurally written GP strokes, or as GP plus Armature/Hook modifiers, match the thin dark limb lines well. Faces as image planes with swapped textures.
- **nijiGPen**: https://github.com/chsh2/nijiGPen. 385★, **GPL-3.0**, supports Blender 3.3–4.2 (GPv2) and **4.3–5.2 (GPv3)**. Stroke boolean/offset, line cleanup, and 2D→3D shading. Useful for generating clean outlines, not essential.
- **Frame By Plane** (free Blender extension): image/PSD → rigged planes for cut-out and multiplane work ([extensions.blender.org](https://extensions.blender.org/add-ons/frame-by-plane/)).
- **OpenToonz**: https://github.com/opentoonz/opentoonz. 7.9k★, **BSD-3**. A full 2D animation suite with a cut-out "plastic" tool and lip-sync data import. Scripting is limited, so it is not a good batch target.
- **Synfig**: https://github.com/synfig/synfig. 2.3k★, **GPL-3.0**. Vector tweening with skeleton layers, a CLI renderer and Papagayo lip-sync import (the repo page did not list these, so check the Synfig docs).
- **Papagayo-NG**: https://github.com/morevnaproject-org/papagayo-ng. 292★. Manual phoneme timing, exportable to Synfig, Blender and others.

---

## 5. Lip-sync

### Rhubarb Lip Sync: https://github.com/DanielSWolf/rhubarb-lip-sync
- **2.7k★**, **MIT** (dependencies MIT, BSD or Boost). A CLI that turns WAV (+ optional script text) into timed mouth shapes A–H/X as TSV, JSON or XML.
- **Fit:** if a character ever speaks on screen, draw 6–9 mouth PNGs per character with GPT-image (using the same head-edit technique as emotions) and swap them by Rhubarb's cue list. **Reference relevance:** low. The narrator is off-screen and mouths change with *emotion*, not with phonemes.

---

## 6. Faces and expressions: procedural and AI-assisted

- **facesjs**: https://github.com/zengm-games/facesjs. **1.4k★, Apache-2.0**. Procedural SVG cartoon faces (Mii-like), with a React component and CLI. Expressions are not a feature. **Use as a design pattern only:** its "face = small JSON of feature IDs → SVG" approach is exactly how a **procedural bean-head** generator should work. Example: `{head:'circle', eyes:'shocked', brows:'raised', mouth:'O', cheeks:true, sweat:'right', tears:false}`. The look is not a match.
- **Build-your-own procedural bean head** (recommended if crispness and smooth tweening matter more than painterly shading):
  - Head: a circle with a 6–8 px dark stroke, a lavender-white fill and a radial-gradient shade band.
  - Eyes: ellipses, or arcs for closed eyes. Mouth: SVG path presets. Cheeks: pink ellipses at 60% opacity.
  - Tear streams: blue rounded paths. Sweat drop: a teardrop path. Hair: 2–3 tuft paths.
  - All of this is animatable per frame in Remotion or Motion Canvas.
  - **Gap vs reference:** the reference heads have subtle painted shading and irregular hand-made line weight. Add an SVG turbulence/displacement filter and a soft inner shadow to approach it.
- **LivePortrait**: https://github.com/KwaiVGI/LivePortrait. **19.3k★, MIT code.** The InsightFace detection models it uses are **non-commercial**, so swap them for commercial use. Drives a portrait with a driving video, and has an animal (cat/dog) mode. **Honest assessment:** it relies on face keypoint detection. Dot-eyed, noseless bean heads will likely fail detection, so expect poor results without custom keypoints.
- **ToonCrafter**: https://github.com/Doubiiu/ToonCrafter. **6.0k★, Apache-2.0, last push 2025-03.** Generative interpolation between two cartoon keyframes (SIGGRAPH Asia 2024). **Fit:** in-betweens such as neutral → shocked, or a pose A → pose B for limbs. **Gaps:** low native resolution and short clips (it was designed at 512×320 and needs an upscaler), plus artifacts on thin lines. Experimental only.
- **AnimatedDrawings** (Meta): https://github.com/facebookresearch/AnimatedDrawings. **12.8k★, MIT, archived** (last push 2025-09). Segments a drawn human figure, rigs it automatically and retargets BVH motion. **Fit:** in principle it could animate a full-body bean figure with walk or jump motions. **Gaps:** the very thin stick limbs and the oversized head will likely break segmentation and pose estimation, and the project is no longer maintained.

---

## 7. Word-by-word captions (timing and rendering)

| Repo | ★ | License | Notes |
|---|---|---|---|
| **WhisperX**: https://github.com/m-bain/whisperX | 24.9k | BSD-2 | Word timestamps via wav2vec2 forced alignment, diarization. Last push 2026-10-22. **Recommended** |
| **faster-whisper**: https://github.com/SYSTRAN/faster-whisper | 26.2k | MIT | CTranslate2 Whisper, `word_timestamps=True`. Fast on CPU |
| **stable-ts**: https://github.com/jianfch/stable-ts | 2.3k | MIT | `align()` aligns **known text** to audio at word level, which is exactly our case since the script exists. **Archived 30 May 2026**: still usable, but unmaintained |
| **whisper-timestamped**: https://github.com/linto-ai/whisper-timestamped | 2.9k | **AGPL-3.0** | Word timestamps and confidences. The AGPL needs care |
| **captacity**: https://github.com/unconv/captacity | 139 | MIT | Shorts-style burned captions (Whisper + MoviePy), with font, stroke, shadow and current-word highlight. Good reference implementation, but small and possibly stale |
| **Remotion template-tiktok**: https://github.com/remotion-dev/template-tiktok | 294 | Remotion License | Whisper.cpp → TikTok-style word captions |

**Recommended caption chain:**
1. Take the script from the SRT (`SRT.txt`).
2. Run WhisperX alignment (or `stable_ts.align`) against the voiceover to get per-word start/end times.
3. Choose one renderer:
   - Remotion `createTikTokStyleCaptions` with `combineTokensWithinMilliseconds` small, giving a single word per page as in the reference.
   - An `.ass` file with `\fad` and `\fscx/\fscy` pop, burned with `ffmpeg -vf ass=`.
   - Blender VSE `TEXT` strips (code in `blender_5_2_notes.md` §3.5).

Note that the SRT files in this repo are YouTube-transcript style: line-level timestamps at 1–2 s granularity, with tags like `[music]`. They are **not word-level**, so alignment against audio is required.

---

## 8. All-in-one "faceless Shorts" repos (for workflow reference)

- **MoneyPrinterTurbo**: https://github.com/harry0703/MoneyPrinterTurbo. **135.8k★, MIT.** LLM script → stock footage *or* AI video (MiniMax, Seedance, Wan) / text-to-image clips → TTS (Edge, ElevenLabs, …) → subtitles (Edge timestamps or faster-whisper) → ffmpeg. **Style gap:** stock-footage aesthetic with no character system. Useful as an orchestration reference.
- **stickman-video-director**: https://github.com/kaomei/stickman-video-director. **3.2k★, MIT**, created Aug 2026. An agent-skill pipeline for **faceless stickman channels**:
  - "Director mode" writes storyboards and per-scene video prompts. Clips are generated in **Google Flow** (Veo), then edited and captioned in **CapCut**.
  - "Autopilot" produces illustrated scenes with pans, zooms and captions.
  - Its style catalogue includes round-headed figures with solid white heads and black oval eyes in "fully illustrated 2D environments" (styles A4/A5).
  - **This is the closest public analogue to the reference workflow** (see `toolchain_hypotheses.md`).
- **Blender MCP**: https://github.com/ahujasid/mcp-for-blender. 32.5k★, MIT. Lets an LLM drive Blender, useful for an agentic Blender assembly step.

---

## 9. AI motion and depth (self-hostable)

| Repo | ★ | License | Fit |
|---|---|---|---|
| **Wan 2.2**: https://github.com/Wan-Video/Wan2.2 | 18.2k | Apache-2.0 | TI2V-5B (720p/24 fps, ≥24 GB VRAM with offload), I2V-A14B (≥80 GB), **Animate-14B** (character animation/replacement from a driving video). Self-hosted image-to-video for character shots |
| **LTX-2**: https://github.com/Lightricks/LTX-2 | 9.9k | Custom LTX license, gated weights | Audio+video model with image-to-video, keyframe interpolation pipelines and LoRA/IC-LoRA training. **A style LoRA could lock the bean-head look** |
| **DepthFlow**: https://github.com/BrokenSource/DepthFlow | 1.6k | **AGPL-3.0** | Single image → depth → parallax camera video (GLSL). Quick "living background" push-ins without layer separation |
| **Depth-Anything-V2**: https://github.com/DepthAnything/Depth-Anything-V2 | 9.0k | Small: Apache-2.0; Base/Large: **CC-BY-NC-4.0** | Depth maps for DepthFlow, or to split plates into parallax layers |
| **rembg**: https://github.com/danielgatis/rembg | 25.2k | MIT | Cut-outs when an image model returns an opaque background |

---

## 10. Recommended open-source stack for this project (honest summary)

1. **Assets:** GPT-image 2.5 masters, emotions and backgrounds (see `chatgpt_image_prompting_2026.md`), then align faces in code.
2. **Animation layer (deterministic):**
   - **Remotion** if the team is JS-comfortable and has 3 or fewer employees. It gives the best captions, UI overlays and 2D layering.
   - **Blender 5.2** if real parallax, DOF, lighting and GPL licensing matter more.
   - In either case, characters are PNG layers with face-swap timelines, bob/squash transforms, and procedural stick limbs drawn as SVG paths or GP strokes.
3. **Motion that code can't fake** (sitting down, falling, 3D crane moves): AI image-to-video per shot. Use commercial Kling/Veo/Seedance to match the reference, or self-hosted Wan 2.2 / LTX-2 with a style LoRA. Then composite captions and overlays on top.
4. **Captions:** WhisperX alignment to the known script, then word-by-word renderer.
5. **What you should not expect** from rigs (Rive/Spine/Inochi2D/Live2D): reproducing the reference's painterly, perspective-changing shots. They suit a cleaner, flatter look and add manual authoring.

---

## Sources
- Remotion: https://github.com/remotion-dev/remotion ; license https://remotion.dev/license ; https://github.com/remotion-dev/remotion/blob/main/LICENSE.md ; pricing https://www.remotion.dev/docs/pricing ; captions exports https://raw.githubusercontent.com/remotion-dev/remotion/main/packages/captions/src/index.ts ; template https://github.com/remotion-dev/template-tiktok ; skills https://github.com/remotion-dev/skills ; comparison https://www.remotion.dev/docs/compare/motion-canvas
- Motion Canvas: https://github.com/motion-canvas/motion-canvas ; https://motioncanvas.io/blog/version-3.8.0
- Revideo: https://github.com/redotvideo/revideo
- Manim: https://github.com/ManimCommunity/manim
- MoviePy: https://github.com/Zulko/moviepy
- Rive: https://github.com/rive-app/rive-runtime ; https://github.com/rive-app/rive-wasm ; https://github.com/rive-app/rive-react ; https://github.com/rive-app/rive-flutter
- Lottie: https://github.com/airbnb/lottie-web ; https://github.com/airbnb/lottie-android ; https://github.com/airbnb/lottie-ios ; https://github.com/LottieFiles/dotlottie-web
- Glaxnimate: https://github.com/KDE/glaxnimate
- Spine: https://github.com/EsotericSoftware/spine-runtimes
- Inochi2D: https://github.com/Inochi2D/inochi2d ; https://github.com/Inochi2D/inochi-creator ; https://github.com/Inochi2D/inox2d
- pixi-live2d-display: https://github.com/guansss/pixi-live2d-display
- Moho: https://moho.lostmarble.com/blogs/news/moho-14-2-is-here-free-update-for-moho-14-owners ; https://mohoanimation.com/pages/features
- Cavalry: https://www.3dart.it/en/cavalry-pro-is-now-completely-free-the-after-effects-alternative-rides-in/ ; https://cavalry.studio/docs/applications/cavalry-cli/
- nijiGPen: https://github.com/chsh2/nijiGPen
- Frame By Plane: https://extensions.blender.org/add-ons/frame-by-plane/
- OpenToonz: https://github.com/opentoonz/opentoonz (LICENSE.txt BSD-3)
- Synfig: https://github.com/synfig/synfig
- Papagayo-NG: https://github.com/morevnaproject-org/papagayo-ng
- Rhubarb Lip Sync: https://github.com/DanielSWolf/rhubarb-lip-sync (LICENSE.md)
- facesjs: https://github.com/zengm-games/facesjs
- LivePortrait: https://github.com/KwaiVGI/LivePortrait (LICENSE)
- ToonCrafter: https://github.com/Doubiiu/ToonCrafter
- AnimatedDrawings: https://github.com/facebookresearch/AnimatedDrawings
- WhisperX: https://github.com/m-bain/whisperX
- faster-whisper: https://github.com/SYSTRAN/faster-whisper
- stable-ts: https://github.com/jianfch/stable-ts
- whisper-timestamped: https://github.com/linto-ai/whisper-timestamped
- captacity: https://github.com/unconv/captacity
- MoneyPrinterTurbo: https://github.com/harry0703/MoneyPrinterTurbo
- stickman-video-director: https://github.com/kaomei/stickman-video-director ; https://github.com/kaomei/stickman-video-director/blob/main/README.en.md
- Blender MCP: https://github.com/ahujasid/mcp-for-blender
- Wan 2.2: https://github.com/Wan-Video/Wan2.2
- LTX-2: https://github.com/Lightricks/LTX-2
- DepthFlow: https://github.com/BrokenSource/DepthFlow
- Depth-Anything-V2: https://github.com/DepthAnything/Depth-Anything-V2
- rembg: https://github.com/danielgatis/rembg
