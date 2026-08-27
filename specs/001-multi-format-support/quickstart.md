# Quickstart: Multi-Format Medical Image Support

**Date**: 2026-08-26
**Feature**: 001-multi-format-support

## Prerequisites

- Python 3.13 environment with UV
- All dependencies installed (`make install`)
- Test images available in various formats

## Validation Scenarios

### Scenario 1: Load Single NIFTI File

**Setup**: Ensure you have a .nii or .nii.gz file available

**Steps**:
1. Run `make run` to start the application
2. Click "Cargar Imagen" button
3. Select a NIFTI file (.nii or .nii.gz)
4. Verify image displays in the left pane
5. Click "Predecir" button
6. Verify prediction result appears

**Expected Outcome**: 
- Image loads within 3 seconds
- Prediction result displays with label and confidence
- No error messages appear

### Scenario 2: Load NIFTI File with 4D Data

**Setup**: Use a NIFTI file with 4D data (time series)

**Steps**:
1. Run `make run` to start the application
2. Click "Cargar Imagen" button
3. Select a 4D NIFTI file
4. Verify the middle time slice is displayed
5. Verify prediction works correctly

**Expected Outcome**:
- Only one slice is displayed (middle time slice)
- Image loads without errors
- Prediction completes successfully

### Scenario 3: Load PNG with Alpha Channel

**Setup**: Use a PNG file with alpha channel (RGBA)

**Steps**:
1. Run `make run` to start the application
2. Click "Cargar Imagen" button
3. Select a PNG file with alpha channel
4. Verify image displays without transparency
5. Verify white background appears where alpha was transparent

**Expected Outcome**:
- Image displays correctly
- No transparency visible
- Prediction works normally

### Scenario 4: Load 16-bit PNG

**Setup**: Use a 16-bit PNG image

**Steps**:
1. Run `make run` to start the application
2. Click "Cargar Imagen" button
3. Select a 16-bit PNG file
4. Verify image displays with correct intensity values
5. Verify no data loss in normalization

**Expected Outcome**:
- Image displays with proper contrast
- Intensity values normalized correctly
- Prediction works with normalized image

### Scenario 5: Batch Loading

**Setup**: Have 5+ images of the same format ready

**Steps**:
1. Run `make run` to start the application
2. Click "Cargar Imagen" button
3. Use Ctrl+Click to select multiple files
4. Verify all images load correctly
5. Verify batch completes within 30 seconds

**Expected Outcome**:
- All selected images load
- Progress indicator shows during loading
- No memory errors

### Scenario 6: Large NIFTI File Warning

**Setup**: Use a NIFTI file >500MB

**Steps**:
1. Run `make run` to start the application
2. Click "Cargar Imagen" button
3. Select a large NIFTI file
4. Verify warning message appears
5. Verify progress indicator shows during loading

**Expected Outcome**:
- Warning about file size appears
- Progress indicator visible
- File loads successfully (may take longer)

### Scenario 7: Unsupported Format Error

**Setup**: Use a file with unsupported extension (e.g., .bmp, .tiff)

**Steps**:
1. Run `make run` to start the application
2. Click "Cargar Imagen" button
3. Select an unsupported file format
4. Verify error message appears

**Expected Outcome**:
- Clear error message indicating format not supported
- Application remains functional
- No crash or hang

### Scenario 8: Corrupted File Handling

**Setup**: Use a corrupted image file

**Steps**:
1. Run `make run` to start the application
2. Click "Cargar Imagen" button
3. Select a corrupted file
4. Verify error message appears

**Expected Outcome**:
- Clear error message about corrupted file
- Application remains functional
- No crash or hang

## Regression Testing

### Existing DICOM Functionality

**Steps**:
1. Load a DICOM file (.dcm)
2. Verify image displays correctly
3. Verify prediction works
4. Verify PDF generation works
5. Verify CSV export works

**Expected Outcome**: All existing functionality works unchanged

### Existing JPEG Functionality

**Steps**:
1. Load a JPEG file (.jpg, .jpeg)
2. Verify image displays correctly
3. Verify prediction works
4. Verify all existing features work

**Expected Outcome**: All existing functionality works unchanged

## Performance Validation

### Single File Load Time

**Test**: Load 10 different NIFTI files
**Measure**: Time from file selection to image display
**Target**: <3 seconds average

### Batch Load Time

**Test**: Load 50 images in batch
**Measure**: Total time from file selection to all images loaded
**Target**: <30 seconds total

### Memory Usage

**Test**: Monitor memory during batch load of 50 images
**Measure**: Peak memory usage
**Target**: <500MB total

## Test Commands

```bash
# Run all tests
make test

# Run specific format tests
uv run pytest test/test_read_img.py -v

# Run performance tests
uv run pytest test/test_performance.py -v

# Run lint check
make lint
```

## Troubleshooting

### Common Issues

1. **NIFTI file won't load**: Check if file is corrupted or in unsupported NIfTI-2 format
2. **PNG displays incorrectly**: Verify file isn't CMYK (out of scope)
3. **Batch load fails**: Check available memory; reduce batch size
4. **Progress bar freezes**: Ensure threading is working correctly

### Debug Mode

Add debug logging by setting environment variable:
```bash
export DEBUG_NIFTI=1
make run
```
