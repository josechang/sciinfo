
<?php
   
           
   if(isset($_POST['get_id']))
   {

    $conn = mysql_connect('localhost','z7724581','624001479') ;   
           mysql_select_db('z7724581_database'); 
  
    $p=$_POST['get_option'];
    $id= $_POST['get_id'];
    $sql=("SELECT * FROM SRR970490 WHERE COL2 = '$id'");
    $result = mysql_query($sql,$conn);
    $result1 = mysql_query($sql,$conn);
            if(!empty(mysql_fetch_array($result))){
             ?><table> 
                  <tr>
                      <td style="background:#F6FDFE;padding:0;border:0px solid #000000;"><input type="checkbox" name="<? echo 'select'.$_POST['get_option'];?>">Select All 
                      </td>
                  </tr><?
             }else{
              echo "無資料";
             }

             $i=0;
             $j=0;
             ?>

             
             <?
             while($row=mysql_fetch_array($result1))
             {  
                $j++;
                $row['COL1']=str_replace( ">" , "" , $row['COL1']);

                if($j==1){  
                ?><tr><td style="background:#F6FDFE;padding:0;border:0px solid #000000;"><input type="checkbox"  name="<? echo $_POST['get_option'].'_ck[]';?>" value="<? echo $row['COL1']; ?>"><? echo $row['COL1']."</td>";
                }elseif($j==2){  
                ?><td style="background:#F6FDFE;padding:0;border:0px solid #000000;"><input type="checkbox"  name="<? echo $_POST['get_option'].'_ck[]';?>" value="<? echo $row['COL1']; ?>"><? echo $row['COL1']."</td>";
                }else{$j=0;?>
                      

                      <td style="background:#F6FDFE;padding:0;border:0px solid #000000;"><input type="checkbox"  name="<? echo $_POST['get_option'].'_ck[]';?>" value="<? echo $row['COL1']; ?>"><? echo $row['COL1']."</td><tr>";
               }
                $i++;
             }
   
     
   }

?>