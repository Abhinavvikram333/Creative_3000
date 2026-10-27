# ChatGPT / OpenAI image generation: best practice, late 2026

Researched 2026-10-27. openai.com and platform.openai.com could not be fetched from this sandbox. Facts below come from web-search extracts of OpenAI's own pages (developers.openai.com guides and reference, the OpenAI Cookbook, openai.com announcements) and are cross-checked against reputable secondary coverage. Items that only appear in third-party sources are marked *(3rd-party)*. **Re-verify model IDs and parameter limits on developers.openai.com before you build on them.**

---

## 1. What is current (Oct 2026)

| Model / product | Released | Status | Notes |
|---|---|---|---|
| **ChatGPT Images 2.5** = API **`gpt-image-2.5-flare`** (fast, default) and **`gpt-image-2.5-sunburst`** (precision, slower) | **8 Sep 2026** | **Current flagship** | Snapshots reported as `gpt-image-2.5-flare-2026-09-08` / `-sunburst-2026-09-08` *(3rd-party)*. Both support generation, editing and **transparent backgrounds**. About 50% lower latency than Images 2.0 (OpenAI claim). New Sketch tool and image comments in ChatGPT. C2PA metadata plus a SynthID watermark ([OpenAI announcement](https://openai.com/index/introducing-chatgpt-images-2-5/), [DataCamp](https://www.datacamp.com/blog/chatgpt-images-2-5), [Unite.AI](https://www.unite.ai/openai-releases-chatgpt-images-2-5-with-sketch-and-two-new-api-models/), [The Rundown](https://www.therundown.ai/news/openai-chatgpt-images-2-5-speed-editing-arena), [Wikipedia](https://en.wikipedia.org/wiki/GPT_Image)) |
| **`gpt-image-2`** (ChatGPT Images 2.0) | 21 Apr 2026 | Still served | First "reasoning" image model, with strong text rendering. **Transparent backgrounds were in preview, then rejected**: the API now returns `invalid_value … Transparent background is not supported for this model` ([OpenAI forum](https://community.openai.com/t/is-transparent-background-support-broken-in-gpt-image-2/1402707), [openai/codex #43757](https://github.com/openai/codex/issues/43757)). One third-party source dates the removal to 2026-09-30 *(3rd-party)* ([APIYI](https://help.apiyi.com/en/gpt-image-2-transparent-background-not-supported-fix-en.html)) |
| `gpt-image-1.5` | 16 Dec 2025 | Migration only | Supports `background:"transparent"` ([Codex issue](https://github.com/openai/codex/issues/43757), [Fortune](https://fortune.com/2025/12/16/openai-releases-new-image-model-as-it-races-to-outpace-googles-nano-banana-amid-company-code-red/)) |
| `gpt-image-1` | Apr 2025 | Legacy | Reportedly scheduled for removal 23 Oct 2026; check the deprecations page ([invideo](https://invideo.io/blog/gpt-image-ai-image-generator/)) |
| DALL·E 2/3 | — | Removed from API 12 May 2026 | ([invideo](https://invideo.io/blog/gpt-image-ai-image-generator/)) |

**Choice for this project:**
- **`gpt-image-2.5-sunburst`** for master character sheets and hero backgrounds.
- **`gpt-image-2.5-flare`** for bulk emotion, pose and overlay variants.
- Transparent PNG/WebP cut-outs need a **2.5-series** model (or 1.5 as a fallback). Do not use `gpt-image-2` for alpha.

---

## 2. API surface

### Endpoints
- `POST /v1/images/generations`: text → image.
- `POST /v1/images/edits`: image(s) (+ optional mask) + text → image. Accepts **up to 16 input images** for GPT image models. **The mask applies to the first image only.** The mask is a PNG with an alpha channel, same size as the image, under 4 MB. Transparent pixels mark the editable region ([OpenAI reference: create image edit](https://developers.openai.com/api/reference/resources/images/methods/edit), [OpenAI guide](https://developers.openai.com/api/docs/guides/image-generation), [community summary](https://docs.aimlapi.com/api-references/image-models/openai/gpt-image-1)).
- **Responses API `image_generation` tool**: multi-turn editing via `previous_response_id`, or by passing earlier image-generation call IDs back in. Streaming with `partial_images` 0–3 ([OpenAI guide](https://developers.openai.com/api/docs/guides/image-generation), [OpenAI Responses tools](https://openai.com/index/new-tools-and-features-in-the-responses-api/)). Good for conversational refinement. For a reproducible asset library, prefer explicit `/images/edits` calls with saved reference files.

### Parameters (GPT-image family; check per model)
| Param | Values | Notes |
|---|---|---|
| `model` | `gpt-image-2.5-flare`, `gpt-image-2.5-sunburst`, `gpt-image-2`, `gpt-image-1.5` | |
| `size` | presets `1024x1024`, `1536x1024`, `1024x1536`, `auto`; **custom sizes allowed** for 2 / 2.5: both edges multiples of 16, max edge 3840, long:short ≤ 3:1, total pixels 655,360–8,294,400 ([OpenAI image-prompting guide](https://developers.openai.com/api/docs/guides/image-prompting), [Cloudflare docs](https://developers.cloudflare.com/ai/models/openai/gpt-image-2/), [seeapi](https://www.seeapi.com/blogs/news/gpt-image-2-5-whats-new/)) | **9:16 options:** `720x1280` (valid: 45×16 by 80×16, 921,600 px, the exact target size), **`1152x2048`** (recommended master), `2160x3840` (4K; outputs above 2560×1440 are labelled *experimental*). `1080x1920` is **invalid** because 1080 is not a multiple of 16; use `1088x1920` and crop |
| `quality` | `low`, `medium`, `high`, `auto`; 2.5 adds `xhigh`, `max` *(3rd-party: [fal](https://fal.ai/gpt-image-2.5))* | Higher quality costs more output tokens and time ([APIYI perf](https://help.apiyi.com/en/gpt-image-2-api-performance-tuning-quality-size-guide-en.html)) |
| `background` | `auto`, `opaque`, `transparent` | `transparent` requires `output_format` **png** or **webp** ([OpenAI guide](https://developers.openai.com/api/docs/guides/image-prompting), [DataCamp](https://www.datacamp.com/blog/chatgpt-images-2-5)) |
| `output_format` | `png`, `webp`, `jpeg` | Defaults vary by model and provider; always set it explicitly |
| `output_compression` | 0–100 (webp/jpeg) | |
| `moderation` | `auto`, `low` | |
| `n` | number of images | Use n>1 for candidate selection |
| `input_fidelity` | — | **Omit for gpt-image-2 / 2.5.** Inputs are always processed at high fidelity, and sending the parameter can error ([OpenAI cookbook](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide), [image-prompting guide](https://developers.openai.com/api/docs/guides/image-prompting)) |

There is **no seed parameter**. Reproducibility comes from **saved reference images plus a fixed text "style bible"**, not from seeds.

**Pricing:** 2.5 Flare and Sunburst are reported at **$30 per 1M output tokens** ([DataCamp](https://www.datacamp.com/blog/chatgpt-images-2-5)). Reference images are billed as input at high fidelity, so **downscale references** to what the job needs, for example a 1024-px head reference ([APIYI guide](https://docs.apiyi.com/en/api-capabilities/gpt-image-2/overview)).

### Minimal Python (openai SDK)
```python
from openai import OpenAI
import base64
client = OpenAI()

# 1) generate a background plate (opaque, 9:16)
r = client.images.generate(model="gpt-image-2.5-sunburst", prompt=BG_PROMPT,
                           size="1152x2048", quality="high", output_format="png")
open("bg_beach_day.png","wb").write(base64.b64decode(r.data[0].b64_json))

# 2) same character, new emotion, transparent PNG, using master refs
r = client.images.edit(model="gpt-image-2.5-flare",
        image=[open("char/Bob/master_front.png","rb"),      # image 1 = identity
               open("char/Bob/expr_sheet_v1.png","rb")],     # image 2 = style/expression vocab
        prompt=EMOTION_PROMPT.format(emotion="shocked"),
        size="1024x1024", background="transparent", output_format="png", quality="high")
```
After every transparent output, **check the alpha channel**: `Image.open(p).getchannel('A').getextrema()` must include 0. A drawn checkerboard is *not* transparency ([ofox](https://ofox.ai/blog/gpt-image-2-5-transparent-background/)).

---

## 3. Prompting principles (OpenAI cookbook plus field guides)

From OpenAI's **GPT Image Generation Models Prompting Guide** ([cookbook](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)) and the image-prompting doc ([guide](https://developers.openai.com/api/docs/guides/image-prompting)), as summarised by [i-scoop](https://www.i-scoop.eu/prompting-gpt-image-2-like-a-pro-guide/), [fal](https://fal.ai/learn/tools/prompting-gpt-image-2) and [felo](https://felo.ai/blog/openai-gpt-image-2-5-prompting-guide-decoded/):
1. **Consistent order:** background/scene → subject → key details → constraints. Use **labelled segments** (STYLE:, SUBJECT:, COMPOSITION:, CONSTRAINTS:) for complex requests.
2. **Text in images:** put the exact string in quotes, say it is verbatim, and specify placement, font style and colour. This matters for UI overlays like "NIGHT 1 · 9:42 PM".
3. **Edits:** keep the change narrow ("change only X"), **repeat the preserve list every time**, and make one change per iteration. Use an **approved master as the source of truth**, never the latest output, because drift compounds ([Leadde](https://leadde.ai/blog/how-to-keep-characters-consistent-in-gpt-image-2-5-fix-face-and-pose-drift), [wavespeed](https://wavespeed.ai/blog/posts/gpt-image-2-api-guide/)).
4. **Multi-reference:** give each input image one role and refer to them by upload order ("image 1 = identity, image 2 = style, image 3 = pose"). More references are not automatically better, because conflicting refs get blended ([APIYI consistency](https://help.apiyi.com/en/gpt-image-multi-image-generation-consistency-guide-en.html), [mindstudio](https://www.mindstudio.ai/blog/what-is-gpt-image-2-openai)).
5. **One sheet, one purpose:** a turnaround sheet *or* an expression grid *or* an outfit set, never a crowded mix. Specify the grid, equal scale, fixed lighting and "do not crop" ([nanoprompts](https://nanoprompts.org/gpt-image-2/prompt-handbook/character), [image3](https://image3.org/blog/gpt-image-2-character-sheet-prompts), [gpt-image2ai](https://gpt-image2ai.com/blog/gpt-image-2-character-sheet-prompts)).
6. **For pixel-exact needs, composite deterministically.** Prompting cannot guarantee identical pixels ([felo](https://felo.ai/blog/gpt-image-2-5-prompting-guide/)). For face swapping, this means generating **facial features on a fixed head**, then aligning in code (see §5).
7. **Transparent sprites:** ask for an isolated subject with no floor, no cast shadow, no text and generous margins, *and* set `background:"transparent"`. Hair-like tufts, glows and semi-transparent smoke are where alpha breaks, so inspect them ([ofox](https://ofox.ai/blog/gpt-image-2-5-transparent-background/), [poyo sprite tutorial](https://poyo.ai/hub/gpt-image-2-5-sprite-sheet), [Indie Hackers](https://www.indiehackers.com/post/gpt-image-2-5-a-full-sprite-sheet-from-one-reference-110562d19f)).

**In the ChatGPT app** (Images 2.5): upload the master and ask for edits in the same thread. Use **image comments** to target a region, and the **Sketch** tool to block a pose ([DataCamp](https://www.datacamp.com/blog/chatgpt-images-2-5)). Transparent output in the app is unreliable, according to users on the [OpenAI forum](https://community.openai.com/t/having-trouble-getting-transparent-backgrounds-in-chatgpt-images/1380143). Use the API for alpha assets, or run `rembg` as a fallback ([github.com/danielgatis/rembg](https://github.com/danielgatis/rembg), MIT).

---

## 4. Style bible (paste at the top of every prompt)

```
STYLE BIBLE — "Bean-head explainer" (do not deviate):
- 2D cartoon character, clean vector-like cel shading, THICK dark navy/near-black outline (uniform ~6px at 1024px).
- Head: very large, perfectly round, pale lavender-white (#E9E6F2-ish) with subtle cool shading on the lower-left,
  2–3 small hair tufts on top, tiny rosy-pink oval cheeks, small solid dark oval eyes with a tiny white highlight,
  simple single-line mouth. No nose, no ears.
- Body: small pill/capsule torso about 0.8× head width, wearing a patterned shirt; very thin stick arms and legs
  drawn as single thick dark lines; tiny simple shoes. Head:body ratio ≈ 1:1.
- Palette: saturated but soft; no gradients on the character except one soft shade band.
- Rendering: flat colours, crisp edges, no texture, no painterly brushwork on the character, no drop shadow.
```
Background bible (separate on purpose: the reference contrast is *simple character on rich painterly world*):
```
BACKGROUND BIBLE:
- Highly detailed painterly illustration with a soft 2.5D / semi-3D look (like a high-end animated feature
  background painting), volumetric light, depth haze, rich foliage detail, slightly stylised proportions.
- Vertical 9:16 composition, strong readable silhouette, empty middle-ground floor area (lower 35–60 % of frame)
  where a character will be composited; nothing important behind the vertical centre line at 45–55 % height
  (captions sit there).
- No people, no characters, no text, no logos.
```

---

## 5. Character consistency workflow (fits CLAUDE.md rule 3: `library/characters/<Name>/emotions/`)

1. **Master (identity) image.** Sunburst, 1024×1024, transparent, front view, neutral expression, full body. Generate n=4, pick one, and freeze it as `master_front.png`. This is the single source of truth.
2. **Head-only master.** Edit the master: "crop to head only, same drawing", at a fixed canvas such as 768×768 with the head centred and the circle diameter fixed. Freeze as `head_neutral.png`.
3. **Emotions.** For each emotion, run `images.edit` with `image=[head_neutral.png]` and the emotion prompt. **Never chain from a previous emotion.**
   - Optional: a mask (alpha = 0 over the face interior only) so the outline stays put. Masks act as soft guidance on GPT-image models and the whole image may still be regenerated ([OpenAI forum](https://community.openai.com/t/gpt-image-1-problems-with-mask-edits/1240639)). So **always post-align**: detect the head circle with OpenCV `HoughCircles` or an alpha-mask fit, then scale and translate to the master's centre and diameter. Optionally, paste only the *interior features* onto the exact master head disc for pixel-identical outlines (the deterministic-compositing advice above).
4. **Expression sheet** (optional, for review and vocabulary). A 3×3 grid at 1536×1536 with the same head. Use it as image 2 (style vocabulary) in later edits, not as the asset source. Slicing grids gives inconsistent scale.
5. **Turnaround / poses.** Edit from `master_front.png`, with "image 1 = identity" and the pose described in words, transparent. Typical poses for this style: standing neutral, hands on hips, sitting on ground legs out, crouching, running, holding object, lying down, pointing, shrugging, arms raised in panic.
6. **Validation.** Automatically compare each output to the master: head-circle diameter within ±2%, outline colour, shirt palette (k-means on the shirt region), and alpha present. Reject and regenerate on failure.

### Emotion list matching the reference videos
`neutral`, `content-smile (closed eyes, rosy)`, `worried (brows up, small wavy mouth)`, `shocked (wide white eyes with tiny pupils, open O mouth, single blue sweat drop)`, `crying (closed/upturned eyes, two thick light-blue tear streams down cheeks)`, `gritted-teeth pain (eyes squeezed > <, rectangular white teeth)`, `blushing-happy (closed arc eyes, big pink cheeks)`, `annoyed/flat (half-lidded eyes, straight mouth)`, `angry (V brows)`, `dead/KO (X eyes)`, `sick (greenish tint, spiral eyes)`, `sunburnt-panic (whole head red, sweat, steam puffs)`. All of these appear in video 1 (see contact sheets in the analysis folder).

---

## 6. Prompt templates (copy-ready)

### 6.1 Master character (transparent)
```
{STYLE BIBLE}
SUBJECT: one adult male "bean-head" character named BOB, full body, front view, standing relaxed, arms hanging,
neutral expression (small dark oval eyes, short flat mouth). Shirt: short-sleeve orange Hawaiian shirt with white
five-petal flowers and green leaves, open collar. Navy shorts, tiny white-and-brown sandals.
COMPOSITION: centred, whole figure visible with 10 % margin on every side, feet on an invisible baseline.
CONSTRAINTS: transparent background, no floor, no shadow, no text, no extra characters.
```
API: `images.generate(model="gpt-image-2.5-sunburst", size="1024x1536", background="transparent", output_format="png", quality="high", n=4)`

### 6.2 Same face, different emotion (edit)
```
Image 1 is the approved head of BOB. Keep EXACTLY: head size, perfectly round head outline and line weight,
pale lavender-white skin colour, hair tufts (same count, shape, position), cheek positions, canvas size and
head position. Change ONLY the facial expression to: SHOCKED — eyes become large white circles with tiny black
pupils, eyebrows raised high, mouth a small open dark oval, one light-blue sweat drop at upper right of head.
Transparent background, no shadow, no text.
```
`images.edit(model="gpt-image-2.5-flare", image=[head_neutral.png], size="768x768", background="transparent", output_format="png")`

### 6.3 Expression sheet (review)
```
{STYLE BIBLE}
Image 1 is BOB's approved head. Create a 3×3 expression sheet of BOB's HEAD ONLY, identical head size, outline,
tufts and colours in every cell, evenly spaced, each cell same scale, no labels, transparent background.
Row 1: neutral, content smile with closed eyes, worried. Row 2: shocked with sweat drop, crying with two blue tear
streams, gritted teeth in pain. Row 3: blushing happy, annoyed half-lidded, dead with X eyes.
```

### 6.4 Pose sheet / turnaround
```
{STYLE BIBLE}
Image 1 is the approved full-body BOB. Draw BOB in this pose: sitting on the ground, legs stretched forward,
leaning back on both hands, content smile with closed eyes. Same proportions, same shirt pattern scale and colours,
same line weight. Three-quarter view facing right. Transparent background, no floor, no shadow.
```
For a turnaround: "front, three-quarter left, side left, back, in a 4-column row, equal scale, same baseline, no labels." Keep it a separate request from the expression sheet.

### 6.5 Background plate (opaque, 9:16)
```
{BACKGROUND BIBLE}
SCENE: deserted tropical beach at midday. On the left third, a single leafy manchineel tree with a thick curved
trunk and dense glossy green leaves, small green apple-like fruits hanging; a bold red painted X on the trunk at
about 40 % height. Turquoise sea and white surf band at 45 % height, bright blue sky with soft cumulus.
Warm sunlight from upper right, soft dappled shade under the canopy.
COMPOSITION: camera at standing eye level, slight low angle; empty sand area in lower centre for a character.
```
`size="1152x2048", quality="high", background="opaque"`

**Lighting variants (same plate):** edit with image 1 = the day plate.
`"Keep composition, objects, and camera IDENTICAL. Change only the time of day to: night, cold blue moonlight, heavy rain streaks, dark storm clouds, wet sand reflections."` Other variants: "golden-pink sunset sky", "warm orange firelight from a small campfire at lower centre". Run each variant from the **day master**, not chained.

### 6.6 "Unique images" / fake UI (opaque, text verbatim)
```
Vertical 9:16 smartphone-style weather radar screen, dark navy UI. Top centre small teal caps text "SATELLITE · LIVE",
below it large white bold sans text "NIGHT 1 · 9:42 PM". Full-screen satellite radar map of a small tropical island
with swirling white storm clouds and green-yellow-red precipitation bands; a small white circle marker with label "YOU"
at the island centre. Bottom: rounded red pill banner with a yellow warning triangle icon and white bold text
"SEVERE STORM". Text must be exactly as quoted, crisp, correctly spelled. No other text.
```
Similar templates:
- Thermal camera: header "THERMAL" left, "LUNGS: 451°F" right, a colour-bar scale, the BOB head on top, and orange-yellow lungs.
- X-ray: "X-RAY", "THROAT: ON FIRE", a glowing cyan skeleton of a bean-head figure.
- Vintage botanical poster: aged parchment, an engraved tree illustration, a title in serif caps "MANCHINEEL", and a Latin subtitle "Hippomane mancinella".
- Macro diagrams: a leaf close-up with a dashed callout labelled "MILKY SAP", and a skin cross-section labelled "INSIDE YOUR SKIN".

Build **numbers and clock text as overlays in code** when they must animate, because generated text is static.

### 6.7 Transparent FX overlays
```
Single cartoon smoke puff cluster: 4 overlapping round white puffs with thick dark outline matching the bean-head
style, flat light-grey shading, isolated, transparent background, no shadow.
```
Other overlays: "bold hand-painted red X mark, slightly dripping", "light-blue sweat drop", "pair of thick light-blue tear streams (to place under eyes)", "yellow four-point sparkle stars ×3", "wavy heat lines". For animated FX, generate 3–4 variants ("variation 1 of 4, same style, slightly different puff arrangement") and cycle them every 2–3 frames to get the boil seen in the reference.

---

## 7. Fallbacks and alternatives
- **Google Nano Banana Pro** (Gemini 3 Pro Image) takes up to about 14 reference images with multi-character consistency, which makes it a good second opinion for scenes with several characters ([wavespeed](https://wavespeed.ai/blog/posts/google-nano-banana-pro-complete-guide-2026), [techspot](https://www.techspot.com/news/110342-google-nano-banana-pro-model-makes-ai-images.html)).
- Background removal for opaque outputs: `rembg` (MIT).
- If identity drift is unacceptable, generate **parts** (head disc, face features, shirt torso, limbs drawn procedurally as strokes) and assemble them in code. See `face_animation_github.md`.

---

## Sources
- OpenAI: Introducing ChatGPT Images 2.5: https://openai.com/index/introducing-chatgpt-images-2-5/
- OpenAI image generation guide: https://developers.openai.com/api/docs/guides/image-generation
- OpenAI image prompting guide: https://developers.openai.com/api/docs/guides/image-prompting
- OpenAI API reference: create image edit: https://developers.openai.com/api/reference/resources/images/methods/edit (python: https://developers.openai.com/api/reference/python/resources/images/methods/edit)
- OpenAI Cookbook: GPT Image Generation Models Prompting Guide: https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide
- OpenAI Responses API tools: https://openai.com/index/new-tools-and-features-in-the-responses-api/
- OpenAI community (gpt-image-2 transparency): https://community.openai.com/t/is-transparent-background-support-broken-in-gpt-image-2/1402707 ; https://community.openai.com/t/transparent-backgrounds-are-now-available-in-preview-for-gpt-image-2-in-the-api/1391541?page=2 ; https://community.openai.com/t/having-trouble-getting-transparent-backgrounds-in-chatgpt-images/1380143
- OpenAI community (mask behaviour): https://community.openai.com/t/gpt-image-1-problems-with-mask-edits/1240639 ; https://community.openai.com/t/image-editing-inpainting-with-a-mask-for-gpt-image-1-replaces-the-entire-image/1244275
- openai/codex issue #43757: https://github.com/openai/codex/issues/43757
- DataCamp Images 2.5: https://www.datacamp.com/blog/chatgpt-images-2-5
- Unite.AI: https://www.unite.ai/openai-releases-chatgpt-images-2-5-with-sketch-and-two-new-api-models/
- The Rundown: https://www.therundown.ai/news/openai-chatgpt-images-2-5-speed-editing-arena
- Wikipedia GPT Image: https://en.wikipedia.org/wiki/GPT_Image
- digitalapplied (Images 2.0): https://www.digitalapplied.com/blog/chatgpt-images-2-0-features-use-cases-impact
- TheNextWeb (gpt-image-2): https://thenextweb.com/news/openai-chatgpt-images-2-0-reasoning-image-generation
- Fortune (gpt-image-1.5): https://fortune.com/2025/12/16/openai-releases-new-image-model-as-it-races-to-outpace-googles-nano-banana-amid-company-code-red/
- invideo (deprecations): https://invideo.io/blog/gpt-image-ai-image-generator/
- Cloudflare gpt-image-2 docs: https://developers.cloudflare.com/ai/models/openai/gpt-image-2/
- seeapi 2.5 sizes: https://www.seeapi.com/blogs/news/gpt-image-2-5-whats-new/
- fal GPT Image 2.5: https://fal.ai/gpt-image-2.5
- ofox 2.5 API / transparency: https://ofox.ai/blog/gpt-image-2-5-api-guide/ ; https://ofox.ai/blog/gpt-image-2-5-transparent-background/
- APIYI (transparency removal, performance, consistency): https://help.apiyi.com/en/gpt-image-2-transparent-background-not-supported-fix-en.html ; https://help.apiyi.com/en/gpt-image-2-api-performance-tuning-quality-size-guide-en.html ; https://help.apiyi.com/en/gpt-image-multi-image-generation-consistency-guide-en.html ; https://docs.apiyi.com/en/api-capabilities/gpt-image-2/overview
- wavespeed gpt-image-2 guide: https://wavespeed.ai/blog/posts/gpt-image-2-api-guide/
- mindstudio: https://www.mindstudio.ai/blog/what-is-gpt-image-2-openai
- Leadde (2.5 drift): https://leadde.ai/blog/how-to-keep-characters-consistent-in-gpt-image-2-5-fix-face-and-pose-drift
- i-scoop prompting: https://www.i-scoop.eu/prompting-gpt-image-2-like-a-pro-guide/
- fal prompting gpt-image-2: https://fal.ai/learn/tools/prompting-gpt-image-2
- felo 2.5 guides: https://felo.ai/blog/gpt-image-2-5-prompting-guide/ ; https://felo.ai/blog/openai-gpt-image-2-5-prompting-guide-decoded/
- Character sheets: https://nanoprompts.org/gpt-image-2/prompt-handbook/character ; https://image3.org/blog/gpt-image-2-character-sheet-prompts ; https://gpt-image2ai.com/blog/gpt-image-2-character-sheet-prompts ; https://image-2.net/blog/gpt-image-2-character-reference-sheet/
- Sprite sheets: https://poyo.ai/hub/gpt-image-2-5-sprite-sheet ; https://www.indiehackers.com/post/gpt-image-2-5-a-full-sprite-sheet-from-one-reference-110562d19f
- Nano Banana Pro: https://wavespeed.ai/blog/posts/google-nano-banana-pro-complete-guide-2026 ; https://www.techspot.com/news/110342-google-nano-banana-pro-model-makes-ai-images.html
- rembg: https://github.com/danielgatis/rembg
