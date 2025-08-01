#!/bin/bash

# YouTube 오디오 추출 스크립트
# Docker Compose를 사용하여 오디오 추출기를 실행합니다

echo "YouTube 오디오 추출을 시작합니다."
echo ""

# YouTube URL 입력 받기
read -p "YouTube URL을 입력하세요: " youtube_url

# URL 입력 검증
if [ -z "$youtube_url" ]; then
    echo "오류: URL이 입력되지 않았습니다."
    exit 1
fi

echo "URL: $youtube_url"
echo "오디오 추출을 진행합니다."
echo ""

# Docker Compose 명령어 실행 (URL을 인자로 전달)
docker-compose run --rm youtube-audio-extractor python audio_extractor.py "$youtube_url"

# 실행 결과 확인
if [ $? -eq 0 ]; then
    echo "오디오 추출이 성공적으로 완료되었습니다."
else
    echo "오디오 추출 중 오류가 발생했습니다."
    exit 1
fi
