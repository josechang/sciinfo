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
                    
                   echo "<td>".$express[0]['COL1']."</td>"; 
                   
                      
                      echo "<td>".$express[0]['COL2']."</td>"; 
                      echo "<td>".round($express[0]['COL3'],3)."</td>"; 
                      echo "<td>".round($express[0]['COL4'],3)."</td>"; 
                      echo "<td>".round($express[0]['COL5'],3)."</td>"; 
                      echo "<td>".round($express[0]['COL6'],3)."</td>"; 
                      echo "<td>".round($express[0]['COL7'],3)."</td>"; 
                      echo "<td>".round($express[0]['COL9'],3)."</td></tr>"; 
                   
                 }

             ?>
        </table><br><br><br><table>
                 <tr>
                     <th colspan="2"><?php echo $express[0]['COL1']."=> ".$express[0]['COL2'] ;?></th>
                 </tr>
                 <tr>

                     <th>SQL</th>
                     <th>Img</th>
                 </tr>
        <?php
        // echo "<pre>";
        // print_r($data);
        for($i=0;$i<count($data)-2;$i++){
          $number =count($data[$i]['data']);
          ?>
          
                 <?php 
                    
                      // echo "<tr><td>".$data[$j]['sql']."</td>"; 
                      echo "<td>".$data[$i]['data'][0]['COL1']."</td>"; 
                      
                      $jpg   = '/one_id'.$rand.$data[$i]['data'][0]['COL1'].'_'.$data[$i]['data'][0]['COL2']."_".$data[$i]['sql'].'.jpg';
                      ?>
                       <td><a><img src="<?php  echo base_url('gd_img').$jpg ;?>"></a></td></tr>
                      

            

<?php }?>



          </table>




        

   <div id="msg2" style="display: none"></div>


</body>
</html>