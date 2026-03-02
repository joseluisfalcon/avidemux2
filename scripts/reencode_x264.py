# Example Script: Re-encoding to MKV with x264
# Usage: avidemux_cli.exe --load input.mp4 --run reencode_x264.py --save output.mkv --quit

adm = Avidemux()
if not adm.loadVideo("input.mp4"):
    print("Error: Could not load input.mp4")
else:
    # Set Video Codec
    adm.videoCodec("x264", "quality=20", "bitrate=0", "useCron=False")
    
    # Set Audio Codec (Copy)
    adm.audioClearTracks()
    adm.audioAddTrack(0)
    adm.audioCodec(0, "copy")
    
    # Set Output Format
    adm.setContainer("MKV")
    
    # Save the result
    if not adm.save("output.mkv"):
        print("Error: Failed to save output.mkv")
    else:
        print("Success: File saved as output.mkv")
