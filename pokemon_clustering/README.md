# Pokemon Projects Hub

This repository collects Pokémon-related analyses as independent projects. Use this contents page to find project folders, data, and contribution pointers.

## Contents

- `pokemon_clustering/` — Pokemon clustering analysis (SeCo framework). See `pokemon_clustering/README.md` for details.
- `pokemon_optimization/` — Placeholder for future optimization work (currently empty).
- `data/` — Shared raw datasets used across projects (e.g. `pokemon_stats.csv`).

## Quick pointers

- To run the clustering analysis: open `pokemon_clustering/notebooks/pokemon_clustering.ipynb` with Jupyter or VS Code. See `pokemon_clustering/README.md` for project-specific instructions.
- Shared raw data should remain in `data/` at the repository root. Project-specific derived outputs belong in `PROJECT/outputs/` and may be added to `.gitignore`.

## Contributing / Adding a new project

1. Create a folder under the repository root named for your project (e.g. `my_project/` or `another_project/`).
2. Add a `README.md` describing entry points and data expectations.
3. Keep shared data in `data/` and project outputs under `PROJECT/outputs/`.

If you want, I can add a `requirements.txt` and `.gitignore` entries for outputs — say the word and I will do it.

