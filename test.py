import cv2
import matplotlib.pyplot as plt

# 영상 파일 경로 지정
video_path = '/hub_data2/intern/jinwoo/iVQA/videos/TDD6qC0PKy8_354_366.webm'  # 예시 파일명

# 비디오 열기
cap = cv2.VideoCapture(video_path)

# 총 프레임 수 확인
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(f"총 프레임 수: {frame_count}")

# 몇몇 프레임 시각화 (예: 0%, 25%, 50%, 75%, 100%)
sample_indices = [0, frame_count//4, frame_count//2, (3*frame_count)//4, frame_count-1]
frames = []

for idx in sample_indices:
    cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
    ret, frame = cap.read()
    if ret:
        # BGR → RGB 변환 (matplotlib용)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frames.append((idx, frame_rgb))

cap.release()

# 시각화
plt.figure(figsize=(15, 4))
for i, (frame_idx, frame_img) in enumerate(frames):
    plt.subplot(1, len(frames), i+1)
    plt.imshow(frame_img)
    plt.title(f'Frame {frame_idx}')
    plt.axis('off')
plt.tight_layout()
plt.savefig("frame.png")

# plt.show()