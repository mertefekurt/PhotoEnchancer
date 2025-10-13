# ✨ Photo Enhancer

A modern, open-source photo processing application with a beautiful UI that automatically enhances images in bulk by adjusting brightness, contrast, and saturation.

## 🎨 Features

- **Batch Processing**: Process multiple images at once with ease
- **Adjustable Enhancement Settings**:
  - ☀️ Brightness (0.5 - 2.0)
  - 🎨 Contrast (0.5 - 2.0)
  - 🌈 Saturation (0.5 - 2.0)
- **Auto-Save Settings**: Your preferences are automatically saved
- **Modern UI**: Clean, dark-themed interface with intuitive controls
- **Real-time Preview**: Visual feedback with emoji indicators
- **Progress Tracking**: Monitor your processing status
- **Cancel Anytime**: Stop processing whenever you need

## Screenshots

### Before and After Comparison

<div align="center">
  <table>
    <tr>
      <td align="center"><strong>Before</strong></td>
      <td align="center"><strong>After</strong></td>
    </tr>
    <tr>
      <td><img src="screenshots/Before.jpg" width="300" alt="Before enhancement"></td>
      <td><img src="screenshots/After.jpg" width="300" alt="After enhancement"></td>
    </tr>
  </table>
</div>

### Main Application Window

<div align="center">
  <img src="screenshots/Interface.png" alt="Main application window" width="600"/>
</div>

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/PhotoEnchancer.git
   cd PhotoEnchancer
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python src/image_processor_gui.py
   ```

## 📖 Usage

1. **Select Input Folder**: Click "Browse..." next to Input to select the folder containing your images
2. **Select Output Folder**: Choose where you want the enhanced images to be saved
3. **Adjust Settings**: Use the sliders to fine-tune brightness, contrast, and saturation
4. **Start Processing**: Click the "▶ Start Processing" button
5. **Monitor Progress**: Watch the progress bar and status updates
6. **Find Your Images**: Enhanced images will be saved with "enhanced_" prefix in the output folder

## 🛠️ Technologies Used

- **Python 3.x**
- **Tkinter**: For the graphical user interface
- **Pillow (PIL)**: Image processing library
- **OpenCV**: Additional image processing capabilities

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📄 License

This project is open source and available under the MIT License.

## 💡 Tips

- Supported image formats: JPG, JPEG, PNG
- Settings are automatically saved between sessions
- Use the "Reset to Defaults" button to restore original values
- You can cancel processing at any time without losing completed images
- Enhanced images are saved with "enhanced_" prefix
