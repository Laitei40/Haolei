#!/bin/sh

while true; do
    echo -n "Enter video file name (e.g., video.mp4) or q to quit: "
    read video
    if [ "$video" = "q" ]; then
        echo "Quitting..."
        break
    fi

    if [ ! -f "$video" ]; then
        echo "❌ File not found: video"
        continue
    fi

    echo -n "Enter output audio file name (e.g., audio.mp3): "
    read audio

    ffmpeg -i "$video" -vn -acodec copy "audio"
    echo "✅ Converted:audio"
done
