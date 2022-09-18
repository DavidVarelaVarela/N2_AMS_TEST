# CONEXION A BD 

import pyodbc 
import datetime

server = 'DESKTOP-7B98MI7\\N2_TEST' 
database = 'N2_AMS' 
username = 'sa' 
password = 'local' 

def create_connetion():
    try:
        conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password+';TrustServerCertificate=YES;Encrypt=yes')

        print("CONEXION EXITOSA")

        return conn
    except Exception as error:
        print("VUELVE A INTENTARLO", error)
   
def update_costo(conn, newCosto, initDate, endDate):
  sql = "UPDATE Libros SET Costo = ? WHERE FechaEdicion >= ? and FechaEdicion <= ?"
  cur = conn.cursor()
  r = cur.execute(sql, (newCosto, initDate, endDate))
  print (r.rowcount)
  cur.close()
  
def save_historico_backup(conn, new_costo, init_date, end_date):
  today = datetime.date.today()
  sql = """INSERT INTO HistoricoCostos (LibroID, CostoSustituido, CostoPesetas, FechaCambio)
          SELECT LibroID, %s, Costo * 166, '%s'
          FROM Libros
          WHERE Costo > 3
          AND  FechaEdicion >= '%s' AND FechaEdicion <= '%s'
      """ % (new_costo, today, init_date, end_date)
  cur = conn.cursor()
  r = cur.execute(sql)
  print(r.rowcount) 
  cur.close()
  
def main():
     conn = create_connetion()
     new_costo = 21 
     init_date = "2021-09-01" 
     end_date = "2022-09-01"
     save_historico_backup(conn, new_costo, init_date, end_date)
     update_costo(conn, new_costo, init_date, end_date)

     conn.commit()
     conn.close()
     
if __name__ == "__main__":
   main()
