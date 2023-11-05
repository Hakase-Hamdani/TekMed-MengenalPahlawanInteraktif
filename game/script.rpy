# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
image bg = "images/bg_monas.jpg"
image a normal = "images/eileen happy.png"
image a sad = "images/eileen concerned.png"
image a happy = "images/eileen vhappy.png"

image p sukarno ="images/soekarno.jpg"
image p hatta ="images/hatta.jpg"
image p kartini ="images/kartini.jpg"
image p dien ="images/dien.jpg"

# Deklarasikan karakter yang digunakan di game.
define e = Character('Eileen', color="#ff0000")

# Game dimulai disini.
label start:

    scene bg  with dissolve
    show a happy with dissolve
    e "Hai! Selamat Datang di Belajar Mengenal Pahlawan!"

    show a normal at right with dissolve
    e "Apa yang akan kita lakukan sekarang?"

    menu:
        "Belajar Mengenal.":
            jump mengenal

        "Belajar Menebak.":
            jump menebak


label mengenal:
    show a happy at left with dissolve
    show p sukarno with dissolve:
        xalign 0.5
        yalign 0.5
    e "Gambar yang kau lihat di tengah ini adalah gambar Sukarno."
    e "Soekarno adalah proklamator kemerdekaan Indonesia pada tanggal 17 Agustus 1945."
    e "Soekarno dikenal sebagai pemimpin karismatik yang memainkan peran kunci dalam perjuangan kemerdekaan Indonesia dari penjajahan Belanda."
    e "Ia juga menjadi Presiden pertama Republik Indonesia yang memimpin negara tersebut dari tahun 1945 hingga 1967."

    show p hatta with dissolve:
        xalign 0.5
        yalign 0.5
    e "Berikutnya adalah Muhammad Hatta."
    e "Ia adalah salah satu pemimpin kemerdekaan Indonesia bersama dengan Soekarno."
    e "Bersama-sama, Soekarno dan Hatta memainkan peran kunci dalam perjuangan kemerdekaan Indonesia dari penjajahan Belanda."
    e " Ia juga merupakan salah satu penulis Piagam Jakarta pada tahun 1945, yang menjadi dasar bagi Proklamasi Kemerdekaan Indonesia pada tanggal 17 Agustus 1945."

    show p kartini with dissolve:
        xalign 0.5
        yalign 0.5
    e "Berikutnya adalah Kartini."
    e "Juga Dikenal sebagai Raden Ajeng Kartini, ia dikenal sebagai pelopor perjuangan hak-hak perempuan dan pendidikan perempuan di Indonesia."
    e "Kartini dianggap sebagai simbol penting dalam sejarah perjuangan hak-hak perempuan dan pendidikan di Indonesia."

    show p dien with dissolve:
        xalign 0.5
        yalign 0.5
    e "Untuk saat ini, yang terakhir adalah Cut Nyak Dien."
    e "Cut Nyak Dien adalah salah seorang pemimpin perlawanan Aceh yang gigih terhadap invasi Belanda."
    e "Cut Nyak Dien dihormati sebagai pahlawan nasional Indonesia karena perjuangan kerasnya dalam mempertahankan kemerdekaan dan budaya Aceh dari penjajahan Belanda."

    hide p dien with dissolve
    show a happy at center with dissolve
    e "Karena Game ini masih dalam tahap awal, masih tidak banyak pahlawan yang bisa saya kenalkan."
    e "Saya benar-benar minta maaf."


label start2:

    show a normal at right with dissolve
    e "Apa yang akan kita lakukan sekarang?"

    menu:
        "Belajar Mengenal.":
            jump mengenal

        "Belajar Menebak.":
            jump menebak

label menebak_dien:
    show a happy with dissolve
    e "Kau mau main tebak-tebakkan?"
    e "Baiklah!"

    show a normal at left with dissolve
    show p dien at right with dissolve:
        xalign 0.5
        yalign 0.5
    e "Siapakah yang ada di foto ini?"
    menu:
        "Sukarno"
        
        "Muhammad Hatta"

        "Kartini"

        "Cut Nyak Dien"

label benar:
    show a happy at center with dissolve
    e "Kau Benar!"

label salah:
    show a sad at center with dissolve


    return
