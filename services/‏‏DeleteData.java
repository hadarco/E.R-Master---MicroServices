package er2019n2;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
import java.sql.ResultSet;
import java.sql.PreparedStatement;


public class DeleteData {
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
    
    public void delete(String table, String id)
    {
        String sql;
        sql="DELETE FROM "+table+" WHERE ID ='"+id+"'";
        try (Connection conn = this.connect();
                PreparedStatement pstmt = conn.prepareStatement(sql)) 
        {
            pstmt.executeUpdate();
            
        } 
        catch (SQLException e) 
        {
            System.out.println(e.getMessage());
        }
    }
    
    public static void main(String[] args) {
        DeleteData app = new DeleteData();
        String table = args[0];
        String id = args[1];
        app.delete(table, id);
    }
 
}
