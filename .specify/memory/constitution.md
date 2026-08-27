<!-- Sync Impact Report
Version change: 0.0.0 → 1.0.0
Added principles:
  - I. Modular Architecture
  - II. Medical Data Integrity
  - III. Test-First Development
  - IV. Reproducibility
  - V. Simplicity & Maintainability
Added sections:
  - Security & Privacy Requirements
  - Development Workflow & Quality Gates
Removed sections: None
Modified sections: None
Deferred items: None
-->

# Proyecto Neumonía - UAO Constitution

## Core Principles

### I. Modular Architecture
Every feature MUST be implemented as a self-contained module within `src/`. Each module MUST have a single responsibility, clear interface, and be independently testable. Module boundaries MUST be enforced through explicit imports. No circular dependencies allowed between modules.

### II. Medical Data Integrity
All medical image processing (DICOM, JPEG) MUST maintain diagnostic integrity. Image preprocessing pipelines MUST be deterministic and version-controlled. Patient data (cédula, history) MUST be handled with strict confidentiality. No patient-identifiable information MUST be logged or committed to version control.

### III. Test-First Development (NON-NEGOTIABLE)
TDD cycle is mandatory: Tests written → User approved → Tests fail → Then implement. Target: minimum 120 unit tests. Red-Green-Refactor cycle strictly enforced. All new features MUST include corresponding test coverage before merge.

### IV. Reproducibility
All model predictions MUST be reproducible with fixed random seeds. Dependencies MUST be pinned in `pyproject.toml` via UV lockfile. Docker builds MUST produce identical environments across machines. Model artifacts (`.h5` files) MUST be versioned alongside code.

### V. Simplicity & Maintainability
Follow YAGNI principles - implement only what is required. Code MUST be readable without extensive comments. Prefer standard library over external dependencies when functionality is equivalent. Technical debt MUST be documented with TODO markers and tracked for resolution.

## Security & Privacy Requirements

- Patient data MUST NOT be committed to git repositories
- CSV exports MUST contain de-identified data only
- Docker containers MUST run with least-privilege principles
- All external dependencies MUST be audited for known vulnerabilities
- Application MUST validate file inputs to prevent path traversal attacks

## Development Workflow & Quality Gates

- All code changes MUST pass `make lint` (ruff check) before commit
- All tests MUST pass via `make test` before merge
- Docker build MUST succeed before release
- PRs MUST include test coverage for new functionality
- Code review required for all changes to `src/` modules

## Governance

This constitution supersedes all other development practices for the Proyecto Neumonía. Amendments require:
1. Written proposal with rationale
2. Impact analysis on existing codebase
3. Version bump following semantic versioning (MAJOR.MINOR.PATCH)
4. Documentation of migration plan if breaking changes

All PRs and code reviews MUST verify compliance with these principles. Complexity must be justified with concrete use cases. Refer to `README.md` for runtime development guidance.

**Version**: 1.0.0 | **Ratified**: 2026-08-26 | **Last Amended**: 2026-08-26
