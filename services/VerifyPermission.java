package er2019n3;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
import java.sql.ResultSet;

 
public class VerifyPermission
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
    
    public boolean checkPer(String perType, String empType)
    {
        boolean flag=true;
        String sql;
        sql = "SELECT Name, "+empType+" FROM permission WHERE Name='"+perType+"'"; 
        try (Connection conn = this.connect();
             Statement stmt  = conn.createStatement(); 
             ResultSet rs = stmt.executeQuery(sql)){
               System.out.println(rs.getString(empType.toString()));
            if(rs.isClosed()){
                 flag=false;
                 
            }
             else
            {
                System.out.println(rs.getString(empType.toString()));
                if(rs.getString(empType.toString())=="y")
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
        VerifyPermission app = new VerifyPermission();
        String command = args[0];
        String user = args[1];
        if(!(app.checkPer(command,user)))
        {
            System.out.println("permissiom denied");
        }
        else
            System.out.println("permissiom granted");
    }
 
}