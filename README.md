# YouTube To WAV

YouTube URL에서 오디오를 추출하여 WAV 파일로 변환하는 프로그램입니다.

## 설치 및 실행

### 필수 요구사항

- Node.js
- Docker
- Docker Compose

### 설치

1. 저장소를 클론합니다:

```bash
git clone <repository-url>
cd youtube-to-wav
```

2. npm 의존성을 설치합니다:

```bash
npm install
```

## 사용법

### 기본 사용법

```bash
npm run extract <YouTube_URL>
```

### 예시

```bash
# YouTube 비디오에서 오디오 추출
npm run extract https://www.youtube.com/watch?v=dQw4w9WgXcQ

# 임시 파일 유지 옵션과 함께 실행
npm run extract https://www.youtube.com/watch?v=dQw4w9WgXcQ --keep-files
```

### 옵션

- `--keep-files`: 추출 과정에서 생성된 임시 파일들을 삭제하지 않고 유지합니다.

## 작동 방식

이 프로그램은 Docker Compose를 사용하여 격리된 환경에서 실행됩니다:

1. `npm run extract` 명령어가 실행되면
2. Docker Compose가 컨테이너를 시작하고
3. Python 스크립트 `audio_extractor.py`가 YouTube URL을 처리하여
4. 오디오를 추출하고 WAV 파일로 변환합니다

## 출력

추출된 WAV 파일은 프로젝트 디렉토리에 저장됩니다.
