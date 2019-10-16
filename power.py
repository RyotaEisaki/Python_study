import numpy as np
import cv2
import matplotlib.pyplot as plt

def main():
    # 入力画像をグレースケールで読み込み
    img = cv2.imread("input.png")

    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 高速フーリエ変換(2次元)
    fimg = np.fft.fft2(gray)
    
    # 第1象限と第3象限, 第2象限と第4象限を入れ替え
    fimg =  np.fft.fftshift(fimg)

    # パワースペクトルの計算
    mag = 20*np.log(np.abs(fimg))
    
    # 入力画像とスペクトル画像をグラフ描画
    plt.subplot(121)
    plt.imshow(gray, cmap = 'gray')
    plt.subplot(122)
    plt.imshow(mag, cmap = 'gray')
    plt.show()


if __name__ == "__main__":
    main()