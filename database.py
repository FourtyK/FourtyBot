import sqlite3

class DataBase:
    def __init__(self):
        self.con = sqlite3.connect("FourtyK.db") # создание базы данных
        self.cur = self.con.cursor() # подключение к базе данных

    "СОЗДАНИЕ БАЗЫ ОТДЕЛЬНОЙ ТАБЛИЦЫ ПРИ ПОДКЛЮЧЕНИИ К БЕСЕДЕ"
    def create_db(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS users 
                            (user_id INTEGER, discrim TEXT, guild_id INTEGER)""")
        self.con.commit()

    "ЗАНЕСЕНИЕ ИНФОРМАЦИИ О ЮЗЕРЕ"
    def add_user(self, usr, dscrm, gld):
        list_to_add = [usr, dscrm, gld]
        self.cur.execute("INSERT INTO users VALUES(?, ?, ?)", list_to_add)
        self.cur.execute("INSERT INTO duels (user_id) VALUES (?)", [usr])
        self.con.commit()

    "УДАЛЕНИЕ ЮЗЕРА ИЗ БАЗЫ ДАННЫХ"
    def delete_user(self, user_id, guild_id):
        self.cur.execute("DELETE FROM users WHERE user_id LIKE ? AND guild_id = ?", [user_id, guild_id])
        self.con.commit()

    "ЗАПИСЬ ИНФОРМАЦИИ В БАЗУ ДАННЫХ"
    def insert_duel_info(self, plr1, plr2, duel_result):
        if duel_result == '00':
            list_to_add = [plr1, plr2]
            self.cur.execute("""UPDATE duels SET draws = draws + 1
            WHERE user_id = ? AND user_id = ?""", list_to_add)
            self.con.commit()

        elif duel_result == '01':
            self.cur.execute("""UPDATE duels SET wins = wins + 1
            WHERE user_id = ?""", [plr2])

            self.cur.execute("""UPDATE duels SET loses = loses + 1
            WHERE user_id = ?""", [plr1])
            self.con.commit()

        elif duel_result == '10':
            self.cur.execute("""UPDATE duels SET wins = wins + 1
            WHERE user_id = ?""", [plr1])

            self.cur.execute("""UPDATE duels SET loses = loses + 1
            WHERE user_id = ?""", [plr2])
            self.con.commit()

    "ПОЛУЧЕНИЕ СТАТИСТИКИ ИГРОКА ИЗ БАЗЫ ДАННЫХ"
    def get_duel_info(self, user_id):
        res = (self.cur.execute("SELECT * FROM duels WHERE user_id LIKE ?", [user_id])).fetchall()[0][1:6]
        return res