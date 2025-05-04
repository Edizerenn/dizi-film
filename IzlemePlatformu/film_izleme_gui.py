import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from tkinter import font as tkfont
import random

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.watchlists = {category: [] for category in categories}
        self.favorites = []
        self.history = []

class Content:
    def __init__(self, title, genre, duration, description=""):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.description = description
        self.rating = 0
        self.comments = []

    def __str__(self):
        return f"{self.title} | {self.genre} | {self.duration} dk | {self.get_rating()}"

    def add_comment(self, comment):
        self.comments.append(comment)

    def set_rating(self, rating):
        if 1 <= rating <= 5:
            self.rating = rating
        else:
            messagebox.showerror("Hatalı Puan", "Puan 1 ile 5 arasında olmalıdır.")

    def get_rating(self):
        return f"Rating: {self.rating} / 5"

categories = [
    "Favorilerim", "Daha Sonra İzle", "Aksiyon", "Komedi", "Bilim Kurgu",
    "Romantik", "Animasyon", "Gerilim", "Korku", "Dram",
    "Belgesel", "Macera", "Tarihî", "Fantastik", "Yabancı Diziler"
]

sample_contents = [
    Content("Inception", "Bilim Kurgu", 148, "Zihinlere giren bir hırsız, bir iş adamına fikir çalmayı teklif eder."),
    Content("Titanic", "Romantik", 195, "Titanik gemisinde geçen bir aşk hikayesi, trajik bir şekilde sona erer."),
    Content("Shrek", "Animasyon", 90, "Yeşil bir orman yaratığı, prensesi kurtarmak için yola çıkar."),
    Content("Breaking Bad", "Dram", 60, "Bir lise öğretmeni, meth üreticisi olarak suç dünyasına adım atar."),
    Content("The Witcher", "Fantastik", 55, "Bir canavar avcısı, mistik yaratıklarla savaşır."),
    Content("The Matrix", "Bilim Kurgu", 136, "Bir hacker, dünyanın gerçeğini öğrenir."),
    Content("Avatar", "Bilim Kurgu", 162, "Felçli bir adam, Pandora adlı bir gezegende yerli halkla etkileşime girer."),
    Content("The Dark Knight", "Aksiyon", 152, "Batman, Joker ile Gotham şehrini kurtarmak için savaşır."),
    Content("Guardians of the Galaxy", "Aksiyon, Bilim Kurgu", 121, "Bir grup uzay maceracısı, kozmik bir kötüye karşı savaşır."),
    Content("The Godfather", "Dram, Suç", 175, "Bir mafya ailesinin gücünü ve içsel çatışmalarını anlatan bir hikaye."),
    Content("Pulp Fiction", "Dram, Suç", 154, "Los Angeles'ta suç dünyasında geçen bir dizi birbirine bağlı hikaye."),
    Content("The Shawshank Redemption", "Dram", 142, "Yanlış suçlamalarla hapse giren bir adam, umudunu kaybetmeden hayatta kalmaya çalışır."),
    Content("Forrest Gump", "Dram, Romantik", 142, "Forrest Gump’ın sıra dışı hayatı, tüm Amerika’yı etkiler."),
    Content("The Lion King", "Animasyon, Macera", 88, "Bir aslan yavrusu, hayatı ve sorumlulukları hakkında derin dersler alır."),
    Content("Spider-Man: No Way Home", "Aksiyon, Fantastik", 148, "Spider-Man, çoklu evrenin ortaya çıkmasıyla karşı karşıya gelir."),
    Content("Interstellar", "Bilim Kurgu, Dram", 169, "Bir grup astronot, bir solan dünyadan kurtulmak için yeni bir gezegen arar."),
    Content("Joker", "Dram, Suç", 122, "Bir adamın toplumdan dışlanarak, Joker adlı kötü karaktere dönüşümünü anlatan hikaye."),
    Content("Inglourious Basterds", "Aksiyon, Savaş", 153, "Bir grup asker, II. Dünya Savaşı sırasında Nazi subaylarını hedef alır."),
    Content("Mad Max: Fury Road", "Aksiyon, Macera", 120, "Kıyamet sonrası dünyada, Max, bir grup isyancıya yardım eder."),
    Content("The Avengers", "Aksiyon, Macera, Bilim Kurgu", 143, "Bir grup süper kahraman, dünyayı korumak için bir araya gelir.")
]



