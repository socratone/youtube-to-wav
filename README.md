# YouTube To WAV

YouTube URL에서 오디오를 추출하여 WAV 파일로 변환하는 프로그램입니다.

## 설치 및 실행

### 필수 요구사항

- Docker
- Docker Compose
- Bash (Linux/macOS 기본 제공)

### 설치

1. 저장소를 클론합니다:

```bash
git clone <repository-url>
cd youtube-to-wav
```

2. 스크립트에 실행 권한을 부여합니다:

```bash
chmod +x extract.sh
```

## 사용법

### 기본 사용법

```bash
./extract.sh
```

스크립트를 실행하면 YouTube URL 입력을 요청합니다.

### 예시

```bash
# 스크립트 실행
./extract.sh

# 실행 후 나타나는 프롬프트에 URL 입력
YouTube URL을 입력하세요: https://youtu.be/ez9y6qqkR98?si=tAMdTWMCLHAMLs1F
```

## 작동 방식

이 프로그램은 Docker Compose를 사용하여 격리된 환경에서 실행됩니다:

1. `./extract.sh` 스크립트가 실행되면
2. 사용자에게 YouTube URL 입력을 요청합니다
3. 입력된 URL을 검증하고 Docker Compose가 컨테이너를 시작합니다
4. Python 스크립트 `audio_extractor.py`가 YouTube URL을 처리하여
5. 오디오를 추출하고 WAV 파일로 변환합니다

## 출력

추출된 WAV 파일은 프로젝트 디렉토리에 저장됩니다.
