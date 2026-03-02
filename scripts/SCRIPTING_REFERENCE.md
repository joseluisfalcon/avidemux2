# Avidemux2 tinyPy Scripting Reference

Avidemux2 uses the `tinyPy` engine for scripting. Scripts can be run from the GUI (File -> Tinypy Project -> Run Script) or via CLI using `--run script.py`.

## Core Objects

### Avidemux()
The main object for project-level operations.

| Method | Parameters | Description |
| :--- | :--- | :--- |
| `loadVideo(path)` | `str` | Loads a video file. |
| `appendVideo(path)` | `str` | Appends a video file to the current project. |
| `clearSegments()` | None | Clears all segments. |
| `addSegment(ref, start, duration)` | `int, float, float` | Adds a segment. |
| `setContainer(name, *couples)` | `str, ...` | Sets output container (e.g. "MKV", "MP4"). |
| `videoCodec(name, *couples)` | `str, ...` | Sets video encoder and parameters. |
| `audioCodec(track, name, *couples)` | `int, str, ...` | Sets audio encoder for a specific track. |
| `save(path)` | `str` | Saves the project to a file. |
| `closeVideo()` | None | Closes the current video. |
| `audioAddTrack(poolIdx)` | `int` | Adds an audio track from the pool. |
| `audioAddExternal(path)` | `str` | Adds an external audio track. |
| `audioClearTracks()` | None | Removes all audio tracks. |
| `markerA` | `float` | Attribute: Get/Set Marker A position in microseconds. |
| `markerB` | `float` | Attribute: Get/Set Marker B position in microseconds. |

### Navigation & Seeking
These methods are also part of the `Avidemux()` object (mapped from the internal editor).

| Method | Parameters | Description |
| :--- | :--- | :--- |
| `seekFrame(n)` | `int` | Seeks forward/backward by `n` frames. |
| `seekKeyFrame(n)` | `int` | Seeks forward/backward by `n` keyframes. |
| `setCurrentPts(pts)` | `float` | Seeks to a specific presentation time. |

### Editor()
Handles low-level video information and editing.

| Method | Parameters | Description |
| :--- | :--- | :--- |
| `getVideoCount()` | None | Number of loaded videos. |
| `getWidth()` | None | Video width in pixels. |
| `getHeight()` | None | Video height in pixels. |
| `getFps1000()` | None | Frame rate multiplied by 1000. |
| `getDuration()` | None | Total duration in microseconds. |
| `getPts(frame)` | `int` | Presentation Time Stamp of a frame. |
| `getDts(frame)` | `int` | Decoding Time Stamp of a frame. |

### Gui()
Interaction with the user interface.

| Method | Parameters | Description |
| :--- | :--- | :--- |
| `displayInfo(title, msg)` | `str, str` | Shows an info dialog. |
| `displayError(title, msg)` | `str, str` | Shows an error dialog. |
| `fileSelRead(title)` | `str` | Opens a file selection dialog (Read). |
| `fileSelWrite(title)` | `str` | Opens a file selection dialog (Write). |
| `dirSelect(title)` | `str` | Opens a directory selection dialog. |

### Tools()
Miscellaneous helper functions.

| Method | Parameters | Description |
| :--- | :--- | :--- |
| `randint(min, max)` | `int, int` | Returns a random integer. |
| `time()` | None | Returns current epoch time. |
| `date()` | None | Returns a formatted date string. |
| `upper(str)` | `str` | Returns uppercase string. |
| `lower(str)` | `str` | Returns lowercase string. |

## Global Utility Functions (addons)

These are available without a class prefix:

- `get_folder_content(path, ext)`: Returns a list of files with a specific extension.
- `get_file_size(path)`: Returns the size of a file in bytes.
- `basename(path)`: Returns the filename part of a path.
- `dirname(path)`: Returns the directory part of a path.
- `splitext(path)`: Splits path into (root, ext) list.

## Passing Parameters (Couples)
Many functions like `videoCodec` accept "couples", which are string pairs passed as separate arguments:
```python
adm.videoCodec("x264", "quality=20", "bitrate=0")
```

### 💡 Pro Tip: Finding Plugin Parameters
If you are unsure about the parameters for a specific codec or filter:
1.  Configure the codec/filter in the Avidemux GUI.
2.  Go to **File -> Tinypy Project -> Save Project**.
3.  Open the saved `.py` file. It will contain the exact `videoCodec` or `addVideoFilter` call with all the required "couples" for that configuration.
Available parameters depend on the specific plugin (e.g., x264, x265, Lame).
