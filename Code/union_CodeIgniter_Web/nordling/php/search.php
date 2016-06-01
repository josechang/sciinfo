<?php   
   $conn = mysql_connect('localhost','z7724581','624001479') ;   
           mysql_select_db('z7724581_database'); 
  
    // $query=mysql_query("SELECT * FROM SRR970490 WHERE COL2 like '" . $_GET['term'] . "%'");
  
    $sql=("SELECT COL2 FROM gd_range5 WHERE COL2 like '" . $_GET['term'] . "%' order by length(COL2)");
    // echo $sql;
    $result = mysql_query($sql,$conn);
    
     //預設的變數名稱是term  
    
    while($row=mysql_fetch_array($result)){  
        $name[] = $row['COL2'];    
    }  
    $name1=array_values(array_unique($name));

    mysql_close();  
     
    echo json_encode($name1); //輸出的格式必須是json  
?>  