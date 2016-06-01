<?php 
class get_gene extends CI_Model{

      public function get($data){             

            $conn = mysql_connect('localhost','z7724581','624001479') ;   
                    mysql_select_db('z7724581_database'); 
  
            $sql=("SELECT COL2 FROM get_range5 WHERE COL2 like '" . $_GET['term'] . "%' order by length(COL2)");
            $result = mysql_query($sql,$conn);
    
            while($row=mysql_fetch_array($result)){ 

                  $name[] = $row['COL2'];    
            }  
            $name=array_values(array_unique($name));

            mysql_close();  
     
            echo json_encode($name); //輸出的格式必須是json  
      }
}
?>  