# Data Model: Multi-Format Medical Image Support

**Date**: 2026-08-26
**Feature**: 001-multi-format-support

## Entities

### ImageFormat

Represents supported image formats and their characteristics.

**Attributes**:
- `name` (str): Human-readable format name (e.g., "NIFTI", "PNG")
- `extensions` (list[str]): Supported file extensions (e.g., [".nii", ".nii.gz"])
- `mime_types` (list[str]): MIME types (e.g., ["application/nifti", "image/png"])
- `max_file_size_mb` (int): Maximum recommended file size in MB
- `requires_preprocessing` (bool): Whether format needs special preprocessing

**Validation Rules**:
- Name must be unique across all formats
- Extensions must start with a dot
- Max file size must be positive

**State Transitions**:
- None (immutable configuration object)

### ImageProcessor

Handles format-specific loading and preprocessing logic.

**Attributes**:
- `supported_formats` (dict[str, Callable]): Mapping of format names to loader functions
- `progress_callback` (Optional[Callable]): Callback for progress updates
- `cancel_flag` (bool): Flag to cancel ongoing operations

**Methods**:
- `load_image(filepath: str) -> tuple[np.ndarray, Image]`: Load image from file
- `validate_format(filepath: str) -> bool`: Check if format is supported
- `get_format_info(filepath: str) -> ImageFormat`: Get format metadata

**Validation Rules**:
- Must support all formats in ImageFormat registry
- Progress callback must accept integer (0-100)
- Cancel flag must be thread-safe

**State Transitions**:
- `idle` → `loading` → `loaded` or `error`
- `loading` → `cancelled` (if cancel_flag set)

### PredictionResult

Contains prediction output with confidence scores.

**Attributes**:
- `label` (str): Prediction label (e.g., "Normal", "Neumonía")
- `confidence` (float): Confidence score (0.0 to 1.0)
- `processing_time_ms` (int): Time taken for prediction in milliseconds
- `input_format` (str): Format of input image
- `input_shape` (tuple[int, int, int]): Shape of processed image (H, W, C)

**Validation Rules**:
- Confidence must be between 0.0 and 1.0
- Processing time must be non-negative
- Input shape must be 3D (height, width, channels)

**State Transitions**:
- None (immutable result object)

## Relationships

```
ImageProcessor ──uses──► ImageFormat (many-to-many)
ImageProcessor ──produces──► PredictionResult (one-to-many)
ImageProcessor ──loads──► Image (many-to-many)
```

## Data Flow

```
1. User selects file(s) via file dialog
2. ImageProcessor.validate_format() checks extension
3. ImageProcessor.load_image() reads file based on format
4. ImageProcessor applies format-specific preprocessing
5. Preprocessed image passed to existing prediction pipeline
6. PredictionResult returned with metadata
```

## Storage Considerations

- No persistent storage changes required
- Images are processed in-memory
- Temporary files (if any) stored in system temp directory
- No database schema changes needed

## Thread Safety

- ImageProcessor.cancel_flag must be thread-safe (use threading.Event)
- Progress callback must be thread-safe (use queue or tkinter's after() method)
- Image loading should run in separate thread to prevent GUI freezing
