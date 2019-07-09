using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.SQLite;
using System.Data;

namespace ER2019NEW
{
    class ShowPatientData
    {
        static void Main(string[] args)
        {
            ShowPatientData n = new ShowPatientData();
            string id = args[0];
            Console.WriteLine(n.ShowPatientDetailsID(id));

        }


        private SQLiteConnection sqlite;
        public ShowPatientData()
        {
            sqlite = new SQLiteConnection("Data Source=C:\\sqlite3\\db\\chinook.db");
        }

        public string ShowPatientDetailsID(string ID)
        {
            string res = "";
            string q = "Select * from Patient where ID='" + ID + "'";
            try
            {
                sqlite.Open();
                SQLiteCommand cmd = new SQLiteCommand(sqlite);
                cmd.CommandText = q;
                SQLiteDataReader rd = cmd.ExecuteReader();
                if (!rd.HasRows)
                {
                    sqlite.Close();
                    return "patient doesnt exist";
                }
                DataTable table = new DataTable();
                table.Load(rd);
                foreach (DataRow row in table.Rows)
                {
                    string Pid = row["ID"].ToString();
                    string Name = row["Name"].ToString();
                    string DateVisit = row["DateVisit"].ToString();
                    string DateRelease = row["DateRelease"].ToString();
                    string Symptoms = row["symptoms"].ToString();
                    string Metrics = row["Metrics"].ToString();
                    string Diagnostic = row["Diagnostic"].ToString();
                    string Medication = row["Medication"].ToString();
                    res += Pid + " " + Name + ' ' + DateVisit + ' ' + DateRelease + ' ' + Symptoms + ' ' + Metrics + " " + Diagnostic + ' ' + Medication + '\n';
                }


            }
            catch (SQLiteException ex)
            {
                Console.WriteLine(ex);
            }
            sqlite.Close();
            return res;
        }
    }

}
