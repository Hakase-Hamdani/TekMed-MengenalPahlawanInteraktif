# Kamu dapat taruh script game mu di file ini.
default salah_flag = True
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
            jump menebak_dien


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
            jump menebak_dien

label menebak_dien:
    show a happy with dissolve
    if salah_flag:
        e "Kau mau main tebak-tebakkan?"
        e "Baiklah!"
    else:
        e "Mari kita ulang."

    show a normal at left with dissolve
    show p dien at right with dissolve:
        xalign 0.9
        yalign 0.5
    e "Siapakah yang ada di foto ini?"
    menu:
        "Sukarno":
            jump salah
        
        "Muhammad Hatta":
            jump salah

        "Kartini":
            jump salah

        "Cut Nyak Dien":
            jump menebak_soekarno
            hide p dien

label menebak_soekarno:
    show a happy at center with dissolve
    e "Kau Benar! Tadi itu adalah Cut Nyak Dien"

    show a normal at left with dissolve
    show p sukarno at right with dissolve:
        xalign 0.9
        yalign 0.5
    e "Siapa yang ada di foto ini?"
    menu:
        "Sukarno":
            jump menebak_kartini
            hide p sukarno
        
        "Muhammad Hatta":
            jump salah

        "Kartini":
            jump salah

        "Cut Nyak Dien":
            jump salah

label menebak_kartini:
    show a happy at center with dissolve
    e "Kau benar lagi! Tadi itu adalah Sukarno"

    show a normal at left with dissolve
    show p kartini at right with dissolve:
        xalign 0.9
        yalign 0.5
    e "Sekarang, siapakah yang ada di foto ini?"
    menu:
        "Sukarno":
            jump salah
        
        "Muhammad Hatta":
            jump salah

        "Kartini":
            jump menebak_hatta
            hide p kartini

        "Cut Nyak Dien":
            jump salah
            

label menebak_hatta:
    show a happy at center with dissolve
    e "Kau memang pintar! Tadi itu adalah foto Kartini"

    show a normal at left with dissolve
    show p hatta at right with dissolve:
        xalign 0.9
        yalign 0.5
    e "Terakhir, siapakah pahlawan yang ada di foto ini?"
    menu:
        "Sukarno":
            jump salah
        
        "Muhammad Hatta":
            jump final
            hide p hatta

        "Kartini":
            jump salah

        "Cut Nyak Dien":
            jump salah

label salah:
    $ salah_flag = False
    hide p dien
    hide p hatta
    hide p kartini
    hide p sukarno
    show a sad at center with dissolve
    e "Kau salah!"
    e "Kau harus mengulang!"
    jump menebak_dien

label final:
    show a happy at center with dissolve
    e "Hebat! Kau berhasil menjawab semua pertanyaan dengan benar!"
    show a sad
    e "Sayangnya, hanya itu saja tebakan yang saya punya..."
    show a normal
    e "Tetapi saya berharap akan lebih banyak konten lagi di tambahkan!"
    show a happy
    e "Bye!"
    jump habis

label habis:

    return
