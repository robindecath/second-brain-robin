# Third-Party Notices

This project integrates several third-party components. This file records the attribution
required by their licenses.

---

## BMAD-METHOD (BMad Code, LLC)

This repository holds Decathlon's **team-level customization bundle**: TOML overrides,
Decathlon-specific personas and knowledge routing, layered on top of the agents and
workflows provided by BMAD-METHOD. BMAD is the agent and workflow engine we customize —
one of the building blocks of the wider AI Augmented SDLC platform, not the whole of it.

| | |
|---|---|
| Project | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) |
| License | MIT — see the [upstream LICENSE](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/LICENSE) |
| Copyright | Copyright (c) 2025 BMad Code, LLC |
| Trademarks | see the [upstream TRADEMARK.md](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/TRADEMARK.md) |

### How this project uses BMAD-METHOD

BMAD-METHOD is **not vendored or redistributed** here. This repository contains only
Decathlon-authored customization files, consumed by BMAD's documented customization and
custom-module mechanisms:

- `bmad-*.toml` at the repository root — team overrides merged on top of the upstream
  `customize.toml` of the corresponding BMAD agent or workflow, following the
  [Customize BMad](https://docs.bmad-method.org/how-to/customize-bmad/) contract
- `modules/**` — Decathlon custom modules (e.g. `sre-platform`) installed through
  `npx bmad-method install --custom-source`, following the
  [Install Custom Modules](https://docs.bmad-method.org/how-to/install-custom-modules/) contract

The file names, the TOML keys, the `module.yaml` / `module-help.csv` layout and the
`bmad-*` command namespace are dictated by those upstream contracts — they are interface
requirements, not copied content. Where a skill name or short description matches BMAD's
own `module-help.csv`, it is used under the terms of the upstream MIT License linked above.

### Trademarks

BMad™, BMad Method™, BMad Core™ and BMad Code™ are trademarks of BMad Code, LLC, covering
all casings and variations. They are **not** covered by the MIT License, which applies to
the code only and not to the BMad brand.

**Decathlon is not affiliated with, endorsed by, sponsored by, or certified by BMad Code,
LLC.** This repository is not an official BMad product, module or distribution. Its name
and the `bmad-*` file and command prefixes are descriptive: they identify which upstream
agents and workflows each file customizes, as permitted by the upstream trademark
guidelines for community modules.
