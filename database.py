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
    

    def record_match(self, winner, loser):
        self._change_duel_info_variable(winner, 'wins')
        self._change_duel_info_variable(loser, 'loses')
        self._commit_changes()

    
    def record_draw_match(self, player1, player2):
        self._change_duel_info_variable(player1, 'draws')
        self._change_duel_info_variable(player2, 'draws')
        self._commit_changes()


    "ПОЛУЧЕНИЕ СТАТИСТИКИ ИГРОКА ИЗ БАЗЫ ДАННЫХ"
    def get_duel_info(self, user_id):
        return (self.cur.execute("SELECT * FROM duels WHERE user_id LIKE ?", [user_id])).fetchall()[0][1:6]


    def _change_duel_info_variable(self, user_id : int, variable : str, delta : int = 1):
        self.cur.execute(f"""UPDATE duels SET {variable} = {variable} + {delta}
        WHERE user_id = ?""", [user_id])


    def _commit_changes(self):
        self.con.commit()