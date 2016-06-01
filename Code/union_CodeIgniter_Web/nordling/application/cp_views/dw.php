<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<link rel="stylesheet" href="http://140.116.215.238/~z7724581/GD/css/z1.css" />  

<style type="text/css">
        
        table {
              margin: 0 auto;
              width:  1520px;

        }
        th {
            background: #E85B5B;
        }
        td{
            background: #F5F5F8;
        }

        #show_sql th{
           background: #989BE6;   

        }
        #show_id th{
           background: #989BE6;      
        }

        #range{
              margin-left: 71%;
        }

        #goToTop {
                            position: fixed;
                            width: 100px;
                            height: 30px;
                            background: #FCEFA1;
                            text-align: none;
                            border: 2px black solid;
                            bottom: 60px;
                            right: 2%;
                         }
        #goback {
                            position: fixed;
                            width: 100px;
                            height: 30px;
                            background: #FCEFA1;
                            text-align: none;
                            border: 2px black solid;
                            bottom: 10px;
                            right: 2%;
                         }




</style>

</head>

<body>
      <table style="font-size: 20px;">
          
          <tr>

             <th>Gene</th>
             <th>Isoform</th>
             <th>Ribo_H_Rep1_CPM</th>
             <th>Ribo_H_Rep2_CPM</th>
             <th>Ribo_N_Rep1_CPM</th>
             <th>Ribo_N_Rep2_CPM</th>
             <th>Fold_change</th>
             <th>P_value</th>
          </tr> 


             <?php
                   // echo "<pre>";
                   // print_r($data);
                   // print_r($express);

                   if(!empty($express[0]['COL1'])){
                    $a=count($express)-1;
                   echo "<td rowspan=".$a.">".$express[0]['COL1']."</td>"; 
                   for($i=0;$i<count($express)-1;$i++){
                      
                      echo "<td>".$express[$i]['COL2']."</td>"; 
                      echo "<td>".round($express[$i]['COL3'],3)."</td>"; 
                      echo "<td>".round($express[$i]['COL4'],3)."</td>"; 
                      echo "<td>".round($express[$i]['COL5'],3)."</td>"; 
                      echo "<td>".round($express[$i]['COL6'],3)."</td>"; 
                      echo "<td>".round($express[$i]['COL7'],3)."</td>"; 
                      echo "<td>".round($express[$i]['COL9'],3)."</td></tr>"; 
                   }
                 }

             ?>
        </table><br><br><br>
        <?php
        
        for($i=0;$i<count($data);$i++){
          $number =count($data[$i]['data']);
          ?>
          <table>
                 <tr>
                     <th colspan="3"><?php echo $data[$i]['sql'] ;?></th>
                 </tr>
                 <tr>
                     <th>Gene</th>
                     <th>ID</th>
                     <th>Img</th>
                 </tr>
                 <?php 
                    for($j=0;$j<count($data[$i]['data']);$j++){
                      echo "<tr><td>".$data[$i]['data'][$j]['COL2']."</td>"; 
                      echo "<td>".$data[$i]['data'][$j]['COL1']."</td>"; 
                      
                      $jpg   = '/one'.$rand.$data[$i]['data'][$j]['COL1'].'_'.$data[$i]['data'][$j]['COL2']."_".$data[$i]['sql'].'.jpg';
                      ?>
                       <td><a><img src="<?php  echo base_url('gd_img').$jpg ;?>"></a></td></tr>
                        


                      <?php
                    
                    }
                 ?>

            





          </table>




        <?php }?>

   <div id="msg2" style="display: none"></div>


</body>
</html>