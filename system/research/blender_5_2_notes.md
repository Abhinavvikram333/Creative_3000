# Blender 5.2 LTS: notes for automating 2.5D vertical Shorts

Researched 2026-10-27. Most blender.org pages could not be fetched directly from this sandbox. Facts marked **[src]** were checked against the Blender source on the official GitHub mirror (`blender/blender`, branch `blender-v5.2-release`, read through raw.githubusercontent.com). The other facts come from web-search extracts of the official release notes and manual, and are cited.

---

## 1. Version facts

| Item | Value |
|---|---|
| Release | **Blender 5.2 LTS**, released **14 July 2026**. It is the first LTS in the 5.x series and is supported until July 2028 ([release notes](https://developer.blender.org/docs/release_notes/5.2/), [Phoronix](https://www.phoronix.com/news/Blender-5.2-Released)) |
| Current patch | **5.2.3**. Source has `BLENDER_VERSION 502`, `BLENDER_VERSION_PATCH 3`, `CYCLE release` **[src]**. blender.org dates 5.2.3 to 22 Oct 2026 ([blender.org 5.2](https://www.blender.org/download/releases/5-2/)). 5.2.2 shipped 15 Sep 2026 ([SteamDB](https://steamdb.info/patchnotes/25315940/)) |
| Next | 5.3 is in public beta. It makes **Vulkan the default backend on Windows/Linux** ([5.3 notes](https://developer.blender.org/docs/release_notes/5.3/eevee/), [LinuxToday](https://www.linuxtoday.com/blog/blender-5-3-enters-public-beta-testing-with-vulkan-backend-by-default-on-linux/)), so 5.2 still defaults to OpenGL |
| Python | 3.13. This changed in 5.1 and affects compiled add-ons only ([CG Channel 5.1](https://www.cgchannel.com/2026/03/discover-5-key-features-in-blender-5-1/), [Strayspark](https://www.strayspark.studio/blog/blender-5-1-addon-compatibility-python-313-guide)) |

**Recommendation:** pin the pipeline to **5.2.x LTS**. It gets two years of fixes, and API churn between 5.2.x patches should be small.

---

## 2. What is new in 5.x that matters for this style

### 5.2 (July 2026)
- **VSE Compositor effect strip.** A new effect strip runs a compositor node tree directly on the timeline, with zero, one or two inputs. That makes custom transitions and glow/blur/vignette possible inside the VSE. Compositor node trees can also be saved as **Strip Modifier assets**. Strip modifiers now expose node-group inputs in their panel, and fully opaque results take a faster render path ([5.2 Sequencer notes](https://developer.blender.org/docs/release_notes/5.2/sequencer/)). `COMPOSITOR` is a valid `type` for `strips.new_effect()` **[src]**.
- **Text strips.** Line spacing can be relative or absolute in pixels (`space_line`, `abs_space_line`, `use_absolute_line_spacing` **[src]**), and there are **style presets** (Subtitles, Main Title, Corner Title). A third-party write-up says text strips are no longer capped at 512 bytes and that bounding boxes now fit the text ([5.2 Sequencer notes](https://developer.blender.org/docs/release_notes/5.2/sequencer/), [MakeUseOf](https://www.makeuseof.com/blenders-video-editor-became-something-actually-use/)).
- **Scene strips** gain a view-layer selector and a workbench-world override ([5.2 Sequencer notes](https://developer.blender.org/docs/release_notes/5.2/sequencer/)).
- **Compositor.** 35 new nodes and six new socket types (Matrix, Rotation, String, Object, Font, Integer Vector). New nodes include **Blank Image** and **String To Image** (useful for procedural labels). A Switch with a fixed condition is now evaluated lazily, the Group Output node shows execution time, and File Output has its own extension checkbox ([5.2 Compositor notes](https://developer.blender.org/docs/release_notes/5.2/compositor/), [CG Channel](https://www.cgchannel.com/2026/07/blender-5-2-lts-is-here-discover-its-5-key-features/)).
- **Grease Pencil.** A new **Delaunay fill** algorithm is now the default: exact geometry, automatic gap detection, inverse fill, zoom independent. Dots/Squares line materials get placement settings and are generated at render time. The Draw tool can choose its curve type (Bézier, Catmull-Rom, NURBS). The online Essentials library adds textured brushes ([5.2 Grease Pencil notes](https://developer.blender.org/docs/release_notes/5.2/grease_pencil/), [BlenderNation](https://www.blendernation.com/2026/07/06/blender-5-2-grease-pencil-16-new-features-breakdown/)).
- **EEVEE.** Lights get camera-ray visibility, instancing is up to 2× faster, and SSR was overhauled ([Phoronix](https://www.phoronix.com/news/Blender-5.2-Released)).
- **Geometry Nodes.** New Sample Sound Frequencies node and Sound socket (audio-reactive motion), Transfer Attributes node, Bundles and Lists ([Phoronix](https://www.phoronix.com/news/Blender-5.2-Released)).
- **Online asset libraries** (remote libraries, downloaded on demand) ([Phoronix](https://www.phoronix.com/news/Blender-5.2-Released)).

### 5.1 (17 March 2026)
- Grease Pencil fills can have holes. Fill vs stroke is now a per-line attribute. New Python API: `LayerGroup.children`, `GreasePencil.root_nodes`, stroke `fill_id`/`hide_stroke`, `layer.layer_masks.add/remove` ([5.1 GP notes](https://developer.blender.org/docs/release_notes/5.1/grease_pencil/), [CG Channel](https://www.cgchannel.com/2026/03/discover-5-key-features-in-blender-5-1/)).
- Compositor: **Mask to SDF** node (handy for outline/glow around cut-outs), Mix now mixes alpha, Glare/Blur up to 2× faster ([CG Channel](https://www.cgchannel.com/2026/03/discover-5-key-features-in-blender-5-1/)).
- VSE strip time properties renamed (`frame_final_duration` → `duration`, and so on). The old names are deprecated and will be removed in 6.0 ([5.1 Python API](https://developer.blender.org/docs/release_notes/5.1/python_api/)).

### 5.0 (Nov 2025): the big breaking API release
- **Compositor:** `scene.node_tree` was **removed**. Use `scene.compositing_node_group`, a stand-alone `CompositorNodeTree` data-block that you create and assign. The Composite node was replaced by **Group Output**, and `scene.use_nodes` is deprecated and always returns True ([5.0 Python API](https://developer.blender.org/docs/release_notes/5.0/python_api/), [interplanety](https://b3d.interplanety.org/en/changes-in-node-tree-creation-for-compositor-in-blender-5-0/)). Confirmed in 5.2 source: only `compositing_node_group` exists **[src]**.
- **Animation:** `Action.fcurves`, `Action.groups` and `Action.id_root` were **removed** (slotted/layered actions). Use `bpy_extras.anim_utils.action_ensure_channelbag_for_slot(action, slot).fcurves` ([5.0 Python API](https://developer.blender.org/docs/release_notes/5.0/python_api/), [BlenderArtists](https://blenderartists.org/t/how-to-access-fcurves-in-blender-5-0/1623022)). `obj.keyframe_insert()` still works and is the simplest path.
- **Render output:** `image_settings.media_type` (`IMAGE` / `MULTI_LAYER_IMAGE` / `VIDEO`) must be set **before** `file_format='FFMPEG'`, otherwise a TypeError is raised ([bug #152175](https://projects.blender.org/blender/blender/issues/152175), [terminalskills](https://terminalskills.io/skills/blender-render-automation)). Enum items confirmed **[src]**.
- **VSE:** `sequence_editor.sequences` is gone. Use `sequence_editor.strips` (top level) and `strips_all` ([TMHSDigital #502](https://github.com/TMHSDigital/Blender-Developer-Tools/issues/502)). Confirmed: 5.2 source defines `strips` ("Top-level strips only") and `strips_all`, and no `sequences` **[src]**.
- **Grease Pencil data:** `bpy.data.grease_pencils_v3` existed only in 4.3–4.5. In 5.x, `bpy.data.grease_pencils` holds the v3 type ([BlenderArtists](https://blenderartists.org/t/how-to-use-the-grease-pencil-api-to-draw-strokes/1613077)). The 5.2 source still names the RNA struct `BlendDataGreasePencilsV3` internally **[src]**.

### 5.2 compatibility gotchas
- The Geometry Nodes modifier property API was refactored. Old `mod["Socket_2"]` dict paths break; use `modifier.properties.inputs.<identifier>.value`. Compare/Random Value socket identifiers changed ([compatibility index](https://developer.blender.org/docs/release_notes/compatibility/), [3dredbox](https://www.3dredboxstudio.com/blog/blender-5-2-geometry-nodes-modifier-api-what-broke)).
- `paint.eraser_brush*` removed ([Phoronix](https://www.phoronix.com/news/Blender-5.2-Released)).

---

## 3. Python API cheat-sheet for this pipeline (5.2)

### 3.1 Scene / output (720×1280, 30 fps)
```python
import bpy
sc = bpy.context.scene
sc.render.resolution_x, sc.render.resolution_y = 720, 1280
sc.render.resolution_percentage = 100
sc.render.fps, sc.render.fps_base = 30, 1.0
sc.frame_start, sc.frame_end = 1, 30 * 60
# keep AI-art colours exactly as generated (AgX/Filmic would shift them)
sc.view_settings.view_transform = 'Standard'
sc.view_settings.look = 'None'
# video output: media_type FIRST (5.0+)
ims = sc.render.image_settings
ims.media_type = 'VIDEO'
ims.file_format = 'FFMPEG'
sc.render.ffmpeg.format = 'MPEG4'
sc.render.ffmpeg.codec = 'H264'
sc.render.ffmpeg.audio_codec = 'AAC'
sc.render.filepath = '//out/short.mp4'
```
The colour-management tip is standard practice for flat 2D art: emission-shaded planes plus the Standard view transform give pixel-faithful colours. Choose the engine as described in §4.

### 3.2 Image planes (backgrounds, characters, faces, overlays)
The built-in operator in 5.2 is **`bpy.ops.image.import_as_mesh_planes`**, with a companion `image.convert_to_mesh_plane` **[src]** (file `scripts/startup/bl_operators/image_as_planes.py`). Key properties **[src]**:
`files`, `directory`, `shader` (`PRINCIPLED`/`SHADELESS`/`EMISSION`), `emit_strength`, `render_method` (`DITHERED`/`BLENDED`), `use_transparency` (default True), `interpolation` (`Linear`/`Closest`/`Cubic`/`Smart`), `extension`, `relative`, `image_sequence`, `offset`, `offset_axis`, `offset_amount`, `align_axis` (`CAM`, `CAM_AX`, ±X/Y/Z), `align_track`, `size_mode` (`ABSOLUTE`/`CAMERA`/`DPI`/`DPBU`), `fill_mode` (`FILL`/`FIT`), `height`, `factor`.

```python
bpy.ops.image.import_as_mesh_planes(
    files=[{"name": "bg_beach.png"}], directory="/abs/assets/bg/",
    shader='SHADELESS', use_transparency=True, render_method='BLENDED',
    size_mode='CAMERA', fill_mode='FILL', align_axis='CAM_AX', relative=False)
plane = bpy.context.active_object
```
Operators need a valid context. In `blender -b` they generally work for import operators, but the most robust headless path is to **build the plane yourself**: `bpy.data.meshes.new` + `from_pydata` with 4 verts and UVs, plus a material that uses an Image Texture → Emission (or a Mix with Transparent BSDF using alpha). That avoids operator-context issues.

**Face swapping (owner rule: per-emotion PNGs).** Three options:
1. One plane per emotion, keying `hide_render`/`hide_viewport` with **CONSTANT** interpolation.
2. A single plane whose Image Texture uses `image.source = 'SEQUENCE'` (files `face_0001.png` … one per emotion). Key `node.image_user.frame_offset` with constant interpolation, or drive `frame_current` through a handler. Set `image_user.use_auto_refresh = True`.
3. `bpy.app.handlers.frame_change_pre` swaps `node.image` from a timeline JSON. Handlers run during `-b -a` renders. Make them `@persistent` if a .blend is reloaded.

### 3.3 Camera: push-ins, drift, parallax, punch-ins
- Use a perspective camera with planes spaced in Z (bg at -20, mid at -8, character at -4, fg at -2), each scaled to stay frame-filling. A dolly move then gives true parallax for free. An orthographic camera gives none, so use perspective. (Superhive "Parallax Layers" automates the spreading and scaling: [Superhive](https://superhivemarket.com/products/2-5d-parallax).)
- Keyframes: `cam.keyframe_insert('location', frame=f)`. To set easing, edit F-curves through the 5.x channelbag API:
```python
from bpy_extras import anim_utils
ad = cam.animation_data
cb = anim_utils.action_ensure_channelbag_for_slot(ad.action, ad.action_slot)
for fc in cb.fcurves:
    for kp in fc.keyframe_points:
        kp.interpolation = 'BEZIER'; kp.easing = 'EASE_IN_OUT'
```
- **Punch-in close-ups** = a hard cut to a new camera (markers: `sc.timeline_markers.new('c', frame=f).camera = cam2`) or a 2–3-frame ease of `cam.data.lens`.
- **Camera shake**: an F-curve **Noise modifier** (`fc.modifiers.new('NOISE')`) on location/rotation.
- **Fisheye peephole POV**: Cycles panoramic camera (`cam.data.type='PANO'`, `panorama_type='FISHEYE_EQUISOLID'`), or a lens-distortion node in the compositor.
- **Soft drop shadows** under characters: a duplicate plane tinted black, blurred alpha, offset, low opacity. Alternatively use a real light with shadow-catcher-like setups, but a fake shadow plane is cheaper and closer to the look.

### 3.4 Compositor (5.x API)
```python
tree = bpy.data.node_groups.new("Comp", 'CompositorNodeTree')
sc.compositing_node_group = tree
out = tree.nodes.new('NodeGroupOutput')
tree.interface.new_socket('Image', in_out='OUTPUT', socket_type='NodeSocketColor')
rl = tree.nodes.new('CompositorNodeRLayers')
glare = tree.nodes.new('CompositorNodeGlare')   # sparkles / bloom
tree.links.new(rl.outputs['Image'], glare.inputs['Image'])
tree.links.new(glare.outputs['Image'], out.inputs[0])
```
(`node_groups.new(name, type)` signature **[src]**. Group Output replaces Composite since 5.0: [5.0 Python API](https://developer.blender.org/docs/release_notes/5.0/python_api/).) Node input names changed in 5.0, when many options became sockets, so check names in the 5.2 UI or with `[s.name for s in node.inputs]`.

### 3.5 VSE: word-by-word captions as text strips
`strips.new_effect(name, type, channel, frame_start, length=0, input1=None, input2=None)`. There is **no `frame_end` argument**; use `length` **[src]**. Other creators: `new_image(name, filepath, channel, frame_start, fit_method)`, `new_movie(..., fit_method, stream)`, `new_sound(...)`, `new_scene(name, scene, channel, frame_start)` **[src]**.

TextStrip properties in 5.2 **[src]**: `text`, `font` (VFont), `font_size` (0–2000), `color`, `use_bold`, `use_italic`, `use_shadow`, `shadow_color`, `shadow_angle`, `shadow_offset`, `shadow_blur`, `use_outline`, `outline_color`, `outline_width` (0–1), `use_box`, `box_color`, `box_margin`, `box_roundness`, `location` (normalised x,y), `wrap_width`, `anchor_x/anchor_y` (LEFT/CENTER/RIGHT, TOP/CENTER/BOTTOM), `alignment_x`, `space_line`, `abs_space_line`, `use_absolute_line_spacing`. Strip transform: `strip.transform.offset_x/offset_y/scale_x/scale_y/rotation/origin` **[src]**.

```python
se = sc.sequence_editor or sc.sequence_editor_create()
font = bpy.data.fonts.load('/abs/fonts/Montserrat-ExtraBold.ttf')
for w in words:   # from WhisperX / SRT alignment: w.text, w.start, w.end (seconds)
    s = se.strips.new_effect(name=f"w{w.i}", type='TEXT', channel=5,
                             frame_start=round(w.start*30)+1,
                             length=max(1, round((w.end-w.start)*30)))
    s.text = w.text; s.font = font; s.font_size = 64
    s.color = (1,1,1,1); s.use_outline = True; s.outline_color = (0,0,0,1); s.outline_width = 0.12
    s.use_shadow = True; s.shadow_blur = 0.3
    s.location = (0.5, 0.5); s.anchor_x = s.anchor_y = 'CENTER'; s.alignment_x = 'CENTER'
```
To combine the 3D camera render with VSE captions, render the 3D scene through a **Scene strip** (`new_scene`) inside a separate "edit" scene, and keep `render.use_sequencer=True` on that scene. Alternatively, burn captions afterwards with ffmpeg/ASS (see `face_animation_github.md`).

### 3.6 Grease Pencil v3 from Python (5.x)
Data model: `GreasePencil` → `layers` → `frames` → `frame.drawing` (`GreasePencilDrawing`). API in 5.2 **[src]**:
- `layers.new(name, set_active, layer_group)`, `layers.remove/move/move_top/move_bottom/move_to_layer_group`
- `layer_groups.new(name, parent_group)`
- `frames.new(frame_number)`, `frames.remove(n)`, `frames.copy(from, to, instance_drawing)`, `frames.move(from, to)`
- `layer.get_frame_at(n)`, `layer.current_frame()`
- `drawing.add_strokes(sizes)`, `remove_strokes`, `resize_strokes`, `reorder_strokes`, `set_types`, `tag_positions_changed()`, vertex-group helpers
- `layer.layer_masks.add/remove` (5.1+)

```python
gp = bpy.data.grease_pencils.new("Limbs")
ob = bpy.data.objects.new("Limbs", gp); sc.collection.objects.link(ob)
mat = bpy.data.materials.new("Ink"); bpy.data.materials.create_gpencil_data(mat)
gp.materials.append(mat)
layer = gp.layers.new("arms", set_active=True)
fr = layer.frames.new(1)
d = fr.drawing
d.add_strokes([3])                               # one 3-point stroke (shoulder-elbow-hand)
pos = d.attributes["position"].data
for i, p in enumerate([(0,0,0),(0.1,0,-0.3),(0.25,0,-0.5)]): pos[i].vector = p
d.attributes["radius"].data[0].value = 0.01      # attribute API is the fast path
d.tag_positions_changed()
```
Data access is through attributes (`position`, `radius`, `opacity`, `material_index`, `cyclic`), which is the recommended fast path. The high-level `drawing.strokes` API is slower ([4.3 migration guide](https://developer.blender.org/docs/release_notes/4.3/grease_pencil_migration/), [devtalk](https://devtalk.blender.org/t/blender-4-3-grease-pencil-v3-feedback/32115?page=3)). **Use case here:** procedurally drawn stick arms and legs (thick dark lines like the reference) that follow empties or hooks. A Hook or Armature modifier on the GP object lets you animate limbs by moving bones or empties instead of rewriting points. Points can also be rewritten per frame from Python for full control.

---

## 4. Headless rendering

```bash
blender -b scene.blend --python-exit-code 1 -P build_and_render.py -- --plan plan.json
blender -b scene.blend -o //frames/f_##### -F PNG -s 1 -e 1800 -a     # PNG sequence
blender -b --factory-startup -P make_scene.py -- args                  # no user prefs/add-ons
```
- `-b` background, `-P` script, `--python-exit-code N` makes CI fail on Python exceptions, `-a` renders the animation, `-o` sets the output pattern (`#` = frame digits), `-F` sets the format. **Arguments run in order**, so put `-o/-F` before `-a` ([manual: command line](https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html), [mankier](https://mankier.com/1/blender)). Everything after `--` is passed to the script (`sys.argv[sys.argv.index('--')+1:]`).
- With `--factory-startup`, FFmpeg output in 5.0.x raised a TypeError unless `media_type='VIDEO'` was set first ([#152175](https://projects.blender.org/blender/blender/issues/152175)). Rendering a PNG sequence and muxing with system ffmpeg is the most robust route anyway.
- **Engine choice for a GPU-less Linux server:** EEVEE is GPU-only, and the manual says no CPU fallback is planned ([EEVEE limitations, 5.2 manual](https://docs.blender.org/manual/en/latest/render/eevee/limitations/limitations.html)). Mesa EGL lets bpy *start* headless but does not prove that EEVEE renders ([polywright PR](https://github.com/m4bwav/polywright/pull/1)). Options:
  - **Cycles on CPU** with very low samples (8–16) plus the denoiser. For emission-only planes, 1–4 samples are enough with Filter Size about 1.0. Light paths can be cut to zero bounces.
  - **Workbench** with flat/texture colour also renders images on planes, but has no alpha blending finesse.
  - EEVEE on a GPU box (fastest).
- `blender --background --python-expr "import bpy; print(bpy.app.version_string)"` is a quick install check.

Pip-installable **`bpy`** module: the Blender-as-a-Python-module wheel is published to PyPI per release (`pip install bpy==5.2.*`, which needs the exact matching CPython, 3.13 for 5.x). This is handy for CI. Verify the wheel exists for your platform before relying on it (not verified here).

---

## 5. Add-ons and tools relevant to 2.5D, parallax and captions

| Tool | What | Notes |
|---|---|---|
| Built-in **Images as Planes** (`image.import_as_mesh_planes`) | Planes sized to image, material set up | Core since 4.2 ([4.2 manual](https://docs.blender.org/manual/en/4.2/modeling/meshes/import_images_as_planes.html), [brandon3d](https://brandon3d.com/how-to-import-images-as-planes-in-blender-3d/)) |
| **Frame By Plane** (free, Extensions) | Images, sequences, video and PSD to rigged planes; multiplane camera, parallax, cut-out animation | [extensions.blender.org/add-ons/frame-by-plane](https://extensions.blender.org/add-ons/frame-by-plane/) |
| **Parallax Layers / 2.5D Parallax** (Superhive, paid) | Folder of PSD layers → depth-spread, frame-filling planes plus push-in/truck/float camera presets | [superhivemarket.com/products/2-5d-parallax](https://superhivemarket.com/products/2-5d-parallax) |
| **nijiGPen** (GPL-3) | GP v3 helpers: boolean/offset, line cleanup, 2D→3D shading. Supports **4.3–5.2** | [github.com/chsh2/nijiGPen](https://github.com/chsh2/nijiGPen) |
| **Blender MCP** (MIT, ~32.5k★) | LLM-driven Blender over a socket server; runs Python in Blender | [github.com/ahujasid/mcp-for-blender](https://github.com/ahujasid/mcp-for-blender) |
| **DepthFlow** (AGPL-3, ~1.6k★) | Not a Blender add-on. Single image + depth map → parallax video in a GLSL shader. An alternative to manual layer splitting for "living background" moves | [github.com/BrokenSource/DepthFlow](https://github.com/BrokenSource/DepthFlow) |
| Auto-captions | No mature, maintained Blender add-on found. Recommended: WhisperX/stable-ts word timings → `strips.new_effect(type='TEXT')` (script in §3.5) | see `face_animation_github.md` |

---

## 6. Practical recommendations for this project
1. **Pin 5.2.x and write 5.x-native code**: `strips`, `compositing_node_group`, `media_type`, channelbag F-curves, `grease_pencils`. Old tutorials and LLM-written snippets (`sequences`, `scene.node_tree`, `action.fcurves`) will fail.
2. **Shot = one .blend scene generated from a JSON shot plan**: planes for bg/mid/character/face/overlay, a camera with eased keys and an optional Noise modifier, and a face-swap timeline. Render each shot to a PNG sequence with Cycles CPU at low samples, or EEVEE on a GPU. Assemble and caption in the VSE or with ffmpeg.
3. Keep colour management on **Standard** and shade planes with emission or shadeless, so GPT-image assets render with their original colours.
4. Use the **Compositor effect strip** (5.2) or compositor modifiers for glow, film grain or vignette, and for dissolves between shots. 1–4-frame cross-dissolves are what the reference videos mostly use; the transition analysis in `toolchain_hypotheses.md` found very few hard cuts.

---

## Sources
- Blender 5.2 release notes: https://developer.blender.org/docs/release_notes/5.2/
- 5.2 Sequencer: https://developer.blender.org/docs/release_notes/5.2/sequencer/
- 5.2 Compositor: https://developer.blender.org/docs/release_notes/5.2/compositor/
- 5.2 Grease Pencil: https://developer.blender.org/docs/release_notes/5.2/grease_pencil/
- Compatibility index: https://developer.blender.org/docs/release_notes/compatibility/
- 5.1 Python API: https://developer.blender.org/docs/release_notes/5.1/python_api/
- 5.1 Grease Pencil: https://developer.blender.org/docs/release_notes/5.1/grease_pencil/
- 5.0 Python API: https://developer.blender.org/docs/release_notes/5.0/python_api/
- 4.3 GP migration: https://developer.blender.org/docs/release_notes/4.3/grease_pencil_migration/
- 5.3 EEVEE (Vulkan default): https://developer.blender.org/docs/release_notes/5.3/eevee/
- blender.org 5.2 page: https://www.blender.org/download/releases/5-2/
- Phoronix 5.2: https://www.phoronix.com/news/Blender-5.2-Released
- CG Channel 5.2: https://www.cgchannel.com/2026/07/blender-5-2-lts-is-here-discover-its-5-key-features/
- CG Channel 5.1: https://www.cgchannel.com/2026/03/discover-5-key-features-in-blender-5-1/
- BlenderNation GP 5.2: https://www.blendernation.com/2026/07/06/blender-5-2-grease-pencil-16-new-features-breakdown/
- SteamDB 5.2.2: https://steamdb.info/patchnotes/25315940/
- MakeUseOf VSE: https://www.makeuseof.com/blenders-video-editor-became-something-actually-use/
- LinuxToday 5.3 beta: https://www.linuxtoday.com/blog/blender-5-3-enters-public-beta-testing-with-vulkan-backend-by-default-on-linux/
- 3dredbox (GN modifier API break): https://www.3dredboxstudio.com/blog/blender-5-2-geometry-nodes-modifier-api-what-broke
- interplanety (5.0 compositor tree): https://b3d.interplanety.org/en/changes-in-node-tree-creation-for-compositor-in-blender-5-0/
- Blender bug #152175 (FFmpeg/media_type): https://projects.blender.org/blender/blender/issues/152175
- terminalskills render automation: https://terminalskills.io/skills/blender-render-automation
- TMHSDigital issue (sequences→strips): https://github.com/TMHSDigital/Blender-Developer-Tools/issues/502
- BlenderArtists GP v3 API: https://blenderartists.org/t/how-to-use-the-grease-pencil-api-to-draw-strokes/1613077
- BlenderArtists fcurves in 5.0: https://blenderartists.org/t/how-to-access-fcurves-in-blender-5-0/1623022
- devtalk GP v3 feedback: https://devtalk.blender.org/t/blender-4-3-grease-pencil-v3-feedback/32115?page=3
- Command-line arguments manual: https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html ; https://mankier.com/1/blender
- EEVEE limitations (5.2 manual): https://docs.blender.org/manual/en/latest/render/eevee/limitations/limitations.html
- polywright Mesa EGL PR: https://github.com/m4bwav/polywright/pull/1
- Images as Planes 4.2 manual: https://docs.blender.org/manual/en/4.2/modeling/meshes/import_images_as_planes.html ; https://brandon3d.com/how-to-import-images-as-planes-in-blender-3d/
- Frame By Plane: https://extensions.blender.org/add-ons/frame-by-plane/
- Superhive 2.5D Parallax: https://superhivemarket.com/products/2-5d-parallax
- nijiGPen: https://github.com/chsh2/nijiGPen
- Blender MCP: https://github.com/ahujasid/mcp-for-blender
- DepthFlow: https://github.com/BrokenSource/DepthFlow
- Blender source (official GitHub mirror, branch blender-v5.2-release): https://github.com/blender/blender/tree/blender-v5.2-release. Files read: `source/blender/blenkernel/BKE_blender_version.h`, `source/blender/makesrna/intern/rna_sequencer_api.cc`, `rna_sequencer.cc`, `rna_scene.cc`, `rna_grease_pencil_api.cc`, `rna_main_api.cc`, `scripts/startup/bl_operators/image_as_planes.py`
