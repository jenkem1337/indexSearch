
def indexSerach(array, somethingInArray):
    i = 0
    while i <= len(array):
        if somethingInArray == array[i]:
            print(f"Your index in here => {i}")
            break
        else:
            i = i + 1
            
#exemple in below             
while True:
    cities = ["adana", "adiyaman", "afyon", "agri", "amasya", "ankara", "antalya", "artvin", "aydin", "balikesir", "bilecik", "bingol", "bitlis", "bolu", "burdur", "bursa", "canakkale", "cankiri", "corum", "denizli", "diyarbakir", "edirne", "elazig", "erzincan", "erzurum", "eskisehir", "gaziantep", "giresun", "gumushane", "hakkari", "hatay", "isparta", "icel (mersin)", "istanbul", "izmir", "kars", "kastamonu", "kayseri", "kirklareli", "kirsehir", "kocaeli", "konya", "kutahya", "malatya", "manisa", "kahramanmaras", "mardin", "mugla", "mus", "nevsehir", "nigde", "ordu", "rize", "sakarya", "samsun", "siirt", "sinop", "sivas", "tekirdag", "tokat", "trabzon", "tunceli", "sanliurfa", "usak", "van", "yozgat", "zonguldak", "aksaray", "bayburt", "karaman", "kirikkale", "batman", "sirnak", "bartin", "ardahan", "igdir", "yalova", "karabuk", "kilis", "osmaniye", "duzce"]
    whichCity = input("Enter any city : ")
    if whichCity not in cities:
        print("if not in city in array you may have written it wrong, try again")
    
    indexSerach(cities, whichCity)
    
    #indexSerach(cities, whichCity(istanbul)
    # it will return "Your index in here => 33"

    
