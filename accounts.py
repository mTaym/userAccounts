username_list = ["alice", "bob", "charlie"]
password_list = ["123456", "234567", "345678"]

# Kayıt fonksiyonu
def kayit(username, password):
    username_list.append(username)
    password_list.append(password)
    print(f"{username} isimli kullanıcının kaydı başarıyla oluşturuldu.")

# Giriş Fonksiyonu
def giris(username, password):
    if username in username_list:
        pos = username_list.index(username)
        if password_list[pos] == password:
            print(f"{username} isimli kullanıcı giriş yaptı.")
            return True
        else:
            print("Kullanıcı adınız veya parolanız yanlış.")
    else:
        print("Kullanıcı adınız veya parolanız yanlış.")
        return False