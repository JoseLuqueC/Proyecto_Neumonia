# Research: Multi-Format Medical Image Support

**Date**: 2026-08-26
**Feature**: 001-multi-format-support

## Research Tasks

### 1. NIFTI Format Research

**Decision**: Use `nibabel` library for NIfTI-1 file reading

**Rationale**: 
- nibabel is the de facto standard for neuroimaging in Python
- Supports both .nii and .nii.gz formats
- Well-documented API with extensive community support
- Maintained by the neuroimaging community (nipype)

**Alternatives Considered**:
- `nipy`: More comprehensive but heavier dependency
- `SimpleITK`: Overkill for NIFTI-only reading
- Custom implementation: Too complex, reinventing the wheel

**Key API Findings**:
```python
import nibabel as nib
img = nib.load('file.nii.gz')
data = img.get_fdata()  # Returns numpy array
```

### 2. PNG Alpha Channel Handling

**Decision**: Remove alpha channel by compositing against white background

**Rationale**:
- Medical images don't use transparency diagnostically
- White background is standard for medical imaging display
- Preserves RGB values while removing alpha

**Implementation Approach**:
```python
from PIL import Image
img = Image.open('file.png')
if img.mode == 'RGBA':
    # Create white background
    background = Image.new('RGB', img.size, (255, 255, 255))
    background.paste(img, mask=img.split()[3])  # Paste using alpha channel
    img = background
```

### 3. 4D NIFTI Processing

**Decision**: Extract middle time slice automatically

**Rationale**:
- Middle slice provides representative view of the dataset
- Simple implementation with predictable behavior
- Avoids complexity of user selection for initial implementation

**Implementation Approach**:
```python
data = img.get_fdata()
if data.ndim == 4:
    # Extract middle time slice
    mid_idx = data.shape[3] // 2
    data = data[:, :, :, mid_idx]
```

### 4. Memory Management for Large Files

**Decision**: Implement chunked loading with progress indicator

**Rationale**:
- Large NIFTI files (500MB+) can cause memory issues
- Progress indicator provides user feedback
- Allows cancellation of long-running operations

**Implementation Approach**:
- Use memory mapping for initial file access
- Load data in chunks if file > 200MB
- Show progress bar in tkinter GUI
- Allow user to cancel operation

### 5. Progress Indicators in tkinter

**Decision**: Use `ttk.Progressbar` with threading

**Rationale**:
- Native tkinter widget, no additional dependencies
- Threading prevents GUI freezing during loading
- Standard UI pattern for progress indication

**Implementation Approach**:
```python
import threading
from tkinter import ttk

def load_with_progress(filepath, progress_var):
    def load():
        # Load file
        img_data = load_image(filepath)
        progress_var.set(100)
    
    thread = threading.Thread(target=load)
    thread.start()
```

### 6. Bit Depth Normalization

**Decision**: Normalize to 8-bit using min-max scaling

**Rationale**:
- Preserves relative intensity relationships
- Compatible with existing model input requirements
- Simple implementation with predictable results

**Implementation Approach**:
```python
import numpy as np

def normalize_to_8bit(img_array):
    img_min = img_array.min()
    img_max = img_array.max()
    if img_max - img_min > 0:
        normalized = ((img_array - img_min) / (img_max - img_min) * 255).astype(np.uint8)
    else:
        normalized = np.zeros_like(img_array, dtype=np.uint8)
    return normalized
```

## Dependencies to Add

```toml
[project.dependencies]
nibabel = ">=5.2.0"
```

## Risk Assessment

| Risk | Impact | Mitigation |
|------|--------|------------|
| nibabel dependency conflicts | Medium | Test with existing dependencies; use virtual environment |
| Memory issues with large files | High | Implement chunked loading; add memory monitoring |
| 4D NIFTI complexity | Medium | Start with middle slice extraction; defer 4D viewing to future |
| Thread safety in tkinter | Low | Use proper thread synchronization; queue-based communication |
