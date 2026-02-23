import numpy as np
from scipy.fft import fft, fftfreq
from pydub import AudioSegment
import matplotlib.pyplot as plt

def analyze_audio_spectrum_mp3(file_path):
    try:
        # Đọc file âm thanh MP3 bằng pydub
        audio_segment = AudioSegment.from_mp3(file_path)

        # Chuyển đổi sang dạng mảng NumPy
        audio_data = np.array(audio_segment.get_array_of_samples())

        # Lấy tần số lấy mẫu (sampling rate)
        sr = audio_segment.frame_rate

        # Nếu là âm thanh stereo (nhiều kênh), lấy một kênh để phân tích
        if len(audio_data.shape) > 1:
            audio_data = audio_data[:, 0]

        # Số điểm dữ liệu trong tín hiệu âm thanh
        N = len(audio_data)

        # Thực hiện FFT
        yf = fft(audio_data)

        # Tính toán các tần số tương ứng
        xf = fftfreq(N, 1 / sr)

        # Lấy biên độ và tần số cho nửa đầu (tần số dương)
        amplitude = np.abs(yf[:N//2])
        frequencies = xf[:N//2]

        return frequencies, amplitude

    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{file_path}' 😞")
        return None, None
    except Exception as e:
        print(f"Đã xảy ra lỗi khi xử lý file '{file_path}': {e} 😥")
        return None, None

def plot_spectrum(frequencies, amplitude, title):
    plt.figure(figsize=(8, 2))
    plt.plot(frequencies, amplitude)
    plt.title(title)
    plt.xlabel("Tần số (Hz)")
    plt.ylabel("Biên độ")
    plt.grid(True)
    max_freq_display = min(np.max(frequencies), 30000) # Giới hạn hiển thị tối đa 30kHz
    plt.xlim(0, max_freq_display)
    plt.show()

file_am_thanh_1_mp3 = 'original.mp3'
file_am_thanh_2_mp3 = 'DNA.mp3'

# Phân tích và vẽ phổ cho file MP3 1
frequencies1_mp3, amplitude1_mp3 = analyze_audio_spectrum_mp3(file_am_thanh_1_mp3)
if frequencies1_mp3 is not None:
    plot_spectrum(frequencies1_mp3, amplitude1_mp3, f"Phổ tần số của: {file_am_thanh_1_mp3}")

# Phân tích và vẽ phổ cho file MP3 2
frequencies2_mp3, amplitude2_mp3 = analyze_audio_spectrum_mp3(file_am_thanh_2_mp3)
if frequencies2_mp3 is not None:
    plot_spectrum(frequencies2_mp3, amplitude2_mp3, f"Phổ tần số của: {file_am_thanh_2_mp3}")

