#!/usr/bin/env python3
"""
YouTube URL에서 오디오를 추출하는 독립적인 프로그램
"""

import os
import sys


def download_youtube_video(url: str) -> str:
    """
    YouTube URL에서 비디오를 다운로드합니다.

    Args:
        url: YouTube URL

    Returns:
        다운로드된 비디오 파일 경로

    Raises:
        Exception: 다운로드 실패 시
    """
    try:
        import yt_dlp

        # 다운로드 옵션 설정
        ydl_opts = {
            "format": "best[ext=mp4]",
            "outtmpl": "downloads/%(title)s.%(ext)s",
        }

        # downloads 디렉토리 생성
        os.makedirs("downloads", exist_ok=True)

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # 비디오 정보 추출
            info = ydl.extract_info(url, download=False)
            filename = ydl.prepare_filename(info)

            # 비디오 다운로드
            ydl.download([url])

            return filename

    except ImportError:
        raise Exception(
            "yt-dlp 패키지가 설치되지 않았습니다. 'pip install yt-dlp'로 설치해주세요."
        )
    except Exception as e:
        raise Exception(f"YouTube 비디오 다운로드 실패: {str(e)}")


def extract_audio_from_video(video_path: str, audio_path: str) -> None:
    """
    비디오 파일에서 오디오를 추출합니다.

    Args:
        video_path: 입력 비디오 파일 경로
        audio_path: 출력 오디오 파일 경로

    Raises:
        Exception: 오디오 추출 실패 시
    """
    try:
        import ffmpeg

        # FFmpeg를 사용하여 오디오 추출
        (
            ffmpeg.input(video_path)
            .output(audio_path, acodec="pcm_s16le", ac=1, ar="16000")
            .overwrite_output()
            .run(quiet=True)
        )

    except ImportError:
        raise Exception(
            "ffmpeg-python 패키지가 설치되지 않았습니다. 'pip install ffmpeg-python'로 설치해주세요."
        )
    except Exception as e:
        raise Exception(f"오디오 추출 실패: {str(e)}")


def delete_file(file_paths: list) -> None:
    """
    파일들을 삭제합니다.

    Args:
        file_paths: 삭제할 파일 경로 리스트
    """
    for file_path in file_paths:
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"파일 삭제됨: {file_path}")
        except Exception as e:
            print(f"파일 삭제 실패 {file_path}: {str(e)}")


def extract_audio_from_youtube_url(url: str) -> str:
    """
    YouTube URL에서 오디오를 추출하는 메인 함수

    Args:
        url: YouTube URL

    Returns:
        추출된 오디오 파일 경로

    Raises:
        Exception: 처리 과정에서 오류 발생 시
    """
    video_file_path = None
    audio_file_path = None

    try:
        print(f"YouTube URL 처리 시작: {url}")

        # 1. YouTube 비디오 다운로드
        print("비디오 다운로드 중...")
        video_file_path = download_youtube_video(url)
        print(f"비디오 다운로드 완료: {video_file_path}")

        # 2. 오디오 파일 경로 설정
        base, _ = os.path.splitext(video_file_path)
        audio_file_path = f"{base}.wav"

        # 3. 오디오 추출
        print("오디오 추출 중...")
        extract_audio_from_video(video_file_path, audio_file_path)
        print(f"오디오 추출 완료: {audio_file_path}")

        # 4. 임시 파일 정리
        delete_file([video_file_path])

        return audio_file_path

    except Exception as e:
        # 오류 발생 시 생성된 파일들 정리
        if video_file_path and os.path.exists(video_file_path):
            delete_file([video_file_path])
        if audio_file_path and os.path.exists(audio_file_path):
            delete_file([audio_file_path])

        raise Exception(f"오디오 추출 실패: {str(e)}")


def main():
    """메인 실행 함수"""
    if len(sys.argv) < 2:
        print("사용법: python audio_extractor.py <YouTube_URL>")
        print(
            "예시: python audio_extractor.py https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        )
        sys.exit(1)

    url = sys.argv[1]

    try:
        audio_path = extract_audio_from_youtube_url(url)
        print(f"\n✅ 성공! 오디오 파일이 생성되었습니다: {audio_path}")

    except Exception as e:
        print(f"\n❌ 오류 발생: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
