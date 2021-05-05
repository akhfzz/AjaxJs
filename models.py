import pymysql
import config

db = cursor = None
class Akademik:
	def OpenDB(self):
		global db, cursor
		db = pymysql.connect(
				host=config.DB_HOST,
				user=config.DB_USER,
				password=config.DB_PASSWORD,
				database=config.DB_NAME
			)
		cursor = db.cursor()

	def CloseDB(self):
		global db, cursor
		db.close()

	def SelectRDB(self, id):
		self.OpenDB()
		cursor.execute("SELECT kdprodi, nama_prodi, kdfakultas from program_studi where kaprodi='{0}'".format(id))
		data = cursor.fetchone()
		self.CloseDB()
		return data

	def SelectDB(self):
		self.OpenDB()
		cursor.execute("SELECT kdprodi, nama_prodi, kdfakultas,keterangan from program_studi")
		container = []
		for kdprodi, nama_prodi, kdfakultas, keterangan in cursor.fetchall():
			container.append((kdprodi, nama_prodi, kdfakultas, keterangan))
		self.CloseDB()
		return container