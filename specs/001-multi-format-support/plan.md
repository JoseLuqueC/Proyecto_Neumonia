# Implementation Plan: Multi-Format Medical Image Support

**Branch**: `001-multi-format-support` | **Date**: 2026-08-26 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/001-multi-format-support/spec.md`

## Summary

This feature adds support for NIFTI (.nii, .nii.gz) and enhanced PNG formats to the existing pneumonia detection tool. The implementation will extend the current `read_img.py` module to handle additional medical image formats while maintaining backwards compatibility with existing DICOM and JPEG functionality.

## Technical Context

**Language/Version**: Python 3.13

**Primary Dependencies**: 
- `nibabel` (NIFTI reading)
- `Pillow` (PNG handling with alpha channels)
- `numpy` (array operations)
- `opencv-python` (image processing)

**Storage**: File-based (no database changes required)

**Testing**: pytest (existing test framework)

**Target Platform**: Desktop application (tkinter GUI)

**Project Type**: Desktop application with GUI

**Performance Goals**: 
- Single NIFTI file load: <3 seconds
- Batch load (50 images): <30 seconds
- PNG load: <1 second

**Constraints**: 
- Must maintain existing DICOM/JPEG functionality
- Memory usage must stay under 500MB for batch operations
- NIFTI files >500MB require progress indicator

**Scale/Scope**: 
- Single-user desktop application
- Up to 50 images per batch operation
- Support for NIfTI-1 format (most common in clinical settings)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Notes |
|-----------|--------|-------|
| I. Modular Architecture | ✅ PASS | New format support will be added as separate functions in `read_img.py` module |
| II. Medical Data Integrity | ✅ PASS | NIFTI processing will maintain diagnostic integrity; no patient data changes |
| III. Test-First Development | ✅ PASS | Tests will be written before implementation for each format |
| IV. Reproducibility | ✅ PASS | Fixed random seeds will be used; dependencies pinned in pyproject.toml |
| V. Simplicity & Maintainability | ✅ PASS | Implementation follows YAGNI; minimal new dependencies |

**Security & Privacy Requirements**:
- ✅ Patient data not affected by this feature
- ✅ File input validation will be implemented for new formats
- ✅ No external dependencies that could introduce vulnerabilities

**Development Workflow & Quality Gates**:
- ✅ All code will pass `make lint` (ruff check)
- ✅ All tests will pass via `make test`
- ✅ Docker build will be tested

## Project Structure

### Documentation (this feature)

```text
specs/001-multi-format-support/
├── spec.md              # Feature specification
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output (empty - desktop app)
└── checklists/
    └── requirements.md  # Quality checklist
```

### Source Code (repository root)

```text
src/
├── read_img.py          # Extend with NIFTI and enhanced PNG support
├── detector_neumonia.py # Update file dialog to support new formats
├── integrator.py        # No changes required
├── load_model.py        # No changes required
└── preprocess_img.py    # May need minor updates for normalization

test/
├── test_read_img.py     # Add tests for NIFTI and PNG formats
└── test_preprocess.py   # Add tests for new format preprocessing
```

**Structure Decision**: Single project structure maintained. New format support will be added as functions within the existing `read_img.py` module, following the modular architecture principle.

## Complexity Tracking

No constitution violations identified. Implementation follows existing patterns and maintains simplicity.

## Research Tasks (Phase 0)

1. **NIFTI Format Research**: Investigate nibabel library API for reading NIfTI-1 files
2. **PNG Alpha Channel Handling**: Research best practices for removing alpha channels while preserving diagnostic information
3. **4D NIFTI Processing**: Investigate methods for extracting middle time slice from 4D datasets
4. **Memory Management**: Research memory-efficient loading strategies for large NIFTI files
5. **Progress Indicators**: Investigate tkinter progress bar implementation for long-running operations

## Design Artifacts (Phase 1)

1. **data-model.md**: Define ImageFormat, ImageProcessor, and PredictionResult entities
2. **quickstart.md**: Validation scenarios for NIFTI and PNG loading
3. **contracts/**: Empty (desktop application, no external interfaces)
