package er2019;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
import java.sql.ResultSet;

 
public class SearchEmployee
{
    private Connection connect() 
    {
        // SQLite connection string
        String url = "jdbc:sqlite:C:/sqlite3/db/chinook.db";
        Connection conn = null;
        try {
            conn = DriverManager.getConnection(url);
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
        return conn;
    }
    
    public boolean checkEmp(String id,String Etype)
    {
        boolean flag=true;
        String sql;
        sql = "SELECT ID FROM employee WHERE ID='"+id+"' and type='"+Etype+"'"; 
        try (Connection conn = this.connect();
             Statement stmt  = conn.createStatement(); 
             ResultSet rs = stmt.executeQuery(sql))
        {
             if(rs.isClosed())
                 flag=false;
             else{
                if(rs.getString("ID")==id)
                flag=true;
             }

            
        } 
        catch (SQLException e) 
        {
            System.out.println(e.getMessage());
        }
        return flag;
    }
    
    public static void main(String[] args) {
        SearchEmployee app = new SearchEmployee();
        String id = args[0];
        String Etype=args[1];
        if((app.checkEmp(id,Etype)))
            System.out.println("emp exist");
        else 
            System.out.println("emp doesnt exist");
    }
 
}