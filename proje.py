from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QTimeEdit, QListWidgetItem, QMenu
from PyQt5.QtCore import QDate, QTime, Qt , QTimer 
import sys
from login import Ui_MainWindow as LoginWindow
from kayıt import Ui_MainWindow as RegisterWindow
from anaekran import Ui_MainWindow as MainAppWindow
from hata import Ui_MainWindow as ErrorWindow
from alandoldurma import Ui_MainWindow as AlanDoldurmaWindow
from alınmışkullanıcıadı import Ui_MainWindow as AlinmisKAWindow
from ekleme import Ui_Dialog as EklemeDialog
from eklemenot import Ui_Dialog as EklemeNotDialog
from ödemehatırlat import Ui_MainWindow as OdeHatWindow
from görevhatırlat import Ui_MainWindow as GorHatWindow
from kayıtbaşarılı import Ui_MainWindow as KayıtBaşarılıWindow
from pymongo import MongoClient

# MongoDB bağlantısı
client = MongoClient("mongodb://localhost:27017/")  
db = client["task_tracker"]
users_collection = db["users"]

# Giriş ekranı╣
class LoginScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = LoginWindow()
        self.ui.setupUi(self)

        self.ui.loginBut.clicked.connect(self.go_to_main_app)
        self.ui.registerBut.clicked.connect(self.go_to_register)

    def go_to_main_app(self):
        username = self.ui.userNameLE.text()
        password = self.ui.passwordLE.text()

        user = users_collection.find_one({"username": username, "password": password})

        if user:
            selected_date = QDate.currentDate()
            self.main_app = MainAppScreen(username, selected_date)
            self.main_app.show()
            self.close()
        else:
            self.show_error_screen() 

    def show_error_screen(self):
        self.error_screen = ErrorScreen()
        self.error_screen.show()

    def go_to_register(self):
        self.register_screen = RegisterScreen()
        self.register_screen.show()
        self.close()

# Hata ekranı
class ErrorScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ErrorWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.close)

