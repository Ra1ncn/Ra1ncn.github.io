# Project demos

Add `clear.mp4`, `organizeit.mp4`, and `micromvp.mp4` here. Rebuild or restart Jekyll to replace the corresponding video placeholder with a native video player. Optional posters and text descriptions are configured in `_data/projects.yml`. See the root README for encoding guidance.

Demos should contain no audio track. For an existing H.264 MP4, remove audio without changing the video: `ffmpeg -i input.mp4 -map 0:v:0 -c:v copy -an -movflags +faststart output.mp4`. Keep the original separately and use the silent output on the website.
