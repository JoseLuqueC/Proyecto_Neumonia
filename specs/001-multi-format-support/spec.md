# Feature Specification: Multi-Format Medical Image Support

**Feature Branch**: `001-multi-format-support`

**Created**: 2026-08-26

**Status**: Draft

**Input**: User description: "Add support for NIFTI, PNG, and other medical image formats"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Load NIFTI Files (Priority: P1)

As a medical professional, I want to load NIFTI format brain scan images so that I can analyze neurological conditions alongside chest X-rays.

**Why this priority**: NIFTI is a standard format in neuroimaging and expands the tool's diagnostic capabilities significantly.

**Independent Test**: Can be fully tested by loading a .nii or .nii.gz file and verifying the image displays correctly in the viewer.

**Acceptance Scenarios**:

1. **Given** the application is open, **When** the user selects a .nii or .nii.gz file, **Then** the image is loaded and displayed in the viewer pane.
2. **Given** a NIFTI file is loaded, **When** the user clicks "Predecir", **Then** the system processes the image and returns a prediction.
3. **Given** an invalid NIFTI file, **When** the user attempts to load it, **Then** an appropriate error message is displayed.

---

### User Story 2 - Enhanced PNG Support (Priority: P2)

As a user, I want to load PNG images with alpha channels and various bit depths so that I can use a wider range of medical imaging sources.

**Why this priority**: PNG is the most common web image format and supporting variations improves accessibility.

**Independent Test**: Can be tested by loading PNG files with different bit depths (8-bit, 16-bit, 32-bit) and verifying correct display.

**Acceptance Scenarios**:

1. **Given** the application is open, **When** the user selects a PNG file with alpha channel, **Then** the alpha channel is removed and the image displays correctly.
2. **Given** a 16-bit PNG is loaded, **When** the image is displayed, **Then** the intensity values are normalized to 8-bit for display while preserving diagnostic information.

---

### User Story 3 - Format Detection and Validation (Priority: P3)

As a user, I want the system to automatically detect the image format and validate it before processing so that I receive clear feedback about unsupported formats.

**Why this priority**: Improves user experience by providing immediate feedback rather than cryptic errors.

**Independent Test**: Can be tested by attempting to load files with various extensions and verifying appropriate messages appear.

**Acceptance Scenarios**:

1. **Given** the application is open, **When** the user selects a file with an unsupported extension, **Then** a message indicates the format is not supported.
2. **Given** a corrupted image file, **When** the user attempts to load it, **Then** a clear error message explains the file appears to be corrupted.

---

### Edge Cases

- What happens when a NIFTI file contains 4D data (time series)? → System extracts and displays the middle time slice automatically
- How does the system handle extremely large NIFTI files (>500MB)? → System shows a warning and allows processing with a progress indicator
- What happens when a PNG file has an ICC color profile?
- How does the system handle NIFTI files with unusual voxel dimensions?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST read and display NIFTI format files (.nii, .nii.gz)
- **FR-002**: System MUST read and display PNG files with alpha channels
- **FR-003**: System MUST read and display 16-bit and 32-bit PNG images
- **FR-004**: System MUST automatically detect image format from file extension
- **FR-005**: System MUST validate file integrity before processing
- **FR-006**: System MUST display appropriate error messages for unsupported formats
- **FR-007**: System MUST normalize multi-bit-depth images to 8-bit for display
- **FR-008**: System MUST preserve original pixel data for model predictions
- **FR-009**: System MUST support batch loading of up to 50 images in the same format via multi-select file picker
- **FR-010**: System MUST maintain backwards compatibility with existing DICOM and JPEG functionality
- **FR-011**: System MUST extract and display the middle time slice from 4D NIFTI files
- **FR-012**: System MUST display a warning for NIFTI files larger than 500MB and show a progress indicator during processing

### Key Entities

- **ImageFormat**: Represents supported image formats with their extensions and MIME types
- **ImageProcessor**: Handles format-specific loading and normalization logic
- **PredictionResult**: Contains prediction output with confidence scores

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can load single NIFTI files in under 3 seconds and batches of 50 images in under 30 seconds
- **SC-002**: System successfully processes 95% of standard NIFTI files without errors
- **SC-003**: PNG files with alpha channels load correctly 100% of the time
- **SC-004**: Error messages are clear and actionable for 90% of failure cases
- **SC-005**: Existing DICOM and JPEG functionality continues to work without regression

## Clarifications

### Session 2026-08-26

- Q: How should batch loading of multiple images work in the user interface? → A: File picker dialog with multi-select (Ctrl+Click)
- Q: How should the system handle NIFTI files containing 4D data (time series)? → A: Extract and display the middle time slice automatically
- Q: What is the maximum number of images that should be supported in a single batch loading operation? → A: Up to 50 images
- Q: What should be the maximum time allowed for loading a batch of 50 images? → A: Under 30 seconds
- Q: How should the system handle NIFTI files larger than 500MB? → A: Show a warning and allow processing with progress indicator

## Assumptions

- NIFTI files will be single-volume (3D) rather than 4D time series for initial implementation
- Users will primarily work with NIfTI-1 format (most common in clinical settings)
- PNG images will be RGB or grayscale; CMYK medical images are out of scope
- File sizes will typically be under 200MB; extreme cases may require pagination
- The existing TensorFlow model can accept normalized 8-bit input from any format
