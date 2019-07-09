using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.SQLite;
using System.Data;



namespace ConsoleApp3
{
    class UpdateDetails
    {
        public static void Main(string[] args)
        {
            UpdateDetails a = new UpdateDetails();
            a.UpdateDetailsID(args[0], args[1], args[2], args[3]);
        }
        private SQLiteConnection sqlite;

        public UpdateDetails()
        {
            sqlite = new SQLiteConnection("Data Source=C:\\sqlite3\\db\\chinook.db");

        }

        public void UpdateDetailsID(string ID, string date, string what, string value)
        {
            string q = "UPDATE Patient SET " + what + " = '" + value + "' where ID='" + ID + "' and dateVisit='" + date + "'";


            try
            {

                sqlite.Open();  //Initiate connection to the db
                SQLiteCommand cmd = new SQLiteCommand(sqlite);
                cmd.CommandText = q;  //set the passed query
                cmd.ExecuteNonQuery();
            }
            catch (SQLiteException ex)
            {
                System.Console.WriteLine("THERE IS NO SOUCH CULOMN OR TABLE");
            }
            sqlite.Close();

        }

    }
}
