# Asset Library — index

Built from the 30 fps decode of pilot videos 1–5. Every crop has a matching prompt in the folder's `.md` file.
Attach the crop as the reference image when generating with the image model.

## Characters

| Character | Video | Emotion crops | Pose crops | Reference crops | Folder |
|---|---|---|---|---|---|
| Amy | 04 | 3 | 2 | 1 | [`Amy/`](characters/Amy/) |
| Beanie | 05 | 0 | 0 | 1 | [`Beanie/`](characters/Beanie/) |
| Biscuit | 04 | 0 | 0 | 1 | [`Biscuit/`](characters/Biscuit/) |
| Bling | 05 | 4 | 3 | 2 | [`Bling/`](characters/Bling/) |
| Carl | 04 | 0 | 0 | 1 | [`Carl/`](characters/Carl/) |
| Cooper | 04 | 0 | 0 | 1 | [`Cooper/`](characters/Cooper/) |
| Deb | 04 | 1 | 0 | 1 | [`Deb/`](characters/Deb/) |
| Dex | 04 | 11 | 7 | 3 | [`Dex/`](characters/Dex/) |
| Dr Klaus | 04 | 3 | 4 | 2 | [`Dr_Klaus/`](characters/Dr_Klaus/) |
| Edison | 02 | 4 | 1 | 2 | [`Edison/`](characters/Edison/) |
| Elmer | 04 | 4 | 2 | 1 | [`Elmer/`](characters/Elmer/) |
| Gil | 04 | 4 | 1 | 1 | [`Gil/`](characters/Gil/) |
| Gus | 04 | 0 | 0 | 1 | [`Gus/`](characters/Gus/) |
| Hank | 04 | 0 | 0 | 1 | [`Hank/`](characters/Hank/) |
| Kai | 01 | 36 | 24 | 4 | [`Kai/`](characters/Kai/) |
| Lenny | 05 | 11 | 10 | 4 | [`Lenny/`](characters/Lenny/) |
| Marge | 03 | 5 | 9 | 3 | [`Marge/`](characters/Marge/) |
| Mo | 04 | 0 | 0 | 1 | [`Mo/`](characters/Mo/) |
| Nina | 03 | 2 | 2 | 1 | [`Nina/`](characters/Nina/) |
| Noggin | 04 | 5 | 3 | 1 | [`Noggin/`](characters/Noggin/) |
| Officer Dale | 03 | 2 | 5 | 2 | [`Officer_Dale/`](characters/Officer_Dale/) |
| Ray | 04 | 0 | 0 | 1 | [`Ray/`](characters/Ray/) |
| Rico | 03 | 21 | 12 | 3 | [`Rico/`](characters/Rico/) |
| Tad | 04 | 3 | 2 | 1 | [`Tad/`](characters/Tad/) |
| Theo | 02 | 21 | 10 | 4 | [`Theo/`](characters/Theo/) |

Each character folder: `character.md` (design spec + master prompt), `reference/`, `poses/` + `poses.md`, `emotions/` + `emotions.md` (expression timeline + per-emotion prompts).
Extras with only a reference crop are background/one-scene characters.

## Scene assets (per video)

| Video | Backgrounds | 3D-look assets | Unique images | Overlays / UI / VFX |
|---|---|---|---|---|
| 01_this_tree_hates_you | [16](backgrounds/01_this_tree_hates_you/index.md) | [10](assets_3d/01_this_tree_hates_you/index.md) | [4](unique_images/01_this_tree_hates_you/index.md) | [30](overlays_ui/01_this_tree_hates_you/index.md) |
| 02_your_brains_secret_idea_zone | [9](backgrounds/02_your_brains_secret_idea_zone/index.md) | [11](assets_3d/02_your_brains_secret_idea_zone/index.md) | [8](unique_images/02_your_brains_secret_idea_zone/index.md) | [17](overlays_ui/02_your_brains_secret_idea_zone/index.md) |
| 03_why_humans_cant_pick_random_numbers | [13](backgrounds/03_why_humans_cant_pick_random_numbers/index.md) | [18](assets_3d/03_why_humans_cant_pick_random_numbers/index.md) | [9](unique_images/03_why_humans_cant_pick_random_numbers/index.md) | [14](overlays_ui/03_why_humans_cant_pick_random_numbers/index.md) |
| 04_the_scientists_insane_time_test | [16](backgrounds/04_the_scientists_insane_time_test/index.md) | [11](assets_3d/04_the_scientists_insane_time_test/index.md) | [10](unique_images/04_the_scientists_insane_time_test/index.md) | [16](overlays_ui/04_the_scientists_insane_time_test/index.md) |
| 05_the_science_behind_slot_machines | [7](backgrounds/05_the_science_behind_slot_machines/index.md) | [13](assets_3d/05_the_science_behind_slot_machines/index.md) | [4](unique_images/05_the_science_behind_slot_machines/index.md) | [8](overlays_ui/05_the_science_behind_slot_machines/index.md) |
| **Total** | **61** | **63** | **35** | **85** |

Shared rules: style → `system/STYLE_GUIDE.md`, colours → `system/COLOR_SYSTEM.md`, prompt method → `system/research/chatgpt_image_prompting_2026.md`.
