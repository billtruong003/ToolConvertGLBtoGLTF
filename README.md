# GLB to GLTF Converter

This script allows you to batch-convert `.glb` files to `.gltf` files with a simple user interface built using `tkinter`.

## Requirements

- Python 3.x
- Python libraries:
  - `pygltflib` for handling `.glb` and `.gltf` files
  - `tkinter` (comes pre-installed with most Python distributions)

## Library Installation

Before using the script, install the `pygltflib` library:

```bash
pip install pygltflib
```

## Usage Instructions

1. **Run the Script**: Run the Python script in your terminal or development environment (IDE):

   ```bash
   python glb_to_gltf_converter.py
   ```

2. **User Interface**: The main interface will appear with fields to select the folder containing `.glb` files and the output folder for `.gltf` files.

3. **Select Input Folder**:
   - Click the **Select** button next to the "Folder containing .glb files" field.
   - Choose the folder with the `.glb` files you want to convert.

4. **Select Output Folder**:
   - Click the **Select** button next to the "Output folder for .gltf files" field.
   - Choose or create a folder to store the converted `.gltf` files.

5. **Start Conversion**:
   - Click the **Convert** button to begin the conversion process.
   - Each `.glb` file will be converted to `.gltf` and saved in a subfolder within the output directory, with the subfolder named after the original `.glb` file (excluding the extension).

6. **Completion**:
   - A confirmation message will appear once all files have been converted.
   - Check the output directory to see subfolders containing the `.gltf` files.

## Additional Information

- **Automatic Subfolder Creation**: The script automatically creates a subfolder in the output directory for each `.glb` file, named after the `.glb` file itself (without the extension).
- **Error Handling**: If either the input or output folder is not selected, the script will prompt you to select the missing folder(s).

## Example

Suppose you have `.glb` files in an `input` folder and want to save the converted `.gltf` files in an `output/gltf` folder. The interface guides you through selecting the folders and quickly performs the conversion.

--- 

Let me know if you need any further customization!