from tkinter import *
import base64
import PIL
top = Tk()
IMAGE = "iVBORw0KGgoAAAANSUhEUgAAADcAAAA3CAYAAACo29JGAAAABGdBTUEAAK/INwWK6QAAABl0RVh0U29\
mdHdhcmUAQWRvYmUgSW1hZ2VSZWFkeXHJZTwAAAJsSURBVHja7JrrbYMwEIAvqAu4I7Qj0BHMCGQEGAF\
GgBGaEcIIZYRkBVZgBArSIbmubTAPc0Y56X7EhITP9wYuXdfBWSWAE8sl/D4Vz0DT9Fo+kg7eTgIVIxj\
rte21GiB9h2MIFQtrFVrPa8uJ1gK0WIpw4DPcXbLWs9fraDFfs2XY60Phhl8ymG9wMYKFwlqOFlOKL25\
Z9JpJa1Gvtekk6nAM44sLaw1a6zl1MmW4DwQLJbBIFV8+wQ1AP0KaHzNihCnf296SY+JYBUYRjqPFRKk\
x1be2P0YJLtGARb6PPAm2UqDoOrye53Rg0RJXpAQXK8DGOtau/fHg4ORxl9ZamzpGFS5UJA/YEuwoOB3\
YrJaKMtzYUjFpPReHTF/h7ggI0jxW7vFngWOwcOtaRgEuk6bnMTNe9/xTF3AxDpuypFtmxiPgPhRFGjD\
Gqr13NXAQZ0wRZ7mLWAgUY/0QHx2qKrvZ3PcIXceZbhLnip2O8QJtO4cY/t/QGd2xcQUXSLMU08SN7ph\
NnO1Wz0xwDLWZuOBsRZy1ruJMhmtxRz8ndjZTxNDc7zh1R11CyScAiwnrqo7Xrt3RVApyQ3fO4e8NUlF\
0jzFzOEh0de464XqqNa5xxyc1uMbgSlyKK12yaY9yxzkdSmm4j5FIVmOW5x8OZ9r5BIG4BDrH8iTgBrl\
NWK8wWB2ow7WG7r3Q1LQGN4U83BIrkLDaXLjGYvYiYzWbee628fdIwdUze0Mv4eZc+O3ourYWznTxFRA\
TGzhTWUhh4rUJ6nAq6wyf36nF2lK4WnDNFDZ6jraXLHlVo0TIJxCXy+sd5xccPfkVYADDOZXimxZ6tAA\
AAABJRU5ErkJggg=="
button_image = ImageTk.PhotoImage(data=base64.b64decode(IMAGE)) # desencodifica a imagem
ok_button = Button(top, text="ok",image=button_image,compound=LEFT)
ok_button.grid()
top.mainloop()