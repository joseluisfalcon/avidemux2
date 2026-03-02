# Example Script: Simple Remux (MP4 to MKV)
# Usage: avidemux_cli.exe --load input.mp4 --run remux_mkv.py --save output.mkv --quit

adm = Avidemux()
if not adm.loadVideo("input.mp4"):
    print("Error loading video")
else:
    # Simple Video and Audio Copy
    adm.videoCodec("Copy")
    adm.audioCodec(0, "copy")
    
    # Set Container
    adm.setContainer("MKV")
    
    # Save
    adm.save("output.mkv")
