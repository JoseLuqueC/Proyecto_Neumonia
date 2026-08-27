# Tasks: Multi-Format Medical Image Support

**Input**: Design documents from `/specs/001-multi-format-support/`

**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are included as requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Add nibabel dependency and update project configuration

- [ ] T001 Add nibabel dependency to pyproject.toml
- [ ] T002 Update uv.lock file with new dependency
- [ ] T003 [P] Create test fixtures directory with sample NIFTI and PNG files in test/fixtures/

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core image processing infrastructure for all formats

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T004 Implement format detection utility in src/read_img.py
- [ ] T005 [P] Implement file validation function in src/read_img.py
- [ ] T006 [P] Implement progress callback infrastructure in src/read_img.py
- [ ] T007 [P] Implement cancel flag mechanism in src/read_img.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Load NIFTI Files (Priority: P1) 🎯 MVP

**Goal**: Load and display NIFTI format medical images

**Independent Test**: Load .nii and .nii.gz files and verify correct display and prediction

### Tests for User Story 1

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T008 [P] [US1] Create test_read_nifti.py with test cases for NIFTI loading in test/test_read_nifti.py
- [ ] T009 [P] [US1] Create test fixtures with sample NIFTI files in test/fixtures/nifti/
- [ ] T010 [P] [US1] Write test for 3D NIFTI loading in test/test_read_nifti.py
- [ ] T011 [P] [US1] Write test for 4D NIFTI handling in test/test_read_nifti.py
- [ ] T012 [P] [US1] Write test for invalid NIFTI error handling in test/test_read_nifti.py

### Implementation for User Story 1

- [ ] T013 [P] [US1] Implement read_nifti_file() function in src/read_img.py
- [ ] T014 [P] [US1] Implement 4D to 3D slice extraction in src/read_img.py
- [ ] T015 [US1] Add NIFTI format to supported formats dictionary in src/read_img.py
- [ ] T016 [US1] Update file dialog in src/detector_neumonia.py to accept .nii and .nii.gz
- [ ] T017 [US1] Add error handling for corrupted NIFTI files in src/read_img.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Enhanced PNG Support (Priority: P2)

**Goal**: Support PNG files with alpha channels and various bit depths

**Independent Test**: Load PNG files with alpha channels and different bit depths

### Tests for User Story 2

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T018 [P] [US2] Create test_read_png.py with enhanced PNG test cases in test/test_read_png.py
- [ ] T019 [P] [US2] Create test fixtures with alpha channel PNGs in test/fixtures/png/
- [ ] T020 [P] [US2] Write test for RGBA PNG loading in test/test_read_png.py
- [ ] T021 [P] [US2] Write test for 16-bit PNG normalization in test/test_read_png.py
- [ ] T022 [P] [US2] Write test for 32-bit PNG handling in test/test_read_png.py

### Implementation for User Story 2

- [ ] T023 [P] [US2] Implement alpha channel removal function in src/read_img.py
- [ ] T024 [P] [US2] Implement bit depth normalization function in src/read_img.py
- [ ] T025 [US2] Update read_jpg_file() to handle enhanced PNG formats in src/read_img.py
- [ ] T026 [US2] Add PNG format detection to format dictionary in src/read_img.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Format Detection and Validation (Priority: P3)

**Goal**: Automatic format detection and clear error messages

**Independent Test**: Test with various file formats and verify appropriate messages

### Tests for User Story 3

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T027 [P] [US3] Create test_format_detection.py in test/test_format_detection.py
- [ ] T028 [P] [US3] Write test for format detection accuracy in test/test_format_detection.py
- [ ] T029 [P] [US3] Write test for unsupported format messages in test/test_format_detection.py
- [ ] T030 [P] [US3] Write test for corrupted file detection in test/test_format_detection.py

### Implementation for User Story 3

- [ ] T031 [P] [US3] Implement format detection from extension in src/read_img.py
- [ ] T032 [P] [US3] Implement file integrity validation in src/read_img.py
- [ ] T033 [US3] Update error messages for unsupported formats in src/read_img.py
- [ ] T034 [US3] Add user-friendly error dialogs in src/detector_neumonia.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: User Story 4 - Batch Loading (Priority: P4)

**Goal**: Load multiple images via multi-select file picker

**Independent Test**: Select multiple files and verify all load correctly

### Tests for User Story 4

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T035 [P] [US4] Create test_batch_loading.py in test/test_batch_loading.py
- [ ] T036 [P] [US4] Write test for multi-select file dialog in test/test_batch_loading.py
- [ ] T037 [P] [US4] Write test for batch load performance in test/test_batch_loading.py
- [ ] T038 [P] [US4] Write test for batch error handling in test/test_batch_loading.py

### Implementation for User Story 4

- [ ] T039 [P] [US4] Implement batch loading function in src/read_img.py
- [ ] T040 [P] [US4] Add threading support for batch operations in src/read_img.py
- [ ] T041 [US4] Update file dialog for multi-select in src/detector_neumonia.py
- [ ] T042 [US4] Add progress indicator for batch loading in src/detector_neumonia.py
- [ ] T043 [US4] Implement batch result storage in src/detector_neumonia.py

**Checkpoint**: All user stories including batch loading should work

---

## Phase 7: User Story 5 - Large File Handling (Priority: P5)

**Goal**: Handle large NIFTI files with warnings and progress indicators

**Independent Test**: Test with files >500MB and verify warning and progress

### Tests for User Story 5

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T044 [P] [US5] Create test_large_files.py in test/test_large_files.py
- [ ] T045 [P] [US5] Write test for file size warning in test/test_large_files.py
- [ ] T046 [P] [US5] Write test for progress indicator in test/test_large_files.py

### Implementation for User Story 5

- [ ] T047 [P] [US5] Implement file size check function in src/read_img.py
- [ ] T048 [P] [US5] Add progress bar widget in src/detector_neumonia.py
- [ ] T049 [US5] Integrate progress indicator with NIFTI loading in src/read_img.py
- [ ] T050 [US5] Add warning dialog for large files in src/detector_neumonia.py

**Checkpoint**: Large file handling complete

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T051 [P] Run quickstart.md validation scenarios
- [ ] T052 [P] Performance optimization for memory usage
- [ ] T053 Code cleanup and refactoring
- [ ] T054 [P] Update documentation in README.md
- [ ] T055 Security audit of file input handling
- [ ] T056 Run full test suite and fix any failures

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3 → P4 → P5)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable

### Within Each User Story

- Tests MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
Task: "Create test_read_nifti.py with test cases for NIFTI loading in test/test_read_nifti.py"
Task: "Create test fixtures with sample NIFTI files in test/fixtures/nifti/"
Task: "Write test for 3D NIFTI loading in test/test_read_nifti.py"
Task: "Write test for 4D NIFTI handling in test/test_read_nifti.py"
Task: "Write test for invalid NIFTI error handling in test/test_read_nifti.py"

# Launch all models for User Story 1 together:
Task: "Implement read_nifti_file() function in src/read_img.py"
Task: "Implement 4D to 3D slice extraction in src/read_img.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1 (NIFTI loading)
   - Developer B: User Story 2 (Enhanced PNG)
   - Developer C: User Story 3 (Format detection)
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