class HatırlatmaOdeme(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = OdeHatWindow()
        self.ui.setupUi(self)
        self.sound()
        self.ui.pushButton.clicked.connect(self.close)
    def sound(self):
        QApplication.beep()

class HatırlatmaGorev(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = GorHatWindow()
        self.ui.setupUi(self)
        self.sound()
        self.ui.pushButton.clicked.connect(self.close)
    def sound(self):
        QApplication.beep()

# Kayıt ekranı
class RegisterScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = RegisterWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.register_user)

    def register_user(self):
        username = self.ui.userNamelbl_2.text()
        password = self.ui.passwordlbl_2.text()
        mail = self.ui.maillbl_2.text()

        if not username or not password or not mail:
            self.show_alan_doldurma()
            return

        if users_collection.find_one({"username": username}):
            self.show_alinmis_kullanici_adi()
            return

        users_collection.insert_one({"username": username, "password": password, "mail": mail})
        self.close()
        self.show_başarılı_kayıt()
        

    def show_başarılı_kayıt(self):
        self.başarılı_kayıt = KayıtBaşarılı()
        self.başarılı_kayıt.show()

    def show_alan_doldurma(self):
        self.alan_doldurma = AlanDoldurma()
        self.alan_doldurma.show()

    def show_alinmis_kullanici_adi(self):
        self.alinmis_kullanici_adi = AlinmisKA()
        self.alinmis_kullanici_adi.show()

# Alan doldurma ekranı
class AlanDoldurma(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = AlanDoldurmaWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.close)

class KayıtBaşarılı(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = KayıtBaşarılıWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.go_to_login)
        

    def go_to_login(self):
        self.login_screen = LoginScreen()
        self.login_screen.show()
        self.close()

# Alınmış kullanıcı adı ekranı
class AlinmisKA(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = AlinmisKAWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.close)

class AddScreenNote(QDialog):
    def __init__(self, username, selected_date):
        super().__init__()
        self.ui = EklemeNotDialog()
        self.ui.setupUi(self)

        self.username = username
        self.selected_date = selected_date

        self.ui.pushButton.clicked.connect(self.save_to_database)

    def save_to_database(self):
        ad = self.ui.lineEdit.text()
        açıklama = self.ui.lineEdit_2.text()
        selected_date = self.selected_date.toString("yyyy-MM-dd")

        users_collection.update_one(
                {"username": self.username},
                {"$push": {
                    "notes": {
                        "ad": ad,
                        "açıklama": açıklama,
                        "selected_date": selected_date,
                    }
                }}
            )
        self.close()

# Ekleme ekranı
class AddScreen(QDialog):
    def __init__(self, username, selected_date, is_payment=False):
        super().__init__()
        self.ui = EklemeDialog()
        self.ui.setupUi(self)

        self.username = username
        self.selected_date = selected_date
        self.is_payment = is_payment  # Ödeme olup olmadığını kontrol et
        self.ui.timeEdit.setTime(QTime.currentTime())

        self.ui.pushButton.clicked.connect(self.save_to_database)

    def save_to_database(self):
        ad = self.ui.lineEdit.text()
        açıklama = self.ui.lineEdit_2.text()
        hatırlatmaSaati = self.ui.timeEdit.time().toString("HH:mm")
        selected_date = self.selected_date.toString("yyyy-MM-dd")

        # Eğer ödeme ekleniyorsa
        if self.is_payment:
            users_collection.update_one(
                {"username": self.username},
                {"$push": {
                    "payments": {
                        "ad": ad,
                        "açıklama": açıklama,
                        "hatırlatmaSaati": hatırlatmaSaati,
                        "selected_date": selected_date,
                        "checked": False  # Yeni ödemede varsayılan olarak checked: False
                    }
                }}
            )
        
        else:  # Görev ekleniyorsa
            users_collection.update_one(
                {"username": self.username},
                {"$push": {
                    "tasks": {
                        "ad": ad,
                        "açıklama": açıklama,
                        "hatırlatmaSaati": hatırlatmaSaati,
                        "selected_date": selected_date,
                        "checked": False
                    }
                }}
            )
    
        self.close()
    
class MainAppScreen(QMainWindow):
    def __init__(self, username, selected_date, parent=None):
        super().__init__(parent)
        self.ui = MainAppWindow()
        self.ui.setupUi(self)

        self.username = username
        self.selected_date = selected_date
        self.update_date_label()
        
        # Sinyalleri bağla
        self.ui.calenderlbl.selectionChanged.connect(self.update_date_label)
        self.ui.taskBut.clicked.connect(self.add_task)
        self.ui.paymentBut.clicked.connect(self.add_payment)
        self.ui.noteBut.clicked.connect(self.add_note)

        # Hatırlatıcıyı başlat
        self.start_reminder_timer()

        # Listeye sağ tık menüsü ekleyelim
        self.ui.listWidget_3.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.listWidget_3.customContextMenuRequested.connect(self.show_context_menu_for_tasks)

        self.ui.listWidget_2.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.listWidget_2.customContextMenuRequested.connect(self.show_context_menu_for_payments)

        self.ui.listWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.listWidget.customContextMenuRequested.connect(self.show_context_menu_for_notes)

    def update_date_label(self):
        self.selected_date = self.ui.calenderlbl.selectedDate()
        selected_date_str = self.selected_date.toString("dd/MM/yyyy")
        self.ui.datelbl.setText(f"TARİH : {selected_date_str}")
        self.load_task()
        self.load_payment()
        self.load_note()
    
    def load_task(self):
        self.ui.listWidget_3.clear()
        selected_date_str = self.selected_date.toString("yyyy-MM-dd")
        user = users_collection.find_one({"username": self.username})
        if user and "tasks" in user:
            tasks = user["tasks"]
            for task in tasks:
                if task.get("selected_date") == selected_date_str:
                    task_text = f"{task['ad']} - {task['hatırlatmaSaati']} - {task['açıklama']}"

                    list_item = QListWidgetItem(task_text)
                    list_item.setFlags(list_item.flags() | Qt.ItemIsUserCheckable)
                    list_item.setCheckState(Qt.Checked if task.get("checked") else Qt.Unchecked)

                # CheckBox durumu değiştiğinde sinyali dinle
                    list_item.setData(Qt.UserRole, task["ad"])
                    self.ui.listWidget_3.addItem(list_item)

    # Checkbox değişimini dinle
        self.ui.listWidget_3.itemChanged.connect(self.update_task_check_status)

    def update_task_check_status(self, item):
        task_name = item.data(Qt.UserRole)
        is_checked = item.checkState() == Qt.Checked

        users_collection.update_one(
        {"username": self.username, "tasks.ad": task_name},
        {"$set": {"tasks.$.checked": is_checked}}
    )

    def load_payment(self):
        self.ui.listWidget_2.clear()
        selected_date_str = self.selected_date.toString("yyyy-MM-dd")
        user = users_collection.find_one({"username": self.username})

        if user and "payments" in user:
            payments = user["payments"]
            for payment in payments:
                if payment.get("selected_date") == selected_date_str:
                    payment_text = f"{payment['ad']} - {payment['hatırlatmaSaati']} - {payment['açıklama']}"

                    list_item = QListWidgetItem(payment_text)
                    list_item.setFlags(list_item.flags() | Qt.ItemIsUserCheckable)
                    list_item.setCheckState(Qt.Checked if payment.get("checked") else Qt.Unchecked)

                # CheckBox durumu değiştiğinde sinyali dinle
                    list_item.setData(Qt.UserRole, payment["ad"])
                    self.ui.listWidget_2.addItem(list_item)

    # Checkbox değişimini dinle
        self.ui.listWidget_2.itemChanged.connect(self.update_payment_check_status)

    def update_payment_check_status(self, item):
        payment_name = item.data(Qt.UserRole)
        is_checked = item.checkState() == Qt.Checked

        users_collection.update_one(
        {"username": self.username, "payments.ad": payment_name},
        {"$set": {"payments.$.checked": is_checked}}
    )

    def load_note(self):
        self.ui.listWidget.clear()
        selected_date_str = self.selected_date.toString("yyyy-MM-dd")
        user = users_collection.find_one({"username": self.username})

        if user and "notes" in user:
            notes = user["notes"]
            for note in notes:
                if note.get("selected_date") == selected_date_str:
                    note_text = f" • {note['ad']} - {note['açıklama']}"  # Madde işareti ekledik
                    list_item = QListWidgetItem(note_text)
                    self.ui.listWidget.addItem(list_item)
    

    def start_reminder_timer(self):
        self.reminder_timer = QTimer(self)
        self.reminder_timer.timeout.connect(self.check_reminders)
        self.reminder_timer.start(60000)  

    def check_reminders(self):
        current_time = QTime.currentTime().toString("HH:mm")
        selected_date_str = QDate.currentDate().toString("yyyy-MM-dd")
        user = users_collection.find_one({"username": self.username})

        if user:
            # Görev hatırlatıcıları
            for task in user.get("tasks", []):
                if task.get("selected_date") == selected_date_str and task.get("hatırlatmaSaati") == current_time:
                    self.show_task_reminder(task)
                    

            # Ödeme hatırlatıcıları
            for payment in user.get("payments", []):
                if payment.get("selected_date") == selected_date_str and payment.get("hatırlatmaSaati") == current_time:
                    self.show_payment_reminder(payment)

    def show_task_reminder(self,task):
        self.gorev_hatırlatıcı = HatırlatmaGorev()
        self.gorev_hatırlatıcı.ui.label_3.setText(task['ad'])
        self.gorev_hatırlatıcı.ui.label_5.setText(task['açıklama'])
        self.gorev_hatırlatıcı.show()

    def show_payment_reminder(self,task):
        self.gorev_hatırlatıcı = HatırlatmaOdeme()
        self.gorev_hatırlatıcı.ui.label_3.setText(task['ad'])
        self.gorev_hatırlatıcı.ui.label_5.setText(task['açıklama'])
        self.gorev_hatırlatıcı.show()

    def show_context_menu_for_tasks(self, pos):
        item = self.ui.listWidget_3.itemAt(pos)
        if item is not None:
            context_menu = QMenu(self)
            delete_action = context_menu.addAction("Sil")
            delete_action.triggered.connect(lambda: self.delete_task(item.text()))
            context_menu.exec_(self.ui.listWidget_3.mapToGlobal(pos))

    def show_context_menu_for_payments(self, pos):
        item = self.ui.listWidget_2.itemAt(pos)
        if item is not None:
            context_menu = QMenu(self)
            delete_action = context_menu.addAction("Sil")
            delete_action.triggered.connect(lambda: self.delete_payment(item.text()))
            context_menu.exec_(self.ui.listWidget_2.mapToGlobal(pos))

    def show_context_menu_for_notes(self, pos):
        item = self.ui.listWidget.itemAt(pos)
        if item is not None:
            context_menu = QMenu(self)
            delete_action = context_menu.addAction("Sil")
            delete_action.triggered.connect(lambda: self.delete_note(item.text()))
            context_menu.exec_(self.ui.listWidget.mapToGlobal(pos))

    def delete_task(self, task_text):
        task_name = task_text.split(" - ")[0]
        user = users_collection.find_one({"username": self.username})

        if user and "tasks" in user:
            tasks = user["tasks"]
            updated_tasks = [task for task in tasks if task["ad"] != task_name]

            users_collection.update_one(
                {"username": self.username},
                {"$set": {"tasks": updated_tasks}}
            )

            item = self.ui.listWidget_3.findItems(task_text, Qt.MatchExactly)
            if item:
                self.ui.listWidget_3.takeItem(self.ui.listWidget_3.row(item[0]))

    def delete_payment(self, payment_text):
        payment_name = payment_text.split(" - ")[0]
        user = users_collection.find_one({"username": self.username})

        if user and "payments" in user:
            payments = user["payments"]
            updated_payments = [payment for payment in payments if payment["ad"] != payment_name]

            users_collection.update_one(
                {"username": self.username},
                {"$set": {"payments": updated_payments}}
            )

            item = self.ui.listWidget_2.findItems(payment_text, Qt.MatchExactly)
            if item:
                self.ui.listWidget_2.takeItem(self.ui.listWidget_2.row(item[0]))

    def delete_note(self, note_text):
        cleaned_note_text = note_text.replace("•","").strip()
        note_name = cleaned_note_text.split(" - ")[0]
        user = users_collection.find_one({"username": self.username})

        if user and "notes" in user:
            notes = user["notes"]
            updated_notes = [note for note in notes if note["ad"] != note_name]

            users_collection.update_one(
                {"username": self.username},
                {"$set": {"notes": updated_notes}}
            )

            matching_items = self.ui.listWidget.findItems(note_text, Qt.MatchExactly)
            if matching_items:
                for item in matching_items:
                    self.ui.listWidget.takeItem(self.ui.listWidget.row(item))
    
    

    def add_task(self):
        dialog = AddScreen(username=self.username, selected_date=self.selected_date, is_payment=False)
        dialog.exec_()
        self.load_task()

    def add_payment(self):
        dialog = AddScreen(username=self.username, selected_date=self.selected_date, is_payment=True)
        dialog.exec_()
        self.load_payment()

    def add_note(self):
        dialog = AddScreenNote(username=self.username, selected_date=self.selected_date)
        dialog.exec_()
        self.load_note()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_screen = LoginScreen()
    login_screen.show()
    sys.exit(app.exec_())
    