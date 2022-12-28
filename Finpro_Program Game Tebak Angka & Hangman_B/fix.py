import random
import string


print()
urname = input("siapa namamu?")
print(f"Selamat Datang {urname}!")
print(f"selamat bersenang senang pada permainan kali ini")
print()
print("sistem ini mempunyai 2 game yaitu:")
print("1. Tebak angka")
print("2. Hangman")
print("3. Keluar")
print()
pilih = int(input("Mau bermain bermain permainan 1 atau 2"))
print()

if pilih == 1:
	print()
	print("Selamat bermain pada permainan Tebak Angka !!!")
	print("noted : anda dapat memasukan jumlah digit yang banyak untuk pengalaman bermain yang gokill!!")
	while(True): # while loop yang akan diisi oleh seluruh isi game
		try:
			num = int(input("Masukkan jumlah digit angka yang ingin di tebak: "))
			if num == 0: # error handling bila input digitnya bernilai 0
				print("digit 0 mau nebak angka berapa hihi, isi lainya yaa")
				continue
			else:
				secret = str(random.randint(10**(num-1), 10**(num)-1))
				print("Pilih jumlah nyawa:\n 1. tak terbatas\n 2. custom")
				lives = int(input("masukkan pilihan nyawa (1/2): "))
				if lives == 1:
					pass # langsung ke game
				elif lives == 2: # pilihan berapa nyawa
					choice = int(input("masukkan kesempatan nyawa: "))
				else:
					print("Pilihan tidak valid!")
					continue

				# ROOKIE LEVEL WITH UNLIMITED LIVES
				if lives == 1:
					while(True):
						guess = input("Tebak: ")
						if guess.isdecimal() == False: # Memeriksa apakah string berisi angka
							print("silahkan masukkan tebakan angka")
							continue
						if len(guess) != len(secret):
							print(f"Bilangan harus {len(secret)} digit!")
						else:
							if guess < secret:
								print("angka yang anda masukkan kurang besar")
							if guess > secret:
								print("angka yang anda masukkan kurang kecil")
							if guess == secret:
								print(f"selamat cs, angka yang kamu tebak benar! (Jawaban: {secret})")
								print(f"jangan lupa coba permainan hangman juga ya!!")
								print(f"HAVING FUN AND ENJOY THE GAME")
								break
				# ROOKIE LEVEL WITH CUSTOM LIVES
				elif lives == 2:
					for i in range(choice):
						i += 1 # i berfungsi sebagai penanda apabila nyawa sudah habis
						guess = input("Tebak: ")
						if guess.isdecimal() == False:
							print("silahkan masukkan tebakan angka")
							continue
						if len(guess) != len(secret): #bila tebakkan tidak sesuai digit
							print(f"Bilangan harus {len(secret)} digit!")
						else:
							if guess < secret:
								print("angka yang anda masukkan kurang besar")
							elif guess > secret:
								print("angka yang anda masukkan kurang kecil")
							else:
								print(f"selamat cs, angka yang kamu tebak benar! (Jawaban: {secret})")
								print(f"jangan lupa coba permainan hangman juga ya!!")
								print(f"HAVING FUN AND ENJOY THE GAME")
								break
							if i == choice: # jika jumlah i sama dengan jumlah nyawa dan tebakan salah
								print(f"Maaf, nyawa anda sudah habis. (Secret number: {secret})")
								break

		except ValueError: # error handling jika input type int bukan int
			print("Mohon masukkan bilangan :)")
			continue
		break

