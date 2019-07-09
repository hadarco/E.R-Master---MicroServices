using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.SQLite;

namespace ER2019NEW
{
    class SearchPatient
    {
        static void Main(string[] args)
        {
            SearchPatient n = new SearchPatient();
            if (n.SearchPatientID(args[0]))
            {
                Console.WriteLine("Patient exists");
            }
            else
                Console.WriteLine("Patient doesn't exists");

        }


        private SQLiteConnection sqlite;
        public SearchPatient()
        {
            sqlite = new SQLiteConnection("Data Source=C:\\sqlite3\\db\\chinook.db");
        }

        public bool SearchPatientID(string ID)
        {
            string q = "Select ID from Patient where ID='" + ID + "'";
            try
            {
                sqlite.Open();
                SQLiteCommand cmd = new SQLiteCommand(sqlite);
                cmd.CommandText = q;
                SQLiteDataReader rd = cmd.ExecuteReader();
                if (rd.HasRows)
                {
                    Console.WriteLine("Patient exists");
                    sqlite.Close();
                    return true;
                }
            }
            catch (SQLiteException ex)
            {
                Console.WriteLine(ex);
            }
            sqlite.Close();
            Console.WriteLine("Patient doesn't exists");
            return false;
        }
    }

}
