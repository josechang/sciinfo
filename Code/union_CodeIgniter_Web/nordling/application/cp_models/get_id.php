<?php 

class get_id extends CI_Model{

      public function get($data){             

             $conn = mysqli_connect('localhost','z7724581','624001479','z7724581_database') ;   
  
             $p=$_POST['get_option'];
             $id= $_POST['get_id'];

             $sql=("SELECT * FROM gd_range5 WHERE COL2 = '$id'");
             $result = mysqli_query($conn,$sql) or die("Error: ".mysqli_error($conn));
             $result1 = mysqli_query($conn,$sql) or die("Error: ".mysqli_error($conn));
             if (!empty(mysqli_fetch_array($result)['COL1'])){?>
         
            <div style="width:450px; height:70px; overflow-y:auto;border: 1px solid black;margin-top:5px;font-size: 12px; ">
             <table style="width:400px;">
                    <tr>
                        <td style="background:#FCFDDC;padding:0;border:0px solid #000000;"><input type="checkbox" name="<?php  echo 'select'.$_POST['get_option'];?>"> Select All</td>

                    </tr>

                    <?php  }else{

                            echo "無資料"."<table>";
                    }
             $j=0;
             $co=0;
             while ($row = mysqli_fetch_array($result1)){
             
                   $j++;
                   $co++;

                   if($j==1){ ?>

                       <tr>
                           <td style="background:#FCFDDC;padding:0;border:0px solid #000000;"><input type="checkbox"  name="<?php  echo $_POST['get_option'].'_ck[]';?>" value="<?php  echo $row['COL1']; ?>">

                           <?php  echo $row['COL1']."</td>";
                   }elseif($j==2){ ?>

                           <td style="background:#FCFDDC;padding:0;border:0px solid #000000;"><input type="checkbox"  name="<?php  echo $_POST['get_option'].'_ck[]';?>" value="<?php  echo $row['COL1']; ?>">

                           <?php  echo $row['COL1']."</td>";
                   }else{
                           $j=0; ?>

                           <td style="background:#FCFDDC;padding:0;border:0px solid #000000;"><input type="checkbox"  name="<?php  echo $_POST['get_option'].'_ck[]';?>" value="<?php  echo $row['COL1']; ?>">

                           <?php  echo $row['COL1']."</td><tr>";
                   }
             }

             $coun = (9 -$co)/3 ;  //預設每排三個   最多9個

             if($co%3 == 0){
                             $coun+=1;
             }

             for($i=1;$i<$coun;$i++){ ?>

               <tr> 
                    <td style="background:#FCFDDC;border: 1px solid #FCFDDC; "> &nbsp; </td>
               </tr> 
             <?php  } ?>

            </table>
</div>
            <?php 
      }
}
?>  