elif pilih == 2:

	WORDLIST = "nama_mobil.txt"

	def load_words():
		print()
		inFile = open(WORDLIST, 'r')
		# line: string
		line = inFile.read()
		# wordlist: list of strings
		wordlist = line.split()
		return wordlist
	def choose_word(wordlist): # Memasukkan jawaban ke sebuah variable
		return random.choice(wordlist)

	wordlist = load_words()

	def is_word_guessed(secret_word, letters_guessed):
		if secret_word == get_guessed_word(secret_word, letters_guessed):
			return True # jika jawaban sama dengan hasil return dari get_guessed_word maka TRUE
		return False
	def get_guessed_word(secret_word, letters_guessed):
		split = list(secret_word) # dibuat list yang berisi tiap character dari secret_word
		n = 0 # hitung
		blank = "" # string yang digunakan untuk mengubah list split menjadi str kembali
		for i in split:
			if i not in letters_guessed: # jika huruf belum ketebak, huruf tersebut diganti dengan "_"
				split.remove(split[n]) # elemen pada index n di-remove
				split.insert(n, "_ ") # kemudian index tersebut di insert dengan "_"
			n += 1 # n di increment sampai i habis
		new_word = blank.join(split) # lalu list di convert kembali ke string
		return new_word

	def get_available_letters(letters_guessed):
		alphabet = "abcdefghijklmnopqrstuvwxyz" # string berisi seluruh huruf lowercase yang belum ditebak
		alphalist = list(alphabet) # kemudian dibuat menjadi list
		blank = ""
		for i in letters_guessed: # jika huruf ada di letters_guessed maka huruf itu akan di remove dari list
			if i in alphalist:
				alphalist.remove(i)
			alphabet = blank.join(alphalist)
		return alphabet

	def hangman(secret_word):
		while(True): # while loop pertama untuk handle input nyawa yang bukan integer
			try:
				print("Selamat bermain pada permainan Hangman!")
				print("Mari kita tebak sebuah merk mobil pada permainan kali ini")
				print("Masukan nyawa sedikit mungkin, agar permainan lebih menantang dan seru !!")
				lives = int(input("Silahkan masukkan jumlah nyawa: "))
				print(f"Panjang kata: {len(secret_word)} huruf.")
				break
			except ValueError:
				print("silahkan masukkan angka")
		while lives != 0: # loop akan berjalan selama lives belum 0
			print("-"*10)
			print(f"nyawa anda yang tersisa: {lives}")
			print(f"ingat kita punya huruf ini saja, ayo tebak!: {get_available_letters(letters_guessed)}")
			base = input("Masukkan huruf: ")
			if base.isalpha() == False: # jika tebakan bukan alphabet akan di handle
				print("Memasukkan huruf")
				continue
			letter = base.lower() # input dibuat lowercase agar tidak case sensitive
			if letter in letters_guessed: # jika huruf sudah ketebak
				print("Anda usai memasukan huruf ini!")
				continue
			else:
				letters_guessed.append(letter) # huruf di append ke list letters_guessed
			if letter in secret_word:
				print(f"tebakan benar! lanjut tebak lagi ya {get_guessed_word(secret_word, letters_guessed)}")
			else:
				print(f"yahh tebakanmu salah, tebak sekali lagi hingga benar yaa!! {get_guessed_word(secret_word,letters_guessed)}")
				lives -= 1
			# kondisi menang
			if is_word_guessed(secret_word, letters_guessed) == True:
				print("Selamat cs!! kamu menang pada permainan ini!")
				print("Jangan lupa mencoba permainan tebak angka yaa!!")
				break
			else:
				continue # jika belum ketebak maka loop diulang lagi
		# kondisi kalah
		if lives == 0:
			print(f"akhirnyaa tebakanmu salah semua dan nyawamu sudah habis, tetap semangat dan coba bermain dilain waktu ya!!! :(\nJawaban: {secret_word}")
			print(f"jangan lupa mencoba permainan tebak angka yaa!!")
	if __name__ == "__main__":

		secret_word = choose_word(wordlist).lower() # dibuat lower
		letters_guessed = []
		hangman(secret_word)
if pilih == 3:
	print("anda keluar dari game, see you")

else:
	print("maaf hanya ada game tebak angka dan hangman saja cs:))..")
