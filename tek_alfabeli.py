# Bu programda harfler 13 adım ötelenecektir. Yani şöyle bir dönüşüm olacak:
# abcçdefgğhıijklmnoöprsştuüvyz
# klmnoöprsştuüvyzabcçdefgğhıij
# bu satırı boşverin: a,b,c,ç,d,e,f,g,ğ,h,ı,i,j,k,l,m,n,o,ö,p,r,s,ş,t,u,ü,v,y,z

print("Aşağıdaki seçeneklere göre ne tip bir işlem yapmak istediğinize göre sayı seçin:")
print("Şifreleme yapmak : 0\nŞifre çözmek : 1")
islem = input("İstediğiniz işlemin numarası: ")

alfabe = ["a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z"]

if islem == "0":
    metin = input("Lütfen şifrelemek istediğiniz metni boşluk bırakmadan ve noktalama işareti koymadan giriniz: ")
    metin_sifre = []
    for x in range(0,len(metin)):
        indis = alfabe.index(metin[x])
        indis += 13                                     # 13 adım kaydırıyorum.
        sifrelenmis_indis = indis % 29
        metin_sifre.append(alfabe[sifrelenmis_indis])
    print("Metninizin şifrelenmiş hali: ", end="")
    print(*metin_sifre, sep="")

if islem == "1":
    metin = input("Lütfen şifresini çözmek istediğiniz metni boşluk bırakmadan ve noktalama işareti koymadan giriniz: ")
    metin_normal = []
    for x in range(0,len(metin)):
        indis = alfabe.index(metin[x])
        indis += 16                                     # 13 adım geri gitmek yerine 16 adım ileri de gidilebilir.
        normal_indis = indis % 29
        metin_normal.append(alfabe[normal_indis])
    print("Metninizin çözümlenmiş hali: ", end="")
    print(*metin_normal, sep="")
