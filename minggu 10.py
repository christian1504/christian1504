#menemukan nilai science dari smith
people = [
    {'name': 'bob', 'age': 20, 'score':{'math':90,'science':70}},
    {'name': 'carry', 'age': 38, 'score':{'math':40,'science':72}},
    {'name': 'smith', 'age': 28, 'score':{'math':80,'science':90}},
    {'name': 'john', 'age': 34, 'score':{'math':75,'science':100}}
]

for person in people:
    if person['name'] == 'smith':
        smith_science_score = person['score']['science']
        print(f"Nilai science dari orang yang bernama Smith adalah {smith_science_score}.")
#mencetak bilangan genap
def print_even_numbers(num_list):
    for num in num_list:
        if num % 2 == 0:
            print(num)
num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]
print_even_numbers(num_list)
#menghitung angka genap
num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]
even_nums = []
for num in num_list:
    if num % 2 == 0:
        even_nums.append(num)
print("Angka genap dalam list adalah:", even_nums)
#menjumlahkan semua angka dalam list
num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]
total = sum(num_list)
print(total)
#cari angka terbesar
num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]
max_num = max(num_list)
print(max_num)
#mencetak gender melalui nomor registrisi
def print_gender(registration_number):
    last_digit = int(registration_number.split("-")[1][-1])
    if last_digit in [1, 3]:
        print("Cowo")
    elif last_digit in [2, 4]:
        print("Cewe")
    else:
        print("Nomor Registrasi tidak valid")