users = {}
current_user = None

class WatchApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Film ve Dizi İzleme Platformu")
        self.geometry("1000x700")
        self.resizable(True, True)
        self.config(bg="#e5e8e8")
        self.login_screen()

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

    def login_screen(self):
        self.clear_screen()

        title_font = tkfont.Font(family="Helvetica", size=26, weight="bold")
        tk.Label(self, text="Film ve Dizi İzleme", font=title_font, fg="#ba4a00", bg="#e5e8e8").pack(pady=40)

        tk.Label(self, text="Kullanıcı Adı:", font=("Arial", 14), fg="#283747", bg="#e5e8e8").pack(pady=5)
        username_entry = tk.Entry(self, font=("Arial", 14), bd=2, relief="solid", highlightbackground="#F39C12")
        username_entry.pack(pady=10)

        tk.Label(self, text="Şifre:", font=("Arial", 14), fg="#283747", bg="#e5e8e8").pack(pady=5)
        password_entry = tk.Entry(self, show="*", font=("Arial", 14), bd=2, relief="solid", highlightbackground="#F39C12")
        password_entry.pack(pady=10)

        def login():
            username = username_entry.get()
            password = password_entry.get()
            global current_user
            user = users.get(username)
            if user and user.password == password:
                current_user = user
                self.main_screen()
            else:
                messagebox.showerror("Hatalı Giriş", "Kullanıcı adı veya şifre hatalı.")

        def register():
            username = username_entry.get()
            password = password_entry.get()
            if username in users:
                messagebox.showerror("Hata", "Bu kullanıcı adı zaten kullanılıyor.")
            else:
                users[username] = User(username, password)
                messagebox.showinfo("Başarılı", "Kayıt tamamlandı!")

        login_button = tk.Button(self, text="Giriş Yap", command=login, bg="#2980b9", fg="#fff", font=("Arial", 14), relief="solid", width=20, height=2)
        login_button.pack(pady=10)
        register_button = tk.Button(self, text="Kayıt Ol", command=register, bg="#27ae60", fg="#fff", font=("Arial", 14), relief="solid", width=20, height=2)
        register_button.pack(pady=10)

    def main_screen(self):
        self.clear_screen()

        welcome_font = tkfont.Font(family="Arial", size=20, weight="bold")
        tk.Label(self, text=f"Hoş geldin, {current_user.username}!", font=welcome_font, fg="#F39C12", bg="#e5e8e8").pack(pady=20)

        random_content_button = tk.Button(self, text="Rastgele İçerik Öner", command=self.random_content, bg="#16a085", fg="#fff", font=("Arial", 14), relief="solid", width=20, height=2)
        random_content_button.pack(pady=10)

        search_frame = tk.Frame(self, bg="#2C3E50")
        search_frame.pack(pady=10)

        tk.Label(search_frame, text="İçerik Ara:", font=("Arial", 12), fg="#ECF0F1", bg="#2C3E50").pack(side="left", padx=5)
        search_entry = tk.Entry(search_frame, font=("Arial", 12), bd=2, relief="solid")
        search_entry.pack(side="left", padx=5)

        search_button = tk.Button(search_frame, text="Ara", command=lambda: self.search_content(search_entry.get()), bg="#2980b9", fg="#fff", font=("Arial", 12), relief="solid")
        search_button.pack(side="left", padx=5)

        notebook = ttk.Notebook(self)
        notebook.pack(expand=True, fill="both", padx=10, pady=10)

        for category in categories:
            frame = tk.Frame(notebook, bg="#34495e")
            notebook.add(frame, text=category)

            listbox = tk.Listbox(frame, bg="#95a5a6", fg="#2c3e50", font=("Arial", 12), selectmode="single")
            listbox.pack(side="left", fill="both", expand=True, padx=10, pady=10)
            self.populate_listbox(listbox, category)

            scrollbar = tk.Scrollbar(frame, command=listbox.yview)
            scrollbar.pack(side="right", fill="y")
            listbox.config(yscrollcommand=scrollbar.set)

            button_frame = tk.Frame(frame, bg="#34495e")
            button_frame.pack(pady=5)

            tk.Button(button_frame, text="İçerik Ekle", command=lambda c=category, lb=listbox: self.add_content(c, lb), bg="#2980b9", fg="#fff", font=("Arial", 12), relief="solid").pack(side="left", padx=5)
            tk.Button(button_frame, text="İçerik Sil", command=lambda c=category, lb=listbox: self.remove_content(c, lb), bg="#e74c3c", fg="#fff", font=("Arial", 12), relief="solid").pack(side="left", padx=5)
            tk.Button(button_frame, text="Puanla", command=lambda c=category, lb=listbox: self.rate_content(c, lb), bg="#f39c12", fg="#fff", font=("Arial", 12), relief="solid").pack(side="left", padx=5)
            tk.Button(button_frame, text="Puanla Göre Sıralama", command=lambda c=category, lb=listbox: self.sort_by_rating(c, lb), bg="#16a085", fg="#fff", font=("Arial", 12), relief="solid").pack(side="left", padx=5)

        logout_button = tk.Button(self, text="Çıkış Yap", command=self.login_screen, bg="#e74c3c", fg="#fff", font=("Arial", 14), relief="solid", width=20, height=2)
        logout_button.pack(pady=20)

    def populate_listbox(self, listbox, category):
        listbox.delete(0, tk.END)
        for content in current_user.watchlists[category]:
            listbox.insert(tk.END, str(content))

    def add_content(self, category, listbox):
        content_titles = [c.title for c in sample_contents]
        selected = simpledialog.askstring("İçerik Seç", f"Aşağıdaki içeriklerden birini yaz:\n{', '.join(content_titles)}")
        for content in sample_contents:
            if content.title.lower() == selected.lower():
                current_user.watchlists[category].append(content)
                self.populate_listbox(listbox, category)
                return
        messagebox.showerror("Bulunamadı", "İçerik bulunamadı.")

    def remove_content(self, category, listbox):
        selected_index = listbox.curselection()
        if selected_index:
            del current_user.watchlists[category][selected_index[0]]
            self.populate_listbox(listbox, category)
        else:
            messagebox.showinfo("Seçim Yok", "Silmek için bir içerik seçin.")

    def random_content(self):
        random_content = random.choice(sample_contents)
        messagebox.showinfo("Rastgele İçerik", f"Bugün izlemek için önerilen içerik:\n{random_content.title}\n\n{random_content.description}")

    def search_content(self, query):
        filtered = [content for content in sample_contents if query.lower() in content.title.lower()]
        if filtered:
            self.show_filtered_contents(filtered)
        else:
            messagebox.showinfo("Arama Sonucu", "Hiçbir içerik bulunamadı.")

    def show_filtered_contents(self, contents):
        messagebox.showinfo("Arama Sonuçları", "\n".join([str(c) for c in contents]))

    def rate_content(self, category, listbox):
        selected_index = listbox.curselection()
        if selected_index:
            selected_content = current_user.watchlists[category][selected_index[0]]
            rating = simpledialog.askinteger("Puanla", f"{selected_content.title} içeriğine bir puan verin (1-5):", minvalue=1, maxvalue=5)
            if rating:
                selected_content.set_rating(rating)
                self.populate_listbox(listbox, category)
        else:
            messagebox.showinfo("Seçim Yok", "Puanlamak için bir içerik seçin.")

    def sort_by_rating(self, category, listbox):
        
        current_user.watchlists[category].sort(key=lambda x: x.rating, reverse=True)
        self.populate_listbox(listbox, category)

if __name__ == "__main__":
    app = WatchApp()
    app.mainloop()
