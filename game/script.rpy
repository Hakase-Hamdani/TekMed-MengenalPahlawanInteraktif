# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
image bg = "images/bg_monas.jpg"
image normal = "images/eileen happy.png"
image sad = "images/eileen concerned.png"
image happy = "images/eileen vhappy.png"

image sukarno ="images/soekarno.jpg"
image hatta ="images/hatta.jpg"
image kartini ="images/kartini.jpg"
image dien ="images/dien.jpg"

# Deklarasikan karakter yang digunakan di game.
define e = Character('Eileen', color="#c8ffc8")

# Game dimulai disini.
label start:

    scene bg  with dissolve
    show happy
    e "Hai! Selamat Datang di Belajar Mengenal Pahlawan!"

    show normal at right
    e "Apa yang akan kita lakukan sekarang?"

    menu:
        "Belajar Mengenal.":
            jump mengenal

        "Belajar Menebak.":
            jump menebak


label mengenal:
    


    return
